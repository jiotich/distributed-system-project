import sys
sys.dont_write_bytecode = True
import json
import time

from flask            import Flask
from flask            import request

from misc.status_code import StatusCode
from misc.load_config import Configs
from log.logger       import Logger

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



status_code                = StatusCode()
configs                    = Configs()
logger                     = Logger()

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
update_user_controller     = UpdateUserController()
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
    begin = time.time()
    
    if (request.method == "POST"):
        
        content_size   = request.headers["Content-Length"]        
        request_parsed = request.get_json() 
        
        username    = request_parsed["username"]
        password    = request_parsed["password"]
        description = request_parsed["description"]

        response = create_user_controller.handle(
            username, 
            password, 
            description
        )
        
        if (response == status_code.OK):
            
            logger.new_rest_log(
                user_ip_address = request.remote_addr, 
                username        = username, 
                bytes_sent      = sys.getsizeof(response), 
                bytes_received  = content_size,
                time_spent      = time.time() - begin,
                http_method     = "POST", 
                url             = "/user/register", 
                http_status     = status_code.OK
            )

            return json.dumps({ 
                "message": "success", "status_code": status_code.OK 
            }), status_code.OK 
            
        elif (response == status_code.UserExists): 
            
            logger.new_rest_log(
                user_ip_address = request.remote_addr, 
                username        = username, 
                bytes_sent      = sys.getsizeof(response), 
                bytes_received  = content_size,
                time_spent      = time.time() - begin,
                http_method     = "POST", 
                url             = "/user/register", 
                http_status     = status_code.UserExists
            )
            
            return json.dumps({ 
                "message": "user already exist", "status_code": status_code.UserExists 
            }), status_code.Error
            
        elif (response == status_code.InvalidUsername):
            
            logger.new_rest_log(
                user_ip_address = request.remote_addr, 
                username        = username, 
                bytes_sent      = sys.getsizeof(response), 
                bytes_received  = content_size,
                time_spent      = time.time() - begin,
                http_method     = "POST", 
                url             = "/user/register", 
                http_status     = status_code.InvalidUsername
            )
            
            return json.dumps({ 
                "message": "invalid username", "status_code": status_code.InvalidUsername 
            }), status_code.Error

@APP.route("/user/login", methods = ["GET"])
def login():
    begin = time.time()
    
    if (request.method == "GET"):
        
        content_size = request.headers["Content-Length"]  
        username     = request.headers["username"]
        password     = request.headers["password"]

        response = auth_user_controller.handle(
            username,
            password
        )

        if (response):
            
            logger.new_rest_log(
                user_ip_address = request.remote_addr, 
                username        = username, 
                bytes_sent      = sys.getsizeof(response), 
                bytes_received  = content_size,
                time_spent      = time.time() - begin,
                http_method     = "GET", 
                url             = "/user/login", 
                http_status     = status_code.OK
            )
            
            return json.dumps({
                "message": "authenticated", 
                "token": response,
                "status_code": status_code.OK
            }), status_code.OK
        else:
            
            logger.new_rest_log(
                user_ip_address = request.remote_addr, 
                username        = username, 
                bytes_sent      = sys.getsizeof(response), 
                bytes_received  = content_size,
                time_spent      = time.time() - begin,
                http_method     = "GET", 
                url             = "/user/login", 
                http_status     = status_code.Unauthorized
            )
            
            return json.dumps({
                "message": "authentication failed", 
                "token": "-1",
                "status_code": status_code.Unauthorized
            }), status_code.Unauthorized

