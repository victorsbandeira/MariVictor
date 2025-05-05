import os
import random

# Caminho da pasta com as imagens
pasta = r"C:\Users\victo\OneDrive\Área de Trabalho\Victor\GaleriaPrincipal"
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

# Gera HTML
html = ['<div class="collage-bg">']
for idx, nome in enumerate(arquivos):
    classe = f"collage-img collage{idx+1}"
    html.append(f'  <img src="GaleriaPrincipal/{nome}" class="{classe}" alt="">')
html.append('</div>')

with open("collage.html", "w", encoding="utf-8") as f:
    f.write('\n'.join(html))

# Gera CSS
css = [
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
    css.append(f".collage{idx+1} "+"{"
               f" width: {width}px; height: {height}px;"
               f" top: {top}%; left: {left}%;"
               f" transform: rotate({rot}deg);"
               f" z-index: {z};"
               "}")

css.append("""
@media (max-width: 900px) {
  .collage-img {
    width: 60px !important; height: 40px !important;
  }
}
""")

with open("collage.css", "w", encoding="utf-8") as f:
    f.write('\n'.join(css))

print("Arquivos 'collage.html' e 'collage.css' gerados com sucesso!")