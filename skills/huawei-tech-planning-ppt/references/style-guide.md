# Huawei Technical Planning Style Guide

## What The Reference Samples Teach

The style is a technical planning report, not a marketing deck.

- **Insight pages:** very dense, multi-source, and judgment-led. They combine charts, competitor matrices, paper/product references, process diagrams, and red callouts. The slide earns its density by ending in a precise point of view.
- **Planning pages:** more architectural. The common layout is left visual plus right explanation. The left side shows architecture, flow, layered capability, or mechanism. The right side explains competitiveness, key technologies, constraints, and roadmap.
- **Red is argumentative:** it marks the thesis, risk, or key path. It is not decoration.
- **Gray is structural:** frames, grids, tables, and separators use light gray.
- **The title is a claim:** title text usually contains the conclusion, not a neutral topic label.

## Canvas

- 16:9 widescreen.
- White or very light gray background.
- Thin gray outer guide lines or section dividers are acceptable.
- Leave a tight but consistent margin. These decks can be dense, but they are not chaotic.

## Typography

- Title: black, bold, top-left, roughly 24-32 pt in editable PPT.
- Subtitle or tag line: dark gray, 10-14 pt.
- Section headers: black or white-on-red strip, 10-14 pt.
- Body text: 8-12 pt depending on density.
- Table text: 6.5-9 pt is acceptable only when the page is meant to be read on a monitor, not projected.
- Use Chinese management-report phrasing. Prefer compressed phrases over full paragraphs.

## Color

- Huawei red: `#C7000B` or close.
- Text black: `#111111`.
- Dark gray text: `#4A4A4A`.
- Frame gray: `#BFBFBF`, `#D9D9D9`, `#E6E6E6`.
- Pale red fill for selected cells: `#FDEBEC`.
- Pale gray fill for grouped areas: `#F5F5F5`.

Avoid black backgrounds, cyberpunk gradients, neon effects, decorative blobs, heavy drop shadows, and large colored title panels.

## Core Layouts

### 1. Dense Insight Board

Use for industry, competitor, technology trend, or customer analysis.

Structure:
- Top title states the judgment.
- 2-4 evidence zones across the page.
- Each evidence zone has a mini title, chart/table/diagram, and 1-2 red keywords.
- Bottom red viewpoint converts evidence into technical implication.
- One page covers one theme only. Do not mix competitor analysis, customer demand, technology trend, and market landscape into one slide.

Good for:
- "数据库分支从 DevOps 工具演进为 agent 基础设施"
- "只比拼秒级分支会失焦，深分支读写、治理、清理才是规模化瓶颈"

### 2. Competitor Capability Matrix

Use for landscape and gap analysis.

Rows:
- Neon/Xata/Supabase/PlanetScale/Turso/Doltgres/DBay.

Columns:
- Branching model
- Version/snapshot
- Diff/merge
- Agent workflow
- Data masking
- Control-plane QoS
- Benchmark transparency

End with a red "战略空窗": where DBay can define a deeper category.

### 2b. Technology Trend Page

Use for research and architecture trend analysis.

Evidence zones:
- agent workload shift: one user/task becomes many parallel agents.
- branching benchmark: fast branch creation vs deep-branch read/write tradeoff.
- state model shift: linear snapshots evolve toward DAG lineage, diff, merge, restore, squash.
- enterprise constraint: masking, audit, QoS, cleanup become product capabilities.

End with a red "技术拐点": branchable databases are becoming agent state infrastructure, not just preview database tooling.

### 2c. Insight Summary Page

Use after the individual insight pages and before strategy pages. It is a bridge page: it condenses competitor, technology, customer, and market insights into the architecture direction.

Layout:
- Title is short and red, usually "洞察总结" or a claim title.
- Left 60-65% is a layered concept architecture that names the emerging target system. It is not yet the detailed final architecture; it is a synthesis model.
- The far-left vertical axis names the major value domains or capability domains, using the current topic's own language.
- The left diagram uses stacked large bands and nested rectangles. It should show how upper applications/capabilities depend on middle platform layers and lower resource/data foundations.
- Right 35-40% is a dense text column with 2-4 red group headers. Each group explains what the prior insights imply for product/architecture planning.

Writing form:
- Start from the conclusion of previous insight pages, not from a new topic.
- Each right-side group uses numbered points. The first phrase is the strategic object, followed by "通过/以/将..." explaining mechanism and impact.
- The page should answer: "These insights imply what new architecture category or technical base?"
- Do not copy reference-specific nouns. Replace them with the current topic's domains, layers, and capability names.

Good structure:
- Left diagram: `<new architecture category>` with layers such as application/capability, platform/control, state/data, runtime/resource, governance/observability.
- Right text groups: `<创新应用>`, `<融合平台>`, `<关键底座>` or better topic-specific names.
- Bottom or final red sentence: the strategic implication that leads directly into the architecture strategy page.

### 3. Architecture Competitiveness Page

Use for target architecture and architecture competitiveness strategy pages.

