import urllib

from Global import Bot,MY_CHAT_WITH_BOT

def PingByFive(ChatId,ListToPing):
    Answer = str()
    Counter = 0
    for User in ListToPing:
        Answer += User + ' '
        Counter += 1
        if (Counter == 5):
            Bot.send_message(ChatId, Answer)
            Answer = ''
            Counter = 0
    Bot.send_message(ChatId, Answer)

def GivePots(ChatId):
        answer = "/g_withdraw"+" p04 " + str(1) + " p05 " + str(1) + " p06 " + str(1)
        answer_url = urllib.parse.quote(answer, )
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Писы" + '</a>'
        Bot.send_message(ChatId, answer_html, parse_mode='HTML')
        answer = "/g_withdraw"+" p01 " + str(1) + " p02 " + str(1) + " p03 " + str(1)
        answer_url = urllib.parse.quote(answer,)
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Раги" + '</a>'
        Bot.send_message(ChatId, answer_html, parse_mode='HTML')

def LowerCheck(List,Ask):
  for Node in List:
    if(Node.lower() == Ask.lower()):
      return Node
  return False

def TryAndSendExceptMe(myfunc):
    try:
        myfunc()
    except Exception as inst:
        Bot.send_message(MY_CHAT_WITH_BOT, inst)

def EmptyStringCheck(x):
    if x is None:
        return ""
    return x
