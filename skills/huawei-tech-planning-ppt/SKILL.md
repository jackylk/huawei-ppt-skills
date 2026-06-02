---
name: huawei-tech-planning-ppt
description: "Use when the user asks for Huawei-style Chinese technical planning PPTs, insight-to-plan narratives, high-density enterprise strategy slides, architecture planning pages, or technical roadmap decks such as Agentic AI/data infrastructure planning."
---

# Huawei Tech Planning PPT

Use this skill for Chinese enterprise technical-planning decks where the job is not only to make slides look Huawei-like, but to turn dense insight material into a sharp technical plan.

The core pattern is:

```text
行业/技术/友商/客户洞察 -> 洞察总结 -> 总体构建策略 -> 总体架构 -> 用户场景 -> 重点模块/关键技术 -> 策略总结
```

For deep technical planning, assume the deck is meant to guide 2-3 years of technical construction, not just explain a product. Default to a 30-40 page structure unless the user asks for a short deck:

```text
Part 1 洞察: 15-20 pages
Part 2 策略: 15-20 pages
```

Each part needs its own directory/agenda slide. For long decks, add a small top-right chapter tag on every page, such as `Part 1 洞察 / 友商分析` or `Part 2 策略 / 关键技术`.

## Interaction Contract

Do not jump straight into slide generation unless the user already supplied a clear outline, audience, and source scope. First lock the writing frame with the user.

Required frame:

```text
Part 1: 洞察
Part 2: 策略
```

The user may rename the parts, but do not merge them. Huawei-style technical planning decks need evidence-led insight pages before architecture planning pages.

Ask questions in stages. Prefer 2-4 concise questions per stage; stop asking once the answer is enough to draft the next artifact.

Before research or slide writing, always understand the user's writing direction. Ask explicitly about:

- **Research focus:** which industries, companies, technologies, customer groups, regions, reports, papers, or conferences matter most.
- **Intended viewpoints:** what conclusions, strategic positions, concerns, or hypotheses the user already wants to express or test.
- **Information density:** whether pages should be high-density technical planning pages, medium-density executive pages, or low-density visual storytelling pages.
- **Audience and decision use:** who will read the deck and what decision or investment it must support.

Give the user selectable options for each question, with a recommended default first. Always allow the user to add free-form constraints. Example option sets:

```text
1. 调研重点
   A. 全景深度调研（推荐）：行业/技术/友商/客户/学术/开源/投资都覆盖
   B. 友商与产品优先：重点看竞品、云厂商、startup、产品架构和发布动态
   C. 技术路线优先：重点看论文、开源、架构、关键技术与工程可行性
   D. 客户与买点优先：重点看用户场景、痛点、付费点和采购决策

2. 已有观点
   A. 帮我从调研中提炼观点（推荐）
   B. 我已有明确观点，需要材料证明
   C. 我有假设，但希望调研挑战和修正
   D. 主要做战略备选方案对比

3. 信息密度
   A. 高密度技术规划页（推荐）：适合专家评审和技术决策
   B. 中密度管理汇报页：适合高层快速判断
   C. 低密度视觉叙事页：适合宣讲和对外材料

4. 决策用途
   A. 未来2-3年技术规划与投入决策（推荐）
   B. 产品立项/路线图评审
   C. 架构方案评审
   D. 客户/销售/生态沟通
```

Do not begin broad research until these are clear enough to guide source selection and slide writing. If the user says to proceed without details, state a reasonable default direction and continue.

Default deck structure:

```text
Part 1 洞察
- 行业趋势洞察
- 技术趋势洞察
- 友商分析
- 客户需求洞察
- 洞察总结

Part 2 策略
- 总体构建策略
- 总体架构图
- 用户场景讲解
- 重点模块与关键技术
- 策略总结
```

Long-form planning structure:

```text
封面
Part 1 洞察目录
核心观点总览
历史脉络与阶段判断
市场/会议/厂商/云厂商/创业公司/开源/学术/客户/投资观点洞察
友商分析若干页
客户、用户、场景、买点分析
洞察总结与策略推导
Part 2 策略目录
总体构建策略
目标架构与竞争力
用户场景与产品包
关键技术若干页（一页一个关键技术）
量化目标、路线图、阶段门禁
策略总结
```

## Guided Workflow

Treat this skill as a multi-stage workflow. Keep track of which stage the user is in; when feedback arrives, route it to the right earlier stage instead of blindly regenerating slides.

For long-form decks, maintain a visible task plan with statuses. The user should see progress through research, reusable materials, claims, slide briefs, imagegen prompts, generation, PPTX packaging, and QA. Update the plan when entering a new stage or completing a material checkpoint.

Example:

```text
Updated Plan
└ 页数已调整为40页，进入详细页稿与生成阶段。
  ✔ 建立40页工程和可复用素材库
  □ 调研厂商、会议、论文、开源、客户和投资观点
  □ 保存来源文本、截图、引用摘录和素材索引
  □ 形成核心洞察、客户/用户场景与买点分析
  □ 形成策略架构、关键技术与量化目标
  □ 形成40页详细页稿和 imagegen 提示词
  □ 生成高密度 imagegen 页面并合成 PPTX
  □ 检查 contact sheet、素材可复用性和交付说明
```

Keep the plan specific to the current deck. Do not leave generic tasks like "do research"; name the actual research domains or source groups when known.

### Stage 1: Frame

   - Confirm topic, audience, expected slide count, delivery mode, and whether there are reference decks/images.
   - State that the deck will be split into **洞察** and **策略**.
   - Ask the mandatory writing-direction questions: research focus, intended viewpoints, information density, and decision use.
   - Create the initial visible plan after the user answers enough to proceed.

### Stage 2: Insight Agenda

   - Treat the default insight scope as industry trend, technology trend, competitor analysis, customer demand, and insight summary.
   - Ask which of the default themes must be included, reduced, or emphasized.
   - Ask for target competitors, reports/sources, target customer types, and must-cover technical signals.
   - Ask what the user already believes or wants challenged, so research can prove, disprove, or refine those viewpoints rather than becoming a generic scan.
   - If the user does not know, propose a default agenda based on the topic.

