def login_clicked(window, username, password):
    return window.client.auth_user(username, password)
    

def signin_clicked(window, username, password):
    return window.client.create_user(username, password)