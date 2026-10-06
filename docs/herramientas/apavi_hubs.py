"""Crea las páginas hub piscinas-de-arena.html y suelos-resineo.html en apavi-green
y actualiza portada, footers, resinas-epoxi y sitemap (uso único).

Uso: python3 -I apavi_hubs.py /home/user/apavi-green
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
BASE = "https://apavigreen.com"
TEMPLATE = (ROOT / "resinas-epoxi.html").read_text(encoding="utf-8")

PROVIDER = {
    "@type": "LocalBusiness", "name": "Apavi Green", "url": BASE, "telephone": "+34654765548",
    "address": {"@type": "PostalAddress", "addressLocality": "Las Palmas de Gran Canaria",
                "addressRegion": "Gran Canaria", "addressCountry": "ES"},
}


def details(q, a):
    return f"""
      <details style="background:var(--g800);border:1px solid var(--g700);border-radius:12px;padding:20px 24px;cursor:pointer;">
        <summary style="font-weight:700;color:#fff;font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;align-items:center;">
          {html.escape(q)}
          <span style="color:var(--g400);font-size:1.3rem;flex-shrink:0;margin-left:12px;">+</span>
        </summary>
        <p style="margin-top:14px;color:rgba(255,255,255,.65);line-height:1.7;">{html.escape(a)}</p>
      </details>
"""


def faq_section(faqs):
    return f"""<!-- FAQ -->
<section style="background:var(--g950);padding:64px 0;">
  <div class="container" style="max-width:760px;">
    <div class="section-label" style="color:var(--g400);margin-bottom:8px;">Preguntas frecuentes</div>
    <h2 class="section-title" style="color:#fff;margin-bottom:40px;">Todo lo que necesitas <em>saber</em></h2>
    <div style="display:flex;flex-direction:column;gap:12px;">
{''.join(details(q, a) for q, a in faqs)}
    </div>
  </div>
</section>
"""


def card(icon, title, desc):
    return f"""      <div class="benefit-card">
        <div class="benefit-icon">{icon}</div>
        <div class="benefit-title">{title}</div>
        <div class="benefit-desc">{desc}</div>
      </div>
"""


def section(label, title, inner, alt=False):
    bg = ' style="background:var(--n50);"' if alt else ""
    return f"""<section class="section"{bg}>
  <div class="container">
    <div class="section-header">
      <div class="deco-line"></div>
      <div class="section-label">{label}</div>
      <h2 class="section-title">{title}</h2>
    </div>
{inner}
  </div>
</section>
"""


def prose(paragraphs):
    ps = "\n".join(f'    <p style="color:var(--n700);line-height:1.8;margin-bottom:16px;">{p}</p>' for p in paragraphs)
    return f'    <div style="max-width:760px;">\n{ps}\n    </div>'


def landing_box(text, url, label):
    return f"""<section style="background:linear-gradient(135deg,var(--g950),var(--g800));padding:56px 0;">
  <div class="container" style="max-width:760px;text-align:center;">
    <div class="section-label" style="color:var(--g400);margin-bottom:8px;">Web oficial</div>
    <p style="color:rgba(255,255,255,.75);line-height:1.7;margin-bottom:24px;">{text}</p>
    <a href="{url}" class="btn-primary" target="_blank" rel="noopener">{label} &rarr;</a>
  </div>
</section>
"""


def cta(text):
    return f"""<!-- CTA -->
<section style="background:linear-gradient(135deg,var(--g950),var(--g800));padding:64px 0;text-align:center;">
  <div class="container" style="max-width:600px;">
    <div class="section-label" style="color:var(--g400);margin-bottom:8px;">¿Interesado?</div>
    <h2 class="section-title" style="color:#fff;margin-bottom:16px;">Presupuesto gratis <em>en 24h</em></h2>
    <p style="color:rgba(255,255,255,.6);margin-bottom:32px;line-height:1.7;">{text}</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
      <a href="cuestionario.html" class="btn-primary">Pedir presupuesto gratis &rarr;</a>
      <a href="https://wa.me/34654765548" class="btn-ghost">&#128172; WhatsApp</a>
    </div>
  </div>
