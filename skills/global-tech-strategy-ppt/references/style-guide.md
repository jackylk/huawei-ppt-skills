# Global Technology Strategy Style Guide

## What The Style Should Feel Like

This is a global technology strategy consulting deck, not a marketing deck and not a corporate brand imitation.

- **Insight pages:** dense, evidence-led, chart-first. They combine market maps, competitor matrices, customer pain, startup signals, technology mechanism diagrams, and short source notes. Each page ends in a hard judgment.
- **Strategy pages:** technical and decision-oriented. They show target architecture, capability stacks, operating model, roadmap gates, and key-technology mechanisms with measurable build targets.
- **Color is a signal:** blue/teal show strategy direction and architecture flow; amber shows timing or risk; muted crimson marks contradiction, gap, threat, or final judgment. Color is not decoration.
- **The title is a claim:** titles should state the conclusion, not merely label the topic.

## Canvas

- 16:9 widescreen.
- White, off-white, or very light cool-gray background.
- Use tight but consistent margins, aligned grids, thin separators, and dense tables.
- Avoid decorative gradients, black hero panels, neon effects, bokeh/orbs, oversized empty cards, and fake logos.

## Typography

- Title: charcoal/black, bold, claim-like, top-left.
- Subtitle: dark gray, compact, usually one line.
- Section headers: small all-caps English labels or compact Chinese labels are acceptable.
- Body text: compact Chinese management-report phrasing; prefer phrases over long paragraphs.
- Table and diagram labels: dense but legible; do not rely on tiny unreadable text.
- Use a top-right chapter tag on long decks, usually a small gray or blue-gray pill.

## Color

- Charcoal title/text: `#111827`.
- Slate body text: `#374151`.
- Cool gray frame/fill: `#E5E7EB`, `#F3F4F6`, `#F9FAFB`.
- Strategy blue: `#1D4ED8`.
- Architecture teal: `#0F766E`.
- Timing/risk amber: `#B45309`.
- Gap/threat crimson: `#B91C1C`.

Keep accents restrained. Most of the slide should remain white/gray/charcoal.

## Core Layouts

### 1. Dense Insight Board

Use for industry, technology trend, competitor, customer, investor, or startup analysis.

Structure:
- Top title states a hard judgment.
- 2-4 evidence zones across the page.
- Each evidence zone has a mini title, chart/table/diagram, and 1-2 highlighted keywords.
- Bottom judgment converts evidence into a technical or strategic implication.
- One page covers one theme only.

### 2. Market / Category Map

Use when explaining where value is moving.

Recommended elements:
- Segment grid or value-chain map.
- Incumbents/platforms/startups/open-source placed by role.
- Customer budget owner and buying center annotations.
- Callout for commoditized layer vs emerging control point.
- Bottom judgment: which segment to enter first and why.

### 3. Competitor Route Matrix

Use for landscape and gap analysis.

Rows:
- competitor products, cloud platforms, startups, OSS projects, and our current product/service combination.

Columns:
- customer need, product wedge, architecture route, integration surface, governance/trust, packaging/pricing, technical moat, our gap.

End with a concise "strategic opening" or "defense requirement".

### 4. Competitor Mechanism Page

Use for an important competitor or route.

Layout:
- Left/top: 2-3 official screenshots, charts, product diagrams, or source excerpts when available.
- Center/left: redrawn architecture or principle diagram based on the researched mechanism.
- Right: 3-5 viewpoint bullets tied to what the evidence proves.
- Bottom: one implication for build strategy, differentiation, or gap closure.

Do not fabricate product UI screenshots. If exact screenshots are unavailable, use clearly labeled source blocks and a redrawn mechanism diagram.

### 5. Insight Summary Bridge

Use after individual insight pages and before strategy pages.

Layout:
- Left 60-65%: synthesized target category or control-plane model.
- Right 35-40%: 3-4 grouped implications.
- Bottom: one sentence that directly leads into the strategy part.

This page answers: "Given the evidence, what architecture category should we build toward?"

### 6. Architecture Competitiveness Page

Use for target architecture and competitive strategy.

Left 55-65%:
- Layered architecture stack or operating model diagram.
- Concrete module names, interfaces, flows, policy/observability loops, and dependency arrows.

Right 35-45%:
- Architecture competitiveness bullets.
- Use this form: `<quantified target> -> <technical lever> -> <customer/competitive effect>`.

Bottom:
- restrained judgment callout with blue/teal/amber/crimson depending on meaning.

### 7. Key Technology Mechanism

Use one page per key technology.

Must show:
- problem/failure mode
- architecture position
- module decomposition
- core objects/interfaces
- data/control flow
- evaluation method
- table-stakes / competitive / leading quantitative targets

Good diagrams:
- `Input/Event -> State/Context -> Planner/Policy -> Tool/Runtime -> Verification -> Feedback`
- `API -> Control plane -> Runtime -> Storage/index -> Evaluation -> Ops`
- `Object schema -> lifecycle -> permission -> execution -> audit/replay`

### 8. Roadmap With Decision Gates

Use for strategy summary or construction plan.

Layout:
- swimlanes by capability, product package, platform foundation, evaluation/governance, GTM/customer validation.
- phases by quarter/half-year/year.
- gates with metric thresholds and go/no-go decisions.

## Language Patterns

Use hard, compressed strategic judgment:

- "价值从功能入口迁移到可治理的任务控制面。"
- "单点 Copilot 会被通用模型商品化，护城河必须落在上下文、权限、执行闭环和评测。"
- "客户愿意为生产级可信闭环付费，而不是为一个更会写文案的助手付费。"
- "领先不是功能更多，而是关键任务在真实企业约束下可度量、可回滚、可审计。"

Avoid:
- vague adjectives such as "先进", "领先", "智能化" without proof.
- pure source lists with no contradiction or implication.
- decorative diagrams that do not explain technical mechanism.

## Final QA

At thumbnail size, each slide should reveal a different proof object: market map, matrix, mechanism, architecture, roadmap, decision tree, or evidence board.

At readable size, check:
- title is a judgment.
- text is legible and not fake/garbled.
- density is high but grouped.
- strategy pages visibly derive from insight pages.
- color is restrained and meaningful.
- key-technology pages explain what engineers should build and how to judge success.
