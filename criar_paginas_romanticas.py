import os

pasta = r"C:\Users\victo\OneDrive\Área de Trabalho\Victor"

nosdesdeentao_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Desde o primeiro olhar até agora...</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    body {
      background: #fff6fa;
      font-family: 'Segoe UI', Arial, sans-serif;
      color: #a14a76;
      margin: 0;
      padding: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    h1 {
      margin-top: 40px;
      font-size: 2.2em;
      font-weight: 600;
      text-align: center;
      letter-spacing: 1px;
      color: #d16ba5;
      text-shadow: 0 2px 8px #fff0f7;
    }
    .carousel-container {
      margin: 40px 0 20px 0;
      background: #fff;
      border-radius: 24px;
      box-shadow: 0 8px 32px rgba(209, 107, 165, 0.10), 0 2px 8px #f8e1ec;
      width: 90vw;
      max-width: 480px;
      min-height: 350px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      overflow: hidden;
      transition: box-shadow 0.3s;
    }
    .carousel-slide {
      width: 100%;
      height: 350px;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      position: absolute;
      top: 0;
      left: 0;
      transition: opacity 0.7s;
      z-index: 1;
    }
    .carousel-slide.active {
      opacity: 1;
      position: relative;
      z-index: 2;
    }
    .carousel-slide img, .carousel-slide video {
      max-width: 95%;
      max-height: 320px;
      border-radius: 18px;
      box-shadow: 0 4px 24px #f8e1ec;
      background: #fff;
      object-fit: cover;
    }
    .carousel-controls {
      width: 100%;
      display: flex;
      justify-content: space-between;
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      z-index: 3;
      pointer-events: none;
    }
    .carousel-btn {
      background: rgba(209, 107, 165, 0.15);
      border: none;
      border-radius: 50%;
      width: 44px;
      height: 44px;
      font-size: 2em;
      color: #d16ba5;
      cursor: pointer;
      box-shadow: 0 2px 8px #f8e1ec;
      transition: background 0.2s, transform 0.2s;
      pointer-events: all;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
    }
    .carousel-btn:hover {
      background: #f8e1ec;
      transform: scale(1.1);
    }
    .carousel-indicators {
      display: flex;
      justify-content: center;
      margin: 18px 0 10px 0;
      gap: 8px;
    }
    .carousel-indicator {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #f8e1ec;
      border: 2px solid #d16ba5;
      opacity: 0.5;
      cursor: pointer;
      transition: opacity 0.2s, background 0.2s;
    }
    .carousel-indicator.active {
      background: #d16ba5;
      opacity: 1;
    }
    .back-btn {
      margin: 40px 0 30px 0;
      padding: 12px 32px;
      background: linear-gradient(90deg, #d16ba5 0%, #c777b9 100%);
      color: #fff;
      border: none;
      border-radius: 18px;
      font-size: 1.1em;
      font-weight: 500;
      cursor: pointer;
      box-shadow: 0 2px 8px #f8e1ec;
      transition: background 0.2s, transform 0.2s;
    }
    .back-btn:hover {
      background: linear-gradient(90deg, #c777b9 0%, #d16ba5 100%);
      transform: scale(1.04);
    }
    @media (max-width: 600px) {
      .carousel-container {
        max-width: 98vw;
        min-height: 220px;
      }
      .carousel-slide {
        height: 220px;
      }
      .carousel-slide img, .carousel-slide video {
        max-height: 180px;
      }
    }
  </style>
</head>
<body>
  <h1>Desde o primeiro olhar até agora... nossa história em imagens.</h1>
  <div class="carousel-container" id="carousel">
    <!-- Slides serão inseridos via JS -->
    <div class="carousel-controls">
      <button class="carousel-btn" id="prevBtn" aria-label="Anterior">&#10094;</button>
      <button class="carousel-btn" id="nextBtn" aria-label="Próximo">&#10095;</button>
    </div>
    <!-- Indicadores -->
    <div class="carousel-indicators" id="carouselIndicators"></div>
  </div>
  <button class="back-btn" onclick="window.location.href='principal.html'">Voltar à Página Principal</button>

  <script>
    // Lista de arquivos da galeria (adicione aqui os nomes dos arquivos, na ordem desejada)
    const slides = [
      // Fotos (ordem cronológica, nomes de exemplo)
      { type: 'img', src: 'Galeria/01-01-2023 (1).jpg', date: '01-01-2023' },
      { type: 'img', src: 'Galeria/14-02-2023 (1).jpg', date: '14-02-2023' },
      { type: 'img', src: 'Galeria/14-02-2023 (2).jpg', date: '14-02-2023' },
      { type: 'img', src: 'Galeria/01-03-2023 (1).jpg', date: '01-03-2023' },
      // Vídeos (nomes de exemplo)
      { type: 'video', src: 'Galeria/video1.mp4', date: '10-03-2023' },
      { type: 'img', src: 'Galeria/01-04-2023 (1).jpg', date: '01-04-2023' },
      { type: 'video', src: 'Galeria/video2.mp4', date: '20-04-2023' },
      // ...adicione mais arquivos conforme necessário
    ];

    // Função para criar slides dinamicamente
    function createSlides() {
      const carousel = document.getElementById('carousel');
      slides.forEach((slide, idx) => {
        const div = document.createElement('div');
        div.className = 'carousel-slide';
        if (idx === 0) div.classList.add('active');
        if (slide.type === 'img') {
          const img = document.createElement('img');
          img.src = slide.src;
          img.alt = `Foto ${slide.date}`;
          div.appendChild(img);
        } else if (slide.type === 'video') {
          const video = document.createElement('video');
          video.src = slide.src;
          video.controls = true;
          video.autoplay = false;
          video.loop = true;
          video.style.background = "#f8e1ec";
          div.appendChild(video);
        }
        carousel.insertBefore(div, carousel.querySelector('.carousel-controls'));
      });
    }

    // Função para criar indicadores
    function createIndicators() {
      const indicators = document.getElementById('carouselIndicators');
      slides.forEach((_, idx) => {
        const dot = document.createElement('div');
        dot.className = 'carousel-indicator' + (idx === 0 ? ' active' : '');
        dot.addEventListener('click', () => showSlide(idx));
        indicators.appendChild(dot);
      });
    }

    let currentSlide = 0;
    let autoPlayInterval = null;

    function showSlide(idx) {
      const allSlides = document.querySelectorAll('.carousel-slide');
      const allDots = document.querySelectorAll('.carousel-indicator');
      if (idx < 0) idx = slides.length - 1;
      if (idx >= slides.length) idx = 0;
      allSlides.forEach((slide, i) => {
        slide.classList.toggle('active', i === idx);
        // Pausa vídeos que não estão ativos
        if (slide.querySelector('video')) {
          slide.querySelector('video').pause();
        }
      });
      allDots.forEach((dot, i) => {
        dot.classList.toggle('active', i === idx);
      });
      // Se for vídeo, dá play automático
      const activeSlide = allSlides[idx];
      if (slides[idx].type === 'video') {
        const video = activeSlide.querySelector('video');
        if (video) video.play();
      }
      currentSlide = idx;
    }

    function nextSlide() {
      showSlide(currentSlide + 1);
    }
    function prevSlide() {
      showSlide(currentSlide - 1);
    }

    function startAutoPlay() {
      autoPlayInterval = setInterval(() => {
        nextSlide();
      }, 4000);
    }
    function stopAutoPlay() {
      clearInterval(autoPlayInterval);
    }

    // Inicialização
    createSlides();
    createIndicators();
    document.getElementById('nextBtn').onclick = () => { nextSlide(); stopAutoPlay(); startAutoPlay(); };
    document.getElementById('prevBtn').onclick = () => { prevSlide(); stopAutoPlay(); startAutoPlay(); };

    // Autoplay
    startAutoPlay();

    // Pausa autoplay ao passar mouse
    document.getElementById('carousel').addEventListener('mouseenter', stopAutoPlay);
    document.getElementById('carousel').addEventListener('mouseleave', startAutoPlay);

    // Fade-in inicial
    window.onload = () => {
      document.body.style.opacity = 1;
    };
  </script>
</body>
</html>
"""

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
    <button class="btn" onclick="window.location.href='qrcode.html'">
      <!-- Ícone de QR Code -->
      <svg viewBox="0 0 24 24"><path d="M3 3h8v8H3V3zm2 2v4h4V5H5zm6 0h2v2h-2V5zm4 0h2v2h-2V5zm2 2h2v2h-2V7zm-2 2h2v2h-2V9zm-2 2h2v2h-2v-2zm-2 2h2v2h-2v-2zm-2 2h2v2H7v-2zm-2 2h2v2H5v-2zm0 2v2h2v-2H5zm2 2h2v2H7v-2zm2 2h2v2h-2v-2zm2 2h2v2h-2v-2zm2 2h2v2h-2v-2zm2 2h2v2h-2v-2zm2 2h2v2h-2v-2z"/></svg>
      Ir para o QR Code
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

# Criação dos arquivos
with open(os.path.join(pasta, "nosdesdeentao.html"), "w", encoding="utf-8") as f:
    f.write(nosdesdeentao_html.strip())
print("Arquivo nosdesdeentao.html criado/atualizado.")

with open(os.path.join(pasta, "principal.html"), "w", encoding="utf-8") as f:
    f.write(principal_html.strip())
print("Arquivo principal.html criado/atualizado.")

print("\nTudo pronto! Agora personalize os nomes das imagens e vídeos conforme suas pastas Galeria/ e GaleriaPrincipal/.\n")