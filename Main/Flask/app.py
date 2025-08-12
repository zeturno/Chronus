from extensões import app, caminhos_arquivos, send_file

@app.route('/')
def home():
    return send_file(caminhos_arquivos("index.html"))