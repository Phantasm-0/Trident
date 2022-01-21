import telebot
import urllib
import logging


class MessageManager(telebot.AsyncTeleBot) :
    def __int__(self):
        super(MessageManager, self).__int__()
        logger = telebot.logger
        telebot.logger.setLevel(logging.DEBUG)
        self.MY_CHAT_WITH_BOT = 450927903
    def PingByFive(self,ChatId, ListToPing):
        Answer = str()
        Counter = 0
        responce = list()
        for User in ListToPing:
            Answer += '@' + User + ' '
            Counter += 1
            if (Counter == 5):
                send_message = self.send_message(ChatId, Answer)
                responce.append(send_message.wait())
                Answer = ''
                Counter = 0
        send_message = self.send_message(ChatId, Answer)
        responce.append(send_message.wait())
        return responce

    def GivePots(self,ChatId):
        answer = "/g_withdraw" + " p04 " + str(1) + " p05 " + str(1) + " p06 " + str(1)
        answer_url = urllib.parse.quote(answer, )
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Писы" + '</a>'
        self.send_message(ChatId, answer_html, parse_mode='HTML')
        answer = "/g_withdraw" + " p01 " + str(1) + " p02 " + str(1) + " p03 " + str(1)
        answer_url = urllib.parse.quote(answer, )
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Раги" + '</a>'
        self.send_message(ChatId, answer_html, parse_mode='HTML')

    def SendResourcesWithShareLink(self,ChatId,AsnwerForSendList):
        AnswerForSend = str()
        for ReqestString in AsnwerForSendList:
            AnswerForHTML = ReqestString[0]
            AnswerForDisplay = ReqestString[1]
            AnswerForHTML = urllib.parse.quote(AnswerForHTML, )
            AnswerForSend += f'<a href="https://t.me/share/url?url={AnswerForHTML}">{AnswerForDisplay} </a> \n'
        self.send_message(ChatId, AnswerForSend, parse_mode='HTML')


    #def edit_message_text(self, *args, **kwargs):
        #try:
           # super().edit_message_text(args,kwargs)
       # except ApiException as Error:
           # self.send_message(self.MY_CHAT_WITH_BOT,str(Error))
          #  print("SHIT")