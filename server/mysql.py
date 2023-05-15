""" This is the module with all the mysql stuff """

import json
import pymysql
from data.requests import UserRequest

CONNECTION = pymysql.connect("localhost",
                                "webapp",
                                "webapp",
                                "webapp",
                                cursorclass = pymysql.cursors.DictCursor)

class MySQLhandler:
    """ This class provides the interface for the mysql database """

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
                            result["description"],
                            True if result["mic"] == 1 else False, 
                            result["region"],
                            result["pnumber"],
                            json.loads(result["skills"]),
                            result["plat"],
                            result["gamemode"]
                        )

                    return requests
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")

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
                        (uuid, user_id, game, time, description, mic, region, pnumber, skills, plat, gamemode) \
                        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                    cursor.execute(sql, (
                        req.uuid,
                        req.user_id,
                        req.game,
                        int(req.time),
                        req.desc,
                        req.mic,
                        req.region,
                        int(req.pnumber),
                        json.dumps(req.skills),
                        req.plat,
                        req.mode
                    ))

                    CONNECTION.commit()
                except pymysql.Error as error:
                    print(f"MySQL error {error.args[0]}: {error.args[1]}")
