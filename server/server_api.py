import sys
sys.dont_write_bytecode = True

from flask import jsonify
from flask              import Flask
from flask              import request
from flask_cors         import CORS

import json

from core.controller  import CreateUserController
from core.controller  import CreatePostController
from core.controller  import FollowUserController
from core.controller  import AuthUserController
from core.controller  import RetrieveFeedController
from core.controller  import RemoveFollowerController
from core.controller  import RemoveFollowedController
from core.controller  import ListPostsController
from core.controller  import ListFollowersController
from core.controller  import ListFollowedsController
from core.controller  import FindUserController
from core.controller  import UpdateUserController

from core.middlewares import EnsureAuthenticated

create_user_controller     = CreateUserController()
create_post_controller     = CreatePostController()
follow_user_controller     = FollowUserController()
auth_user_controller       = AuthUserController()
retrieve_feed_controller   = RetrieveFeedController()
remove_follower_controller = RemoveFollowerController()
remove_followed_controller = RemoveFollowedController()
list_post_controller       = ListPostsController()
list_followers_controller  = ListFollowersController()
list_followeds_controller  = ListFollowedsController()
find_user_controller       = FindUserController()
upade_user_controller      = UpdateUserController()

ensure_authenticated       = EnsureAuthenticated()


APP = Flask(__name__)

@APP.errorhandler(404)
def route_not_found(error):
    code, message = str(error).split(": ")
    return json.dumps(
        {
            "message": message, 
            "status_code": "404"
        }
    ), 404



# ================================ USER ROUTES ================================


@APP.route("/user/register", methods = ["POST"])
def register():
    if (request.method == "POST"):
        
        request_parsed = request.get_json() 
        username    = request_parsed["username"]
        password    = request_parsed["password"]
        description = request_parsed["description"]

        response = create_user_controller.handle(
            username, 
            password, 
            description
        )
        
        if (response):
            return json.dumps({ 
                "message": "success", "status_code": 200 
            })
        else: 
            return json.dumps({ 
                "message": "failed", "status_code": 400 
            })


@APP.route("/user/login", methods = ["GET"])
def login():

    if (request.method == "GET"):
        username = request.headers["username"]
        password = request.headers["password"]

        response = auth_user_controller.handle(
            username,
            password
        )

        if (response):
            return json.dumps({
                "message": "success", 
                "token": response,
                "status_code": 200
            }), 200
        else:
            return json.dumps({
                "message": "failed", 
                "token": "-1",
                "status_code": 400
            }), 400

# TODO: não deixar a coluna para ser passada como parametro
@APP.route("/user/update", methods = ["PUT"])
def update_user():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "PUT"):
            username = request.headers["username"]
            data     = request.headers["data"]
            column   = request.headers["column"]

            response = upade_user_controller.handle(
                username,
                data,
                column
            )

            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/user/get", methods = ["GET"])
def get_user():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "GET"):
            username = request.headers["username"]

            response = find_user_controller.handle(
                username,
            )

            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401


# ================================ FOLLOW ROUTES ================================


@APP.route("/follow_user", methods = ["POST"])
def follow_user():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "POST"):
            
            request_parsed = request.get_json()
            
            followed_username = request_parsed["followed_user"]
            follower_username = request_parsed["follower_user"]

            response = follow_user_controller.handle(
                followed_username,
                follower_username
            )
            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/follow_user/list/followers", methods = ["GET"])
def list_followers():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "GET"):
            followed_username = request.headers["username"]

            response = list_followers_controller.handle(
                followed_username
            )

            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401
    
@APP.route("/follow_user/list/followeds", methods = ["GET"])
def list_followeds():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "GET"):
            follower_username = request.headers["username"]

            response = list_followeds_controller.handle(
                follower_username
            )

            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/follow_user/remove/follower", methods = ["DELETE"])
def remove_follower():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "DELETE"):

            followed_username = request.headers["followed"]
            follower_username = request.headers["follower"]

            response = remove_follower_controller.handle(
                followed_username,
                follower_username
            )

            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401
    
@APP.route("/follow_user/remove/followed", methods = ["DELETE"])
def remove_followed():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "DELETE"):
            
            follower_username = request.headers["follower"]
            followed_username = request.headers["followed"]

            response = remove_followed_controller.handle(
                follower_username,
                followed_username
            )

            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401


# ================================ POST ROUTES ================================


@APP.route("/post/new", methods = ["POST"])
def create_post():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "POST"):
            
            request_parsed = request.get_json()
            
            username    = request_parsed["username"]
            description = request_parsed["description"]
            image       = request_parsed["image"]

            response = create_post_controller.handle(
                username,
                description,
                image
            )
            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/post/list", methods = ["GET"])
def list_posts():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "GET"):
            username = request.headers["username"]

            response = list_post_controller.handle(
                username
            )
            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401



# ================================ FEED ROUTES ================================


@APP.route("/feed/retrieve", methods = ["GET"])
def retrieve_feed():

    auth = ensure_authenticated.handle(
        request.headers["token"]
    )

    if (auth):
        if (request.method == "GET"):
            username = request.headers["username"]
            limit    = request.headers["post-limit"]

            response = RetrieveFeedController.handle(
                username,
                limit
            )
            return response, json.loads(response)["status_code"]
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401



if (__name__ == "__main__"):
    APP.run(debug=True, port=5006)
