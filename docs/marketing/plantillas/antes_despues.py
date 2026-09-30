"""Genera una pieza "Antes / Después" 1080x1350 (WhatsApp / Instagram) con QR.

Uso:
  python3 antes_despues.py --antes a.jpg --despues d.jpg --salida out.png \
      --titulo "..." --subtitulo "..." --url "https://www.apavigreen.com/...?utm_..." \
      [--rotulo "Imagen ilustrativa"]   # obligatorio si alguna imagen es generada por IA
"""
import argparse, os, segno
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
F = lambda n, s: ImageFont.truetype(os.path.join(HERE, "fonts", n), s)
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LOGO = os.path.join(ROOT, "assets/img/logo/logo-apavigreen-transp.webp")

BG, BG2 = (8, 32, 18), (14, 50, 28)
LIME, WHITE, MUTED = (141, 198, 63), (255, 255, 255), (200, 214, 204)
W, H = 1080, 1350

def fit(img, w, h):
    return ImageOps.fit(img.convert("RGB"), (w, h), Image.LANCZOS, centering=(0.5, 0.5))

def pill(d, xy, text, fill, fg, font):
    x, y = xy
    tw = d.textlength(text, font=font)
    d.rounded_rectangle([x, y, x + tw + 36, y + 46], radius=23, fill=fill)
    d.text((x + 18, y + 23), text, font=font, fill=fg, anchor="lm")

def build(antes, despues, salida, titulo, subtitulo, url, rotulo=None,
          puntos=("Acabado continuo, sin juntas", "Fácil limpieza e higiene", "Ejecución rápida, mínima molestia")):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # degradado sutil
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=tuple(int(BG[i] + (BG2[i] - BG[i]) * t) for i in range(3)))
    # cabecera
    logo = Image.open(LOGO).convert("RGBA"); logo.thumbnail((180, 96))
    d.rounded_rectangle([48, 40, 48 + logo.width + 24, 40 + logo.height + 24], 14, fill=WHITE)
    im.paste(logo, (60, 52), logo)
    d.text((W - 60, 98), "www.apavigreen.com", font=F("Inter-600.ttf", 26), fill=MUTED, anchor="rm")
    # títulos
    d.text((60, 200), "ANTES Y DESPUÉS", font=F("Inter-700.ttf", 26), fill=LIME)
    d.text((60, 236), titulo, font=F("PJS-800.ttf", 64), fill=WHITE)
    d.text((60, 322), subtitulo, font=F("Inter-400.ttf", 30), fill=MUTED)
    # imágenes
    pw, ph, gap, top = 470, 500, 20, 390
    for i, (src, lab, col, fg) in enumerate([(antes, "ANTES", (60, 60, 60), WHITE), (despues, "DESPUÉS", LIME, BG)]):
        x = 60 + i * (pw + gap)
        ph_img = fit(Image.open(src), pw, ph)
        mask = Image.new("L", (pw, ph), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, pw, ph], 22, fill=255)
        im.paste(ph_img, (x, top), mask)
        pill(d, (x + 18, top + 18), lab, col, fg, F("PJS-800.ttf", 24))
    if rotulo:
        f = F("Inter-500.ttf", 20)
        tw = d.textlength(rotulo, font=f)
        d.rounded_rectangle([W - 60 - tw - 24, top + ph - 44, W - 60 - 8, top + ph - 12], 8, fill=(0, 0, 0))
        d.text((W - 60 - 20 - tw / 2 - 2, top + ph - 28), rotulo, font=f, fill=WHITE, anchor="mm")
    # puntos
    y = top + ph + 32
    for p in puntos:
        d.ellipse([60, y + 6, 84, y + 30], fill=LIME)
        d.text((72, y + 18), "✓", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18), fill=BG, anchor="mm")
        d.text((100, y + 18), p, font=F("Inter-500.ttf", 30), fill=WHITE, anchor="lm")
        y += 52
    # bloque CTA + QR
    cy = H - 250
    d.rounded_rectangle([40, cy, W - 40, H - 40], 28, fill=WHITE)
    q = segno.make(url, error="q")
    qpath = salida + ".qr.png"
    q.save(qpath, scale=10, border=2, dark="#08200F", light="#FFFFFF")
    qr = Image.open(qpath).convert("RGB").resize((180, 180), Image.NEAREST); os.remove(qpath)
    im.paste(qr, (W - 40 - 200, cy + 15))
    d.text((80, cy + 42), "Pide tu presupuesto gratis", font=F("PJS-800.ttf", 40), fill=BG)
    d.text((80, cy + 105), "Tel. y WhatsApp  654 765 548", font=F("Inter-700.ttf", 32), fill=(20, 110, 55))
    d.text((80, cy + 152), "Escanea el código o escríbenos", font=F("Inter-400.ttf", 26), fill=(70, 80, 72))
    im.save(salida, quality=95)
    return salida

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    for k in ("antes", "despues", "salida", "titulo", "subtitulo", "url"): a.add_argument("--" + k, required=True)
    a.add_argument("--rotulo")
    o = a.parse_args()
    build(o.antes, o.despues, o.salida, o.titulo, o.subtitulo, o.url, o.rotulo)
