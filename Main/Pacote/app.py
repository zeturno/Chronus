from BackEnd.extensoes import caminhos_arquivos, send_file, request, Flask, os, time, io
app = Flask(__name__)

@app.route('/')
def home():
    arquivo = caminhos_arquivos("index.html")  # pode ser bytes ou caminho

    if isinstance(arquivo, bytes):
        # bytes: cria um arquivo em memória para o Flask enviar
        return send_file(io.BytesIO(arquivo), mimetype='text/html')
    else:
        # caminho de arquivo: serve normal
        return send_file(arquivo)

@app.route("/shutdown_now", methods = ["POST"])
def desligar_API():
    resposta_JS = request.get_json()
    if resposta_JS["Desligar"] == "Start":
        os.system("shutdown /s /t 0")
        print("Simulação ok")
        time.sleep(60)
        return 200
    else:
        print("erro na requisição!")
        return 400