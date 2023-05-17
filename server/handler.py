""" This module contains the ServerTemplate object wich
    is used to define all the handlers for our webserver """

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from uuid import uuid4
import json

from server.mysql import MySQLhandler
from data.requests import RequestError, ComplexEncoder, ServerRquests
from data.users import UserError, ServerUsers
from data.games import GAMES

class ServerHandler(BaseHTTPRequestHandler):
    """ Custom http request handler """

    _TOKENS: dict[str: str] = {}
    _USERS: ServerUsers = ServerUsers(users = MySQLhandler.fetch_users())
    _REQUESTS: ServerRquests = ServerRquests(requests = MySQLhandler.fetch_requests())

    def __send_status_message(self, code, string, message):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        if string:
            self.wfile.write(bytes(
                            json.dumps({"answer": f"{message}"}),
                            "utf-8"))
        else:
            self.wfile.write(bytes(message, "utf-8"))

    def __img(self, query_components):
        if "name" not in query_components:
            self.__send_status_message(404, True, "Failure")

        name = query_components["name"][0]

        try:
            with open(f"imgs/{name}.png", "rb") as img:
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.end_headers()
                self.wfile.write(img.read())
        except FileNotFoundError:
            self.__send_status_message(404, True, "Failure")

    def __games(self):
        self.__send_status_message(200, False, json.dumps({"games": GAMES},
                                                            cls = ComplexEncoder))

    def __requests(self):
        self.__send_status_message(200, False, json.dumps(self._REQUESTS.repr_json(),
                                                            cls = ComplexEncoder))

    def __insert(self, query_components):
        """ Handler for /insert route """

        try:
            _uuid = self._REQUESTS.add_request(query_components)
            MySQLhandler.insert_request(self._REQUESTS.requests[_uuid])
        except RequestError as _e:
            self.__send_status_message(400, True, _e.args[0])
            return

        self.__send_status_message(200, True, "Success")

    def __delete(self, query_components):
        """ Handler for /delete route """

        if "uuid" not in query_components:
            self.__send_status_message(400, True, "Failure")

        _uuid = query_components["uuid"][0]

        try:
            self._REQUESTS.delete_request(_uuid)
            MySQLhandler.delete_request(_uuid)
        except RequestError as _e:
            self.__send_status_message(400, True, _e.args[0])
            return

        self.__send_status_message(200, True, "Success")

    def __logout(self, query_components):
        """ Handler for /logout route """

        if "email" not in query_components \
                or len(str(query_components["email"][0])) < 1:
            self.__send_status_message(400, True, "Invalid email")

        elif query_components["email"][0] in self._TOKENS:
            self._TOKENS.pop(query_components["email"][0])
            self.__send_status_message(200, True, "Success")

    def __signup(self, query_components):
        """ Handler for /signup route """

        try:
            _email = self._USERS.add_user(query_components)
            MySQLhandler.insert_user(self._USERS.users[_email])
        except UserError as _e:
            self.__send_status_message(400, True, _e.args[0])
            return

        self.__send_status_message(200, True, "Success")

    def __signin(self, query_components):
        """ Handler for /signin route """

        try:
            _user = self._USERS.retrieve_user(query_components)
            self._TOKENS[_user.email] = uuid4()
        except UserError as _e:
            self.__send_status_message(400, True, _e.args[0])
            return

        self.__send_status_message(
            200,
            False,
            json.dumps({"answer": str(self._TOKENS[_user.email]), "user": _user}, 
                                                            cls = ComplexEncoder)
        )

    # Parent class method naming does not conform to PEP8
    def do_GET(self):
        """ Default get method handler """

        parsed_url = urlparse(self.path)
        query_route = parsed_url.path
        query_components = parse_qs(parsed_url.query)

        if query_route == "/signup":
            self.__signup(query_components)

        elif query_route == "/signin":
            self.__signin(query_components)

        elif query_route == "/logout":
            self.__logout(query_components)

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
            self.__send_status_message(404, True, "Route not found")
