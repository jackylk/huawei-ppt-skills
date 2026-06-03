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
- Do not place page numbers inside the generated slide image. Avoid large top-left number blocks such as `04.`; the title should start directly with the claim or section label.

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

### 0. Clean Technical Cover

Use for the first slide of serious technical-planning decks.

The cover should be calmer and cleaner than the body pages:
- Keep only the main title, subtitle, date, author/owner, and at most 2-3 compact scenario/topic cards.
- Do not place architecture stacks, capability matrices, state-object lists, evidence blocks, source notes, or KPI dashboards on the cover.
- If scenario cards are useful, make them thin-outline cards under the subtitle. Each card should have one short title and one compact descriptor line. They should signal the planning scope, not explain the architecture.
- Use plenty of whitespace. A thin Huawei-red rule under the title or near the bottom is enough for brand emphasis.
- Prefer bottom-left metadata such as `日期：YYYY年M月D日` and `作者：<name> 与 Codex 联合共创` when the user asks for author/date.
- Avoid logos unless the user explicitly asks. Do not add page numbers, dates outside the metadata block, version badges, decorative icons, or technical module chips.

Good cover structure:
- main title
- subtitle
- optional compact scenario cards
- date and author metadata
- one restrained red rule

Bad cover structure:
- title plus architecture diagram
- title plus seven or more object chips
- title plus competitor logo strip
- dense claim matrix or evidence board

### 1. Dense Insight Board

Use for industry, competitor, technology trend, or customer analysis.

Structure:
- Top title states the judgment.
- 2-4 evidence zones across the page.
- Each evidence zone has a mini title, chart/table/diagram, and 1-2 red keywords.
- Bottom red viewpoint converts evidence into technical implication.
- One page covers one theme only. Do not mix competitor analysis, customer demand, technology trend, and market landscape into one slide.

Good for:
- "<technology primitive> 从单点工具演进为 <system foundation>"
- "只比拼单项性能会失焦，端到端任务成功率、治理、恢复和验证才是规模化瓶颈"

### 2. Competitor Capability Matrix

Use for landscape and gap analysis.

Rows:
- Representative incumbents, cloud/platform vendors, startups, open-source projects, and internal alternatives.

Columns:
- Core capability route
- State/version/recovery model
- Integration surface
- Governance/security
- Cost/operations
- Evaluation transparency
- Customer/workflow fit

End with a red "战略空窗": where a differentiated system, product, or platform can define a deeper category.

### 2b. Technology Trend Page

Use for research and architecture trend analysis.

Evidence zones:
- workload shift: short single-step usage becomes long-running, multi-step, multi-actor, or governed workflow.
- benchmark shift: single performance metric is no longer enough; task success, recovery, quality, cost, and review time matter.
- state/model shift: linear records evolve toward traceable state, versioning, lineage, diff, merge, restore, or audit.
- enterprise constraint: permission, audit, safety, cost, cleanup, and governance become product capabilities.

End with a red "技术拐点": a capability is moving from helper/tool feature to system-level infrastructure.

### 2c. Technical Insight Mechanism Page

Use for technology-analysis pages inside the insight section, especially when the slide needs to explain a technical mechanism, route evolution, startup/open-source approach, paper idea, or vendor architecture direction.

Top:
- Title is a judgment, not a topic label. Example: `洞察：在线和离线两种模式互补，实现 Skill/Tool/系统提示词的全面自进化`.
- Top-right uses a thin segmented navigator. Default segments: `洞察分析 | 技术构想 | 执行策略`, with `洞察分析` highlighted in Huawei red. Add `任务书` only if the deck-wide reference style explicitly requires it.

Left 58-62%:
- Use one large technical mechanism visual as the page's proof object.
- Valid visual forms include online/offline loop, timeline plus mechanism, control loop, evaluation loop, skill/tool/prompt lifecycle, state transition diagram, tool routing flow, architecture mechanism, protocol flow, or research pipeline.
- The visual should explain the technology's operating principle, not decorate the page.
- Include named boxes, arrows, loop labels, source labels, and small metric notes where useful.

Right 34-38%:
- Column title: `关键技术`.
- Use 2-3 boxed text blocks with red mechanism headings.
- Each block names one concrete mechanism such as `Skill增量更新（skill patch）`, `基于反思的提示词进化（GEPA）`, `在线执行轨迹沉淀`, `离线评测驱动优化`, or topic-specific equivalents.
- Bullets start with bold mechanism labels and a colon, then state implementation plus implication:
  - `模糊匹配链：采用多策略匹配链进行文本替换，容错 LLM 输出格式变化；`
  - `原子化写入：先检测威胁模式，再决定 Skill 内容是否回滚；`
  - `结构与大小验证：校验结构完整性和内容大小，避免技能膨胀导致加载性能下降；`

Bottom or right-bottom:
- Add `洞察观点`.
- Use 2-3 numbered judgments, or one compact bottom-band judgment.
- The viewpoint must answer: what changed, why it matters, and what planning implication follows.

Writing form:
- Use named mechanisms, not generic nouns.
- Make the right side analytical: mechanism -> why it works -> what limitation or strategic implication follows.
- Do not write a neutral source summary. The page must end in a viewpoint.

### 2d. Insight Summary Page

