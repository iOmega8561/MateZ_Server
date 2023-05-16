""" This module contains the request dataclass and ServerRequest manager """

from dataclasses import dataclass
from uuid import uuid4
import json

from data.games import GAMES

class RequestError(Exception):
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

    # More than 7 instances are needed for our means

    uuid: str
    user_id: str
    game: str
    time: int
    mic: bool
    region: str
    pnumber: int
    skills: [str]
    plat: str
    mode: str

    def repr_json(self):
        """ This method gets called to get the dict rapresentation of the object """

        return dict(
            uuid = self.uuid,
            user_id = self.user_id,
            game = self.game,
            time = self.time,
            mic = self.mic,
            region = self.region,
            pnumber = self.pnumber,
            skills = self.skills,
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

        if len(str(uuid)) < 1 \
                or uuid not in self.requests:
            raise RequestError("UUID not valid for deletion")

        self.requests.pop(uuid)

    def add_request(self, query):
        """ This method gets called to add a request to the dictionary """

        _skill = False

        if len(query) < 8:
            raise RequestError("Not enough query parameters")

        if "user" not in query \
                or len(str(query["user"][0])) < 1 :
            raise RequestError("Invalid or missing user identifier")

        if "game" not in query \
                or len(str(query["game"][0])) < 1 \
                or query["game"][0] not in GAMES:
            raise RequestError("Invalid or missing game")

        if "time" not in query \
                or int(query["time"][0]) < 1:
            raise RequestError("Invalid or missing timeframe")

        if "mic" not in query \
                or (str(query["mic"][0]) != "true" \
                and str(query["mic"][0]) != "false"):
            raise RequestError("Invalid or missing mic")

        if "region" not in query \
                or len(str(query["region"][0])) < 1:
            raise RequestError("Invalid or missing region")

        if "plat" not in query \
                or query["plat"][0] not in GAMES[query["game"][0]].plat:
            raise RequestError("Invalid or missing platform")

        if "mode" not in query \
                or query["mode"][0] not in GAMES[query["game"][0]].modes:
            raise RequestError("Invalid or missing gamemode")

        if "pnumber" not in query \
                or int(query["pnumber"][0]) < 1:
            raise RequestError("Invalid or missing player number")

        if "skills" in query:
            for skill in query["skills"]:

                if skill not in GAMES[query["game"][0]].skills:
                    raise RequestError("Invalid or missing skill")

            _skill = True

        _uuid = str(uuid4())

        self.requests[_uuid] = UserRequest(
                _uuid,
                query["user"][0],
                query["game"][0],
                int(query["time"][0]),
                True if query["mic"][0] == "true" else False,
                query["region"][0],
                int(query["pnumber"][0]),
                query["skills"] if _skill else [],
                query["plat"][0],
                query["mode"][0]
            )

        return _uuid
