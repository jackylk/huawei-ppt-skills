# Huawei-Style Enterprise PPT Guide

This is a general Huawei-like enterprise presentation style guide. It covers visual system, cover style, common slide layouts, prompt discipline, and QA rules. It is not limited to technical-planning decks.

## Visual System

- Background: white or very light gray only.
- Title: black, bold, top-left. The title should usually state a judgment or action, not a neutral topic label.
- Subtitle/tag line: dark gray.
- Content boxes: Huawei gray outlines, usually `#BFBFBF`, `#D9D9D9`, or `#E6E6E6`.
- Emphasis: Huawei red, usually `#C7000B`.
- Pale red fill for selected cells or conclusion callouts: `#FDEBEC`.
- Pale gray fill for grouped areas: `#F5F5F5`.
- Red is argumentative: use it for thesis, risk, selected labels, arrows, and bottom viewpoint. It is not decoration.
- Gray is structural: use it for frames, grids, separators, matrix lines, and normal content boxes.

Avoid:
- black panels, dark brush strokes, cyberpunk gradients, neon glow, decorative blobs, heavy drop shadows, large colored title panels.
- generated/approximate logos, fake product UI screenshots, watermarks, metadata footers.
- page numbers inside generated slide images, especially large top-left page-number blocks such as `04.`.
- thick red borders, large pure-red frames, full red panels, repeated red rectangles, or red containers around normal content.

## Canvas And Typography

- Canvas: 16:9 widescreen.
- Margin: tight but consistent. Dense does not mean chaotic.
- Title size in editable reference terms: roughly 24-32 pt.
- Subtitle or tag line: roughly 10-14 pt.
- Section headers: 10-14 pt.
- Body text: 8-12 pt depending on density.
- Table text can be small only if the slide is meant for monitor reading.
- Use Chinese management-report phrasing. Prefer compressed phrases and named mechanisms over long paragraphs.

## Clean Cover

Use for the first slide of serious enterprise decks.

The cover should be calmer and cleaner than body pages:
- Keep only the main title, subtitle, date, author/owner, and at most 2-3 compact scenario/topic cards.
- Do not place architecture stacks, capability matrices, object-chip rows, evidence blocks, source notes, logo strips, or KPI dashboards on the cover.
- If scenario/topic cards are useful, make them thin-outline cards under the subtitle. Each card should have one short title and one compact descriptor line.
- Use plenty of whitespace. A thin Huawei-red rule under the title or near the bottom is enough.
- Prefer bottom-left metadata such as `日期：YYYY年M月D日` and `作者：<name> 与 Codex 联合共创` when the user asks for author/date.
- Avoid logos unless the user explicitly asks.

Good cover structure:
- main title
- subtitle
- optional compact scenario/topic cards
- date and author metadata
- one restrained red rule

Bad cover structure:
- title plus architecture diagram
- title plus seven or more object chips
- title plus competitor logo strip
- dense claim matrix or evidence board

## Common Slide Anatomy

Most Huawei-style pages should have:

1. Black judgment title.
2. Optional dark gray subtitle or top-right chapter tag.
3. Main proof object: diagram, table, matrix, control flow, architecture stack, roadmap, or evidence board.
4. Right-side or bottom explanation when the diagram needs interpretation.
5. Bottom viewpoint/conclusion with restrained Huawei-red treatment.

Preferred bottom viewpoint treatments:
- Pale-red callout with 1-2px red border.
- White callout with 4-6px red left bar.
- Thin red top/bottom rule plus black judgment text.
- Small red label such as `判断` / `启示` followed by black body text.

## Core Layouts

### 1. Dense Insight Board

Use for industry, customer, competitor, technology trend, or market analysis.

Structure:
- Top title states the judgment.
- 2-4 evidence zones across the page.
- Each evidence zone has a mini title, chart/table/diagram, and 1-2 red keywords.
- Bottom red viewpoint converts evidence into implication.
- One page covers one theme only. Do not mix market landscape, competitor analysis, customer demand, and technology trend on the same slide unless the page is explicitly a synthesis.

### 2. Competitor / Capability Matrix

Use for landscape and gap analysis.

Typical columns:
- capability route
- state/version/recovery model
- integration surface
- governance/security
- cost/operations
- evaluation transparency
- customer/workflow fit

End with a red gap or opportunity statement.

### 3. Technical / Mechanism Insight Page

Use when explaining a mechanism, product route, paper idea, open-source approach, or vendor architecture direction.

Layout:
- Left 58-62%: one large mechanism visual as the proof object.
- Right 34-38%: 2-3 named mechanism blocks with compact bullets.
- Bottom or right-bottom: insight viewpoint.

Valid mechanism visuals:
- online/offline loop
- control loop
- evaluation loop
- state transition diagram
- tool routing flow
- protocol flow
- research pipeline
- lifecycle map

The visual should explain the operating principle, not decorate the page.

### 4. Architecture Page

Use for target architecture, system design, or architecture competitiveness.

