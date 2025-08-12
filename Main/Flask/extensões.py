from flask import Flask, redirect, url_for, session, abort, send_file, send_from_directory
import socket
import webview
from waitress import serve
import subprocess
import threading
import requests
import os
import sys
import time
import random
import string
#Modulos necessarios para rodar a aplicação sem erros!

app = Flask(__name__)
#objetos importante para rodar o App!

def caminhos_arquivos(Nome_HTML):
    caminho = os.path.dirname(__file__)
    caminho_abs = os.path.join(caminho,"..","Static", Nome_HTML)
    return caminho_abs

def porta_dinâmica(IP= "localhost",Porta = 0):
    #Argumentos para fornecer o IP que vai procurar a porta, caso queira uma porta fixa usar o número no argmento!
    while True:
    #cria um loop para funcionar apenas quando tiver uma porta aberta!
    
        try:
            canal = socket.socket()
            canal.bind((IP, Porta))
            porta = canal.getsockname()[1]
            canal.close()
            print(f"Porta aberta: {porta}, testando...")
             #Printa a porta no terminal para teste em rede local!

            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as verificar:
                 testar_porta = verificar.connect_ex((IP, porta))
                 #Caso a porta seja igual a zero significa que já está em uso, então tenta outra porta!
            if testar_porta == 0:
                print("Porta em Uso, testar outra!")
            
            else:
                print("Porta aberta, seguir com a requisição!")
                return porta
                
        except OSError as erro:
            print(f"Erro na parte de portas: {erro}")
            break

def Link_Start(Navegador, Porta = None ,IP = "localhost"):
    Porta = porta_dinâmica()
    abrir_threading = threading.Thread(target=lambda: serve(app,host = IP, port = Porta),daemon = True)
    abrir_threading.start()
    token = ''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(12))
    URL_local = f"http://{IP}:{Porta}/?token={token}"
    print(URL_local)
    teste_HTTP = requests.get(URL_local)

    while teste_HTTP.status_code != 200:
        teste_HTTP = requests.get(URL_local)
        print(f"Erro ao criar o servidor, tentando novamente em 5 segundos...")
        print(teste_HTTP.status_code)
        time.sleep(5)
        if teste_HTTP.status_code == 200:
            print(f"servidor online, tudo certo para servir, URL: {URL_local}")
            break
        else:
            print(f"Erro ao criar o servidor, tentando novamente em 5 segundos...")
            print(teste_HTTP.status_code)
            

    if Navegador == "pywebview":
        Config = {
            "width" : 420, "height" : 300
        }
        print(teste_HTTP.status_code)
        webview.create_window("Chronus", URL_local,**Config)
        webview.start()
        
    else:
        print("Aqui vai ficar o Electron!")

