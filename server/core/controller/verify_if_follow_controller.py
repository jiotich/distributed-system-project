import json
from core.services import VerifyIfFollow

class VerifyIfFollowController:
    def handle(self, follower_username, followed_username):
        verify_if_follow = VerifyIfFollow()
        response = verify_if_follow.execute(follower_username, followed_username)
        
        if (response):
            return json.dumps({"status_code": "200"})

        else:
            return json.dumps({"status_code": "400"})
        