Use after the individual insight pages and before technical-construction pages. It is a bridge page: it condenses competitor, technology, customer, and market insights into the architecture direction.

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
- Bottom or final red sentence: the strategic implication that leads directly into the technical-construction architecture page.

### 3. Architecture Competitiveness Page

Use for target architecture and architecture competitiveness pages in the technical-construction section.

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

### 4. Overall Technical Construction Page

Use at the start of the technical-construction part. It translates insight summary into construction principles.

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

### 6b. Key Technology Scenario And Competitiveness

Use for pages titled like `关键技术1：<技术机制>，<竞争力结果>` where the goal is to explain one key technology deeply enough to guide construction.

Top:
- Title is a hard technical claim, for example `关键技术1：基于元上下文锁定和跨步回溯，保障长程任务的可靠运行`.
- Top-right uses a segmented chapter navigator, not a pill tag. Example segments: `洞察分析 | 技术构想 | 执行策略`.
- Highlight the current segment in Huawei red. Keep inactive segments white/light gray with thin borders.

Left 48-52%:
- Header: `长程任务应用场景与诉求` or `<topic>应用场景与诉求`.
- A compact mechanism diagram chosen for the technology itself. Use named boxes and arrows, but do not force a layered workflow.
- Valid left-side diagram forms include task DAG, dependency graph, state machine, control loop, data-flow, sequence diagram, architecture stack, lifecycle map, version DAG, failure-recovery loop, evaluation loop, or tool-dispatch trace.
- Pick the diagram form that makes the technology principle easiest to understand. For example, Task Planner should often use a DAG/dependency graph or plan-verify-replan loop; Workspace should use version DAG/branch lifecycle; Guardrails should use risk state machine; Evaluation should use offline-online feedback loop.
- Keep the left diagram clean. Do not force red numbered anchors on the mechanism diagram, and do not add a separate process-step numbering system such as 1-5 red dots.
- Use plain arrows, module labels, grouping boxes, and subtle red highlights only where needed. The right-side numbered construction items are the primary numbering system.
- 3-4诉求 boxes stacked vertically to the right of the diagram or below it.
- Each诉求 box follows:
  - red header: `诉求一：<demand>`
  - 1-2 bullets: `挑战一：<specific failure mode>`, `挑战二：<specific failure mode>`

Right 48-52%:
- Header: `关键竞争力目标`.
- Top row has 3 goal capsules. Each capsule combines a number with business/technical meaning, such as `7*24小时 自主工作`, `100+ Agent 协同开发`, `1000+ 工具调用 不丢失目标`.
- Below the capsules, write 3-5 numbered technical construction items.
- Each item uses a red numbered headline and black mechanism bullets:

```text
① <capability action + competitive result>
• <bold mechanism name>：<specific implementation>, <effect or prevention>;
• <bold mechanism name>：<runtime/evaluation method>, <threshold or acceptance condition>;
```

Writing style:
- The red headline should be action-oriented: `元上下文锁定，避免目标漂移`, `CheckPoint快照，错误恢复时间缩短至毫秒级`, `自适应熔断，打破工具调用死循环`.
- Start bullets with the mechanism name in bold, then explain the implementation. Avoid vague "提升/增强/优化" language.
- Use concrete objects: `System prompt`, `缓存层`, `DAG状态图`, `state/memory`, `行为指纹Hashing`, `滑动窗口`, `动态熔断器`, `上下文裁剪`, `过程反馈信号`.
- Include quantitative or operational thresholds where possible: `每5-10步`, `语义相似度>85%`, `毫秒级恢复`, `短时间超阈值`, `7*24小时`.
- End the item by tying mechanism to competitive result: less drift, faster recovery, fewer dead loops, lower token waste, better convergence.

This pattern is preferred over generic "关键技术/难点/指标" boxes when a single technology deserves a full design page.

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

- "单点性能只是入口，端到端可验证成功率才是规模化控制点。"
- "系统差异化不在工具清单，而在可恢复、可审计、可治理的运行闭环。"
- "版本化与因果链路把临时实验变成可治理资产。"
- "权限、成本和回滚必须产品化，否则并行执行会放大控制面风险。"

Avoid:
- vague adjectives: "先进", "领先", "智能化" without proof.
- pure lists with no conclusion.
- long paragraph explanations where a matrix or mechanism diagram is better.

## Domain-Specific Content Heuristics

When building a domain-specific technical planning deck:

- Start with the category shift: what used to be a helper/tool capability is becoming a system-level foundation.
- Show that competitors optimize different axes: user workflow, platform integration, governance, reliability, cost, evaluation, or ecosystem leverage.
- Position the proposed system around the real wedge scenario and the capabilities required to win that scenario.
- Make the technical plan concrete: APIs, lifecycle state machine, metadata model, execution hooks, policy enforcement, evaluation loop, cleanup/operations jobs.
- Use benchmarks, task sets, fault injection, pilot workflows, or acceptance rubrics as product proof.

## Final QA

At thumbnail size, each slide should reveal a different proof object and a red argument path.

At readable size, check:
- title is black and claim-like.
- no page number is embedded in the generated image, especially no large top-left number block.
- text is not fake or garbled.
- dense pages still have grouping and hierarchy.
- technical-construction and execution-strategy pages visibly use left visual/right explanation when appropriate.
- red is scarce and meaningful.
- bottom viewpoint is a conclusion, not a label.