### Stage 3: Insight Research

   - Search the web for current primary or high-quality sources after the user confirms the insight agenda.
   - Save useful screenshots, charts, source images, or page captures under the project output directory when they may become PPT material.
   - Record source URLs, dates, and why each source matters.
   - Convert research into one-theme insight claims; do not make a slide just because a source exists.
   - Use `references/research-assets.md` for the asset workflow.
   - Use the Deep Research Matrix below. Cover market/category, customers/users, technology trends, competitors/incumbents, startups, academic/open-source, investor/analyst views, and key-person viewpoints unless the user explicitly narrows the scope.
   - For rapidly changing topics, research recent product releases, conference announcements, roadmap signals, X posts by company leaders/key engineers, startup launches, open source projects, academic papers, customer pain points, consulting reports, and investor views.
   - Preserve reusable source material under a stable research directory: raw pages, extracted text, screenshots, product screenshots, chart images, quote snippets, and a material index. Future revisions should enrich this repository rather than restart research.
   - Separate page screenshots from true product screenshots. Product screenshots must come from official docs, official blogs, demos, or other attributable sources. Do not let image generation invent competitor product UIs.
   - For competitor/technology pages, first understand the architecture and mechanism, then redraw the key technical principle in the deck. Use original screenshots as evidence and the redrawn diagram as interpretation.
   - Treat research and slide writing as auditable artifacts. Save synthesis notes, slide claims, and imagegen prompts in reviewable Markdown/JSON files so the user can inspect or edit them before regeneration.
   - Do not treat a quick web scan or a list of major vendors as "deep research". For long-form planning decks, Stage 3 must pass the research sufficiency gate below before writing the final outline or claiming the insight work is complete.
   - Update the visible plan when each research group is completed: vendors, conferences, papers, open source, customer/user evidence, investor/analyst views, and leader/key-person viewpoints.
   - Research must produce sharp judgments, not neutral summaries. For every major insight, write the evidence chain, the opposing interpretation, why the chosen judgment is stronger, and what strategic action follows.

### Stage 4: Strategy Agenda

   - Treat the default strategy scope as overall construction strategy, overall architecture diagram, user scenarios,重点模块与关键技术, and strategy summary.
   - Ask what strategy output needs extra emphasis: architecture competitiveness, roadmap, product packaging, benchmark/KPI, governance, or delivery phases.
   - Ask what existing product constraints, technical assumptions, and desired differentiators must be reflected.

### Stage 5: Deck Spec

   - Return a two-part outline with slide titles and one claim per slide.
   - Get user approval before generating slides or PPTX.
   - For deep 30-40 page decks, do not stop after producing only an outline unless the user explicitly asked for an outline-only checkpoint. If the output is only an early outline, label it clearly as `preliminary outline, not deep analysis yet` and continue with research or ask whether to continue.
   - Update the visible plan after the outline is accepted or revised.

### Stage 6: Slide Plan

   - For each slide, write title, claim, proof object, layout, red judgment, and key source needs.
   - For architecture pages, use the current topic's own layer names and modules; do not copy terms from reference examples.
   - For insight pages, start from a small set of core viewpoints. Write one overview page of these viewpoints, then use customer pain points, vendor product evidence, academic/open-source trends, and investor/analyst/customer quotes to support each viewpoint.
   - For strategy pages, every architecture, scenario, and key technology page must visibly derive from a prior insight. Avoid service introductions unless they explain a technical lever, competitive capability, or required new capability.
   - Persist the slide plan as a user-editable source of truth. The user may directly edit a slide claim, evidence list, layout instruction, or imagegen prompt and ask to regenerate only that page.
   - Do not let a slide plan remain at the level of `title + claim + layout type`. For high-density planning decks, each slide brief must contain enough concrete content to render a strong page: exact diagram nodes, evidence blocks, labels, metrics, comparison dimensions, source notes, and the bottom judgment text.
   - Before generation, expand each slide brief into a page-level content spec. A prompt that only says "四象限矩阵" or "八层架构" without concrete quadrant/layer labels, supporting evidence, and visual hierarchy is not acceptable.

### Stage 7: Generate

   - Generate every final slide as one full-slide imagegen PNG. This skill has one output path: full-page imagegen slides assembled into PPTX.
   - Do not switch to editable/native PPTX, hybrid rebuilds, or post-composited page construction just because a packaging dependency is missing.
   - For imagegen decks, write one prompt file per slide before generation. Use stable filenames such as `prompts/slide-01.md` or `prompts/slide-01.json`.
   - Each per-slide prompt must be a full page specification, not a short title/claim stub. It must include title, subtitle, page layout zones, concrete diagram/table contents, evidence/source blocks, bottom viewpoint, and visual density instructions.
   - After generating, copy final images into the project output directory and keep the prompt files next to them. Do not leave the only prompt copy hidden in the chat transcript.
   - Render a contact sheet and inspect against the quality gates before delivery.
   - In the delivery summary, always tell the user where the source workspace is, where the reusable materials are, where the slide plan and per-slide prompts are, and how to request an incremental revision.
   - Update the visible plan after image generation, PPTX packaging, and QA are complete.

### Stage 8: Revise

   - First classify the user feedback: insight scope, source evidence, claim spine, architecture, architecture competitiveness, key technology, roadmap, visual style, text accuracy, or output format.
   - If the feedback changes the argument, return to the relevant agenda/spec stage before regenerating.
   - If the feedback is local visual/text polish, revise only the affected slide(s).
   - If the user edits a page prompt or slide brief, regenerate that page from the edited artifact, then rebuild the PPTX and contact sheet.
   - If the user adds new information after a first version, run incremental research for the affected section, add sources to the existing research directory, update the synthesis/claims, then revise only affected slide briefs and prompts.
   - Preserve old versions unless the user asks to overwrite. Use versioned folders or filenames when making substantial revisions.
   - Use `references/revision-flow.md` for routing.

For the detailed question bank, use `references/question-flow.md`.

## Research Sufficiency Gate

For deep technical planning decks, the agent must pass this gate before presenting the main deck outline as a serious planning result.

Minimum evidence coverage:

- **Market/category analysis:** category definition, market timing, adoption drivers, ecosystem shifts, business model/buying center, and where value migrates.
- **Category history:** past state, current transition, future inflection, and why the timing matters.
- **Major incumbents/platforms:** representative leaders in the domain, including product releases, architecture direction, and public roadmap/conference signals.
- **Cloud/platform vendors:** domestic and international where relevant.
- **Startup/new entrants:** recent companies, funding/product launches, or emerging product routes.
- **Academic and open-source signals:** papers, benchmarks, datasets, GitHub projects, standards, protocols, or technical communities.
- **Customer/user/buy-point evidence:** pain points, workflows, willingness-to-pay, self-build boundary, and adoption blockers.
- **Investor/consulting/analyst views:** when available, to validate market direction and category framing.
- **Leader/key-person viewpoints:** X posts, talks, interviews, blogs, or public statements when relevant and accessible.

