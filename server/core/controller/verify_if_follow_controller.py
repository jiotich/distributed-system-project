import json
from core.services import VerifyIfFollow

class UpdateUserController:
    def handle(self, follower_username, followed_username):
        verify_if_follow = VerifyIfFollow()
        response = verify_if_follow.execute(followed_username, followed_username)
        
        if (response):
            return json.dumps({"status_code": "200"})

        else:
            return json.dumps({"status_code": "400"})
        