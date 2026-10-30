# university_is_dead 🎓

[English](README.md) | [한국어](README.ko.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | **Español** | [Tiếng Việt](README.vi.md) | [Português](README.pt-BR.md)

**Un conjunto de instrucciones y plantillas de notas de Obsidian para estudiar las clases de la universidad con Claude.**
Agrega los PDF de tus clases y usa comandos cortos como `운체 3` (capítulo 3 de Sistemas Operativos), `다음` (siguiente) o `시험 정리본` (resumen para el examen) para obtener explicaciones detalladas en el orden de las diapositivas. Claude también puede crear esqueletos de notas, resúmenes para el examen y libros ilustrados ELI5.

> **Nota sobre el idioma:** Las instrucciones, las plantillas, los comandos y la bóveda de ejemplo están en coreano, y Claude responde en coreano de forma predeterminada. Por ahora, solo la documentación y los archivos para colaboradores tienen versión en inglés. Este README es una traducción de la versión en inglés; si difieren, prevalece el README en inglés.

---

## Qué hace

| Lo que dices | Lo que ocurre |
|---|---|
| `운체 3` | Muestra un mapa del capítulo 3 dividido en grupos, con una pregunta clave por grupo, y luego explica el grupo 1 |
| `운체 3-2` / `다음` | Explica un grupo en el orden de las diapositivas, con fórmulas, ejemplos numéricos resueltos y preguntas de autoevaluación |
| `골격 만들어줘` + PDF | Crea una nota vacía con el formato `## Sección / ### Slide Title (coreano) / - ` |
| `정리해줘` | Completa tus notas a partir del PDF sin tocar lo que escribiste |
| `시험 정리본` | Marcas de importancia ★, tablas comparativas, ejercicios de práctica con criterios de calificación y preguntas y respuestas sobre los puntos clave del examen |
| `/eli5 {nota}` | Un libro ilustrado en HTML que distingue las analogías de las definiciones de la clase |
| `저장해줘` / `운체 3 전부` | Guarda las explicaciones de los grupos como notas en `클코 설명/`, encadenadas de la primera a la última con enlaces `다음 →` |
| `기출 분석` + exámenes anteriores o reseñas de exámenes | Escribe en `클코 정리/기출 분석.md` tablas de problemas por año, temas frecuentes y prioridades |
| (`증명 과목` en las excepciones del curso) | Plantillas de demostración para cada teorema, tablas de recíprocos y condiciones, y simulacros de examen con el formato de los exámenes anteriores |

## Configuración en 5 minutos

1. Obtén este repositorio: **Use this template** en GitHub, o Code → Download ZIP.
2. Tomando `example-vault/` como referencia, crea una carpeta para el curso en tu bóveda de Obsidian. Puedes ponerla dentro de una carpeta del semestre; en ese caso, escribe la ruta completa en la tabla de cursos.
   ```
   (raíz de la bóveda)/
   ├── CLAUDE.md          ← si usas Claude Code (paso 4)
   ├── templates/         ← copia de templates/ de este repositorio
   ├── tools/             ← copia de tools/ de este repositorio
   └── {curso}/
       ├── 강의자료/        ← PDF de las clases (solo lectura)
       ├── {título de la clase}.md  ← notas semanales
       ├── 개념.md          ← nota central de conceptos + tabla de notas semanales
       ├── 클코 정리/       ← resúmenes para el examen, análisis de exámenes anteriores
       ├── 클코 설명/       ← explicaciones de grupos guardadas
       └── 학습자료/        ← HTML ELI5
   ```
   Ponle a cada PDF de clase el mismo nombre que a su nota (`1주차 정렬 기초.md` ↔ `강의자료/1주차 정렬 기초.pdf`) para que funcionen los enlaces a páginas del PDF.
3. Abre `INSTRUCTIONS.md` y completa tu universidad, tus cursos y sus abreviaturas en el bloque **"📝 여기만 고치세요"** ("edita solo aquí"). Escribe cada carpeta de curso como una ruta desde la raíz de la bóveda (p. ej., `딥러닝/`).
4. Pásale las instrucciones a Claude.
   - **Claude Projects**: pega el contenido en Project instructions y sube la carpeta del curso y los archivos de `templates/` como conocimiento del proyecto.
   - **Claude Code**: haz los mismos cambios en `CLAUDE.md`, copia `CLAUDE.md`, `templates/` y `tools/` a la raíz de tu bóveda y ejecuta Claude Code desde ahí. El verificador de enlaces requiere Python 3.8 o posterior.
5. Prueba con `{abreviatura} 1`.

## Estructura del repositorio

| Ruta | Contenido |
|---|---|
| [`INSTRUCTIONS.md`](INSTRUCTIONS.md) | Las instrucciones (para Claude Projects) |
| [`CLAUDE.md`](CLAUDE.md) | Las mismas instrucciones (para Claude Code) |
| [`templates/`](templates) | Plantillas vacías: esqueleto de notas, 개념.md, resumen para el examen, explicación de grupo, análisis de exámenes anteriores, HTML ELI5 |
| [`tools/check_links.py`](tools/check_links.py) | Verificador de enlaces de Obsidian (detecta notas, encabezados y archivos adjuntos que faltan) |
| [`example-vault/알고리즘/`](example-vault/알고리즘) | Un ejemplo completo con un curso ficticio de Algoritmos. Ábrelo en Obsidian |
| [`docs/usage-examples.md`](docs/usage-examples.md) | Flujo de conversación de cada comando |
| [`docs/FAQ.md`](docs/FAQ.md) | Preguntas frecuentes |

## Principios básicos

- **Los materiales de clase son la fuente de verdad.** Todo lo que no está en las diapositivas se marca como "교재 보충" (complemento del libro de texto).
- **Tus notas nunca se sobrescriben.** Claude solo agrega lo que falta, con cambios mínimos.
- **Se respeta el orden de las diapositivas.** Los grupos nunca se mezclan y las diapositivas del apéndice tienen sus propios grupos.
- **Las explicaciones nunca se quedan cortas.** Cada concepto sigue el orden motivación → intuición → definición/fórmula → ejemplo numérico → limitaciones.

## ⚠️ No subas los materiales de clase

Los materiales de clase de tus profesores, y las notas que transcriben el contenido de las clases, son obras protegidas por derechos de autor. Si haces una copia de seguridad de tu bóveda en GitHub, usa el [`.gitignore`](.gitignore) de este repositorio y no la subas a un repositorio público. Todos los ejemplos de este repositorio son clases ficticias escritas desde cero.

## Cómo contribuir

Son bienvenidos los nuevos comandos, las reglas para otros tipos de cursos y las mejoras en las plantillas. Lee [`CONTRIBUTING.md`](CONTRIBUTING.md), abre un issue con una de las plantillas de issues (Bug Report / Enhancement Request / Common Issue) y luego envía un PR. En cada PR se comprueba automáticamente la sincronización de los archivos de instrucciones, los enlaces de la bóveda de ejemplo y si se subieron materiales de clase.

## Licencia

[MIT](LICENSE)
