""" This module contains the ServerTemplate object wich
    is used to define all the handlers for our webserver """

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

from server.mysql import MySQLhandler
from data.requests import RequestError, ComplexEncoder, ServerRquests
from data.games import GAMES

class ServerHandler(BaseHTTPRequestHandler):
    """ Custom http request handler """

    _REQUESTS: ServerRquests = ServerRquests(requests = MySQLhandler.fetch_requests())

    def __send_status_message(self, code, message):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(bytes(
                        json.dumps({"answer": f"{message}"}),
                        "utf-8"))

    def __img(self, query_components):
        if "name" not in query_components:
            self.__send_status_message(404, "Failure")

        name = query_components["name"][0]

        try:
            with open(f"imgs/{name}.png", "rb") as img:
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.end_headers()
                self.wfile.write(img.read())
        except FileNotFoundError:
            self.__send_status_message(404, "Failure")

    def __games(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(
                        json.dumps({"games": GAMES},
                                    cls = ComplexEncoder),
                        "utf-8"))

    def __requests(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(
                        json.dumps(self._REQUESTS.repr_json(),
                                     cls = ComplexEncoder),
                        "utf-8"))

    def __insert(self, query_components):
        """ Handler for /insert route """

        try:
            _uuid = self._REQUESTS.add_request(query_components)
            MySQLhandler.insert_request(self._REQUESTS.requests[_uuid])
        except RequestError as _e:
            self.__send_status_message(400, _e.args[0])
            return

        self.__send_status_message(200, "Success")

    def __delete(self, query_components):
        """ Handler for /delete route """

        if "uuid" not in query_components:
            self.__send_status_message(400, "Failure")

        _uuid = query_components["uuid"][0]

        try:
            self._REQUESTS.delete_request(_uuid)
            MySQLhandler.delete_request(_uuid)
        except RequestError as _e:
            self.__send_status_message(400, _e.args[0])
            return

        self.__send_status_message(200, "Success")

    def __greet(self, query_components):
        """ Handler for /greet route """

        if "name" not in query_components:
            self.__send_status_message(400, "Failure")
            return

        self.__send_status_message(200, query_components["name"][0])

    # Parent class method naming does not conform to PEP8
    def do_GET(self):
        """ Default get method handler """

        parsed_url = urlparse(self.path)
        query_route = parsed_url.path
        query_components = parse_qs(parsed_url.query)

        if query_route == "/greet":
            self.__greet(query_components)

        elif query_route == "/img":
            self.__img(query_components)

        elif query_route == "/games":
            self.__games()

        elif query_route == "/requests":
            self.__requests()

        elif query_route == "/delete":
            self.__delete(query_components)

        elif query_route == "/insert":
            self.__insert(query_components)

        else:
            self.__send_status_message(404, "Route not found")
