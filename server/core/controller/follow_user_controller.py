import json
from core.services import FollowUserService

class FollowUserController:
    def handle(self, followed_username, follower_username):
        follow_user_service = FollowUserService()
        response = follow_user_service.execute(followed_username, follower_username)
        
        if (response):
            return json.dumps({"status_code": "200"})
            
        else:
            return json.dumps({"status_code": "400"})
            