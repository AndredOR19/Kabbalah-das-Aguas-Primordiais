#!/usr/bin/env python3
"""
Servidor HTTP simples para o Atlas do Verbo Encarnado
Resolve problemas de CORS com arquivos locais
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os
from pathlib import Path

class AtlasHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Log personalizado
        if 'estado_atual.json' in args[0]:
            print(f"🔄 Atlas consultou estado: {args[0]}")
        elif 'GET' in args[0] and 'atlas_anatomico_3d.html' in args[0]:
            print(f"🌐 Atlas carregado: {args[0]}")

class ServidorAtlas:
    def __init__(self, port=8000):
        self.port = port
        self.server = None
        self.server_thread = None
        
    def iniciar(self):
        """Inicia o servidor HTTP"""
        try:
            # Mudar para o diretório do projeto
            os.chdir(Path(__file__).parent)
            
            # Criar servidor
            handler = AtlasHTTPRequestHandler
            self.server = socketserver.TCPServer(("", self.port), handler)
            
            print(f"🌐 Servidor Atlas iniciado em: http://localhost:{self.port}")
            print(f"📁 Servindo arquivos de: {Path.cwd()}")
            
            # Iniciar em thread separada
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao iniciar servidor: {e}")
            return False
    
    def parar(self):
        """Para o servidor HTTP"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print("🛑 Servidor Atlas parado")
    
    def abrir_atlas(self):
        """Abre o Atlas no navegador"""
        url = f"http://localhost:{self.port}/atlas_anatomico_3d.html"
        print(f"🚀 Abrindo Atlas em: {url}")
        
        try:
            webbrowser.open(url)
            return True
        except Exception as e:
            print(f"❌ Erro ao abrir navegador: {e}")
            return False
    
    def executar_com_atlas(self):
        """Executa servidor e abre Atlas"""
        if self.iniciar():
            time.sleep(1)  # Aguardar servidor inicializar
            
            if self.abrir_atlas():
                print("\n✅ Atlas do Verbo Encarnado está rodando!")
                print("🔄 O servidor ficará ativo para servir o Atlas")
                print("📡 Monitorando requisições do estado_atual.json...")
                print("\n💡 Dicas:")
                print("   - Use demo_ponte_completa.py para testar a ponte")
                print("   - O Atlas atualiza automaticamente a cada 2 segundos")
                print("   - Pressione Ctrl+C para parar o servidor")
                
                try:
                    # Manter servidor ativo
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\n🛑 Parando servidor...")
                    self.parar()
            else:
                self.parar()
        else:
            print("❌ Não foi possível iniciar o servidor")

def main():
    import sys
    
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Porta inválida, usando porta padrão 8000")
    
    servidor = ServidorAtlas(port)
    servidor.executar_com_atlas()

if __name__ == "__main__":
    main()