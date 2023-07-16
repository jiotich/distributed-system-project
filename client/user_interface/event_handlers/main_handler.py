def search_click(window, search):
    user = window.client.find_user(window.username, search)
    return user

def home_click(window):
    posts = window.client.retrieve_feed(window.username)
    return posts

def publish_click(window, image_path, description):
    return window.client.create_post(window.username, description, image_path)
    
def self_profile_click(window, username):
    posts = window.client.list_posts(username, username)
    description = window.client.find_user(window.username, username)[2]
    return [description, posts]

def change_user_description(window, username, description):
    window.client.update_user_description(username, description)

def profile_click(window, username):
    posts = window.client.list_posts(window.username, username)
    description = window.client.find_user(window.username, username)[2]
    is_followed = window.client.check_if_follows(window.username, username)
    return [description, is_followed, posts]

def follow_user(window, username):
    window.client.follow_user(username, window.username)

def unfollow_user(window, username):
    window.client.remove_user_followed(username, window.username)

def liked_post(window, user, post_id):
    window.client.like_post(user, post_id)

def unliked_post(window, user, post_id):
    window.client.unlike_post(user, post_id)
    