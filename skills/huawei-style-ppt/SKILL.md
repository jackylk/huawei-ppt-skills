---
name: huawei-style-ppt
description: "Use when the user asks for Huawei-style PPT in 汇报版 or 生动版, white/red Chinese enterprise reports, vivid illustrated technical architecture or scenario slides, or imagegen slide images assembled into a PPTX."
---

# Huawei-Style PPT

Use this skill to create Chinese enterprise technical-report slides in a Huawei-like white/red style by generating full-slide PNGs with `imagegen` and assembling them into a 16:9 PPTX.

This skill has one output mode: **full-page imagegen slides assembled into PPTX**. Do not switch to editable/native PPTX, hybrid rebuilds, or native PowerPoint shape/text generation inside this skill. If the user asks for editable PPT, explain that this skill is optimized for full-page imagegen output and suggest using a separate editable-PPT workflow.

## Choose the Visual Edition

These are two visual editions of this skill, not separate output formats:

| Edition | Choose when | Visual treatment |
| --- | --- | --- |
| **汇报版 (report, default)** | The user requests 汇报版, formal management/board reporting, or gives no visual preference | The original restrained white/red/gray style: structured diagrams, evidence boards, matrices and roadmaps. Read [references/style-guide.md](references/style-guide.md). |
| **生动版 (lively)** | The user requests 生动版, asks for more vivid/形象/活泼 scene-based explanation, or supplies a reference in this style | People and friendly Agent illustrations, concrete files/devices/systems, and labeled process/feedback paths within the same enterprise grid. Read [references/lively-style.md](references/lively-style.md). |

An explicit edition or supplied visual reference takes precedence over the default. Do not ask again when the choice is already clear. Record the edition in the slide plan and each imagegen prompt; preserve it during revisions. 生动版 retains technical depth and can contain a text-first table with no characters when the content calls for it. Do not automatically add mascots or reduce information density on every page.

## Workflow

1. Establish the edition, deck outline, audience, and slide count from the request; clarify only missing information that affects the result.
2. Draft each slide as a concise message: title, claim, main proof object, layout zones, and bottom viewpoint.
3. Generate each slide as a 16:9 PNG with `imagegen`.
4. When an exact paper figure, chart, or official screenshot must appear, embed the saved original in a reserved box on that PNG using `scripts/embed_source_figures.py`.
5. Inspect the final slide images, including the embedded figures; use a contact sheet when there are more than 3 slides.
6. Copy final PNGs into the project output directory and use `scripts/make_image_pptx.py` to place one PNG full-bleed on each PPT slide.
7. Report the PPTX path and the image folder path.

For production decks where text correctness matters, keep the page as full-slide imagegen output, but make the prompt more explicit, regenerate weak pages, and inspect the contact sheet. Do not rebuild the deck as editable native PowerPoint inside this skill.

## Exact Source Figures

ImageGen may use a reference image to guide composition, but it can redraw labels, numbers, or arrows. When the user wants the **original** paper figure, chart, or official screenshot, save the source asset locally with its URL, figure/page identifier, and access date. Reserve a plain rectangular image area in the full-slide prompt. Generate the whole page first, then programmatically place the saved source image into that area of the slide PNG. This keeps the final PPTX as one flattened image per slide. Do not call an ImageGen recreation an original figure.

Use pixel coordinates from the generated slide. The JSON paths are relative to the placement file:

```json
[{"source":"../research/figures/paper-fig-2.png","box":[100,280,800,720],"padding":12,"background":"#FFFFFF"}]
```

```bash
python ~/.codex/skills/huawei-style-ppt/scripts/embed_source_figures.py \
  --base outputs/<deck-name>/imagegen/slide-01-generated.png \
  --placements outputs/<deck-name>/prompts/slide-01-figures.json \
  --output outputs/<deck-name>/images/slide-01.png
```

The helper requires Pillow. Keep the unaltered ImageGen output and source asset for later revisions. After every regeneration of the page, embed the source again. Check that the figure is legible, uncropped, and attributed in the slide/source notes before packaging.

## Style Rules

Use the selected edition's reference for visual rules, layouts and prompt examples. `references/style-guide.md` preserves the original **汇报版**; `references/lively-style.md` defines **生动版**. Both share these essentials:

- White background.
- Black titles, never colored titles.
- Titles should normally state a judgment or action, not just a topic label.
- Huawei gray content frames for normal boxes.
- Red only for emphasis, arrows, selected labels, warning accents, and restrained conclusion treatment.
- No black panels, no dark brush headers, no page numbers beside titles.
- Clean covers: main title, subtitle, date/author metadata, and at most 2-3 compact scenario/topic cards. Do not put architecture diagrams, dense object chips, evidence boards, logo strips, or KPI matrices on the cover.
- Bottom viewpoint/conclusion should use restrained Huawei-red treatment: pale-red callout, thin red rule, red left bar, or small red `判断` / `启示` label. Avoid large pure-red frames and thick red boxes.
- Layouts use a proof object appropriate to the content: architecture, scene/process, comparison matrix, roadmap, control-flow, evidence board or validation/KPI matrix.
- Overall architecture pages should not be diagram-only; include a right-side explanation panel unless the user explicitly asks for a pure visual.

## Huawei Red Discipline

Keep the Huawei white/red style, but use red as a precision signal rather than a large emotional block.

- Use dark red for text accents and arrows, Huawei red for thin rules and selected marks, and pale red backgrounds for conclusion callouts.
- Avoid thick red borders, large red outline boxes, full red panels, and repeated red rectangles; they look too刺眼 for enterprise report pages.
- Keep red visual area roughly under 5-8% of a dense slide. Most structure should remain white, light gray, dark gray, and black.
- Prefer these conclusion treatments:
  - Pale-red callout with 1-2px red border.
  - White callout with 4-6px red left bar.
  - 2px red top/bottom rule plus black judgment text.
  - Small red label followed by black body text.
- Use solid red or heavy red frames only for exceptional warning pages.

## Imagegen Prompt Pattern

Use this structure for each generated slide:

```text
Use case: productivity-visual
Edition: <汇报版 / 生动版; include the selected edition's visual treatment>
Asset type: 16:9 full-slide Chinese enterprise PPT page, 1920x1080.
Strict style rules: Huawei-like white report style; no slide number; no title number; no numeric markers unless explicitly required; title must be black; all normal boxes use Huawei gray outlines (#BFBFBF / #D9D9D9); no black panels; no logos; no watermark. Red only for arrows, emphasized keywords, selected marks, and restrained conclusion treatment. Avoid thick red frames, large red outline boxes, and solid red panels.

Title in black: <title>
Subtitle in dark gray: <subtitle>
Claim: <one sharp judgment>
Layout zones: <exact left/right/top/bottom structure with proportions>
Main proof object: <diagram/table/chart instructions with exact node labels, layers, arrows, rows/columns, metrics, or steps>
Right-side or bottom interpretation: <concise judgment bullets or explanatory blocks>
Bottom conclusion treatment: restrained Huawei-red callout, preferably pale-red background with thin red border or a red left bar: <one-sentence viewpoint>
Design quality: formal Huawei-style management technical briefing, clean grid, readable Chinese and English labels, professional, high information density but not crowded.
```

For an actual cover, keep it sparse: title, subtitle, optional 2-3 compact scenario/topic cards, requested metadata, and one restrained red rule. A first-page challenge analysis or architecture overview is a content page, not a cover; give it the explanation its topic needs.

## Packaging

After generating images, copy them into a stable project folder such as:

```text
outputs/<deck-name>/images/slide-01.png
outputs/<deck-name>/images/slide-02.png
```

Then run:

```bash
python ~/.codex/skills/huawei-style-ppt/scripts/make_image_pptx.py \
  --images outputs/<deck-name>/images \
  --output outputs/<deck-name>/<deck-name>.pptx
```

The script sorts image filenames lexicographically, so use zero-padded names like `slide-01.png`.

If `python-pptx` is unavailable, use another packaging tool only to place each generated PNG full-bleed on a blank 16:9 slide. A packaging fallback must not become a native editable PPTX rebuild.

## Checks

Before final delivery, verify:

- The PPTX has the expected slide count.
- Slides are 16:9.
- Final PPTX pages are full-slide image pages; do not silently substitute editable/native PowerPoint shapes.
- The cover is intentionally sparse and does not look like an architecture or insight slide.
- No slide has accidental title numbering.
- Each non-cover slide has one claim, one proof object, and one bottom viewpoint.
- Overall architecture pages include explanatory text, not only a diagram.
- Normal content boxes are gray, not red.
- Red is restrained: no thick red boxes, no large solid red panels, no repeated red containers.
- Bottom conclusions use pale-red callouts, thin red rules, or red left bars unless an exceptional warning page needs stronger treatment.
- Page 3/story pages clearly show the intended business logic, not only abstract labels.
- Generated Chinese is legible; reject pages with garbled Chinese, unreadable labels, or obvious layout collisions.
- The selected edition is consistent. In 生动版, illustrations explain roles, actions or outcomes rather than filling space.
- Read each arrow as a sentence: source, action and destination must be correct; independently inspect query/response and question/feedback directions.
- Preserve user-approved detail and full process sentences. For dense tables, inspect every row and its bottom padding; never let a footer hide the last row.
