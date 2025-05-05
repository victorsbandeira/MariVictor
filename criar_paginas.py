import os

# Caminho da pasta onde os arquivos serão criados
pasta = r"C:\Users\victo\OneDrive\Área de Trabalho\Victor"

arquivos = {
    "principal.html": """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Página Principal</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #fffbe7;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    .btn {
      padding: 20px 40px;
      margin: 20px;
      font-size: 1.2em;
      border: none;
      border-radius: 8px;
      background: #ffb347;
      color: #fff;
      cursor: pointer;
      transition: background 0.2s;
    }
    .btn:hover {
      background: #ff8800;
    }
  </style>
</head>
<body>
  <button class="btn" onclick="window.location.href='qrcode.html'">Ir para o QR Code</button>
  <button class="btn" onclick="window.location.href='index.html'">Ir para o Roteiro da Viagem</button>
</body>
</html>
""",

    "qrcode.html": """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>QR Code - Declaração</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #fffbe7;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    #qrcode {
      margin: 40px 0;
    }
    .btn {
      padding: 10px 30px;
      font-size: 1em;
      border: none;
      border-radius: 8px;
      background: #ffb347;
      color: #fff;
      cursor: pointer;
      transition: background 0.2s;
    }
    .btn:hover {
      background: #ff8800;
    }
  </style>
</head>
<body>
  <h1>Escaneie para ver a declaração</h1>
  <div id="qrcode"></div>
  <button class="btn" onclick="window.location.href='principal.html'">Voltar para a Página Principal</button>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
  <script>
    // Gera o QR Code para a página de declaração
    var url = window.location.origin + window.location.pathname.replace('qrcode.html', 'declaracao.html');
    new QRCode(document.getElementById("qrcode"), url);
  </script>
</body>
</html>
""",

    "declaracao.html": """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Declaração</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 40px;
      background: #fffbe7;
      color: #333;
      max-width: 700px;
      margin: 0 auto;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .texto {
      font-size: 1.5em;
      line-height: 1.6;
      white-space: pre-line;
    }
    .btn {
      margin-top: 40px;
      padding: 10px 30px;
      font-size: 1em;
      border: none;
      border-radius: 8px;
      background: #ffb347;
      color: #fff;
      cursor: pointer;
      transition: background 0.2s;
      align-self: flex-start;
    }
    .btn:hover {
      background: #ff8800;
    }
  </style>
</head>
<body>
  <h1>Para o amor da minha vida</h1>
  <div class="texto">
And I thank God every day
For the girl He sent my way
But I know the things He gives me
He can take away
And I hold you every night
And that's a feeling I wanna get used to
But there's no man as terrified
As the man who stands to lose you
  </div>
  <button class="btn" onclick="window.location.href='principal.html'">Voltar para a Página Principal</button>
</body>
</html>
"""
}

for nome, conteudo in arquivos.items():
    caminho = os.path.join(pasta, nome)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"Arquivo criado: {caminho}")

print("\nTodos os arquivos foram criados com sucesso!")