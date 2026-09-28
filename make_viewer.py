# -*- coding: utf-8 -*-
"""Rebuild price_viewer.html from basket_ready.html + data.js (CATALOG not inlined)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "basket_ready.html"
OUT = ROOT / "price_viewer.html"


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []
    for line in lines:
        if line.startswith("const CATALOG"):
            out.append("</script>")
            out.append('<script src="data.js"></script>')
            out.append("<script>")
            continue
        if line.startswith("const ALL_CHAINS"):
            out.append(
                "const ALL_CHAINS = [...new Set((typeof CATALOG !== 'undefined' ? CATALOG : [])"
                ".flatMap(i => Object.keys(i.ch || {})))].sort();"
            )
            continue
        out.append(line)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
