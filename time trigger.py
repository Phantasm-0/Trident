import datetime,time,pytz

timzone = pytz.timezone('Europe/Moscow')
diff = datetime.timedelta(0,0,0,0,15,0,0,0)
evening = datetime.time(16,45,00,00,tzinfo =  timzone)
morning = datetime.time(8,45,00,00,tzinfo = timzone)
night = datetime.time(00,45,00,00,tzinfo =  timzone )
const_times =[morning,evening,night]

def Righttime(unixtime):
    now_t = time.time()
    now = datetime.datetime.now(timzone)
    unix_datetime = datetime.date.fromtimestamp(unixtime)
