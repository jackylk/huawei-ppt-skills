---
name: huawei-style-ppt
description: "Create Huawei-style enterprise technical presentation decks and slide images. Use when the user asks for Huawei-style PPT, white/red Chinese management-report slides, strategy/architecture decks, imagegen-generated PPT pages, or wants generated slide images assembled into a PPTX."
---

# Huawei-Style PPT

Use this skill to create Chinese enterprise technical-report slides in a Huawei-like white/red style by generating full-slide PNGs with `imagegen` and assembling them into a 16:9 PPTX.

This skill has one output mode: **full-page imagegen slides assembled into PPTX**. Do not switch to editable/native PPTX, hybrid rebuilds, or native PowerPoint shape/text generation inside this skill. If the user asks for editable PPT, explain that this skill is optimized for full-page imagegen output and suggest using a separate editable-PPT workflow.

## Workflow

1. Clarify the deck outline, audience, and slide count if not already clear.
2. Draft each slide as a concise message: title, subtitle, main diagram layout, and bottom conclusion.
3. Generate each slide as a 16:9 PNG with `imagegen`.
4. Inspect a contact sheet or thumbnails before packaging when there are more than 3 slides.
5. Copy final PNGs into the project output directory.
6. Use `scripts/make_image_pptx.py` to place one PNG full-bleed on each PPT slide.
7. Report the PPTX path and the image folder path.

For production decks where text correctness matters, keep the page as full-slide imagegen output, but make the prompt more explicit, regenerate weak pages, and inspect the contact sheet. Do not rebuild the deck as editable native PowerPoint inside this skill.

## Style Rules

Follow `references/style-guide.md` for exact visual rules. The core style is:

- White background.
- Black titles, never colored titles.
- Huawei gray content frames for normal boxes.
- Red only for emphasis, arrows, selected labels, warning accents, and restrained conclusion treatment.
- No black panels, no dark brush headers, no page numbers beside titles.
- Bottom viewpoint/conclusion should use restrained Huawei-red treatment: pale-red callout, thin red rule, red left bar, or small red `判断` / `启示` label. Avoid large pure-red frames and thick red boxes.
- Layouts are management-report diagrams: layered architecture, comparison, matrix, roadmap, capability grid, control-flow.

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
Asset type: 16:9 full-slide Chinese enterprise PPT page, 1920x1080.
Strict style rules: Huawei-like white report style; no slide number; no title number; no numeric markers unless explicitly required; title must be black; all normal boxes use Huawei gray outlines (#BFBFBF / #D9D9D9); no black panels; no logos; no watermark. Red only for arrows, emphasized keywords, selected marks, and restrained conclusion treatment. Avoid thick red frames, large red outline boxes, and solid red panels.

Title in black: <title>
Subtitle in dark gray: <subtitle>
Layout: <diagram/layout instructions>
Bottom conclusion treatment: restrained Huawei-red callout, preferably pale-red background with thin red border or a red left bar: <one-sentence viewpoint>
Design quality: formal Huawei-style management technical briefing, clean grid, readable Chinese and English labels, professional, high information density but not crowded.
```

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
- No slide has accidental title numbering.
- Normal content boxes are gray, not red.
- Red is restrained: no thick red boxes, no large solid red panels, no repeated red containers.
- Bottom conclusions use pale-red callouts, thin red rules, or red left bars unless an exceptional warning page needs stronger treatment.
- Page 3/story pages clearly show the intended business logic, not only abstract labels.
