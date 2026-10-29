# university_is_dead 🎓

[English](README.md) | [한국어](README.ko.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | **Português**

**Um conjunto de instruções e templates de notas do Obsidian para estudar as aulas da faculdade com o Claude.**
Adicione os PDFs das suas aulas e use comandos curtos como `운체 3` (capítulo 3 de Sistemas Operacionais), `다음` (próximo) ou `시험 정리본` (resumo para a prova) para receber explicações aprofundadas na ordem dos slides. O Claude também monta esqueletos de notas, resumos para a prova e livros ilustrados ELI5.

> **Nota sobre o idioma:** As instruções, os templates, os comandos e o vault de exemplo estão em coreano, e o Claude responde em coreano por padrão. Por enquanto, só a documentação e os arquivos voltados a contribuidores têm versão em inglês. Este README é uma tradução da versão em inglês; se houver divergência, vale o README em inglês.

---

## O que ele faz

| Você diz | O que acontece |
|---|---|
| `운체 3` | Mostra um mapa do capítulo 3 dividido em grupos, cada um com uma pergunta-chave, e depois explica o grupo 1 |
| `운체 3-2` / `다음` | Explica um grupo na ordem dos slides, com fórmulas, exemplos numéricos resolvidos e perguntas de autoavaliação |
| `골격 만들어줘` + PDF | Cria uma nota vazia no formato `## Seção / ### Título do Slide (coreano) / - ` |
| `정리해줘` | Completa suas notas a partir do PDF, mantendo o que você escreveu |
| `시험 정리본` | Marcas de importância ★, tabelas comparativas, exercícios com critérios de correção e perguntas e respostas sobre os pontos da prova |
| `/eli5 {nota}` | Um livro ilustrado em HTML que separa as analogias das definições da aula |
| `저장해줘` / `운체 3 전부` | Salva as explicações dos grupos como notas em `클코 설명/`, encadeadas com links `다음 →` do primeiro ao último |
| `기출 분석` + provas anteriores ou relatos de provas | Gera tabelas de questões por ano, tópicos frequentes e prioridades em `클코 정리/기출 분석.md` |
| (`증명 과목` nas exceções da disciplina) | Templates de demonstração para cada teorema, tabelas de recíprocas e condições, e simulados no formato das provas anteriores |

## Configuração em 5 minutos

1. Obtenha este repositório: **Use this template** no GitHub, ou Code → Download ZIP.
2. Usando `example-vault/` como referência, crie uma pasta para a disciplina no seu vault do Obsidian. Você pode colocá-la dentro de uma pasta do semestre; nesse caso, escreva o caminho completo na tabela de disciplinas.
   ```
   (raiz do vault)/
   ├── CLAUDE.md          ← ao usar o Claude Code (passo 4)
   ├── templates/         ← cópia da pasta templates/ deste repositório
   ├── tools/             ← cópia da pasta tools/ deste repositório
   └── {disciplina}/
       ├── 강의자료/        ← PDFs das aulas (somente leitura)
       ├── {título da aula}.md  ← notas semanais
       ├── 개념.md          ← hub de conceitos + tabela de notas semanais
       ├── 클코 정리/       ← resumos para a prova, análise de provas anteriores
       ├── 클코 설명/       ← explicações de grupos salvas
       └── 학습자료/        ← HTML ELI5
   ```
   Dê a cada PDF de aula o mesmo nome da nota correspondente (`1주차 정렬 기초.md` ↔ `강의자료/1주차 정렬 기초.pdf`) para que os links para páginas do PDF funcionem.
3. Abra o `INSTRUCTIONS.md` e preencha sua universidade, suas disciplinas e as abreviações no bloco **"📝 여기만 고치세요"** ("edite só aqui"). Escreva cada pasta de disciplina como um caminho a partir da raiz do vault (por exemplo, `딥러닝/`).
4. Passe as instruções para o Claude.
   - **Claude Projects**: cole o conteúdo em Project instructions e envie a pasta da disciplina e os arquivos de `templates/` como conhecimento do projeto.
   - **Claude Code**: faça as mesmas edições no `CLAUDE.md`, copie `CLAUDE.md`, `templates/` e `tools/` para a raiz do vault e execute o Claude Code a partir dela. O verificador de links precisa do Python 3.8 ou superior.
5. Experimente `{abreviação} 1`.

## Estrutura do repositório

| Caminho | Conteúdo |
|---|---|
| [`INSTRUCTIONS.md`](INSTRUCTIONS.md) | As instruções (para o Claude Projects) |
| [`CLAUDE.md`](CLAUDE.md) | As mesmas instruções (para o Claude Code) |
| [`templates/`](templates) | Templates vazios: esqueleto de nota, 개념.md, resumo para a prova, explicação de grupo, análise de provas anteriores, HTML ELI5 |
| [`tools/check_links.py`](tools/check_links.py) | Verificador de links do Obsidian (encontra notas, títulos e anexos que não existem) |
| [`example-vault/알고리즘/`](example-vault/알고리즘) | Um exemplo preenchido com uma disciplina fictícia de Algoritmos. Abra no Obsidian |
| [`docs/usage-examples.md`](docs/usage-examples.md) | Fluxo de conversa de cada comando |
| [`docs/FAQ.md`](docs/FAQ.md) | Perguntas frequentes |

## Princípios fundamentais

- **Os materiais da aula são a fonte da verdade.** Tudo o que não está nos slides é marcado como "교재 보충" (complemento do livro-texto).
- **Suas notas nunca são sobrescritas.** O Claude só acrescenta o que falta, com edições mínimas.
- **A ordem dos slides é mantida.** Os grupos nunca se misturam, e os slides de apêndice ganham grupos próprios.
- **As explicações nunca são rasas.** Cada conceito segue motivação → intuição → definição/fórmula → exemplo numérico → limitações.

## ⚠️ Não faça upload dos materiais das aulas

Os materiais das aulas dos seus professores, assim como as notas que transcrevem o conteúdo das aulas, são obras protegidas por direitos autorais. Se você fizer backup do seu vault no GitHub, use o [`.gitignore`](.gitignore) deste repositório e não envie o vault para um repositório público. Todos os exemplos deste repositório são aulas fictícias, escritas do zero.

## Contribuindo

Novos comandos, regras para outros tipos de disciplina e melhorias nos templates são todos bem-vindos. Leia o [`CONTRIBUTING.md`](CONTRIBUTING.md), abra uma issue com um dos templates de issue (Bug Report / Enhancement Request / Common Issue) e depois envie um PR. Todo PR é verificado automaticamente quanto à sincronia dos arquivos de instruções, aos links do vault de exemplo e ao envio de materiais de aula.

## Licença

[MIT](LICENSE)
