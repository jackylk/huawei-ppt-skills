---
name: designer-toy-concept-ppt
description: "Use when the user asks for cute designer-toy, blind-box, cartoon, soft mascot, or playful concept PPTs with Chinese insight-to-strategy structure, imagegen-generated full-slide pages, original mascots, and optional openly licensed illustration assets."
---

# Designer Toy Concept PPT

Use this skill for Chinese concept decks that keep the same **洞察 -> 策略** narrative discipline as a technical planning deck, but change the visual style to **原创潮玩盲盒角色 + 可选开放授权插画素材**.

This skill is for lower-to-medium density concept storytelling, product vision, innovation proposal, user scenario, and strategy communication decks. It is not the default for rigorous architecture committee or high-density technical design review.

Core narrative pattern:

```text
行业/技术/用户/竞争洞察 -> 洞察总结 -> 产品/技术构建策略 -> 场景故事 -> 轻架构/能力地图 -> 路线图/行动建议
```

Default length:

```text
Short concept deck: 8-12 pages
Medium concept strategy deck: 15-24 pages
Long narrative deck: 25-30 pages only when requested
```

The deck may keep the two major parts:

```text
Part 1 洞察
Part 2 策略
```

For long decks, add a small top-right chapter tag such as `洞察 / 用户场景` or `策略 / 能力地图`.

## Visual Identity

Use an original cute designer-toy/blind-box inspired visual language.

Reference feel:

- collectible designer toy display, blind-box packaging, toy shelf, soft vinyl, clay-like 3D, rounded mascot cards
- friendly product concept keynote, playful strategy storyboard, cute information graphic
- Open Peeps / OpenMoji / Twemoji / Blush-style friendly illustration assets when appropriate and license-compatible

Visual principles:

- **Characters:** use original mascots only. They can be round-headed, soft-vinyl, collectible, expressive, and playful, but must not copy a specific commercial IP.
- **Density:** low-to-medium by default. One main idea per page, one main visual, 2-4 supporting info blocks.
- **Content ratio:** 60-70% concept/diagram/story, 20-30% mascot or cute visual, 10% decorative stickers or labels.
- **Palette:** cream white, mint green, sky blue, soft lavender, coral pink, butter yellow, warm gray, with dark slate text for readability.
- **Shapes:** rounded cards, toy labels, small stickers, capsule tags, shelf compartments, soft shadows, gentle outlines.
- **Diagrams:** use playful system maps, scene flows, capability cards, journey maps, light architecture diagrams, roadmap islands, and character-led scenario panels.
- **Typography:** friendly but legible. Avoid childish handwriting for core content. Titles can be warm and expressive; body text remains crisp Chinese.

Avoid:

- dense consulting-page grids unless the user explicitly asks for higher density
- low-readability pastel text
- full-page toy illustration with no strategy content
- copying any commercial character, packaging, logo, face, costume, silhouette, or signature motif
- generating fake official screenshots, logos, or branded merchandise

## IP And Asset Rules

Do not generate or imitate specific commercial IP characters such as Labubu, Molly, Pop Mart characters, Disney characters, Pokemon, Doraemon, or other identifiable copyrighted/trademarked characters.

Allowed:

- Generate **original** designer-toy mascots.
- Use public/open illustration systems when license-compatible and attribution requirements are handled.
- Use user-provided images of commercial IP only if the user explicitly says they have the right to use them. In that case, place or reference the supplied image as material; do not generate a copycat variation.
- Say clearly in the workspace/material index when an asset is user-provided, open-source, or generated original art.

Suggested wording in prompts:

```text
Original cute designer-toy mascot, blind-box inspired, soft vinyl texture, round head, friendly expression, pastel collectible-toy feel. Do not resemble or reference any existing commercial character or brand.
```

For user-provided authorized commercial-IP images:

```text
Use the user-provided authorized image as a placed reference/material only. Do not generate a new imitation of the character. Keep source attribution in research/material-index.md.
```

## Optional Open Asset Sources

When the user asks for existing reusable cartoon assets, prefer these classes:

- **Open Peeps:** hand-drawn people, CC0-style public-use positioning. Good for friendly human roles.
- **OpenMoji:** emoji/icon character system. Check CC BY-SA 4.0 attribution/share-alike implications.
- **Twemoji:** emoji graphics. Check CC BY 4.0 attribution for graphics.
- **Blush:** illustration marketplace/library. Check the selected asset/license before reuse.
- **unDraw:** flat illustration assets. Good for simple concept pages, less toy-like.

Do not assume every downloaded illustration is unrestricted. Save source URL, license note, and attribution requirements under `research/material-index.md`.

## Interaction Contract

Before creating slides, ask 2-4 concise questions with options unless the user already specified direction.

Required choices:

```text
1. 风格强度
   A. 专业可爱平衡（推荐）：潮玩角色只做引导，主体仍是图表/场景
   B. 更可爱：角色更大，适合产品愿景/路演
   C. 更专业：只用少量贴纸和柔和视觉，不突出角色

2. 信息密度
   A. 中低密度（推荐）：每页 1 个观点 + 1 个主视觉 + 2-4 个信息块
   B. 中密度：每页 1 个观点 + 1 个图表/流程 + 4-6 个信息块
   C. 低密度：大主视觉 + 极少文字，适合宣讲

3. 素材策略
   A. 全部原创 imagegen 角色（推荐）
   B. 原创角色 + 开放授权素材
   C. 使用用户提供且确认有权使用的图片素材

4. 决策用途
   A. 创新概念/产品愿景（推荐）
   B. 用户场景故事
   C. 内部立项/路演
   D. 对外演示/课程学习
```

