import os
import random

# Caminhos
pasta = r"C:\Users\victo\OneDrive\Área de Trabalho\Victor\GaleriaPrincipal"
html_path = r"C:\Users\victo\OneDrive\Área de Trabalho\Victor\principal.html"

# Lista de imagens
arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# Parâmetros para espalhar as imagens
tops = [i for i in range(5, 80, 7)]
lefts = [i for i in range(5, 80, 8)]
widths = [120, 130, 140, 150, 160, 170, 180]
heights = [80, 90, 100, 110, 120, 130]
rotations = [-8, -6, -4, -2, 2, 4, 6, 8]
zindexes = [1, 2, 3, 4]

random.shuffle(tops)
random.shuffle(lefts)

# Gera HTML da colagem
collage_html = ['<div class="collage-bg">']
for idx, nome in enumerate(arquivos):
    classe = f"collage-img collage{idx+1}"
    collage_html.append(f'  <img src="GaleriaPrincipal/{nome}" class="{classe}" alt="">')
collage_html.append('</div>')
collage_html = '\n'.join(collage_html)

# Gera CSS da colagem
collage_css = [
    ".collage-bg {",
    "  position: fixed;",
    "  top: 0; left: 0; width: 100vw; height: 100vh;",
    "  z-index: 0;",
    "  pointer-events: none;",
    "  overflow: hidden;",
    "}",
    ".collage-img {",
    "  position: absolute;",
    "  border: 4px solid #fff;",
    "  box-shadow: 0 4px 16px #0002, 0 1px 4px #d16ba5aa;",
    "  border-radius: 10px;",
    "  opacity: 0.92;",
    "  object-fit: cover;",
    "  transition: filter 0.3s;",
    "}",
]
for idx, nome in enumerate(arquivos):
    top = random.choice(tops)
    left = random.choice(lefts)
    width = random.choice(widths)
    height = random.choice(heights)
    rot = random.choice(rotations)
    z = random.choice(zindexes)
    collage_css.append(f".collage{idx+1} "+"{"
               f" width: {width}px; height: {height}px;"
               f" top: {top}%; left: {left}%;"
               f" transform: rotate({rot}deg);"
               f" z-index: {z};"
               "}")
collage_css.append("""
@media (max-width: 900px) {
  .collage-img {
    width: 60px !important; height: 40px !important;
  }
}
""")
collage_css = '\n'.join(collage_css)

# Lê o HTML principal
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Insere o CSS no <head>
if "<style" in html:
    # Insere antes do fechamento do primeiro <style>
    html = html.replace("</style>", collage_css + "\n</style>", 1)
else:
    # Insere um novo <style> antes do </head>
    html = html.replace("</head>", f"<style>\n{collage_css}\n</style>\n</head>", 1)

# Insere o bloco da colagem logo após <body>
if "<body>" in html:
    html = html.replace("<body>", "<body>\n" + collage_html, 1)
else:
    # Se não encontrar <body>, insere no início
    html = collage_html + "\n" + html

# Salva o HTML modificado
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Colagem inserida diretamente no principal.html com sucesso!")