</section>
"""


def build(slug, title, desc, og_title, image, image_alt, img_style, h1, sub, schema_service, faqs, body):
    s = TEMPLATE
    head, rest = s.split("<!-- HERO -->", 1)
    footer = rest[rest.index('<footer class="footer">'):]
    head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, count=1)
    for pat, val in [
        (r'(<meta name="description" content=")[^"]*', desc),
        (r'(<link rel="canonical" href=")[^"]*', f"{BASE}/{slug}"),
        (r'(<meta property="og:title" content=")[^"]*', og_title),
        (r'(<meta property="og:description" content=")[^"]*', desc),
        (r'(<meta property="og:url" content=")[^"]*', f"{BASE}/{slug}"),
        (r'(<meta property="og:image" content=")[^"]*', f"{BASE}/{image}"),
        (r'(<meta name="twitter:title" content=")[^"]*', title),
        (r'(<meta name="twitter:description" content=")[^"]*', desc),
    ]:
        head, n = re.subn(pat, lambda m, v=val: m.group(1) + v, head, count=1)
        assert n == 1, pat
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    ld = ("  <script type=\"application/ld+json\">\n  " + json.dumps(schema_service, ensure_ascii=False) + "\n  </script>\n"
          "  <script type=\"application/ld+json\">\n  " + json.dumps(faq_ld, ensure_ascii=False) + "\n  </script>\n")
    head = re.sub(r'  <script type="application/ld\+json">.*?</script>\n  <script type="application/ld\+json">.*?</script>\n',
                  lambda m: ld, head, count=1, flags=re.S)
    assert "FAQPage" in head and slug.split(".")[0].split("-")[0] in head
    hero = f"""<!-- HERO -->
<section style="background:linear-gradient(135deg,#1a1a2e,#2d2d44);padding:80px 0 64px;">
  <div class="container">
    <div class="section-label" style="color:var(--g400);">Servicios</div>
    <h1 class="section-title" style="color:#fff;">{h1}</h1>
    <p class="section-sub" style="color:rgba(255,255,255,.55);margin-bottom:32px;">{sub}</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;">
      <a href="cuestionario.html" class="btn-primary">Presupuesto gratis &rarr;</a>
      <a href="index.html#contacto" class="btn-ghost">Hablar con un experto</a>
    </div>
  </div>
</section>

<!-- IMAGEN DESTACADA -->
<section style="padding:0;background:#111;">
  <div style="{img_style}">
    <img src="{image}" alt="{image_alt}" style="width:100%;height:360px;object-fit:cover;display:block;" loading="eager">
  </div>
</section>

