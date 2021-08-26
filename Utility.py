import urllib

from Global import RoyalTrident_bot

def PingByFive(ChatId,ListToPing):
    Answer = str()
    Counter = 0
    for User in ListToPing:
        Answer += User + ' '
        Counter += 1
        if (Counter == 5):
            RoyalTrident_bot.send_message(ChatId,Answer)
            Answer = ''
            Counter = 0
    RoyalTrident_bot.send_message(ChatId ,Answer )


def GivePots(self):
        answer = "/g_withdraw"+" p04 " + str(1) + " p05 " + str(1) + " p06 " + str(1)
        answer_url = urllib.parse.quote(answer, )
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Писы" + '</a>'
        RoyalTrident_bot.send_message(self.message.chat.id,answer_html,parse_mode='HTML')
        answer = "/g_withdraw"+" p01 " + str(1) + " p02 " + str(1) + " p03 " + str(1)
        answer_url = urllib.parse.quote(answer,)
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Раги" + '</a>'
        RoyalTrident_bot.send_message(self.message.chat.id,answer_html,parse_mode='HTML')