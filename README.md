# Huawei PPT Skills

这是四个可复用的中文 PPT skills，适合在 Codex 中做企业汇报页、技术规划页、架构页、概念故事页和 imagegen 图片页 PPTX。

如果这个仓库对你或同事有帮助，欢迎顺手点一个 Star，不要吝啬 ：）

## 包含的 Skill

- `huawei-style-ppt`：通用华为风格白/红/灰企业汇报页，适合做管理汇报、架构说明、能力矩阵、路线图等。
- `huawei-tech-planning-ppt`：深度技术规划 PPT，强调“洞察 -> 策略”，包含深度调研、友商分析、客户/买点分析、关键技术展开、源码工作区和迭代修改流程。
- `global-tech-strategy-ppt`：全球科技战略咨询风技术规划 PPT，继承 `huawei-tech-planning-ppt` 的叙事、调研和写作结构，但视觉风格改为国际咨询/科技战略报告风，适合高密度市场洞察、技术趋势、竞品路线、架构规划和 2-3 年技术投资决策。
- `designer-toy-concept-ppt`：原创潮玩盲盒概念风 PPT，保持“洞察 -> 策略”的叙事结构，但默认中低信息密度，用原创潮玩角色、盲盒卡片、玩具实验室、能力货架等视觉表达概念、用户场景和产品愿景；可选 Open Peeps/OpenMoji/Twemoji/Blush 等开放素材，但不自动生成或仿制具体商业 IP。

## 如何在 Codex 中安装

> 请帮我安装这个 Codex skill 仓库：https://github.com/jackylk/huawei-ppt-skills 。如果我有访问权限，请 clone 到本地，把 `skills/huawei-style-ppt`、`skills/huawei-tech-planning-ppt`、`skills/global-tech-strategy-ppt` 和 `skills/designer-toy-concept-ppt` 复制到 `~/.codex/skills/`，安装 `python-pptx` 依赖，然后告诉我需要重启 Codex 才能使用。

前提：这个仓库当前是私有仓库，同事需要先获得 GitHub 访问权限，并且本机 `git` 能拉取该仓库。

## Codex 手工安装

```bash
git clone https://github.com/jackylk/huawei-ppt-skills.git
mkdir -p ~/.codex/skills
cp -R huawei-ppt-skills/skills/huawei-style-ppt ~/.codex/skills/
cp -R huawei-ppt-skills/skills/huawei-tech-planning-ppt ~/.codex/skills/
cp -R huawei-ppt-skills/skills/global-tech-strategy-ppt ~/.codex/skills/
cp -R huawei-ppt-skills/skills/designer-toy-concept-ppt ~/.codex/skills/
python3 -m pip install python-pptx
```

安装后重启 Codex，让 Codex 重新发现 skills。

## Codex 使用示例

```text
Use $huawei-style-ppt 做一个华为风格企业汇报 PPT。
```

```text
Use $huawei-tech-planning-ppt 帮我做一个 XXX 主题的技术规划 PPT，30-40 页，必须用 imagegen 生成整页高信息密度图片页并合成 PPTX。请先问我写作方向、调研重点、已有观点、信息密度和决策用途；调研要充分，观点要犀利，策略要能指导未来 2-3 年技术构建，关键技术页要写到技术设计级别，包括要解决的问题、技术原理、模块/接口/流程、评价方法和量化目标。
```

```text
Use $global-tech-strategy-ppt 帮我做一个 XXX 主题的技术规划 PPT，30-40 页，必须用 imagegen 生成整页高信息密度图片页并合成 PPTX。叙事结构保持“洞察 -> 策略”，请先问我写作方向、调研重点、已有观点、信息密度和决策用途；调研要充分，观点要犀利，视觉风格采用全球科技战略咨询报告风。
```

```text
Use $designer-toy-concept-ppt 帮我做一个 XXX 主题的概念 PPT，保持“洞察 -> 策略”的叙事结构，用 imagegen 生成整页图片页并合成 PPTX。视觉采用原创潮玩盲盒角色 + 可选开放授权素材，中低信息密度，每页一个主观点、一个主视觉和 2-4 个信息块。
```

## Claude Code 是否能用

可以用，但能力边界不同：

- Codex：可以完整使用，包括 imagegen 生成图片页、整理素材、打包 PPTX。
- Claude Code：可以用于调研、观点提炼、slide plan 和 imagegen prompt 编写；如果没有图像生成工具，不能完整生成图片页。

Claude Code 手工安装：

```bash
git clone https://github.com/jackylk/huawei-ppt-skills.git
mkdir -p ~/.claude/skills
cp -R huawei-ppt-skills/skills/huawei-style-ppt ~/.claude/skills/
cp -R huawei-ppt-skills/skills/huawei-tech-planning-ppt ~/.claude/skills/
cp -R huawei-ppt-skills/skills/global-tech-strategy-ppt ~/.claude/skills/
cp -R huawei-ppt-skills/skills/designer-toy-concept-ppt ~/.claude/skills/
```

## PPTX 打包依赖

技术规划类 skill 带有 `scripts/make_image_pptx.py`，用于把一组 `slide-01.png`、`slide-02.png` 图片页打包成 16:9 PPTX。

依赖：

```bash
python3 -m pip install python-pptx
```

## 技术规划 PPT 的迭代工作区

`huawei-tech-planning-ppt`、`global-tech-strategy-ppt` 和 `designer-toy-concept-ppt` 都会要求生成可复用的源码工作区，而不是只给一个最终 PPTX：

```text
outputs/<deck-name>/
  research/   # 原始资料、摘录、截图、产品截图、素材索引、研究综合
  planning/   # deck outline、洞察观点、策略观点、slide plan
  prompts/    # 每页 imagegen 输入，如 slide-12.md
  images/     # 生成后的每页图片
  output/     # PPTX 和 contact sheet
```

用户可以看和改：

- `research/material-index.md`：素材和来源索引
- `planning/slide-plan.md`：每页观点、证据和版式
- `prompts/slide-XX.md`：某页 imagegen 输入

如果只改某一页，可以让 Codex 只重生成该页并重建 PPTX。  
如果补充新的客户分析、技术趋势或友商信息，可以让 Codex 做增量调研，并合并到已有 `research/` 和 `planning/` 目录中。
