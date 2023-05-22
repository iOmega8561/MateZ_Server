""" This module contains the user dataclass """

import hashlib
import re
from dataclasses import dataclass

class UserError(Exception):
    """ This exception will be raised by the ServerUsers class methods """

@dataclass
class User:
    """ This class represents the user data model """

    username: str
    hashedpass: str
    avatar: str

    def repr_json(self):
        """ This method gets called to get the dict rapresentation of the object """

        return dict(
            username = self.username,
            hashedpass = self.hashedpass,
            avatar = self.avatar
        )

@dataclass
class ServerUsers:
    """ This will be the template for the server's shared object """

    users: dict[str, User]

    def repr_json(self):
        """ This method gets called to encode the shared object in JSON """

        return dict(users = self.users)

    def delete_user(self, username):
        """ This method gets called to delete a user from the dictionary """

        if len(str(username)) < 1 \
                or username not in self.users:
            raise UserError("Invalid username")

        self.users.pop(username)

    def retrieve_user(self, query):
        """ This method gets called to retrieve a user object from the dictionary """

        if "username" not in query \
                or len(str(query["username"][0])) < 1 \
                or query["username"][0] not in self.users:
            raise UserError("Invalid username")

        if "password" not in query \
                or len(str(query["password"][0])) < 1:
            raise UserError("Invalid password")

        _username = query["username"][0]
        _enc_pass = query["password"][0].encode()
        _hash_pass = hashlib.md5(_enc_pass).hexdigest()

        if self.users[_username].hashedpass != _hash_pass:
            raise UserError("Invalid password")

        return self.users[_username]

    def update_user(self, query):
        """ This method gets called to update a user object in the dictionary """

        if len(query) < 2:
            raise UserError("Not enough query parameters")

        if "username" not in query \
                or len(str(query["username"][0])) < 1 \
                or query["username"][0] not in self.users:
            raise UserError("Invalid username")

        if "avatar" not in query \
                or len(str(query["avatar"][0])) < 1:
            raise UserError("Invalid avatar")

        _username = query["username"][0]

        self.users[_username].avatar = query["avatar"][0]

        return self.users[_username]

    def add_user(self, query):
        """ This method gets called to add a new user to the dictionary """

        if len(query) < 2:
            raise UserError("Not enough query parameters")

        if "username" not in query \
                or len(str(query["username"][0])) < 1:
            raise UserError("Invalid or missing username")

        _regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')

        if _regex.search(query["username"][0]) is not None:
            raise UserError("Invalid username chars")

        if query["username"][0] in self.users:
            raise UserError("User exists already")

        if "password" not in query \
                or len(str(query["password"][0])) < 1:
            raise UserError("Invalid or missing password")

        _username = query["username"][0]
        _enc_pass = query["password"][0].encode()
        _hash_pass = hashlib.md5(_enc_pass).hexdigest()

        self.users[_username] = User(
            username = _username,
            hashedpass = _hash_pass,
            avatar = "user_generic"
        )

        return _username
