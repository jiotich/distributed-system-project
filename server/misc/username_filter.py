class UsernameFilter:
    def __init__(self):
        self.forbiden_characters = [
            " ", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "=", "+",
            ",", ".", ";", ":", "/", "|", "-", "[", "]", "{", "}", "ç",
            "`", "'", '"', "^", "~", "<", ">" 
        ]
    
    def filter(self, username: str):
        lenght = self._verify_lenght(username, 4, 13)
        
        if (lenght == False):
            return False
        filter = self._character_filter(username)

        if (filter == False):
            return False

        return True
    
    def _verify_lenght(self, username: str, min, max):
        if (len(username) > max or len(username) < min):
            return False
    
    def _character_filter(self, username: str):
        print(username)
        for character in self.forbiden_characters:
            for name_character in username:
                if (character == name_character):
                    return False
        return True  