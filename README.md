# Huawei PPT Skills

Two reusable AI skills for creating Huawei-style Chinese enterprise PPTs.

## Skills

- `huawei-style-ppt`: general Huawei-style white/red enterprise report slides, slide images, and PPTX packaging.
- `huawei-tech-planning-ppt`: deep technical planning decks with insight-to-strategy structure, research workspace, competitor analysis, customer/buy-point analysis, per-slide imagegen prompts, and iterative revision workflow.

## Recommended Use

Use **Codex** for the full workflow because these skills can rely on `imagegen` to create slide images.

Claude Code can still use the skills for research, outlines, slide plans, and image prompts, but it cannot complete image generation unless your environment provides a separate image-generation tool.

## Install For Codex

Clone the repo and copy the skill folders into your Codex skills directory:

```bash
git clone https://github.com/jackylk/huawei-ppt-skills.git
mkdir -p ~/.codex/skills
cp -R huawei-ppt-skills/skills/huawei-style-ppt ~/.codex/skills/
cp -R huawei-ppt-skills/skills/huawei-tech-planning-ppt ~/.codex/skills/
```

Restart Codex after installation so the skills are discovered.

## Install For Claude Code

Claude Code can use the same skill documents as planning guides:

```bash
git clone https://github.com/jackylk/huawei-ppt-skills.git
mkdir -p ~/.claude/skills
cp -R huawei-ppt-skills/skills/huawei-style-ppt ~/.claude/skills/
cp -R huawei-ppt-skills/skills/huawei-tech-planning-ppt ~/.claude/skills/
```

For Claude Code, treat imagegen-related steps as prompt/spec generation unless an image-generation capability is available.

## Python Dependency For PPTX Packaging

The bundled `make_image_pptx.py` scripts use `python-pptx`:

```bash
python3 -m pip install python-pptx
```

## Typical Prompts

```text
Use $huawei-style-ppt to create a Huawei-style enterprise report PPT.
```

```text
Use $huawei-tech-planning-ppt to create a 30-40 page Chinese technical planning deck. Ask me the writing-direction questions first.
```

## Iterative Workflow

For technical planning decks, the skill asks the agent to create a source workspace:

```text
outputs/<deck-name>/
  research/
  planning/
  prompts/
  images/
  output/
```

Users can review `research/material-index.md`, `planning/slide-plan.md`, and `prompts/slide-XX.md`, then ask the agent to regenerate only affected pages or run incremental research for a section update.