Recommended artifact expectations for a 30-40 page deck:

- `research/source-registry.json` contains enough sources to support every major section, not just 5-8 headline links.
- `research/material-index.md` groups sources by theme and explains why each source matters.
- `research/synthesis.md` contains evidence-backed, opinionated viewpoints, not only summaries.
- `planning/insight-claims.md` maps each core viewpoint to evidence from at least two source types where possible.
- Competitor pages have official screenshots/charts or clearly labeled page evidence plus redrawn architecture/mechanism diagrams.

If research is not sufficient, say so explicitly and continue researching. Do not imply the deck is substantially done. Use wording like:

```text
当前只是第一轮方向性调研，还没有达到深度技术规划标准。下一步我会补齐：竞品/云厂商/startup/学术开源/客户买点/投资观点/关键人物观点，并把证据合并到现有 research 目录。
```

For a user who asks "都做了调研了吗" or challenges depth, audit the research against this gate and list what is complete, what is missing, and what you will research next.

## Deep Research Matrix

For a deep planning deck, produce and save `research/deep-research-matrix.md` or an equivalent section in `research/synthesis.md`. Each row should connect raw signals to planning conclusions.

Required dimensions:

| Dimension | What to research | Minimum output |
| --- | --- | --- |
| 市场/品类 | category boundary, market timing, adoption drivers, value-chain shift, buying center, monetization/budget owner | 2-4 hard judgments about why now, where value migrates, and what becomes commoditized |
| 客户/用户/买点 | personas, jobs-to-be-done, pain transfer, self-build boundary, willingness-to-pay, procurement blockers, security/trust concerns | customer segmentation, buy-point analysis, self-build vs vendor-dependent boundary |
| 技术趋势 | architecture evolution, model/tool/runtime changes, benchmarks, standards/protocols, infra constraints, security/privacy techniques | technical inflection points and what core technologies must be mastered |
| 友商/平台 | incumbents, cloud vendors, OS/platform players, product releases, conference signals, roadmaps, pricing/packaging if relevant | competitor route map, architecture/mechanism redraw, threat/opportunity judgment |
| Startup/新进入者 | new product routes, funding, traction, wedge use case, technical differentiation, go-to-market | which startup route may disrupt incumbents and which capabilities are real vs demo |
| 学术/开源 | papers, benchmarks, datasets, GitHub projects, protocols, communities, reproducibility limits | what is becoming technically feasible and what remains unsolved |
| 投资/咨询/分析师 | a16z/VC reports, Gartner/IDC/Forrester or domain analysts, market maps, enterprise adoption surveys | external category framing and investment thesis; validate or challenge internal thesis |
| 关键人物观点 | X posts, talks, interviews, blogs by founders, researchers, platform leaders, customer CTOs | direct quotes or paraphrased viewpoints that reveal strategic direction |

For each dimension, write:

```text
Source signals -> What changed -> Customer/market pain -> Technical mechanism -> Competitive implication -> Slide ids
```

Minimum expectations:

- Do not let one famous vendor dominate the research. Include incumbents, platform players, startups, and open-source/academic signals where relevant.
- Customer analysis is not optional. If direct customer evidence is unavailable, use user workflows, public reviews/forums, enterprise adoption reports, or adjacent case studies and label the inference.
- Technology trend analysis must explain mechanism, not buzzwords.
- Competitor analysis must explain architecture/product route, not just feature lists.
- Market analysis must identify value migration and commoditization pressure, not just "market is growing".
- If a dimension lacks evidence, mark it as a gap and continue researching before final slide generation.

## Market-Customer-Competition-Industry Analysis

For solution or product technical planning, include a structured "四看" analysis. Save it as `research/market-customer-competition-industry.md` or include it in `research/synthesis.md`.

### 1. 看市场

Analyze the market at three levels:

- **宏观市场:** market size/timing, value demand, budget owner, buying center, policy/ecosystem constraints, macro drivers and inhibitors.
- **细分市场:** target segments, segment boundaries, application scenarios, demand characteristics, competitive needs, adoption maturity, monetization logic.
- **重点/典型客户:** representative customers or customer archetypes, their current workflow, decision criteria, deployment constraints, and expected value.

Output requirements:

```text
Segment -> Typical customer -> Scenario -> Value demand -> Required capabilities -> Competitive requirement -> PPT implication
```

Do not say only "market is growing". Identify which segment is worth entering first, which segment is not attractive, and why.

### 2. 看客户

Analyze typical target customers deeply:

- who the user, buyer, operator, risk owner, and technical decision maker are
- what task/job they need to complete
- where the current pain is: cost, efficiency, quality, risk, compliance, integration, skill threshold, reliability, or experience
- what value the solution creates: revenue, cost reduction, automation, quality improvement, risk reduction, new experience, ecosystem leverage
- what adoption blockers remain: migration cost, trust, data access, security review, budget, organizational boundary, integration workload

Output requirements:

```text
Customer archetype -> Current workflow -> Pain point -> Root cause -> Solution value -> Adoption blocker -> Willingness-to-pay signal
```

### 3. 看竞争

Analyze competition in the target customer market, not as a generic vendor list.

- Compare how competitors satisfy the target market's feature, scenario, integration, trust, and deployment needs.
- Evaluate competitor product-combination competitiveness, not only single product functions.
- Extract competitors' key competitive characteristics: architecture route, product packaging, ecosystem position, customer lock-in, pricing/bundling, operation model, and technical moat.
- Compare competitor product combinations with our product/service combination.
- Identify our unmet characteristics and derive solution competitiveness requirements.

Output requirements:

```text
Customer/segment need -> Competitor capability -> Competitor strength -> Our current capability -> Gap -> Required solution competitiveness
```

Use this to derive strategy pages. Do not write "we should improve competitiveness" without naming the missing capabilities.

### 4. 看行业

Analyze the broader industry environment:

- market development trend and demand migration
- 产业链/生态位 changes, platform power shifts, standards/protocols, regulation, supply constraints, and channel changes
- competitive landscape evolution: consolidation, platform bundling, startup disruption, open-source commoditization
- macro support and constraints: policy, privacy/security, compute cost, model capability, device penetration, developer ecosystem, customer budget cycle
- future market outlook and what it means for timing, entry point, and investment pacing

