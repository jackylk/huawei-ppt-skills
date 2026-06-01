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
   - For rapidly changing topics, research recent product releases, conference announcements, roadmap signals, X posts by company leaders/key engineers, startup launches, open source projects, academic papers, customer pain points, consulting reports, and investor views.
   - Preserve reusable source material under a stable research directory: raw pages, extracted text, screenshots, product screenshots, chart images, quote snippets, and a material index. Future revisions should enrich this repository rather than restart research.
   - Separate page screenshots from true product screenshots. Product screenshots must come from official docs, official blogs, demos, or other attributable sources. Do not let image generation invent competitor product UIs.
   - For competitor/technology pages, first understand the architecture and mechanism, then redraw the key technical principle in the deck. Use original screenshots as evidence and the redrawn diagram as interpretation.
   - Treat research and slide writing as auditable artifacts. Save synthesis notes, slide claims, and imagegen prompts in reviewable Markdown/JSON files so the user can inspect or edit them before regeneration.
   - Do not treat a quick web scan or a list of major vendors as "deep research". For long-form planning decks, Stage 3 must pass the research sufficiency gate below before writing the final outline or claiming the insight work is complete.
   - Update the visible plan when each research group is completed: vendors, conferences, papers, open source, customer/user evidence, investor/analyst views, and leader/key-person viewpoints.

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

### Stage 7: Generate

   - Choose editable, imagegen, or hybrid route.
   - For imagegen decks, write one prompt file per slide before generation. Use stable filenames such as `prompts/slide-01.md` or `prompts/slide-01.json`.
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
- `research/synthesis.md` contains evidence-backed viewpoints, not only summaries.
- `planning/insight-claims.md` maps each core viewpoint to evidence from at least two source types where possible.
- Competitor pages have official screenshots/charts or clearly labeled page evidence plus redrawn architecture/mechanism diagrams.

If research is not sufficient, say so explicitly and continue researching. Do not imply the deck is substantially done. Use wording like:

```text
当前只是第一轮方向性调研，还没有达到深度技术规划标准。下一步我会补齐：竞品/云厂商/startup/学术开源/客户买点/投资观点/关键人物观点，并把证据合并到现有 research 目录。
```

For a user who asks "都做了调研了吗" or challenges depth, audit the research against this gate and list what is complete, what is missing, and what you will research next.

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

## Output Route

Choose one route before building:

- **Editable PPTX route:** Use for serious delivery, text accuracy, review cycles, or dense Chinese content. Build native PowerPoint shapes, text, tables, and diagrams. Imagegen may be used only for visual references.
- **Imagegen route:** Use for quick style exploration, visual concept pages, or when the user explicitly asks for generated slide images. Keep Chinese text short because imagegen may distort small text.
- **Imagegen evidence route:** When the user asks for imagegen but the deck contains competitor evidence, generate the slide layout, rewritten architecture/principle diagram, and judgment area with imagegen; then composite official screenshots/charts into reserved placeholders. Do not use imagegen to fabricate product UI screenshots.
- **Hybrid route:** Generate a visual reference page, then rebuild all critical Chinese text and diagrams as editable PPT objects.

If the user asks to compare imagegen and non-imagegen output, produce both with the same claim spine and slide titles so the tradeoff is visible.

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
- For imagegen decks, ask imagegen to create empty screenshot frames and the redrawn mechanism; paste official screenshots afterward.
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
Main visual: <diagram/table/chart instructions>
Right/Bottom explanation: <short Chinese text blocks only>
Bottom viewpoint treatment: restrained Huawei-red callout, preferably pale-red background with thin red border or red left bar; avoid thick red frames and large solid red areas.
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

## Quality Gates

Before delivery:

- Each slide has one claim, one proof object, and one bottom viewpoint.
- Insight pages contain evidence plus judgment, not raw information lists.
- Strategy pages use left visual/right explanation unless another structure is clearly better.
- Normal content boxes use gray outlines; red is reserved for thesis, arrows, selected labels, and restrained conclusion treatments.
- Red must feel like Huawei-style emphasis, not a warning poster: avoid thick red boxes, solid red panels, and overusing red on every container.
- No colored title, no black title panel, no decorative gradient/orbs, no fake Huawei logo.
- Editable route: key text remains editable and Chinese text fits inside boxes.
- Imagegen route: inspect generated images; reject slides with garbled Chinese or unreadable small labels.
- Delivery summary includes PPTX, contact sheet, source workspace, reusable materials, slide plan, prompt files, and iteration instructions.
