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
  extracted/
```

Save:

- screenshots of relevant diagrams, charts, tables, product docs, benchmark figures, or architecture pages that may be visually cited or redrawn.
- source notes in `sources.md`: title, URL, date/access date, why it matters, likely slide.
- extracted facts or metrics in `extracted/` when the source has dense data.

Do not use screenshots as decorative filler. Use them only if they prove a claim, guide a chart, or supply a visual object to redraw.

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
