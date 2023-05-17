""" This module contains the user dataclass """

import hashlib
import re
from dataclasses import dataclass

MAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class UserError(Exception):
    """ This exception will be raised by the ServerUsers class methods """

@dataclass
class User:
    """ This class represents the user data model """

    email: str
    username: str
    hashedpass: str

    def repr_json(self):
        """ This method gets called to get the dict rapresentation of the object """

        return dict(
            email = self.email,
            username = self.username,
            hashedpass = self.hashedpass
        )

@dataclass
class ServerUsers:
    """ This will be the template for the server's shared object """

    users: dict[str, User]

    def repr_json(self):
        """ This method gets called to encode the shared object in JSON """

        return dict(users = self.users)

    def delete_user(self, email):
        """ This method gets called to delete a user from the dictionary """

        if len(str(email)) < 1 \
                or email not in self.users:
            raise UserError("EMAIL not valid for deletion")

        self.users.pop(email)

    def retrieve_user(self, query):
        """ This method gets called to retrieve a user object from the dictionary """

        if "email" not in query \
                or len(str(query["email"][0])) < 1 \
                or query["email"][0] not in self.users:
            raise UserError("Invalid email")

        if "password" not in query \
                or len(str(query["password"][0])) < 1:
            raise UserError("Invalid password")

        _email = query["email"][0]
        _enc_pass = query["password"][0].encode()
        _hash_pass = hashlib.md5(_enc_pass).hexdigest()

        if self.users[_email].hashedpass != _hash_pass:
            raise UserError("Invalid password")

        return self.users[_email]

    def add_user(self, query):
        """ This method gets called to add a new user to the dictionary """

        if len(query) < 3:
            raise UserError("Not enough query parameters")

        if "email" not in query \
                or len(str(query["email"][0])) < 1:
            raise UserError("Invalid or missing email")

        if not re.fullmatch(MAIL_REGEX, query["email"][0]):
            raise UserError("Invalid email format")

        if query["email"][0] in self.users:
            raise UserError("User exists already")

        if "username" not in query \
                or len(str(query["username"][0])) < 1:
            raise UserError("Invalid or missing username")

        if "password" not in query \
                or len(str(query["password"][0])) < 1:
            raise UserError("Invalid or missing password")

        _email = query["email"][0]
        _enc_pass = query["password"][0].encode()
        _hash_pass = hashlib.md5(_enc_pass).hexdigest()

        self.users[_email] = User(
            email = _email,
            username = query["username"][0],
            hashedpass = _hash_pass
        )

        return _email
