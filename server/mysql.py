""" This is the module with all the mysql stuff """

import json
import pymysql
from data.requests import UserRequest
from data.users import User

CONNECTION = pymysql.connect("localhost",
                                "webapp",
                                "webapp",
                                "webapp",
                                cursorclass = pymysql.cursors.DictCursor)

class MySQLhandler:
    """ This class provides the interface for the mysql database """

    @staticmethod
    def fetch_users():
        """ This method will be used to fetch all User objects from remote database """

        with CONNECTION:
            with CONNECTION.cursor() as cursor:

                try:
                    sql = "select * from users"
                    cursor.execute(sql)
                    users = {}

                    for result in cursor.fetchall():
                        users[result["username"]] = User(
                            result["username"],
                            result["hashedpass"],
                            result["avatar"],
                            json.loads(result["fgames"])
                        )

                    return users
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")
                    return {}

    @staticmethod
    def delete_user(username: str):
        """ This method will be used to delete User objects from remote database """

        with CONNECTION:
            with CONNECTION.cursor() as cursor:

                try:
                    sql = "delete from users where username = %s"
                    cursor.execute(sql, (username))

                    CONNECTION.commit()
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")

    @staticmethod
    def update_user(user: User):
        """ This method will be used to update User objects in remote database """

        with CONNECTION:
            with CONNECTION.cursor() as cursor:

                try:
                    sql = "update users set avatar = %s, fgames = %s where username = %s"

                    cursor.execute(sql, (
                        user.avatar,
                        json.dumps(user.fgames),
                        user.username
                    ))

                    CONNECTION.commit()
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")

    @staticmethod
    def insert_user(user: User):
        """ This method will be used to send User objects to remote database """

        with CONNECTION:
            with CONNECTION.cursor() as cursor:

                try:
                    sql = "insert into users \
                        (username, hashedpass, avatar, fgames) \
                        values (%s, %s, %s, %s)"

                    cursor.execute(sql, (
                        user.username,
                        user.hashedpass,
                        user.avatar,
                        user.fgames
                    ))

                    CONNECTION.commit()
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")

    @staticmethod
    def fetch_requests():
        """ This method will be used to fetch all UserRequest objects from remote database """

        with CONNECTION:
            with CONNECTION.cursor() as cursor:

                try:
                    sql = "select * from requests"
                    cursor.execute(sql)
                    requests = {}

                    for result in cursor.fetchall():
                        requests[result["uuid"]] = UserRequest(
                            result["uuid"],
                            result["user_id"],
                            result["game"],
                            result["time"],
                            True if result["mic"] == 1 else False,
                            result["region"],
                            result["pnumber"],
                            json.loads(result["skills"]),
                            result["plat"],
                            result["gamemode"],
                            result["submitdate"].isoformat()
                        )

                    return requests
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")
                    return {}

    @staticmethod
    def delete_request(uuid: str):
        """ This method will be used to delete UserRequest objects from remote database """

        with CONNECTION:
            with CONNECTION.cursor() as cursor:

                try:
                    sql = "delete from requests where uuid = %s"
                    cursor.execute(sql, (uuid))

                    CONNECTION.commit()
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")

    @staticmethod
    def insert_request(req: UserRequest):
        """ This method will be used to send UserRequest objects to remote database """

        with CONNECTION:
            with CONNECTION.cursor() as cursor:

                try:
                    sql = "insert into requests \
                        (uuid, user_id, game, time, mic, region, pnumber, skills, plat, gamemode, submitdate) \
                        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                    cursor.execute(sql, (
                        req.uuid,
                        req.user_id,
                        req.game,
                        int(req.time),
                        req.mic,
                        req.region,
                        int(req.pnumber),
                        json.dumps(req.skills),
                        req.plat,
                        req.mode,
                        req.date
                    ))

                    CONNECTION.commit()
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")