Left 55-65%:
- one large layered architecture or system-flow diagram.
- layer names come from the current topic, not from a sample deck.
- modules are concrete components or capabilities.
- include arrows for dependency, data flow, lifecycle, feedback, governance, or observability.

Right 35-45%:
- explanation column headed `架构说明`, `架构竞争力`, `关键机制`, or another topic-specific label.
- group bullets by architecture layers or capability domains.
- each bullet should follow: `<capability>：通过<mechanism/modules>，实现<effect>`。

Overall architecture pages should not be diagram-only; include a right-side explanation panel unless the user explicitly asks for a pure visual.

### 5. Key Technology / Key Capability Page

Use for pages that explain one capability deeply enough to guide construction.

Recommended structure:
- Left: mechanism diagram chosen for the capability itself. Use task DAG, dependency graph, state machine, control loop, data-flow, sequence diagram, architecture stack, lifecycle map, version DAG, failure-recovery loop, evaluation loop, or tool-dispatch trace.
- Right: `关键机制`, `建设目标`, `难点`, `验证指标`, or `竞争力目标` blocks.
- Bottom: one viewpoint explaining why this capability matters.

Do not force red numbered anchors on the left diagram. Use plain arrows, module labels, grouping boxes, and subtle red highlights.

### 6. Scenario Explanation Page

Use to explain how users, customers, or workflows use the system.

Structure:
- left: scenario flow from trigger to action to system modules to outcome.
- right: user pain, involved modules, value, and metrics.
- 2-3 scenarios are acceptable if each is compact; otherwise explain one scenario deeply.

Writing form:
- `<用户/场景> -> <任务动作> -> <调用模块> -> <可量化结果>`。

### 7. Roadmap Page

Use for phased plans.

Structure:
- 3-4 stages across a horizontal timeline.
- each stage has deliverables, acceptance criteria, and key risks.
- bottom strip states strategic sequencing: what to do first and what to defer.

### 8. Validation / KPI Page

Use when a deck must prove feasibility or value.

Structure:
- benchmark/task set/customer pilot/ops trace on one side.
- KPI groups on the other side.
- connect each KPI to a measurable surface.

Avoid abstract metrics without measurement surfaces.

## Imagegen Prompt Discipline

Each final imagegen prompt should include:

```text
Use case / asset type / style
Forbidden elements: no slide number, no page number, no title numbering prefix, no logos unless provided, no black panels, no glow.
Top-right chapter tag if useful
Title and subtitle
Claim: one sharp judgment
Layout zones: exact left/right/top/bottom structure with proportions
Main proof object: exact diagram/table/matrix content, including node labels, arrows, layers, axes, metrics, or scenario steps
Evidence or content blocks: labels and short phrases to place on the page
Right-side or bottom interpretation: concise judgment bullets
Bottom viewpoint: exact one-sentence conclusion
Visual density: enough content units for the page type, but not crowded
```

Bad prompt:

```text
Title: 总体架构
Layout: 八层架构
Main claim: 四个对象是关键。
```

Good prompt:

```text
Layout: left 62% layered architecture stack, right 32% key mechanism cards, bottom restrained red viewpoint.
Architecture layers from bottom to top: input capture, event normalization, context snapshot, intent package, permission ticket, routing, execution receipt, memory.
Show red arrows from intent package -> permission ticket -> routing -> execution receipt.
Right cards: intent package = goal/constraints/context refs; context snapshot = authorized/expiring/traceable; permission ticket = least privilege/risk level; execution receipt = result/failure/next confirmation.
Bottom viewpoint: 没有对象协议，输入层只能做文本增强；有对象协议，输入层才能成为控制面。
```

## Text Density

For imagegen slides:

- Keep titles concise but judgment-led.
- Keep each card to one heading plus 1-2 short lines.
- Dense pages are acceptable when they have a real proof object: matrix, architecture, process, data-flow, evidence board, or KPI table.
- Avoid long prose paragraphs. Use compressed phrases.
- Use English technical labels only where they improve recognition.

## Quality Checks

Before delivery:

- Expected slide count matches the user request.
- Slides are 16:9.
- Final PPTX pages are full-slide image pages; do not silently substitute editable/native PowerPoint shapes.
- Cover is intentionally sparse: title, subtitle, date/author metadata, and at most 2-3 compact scenario/topic cards.
- A directory/agenda slide is present when the deck is more than a few pages or the user asks for a report-style deck.
- Each non-cover slide has one claim, one proof object, and one bottom viewpoint.
- Overall architecture pages are not diagram-only; they include explanatory text.
- Normal content boxes use gray outlines; red is reserved for thesis, arrows, selected labels, and restrained conclusion treatments.
- Red does not dominate the page. Avoid thick red boxes, solid red panels, and overusing red on every container.
- No colored title, no black title panel, no decorative gradient/orbs, no fake logos.
- Generated Chinese is legible. Regenerate slides with garbled Chinese, unreadable small labels, sparse content, or obvious layout collisions.
- Contact sheet inspection is mandatory for decks with more than 3 slides.