Output requirements:

```text
Industry trend -> Supportive forces -> Constraints -> Competitive landscape change -> Timing implication -> Strategy response
```

In the insight section, use "四看" evidence to support the core viewpoint overview. In the strategy section, use it to derive target customer selection, product package, architecture requirements, key technologies, and quantified competitiveness targets.

## Sharp Viewpoint Standard

Deep technical planning decks need hard judgments. Do not write safe, neutral, encyclopedic pages.

Every core viewpoint should pass this test:

```text
Observation: what changed in the market/technology/customer behavior?
Contradiction: what old assumption is now wrong?
Evidence chain: which customer, vendor, product, paper, open-source, or investor signals prove it?
Opposing view: what would a reasonable skeptic argue?
Judgment: what is the sharper conclusion?
Strategic implication: what should we build, avoid, or measure?
```

Good viewpoint language:

- `只做 AI 写作会被 OS 级能力商品化，输入法必须上移为意图与上下文控制面。`
- `入口不是护城河，能安全调度任务并拿到回执才是护城河。`
- `多模态不是功能清单，而是把用户意图从文本流升级为可授权的上下文流。`

Weak viewpoint language to avoid:

- `AI 输入法发展迅速。`
- `各厂商都在布局智能助手。`
- `需要提升用户体验和安全能力。`
- `未来值得关注多模态和隐私。`

If a slide title or claim could appear in any generic industry report, rewrite it. A good slide claim should force a strategic choice, expose a contradiction, or name a competitive gap.

## Research Analysis Method

Do not stop at collecting sources. Convert sources into analysis:

1. Cluster sources by theme, not by vendor list.
2. Identify the shift: past optimization target -> current competition point -> future control point.
3. Find the conflict: incumbent route vs startup route, OS platform vs third-party product, customer self-build vs vendor-paid capability, open source vs commercial moat.
4. Extract the technical mechanism behind product announcements; redraw what is happening architecturally.
5. Derive the build thesis: what core technology must be mastered, what level is table stakes, what level is leading.

For every major section, produce a short "观点推导表":

```text
Source signals -> What they prove -> Contradiction -> Judgment -> Strategy response -> Slide ids
```

If the analysis cannot fill this table, keep researching before generating slides.

## Example First Response

For a request like "给 Agent DB 做一个华为风格技术规划 PPT", respond with a scoped planning question, not a draft deck:

```text
我建议固定为两大部分：洞察 + 策略。

先确认写作方向，避免后面调研发散：
1. 调研重点：
   A. 全景深度调研（推荐） B. 友商与产品优先 C. 技术路线优先 D. 客户与买点优先
2. 已有观点：
   A. 帮我从调研中提炼（推荐） B. 我已有明确观点，需要材料证明 C. 我有假设，希望被挑战 D. 做战略备选方案对比
3. 信息密度：
   A. 高密度技术规划页（推荐） B. 中密度管理汇报页 C. 低密度视觉叙事页
4. 决策用途：
   A. 未来2-3年技术规划与投入决策（推荐） B. 产品立项/路线图评审 C. 架构方案评审 D. 客户/销售/生态沟通

也可以直接补充必须纳入或排除的厂商、报告、客户场景、技术路线。
```

After the user answers, ask the next stage about strategy output: target architecture, architecture competitiveness, key technologies, roadmap, KPIs, and constraints.

## Output Mode

This skill has one output mode: **full-page imagegen slides assembled into a 16:9 PPTX**.

- Generate each final slide as a complete full-slide PNG with imagegen. The whole page layout, diagrams, callouts, viewpoint boxes, and visual composition belong in the imagegen prompt.
- Keep the thinking layer editable through `planning/*.md` and `prompts/slide-XX.md`; the final PPT pages themselves are image-based.
- Do not offer or choose editable/native PPTX, hybrid rebuilds, or native-shape alternatives inside this skill.
- If the user asks for editable-native PPT, explain that this skill is optimized for full-page imagegen output and suggest a separate editable-PPT workflow.
- If the deck contains competitor evidence, still produce the final page through imagegen as a whole page. Use official screenshots/charts as source references when the image tool supports references; otherwise represent evidence with clearly labeled source blocks, redrawn mechanisms, and source notes. Do not fabricate competitor product UIs and call them screenshots.

Packaging discipline:

- A missing packaging dependency such as `python-pptx` is not a reason to change the output mode.
- If `python-pptx` is unavailable, first try to install it when reasonable. If installation is not possible, use another packaging mechanism such as `pptxgenjs` only to place each generated slide image full-bleed on a 16:9 slide.
- When using a packaging fallback, keep the deck image-based and tell the user: "打包工具换了，但输出仍是整页 imagegen 图片页 PPTX。"
- Do not present `pptxgenjs` native shape/text generation as a substitute for full-page imagegen slides.

## Artifact and Iteration Workflow

Technical planning PPTs are iterative. Treat the output directory as a small source workspace, not just a final PPT export.

Recommended structure:

```text
outputs/<deck-name>/
  research/
    source-registry.json
    material-index.md
    raw/
    extracts/
    screenshots/
    product-screenshots/
    quotes.md
    synthesis.md
  planning/
    deck-outline.md
    insight-claims.md
    strategy-claims.md
    slide-plan.md
  prompts/
    slide-01.md
    slide-02.md
    ...
  images/
    slide-01.png
    slide-02.png
    ...
  output/
    <deck-name>.pptx
    contact-sheet.png
```

The user must be able to review and modify:

- raw source list and material index
- extracted evidence and quotes
- synthesized viewpoints
- per-slide claim/layout/source notes
- per-slide imagegen prompt

If the user edits `prompts/slide-12.md`, regenerate slide 12 from that prompt, replace `images/slide-12.png` or write a versioned image, rebuild the PPTX, and regenerate the contact sheet. This is a good method for imagegen decks because it makes the otherwise hidden prompt layer explicit and reviewable.

For bigger analysis changes, do not patch only the prompt. Update the chain:

```text
new user information -> incremental research -> material index -> synthesis -> slide claims -> imagegen prompt -> image -> PPTX
```

Use incremental updates instead of restarting. Add new sources and conclusions into the existing research/material directories so future revisions continue from the accumulated evidence base.

## Delivery Summary Checklist

When delivering a generated deck, do not only provide the PPTX path. Always include:

