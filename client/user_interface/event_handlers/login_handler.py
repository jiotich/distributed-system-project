def login_clicked(window, username, password):
    print("Login: ",username," ",password)
    window.client.login(username, password)
    #FAZ REQUISIÇÃO DE LOGIN
    #ABAIXO UM PLACEHOLDER
    #if (username == "admin" and password == "admin"):
        #return True
    #else:
        #return False

def signin_clicked(window, username, password):
    window.client.register_user(username, password)
    print("SignIn: ",username," ",password)
    #FAZ REQUISIÇÃO DE REGISTRAR CONTA