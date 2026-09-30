"""Builds assets/profile.svg from assets/profile.template.svg.

If you put your avatar image at assets/avatar.png (or .jpg/.webp), it is embedded
inside the SVG as base64. GitHub blocks SVGs from loading separate image files,
so embedding is the only way your avatar will show up.
Requires: pip install pillow   (only used to shrink big images)
"""
import base64, io, re, sys
from pathlib import Path

root = Path(__file__).parent / "assets"
tpl = (root / "profile.template.svg").read_text(encoding="utf-8")
avatar = next((p for p in (root / "profile.png", root / "profile.jpg", root / "profile.jpeg", root / "profile.webp") if p.exists()), None)

if avatar is None:
    out = tpl
    print("No avatar file found - built with the fallback laptop drawing.")
else:
    try:
        from PIL import Image
        im = Image.open(avatar).convert("RGBA")
        im.thumbnail((900, 900))
        buf = io.BytesIO(); im.save(buf, "PNG", optimize=True)
        data, mime = buf.getvalue(), "image/png"
    except ImportError:
        data, mime = avatar.read_bytes(), "image/png" if avatar.suffix == ".png" else "image/jpeg"
        print("Pillow not installed - embedding original file (may be large).")
    b64 = base64.b64encode(data).decode()
    img = (f'<image href="data:{mime};base64,{b64}" x="20" y="-120" width="530" height="530" '
           f'preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarClip)"/>')
    out = re.sub(r"<!--AVATAR_START-->.*?<!--AVATAR_END-->", lambda m: img, tpl, flags=re.S)
    print(f"Embedded {avatar.name} ({len(data)//1024} KB).")

(root / "profile.svg").write_text(out, encoding="utf-8")
print("Wrote assets/profile.svg")