- **Final PPTX:** path to the deck.
- **Contact sheet:** path to the visual overview used for QA.
- **Source workspace:** root output directory containing research, planning, prompts, images, and output.
- **Reusable materials:** paths such as `research/material-index.md`, `research/source-registry.json`, screenshots/product screenshots, extracts, and synthesis files.
- **Editable thinking layer:** paths such as `planning/slide-plan.md`, `planning/insight-claims.md`, `planning/strategy-claims.md`.
- **Imagegen inputs:** `prompts/slide-XX.md` or equivalent per-slide prompt files.
- **How to iterate:** explicitly tell the user they can edit a prompt or slide brief and ask to regenerate only that page, or provide new analysis/source material for incremental research and section-level revision.

Example delivery wording:

```text
源码工作区在 `outputs/<deck-name>/`。
你可以先看 `research/material-index.md` 和 `planning/slide-plan.md` 确认素材与观点。
如果要改某页，直接改 `prompts/slide-12.md` 或告诉我第12页要怎么变，我可以只重生成第12页并重建 PPTX。
如果要补充客户分析/技术趋势，把新信息给我，我会增量调研并合并到现有 research 与 planning 目录，不会重做一套。
```

## Core Slide Logic

Read reference decks or sample images first. Separate **洞察页** and **策略页** patterns, then extract a claim spine: one sentence per slide, each sentence must make a judgment, not list facts.

Every slide brief needs:

- black or dark-red judgment title
- short dark-gray subtitle when useful
- proof object: chart, comparison matrix, architecture diagram, roadmap, or control-flow
- concrete diagram/table content: node names, arrows, layer labels, row/column labels, metrics, or scenario steps
- 2-4 evidence blocks or source-backed facts on insight pages
- 3-5 architecture/technology explanation bullets on strategy pages
- restrained Huawei-red conclusion treatment: thin red line, pale-red callout, red left bar, or small red label
- source notes or screenshot/material references for insight pages
- top-right chapter tag for long decks

Build the insight-to-strategy logic:

```text
industry/technology/customer/competitor signal
-> contradiction or gap
-> technical strategy thesis
-> architecture and key technology response
-> measurable competitiveness or roadmap
```

## Deep Insight Writing

For 30-40 page technical planning decks, do not write insights as a source list. Use this structure:

1. **Core viewpoint overview:** 4-6 hard judgments that summarize why the category is changing and what must be built.
2. **Evidence-backed viewpoint pages:** Each viewpoint gets its own pages, supported by customer pain, vendor products, architecture changes, academic/open-source signals, conference/product launches, and investor/analyst/customer views.
3. **Historical arc:** Explain what the field used to optimize for, what changed now, how customer pain shifted, how the market competition point moved, how architecture evolved, and what future direction this implies.
4. **Competitor mechanism pages:** For each important competitor or route, show 2-3 original screenshots/charts on the left/top, redraw the key architecture or technical mechanism, then put viewpoint extraction and strategic judgment on the right.
5. **Customer and buy-point analysis:** Distinguish what customers can self-build, what they still need vendors for, and what they are willing to pay for.

When using quotes, keep them short and attributable. Prefer primary sources: official docs/blogs, conference talks, papers, GitHub repos, customer interviews/reviews, analyst/investor reports, and leader/key-engineer posts.

## Page Density and Visual Quality

High-density technical planning pages should look like serious architecture/strategy pages, not sparse lecture slides.

For each non-cover/non-directory slide:

- Use at least one strong proof object: architecture stack, flow diagram, mechanism diagram, matrix, quantified comparison, roadmap, evidence board, or decision tree.
- Include 6-12 meaningful content units across the page: diagram nodes, table cells, evidence cards, metric chips, scenario steps, or capability blocks.
- Prefer a left visual/right judgment layout, a top evidence/bottom mechanism layout, or a central architecture with side explanation. Avoid a mostly empty canvas with 3-5 floating boxes.
- Use concrete labels. Replace vague nodes like `输入层 Router` with richer mechanism labels such as `意图包解析`, `权限票据校验`, `执行体路由`, `回执验证`, `失败回滚`.
- Insight pages should show evidence and interpretation together: source signal -> what it proves -> strategic judgment.
- Strategy pages should show mechanism and build target together: architecture position -> hard technical point -> measurable target.
- Key-technology pages must include problem definition, module decomposition, technical principle, data/control flow, core objects/interfaces, evaluation method, quantified targets, competitive threshold, and engineering plan; a single router diagram or capability slogan is not enough.
- Avoid generic decorative diagrams, oversized titles, low text density, and empty whitespace. If the page reads as "one idea with a few boxes", revise the prompt before delivery.

Contact sheet inspection must check for density and visual richness. If many pages look sparse, text-light, or diagram-poor, regenerate those pages with stronger prompts before presenting the deck as complete.

## Full-Page Imagegen Prompt Requirements

The per-slide prompt is the source code for the visual page. It must be detailed enough that imagegen can draw the full page without guessing.

Each prompt should include:

```text
Use case / asset type / style
Top-right chapter tag
Title and subtitle
Claim: one sharp judgment
Layout zones: exact left/right/top/bottom structure with proportions
Main proof object: exact diagram/table/matrix content, including node labels, arrows, layers, axes, metrics, or scenario steps
Evidence blocks: source-backed facts or quoted signals to place on the page
Right-side or bottom interpretation: 3-5 concise judgment bullets
Bottom viewpoint: exact one-sentence conclusion
Visual density: high-density Huawei technical planning page; avoid sparse layout, avoid oversized empty cards, use 6-12 content units
Text discipline and red discipline
```

For key-technology pages, use this expanded prompt shape instead of a generic mechanism prompt:

```text
Layout type: key technology scenario + competitiveness page
Top-right segmented navigator: 洞察分析 | 技术构想 | 执行策略, highlight 技术构想 in Huawei red
Title: 关键技术X：<technical mechanism>，<competitive outcome>
Left zone title: <应用场景与诉求>
Left mechanism diagram: <named agents/modules/states/arrows, including step labels>
Left demand boxes:
  诉求一：<demand>; 挑战一：<failure>; 挑战二：<failure>
  诉求二：<demand>; 挑战一：<failure>; 挑战二：<failure>
  诉求三：<demand>; 挑战一：<failure>; 挑战二：<failure>
  诉求四：<demand>; 挑战一：<failure>; 挑战二：<failure>
Right zone title: 关键竞争力目标
Goal capsules: <number + meaning>, <number + meaning>, <number + meaning>
Technical construction items:
  ① <red action headline + outcome>
  • <mechanism name>：<implementation>, <effect/threshold>;
  • <mechanism name>：<runtime/evaluation method>, <effect/threshold>;
  ② ...
Bottom viewpoint: <why this technology becomes a competitive requirement>
```