"""
    out = head + hero + body + faq_section(faqs) + "\n" + footer
    (ROOT / slug).write_text(out, encoding="utf-8")


# ------------------------------------------------------------ piscinas de arena
PISC_FAQ = [
    ("¿Qué es una piscina de arena?",
     "Es una piscina cuyo vaso se reviste con una mezcla de arena, cuarzo y guijarros naturales en lugar de gresite o liner. El resultado recuerda al fondo de una playa: formas orgánicas, entradas graduales y un color de agua natural."),
    ("¿En qué zonas instaláis piscinas de arena Bio.design?",
     "Apavi Green es concesionario oficial de Bio.design para la provincia de Santa Cruz de Tenerife: Tenerife, La Palma, La Gomera y El Hierro. Para otras provincias, Bio.design trabaja con otros concesionarios autorizados."),
    ("¿Cuánto cuesta una piscina de arena?",
     "Cada piscina Bio.design se diseña a medida, así que el precio depende de la forma, el tamaño, los acabados y el terreno. Hacemos una visita técnica y un presupuesto gratuitos y sin compromiso."),
    ("¿Una piscina de arena necesita más mantenimiento?",
     "No más que una piscina convencional. El revestimiento incorpora protección antibacteriana Microban y la depuración funciona como en cualquier piscina con filtro. Te explicamos el mantenimiento en la entrega."),
    ("¿Se puede convertir una piscina existente en piscina de arena?",
     "Depende del estado y de la forma del vaso actual. Lo valoramos en la visita técnica y te decimos si conviene rehabilitar o construir de nuevo."),
]

PISC_BODY = section("Qué es", "La piscina que parece <em>una playa</em>", prose([
    "Una piscina de arena sustituye el clásico gresite azul por un revestimiento de <strong>arena, cuarzo y guijarros naturales</strong>. El vaso deja de ser una caja de hormigón y pasa a tener formas libres, orillas suaves y entradas graduales, como una cala.",
    "En Apavi Green trabajamos con <strong>Bio.design</strong>, el fabricante italiano que nació en Milán en 1980 y que lleva más de 40 años desarrollando este sistema. Su tecnología está patentada y su revestimiento incorpora resinas con protección antibacteriana Microban.",
    "Somos <strong>concesionario oficial de Bio.design para la provincia de Santa Cruz de Tenerife</strong>: Tenerife, La Palma, La Gomera y El Hierro.",
])) + section("Ventajas", "¿Por qué una piscina <em>de arena</em>?", '    <div class="benefit-grid">\n'
    + card("&#127958;&#65039;", "Aspecto natural", "Formas orgánicas, sin bordes rectos ni hormigón visible. Se integra en el jardín y en el paisaje canario.")
    + card("&#128099;", "Entradas graduales", "Accesos tipo playa, cómodos para niños, mayores y mascotas, sin escaleras metálicas.")
    + card("&#127912;", "Totalmente a medida", "Forma, tamaño, colores de arena y combinaciones de guijarros diseñados para tu espacio.")
    + card("&#128737;&#65039;", "Revestimiento antibacteriano", "Protección Microban integrada en el revestimiento, para un vaso más limpio durante más tiempo.")
    + card("&#127807;", "Sostenible", "Sistema premiado por su sostenibilidad, con menor consumo de recursos a lo largo de su vida útil.")
    + card("&#127942;", "Respaldo del fabricante", "Diseño, instalación y mantenimiento con el soporte técnico directo de Bio.design.")
    + "    </div>", alt=True) + section("Para quién", "¿A quién le encaja <em>una piscina de arena</em>?", prose([
    "<strong>Viviendas particulares</strong> que quieren una piscina diferente, integrada en el jardín y no un rectángulo de azulejo.",
    "<strong>Villas y casas vacacionales</strong> del sur de Tenerife (Adeje, Arona, Costa Adeje) que necesitan destacar en fotos y reseñas.",
    "<strong>Hoteles, resorts y complejos turísticos</strong> que buscan una zona de baño con efecto playa y menos mantenimiento.",
    "Si tu proyecto es en Gran Canaria u otra provincia, cuéntanoslo igualmente: te orientamos y, si no podemos instalarla nosotros, te ponemos en contacto con el concesionario de tu zona.",
])) + section("Complementos", "El resto del <em>exterior</em>", prose([
    "Alrededor de la piscina solemos instalar un borde drenante de <a href=\"suelos-resineo.html\" style=\"color:var(--g700);\">suelo Résineo</a>, que no se encharca y no resbala con los pies mojados, y zonas verdes de <a href=\"cesped-artificial-tenerife.html\" style=\"color:var(--g700);\">césped artificial en Tenerife</a>. Un único interlocutor para todo el exterior.",
]), alt=True) + landing_box(
    "Fotos de proyectos, tecnología y configurador de presupuesto en la web oficial de nuestra concesión Bio.design en Tenerife.",
    "https://www.piscinadearenatenerife.com/", "Ver piscinas de arena en Tenerife") + cta(
    "Cuéntanos cómo es tu jardín y te preparamos un presupuesto a medida. Visita técnica gratuita en la provincia de Santa Cruz de Tenerife.")

build(
    "piscinas-de-arena.html",
    "Piscinas de Arena en Tenerife — Bio.design | Apavi Green",
    "Piscinas de arena Bio.design en Tenerife, La Palma, La Gomera y El Hierro: formas naturales, entradas tipo playa y revestimiento antibacteriano. Concesionario oficial.",
    "Piscinas de Arena Bio.design en Tenerife | Apavi Green",
    "assets/img/servicios/piscina-2.webp",
    "Piscina de arena Bio.design con orillas naturales en Tenerife — Apavi Green",
    "max-width:960px;margin:0 auto;",
    "Piscinas de Arena <em>en Tenerife</em>",
    "Piscinas de arena natural Bio.design, diseñadas a medida, con formas orgánicas y entradas tipo playa. Concesionario oficial para la provincia de Santa Cruz de Tenerife.",
    {"@context": "https://schema.org", "@type": "Service", "name": "Piscinas de arena Bio.design",
     "serviceType": "Construcción de piscinas de arena", "url": f"{BASE}/piscinas-de-arena.html",
     "brand": {"@type": "Brand", "name": "Bio.design"}, "provider": PROVIDER,
     "areaServed": ["Tenerife", "La Palma", "La Gomera", "El Hierro"],
     "sameAs": "https://www.piscinadearenatenerife.com/"},
    PISC_FAQ, PISC_BODY)

# ------------------------------------------------------------------ résineo
RES_FAQ = [
    ("¿Qué es el suelo Résineo?",
     "Es un pavimento continuo de piedra natural (mármol o cuarzo) unida con resina de poliuretano transparente, conocido también como moqueta de piedra. Entre los granos quedan poros por los que el agua se filtra, así que no se forman charcos."),
    ("¿En qué se diferencia de la resina epoxi?",
     "La resina epoxi forma una capa lisa y cerrada, ideal para garajes, parkings y locales. Résineo es poroso y drenante, con aspecto de piedra, pensado sobre todo para bordes de piscina, terrazas y caminos exteriores."),
    ("¿Hay que levantar el suelo actual?",
     "En la mayoría de los casos no. Se aplica sobre hormigón o baldosa existente bien adherida, con unos 10 mm de espesor para uso peatonal. Lo comprobamos en la visita técnica."),
    ("¿Es seguro con los pies mojados?",
     "Sí. Résineo Drain tiene clasificación PN18 para zonas de pies descalzos, como las playas de piscina, porque el agua no se queda en la superficie."),
    ("¿En qué islas lo instaláis?",
     "Somos distribuidor oficial de Résineo para todas las Islas Canarias y lo instalamos en Gran Canaria, Tenerife, Lanzarote, Fuerteventura, La Palma, La Gomera y El Hierro."),
]

RES_BODY = section("Qué es", "Piedra natural que <em>deja pasar el agua</em>", prose([
    "<strong>Résineo</strong> es un suelo continuo formado en un 95-97 % por granos de mármol o cuarzo natural, unidos con una resina de poliuretano transparente. Es lo que muchos conocen como <strong>moqueta de piedra</strong> o moqueta de mármol.",
    "Su particularidad es que es <strong>drenante</strong>: el agua se filtra entre los granos, de 30 a 50 litros por segundo y por metro cuadrado. No hay charcos, se seca rápido y agarra incluso descalzo y mojado.",
    "Apavi Green es <strong>distribuidor oficial de Résineo para las Islas Canarias</strong>. El fabricante es LRVision (Toulouse, Francia), que lo desarrolla desde 2004.",
])) + section("Dónde se usa", "Bordes de piscina, terrazas <em>y jardines</em>", '    <div class="benefit-grid">\n'
    + card("&#127946;", "Borde y playa de piscina", "Antideslizante con los pies mojados (clase PN18), sin charcos y sin juntas que se ennegrezcan.")
    + card("&#127968;", "Terrazas y áticos", "Renovación sobre la baldosa existente, sin desescombro y con acabado de piedra natural.")
    + card("&#127795;", "Caminos y patios", "Trazados curvos, alcorques y remates alrededor de plantas, sin malas hierbas entre juntas.")
    + "    </div>", alt=True) + section("Ventajas", "¿Por qué <em>Résineo</em>?", prose([
    "<strong>Sin obra de demolición:</strong> en la mayoría de los casos se aplica sobre el suelo actual, con unos 10 mm sobre hormigón o baldosa.",
    "<strong>Color que dura:</strong> el color es el de la propia piedra, con resina resistente a los rayos UV, algo clave con el sol de Canarias.",
    "<strong>Mantenimiento mínimo:</strong> agua para el día a día y una limpieza anual con cepillo o con hidrolimpiadora a baja presión.",
    "<strong>Certificado:</strong> Résineo Drain cuenta con evaluación técnica del CSTB francés.",
    "¿Buscas un suelo cerrado para un garaje o un parking? Para eso es mejor la <a href=\"resinas-epoxi.html\" style=\"color:var(--g700);\">resina epoxi</a>. ¿Quieres una piscina entera con efecto playa? Mira las <a href=\"piscinas-de-arena.html\" style=\"color:var(--g700);\">piscinas de arena</a>.",
])) + landing_box(
    "Ficha técnica, colores, preguntas frecuentes y ejemplos de proyectos en la web oficial de Résineo Canarias.",
    "https://resineocanarias.com/", "Ver suelos Résineo en Canarias") + cta(
    "Envíanos medidas aproximadas y unas fotos del espacio y te preparamos un presupuesto gratuito con muestras de color.")

build(
    "suelos-resineo.html",
    "Suelo Résineo en Canarias — Piscinas y Terrazas | Apavi Green",
    "Suelo drenante Résineo (moqueta de piedra) para bordes de piscina, terrazas y jardines en Canarias. Antideslizante, sin juntas y sin obra. Distribuidor oficial.",
    "Suelo Résineo drenante en Canarias | Apavi Green",
    "assets/img/servicios/resineo-terraza.webp",
    "Suelo drenante Résineo en terraza junto a piscina en Canarias — Apavi Green",
    "max-width:600px;margin:0 auto;",
    "Suelo Résineo <em>en Canarias</em>",
    "Pavimento drenante de piedra natural y resina para bordes de piscina, terrazas y jardines. Antideslizante, sin juntas y, en la mayoría de los casos, sin levantar el suelo actual.",
    {"@context": "https://schema.org", "@type": "Service", "name": "Instalación de suelo drenante Résineo",
     "serviceType": "Pavimento drenante de piedra natural y resina", "url": f"{BASE}/suelos-resineo.html",
     "brand": {"@type": "Brand", "name": "Résineo"}, "provider": PROVIDER,
     "areaServed": ["Islas Canarias", "Gran Canaria", "Tenerife", "Lanzarote", "Fuerteventura", "La Palma", "La Gomera", "El Hierro"],
     "sameAs": "https://resineocanarias.com/"},
    RES_FAQ, RES_BODY)

# ---------------------------------------------------------------- portada
idx = ROOT / "index.html"
s = idx.read_text(encoding="utf-8")
s = s.replace('<a href="https://www.piscinadearenatenerife.com/" class="bento-card b0a" target="_blank" rel="noopener">',
              '<a href="piscinas-de-arena.html" class="bento-card b0a">', 1)
s = s.replace('<a href="https://resineocanarias.com/" class="bento-card b0b" target="_blank" rel="noopener">',
              '<a href="suelos-resineo.html" class="bento-card b0b">', 1)
old = '<li><a href="#contacto">Piscinas y moqueta de mármol</a></li>'
assert old in s
s = s.replace(old, '<li><a href="piscinas-de-arena.html">Piscinas de Arena</a></li>\n          <li><a href="suelos-resineo.html">Suelo Résineo</a></li>', 1)
assert s.count('href="piscinas-de-arena.html"') == 2 and s.count('href="suelos-resineo.html"') == 2
idx.write_text(s, encoding="utf-8")

# ------------------------------------------------- footers (Servicios) resto
LI = '<li><a href="{p}resinas-epoxi.html">Resinas Epoxi</a></li>'
changed = []
for f in sorted(list(ROOT.glob("*.html")) + list(ROOT.glob("blog/*.html"))):
    if f.name in ("index.html",):
        continue
    t = f.read_text(encoding="utf-8")
    prefix = "../" if f.parent.name == "blog" else ""
    li = LI.format(p=prefix)
    if li in t and "suelos-resineo.html" not in t:
        t = t.replace(li, li + f'<li><a href="{prefix}piscinas-de-arena.html">Piscinas de Arena</a></li><li><a href="{prefix}suelos-resineo.html">Suelo Résineo</a></li>', 1)
        f.write_text(t, encoding="utf-8")
        changed.append(str(f.relative_to(ROOT)))

# --------------------------------------------- resinas-epoxi: enlace contextual
r = ROOT / "resinas-epoxi.html"
t = r.read_text(encoding="utf-8")
old = "Sin juntas donde se acumula agua, antideslizante y de larga duración en el clima canario.</div>"
assert old in t
t = t.replace(old, 'Sin juntas donde se acumula agua, antideslizante y de larga duración en el clima canario. ¿Prefieres un acabado de piedra natural que drene el agua? Mira el <a href="suelos-resineo.html" style="color:var(--g700);">suelo drenante Résineo</a>.</div>', 1)
r.write_text(t, encoding="utf-8")

# ----------------------------------------------------------------- sitemap
sm = ROOT / "sitemap.xml"
t = sm.read_text(encoding="utf-8")
new = "".join(f"""  <url>
    <loc>{BASE}/{p}</loc>
    <lastmod>2026-10-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
""" for p in ("piscinas-de-arena.html", "suelos-resineo.html"))
t = t.replace("</urlset>", new + "</urlset>", 1)
t = t.replace("""    <loc>https://apavigreen.com/</loc>
    <lastmod>2026-08-07</lastmod>""", """    <loc>https://apavigreen.com/</loc>
    <lastmod>2026-10-06</lastmod>""", 1)
t = t.replace("""    <loc>https://apavigreen.com/resinas-epoxi.html</loc>
    <lastmod>2026-08-07</lastmod>""", """    <loc>https://apavigreen.com/resinas-epoxi.html</loc>
    <lastmod>2026-10-06</lastmod>""", 1)
sm.write_text(t, encoding="utf-8")

print("footers:", changed)
