def search_click(user, search):
    #FAZ REQUISIÇÃO DO(S) USUÁRIO(S) QUE TEM MATCH COM A STRING SEARCH
    #RETORNA UMA LISTA DE USUÁRIOS
    #ABAIXO UM PLACEHOLDER
    users = []
    users.append(["Username1", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."])
    users.append(["Username2", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."])
    users.append(["Username3", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."])
    return users

def home_click(user):
    #FAZ REQUISIÇÃO DOS POSTS PARA O FEED
    #ABAIXO UM PLACEHOLDER
    posts = []
    posts.append(["Username1", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0])
    posts.append(["Username2", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0])
    posts.append(["Username3", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0])
    return posts

def publish_click(user, image_path, description):
    #USUÁRIO FAZ PUBLICAÇÃO
    print("Description: ", description, "Path: ", image_path)
    pass
    
def self_profile_click(username):
    #FAZ REQUISIÇÃO DOS POSTS DO USUÁRIO
    #ABAIXO UM PLACEHOLDER
    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    posts = []
    posts.append(["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0])
    posts.append(["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0])
    posts.append(["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0])
    return [description, posts]

def change_user_description(username, description):
    #FAZ A REQUISIÇÃO DE MUDANÇA DE DESCRIÇÃO DO PERFIL
    print("Mudança de descrição: ", description)

def profile_click(user, username):
    #FAZ REQUISIÇÃO DOS POSTS DO USUÁRIO
    #ABAIXO UM PLACEHOLDER
    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    is_followed = False
    posts = []
    posts.append(["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0, 1])
    posts.append(["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0, 1])
    posts.append(["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 0, 1])
    return [description, is_followed, posts]

def follow_user(user, username):
    #O USER (QUE ESTÁ USANDO O CLIENTE) VAI DAR FOLLOW NO USERNAME
    #FAZER REQUISIÇÃO AO SERVIDOR
    print(user, "deu follow no ",username)
    pass

def unfollow_user(user, username):
    #O USER (QUE ESTÁ USANDO O CLIENTE) VAI DAR UNFOLLOW NO USERNAME
    #FAZER REQUISIÇÃO AO SERVIDOR
    print(user, "deu unfollow no ",username)
    pass
    