Bad prompt:

```text
Layout type: 八层架构
Title: 总体架构
Main claim: 四个对象是关键。
```

Good prompt:

```text
Layout: left 62% eight-layer architecture stack, right 32% key object cards, bottom restrained red viewpoint.
Architecture layers from bottom to top: 多端输入采集、事件标准化、上下文快照、意图包解析、权限票据、Agent 路由、执行回执、个性化记忆.
Show red arrows from 意图包 -> 权限票据 -> Agent 路由 -> 执行回执.
Right cards: 意图包=目标/约束/上下文引用; 上下文快照=可授权/可过期/可追溯; 权限票据=最小授权/风险分级; 执行回执=结果/失败原因/下一步确认.
Evidence strip: Apple App Intents, Microsoft Click to Do, Gemini Live screen sharing.
Bottom viewpoint: 没有对象协议，输入法只能做文本增强；有对象协议，输入层才能成为 Agent 控制面。
```

## Competitor Analysis Page Pattern

Use this layout when analyzing products, platforms, startups, or open-source projects:

```text
Title: <competitor route judgment>
Top/Left: 2-3 official screenshots, charts, product diagrams, or source excerpts
Middle/Left: redrawn architecture or principle diagram based on understanding
Right: 3-5 viewpoint bullets, each tied to what the evidence proves
Bottom viewpoint: one strategic judgment or threat/opportunity, preferably as pale-red callout or red left-bar note
Source note: exact source names/URLs or material index ids
```

Rules:

- Original evidence proves what the competitor publicly shows.
- Redrawn diagrams explain what the competitor is technically doing.
- The right side answers "so what should we learn or counter?"
- Final pages are still generated as whole pages by imagegen. If exact official screenshots must appear, use them as image references when supported; otherwise label source evidence clearly and redraw the mechanism instead of fabricating UI screenshots.
- If only web page screenshots are available, label them as page evidence. Do not call them product UI screenshots.

## Narrative Rules

- Do not make an information collage. Every page must answer: "so what?"
- Insight pages carry high information density, but one page should cover one theme only. Do not combine market landscape, competitor analysis, customer analysis, and technology trend on the same slide. Use separate pages such as "友商分析", "技术趋势", "客户需求", and "市场格局"; each page can contain several evidence blocks if they all support the same theme and ladder up to one red judgment.
- Strategy pages are more resolved: usually left visual architecture/flow plus right explanatory text. For target-architecture pages, the right side should first explain **架构竞争力** in several sufficiently developed points; each point should follow "quantified target -> technical lever -> capability/effect". Avoid splitting too early into generic "key technologies / challenges / metrics" blocks unless the slide is explicitly a key-technology or roadmap page.
- When imitating a reference architecture page, extract its layout, writing cadence, hierarchy, typography, and evidence style. Do not copy its domain-specific architecture terms unless those terms belong to the current topic.
- Strategy must visibly inherit the insight. Use repeated terms such as "agent 并发", "版本 DAG", "安全分支", "控制面 QoS" to show continuity.
- Prefer hard, compressed viewpoint language: "分支速度不是终局，agent 规模化需要状态谱系与治理闭环。"
- For technical planning, emphasize the core technologies the team must master and the level needed to be competitive. Do not let the deck become a service catalog.
- When existing internal services or assets are relevant, use them as technical foundations and explicitly state what new capabilities they need. The point is "how to build future competitiveness", not "what services exist today".

## Huawei Red Discipline

Keep the Huawei white/red style, but use red as a precision signal rather than a large emotional block.

- Prefer **dark red** for text accents and arrows, **Huawei red** for thin rules and selected marks, and **pale red** backgrounds for conclusion callouts.
- Avoid large pure-red frames, thick red borders, full red panels, and repeated red rectangles. They look刺眼 and reduce the enterprise report feel.
- Keep red visual area roughly under 5-8% of a dense planning slide. Most structure should be white, light gray, dark gray, and black.
- Replace big red boxes with one of these treatments:
  - 2px top/bottom red rule plus black judgment text.
  - Pale-red callout background with a 1-2px red border.
  - White callout with a 4-6px red left bar.
  - Small red label such as `判断` / `启示` / `风险` followed by black body text.
- Bottom viewpoints should not default to heavy red-outlined boxes. Use a restrained callout unless the slide needs an exceptional warning.
- Chapter tags should be small pale-red pills or gray pills with red text; do not use solid red tags.

## Strategy Writing

The strategy part must be derived from the insight part and answer what to build over the planning horizon.

For each major architecture or key technology page, include:

- **Target capability:** what customer-visible or platform-visible capability must exist.
- **Technical lever:** what mechanism, architecture, algorithm, runtime, governance, or toolchain makes it possible.
- **Quantified competitiveness:** latency, accuracy, cost, scale, reliability, governance coverage, automation rate, recovery time, benchmark score, or adoption metric.
- **Build depth:** what level is table stakes, competitive, and leading.
- **Internal foundation:** which existing services/assets can be reused and what new capability gaps must be filled.

Key technologies should be expanded one page per technology. Each page should explain:

```text
Problem -> mechanism -> architecture position -> hard points -> metrics -> build plan
```

Avoid grouping many hard technologies into one generic "关键技术" page in long decks.

## Technical Design Depth

The strategy section must be deep enough to guide the next phase of technical development. Do not write capability slogans or generic technology labels.

## Key Technology Page Template

For key-technology pages in Huawei technical planning decks, prefer the following reference-derived structure when the slide needs to explain one hard technology in depth.

### Layout

Use a split technical-planning layout:

```text
Top: claim title + small top-right segmented chapter navigator
Left 48-52%: 应用场景与诉求
  - one mechanism/process diagram showing the current task flow or target architecture
  - 3-4诉求 boxes, each with 1-2 concrete challenges
Right 48-52%: 关键竞争力目标
  - 3 metric chips or goal capsules across the top
  - 3-5 numbered technical construction items
Bottom: restrained red conclusion or page number/footer if required
```

The top-right navigator should be a thin segmented tab strip, not a large section label. Example:

```text
洞察分析 | 技术构想 | 执行策略
```

