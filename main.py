""" This is the main 

    Just an example query
    https://test.casarocco.keenetic.link/insert?user=someusername@mail.com&game=League%20of%20Legends&time=10&desc=blablablablablalba&pstyle=acazzo&region=ITA&skill=Tank&plat=PC&mode=Draft%20pick
"""

from http.server import HTTPServer
from server.handler import ServerHandler

HOST_NAME = ""
SERVER_PORT = 9000

if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), ServerHandler)

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
