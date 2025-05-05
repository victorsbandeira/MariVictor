import os

pasta = r"C:\Users\victo\OneDrive\Área de Trabalho\Victor"
principal_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Página Principal</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    body {
      background: #fffbe7;
      font-family: 'Segoe UI', Arial, sans-serif;
      margin: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .frase-romantica {
      margin-top: 40px;
      font-size: 1.7em;
      color: #d16ba5;
      text-align: center;
      font-weight: 500;
      text-shadow: 0 2px 8px #fff0f7;
      letter-spacing: 1px;
    }
    .polaroids-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 32px;
      margin: 40px 0 30px 0;
      width: 90vw;
      max-width: 900px;
    }
    .polaroid {
      background: #fff;
      border: 6px solid #fff;
      border-radius: 18px;
      box-shadow: 0 8px 32px rgba(209, 107, 165, 0.10), 0 2px 8px #f8e1ec;
      padding: 10px 10px 30px 10px;
      width: 160px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transform: rotate(-3deg);
      transition: transform 0.3s, box-shadow 0.3s;
      position: relative;
      opacity: 0;
      animation: fadeInPolaroid 1s forwards;
    }
    .polaroid:nth-child(2) { transform: rotate(2deg); animation-delay: 0.2s; }
    .polaroid:nth-child(3) { transform: rotate(-5deg); animation-delay: 0.4s; }
    .polaroid:nth-child(4) { transform: rotate(4deg); animation-delay: 0.6s; }
    .polaroid img {
      width: 100%;
      height: 140px;
      object-fit: cover;
      border-radius: 10px;
      box-shadow: 0 2px 8px #f8e1ec;
    }
    .polaroid-caption {
      margin-top: 10px;
      font-size: 1em;
      color: #a14a76;
      text-align: center;
      font-style: italic;
    }
    @keyframes fadeInPolaroid {
      from { opacity: 0; transform: translateY(40px) scale(0.95); }
      to { opacity: 1; }
    }
    .botoes-container {
      display: flex;
      flex-direction: row;
      gap: 24px;
      margin: 40px 0 30px 0;
      justify-content: center;
    }
    .btn {
      padding: 18px 36px;
      font-size: 1.1em;
      border: none;
      border-radius: 14px;
      background: linear-gradient(90deg, #d16ba5 0%, #c777b9 100%);
      color: #fff;
      cursor: pointer;
      font-weight: 500;
      box-shadow: 0 2px 8px #f8e1ec;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: background 0.2s, transform 0.2s;
    }
    .btn:hover {
      background: linear-gradient(90deg, #c777b9 0%, #d16ba5 100%);
      transform: scale(1.04);
    }
    .btn svg {
      width: 1.3em;
      height: 1.3em;
      fill: #fff;
    }
    @media (max-width: 700px) {
      .polaroids-container { gap: 16px; }
      .polaroid { width: 110px; padding-bottom: 18px; }
      .polaroid img { height: 80px; }
    }
  </style>
</head>
<body>
  <div class="frase-romantica">
    Nosso amor em pequenos momentos espalhados por aqui 💕
  </div>
  <div class="polaroids-container">
    <!-- Polaroids: adicione/remova conforme desejar -->
    <div class="polaroid">
      <img src="GaleriaPrincipal/polaroid1.jpg" alt="Momento especial 1">
      <div class="polaroid-caption">Nosso primeiro encontro</div>
    </div>
    <div class="polaroid">
      <img src="GaleriaPrincipal/polaroid2.jpg" alt="Momento especial 2">
      <div class="polaroid-caption">Aquele sorriso inesquecível</div>
    </div>
    <div class="polaroid">
      <img src="GaleriaPrincipal/polaroid3.jpg" alt="Momento especial 3">
      <div class="polaroid-caption">Nosso passeio favorito</div>
    </div>
    <div class="polaroid">
      <img src="GaleriaPrincipal/polaroid4.jpg" alt="Momento especial 4">
      <div class="polaroid-caption">Um dia só nosso</div>
    </div>
    <!-- Adicione mais polaroids se quiser -->
  </div>
  <div class="botoes-container">
    <button class="btn" onclick="window.location.href='nosdesdeentao.html'">
      <!-- Ícone de coração/álbum -->
      <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41 0.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
      Nós, desde então!
    </button>
    <button class="btn" onclick="window.location.href='index.html'">
      <!-- Ícone de mapa/roteiro -->
      <svg viewBox="0 0 24 24"><path d="M3.5 6.5l7-2 7 2V19.5l-7 2-7-2V6.5zm7-3.5l-8 2.3v15.4l8 2.3 8-2.3V5.3l-8-2.3zm0 2.1l6 1.7v13.6l-6 1.7-6-1.7V6.8l6-1.7z"/></svg>
      Roteiro da Viagem
    </button>
  </div>
</body>
</html>
"""

with open(os.path.join(pasta, "principal.html"), "w", encoding="utf-8") as f:
    f.write(principal_html.strip())

print("Arquivo principal.html atualizado com sucesso!")