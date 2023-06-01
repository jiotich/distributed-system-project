def login_clicked(username, password):
    print("Login: ",username," ",password)
    if (username == "admin" and password == "admin"):
        return True
    else:
        return False

def signin_clicked(username, password):
    print("SignIn: ",username," ",password)