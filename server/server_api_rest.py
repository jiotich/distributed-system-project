import sys
sys.dont_write_bytecode = True
import json

from misc.error_codes import *

from flask            import jsonify
from flask            import Flask
from flask            import request
from flask_cors       import CORS

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
from core.controller  import ComentPostController
from core.controller  import LikePostController
from core.controller  import UnlikePostController

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
coment_post_controller     = ComentPostController()
like_post_controller       = LikePostController()
unlike_post_controller     = UnlikePostController()

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
        
        if (response == OK):
            return json.dumps({ 
                "message": "success", "status_code": 200 
            }), 200
        elif (response == UserExists): 
            return json.dumps({ 
                "message": "user already exist", "status_code": UserExists 
            }), 400
        elif (response == InvalidUsername):
            return json.dumps({ 
                "message": "invalid username", "status_code": InvalidUsername 
            }), 400


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
        request.headers["token"],
        request.headers["username"]
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

            if (response):
                return json.dumps({
                    "message": "success", "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/user/get", methods = ["GET"])
def get_user():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            username = request.headers["requested-user"]

            response = find_user_controller.handle(
                username,
            )

            if (response):
                return json.dumps({
                    "message": "success" ,"data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed" ,"data": "unexistent", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401


# ================================ FOLLOW ROUTES ================================

@APP.route("/follow_user", methods = ["POST"])
def follow_user():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
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
            
            if (response):
                return json.dumps({
               "message": "success", "status_code": 200 
            }), 200
            
            else:
                return json.dumps({
                    "message": "failed", "status_code": 400 
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/follow_user/list/followers", methods = ["GET"])
def list_followers():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            followed_username = request.headers["username"]

            response = list_followers_controller.handle(
                followed_username
            )

            if (isinstance(response, list)):
                return json.dumps({
                    "message": "success", "data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401
    
@APP.route("/follow_user/list/followeds", methods = ["GET"])
def list_followeds():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            follower_username = request.headers["username"]

            response = list_followeds_controller.handle(
                follower_username
            )

            if (isinstance(response, list)):
                return json.dumps({
                    "message": "success", "data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": 400
                }), 400

    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/follow_user/remove/follower", methods = ["DELETE"])
def remove_follower():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "DELETE"):
            
            request_parsed = request.get_json()
            
            followed_username = request.headers["username"]
            follower_username = request_parsed["follower"]

            response = remove_follower_controller.handle(
                followed_username,
                follower_username
            )

            if (response):
                return json.dumps({
                    "message": "success", "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401
    
@APP.route("/follow_user/remove/followed", methods = ["DELETE"])
def remove_followed():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "DELETE"):
            
            request_parsed = request.get_json()
            
            follower_username = request.headers["username"]
            followed_username = request_parsed["followed"]
            
            response = remove_followed_controller.handle(
                follower_username,
                followed_username
            )

            if (response):
                return json.dumps({
                    "message": "success", "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "status_code": 400
                }), 400

    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401


# ================================ POST ROUTES ================================

@APP.route("/post/new", methods = ["POST"])
def create_post():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
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

            if (response):
                return json.dumps({
                "message": "success",
                "status_code": 200
            }), 200
            else:
                return json.dumps({
                    "message": "failed", 
                    "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/post/list", methods = ["GET"])
def list_posts():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            username = request.headers["username"]

            response = list_post_controller.handle(
                username
            )

            if (isinstance(response, list)):
                return json.dumps({
                    "message": "success", "data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/post/like", methods = ["POST"])
def like_post():
    
    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "POST"):
            username = request.headers["username"]
            post_id  = request.headers["postId"]

            response = like_post_controller.handle(
                username,
                post_id
            )

            if (response):
                return json.dumps({
                    "message": "success", "data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/post/unlike", methods = ["POST"])
def unlike_post():
    
    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "POST"):
            username = request.headers["username"]
            post_id  = request.headers["postId"]

            response = unlike_post_controller.handle(
                username,
                post_id
            )

            if (response):
                return json.dumps({
                    "message": "success", "data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401

@APP.route("/post/coment", methods = ["POST"])
def coment_post():
    
    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            username  = request.headers["username"]
            post_id   = request.headers["postId"]
            comentary = request.headers["comentary"]

            response = coment_post_controller.handle(
                username,
                post_id,
                comentary
            )

            if (response):
                return json.dumps({
                    "message": "success", "data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401


# ================================ FEED ROUTES ================================

@APP.route("/feed/retrieve", methods = ["GET"])
def retrieve_feed():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            username = request.headers["username"]
            limit    = request.headers["post-limit"]

            response = RetrieveFeedController.handle(
                username,
                limit
            )
            
            if (response):
                return json.dumps({
                    "message": "success", "data": response, "status_code": 200
                }), 200
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": 400
                }), 400
    else:
        return json.dumps({"message": "unauthorized", "status_code": "401"}), 401


if (__name__ == "__main__"):
    print("> Starting server at http://localhost:5006")
    APP.run(debug=False, port=5006)