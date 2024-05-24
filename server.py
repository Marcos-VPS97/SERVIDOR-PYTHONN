from http.server import BaseHTTPRequestHandler, HTTPServer

# Defina o endereço e a porta do servidor
HOST = "0.0.0.0"
PORT = 8000

class MeuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Envia a linha de status
        self.send_response(200)
        # Envia os cabeçalhos, incluindo a codificação UTF-8
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        # Conteúdo da mensagem
        mensagem = "<html><body><h1>Olá, Mundo!</h1><p>Este é um servidor HTTP simples em Python com UTF-8.</p></body></html>"
        # Escreve a resposta com codificação UTF-8
        self.wfile.write(mensagem.encode("utf-8"))
        return

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MeuHandler)
    print(f"Servidor rodando em http://{HOST}:{PORT}")
    server.serve_forever()