If the user says to proceed, use defaults: professional-cute balance, medium-low density, original imagegen mascots, concept/product-vision use.

## Workflow

Maintain an auditable workspace:

```text
outputs/<deck-name>/
  research/
    material-index.md
    source-registry.json
    license-notes.md
    user-provided-assets/
  planning/
    deck-outline.md
    storyboard.md
    slide-plan.md
  prompts/
    slide-01.md
  images/
    slide-01.png
  output/
    <deck-name>.pptx
    contact-sheet.png
```

### Stage 1: Frame

- Confirm topic, audience, page count, style strength, information density, and asset strategy.
- Keep **洞察 -> 策略** as the default narrative.
- If the user asks to reuse a commercial IP, explain the asset rule: user-provided authorized material can be used as placed material; do not generate or imitate commercial IP.

### Stage 2: Insight And Story

- Keep the reasoning serious even when the visuals are cute.
- Convert research into a short viewpoint spine: 4-6 core claims for long decks, 2-4 for short decks.
- Use user scenes and pain points more heavily than dense competitor tables.
- For technical topics, still include architecture/capability pages, but draw them as friendly maps or labs rather than dense engineering blueprints.

### Stage 3: Slide Plan

Each slide brief must include:

```text
Slide number
Chapter tag
Title
One-sentence claim
Main visual metaphor: toy shelf / character scene / map / lab / journey / capability cards
Mascot role: guide / user / engineer / operator / data steward / none
Supporting info blocks: 2-4 concise blocks
Bottom takeaway
Asset rule: original generated / open asset / user-provided authorized
```

### Stage 4: Imagegen Prompts

Generate each final slide as one full-slide imagegen PNG. This skill has one output path: **full-page imagegen slides assembled into PPTX**.

Each prompt must specify:

```text
Use case: productivity-visual
Asset type: 16:9 full-slide Chinese cute designer-toy concept PPT page, 1920x1080
Style: original designer-toy blind-box inspired concept report, pastel, soft vinyl mascot, rounded cards, playful but readable
IP rule: original mascot only, do not resemble any existing commercial character or brand
Title / subtitle / chapter tag
Claim
Main visual
Mascot role and appearance
Supporting blocks
Bottom takeaway
Text legibility requirements
```

### Stage 5: Generate And Package

- Use imagegen for every final slide.
- Save prompts under `prompts/slide-XX.md`.
- Copy generated images into `images/slide-XX.png`.
- Package full-bleed image slides into a 16:9 PPTX using `scripts/make_image_pptx.py`.
- Generate a contact sheet and inspect for: text readability, style consistency, non-infringing original characters, and enough content to carry the point.

### Stage 6: Iterate

- If the user edits a prompt, regenerate only that slide and rebuild PPTX/contact sheet.
- If the user changes the story or claims, update `planning/storyboard.md` and affected prompts first.
- Preserve prior versions unless the user asks to overwrite.

## Slide Patterns

### 1. Toy-Lab Cover

Use a large original mascot in a toy-lab or display-shelf environment. Surround it with 3-5 concept labels. Keep title strong and readable.

### 2. Blind-Box Agenda

Use blind-box cards or toy compartments as agenda modules. Each compartment has one chapter, one small icon, and one short phrase.

### 3. Character Scenario Storyboard

Use 3-4 panels showing a user pain point, agent assistance, system capability, and outcome.

### 4. Capability Shelf

Use a toy shelf or capsule display where each item is a capability: context, tools, governance, memory, evaluation, workflow, operations.

### 5. Friendly Architecture Map

Use a simplified system map with 4-6 layers or zones. Keep technical labels real, but make the visual approachable.

### 6. Roadmap Islands

Use three islands or toy stations for phases: now / next / future, or 2026 / 2027 / 2028. Add 2-3 milestones per phase.

## Example Prompt

```text
Use case: productivity-visual
Asset type: 16:9 full-slide Chinese cute designer-toy concept PPT page, 1920x1080.
Style: original designer-toy blind-box inspired concept report, pastel cream background, rounded cards, soft vinyl mascot, toy shelf layout, playful but professional, crisp Chinese typography.
IP rule: original mascot only; do not resemble or reference Labubu, Molly, Pop Mart, Disney, Pokemon, Doraemon, or any existing commercial character or brand.
Title: Agent 时代的数据工作台
Chapter tag: 洞察 / 场景
Claim: 用户不想要更多聊天窗口，而想要一个能把任务安全做完的工作台。
Main visual: a toy-lab control desk with four rounded capability stations: 上下文, 工具, 权限, 回执.
Mascot: original small data-agent toy guide, round head, soft vinyl, mint jacket, holding a tiny dashboard tablet; no recognizable IP traits.
Supporting blocks: 业务用户=问指标和归因; 数据工程师=生成和验证任务; 治理管理员=审批和审计; 运维人员=告警和复盘.
Bottom takeaway: 可爱视觉降低理解门槛，但页面仍然表达清楚系统能力和策略判断。
Text: all Chinese text must be legible, no fake characters, no watermark.
```

## Quality Gates

Before delivery:

- Narrative still follows **洞察 -> 策略**.
- Every slide has one clear claim.
- Cute characters support the point; they do not replace the point.
- No generated character resembles a specific commercial IP.
- Text is legible and not garbled.
- Page density matches the user's selected density.
- Prompts, images, contact sheet, and PPTX are all saved in the workspace.
- Delivery summary explains where the user can inspect/edit prompts and how to regenerate selected pages.

