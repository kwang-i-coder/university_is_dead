"""Regression tests for tools/check_links.py. Run: python3 -m unittest discover tests"""
import pathlib
import subprocess
import sys
import tempfile
import unicodedata
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "tools" / "check_links.py"


class CheckLinksTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / ".obsidian").mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel: str, text: str = "") -> None:
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def run_check(self, target: str = "."):
        r = subprocess.run([sys.executable, str(SCRIPT), target], cwd=self.root,
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def test_ok_links(self):
        self.write("3-1/DL/개념.md", "# 개념\n## 정의\n")
        self.write("3-1/DL/n.md", "[[3-1/DL/개념|허브]] [[3-1/DL/개념#정의]] [[#본문]]\n## 본문\n")
        self.assertEqual(self.run_check("3-1/DL")[0], 0)

    def test_missing_note_and_heading(self):
        self.write("a.md", "[[없는 노트]] [[a#없는 헤딩]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("missing note", out)
        self.assertIn("missing heading", out)

    def test_nfd_filename_matches_nfc_link(self):
        self.write(unicodedata.normalize("NFD", "정렬 기초.md"), "## 버블 정렬\n")
        self.write("a.md", "[[정렬 기초#버블 정렬]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 0, out)

    def test_case_insensitive(self):
        self.write("DL 3.md", "## Loss\n")
        self.write("a.md", "[[dl 3#Loss]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 0, out)

    def test_ambiguous_name_warns_and_checks_all_candidates(self):
        self.write("A/개념.md", "## 알파\n")
        self.write("B/개념.md", "## 베타\n")
        self.write("a.md", "[[개념#베타]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 0, out)
        self.assertIn("ambiguous", out)

    def test_ambiguous_name_missing_heading_is_error(self):
        self.write("A/개념.md", "## 알파\n")
        self.write("B/개념.md", "## 베타\n")
        self.write("a.md", "[[개념#감마]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("missing heading", out)

    def test_inline_code_in_heading_link(self):
        self.write("코드.md", "## `sort()` 함수\n")
        self.write("a.md", "[[코드#`sort()` 함수]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 0, out)

    def test_links_inside_code_are_ignored(self):
        self.write("a.md", "`[[없음1]]`\n```\n[[없음2]]\n## 가짜\n```\n")
        self.assertEqual(self.run_check()[0], 0)

    def test_heading_inside_fence_does_not_count(self):
        self.write("b.md", "```\n## 가짜\n```\n")
        self.write("a.md", "[[b#가짜]]\n")
        self.assertEqual(self.run_check()[0], 1)

    def test_canvas(self):
        self.write("보드.canvas", "{}")
        self.write("a.md", "[[보드.canvas]]\n")
        self.assertEqual(self.run_check()[0], 0)
        self.write("a.md", "[[없는보드.canvas]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("missing file", out)

    def test_missing_attachment_is_warning(self):
        self.write("a.md", "[[강의.pdf#page=2]]\n")
        code, out = self.run_check()
        self.assertEqual(code, 0)
        self.assertIn("missing attachment", out)

    def test_bad_target_exits_2(self):
        self.assertEqual(self.run_check("없는폴더")[0], 2)
        (self.root / "빈폴더").mkdir()
        self.assertEqual(self.run_check("빈폴더")[0], 2)


if __name__ == "__main__":
    unittest.main()
