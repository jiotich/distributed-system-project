import sys
sys.dont_write_bytecode = True
from packet_ops import *
from Pyro5.api import Proxy
import json
import base64

class Client:
    def __init__(self) -> None:
        pass
    
    def create_user(self, username, passord, description=""):
        with Proxy("PYRONAME:user_remote_object") as proxy:
            response = proxy.create_user(
                username,
                passord,
                description
            )
        if response == 700:
            return False
        return response
    
    def auth_user(self, username, password):
        with Proxy("PYRONAME:user_remote_object") as proxy:
            response = proxy.auth_user(
                username,
                password
            )
        if not response:
            return response
        else:
            self.token = response
            return True
    
    def find_user(self, username, target_username):
        with Proxy("PYRONAME:user_remote_object") as proxy:
            response = proxy.find_user(
                username,
                target_username,
                self.token
            )
        return response
    
    def update_user_description(self, username, new_description):
        with Proxy("PYRONAME:user_remote_object") as proxy:
            response = proxy.update_user_description(
                username,
                new_description,
                self.token
            )
        return response
    
    def follow_user(self, followed_username, follower_username):
        with Proxy("PYRONAME:user_remote_object") as proxy:
            response = proxy.follow_user(
                followed_username,
                follower_username,
                self.token
            )
        return response
    
    def check_if_follows(self, follower_username, followed_username):
        with Proxy("PYRONAME:user_remote_object") as proxy:
            response = proxy.list_user_followeds(
                follower_username,
                self.token
            )
            followed_id = proxy.find_user(
                follower_username,
                followed_username,
                self.token
            )[0]
        if not response:
            return False
        else:
            for user in response:
                if (followed_id in user):
                    return True
            return False
    
    def remove_user_followed(self, followed_username, follower_username):
        with Proxy("PYRONAME:user_remote_object") as proxy:
            response = proxy.remove_user_followed(
                followed_username,
                follower_username,
                self.token
            )
        return response
    
    def create_post(self, username, description, image_path):
        image = get_bytearray_from_file(image_path)
        with Proxy("PYRONAME:post_remote_object") as proxy:
            response = proxy.create_post(
                username,
                description,
                image,
                self.token
            )
        return response
    
    def list_posts(self, username, target_username):
        with Proxy("PYRONAME:post_remote_object") as proxy:
            response = proxy.list_posts(
                username,
                target_username,
                self.token
            )
        if not response:
            return response
        else:
            posts = []
            for post in response:
                fixed_json = self.fix_quotes(post[5])
                img_path = get_file_from_bytearray(base64.b64decode(json.loads(fixed_json)['data']), random=True)
                is_liked = True if post[8] == 1 else False
                posts.append([post[6], post[1], post[2], post[0], is_liked, f"temp/{img_path}"])
            return posts
    
    def retrieve_feed(self, username, post_limit=30):
        with Proxy("PYRONAME:post_remote_object") as proxy:
            response = proxy.retrieve_feed(
                username,
                post_limit,
                self.token
            )
        if not response:
            return response
        else:
            posts = []
            for post in response:
                fixed_json = self.fix_quotes(post[5])
                img_path = get_file_from_bytearray(base64.b64decode(json.loads(fixed_json)['data']), random=True)
                is_liked = True if post[8] == 1 else False
                posts.append([post[6], post[1], post[2], post[0], is_liked, f"temp/{img_path}" ])
            return posts
    
    def like_post(self, username, post_id):
        with Proxy("PYRONAME:post_remote_object") as proxy:
            response = proxy.like_post(
                username,
                post_id,
                self.token
            )
        return response
    
    def unlike_post(self, username, post_id):
        with Proxy("PYRONAME:post_remote_object") as proxy:
            response = proxy.unlike_post(
                username,
                post_id,
                self.token
            )
        return response

    def fix_quotes(self,message):
		# obviamente tem um jeito melhor de fazer isso
		# mas estou sem tempo
        return message.replace("\'","\"")

if __name__ == "__main__":
    #image = get_bytearray_from_file("/home/vinicius/Pictures/neon.jpg")
    #print(image)
    client = Client()
    #print(client.auth_user("joseph", "joseph"))
    #print(client.auth_user("joseph", "joseph"))
    #print(client.create_post("joseph", "Description2", "/home/vinicius/Pictures/neon.jpg"))
    #print(client.list_posts("joseph", "joseph"))