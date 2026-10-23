# 生动版 — Lively Enterprise Explanation

Use this edition to make a technical system tangible: who does the work, what files or data move, how the process works, and why the outcome matters. Keep the rigor and information density of an enterprise report. This is a visual edition of `huawei-style-ppt`, with the same full-page imagegen/PPTX workflow.

## Visual Language

- White background, black titles, dark-gray body, thin gray frames and generous alignment. Use restrained red for actions, selected terms and pale-red conclusions.
- Small professional workplace illustrations: people at laptops, friendly original robot Agents, documents, folders, YAML/Markdown pages, databases, clouds, clocks and shields. Soft dimensional rendering and subtle shadows are suitable; avoid toy packaging, childish scenes and imitation commercial characters.
- Treat pictures as diagram nodes with an actual role or action. Use topic-specific objects rather than decorating every slide with the same robot.
- A scene explains the mechanism; the text explains the reasoning and value. Keep body text large enough to read and leave room for full explanations when requested.
- A challenge page can open the deck. Apply a sparse cover treatment only to an actual cover.

Optional visual reference: inspect [the examples](../assets/lively-examples.jpg) when matching the edition. Left: illustrated overview; middle: factual/semantic governance; right: a text-first solution table. These are style examples, not reusable product claims or mandatory architecture components. Do not copy their names, topology or capabilities into unrelated decks.

## Choose the Proof Object

| Content | Lively treatment |
| --- | --- |
| Overall architecture | About 65–70% concrete scene/system diagram plus 25–30% concise value explanation; roles, system boundary and major paths stay readable. |
| Challenge analysis | Two or three substantial zones: concrete situation, explanation of the problem, example and consequence. Let text carry the argument; small scenes support it. Spread challenges across pages when the reasoning needs space. |
| Mechanism | A process, lifecycle, branch/version pipeline or feedback loop using recognizable objects and labeled actions; side notes explain technical guarantees and limits. |
| File organization | A real directory tree and example files, with links between topics and back to source evidence. Keep derived indexes distinct from folders when that is the design. |
| Scenario | User request → responsible role → definitions/evidence → action → output. Use examples without inventing actual financial values or measured results. |
| Detailed comparison | A table is the main visual. Reserve the widest column for the concrete process; keep full approved sentences. Characters are optional and often unnecessary. |

These are layout options, not a fixed deck outline, page count or product architecture.

## Make the Technical Meaning Visible

Before prompting, record each important edge as `source → action → destination`. Separate ingestion, initialization, runtime retrieval, external queries and user feedback when those paths exist in the design. A body paragraph alone is not enough for a capability the user wants visible in the architecture.

For example, if the brief defines a background Agent that verifies external facts and asks experts to resolve concepts, draw both paths with correct endpoints. Do not silently route its external query through a different Agent. Requests and responses need distinct labels and directions; one clearly labeled bidirectional connector can be better than tangled parallel loops.

Use human/Agent icons to show the agreed roles, not to invent new ones. A specialized Work Agent is still a Work Agent when the brief says so. Label platform boundaries, native directories, local copies, remote systems and access-control boundaries accurately. This is semantic QA, not decoration.

## Content and Revisions

- Titles state one topic or judgment; the main proof object substantiates it and the bottom line explains the value.
- Do not turn detailed reasoning or user-approved process sentences back into slogans. In a challenge–solution–technology table, describe the input, processing and returned output; name the mechanisms and responsible roles in the technology column.
- Prefer gray structures with selected red terms over repeated red boxes. Roughly 5–8% red area is enough; image icons can use restrained natural colors.
- For tables, start around 16% / 56% / 28% for challenge / process / technology, then adjust to the actual text. Use variable row heights and keep the footer outside the table. Check the final row at full size.
- Treat requested pixel dimensions as generation targets, not verified output. Inspect the actual image size and legibility; asking for 4K does not establish that the tool produced it.
- Revise only the requested pages. Preserve other page images, notes and order, repackage, and compare unchanged image bytes when practical.
- Keep target design, actual implementation, verification plans and measured results distinct. Style cannot establish correctness or benchmark superiority.

## Prompt Recipes

Fill these with the approved brief; the placeholders are content slots, not invented facts.

### Illustrated architecture

```text
Use case: productivity-visual
Edition: 生动版, professional lively enterprise explanation.
16:9 full-slide Chinese PPT. White background, ALL title text black,
gray frames, thin red separator, restrained red arrows and pale-red conclusion.
Small friendly original Agent robots and people at laptops; concrete files,
folders and systems. No logos, watermark, page number, dark panels or giant red boxes.

Title: <one topic/judgment>
Subtitle: <purpose>
Left 68%: <roles, boundary, files/systems and their placement>.
Exact connections: <source -> labeled action -> destination for each path>.
Right 27%: <three short explanations of mechanisms/value>.
Bottom: <one supported value statement>.
Keep every required path visible and each arrow's endpoints correct.
Use illustrations to explain the mechanism; keep text and diagram equally legible.
```

### Full-process table

```text
Edition: 生动版, text-first enterprise comparison page.
White background, black title, gray table grid and alternating pale-gray rows.
Title: <topic>. Table headers: 挑战 | 选择的方案（具体过程） | 核心技术与执行角色.
Exact rows: <approved full sentences, including all qualifications>.
The process column is widest. Preserve every sentence; do not reduce it to phrases.
No illustration may consume space needed by the table.
Adapt row heights and padding; all rows, especially the last, must remain visible.
Place the restrained conclusion below the table, never over it.
```

## Final Visual Check

Inspect the actual generated image, not just the prompt: black titles, readable Chinese, correct actors/boundaries, arrow directions, visible evidence/feedback paths when required, and unclipped table cells. For more than three slides, inspect a contact sheet as well. Exact third-party figures still follow the shared source-figure embedding workflow; do not redraw an original figure and present it as the source.
