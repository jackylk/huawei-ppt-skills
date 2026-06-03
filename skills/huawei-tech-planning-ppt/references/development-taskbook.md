# Development Taskbook Workflow

Use this reference when the user wants to turn a technical planning PPT into real Codex development work.

## Purpose

The taskbook is not a summary of the PPT. It is an engineering handoff that converts the planning artifacts into executable work for a fresh Codex session.

Write it under the same project workspace:

```text
outputs/<deck-name>/planning/codex-dev-taskbook.md
```

Use a target-specific name when there are multiple implementation tracks:

```text
outputs/<deck-name>/planning/codex-dev-taskbook-<repo-or-system>.md
```

## Inputs To Read

Start from the accumulated PPT workspace:

```text
research/synthesis.md
research/five-lens-analysis.md
research/deep-research-matrix.md
research/source-registry.json
planning/core-claims.md
planning/insight-claims.md
planning/strategy-claims.md
planning/requirements-to-tech.md
planning/slide-plan.md
planning/*implementation*
planning/*architecture*
planning/*evaluation*
```

Read only the files that exist and matter. If target repositories are provided, inspect:

```text
git status --short --branch
top-level files and package manifests
relevant src/test directories
existing API/model/service/module names
existing test commands or CI hints
```

Do not modify the target code repositories while writing the taskbook unless the user explicitly asks for implementation in the same turn.

## Required Structure

Use this structure by default:

```text
# Codex 开发任务书：<topic / system / MVP name>

## 0. 任务书用途
Explain that this file is for a fresh Codex session to continue from the PPT planning output into real development.

## 1. 开发目标
State the sharp MVP goal, wedge scenario, and why this is the right first implementation slice.

## 2. 规划依据
List the most relevant PPT workspace files and the planning conclusions being converted into development tasks.

## 3. 相关代码仓库 / 现有系统
List target repositories, current branch/status summary, and important files/modules discovered.

## 4. MVP 范围
Define what is in scope, out of scope, and what must be proven by the first version.

## 5. 目标对象模型 / API / 数据流
Name concrete objects, records, APIs, state transitions, data flows, and integration boundaries.

## 6. 开发任务拆解
Split by repo/module/system. Each task should include why it exists, files likely affected, expected behavior, and tests.

## 7. 集成任务
Describe cross-repo adapters, protocols, state synchronization, compatibility constraints, and integration tests.

## 8. 推荐实施顺序
Use phases. Each phase should have entry condition, work items, output artifact, tests, and acceptance gate.

## 9. 验收标准
State measurable acceptance criteria. Include functional correctness, reliability, traceability, governance, performance, or benchmark targets as appropriate.

## 10. 风险与待确认问题
Separate coding risks, product/architecture risks, dependency risks, and user decisions needed.

## 11. 给后续 Codex 的启动提示
Provide a copyable prompt that points to this taskbook and tells Codex how to start safely.
```

## Writing Standard

The taskbook must be concrete enough to execute:

- Name target repos and paths when known.
- Name expected objects, interfaces, modules, adapters, stores, validators, or commands.
- Convert each key technology into an implementation unit, not a slogan.
- Include tests or smoke checks for every phase.
- Include acceptance gates with measurable outcomes.
- Tell the next Codex to inspect `git status` and avoid overwriting unrelated user changes.
- If the target repo is dirty, state that clearly and instruct the next Codex to work with existing changes.

Avoid:

- generic instructions such as "build the architecture"
- restating slide titles without implementation steps
- asking Codex to redo all research before coding
- hiding unresolved assumptions
- claiming a repo capability exists unless it was inspected or is clearly marked as a planning assumption

## Copyable Prompt Pattern

End with a prompt like:

```text
请根据 <absolute-path-to-taskbook> 做实际开发。

目标是在 <repo paths> 中实现 <MVP name>：
1. 先审计目标 repo 的 git status，不要覆盖已有未提交改动。
2. 先做 Phase 0 implementation plan，列出要改哪些文件、测试怎么跑、哪些风险需要我确认。
3. 第一阶段优先实现 <narrow MVP slice>，不要一上来做完整平台化能力。
4. 所有实现必须有可运行测试或 smoke test。
5. 每完成一个 phase，更新任务书或生成 phase report。
```

## Delivery Summary

When delivering the taskbook, tell the user:

- taskbook path
- which PPT workspace files were used
- which repos were inspected
- whether any code was modified
- the exact copyable prompt for a fresh Codex session