Highlight the current segment with Huawei red fill or red text, keep inactive tabs white/light gray with thin gray borders.

### Left Side: 应用场景与诉求

The left side must make the engineering problem concrete before proposing the solution.

Include:

- a compact diagram of the actual workflow, control loop, data flow, or agent loop
- numbered arrows or step labels that correspond to the诉求 boxes
- 3-4诉求 boxes such as `诉求一：目标锚定`, `诉求二：中断恢复`, `诉求三：环路干预`, `诉求四：路径纠偏`
- each诉求 box includes concrete failure modes or user/engineering pain, not vague needs

Writing pattern:

```text
诉求一：<short demand>
• 挑战一：<specific failure mode>
• 挑战二：<specific failure mode>
```

Good demand examples:

- `诉求一：目标锚定` -> long tasks drift from the initial goal after many steps.
- `诉求二：中断恢复` -> abnormal interruption loses context or wastes recomputation.
- `诉求三：环路干预` -> blind retry falls into repeated tool-call loops.
- `诉求四：路径纠偏` -> wrong-path confidence causes non-convergent execution.

### Right Side: 关键竞争力目标

Start with quantified goal capsules. Each capsule should combine a number and a competitive meaning:

```text
7*24小时 自主工作
100+ Agent 协同开发
1000+ 工具调用 不丢失目标
```

Then write the technical construction items with this exact style:

```text
① <red capability headline，包含动作和竞争目标>
• <bold mechanism name>：<concrete implementation>, <why it works / what it prevents>;
• <bold mechanism name>：<evaluation or runtime method>, <quantified target or acceptance condition>;
```

Rules:

- The red numbered headline is not a module name. It is a capability action plus outcome, such as `元上下文锁定，避免目标漂移`.
- Each bullet starts with a bold technical mechanism name, then uses `：` to explain how it works.
- Prefer verbs such as `固化`, `注入`, `裁剪`, `对齐`, `拦截`, `熔断`, `回滚`, `校验`, `哈希`, `分离`, `恢复`, `路由`.
- Combine mechanism + concrete object + effect. Avoid "提升能力" phrasing.
- Include at least one measurable threshold or operational condition when possible, such as `语义相似度>85%`, `每5-10步`, `毫秒级恢复`, `短时间超阈值`, `7*24小时`.
- End each item with the reliability/competitiveness effect: prevent drift, shorten recovery, break dead loops, reduce wasted tokens, preserve long-horizon goal, or improve task convergence.

Good writing examples:

```text
① 元上下文锁定，避免目标漂移
• 元上下文锁定：将全局目标固化在System prompt或缓存层，作为高权重读取，不随时间推移滑出窗口；
• 目标语义对齐：每隔5-10步将当前状态与初始目标做语义校验，最终产物语义相似度>85%；

② CheckPoint快照，错误恢复时间缩短至毫秒级
• DAG状态图与节点分离：将Agent执行行为组织为有向无环图，走完节点自动拦截并保持状态；
• 提示词状态注入：将执行步骤state/memory作为缓存前置，任务中断重启直接命中；

③ 自适应熔断，打破工具调用死循环
• 行为指纹Hashing：对工具调用参数和结果组合做哈希，滑动窗口检测重复；
• 动态熔断器：特定工具调用次数或耗时超过阈值，启动熔断和备选路由；

④ 跨步回溯，让Agent少走弯路/错路
• 上下文裁剪：评测到异常时，将上下文恢复到错误前步骤；
• 过程反馈信号：把异常总结为结构化信号拼接至上下文，指导Agent重新路由；
```

Weak writing to avoid:

- `构建记忆能力，提升长期任务效果。`
- `加强稳定性，支持复杂任务。`
- `优化Agent执行，减少错误。`
- `建设工具调用平台。`

Rewrite as:

```text
长程目标锚定：将任务目标、约束、验收标准固化为GoalSpec对象，并在每N步做目标对齐校验，目标偏移时触发重规划。
```

For each proposed key technology, include technical design content:

- **Problem definition:** what exact customer/engineering bottleneck this technology solves, why existing approaches fail, and what breaks if it is not built.
- **Module decomposition:** runtime components, control-plane components, data-plane components, storage/index components, evaluation/ops components.
- **Technical principle:** how the mechanism works, not only what business capability it achieves.
- **Data/control flow:** input objects, intermediate states, decision points, tool calls, execution path, output/feedback path.
- **Core objects and interfaces:** schemas, APIs, protocols, tickets, manifests, DAG nodes, events, context objects, policy objects, or memory objects.
- **Algorithms or mechanisms:** retrieval/ranking, planning, routing, scheduling, sandboxing, permission checking, consistency, rollback, evaluation, cost control, or model selection.
- **State management:** what is persisted, what is ephemeral, lifecycle, TTL, versioning, lineage, replay, audit, and conflict handling.
- **Failure and safety design:** guardrails, fallback, human confirmation, risk levels, rollback, observability, and incident handling.
- **Evaluation method:** benchmark, offline test set, online experiment, replay test, red-team test, customer task success metric, or operational metric used to judge whether the technology is good.
- **Quantified targets:** accuracy, latency, throughput, scale, cost, automation rate, human intervention rate, reliability, privacy/governance coverage, benchmark score.
- **Competitive threshold:** table-stakes target, competitive target, and leading target where possible.
- **Engineering plan:** MVP scope, platform dependencies, build milestones, reusable internal assets, new capability gaps, and validation experiments.

Each key-technology slide should have a concrete mechanism diagram, for example:

```text
Input/Event -> Normalization -> Context/State -> Planner/Policy -> Tool/Runtime -> Verification -> Feedback/Memory
```

or a module/interface diagram:

```text
API / Object schema / Control plane / Runtime / Storage / Evaluation / Ops
```

Weak technology claims to avoid:

- `构建多模态能力`
- `提升上下文理解`
- `加强安全治理`
- `优化 Agent 调度`
- `建设评测体系`

Rewrite them as technical mechanisms:

- `多模态事件流：把语音、文本、屏幕、视觉、位置统一为带时间戳、设备态、授权域和置信度的 InputEvent schema。`
- `上下文快照：将屏幕、App 状态、剪贴板、历史意图、用户偏好组织为可引用、可过期、可脱敏的 ContextSnapshot。`
- `权限票据：用最小授权 token 绑定数据范围、动作范围、风险级别、TTL 和回执要求。`
- `执行回执：要求每个 Agent Action 返回结果、证据、失败原因、回滚建议和下一步确认。`