# TODO: não deixar a coluna para ser passada como parametro
@APP.route("/user/update", methods = ["PUT"])
def update_user():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "PUT"):
            
            content_size = request.headers["Content-Length"]  
            username     = request.headers["username"]
            data         = request.headers["data"]
        

            response = update_user_controller.handle(
                username,
                data
            )

            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = username, 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "PUT", 
                    url             = "/user/update", 
                    http_status     = status_code.OK
                )
                
                return json.dumps({
                    "message": "success", "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = username, 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "PUT", 
                    url             = "/user/update", 
                    http_status     = status_code.Error
                )
                
                return json.dumps({
                    "message": "failed", "status_code": status_code.Error
                }), status_code.Error
    else:
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized

@APP.route("/user/get", methods = ["GET"])
def get_user():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            
            content_size = request.headers["Content-Length"]  
            username     = request.headers["requested-user"]

            response = find_user_controller.handle(
                username,
            )

            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = username, 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/user/get", 
                    http_status     = status_code.OK
                )                
                
                return json.dumps({
                    "message": "success" ,"data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = username, 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/user/get", 
                    http_status     = status_code.Error
                )  
                
                return json.dumps({
                    "message": "failed" ,"data": "unexistent", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = username, 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "GET", 
            url             = "/user/get", 
            http_status     = status_code.Unauthorized
        )  
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized


# ================================ FOLLOW ROUTES ================================

@APP.route("/follow_user", methods = ["POST"])
def follow_user():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "POST"):
            
            content_size   = request.headers["Content-Length"]  
            request_parsed = request.get_json()
            
            followed_username = request_parsed["followed_user"]
            follower_username = request_parsed["follower_user"]

            response = follow_user_controller.handle(
                followed_username,
                follower_username
            )
            
            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/follow/user", 
                    http_status     = status_code.OK
                )  
                
                
                return json.dumps({
               "message": "success", "status_code": status_code.OK 
            }), status_code.OK
            
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/follow/user", 
                    http_status     = status_code.Error
                )  
                
                return json.dumps({
                    "message": "failed", "status_code": status_code.Error 
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "POST", 
            url             = "/follow/user", 
            http_status     = status_code.Unauthorized
        )  
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized

@APP.route("/follow_user/list/followers", methods = ["GET"])
def list_followers():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            
            content_size      = request.headers["Content-Length"]  
            followed_username = request.headers["username"]

            response = list_followers_controller.handle(
                followed_username
            )

            if (isinstance(response, list)):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/follow_user/list/followers", 
                    http_status     = status_code.OK
                ) 
                
                return json.dumps({
                    "message": "success", "data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/follow_user/list/followers", 
                    http_status     = status_code.Error
                ) 
                
                return json.dumps({
                    "message": "failed", "data": "", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "GET", 
            url             = "/follow_user/list/followers", 
            http_status     = status_code.Unauthorized
        ) 
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized
    
@APP.route("/follow_user/list/followeds", methods = ["GET"])
def list_followeds():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            
            content_size      = request.headers["Content-Length"]  
            follower_username = request.headers["username"]

            response = list_followeds_controller.handle(
                follower_username
            )

            if (isinstance(response, list)):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/follow_user/list/followeds", 
                    http_status     = status_code.OK
                ) 
                
                return json.dumps({
                    "message": "success", "data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/follow_user/list/followeds", 
                    http_status     = status_code.Error
                ) 
                
                return json.dumps({
                    "message": "failed", "data": "", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "GET", 
            url             = "/follow_user/list/followeds", 
            http_status     = status_code.Unauthorized
        ) 
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized

@APP.route("/follow_user/remove/follower", methods = ["DELETE"])
def remove_follower():
    begin = time.time()


    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "DELETE"):
            
            content_size   = request.headers["Content-Length"]  
            request_parsed = request.get_json()
            
            followed_username = request.headers["username"]
            follower_username = request_parsed["follower"]

            response = remove_follower_controller.handle(
                followed_username,
                follower_username
            )

            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "DELETE", 
                    url             = "/follow_user/remove/follower", 
                    http_status     = status_code.OK
                ) 
                
                return json.dumps({
                    "message": "success", "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "DELETE", 
                    url             = "/follow_user/remove/follower", 
                    http_status     = status_code.Error
                ) 
                
                return json.dumps({
                    "message": "failed", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "DELETE", 
            url             = "/follow_user/remove/follower", 
            http_status     = status_code.Unauthorized
        ) 
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized
    
@APP.route("/follow_user/remove/followed", methods = ["DELETE"])
def remove_followed():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "DELETE"):
            
            content_size   = request.headers["Content-Length"]  
            request_parsed = request.get_json()
            
            follower_username = request.headers["username"]
            followed_username = request_parsed["followed"]
            
            response = remove_followed_controller.handle(
                follower_username,
                followed_username
            )

            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "DELETE", 
                    url             = "/follow_user/remove/followed", 
                    http_status     = status_code.OK
                ) 
                
                return json.dumps({
                    "message": "success", "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "DELETE", 
                    url             = "/follow_user/remove/followed", 
                    http_status     = status_code.Error
                ) 
                
                return json.dumps({
                    "message": "failed", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "DELETE", 
            url             = "/follow_user/remove/followed", 
            http_status     = status_code.Unauthorized
        ) 
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized


# ================================ POST ROUTES ================================

@APP.route("/post/new", methods = ["POST"])
def create_post():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "POST"):
            
            content_size   = request.headers["Content-Length"]  
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
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/post/new", 
                    http_status     = status_code.OK
                ) 
                
                return json.dumps({
                    "message": "success", "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/post/new", 
                    http_status     = status_code.Error
                ) 
                
                return json.dumps({
                    "message": "failed", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "POST", 
            url             = "/post/new", 
            http_status     = status_code.Unauthorized
        ) 
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized

@APP.route("/post/list", methods = ["GET"])
def list_posts():
    begin = time.time()

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            
            content_size    = request.headers["Content-Length"]  
            username        = request.headers["username"]
            target_username = request.headers["target-username"]

            response = list_post_controller.handle(
                username,
                target_username
            )

            if (isinstance(response, list)):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/post/list", 
                    http_status     = status_code.OK
                ) 
                
                return json.dumps({
                    "message": "success", "data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/post/list", 
                    http_status     = status_code.Error
                ) 
                
                return json.dumps({
                    "message": "failed", "data": "", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "GET", 
            url             = "/post/list", 
            http_status     = status_code.Unauthorized
        ) 
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized

@APP.route("/post/like", methods = ["POST"])
def like_post():
    begin = time.time()
    
    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "POST"):
            
            content_size   = request.headers["Content-Length"]  
            request_parsed = request.get_json() 
            
            username = request.headers["username"]
            post_id  = request_parsed["post_id"]

            response = like_post_controller.handle(
                username,
                post_id
            )

            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/post/like", 
                    http_status     = status_code.OK
                )
                
                return json.dumps({
                    "message": "success", "data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                if (response):
                    logger.new_rest_log(
                        user_ip_address = request.remote_addr, 
                        username        = request.headers["username"], 
                        bytes_sent      = sys.getsizeof(response), 
                        bytes_received  = content_size,
                        time_spent      = time.time() - begin,
                        http_method     = "POST", 
                        url             = "/post/like", 
                        http_status     = status_code.Error
                    )
                
                return json.dumps({
                    "message": "failed", "data": "", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "POST", 
            url             = "/post/like", 
            http_status     = status_code.Unauthorized
        )
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized

#TODO: alterar a rota para usar o metodo delete
@APP.route("/post/unlike", methods = ["POST"])
def unlike_post():
    begin = time.time()
    
    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "POST"):
            
            content_size   = request.headers["Content-Length"]  
            request_parsed = request.get_json() 
            
            username = request.headers["username"]
            post_id  = request_parsed["post_id"]

            response = unlike_post_controller.handle(
                username,
                post_id
            )

            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/post/unlike", 
                    http_status     = status_code.OK
                )
                
                return json.dumps({
                    "message": "success", "data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/post/unlike", 
                    http_status     = status_code.Error
                )
                
                return json.dumps({
                    "message": "failed", "data": "", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "POST", 
            url             = "/post/unlike", 
            http_status     = status_code.Unauthorized
        )
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized

@APP.route("/post/coment", methods = ["POST"])
def coment_post():
    begin = time.time()
    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "POST"):
            
            content_size   = request.headers["Content-Length"]  
            request_parsed = request.get_json()
            
            username  = request_parsed["username"]
            post_id   = request_parsed["post_id"]
            comentary = request_parsed["comentary"]

            response = coment_post_controller.handle(
                username,
                post_id,
                comentary
            )

            if (response):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/post/coment", 
                    http_status     = status_code.OK
                )
                
                return json.dumps({
                    "message": "success", "data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "POST", 
                    url             = "/post/coment", 
                    http_status     = status_code.Error
                )
                
                return json.dumps({
                    "message": "failed", "data": "", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "POST", 
            url             = "/post/coment", 
            http_status     = status_code.Unauthorized
        )
        
        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized


# ================================ FEED ROUTES ================================

@APP.route("/feed/retrieve", methods = ["GET"])
def retrieve_feed():

    auth = ensure_authenticated.handle(
        request.headers["token"],
        request.headers["username"]
    )

    if (auth):
        if (request.method == "GET"):
            begin = time.time()
            
            content_size = request.headers["Content-Length"]  
            username     = request.headers["username"]
            limit        = request.headers["post-limit"]

            response = retrieve_feed_controller.handle(
                username,
                int(limit)
            )
            
            if (isinstance(response, list)):
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/feed/retrieve", 
                    http_status     = status_code.OK
                )

                return json.dumps({
                    "message": "success", "data": response, "status_code": status_code.OK
                }), status_code.OK
            else:
                logger.new_rest_log(
                    user_ip_address = request.remote_addr, 
                    username        = request.headers["username"], 
                    bytes_sent      = sys.getsizeof(response), 
                    bytes_received  = content_size,
                    time_spent      = time.time() - begin,
                    http_method     = "GET", 
                    url             = "/feed/retrieve", 
                    http_status     = status_code.OK
                )

                return json.dumps({
                    "message": "failed", "data": "", "status_code": status_code.Error
                }), status_code.Error
    else:
        logger.new_rest_log(
            user_ip_address = request.remote_addr, 
            username        = request.headers["username"], 
            bytes_sent      = sys.getsizeof(response), 
            bytes_received  = content_size,
            time_spent      = time.time() - begin,
            http_method     = "GET", 
            url             = "/feed/retrieve", 
            http_status     = status_code.Unauthorized
        )

        return json.dumps({
            "message": "unauthorized", "status_code": status_code.Unauthorized
        }), status_code.Unauthorized


if (__name__ == "__main__"):
    
    port  = configs.config["server"]["rest_port"]
    debug = configs.config["server"]["debug"] 
    ip    = configs.config["server"]["ip_address"]
    
    print(f"> Starting server at http://{ip}:{port}")
    
    APP.run(debug=debug, port=port)
    