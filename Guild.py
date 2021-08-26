from GuildMember import GuildMember
class Guild:
    def __init__(self):
        self.Igor = GuildMember('kappainho','Coca-Cola',0,0)
        self.Scuns = GuildMember('Scuns87','Scuns87',0,0)
        self.Bekmuart = GuildMember('bekmurat','Bekish',0,0)
        self.Tea = GuildMember('PlotArmor','PlotArmor KT',0,0)
        self.Vasde =  GuildMember('Vasde','Ну этот как его',0,0)
        self.larina457 = GuildMember('larina457','Старик Семецкий',0,0)
        self.Ksandrax = GuildMember('Ksandrax','Флегматик',0,0)
        self.EPetuhov = GuildMember('EPetuhov','EPetuhov',0,0)
        self.undfndnm = GuildMember('ProydemteMolodoy','undfndnm',0,0)
        self.Soare = GuildMember('Soarelia','Soare',0,0)
        self.Andrey = GuildMember('Ln156','BolshoyMolodecKT',0,0)
        self.AlexanderKobets = GuildMember('Renbrane','Тёпленькая вода',0,0)
        self.Dark = GuildMember('HatredPerson','Shinen',0,0)
        self.phenjan = GuildMember('phenjan','phenjan',0,0)
        self.Tahena = GuildMember('tahena','Итианаа',0,0)
        self.m1sha007 = GuildMember('m1sha007','ОплотМнеВРот',0,0)
        self.Cerethrius = GuildMember('gaelicwar','Cerethrius',0,0)
        self.Phantasm = GuildMember('ElderSign','Phantasm',0,0)
        self.Farfelkygelain = GuildMember('Farfelkygelain','Farfelkygelain',0,0)
        self.Maeve = GuildMember('notaloneindec','Maeve',0,0)
        self.ProoFFie = GuildMember('ProoFFie','Shiawase',0,0)
        self.Kronprincen = GuildMember('lelehrer','Kronprincen',0,0)
        self.catLeopold = GuildMember('GoTo87','cat Leopold',0,0)
        self.VishenkaNyam = GuildMember('VishenkaNyam','Сахарок',0,0)
        self.GuildList = self.Init()
    def Init(self):
        self.Soare.AddTwink(self.Kronprincen)
        self.Soare.AddTwink(self.catLeopold)
        self.Soare.AddTwink(self.Cerethrius)
        self.Soare.AddTwink(self.Ksandrax)
        self.Soare.AddTwink(self.Vasde)
        self.Soare.AddTwink(self.m1sha007)
        self.Soare.AddTwink(self.EPetuhov)
        self.Soare.AddTwink(self.VishenkaNyam)

        self.AlexanderKobets.AddTwink(self.Vasde)
        self.AlexanderKobets.AddTwink(self.EPetuhov)
        self.AlexanderKobets.AddTwink(self.Ksandrax)
        self.AlexanderKobets.AddTwink(self.Cerethrius)
        self.AlexanderKobets.AddTwink(self.Kronprincen)

        self.Tea.AddTwink(self.undfndnm)
        self.Tea.AddTwink(self.Cerethrius)
        self.Tea.AddTwink(self.m1sha007)
        self.Tea.AddTwink(self.VishenkaNyam)
        self.Tea.AddTwink(self.Kronprincen)

        self.Scuns.AddTwink(self.catLeopold)

        return [self.Bekmuart, self.Scuns, self.Igor, self.Tea, self.Vasde, self.larina457,
                self.Ksandrax, self.EPetuhov, self.undfndnm, self.Soare, self.Andrey,
                    self.AlexanderKobets, self.Dark, self.phenjan, self.Tahena, self.m1sha007, self.Cerethrius, self.Phantasm,
                    self.Farfelkygelain, self.Maeve, self.ProoFFie, self.Kronprincen, self.catLeopold, self.VishenkaNyam]
