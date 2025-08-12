from extensões import app, caminhos_arquivos, send_file, request, jsonify, Flask, os

@app.route('/')
def home():
    return send_file(caminhos_arquivos("index.html"))

@app.route("/shutdown_now", methods = ["POST"])
def desligar_API():
    resposta_JS = request.get_json()
    if resposta_JS["Desligar"] == "Start":
        os.system("shutdown /s /t 0")
        return 200
    else:
        print("erro na requisição!")
        return 400