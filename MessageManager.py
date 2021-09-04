import telebot
import urllib

class MessageManager(telebot.AsyncTeleBot) :
    def PingByFive(self,ChatId, ListToPing):
        Answer = str()
        Counter = 0
        for User in ListToPing:
            Answer += '@' +User + ' '
            Counter += 1
            if (Counter == 5):
                self.send_message(ChatId, Answer)
                Answer = ''
                Counter = 0
        self.send_message(ChatId, Answer)
    def GivePots(self,ChatId):
        answer = "/g_withdraw" + " p04 " + str(1) + " p05 " + str(1) + " p06 " + str(1)
        answer_url = urllib.parse.quote(answer, )
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Писы" + '</a>'
        self.send_message(ChatId, answer_html, parse_mode='HTML')
        answer = "/g_withdraw" + " p01 " + str(1) + " p02 " + str(1) + " p03 " + str(1)
        answer_url = urllib.parse.quote(answer, )
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Раги" + '</a>'
        self.Bot.send_message(ChatId, answer_html, parse_mode='HTML')