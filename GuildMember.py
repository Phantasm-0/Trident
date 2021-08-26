

class GuildMember:
    def __init__(self,Username,ChatWarsNickName,ChatWarsLvl,ChatWarsClass):
        self.Username = Username
        self.ChatWarsNickName = ChatWarsNickName
        self.ChatWarsLvl = ChatWarsLvl
        self.ChatWarsClass = ChatWarsClass
        self.TwinksList = list()
        self.MyMains = list()
        self.isMain = True

    def ChangeLevel(self,Level):
        self.ChatWarsLvl = int(Level)
    def AddTwink(self,User):
        self.TwinksList.append(User)
        User.MyMains.append(self)
        User.isMain = False