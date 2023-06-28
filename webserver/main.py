""" This is the main 

    Just an example query
    https://yourdomain.something/insert?user=someusername@mail.com&game=League%20of%20Legends&time=10&desc=blablablablablalba&mic=true&region=ITA&pnumber=2&skills=Top&skills=Bottom&plat=PC&mode=Draft%20pick
    https://yourdomain.something/insert?user=someusername@mail.com&game=Counter%20Strike:%20GO&time=10&desc=blablablablablalba&mic=true&region=ITA&pnumber=2&skills=Fluid%20Roles&plat=PC&mode=Competitive
    https://yourdomain.somwthing/insert?user=someusername@mail.com&game=Rainbow%20Six%20Siege&time=10&desc=blablablablablalba&mic=true&region=ITA&pnumber=1&skills=Fragger&plat=PC&mode=Unranked
"""
import ssl
from http.server import HTTPServer
from server.handler import ServerHandler

HOST_NAME = ""
SERVER_PORT = 8443

if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), ServerHandler)

    sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sslctx.check_hostname = False
    sslctx.load_cert_chain(certfile='samplecert.pem', keyfile="samplekey.pem")
    webServer.socket = sslctx.wrap_socket(webServer.socket, server_side=True)

    if HOST_NAME != "":
        print(f"Server listening on {HOST_NAME}:{SERVER_PORT}")
    else:
        print(f"Server listening on 0.0.0.0:{SERVER_PORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
