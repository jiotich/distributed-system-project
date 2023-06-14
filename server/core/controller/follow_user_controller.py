from core.services import FollowUserService

class FollowUserController:
    def handle(self, followed_username, follower_username):
        follow_user_service = FollowUserService()
        response = follow_user_service.execute(followed_username, follower_username)
        
        return response
        