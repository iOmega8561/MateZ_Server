""" This module contains the dataclasses for our server """

from dataclasses import dataclass
from uuid import uuid4
import json

from data.games import GAMES

class RequestException(Exception):
    """ This exception will be raised by the ServerRequest class methods """

class ComplexEncoder(json.JSONEncoder):
    """ This is a custom encoder for our mess """

    def default(self, o):
        if hasattr(o, "repr_json"):
            return o.repr_json()
        else:
            return json.JSONEncoder.default(self, o)

@dataclass
class UserRequest:
    """ Data class for user requests """

    uuid: str
    user_id: str
    game: str
    time: int
    desc: str
    pstyle: str
    region: str
    skill: str
    plat: str
    mode: str

    def repr_json(self):
        """ This method gets called to get the dict rapresentation of the object """

        return dict(
            uuid = self.uuid,
            user_id = self.user_id,
            game = self.game,
            time = self.time,
            desc = self.desc,
            pstyle = self.pstyle,
            region = self.region,
            skill = self.skill,
            plat = self.plat,
            mode = self.mode
        )

@dataclass
class ServerRquests:
    """ This will be the template for the server's shared object """

    requests: dict[str, UserRequest]

    def repr_json(self):
        """ This method gets called to encode the shared object in JSON """

        return dict(requests = self.requests)

    def delete_request(self, uuid):
        """ This method gets called to remove a request from the dictionary """

        if len(str(uuid)) < 1 or uuid not in self.requests:
            raise RequestException("UUID not valid for deletion")

        self.requests.pop(uuid)

    def add_request(self, query):
        """ This method gets called to add a request to the dictionary """

        if len(query) < 9:
            raise RequestException("Not enough query parameters")
        elif "user" not in query or len(str(query["user"][0])) < 1 :
            raise RequestException("Invalid or missing user identifier")
        elif "game" not in query or len(str(query["game"][0])) < 1 or query["game"][0] not in GAMES:
            raise RequestException("Invalid or missing game")
        elif "time" not in query or int(query["time"][0]) < 1:
            raise RequestException("Invalid or missing timeframe")
        elif "desc" not in query or len(str(query["desc"][0])) < 1:
            raise RequestException("Invalid or missing description")
        elif "pstyle" not in query or len(str(query["pstyle"][0])) < 1:
            raise RequestException("Invalid or missing playstyle")
        elif "region" not in query or len(str(query["region"][0])) < 1:
            raise RequestException("Invalid or missing region")
        elif "skill" not in query or query["skill"][0] not in GAMES[query["game"][0]].skills:
            raise RequestException("Invalid or missing skill")
        elif "plat" not in query or query["plat"][0] not in GAMES[query["game"][0]].plat:
            raise RequestException("Invalid or missing platform")
        elif "mode" not in query or query["mode"][0] not in GAMES[query["game"][0]].modes:
            raise RequestException("Invalid or missing gamemode")

        _uuid = str(uuid4())

        self.requests[_uuid] = UserRequest(
                _uuid,
                query["user"][0],
                query["game"][0],
                query["time"][0],
                query["desc"][0],
                query["pstyle"][0],
                query["region"][0],
                query["skill"][0],
                query["plat"][0],
                query["mode"][0]
            )
