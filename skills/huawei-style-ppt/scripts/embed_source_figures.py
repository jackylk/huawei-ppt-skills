#!/usr/bin/env python3
"""Place original source figures into reserved boxes on a generated slide PNG."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, type=Path, help="ImageGen slide PNG")
    parser.add_argument("--placements", required=True, type=Path, help="JSON placement list")
    parser.add_argument("--output", required=True, type=Path, help="Final slide PNG")
    args = parser.parse_args()

    base = args.base.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if base == output:
        parser.error("--output must differ from --base so the generated slide is preserved")
    if output.suffix.lower() != ".png":
        parser.error("--output must be a PNG")

    manifest = args.placements.expanduser().resolve()
    placements = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(placements, list) or not placements:
        parser.error("--placements must contain a non-empty JSON list")

    with Image.open(base) as raw_slide:
        slide = raw_slide.convert("RGB")
    for index, placement in enumerate(placements, 1):
        source = Path(placement["source"]).expanduser()
        if not source.is_absolute():
            source = manifest.parent / source
        box = placement["box"]
        if (len(box) != 4 or any(not isinstance(v, int) for v in box)
                or not (0 <= box[0] < box[2] <= slide.width)
                or not (0 <= box[1] < box[3] <= slide.height)):
            parser.error(f"placement {index}: invalid pixel box {box}")
        padding = placement.get("padding", 0)
        if not isinstance(padding, int) or padding < 0 or padding * 2 >= min(box[2] - box[0], box[3] - box[1]):
            parser.error(f"placement {index}: invalid padding {padding}")
        ImageDraw.Draw(slide).rectangle(
            (box[0], box[1], box[2] - 1, box[3] - 1),
            fill=placement.get("background", "#FFFFFF"),
        )
        with Image.open(source) as raw_figure:
            figure = ImageOps.contain(
                raw_figure.convert("RGBA"),
                (box[2] - box[0] - 2 * padding, box[3] - box[1] - 2 * padding),
                method=Image.Resampling.LANCZOS,
            )
        x = box[0] + (box[2] - box[0] - figure.width) // 2
        y = box[1] + (box[3] - box[1] - figure.height) // 2
        slide.paste(figure, (x, y), figure)

    output.parent.mkdir(parents=True, exist_ok=True)
    slide.save(output)
    print(output)


if __name__ == "__main__":
    main()
