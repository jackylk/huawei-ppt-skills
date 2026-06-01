# Global Tech Strategy PPT Question Flow

Use this when the user has not already provided a clear writing scope. Ask in stages; do not dump the whole list.

## Stage 1: Frame

Ask enough to establish:

- Topic: What technical planning topic is the deck about?
- Audience: executive review, architecture committee, product planning, customer-facing, or internal R&D?
- Output size: short 5-10 page storyline or full 30-40 page planning deck?
- Delivery route: full-page imagegen slides assembled into PPTX.
- References: are there global strategy/consulting-style sample pages, product docs, benchmark results, or source links?

Default if unclear:

```text
我先按“洞察 15-20 页 + 策略 15-20 页”的结构做一版深度技术规划提纲，之后再收敛。
```

## Stage 2: Insight Agenda

The insight part should normally cover four themes plus a summary:

- 行业趋势洞察
- 技术趋势洞察
- 友商分析
- 客户需求洞察
- 洞察总结

Each page is one theme. Ask:

- Industry trend: What category shift, market timing, policy/ecosystem, or adoption wave matters?
- Competitors: Which vendors/projects must be analyzed? If unknown, propose a reasonable list.
- Reports/sources: Which consulting firms, papers, official docs, benchmark reports, or analyst reports matter?
- Technology trends: Which technical changes should be tested as trends?
- Customer scope: Which customer types or scenarios are target customers?
- Existing hypothesis: What conclusion does the user suspect but wants validated?

Default Agentic DB agenda:

- 友商分析: Neon, Xata, Supabase, PlanetScale, Turso, Doltgres/Dolt.
- 技术趋势: branchable databases, version DAG, agent sandbox, diff/merge, masking, control-plane QoS, benchmark.
- 客户需求: AI coding platforms, enterprise CI/CD, database DevOps, production-data sandboxing.
- 洞察总结: why the category shifts from database branching to agent database workspace.

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

## Stage 4: Strategy Agenda

The strategy part should normally cover:

- 总体构建策略
- 总体架构图
- 用户场景讲解
- 重点模块与关键技术
- 策略总结

Ask:

- Target architecture: Is there an existing architecture to inherit or should the deck propose a new one?
- Differentiators: What must be stronger than competitors?
- Quantified targets: concurrency, latency, p95/p99, cost, cleanup SLA, masking coverage, availability, scale.
- Key technologies: which mechanisms are allowed or preferred?
- User scenarios: Which user workflows should be explained against the architecture?
- Strategy summary: Should the final page focus on roadmap, investment priorities, KPIs, or executive ask?
- Roadmap: short/mid/long horizon and release constraints, if roadmap is part of the strategy summary.
- Governance: audit, compliance, security, cost, quota, lifecycle, operations.

Good architecture-competitiveness wording:

```text
<量化目标/范围>：通过<关键技术/模块组合>，实现<能力效果/竞争力>。
```

## Stage 5: Outline Approval

Return a two-part outline:

```text
Part 1 洞察
1. 行业趋势洞察 - <claim>
2. 技术趋势洞察 - <claim>
3. 友商分析 - <claim>
4. 客户需求洞察 - <claim>
5. 洞察总结 - <claim>

Part 2 策略
6. 总体构建策略 - <claim>
7. 总体架构图 - <claim>
8. 用户场景讲解 - <claim>
9. 重点模块与关键技术 - <claim>
10. 策略总结 - <claim>
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
- For roadmap pages: phase length, release names, must-hit milestones, KPI gates.
