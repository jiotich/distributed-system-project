def search_click(search):
    print("Search: ",search)

def home_click(username):
    #FAZ REQUISIÇÃO DOS POSTS PARA O FEED
    #ABAIXO UM PLACEHOLDER
    posts = []
    posts.append(["Username1", "Description1", 0])
    posts.append(["Username2", "Description3", 0])
    posts.append(["Username3", "Description3", 0])
    return posts

def profile_click():
    print("Profile")

def publish_click():
    print("Publish")
    
def self_profile_click(username):
    #FAZ REQUISIÇÃO DOS POSTS DO USUÁRIO
    #ABAIXO UM PLACEHOLDER
    description = "Profile Description"
    posts = []
    posts.append(["Description1", 0])
    posts.append(["Description2", 0])
    posts.append(["Description3", 0])
    return [description, posts]

def change_user_description(username, description):
    #FAZ A REQUISIÇÃO DE MUDANÇA DE DESCRIÇÃO DO PERFIL
    print("Mudança de descrição: ", description)
    