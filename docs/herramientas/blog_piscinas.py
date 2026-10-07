"""Genera 2 artículos del blog de Apavi Green a partir de la plantilla del caso Carrizal.

Uso: python3 -I blog_piscinas.py /home/user/apavi-green
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
BASE = "https://www.apavigreen.com"
TPL = (ROOT / "blog/caso-exito-cesped-artificial-carrizal.html").read_text(encoding="utf-8")

head, rest = TPL.split('<section class="article-hero">', 1)
tail = rest[rest.index("</article>") + len("</article>"):]

# Estilos propios de Carrizal fuera; añadimos tabla, figuras y FAQ
head = re.sub(r"\n    \.carrizal-[^\n]*", "", head)
head = head.replace("@media(max-width:480px){ .carrizal-grid { grid-template-columns: 1fr; } }", "")
EXTRA_CSS = """
    .art-fig { margin: 28px 0 32px; }
    .art-fig img { width: 100%; height: auto; display: block; border-radius: var(--r8); }
    .art-fig figcaption { font-size: 13px; color: var(--n500); margin-top: 6px; }
    .art-table-wrap { overflow-x: auto; margin: 20px 0 28px; -webkit-overflow-scrolling: touch; }
    .art-table { width: 100%; border-collapse: collapse; font-size: 14.5px; min-width: 520px; }
    .art-table th, .art-table td { padding: 11px 14px; border-bottom: 1px solid var(--n100); text-align: left; vertical-align: top; color: var(--n700); line-height: 1.5; }
    .art-table thead th { background: var(--g950); color: #fff; font-weight: 700; }
    .art-table tbody th { color: var(--n950); font-weight: 700; background: var(--n50); }
    .art-faq details { border-bottom: 1px solid var(--n100); padding: 16px 0; }
    .art-faq summary { cursor: pointer; font-weight: 700; color: var(--n950); font-size: 16px; }
    .art-faq details p { margin: 10px 0 0; }
  </style>"""
head = head.replace("\n  </style>", EXTRA_CSS, 1)


def build(slug, title, meta_desc, og_title, h1, intro, cat, date_iso, date_txt, read_min,
          hero_img, hero_alt, hero_wh, body, faqs, cta_h2, cta_p):
    url = f"{BASE}/blog/{slug}.html"
    h = head
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, count=1)
    for pat, val in [
        (r'(<meta name="description" content=")[^"]*', meta_desc),
        (r'(<link rel="canonical" href=")[^"]*', url),
        (r'(<meta property="og:title" content=")[^"]*', og_title),
        (r'(<meta property="og:description" content=")[^"]*', meta_desc),
        (r'(<meta property="og:image" content=")[^"]*', f"{BASE}/assets/img/blog/piscinas/{hero_img}"),
    ]:
        h, n = re.subn(pat, lambda m, v=val: m.group(1) + v, h, count=1)
        assert n == 1, pat
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": h1, "description": meta_desc,
         "image": f"{BASE}/assets/img/blog/piscinas/{hero_img}",
         "datePublished": date_iso, "dateModified": date_iso, "inLanguage": "es",
         "mainEntityOfPage": url,
         "author": {"@type": "Organization", "name": "Apavi Green", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "Apavi Green", "url": BASE + "/",
                       "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/img/logo/logo-apavigreen-transp.webp"}}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog.html"},
            {"@type": "ListItem", "position": 3, "name": h1, "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
    ]}
    h = re.sub(r'<script type="application/ld\+json">.*?</script>',
               lambda m: '<script type="application/ld+json">\n  ' + json.dumps(graph, ensure_ascii=False) + "\n  </script>",
               h, count=1, flags=re.S)
    hero = f"""<section class="article-hero">
  <div class="container">
    <a href="../blog.html" style="display:inline-flex;align-items:center;gap:6px;font-size:13px;color:rgba(255,255,255,.5);margin-bottom:28px;">&larr; Blog Apavi Green</a>
    <div class="article-meta">
      <span class="article-cat">{cat}</span>
      <span class="article-date">{date_txt}</span>
      <span class="article-read">&#128338; {read_min} min lectura</span>
    </div>
    <h1 style="font-family:var(--font-h);font-size:clamp(26px,4vw,46px);font-weight:900;color:#fff;line-height:1.15;margin-bottom:16px;letter-spacing:-.02em;max-width:760px;">{h1}</h1>
    <p style="font-size:17px;color:rgba(255,255,255,.65);max-width:600px;line-height:1.6;">{intro}</p>
    <div class="article-hero-img">
      <img src="../assets/img/blog/piscinas/{hero_img}" alt="{hero_alt}" width="{hero_wh[0]}" height="{hero_wh[1]}" loading="eager">
    </div>
  </div>
</section>
"""
    faq_html = '\n  <h2>Preguntas frecuentes</h2>\n  <div class="art-faq">\n' + "".join(
        f"    <details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>\n" for q, a in faqs) + "  </div>\n"
    article = '<article class="article-body">\n' + body + faq_html + "</article>"
    t = tail
    t = re.sub(r"<h2>¿Quieres un jardín así <em>sin regar</em>\?</h2>", cta_h2, t, count=1)
    t = t.replace("<p>Te damos un presupuesto exacto en menos de 24h. Sin compromiso.</p>", f"<p>{cta_p}</p>", 1)
    out = h + hero + article + t
    (ROOT / f"blog/{slug}.html").write_text(out, encoding="utf-8")
    return out


def fig(img, alt, cap, wh):
    return (f'  <figure class="art-fig"><img src="../assets/img/blog/piscinas/{img}" alt="{alt}" width="{wh[0]}" '
            f'height="{wh[1]}" loading="lazy"><figcaption>{cap}</figcaption></figure>\n')


# ------------------------------------------------------------------ artículo 1
FAQ1 = [
    ("¿Qué es una piscina de arena?",
     "Es una piscina en la que el vaso se reviste con una mezcla de arena, cuarzo y guijarros naturales en lugar de gresite. Permite formas libres y entradas graduales, como una playa."),
    ("¿Es más cara una piscina de arena que una de gresite?",
     "Depende del proyecto. Una piscina rectangular de gresite suele ser la opción más económica de partida; la piscina de arena es un proyecto a medida cuyo precio depende de la forma, el tamaño, el terreno y los acabados. Lo mejor es pedir presupuesto de las dos opciones para tu caso."),
    ("¿Se puede convertir una piscina de gresite en una de arena?",
     "En algunos casos sí, según el estado y la forma del vaso actual. Hay que valorarlo en una visita técnica."),
    ("¿Dónde instaláis piscinas de arena?",
     "Apavi Green es concesionario oficial de Bio.design para la provincia de Santa Cruz de Tenerife: Tenerife, La Palma, La Gomera y El Hierro. Para otras zonas te orientamos y te ponemos en contacto con el concesionario correspondiente."),
]
BODY1 = """  <p>Si estás pensando en hacer o renovar una piscina, la primera gran decisión es el acabado del vaso. El <strong>gresite</strong> es el clásico de toda la vida: mosaico azul, formas rectas y escalera. La <strong>piscina de arena</strong> es la alternativa que más está creciendo: un acabado de arena y piedra natural con formas libres y entrada tipo playa. En este artículo te contamos en qué se diferencian, qué ventajas tiene cada una y cómo elegir.</p>
  <h2>¿Qué es el gresite?</h2>
  <p>El gresite es un <strong>mosaico de pequeñas piezas vítreas</strong> que se pega con cemento cola sobre el vaso de hormigón ya impermeabilizado, rejuntando pieza a pieza. Es resistente, se fabrica en muchos colores (aunque el azul es el más habitual) y es el acabado que la mayoría tenemos en la cabeza cuando pensamos en una piscina.</p>
  <p>Sus puntos débiles suelen estar en las <strong>juntas</strong>: con los años pueden oscurecerse, acumular algas o perder piezas, y obligan a revisiones y reparaciones periódicas. Además, el diseño suele limitarse a formas geométricas con escalera o peldaños de obra.</p>
  <h2>¿Qué es una piscina de arena?</h2>
  <p>En una piscina de arena el vaso se reviste con una mezcla de <strong>arena, cuarzo y guijarros naturales</strong>. El resultado recuerda al fondo de una playa: el agua toma un color turquesa natural, las orillas son suaves y la entrada puede ser <strong>gradual, como en la orilla del mar</strong>.</p>
  <p>En Apavi Green trabajamos con <strong>Bio.design</strong>, el fabricante italiano que lleva más de 40 años desarrollando este sistema. Su tecnología es patentada, el revestimiento incorpora <strong>protección antibacteriana Microban</strong> y las juntas de dilatación sinuosas reducen las tensiones que provocan grietas.</p>
""" + fig("piscina-arena-bio-design-entrada-playa.webp", "Piscina de arena Bio.design con entrada de playa y formas orgánicas en un jardín tropical", "Piscina de arena Bio.design: formas libres y entrada tipo playa. Imagen: Bio.design.", (1200, 667)) + """  <h2>Comparativa: piscina de arena vs gresite</h2>
  <div class="art-table-wrap">
    <table class="art-table">
      <thead><tr><th></th><th>Gresite</th><th>Piscina de arena</th></tr></thead>
      <tbody>
        <tr><th>Aspecto</th><td>Clásico, mosaico de colores (normalmente azul)</td><td>Natural, efecto playa, agua turquesa</td></tr>
        <tr><th>Formas</th><td>Sobre todo geométricas</td><td>Libres y orgánicas, totalmente a medida</td></tr>
        <tr><th>Entrada al agua</th><td>Escalera o peldaños</td><td>Gradual tipo playa (y también escalones si se quiere)</td></tr>
        <tr><th>Juntas</th><td>Muchas, entre cada pieza</td><td>Pocas, sinuosas y pensadas para evitar grietas</td></tr>
        <tr><th>Tacto</th><td>Liso, resbaladizo en zonas de paso</td><td>Mineral, agradable al pisar descalzo</td></tr>
        <tr><th>Integración</th><td>Destaca como elemento construido</td><td>Se integra en el jardín y el paisaje</td></tr>
        <tr><th>Precio</th><td>Suele ser la opción de partida más económica</td><td>Proyecto a medida: depende de forma, tamaño y acabados</td></tr>
      </tbody>
    </table>
  </div>
  <h2>Ventajas de la piscina de arena</h2>
  <ul>
    <li><strong>Entrada tipo playa:</strong> muy cómoda para niños, personas mayores y mascotas, sin escaleras metálicas.</li>
    <li><strong>Diseño libre:</strong> la forma se adapta al terreno y al jardín, no al revés.</li>
    <li><strong>Aspecto natural:</strong> la arena y el cuarzo dan al agua un color que no se consigue con gresite.</li>
    <li><strong>Agradable al tacto:</strong> el revestimiento mineral es cómodo para pasear descalzo por las zonas de poca profundidad.</li>
    <li><strong>Revestimiento antibacteriano:</strong> la protección Microban ayuda a mantener el vaso limpio durante más tiempo.</li>
  </ul>
""" + fig("piscina-arena-bio-design-jardin-aerea.webp", "Vista aérea de una piscina de arena Bio.design de formas orgánicas rodeada de césped", "Vista aérea de una piscina de arena integrada en el jardín. Imagen: Bio.design.", (1200, 674)) + """  <h2>¿Cuándo tiene sentido el gresite?</h2>
  <p>El gresite sigue siendo una buena opción si buscas una <strong>piscina rectangular sencilla</strong>, de uso deportivo (nadar largos) o con un presupuesto inicial ajustado. También si quieres un estilo clásico o un color muy concreto del mosaico.</p>
  <h2>¿Cómo elegir?</h2>
  <ul>
    <li><strong>Elige piscina de arena</strong> si quieres una piscina diferente, integrada en el jardín, con entrada de playa y pensada para disfrutar en familia o para alojamientos turísticos.</li>
    <li><strong>Elige gresite</strong> si priorizas una forma rectangular estándar, nadar largos o el presupuesto de partida.</li>
  </ul>
  <div class="article-tip">
    <p><strong>¿Piscina de arena en Tenerife?</strong> Somos concesionario oficial de Bio.design para la provincia de Santa Cruz de Tenerife. Toda la información en <a href="../piscinas-de-arena.html">piscinas de arena en Tenerife</a> y en la web de nuestra concesión, <a href="https://www.piscinadearenatenerife.com/" target="_blank" rel="noopener">piscinadearenatenerife.com</a>.</p>
  </div>
""" + fig("piscina-arena-bio-design-mar.webp", "Piscina de arena Bio.design con vistas al mar y orilla de arena natural", "Las piscinas de arena encajan especialmente bien en viviendas y alojamientos con vistas. Imagen: Bio.design.", (1200, 757)) + """  <h2>Completa el exterior</h2>
  <p>Alrededor de la piscina, un borde que no resbale y no se encharque marca la diferencia. Te lo contamos en <a href="suelo-antideslizante-borde-piscina.html">suelo antideslizante para el borde de la piscina</a>. Y para las zonas verdes, mira nuestro <a href="../cesped-artificial-tenerife.html">césped artificial en Tenerife</a>.</p>
"""

out1 = build(
    "piscina-de-arena-vs-gresite",
    "Piscina de arena vs gresite: diferencias y cuál elegir | Apavi Green",
    "Piscina de arena o de gresite: comparamos aspecto, formas, entrada, juntas, mantenimiento y precio para que elijas la mejor opción. Piscinas de arena Bio.design en Tenerife.",
    "Piscina de arena vs gresite: diferencias y cuál elegir | Apavi Green",
    "Piscina de arena vs gresite: diferencias y cuál elegir",
    "Comparamos los dos acabados de piscina más buscados: aspecto, formas, entrada al agua, juntas, mantenimiento y precio. Y te contamos cuándo conviene cada uno.",
    "Piscinas", "2026-10-07", "7 octubre 2026", 6,
    "piscina-arena-bio-design-mar.webp", "Piscina de arena Bio.design con orilla natural y vistas al mar", (1200, 757),
    BODY1, FAQ1,
    "¿Quieres una piscina <em>de arena</em>?",
    "Visita técnica y presupuesto gratis en la provincia de Santa Cruz de Tenerife. Sin compromiso.")

# ------------------------------------------------------------------ artículo 2
FAQ2 = [
    ("¿Qué suelo resbala menos en el borde de una piscina?",
     "Los suelos con textura y que dejan pasar el agua, como la moqueta de piedra drenante, y los pavimentos con clase de resbaladicidad alta para pies descalzos. Lo importante es que no se forme una lámina de agua en la superficie."),
    ("¿Qué clase de resbaladicidad exige la normativa para piscinas?",
     "El Código Técnico de la Edificación (CTE DB SUA 1) exige clase 3, la más alta, en las zonas de piscina y duchas de edificios de uso público. En viviendas no es obligatorio, pero es la referencia recomendable."),
    ("¿Qué suelo de piscina quema menos al sol?",
     "Los de color claro. Cualquier pavimento oscuro expuesto al sol de Canarias se calienta mucho más, sea piedra, cerámica o resina."),
    ("¿Se puede poner un suelo antideslizante sin levantar el actual?",
     "Sí, en muchos casos. Un pavimento como Résineo se aplica sobre la baldosa existente si está bien adherida, con unos 10 mm de espesor, sin obra de demolición."),
]
BODY2 = """  <p>El borde de la piscina es la zona más peligrosa de cualquier casa: <strong>agua, pies descalzos y prisas</strong>. Un mal suelo convierte cada salida del agua en un riesgo de resbalón, sobre todo para niños y personas mayores. En este artículo repasamos qué suelos funcionan mejor, qué dice la normativa y qué conviene en el clima de Canarias.</p>
  <h2>Qué debe tener un buen suelo para el borde de la piscina</h2>
  <ul>
    <li><strong>Agarre con los pies mojados:</strong> es lo más importante. El suelo debe tener textura suficiente para no resbalar descalzo.</li>
    <li><strong>Que no se encharque:</strong> si el agua se queda en la superficie forma una lámina que resbala, por bueno que sea el material.</li>
    <li><strong>Que no queme:</strong> en Canarias el sol aprieta casi todo el año; los tonos claros se calientan mucho menos.</li>
    <li><strong>Resistencia</strong> al cloro, a la sal, a los rayos UV y a las cremas solares.</li>
    <li><strong>Pocas juntas:</strong> las juntas acumulan suciedad, se ennegrecen y pueden levantarse.</li>
  </ul>
  <h2>Qué dice la normativa</h2>
  <p>El <strong>Código Técnico de la Edificación (CTE DB SUA 1)</strong> clasifica los suelos según su resbaladicidad en clases 1, 2 y 3, y exige la <strong>clase 3 —la más exigente— en zonas de piscinas y duchas</strong> de edificios de uso público, como hoteles, comunidades o instalaciones deportivas. En una vivienda no es obligatorio, pero es la mejor referencia para elegir.</p>
  <p>Para zonas de pies descalzos también se usan clasificaciones específicas (por ejemplo, las clases A, B y C de la norma alemana DIN 51097, donde la C es la recomendada para bordes de piscina, o la clasificación PN18 en Francia).</p>
""" + fig("borde-piscina-resineo-terracota.webp", "Borde de piscina desbordante con pavimento drenante Résineo en tono terracota y tumbonas", "Borde de piscina con moqueta de piedra drenante en tono terracota. Imagen: Résineo.", (1200, 900)) + """  <h2>Opciones de suelo para el borde de la piscina</h2>
  <div class="art-table-wrap">
    <table class="art-table">
      <thead><tr><th>Suelo</th><th>Agarre mojado</th><th>Charcos</th><th>Juntas</th><th>A tener en cuenta</th></tr></thead>
      <tbody>
        <tr><th>Gres porcelánico antideslizante</th><td>Bueno si es clase 3</td><td>Sí, si no hay pendiente</td><td>Muchas</td><td>Fácil de encontrar; elegir siempre clase 3 / exterior</td></tr>
        <tr><th>Piedra natural (abujardada, flameada)</th><td>Bueno</td><td>Según pendiente</td><td>Sí</td><td>Bonita, pero puede calentarse y manchar</td></tr>
        <tr><th>Madera o composite</th><td>Medio</td><td>Drena entre lamas</td><td>Lamas</td><td>Mantenimiento; la madera se agrisa y se astilla</td></tr>
        <tr><th>Hormigón impreso</th><td>Medio</td><td>Sí</td><td>Pocas</td><td>Económico; pierde color y resbala si se pule</td></tr>
        <tr><th>Césped artificial</th><td>Bueno</td><td>Drena</td><td>No</td><td>Muy agradable; ideal en zonas de tumbonas</td></tr>
        <tr><th>Moqueta de piedra drenante (Résineo)</th><td>Muy bueno (PN18)</td><td>No: el agua pasa a través</td><td>No</td><td>Se aplica sobre el suelo actual; tonos claros para el sol</td></tr>
      </tbody>
    </table>
  </div>
  <h2>La opción que más recomendamos: suelo drenante de piedra natural</h2>
  <p>La <strong>moqueta de piedra</strong> es un pavimento continuo formado en un 95-97 % por granos de mármol o cuarzo unidos con resina de poliuretano transparente. Entre grano y grano quedan poros por los que el agua <strong>pasa hacia abajo</strong> —de 30 a 50 litros por segundo y metro cuadrado—, así que no se forma lámina de agua y el pie agarra incluso recién salido de la piscina.</p>
  <p>Somos <strong>distribuidor oficial de Résineo para Canarias</strong>. Además de su agarre (clasificación PN18 para zonas de pies descalzos), tiene dos ventajas prácticas:</p>
  <ul>
    <li><strong>Sin obra:</strong> en la mayoría de los casos se aplica sobre la baldosa existente, con unos 10 mm de espesor.</li>
    <li><strong>Sin juntas:</strong> no hay rejuntado que se ennegrezca ni piezas que se levanten.</li>
  </ul>
""" + fig("borde-piscina-resineo-blanco.webp", "Terraza de piscina con pavimento drenante Résineo blanco y diseño geométrico a medida", "En tonos claros, el suelo drenante se calienta menos y admite diseños a medida. Imagen: Résineo.", (1200, 800)) + """  <div class="article-tip">
    <p><strong>Consejo para Canarias:</strong> elige tonos claros (perla, arena, blanco) para el borde y deja los oscuros para cenefas o detalles. Y asegúrate de que el suelo tenga una ligera pendiente (1-2 %) hacia un desagüe.</p>
  </div>
  <h2>¿Y el césped artificial junto a la piscina?</h2>
  <p>Es una opción excelente para la zona de tumbonas y el jardín que rodea la piscina: drena, no resbala y es muy agradable al tacto. Lo contamos en <a href="cesped-artificial-piscina.html">césped artificial para piscinas</a> y puedes verlo en nuestro <a href="caso-exito-cesped-artificial-carrizal.html">caso de éxito en Carrizal</a>.</p>
  <h2>¿Quieres renovar el borde de tu piscina?</h2>
  <p>Te asesoramos sobre la mejor opción para tu caso y te enseñamos muestras reales. Más información en <a href="../suelos-resineo.html">suelo Résineo en Canarias</a> o en la web de <a href="https://resineocanarias.com/piscinas" target="_blank" rel="noopener">Résineo Canarias</a>. ¿Prefieres una piscina entera con efecto playa? Mira la <a href="piscina-de-arena-vs-gresite.html">comparativa piscina de arena vs gresite</a>.</p>
"""

out2 = build(
    "suelo-antideslizante-borde-piscina",
    "Suelo antideslizante para el borde de la piscina | Apavi Green",
    "Qué suelo poner en el borde de la piscina para que no resbale: normativa (clase 3 del CTE), comparativa de gres, piedra, madera, césped y suelo drenante, y consejos para Canarias.",
    "Suelo antideslizante para el borde de la piscina: opciones y normativa | Apavi Green",
    "Suelo antideslizante para el borde de la piscina: opciones y cuál elegir",
    "Qué suelo resbala menos con los pies mojados, qué exige la normativa y qué conviene en el clima de Canarias para que el borde de tu piscina sea seguro.",
    "Piscinas", "2026-10-07", "7 octubre 2026", 6,
    "borde-piscina-resineo-terracota.webp", "Borde de piscina con suelo drenante antideslizante en tono terracota", (1200, 900),
    BODY2, FAQ2,
    "¿Renovamos el <em>borde de tu piscina</em>?",
    "Te enseñamos muestras y te enviamos presupuesto en menos de 24h. Sin compromiso.")

# ------------------------------------------------------------- posts.json
pj = ROOT / "blog/posts.json"
posts = json.loads(pj.read_text(encoding="utf-8"))
new = [
    {"id": 10, "slug": "suelo-antideslizante-borde-piscina", "titulo": "Suelo antideslizante para el borde de la piscina: opciones y cuál elegir",
     "categoria": "Piscinas", "fecha": "2026-10-07",
     "extracto": "Qué suelo resbala menos con los pies mojados, qué exige la normativa y qué conviene en el clima de Canarias para que el borde de tu piscina sea seguro.",
     "imagen": "../assets/img/blog/piscinas/borde-piscina-resineo-terracota.webp", "url": "blog/suelo-antideslizante-borde-piscina.html"},
    {"id": 9, "slug": "piscina-de-arena-vs-gresite", "titulo": "Piscina de arena vs gresite: diferencias y cuál elegir",
     "categoria": "Piscinas", "fecha": "2026-10-07",
     "extracto": "Comparamos aspecto, formas, entrada al agua, juntas, mantenimiento y precio de la piscina de arena y la de gresite, y te contamos cuándo conviene cada una.",
     "imagen": "../assets/img/blog/piscinas/piscina-arena-bio-design-mar.webp", "url": "blog/piscina-de-arena-vs-gresite.html"},
]
slugs = {p["slug"] for p in posts}
posts = [p for p in new if p["slug"] not in slugs] + posts
pj.write_text(json.dumps(posts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- sitemap
sm = ROOT / "sitemap.xml"
t = sm.read_text(encoding="utf-8")
for s in ("piscina-de-arena-vs-gresite", "suelo-antideslizante-borde-piscina"):
    if f"blog/{s}.html" not in t:
        t = t.replace("</urlset>", f"""  <url>
    <loc>{BASE}/blog/{s}.html</loc>
    <lastmod>2026-10-07</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>""", 1)
sm.write_text(t, encoding="utf-8")
print("ok", len(out1), len(out2))
