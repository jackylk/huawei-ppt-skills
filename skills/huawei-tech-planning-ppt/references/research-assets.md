# Research And Asset Workflow

Use during the insight stage. Huawei-style insight pages need evidence, not generic claims.

## Research Rules

- Search after the user confirms the insight agenda.
- Prefer primary sources: official product docs, official blogs, papers, benchmark reports, standards, reputable analyst reports, and company technical posts.
- Use current sources when the topic is fast-moving. Record source date or access date.
- Keep one insight page to one theme. Do not merge competitor, customer, market, and technology trend evidence on the same page.

## Save Assets

Create a project-local research folder:

```text
outputs/<deck-name>/research/
  sources.md
  screenshots/
  figures/
  extracted/
```

Save:

- screenshots of relevant diagrams, charts, tables, product docs, benchmark figures, or architecture pages that may be visually cited or redrawn.
- source notes in `sources.md`: title, URL, date/access date, why it matters, likely slide.
- extracted facts or metrics in `extracted/` when the source has dense data.

Do not use screenshots as decorative filler. Use them only if they prove a claim, guide a chart, or supply a visual object to redraw.

## Embed an Exact Paper Figure or Screenshot

Use this when the slide must show an original figure, chart, or official screenshot with accurate internal labels. ImageGen references guide its rendering but do not preserve source pixels reliably.

1. Download the image asset from the primary source (for example, the paper's HTML figure asset) into `research/figures/`. Record the paper/page/figure identifier, URL, and access date in the material index. If only a PDF is available, crop the actual figure from the PDF and keep the PDF/page provenance.
2. In the page prompt, specify a plain rectangular slot with its approximate size and position. Generate the complete 16:9 slide with ImageGen. Save the unmodified output separately from the final image.
3. Measure the slot on the generated PNG and write a placement file. Coordinates are `[left, top, right, bottom]` pixels, within the slide. Paths are relative to the JSON file:

   ```json
   [{"source":"../research/figures/paper-fig-2.png","box":[100,280,800,720],"padding":12,"background":"#FFFFFF"}]
   ```

4. Embed the source file with the skill's Pillow helper (install `Pillow` if needed):

   ```bash
   python ~/.codex/skills/huawei-tech-planning-ppt/scripts/embed_source_figures.py \
     --base outputs/<deck-name>/imagegen/slide-01-generated.png \
     --placements outputs/<deck-name>/prompts/slide-01-figures.json \
     --output outputs/<deck-name>/imagegen/images/slide-01.png
   ```

5. Inspect the final PNG at slide scale and zoomed figure scale. Check internal labels, arrows, numbers, aspect ratio, no clipping, and contrast with the reserved background. Cite the original in a visible source note or PPTX notes/source index. Package the final PNG as one full-bleed image on the PPT slide.

Repeat the embedding after every ImageGen revision of that page. The figure is an original placed into a generated page, not a native PPT shape or an ImageGen redraw. The final PPTX page remains a single flattened image and is not element-editable.

## Insight Claim Extraction

For each potential insight, write:

```text
Source evidence: <what the source proves>
Conflict/gap: <what tension this creates>
Slide claim: <one-sentence judgment>
Strategy implication: <what architecture or roadmap choice follows>
Material: <screenshot/file/source URL>
```

Only create slides for claims that have both evidence and strategy implication.
