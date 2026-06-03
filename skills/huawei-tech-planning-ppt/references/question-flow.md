# Huawei Tech Planning PPT Question Flow

Use this when the user has not already provided a clear writing scope. Ask in stages; do not dump the whole list.

## Stage 1: Frame

Ask enough to establish:

- Topic: What technical planning topic is the deck about?
- Audience: executive review, architecture committee, product planning, customer-facing, or internal R&D?
- Output size: short 7-12 page storyline or full 30-40 page deck?
- Delivery route: imagegen style sample, editable PPTX, or hybrid?
- References: are there Huawei-style sample pages, product docs, benchmark results, or source links?

Default if unclear:

```text
我先按“洞察分析 + 技术构想 + 执行策略”的三段式结构做一版提纲，并在封面后加总体目录页，之后再收敛。
```

## Stage 2: Insight Agenda

The insight part should normally cover four themes plus a summary:

- 行业趋势洞察
- 技术趋势洞察
- 友商分析
- 客户需求洞察
- 强场景/切入场景筛选
- 洞察总结

Each page is one theme. Ask:

- Industry trend: What category shift, market timing, policy/ecosystem, or adoption wave matters?
- Competitors: Which vendors/projects must be analyzed? If unknown, propose a reasonable list.
- Reports/sources: Which consulting firms, papers, official docs, benchmark reports, or analyst reports matter?
- Technology trends: Which technical changes should be tested as trends?
- Customer scope: Which customer types or scenarios are target customers?
- Strong scenario wedge: Which concrete workflow, user task, or failure mode creates the strongest need?
- Existing hypothesis: What conclusion does the user suspect but wants validated?

Default agenda pattern:

- 友商分析: representative incumbents, cloud/platform vendors, startups, and open-source routes.
- 技术趋势: architecture shifts, benchmarks, standards/protocols, academic signals, and engineering constraints.
- 客户需求: target user workflows, pain points, adoption blockers, self-build boundary, willingness-to-pay.
- 强场景筛选: long-running, high-value, multi-step, governed, auditable, or recovery-sensitive scenarios.
- 洞察总结: why the category is shifting and what system requirements follow.

## Stage 3: Insight Research

After the user confirms the insight agenda:

- Search the web for current sources.
- Prefer official docs, papers, benchmark reports, analyst/consulting reports, and reputable technical posts.
- Save useful screenshots/materials under `outputs/<deck-name>/research/`.
- Write `sources.md` with title, URL, date/access date, why it matters, and likely slide.
- Convert sources into one-theme claims before proposing slides.

Ask only if needed:

- Are screenshots from source pages acceptable as PPT material, or should they be redrawn?
- Are there private/internal sources the user wants to include before web-only research?

## Stage 4: Technical Construction and Execution Agenda

The technical-construction part should normally cover:

- 总体构想 / 构建原则
- 总体架构图
- 目标对象 / 核心 API / 关键模块
- 关键技术（一页一个技术）
- 技术构想总结 / 指标体系

The execution-strategy part should normally cover:

- 改造对象与现有基础
- 关键改造项
- 集成路径与阶段计划
- 验证方案 / 评测集 / 故障注入
- 路线图 / 风险取舍 / 策略总结

Ask:

- Target architecture: Is there an existing architecture to inherit or should the deck propose a new one?
- Differentiators: What must be stronger than competitors?
- Quantified targets: concurrency, latency, p95/p99, cost, cleanup SLA, masking coverage, availability, scale.
- Key technologies: which mechanisms are allowed or preferred?
- User scenarios: Which user workflows should be explained against the architecture?
- Modification target: which existing product, codebase, platform, workflow, or service should the execution strategy build on?
- Validation: which benchmark, task set, fault injection cases, pilot workflow, or acceptance rubric should prove success?
- Strategy summary: Should the final page focus on roadmap, investment priorities, KPIs, or executive ask?
- Roadmap: short/mid/long horizon and release constraints, if roadmap is part of the strategy summary.
- Governance: audit, compliance, security, cost, quota, lifecycle, operations.

Good architecture-competitiveness wording:

```text
<量化目标/范围>：通过<关键技术/模块组合>，实现<能力效果/竞争力>。
```

## Stage 5: Outline Approval

Return a three-part outline:

```text
封面
总体目录

Part 1 洞察分析
1. 行业趋势洞察 - <claim>
2. 技术趋势洞察 - <claim>
3. 友商分析 - <claim>
4. 客户需求洞察 - <claim>
5. 强场景筛选 - <claim>
6. 洞察总结 - <claim>

Part 2 技术构想
7. 总体构想 - <claim>
8. 总体架构图 - <claim>
9. 关键技术一 - <claim>
10. 技术构想总结 / 指标体系 - <claim>

Part 3 执行策略
11. 改造对象与现有基础 - <claim>
12. 关键改造项 - <claim>
13. 验证方案 - <claim>
14. 路线图 / 风险取舍 / 策略总结 - <claim>
```

Ask for approval before slide generation:

```text
这个提纲如果方向对，我下一步会逐页写 slide brief，再生成样页/整套 PPT。
```

## Stage 6: Slide Brief Questions

Only ask follow-ups where missing information would materially change the slide:

- For competitor pages: exact competitors, comparison dimensions, desired conclusion.
- For trend pages: target papers/reports, benchmark dimensions, time horizon.
- For customer pages: customer segment, pain point, adoption blocker, decision criteria.
- For overall construction strategy: design principles, target category, strategic positioning, quantified objectives.
- For architecture pages: layer names, module names, target metrics, constraints.
- For user scenario pages: persona, trigger, workflow, architecture modules involved, success metric.
- For key module pages: module boundary, mechanism, dependency, technical risk, validation metric.
- For execution pages: modification target, existing foundation, integration points, rollout phases, risk controls.
- For validation pages: benchmark/task set, fault injection, baseline comparison, acceptance threshold.
- For roadmap pages: phase length, release names, must-hit milestones, KPI gates.