Left 55-65%:
- Use one large layered architecture diagram with a vertical capability axis on the far left.
- Name layers from the current architecture domain. Do not reuse sample-specific terms unless they are actually part of the user's architecture.
- Each layer is a horizontal band with rectangular module boxes. Module names should be concrete system components or capabilities.
- The top row can show two or three major domain surfaces, product lines, or old/new directions if that helps explain the architecture shift.
- The middle should show the core coordinating layer of the architecture using rectangular modules and one or two loop arrows to indicate orchestration, data flow, or feedback.
- Lower layers should show the foundation services, runtime, data substrate, resource pool, policy plane, or other domain-specific base layers that the architecture truly depends on.
- Some module boxes can carry red markers that correspond to right-side competitiveness points, but do not force every module to map to a point.
- Add a few vertical arrows to show the main dependency path and a few side arrows for feedback, lifecycle, governance, or observability loops.

Right 35-45%:
- Use a planning text column headed "战略规划" or "架构竞争力".
- Group bullets by the architecture's own layers or capability domains. Examples of generic group labels are `<接入层>`, `<编排层>`, `<状态层>`, `<安全层>`, `<基础层>`, but choose labels from the actual architecture.
- Each bullet starts with a bold red capability name, then explains target, technology, and effect in compact management-report language.
- Prefer this writing form: `<量化目标/范围>：通过<关键技术/模块组合>，实现<能力效果/竞争力>`。
- Avoid copying the reference slide's specific nouns such as its product names, resource-pool names, or lakehouse/serverless terms unless the current architecture really uses them.
- Avoid using separate right-side blocks for "关键技术/工程挑战/验证指标" on target-architecture pages; those belong on later mechanism or roadmap pages.

Bottom:
- red-outlined viewpoint box.

### 4. Overall Construction Strategy Page

Use at the start of the strategy part. It translates insight summary into construction principles.

Layout:
- title is a strategic claim.
- left or center uses a framework diagram: strategic objective, design principles, capability pillars, and expected effects.
- right side explains 3-5 construction strategies.

Writing form:
- `<策略方向>：通过<架构/产品/技术抓手>，实现<战略效果>`。
- Include quantified targets where possible.
- This page should answer: "What should we build and why this path?"

### 5. User Scenario Explanation Page

Use after the overall architecture page to explain how target users use the architecture.

Layout:
- left: scenario flow from user/task trigger to architecture modules to outcome.
- right: scenario value, user pain point, involved modules, metrics.
- Use 2-3 scenarios if space allows; otherwise one scenario in depth.

Writing form:
- `<用户/场景> -> <任务动作> -> <调用架构模块> -> <可量化结果>`。
- Do not repeat architecture module descriptions; explain the workflow and value.

### 6. Key Technology Mechanism

Use when explaining the technical core.

Left:
- mechanism diagram: metadata DAG, snapshot lineage, branch lifecycle, diff/merge path, masking flow.

Right:
- bullet groups under "关键技术", "难点", "验证指标".

### 7. Strategy Summary / Roadmap With Governance Gates

Use as the closing strategy page. It can be a roadmap, KPI gate page, investment priority page, or executive summary.

Columns:
- short term: safe agent sandbox
- mid term: checkpoint/restore/version lineage
- long term: collaboration/diff/merge/promotion gate

Rows or bottom band:
- API, storage/metadata, security, control plane, benchmark.

Use red diamonds or vertical gates for decisions.

## Language Patterns

Use strong, concise, technical judgment:

- "分支速度只是入口，状态谱系才是 agent 规模化的控制面。"
- "Agent-native 数据库的关键不在连接串，而在可试错、可回滚、可合并、可审计。"
- "版本 DAG 把并行实验从临时资源变成可治理资产。"
- "安全分支、QoS 与 cleanup 必须产品化，否则 agent 并发会放大控制面风险。"

Avoid:
- vague adjectives: "先进", "领先", "智能化" without proof.
- pure lists with no conclusion.
- long paragraph explanations where a matrix or mechanism diagram is better.

## DBay / Agentic DB Content Heuristics

When building an Agentic DB planning deck:

- Start with the category shift: database branching moves from developer preview environments to AI agent infrastructure.
- Show that competitors optimize different axes: serverless branching, full preview platform, schema governance, Git-like data semantics, edge branching.
- Position DBay around "agent-native database workspace": branch/version lifecycle, version DAG, masking, audit, QoS, cleanup, benchmark.
- Make the technical plan concrete: workspace API, branch lifecycle state machine, version DAG metadata, diff/merge engine, policy enforcement, async cleanup jobs.
- Use benchmarks as product proof: branch create p95, compute ready time, version read p95, branch depth impact, cleanup final consistency, rate-limit predictability.

## Final QA

At thumbnail size, each slide should reveal a different proof object and a red argument path.

At readable size, check:
- title is black and claim-like.
- text is not fake or garbled.
- dense pages still have grouping and hierarchy.
- strategy pages visibly use left visual/right explanation.
- red is scarce and meaningful.
- bottom viewpoint is a conclusion, not a label.