Before generation, audit every key-technology page. If it cannot tell an engineer what modules to build and how they interact, revise the slide brief and prompt.

Every key-technology slide must answer these four questions visibly:

```text
1. 解决什么问题？What bottleneck or failure mode does it remove?
2. 技术原理是什么？What mechanism makes it work?
3. 怎么评价好坏？What benchmark, metric, experiment, or operational signal judges it?
4. 做到什么程度才有竞争力？What quantified table-stakes / competitive / leading targets apply?
```

## Customer, User, and Buy-Point Analysis

For topics affected by coding agents, no-code tools, or general-purpose assistants, include a substitutability analysis:

```text
Can customers self-build this with coding agent + skills?
Can they get similar results with scripts, notebooks, or open source?
What remains hard because of enterprise context, data access, governance, production reliability, integration, cost, evaluation, or scale?
Which remaining hard points are true buy points?
```

Use "买点分析" for the page title when the purpose is willingness-to-pay. Separate:

- **Customer self-build:** low-risk, local, single-user, single-data-source, or simple workflow tasks.
- **Vendor-dependent:** cross-domain, governed, production, auditable, multi-user, high-scale, or high-risk tasks.
- **Paid buy points:** trust, security, integration, automation depth, evaluation, operational guarantees, and business outcome ownership.

## Slide Sequence

A compact technical planning deck usually uses 4-7 pages:

Part 1 **洞察**

1. **行业趋势洞察:** market/category change and why now.
2. **技术趋势洞察:** architecture/benchmark/research trend and the technical inflection.
3. **友商分析:** competitor routes, capability gaps, and strategic opening.
4. **客户需求洞察:** target customers, scenarios, pain points, and purchase/adoption criteria.
5. **洞察总结:** synthesize previous insight pages into the next architecture direction.

Part 2 **策略**

6. **总体构建策略:** the strategic construction thesis and design principles.
7. **总体架构图:** target architecture with architecture competitiveness.
8. **用户场景讲解:** explain key user scenarios against the architecture.
9. **重点模块与关键技术:** module-level mechanisms and hard technical points.
10. **策略总结:** conclusion, roadmap/gates, KPI or investment priorities.

For a short sample, keep the same two-part logic but compress to 5 pages: industry/tech/competitor combined insight, insight summary, overall construction strategy, architecture, strategy summary.

## Page Draft Pattern

Use this compact page brief before creating any slide:

```text
Slide: <number>
Title: <black judgment title>
Subtitle: <scope/context>
Claim: <one sentence, sharp and non-generic>
Proof object: <matrix/chart/architecture/flow/roadmap>
Left side: <visual structure if strategy page>
Right side: <competitiveness/key technologies/implementation text>
Red emphasis: <one phrase or path>
Bottom viewpoint: <one sentence>
```

## Imagegen Prompt Pattern

Use this only for the imagegen route:

```text
Use case: productivity-visual
Asset type: 16:9 full-slide Chinese enterprise technical-planning PPT page, 1920x1080.
Style: Huawei-like white/red technical report, white background, black title, dark gray subtitle, dense but clean management consulting layout, thin gray frames, red only for emphasis and conclusion, no logo, no watermark, no black panels, no gradient glow.
Layout type: <insight matrix | left architecture + right explanation | roadmap | key technology mechanism>
Title in black: <title>
Subtitle in dark gray: <subtitle>
Claim: <one sharp judgment>
Layout zones: <specific left/right/top/bottom structure and proportions>
Main visual: <diagram/table/chart instructions with exact node labels, layers, arrows, rows/columns, metrics, or steps>
Evidence blocks: <2-4 source-backed facts or source labels if insight page>
Right/Bottom explanation: <3-5 concise judgment bullets or technical build bullets>
Bottom viewpoint treatment: restrained Huawei-red callout, preferably pale-red background with thin red border or red left bar; avoid thick red frames and large solid red areas.
Visual density: high-density Huawei technical planning page, 6-12 meaningful content units, avoid sparse layout and oversized empty cards.
Text discipline: all Chinese text must be legible, no fake characters, no title numbering, no page number near title.
```

## Packaging Image Slides

Save generated images with zero-padded filenames:

```text
outputs/<deck-name>/imagegen/images/slide-01.png
outputs/<deck-name>/imagegen/images/slide-02.png
```

Then run:

```bash
python ~/.codex/skills/huawei-tech-planning-ppt/scripts/make_image_pptx.py \
  --images outputs/<deck-name>/imagegen/images \
  --output outputs/<deck-name>/imagegen/<deck-name>-imagegen.pptx
```

If `python-pptx` is missing, do not switch to editable/native PPTX. Either install it:

```bash
python3 -m pip install python-pptx
```

or use an available fallback such as `pptxgenjs` only to place each PNG/JPG full-bleed on a blank 16:9 slide. The fallback PPTX should still contain one full-page image per slide.

## Quality Gates

Before delivery:

- Each slide has one claim, one proof object, and one bottom viewpoint.
- Each non-cover/non-directory slide has concrete page content, not only a title/claim/layout type.
- Each non-cover/non-directory prompt specifies exact visual content: diagram nodes, table labels, evidence blocks, explanation bullets, and bottom judgment.
- Insight pages contain evidence plus judgment, not raw information lists.
- Strategy pages use left visual/right explanation unless another structure is clearly better.
- Strategy and key-technology pages contain architecture/mechanism diagrams with enough labels to explain how the system works.
- Key-technology pages are technical-design-grade: they show the problem being solved, modules, interfaces/objects, flow, mechanisms, state, failure handling, evaluation method, quantified targets, competitive threshold, and development implications.
- Normal content boxes use gray outlines; red is reserved for thesis, arrows, selected labels, and restrained conclusion treatments.
- Red must feel like Huawei-style emphasis, not a warning poster: avoid thick red boxes, solid red panels, and overusing red on every container.
- No colored title, no black title panel, no decorative gradient/orbs, no fake Huawei logo.
- Imagegen output: inspect generated images; reject slides with garbled Chinese or unreadable small labels.
- Contact sheet inspection rejects sparse pages, text-light pages, pages without real proof objects, and pages with excessive empty whitespace.
- Final PPTX pages are image-based full-slide pages; do not silently substitute native editable PPT shapes.
- Delivery summary includes PPTX, contact sheet, source workspace, reusable materials, slide plan, prompt files, and iteration instructions.
