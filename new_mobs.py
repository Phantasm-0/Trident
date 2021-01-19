from global_consts import RoyalTrident_bot
import re
from mob import Mob

mob_list = []


#def inline_update(inline_query):


#def chosen_inline_result(chosen_inline_result):


def update_helpers(call):
  for mob in mob_list:
      if (mob.link == call.data):
            if(mob.mob_update_helpers(call.from_user) is False):
                RoyalTrident_bot.answer_callback_query(call.id,"Ты не пройдешь!",show_alert = True)
                return
  RoyalTrident_bot.answer_callback_query(call.id)

def find_mobs_message(message):
  ambush = False
  timer = 180
  if(re.search("It's an ambush!",message.text)):
    ambush = True
    timer = 360
  link = re.search("\/fight.{1,100}",message.text)
  link = link.group(0)
  mob = Mob(message.from_user, link, ambush,None,message,timer)
  markup = mob.mobs_markups("⚔️ В бой","🤝 Помогаю")
  message_for_update = RoyalTrident_bot.send_message(message.chat.id,mob.mobs_text,reply_markup = markup,parse_mode='HTML')
  message_for_update = message_for_update.wait()
  mob.message_for_update = message_for_update
  mob_list.append(mob)
  mob.updating()
  mob_list.remove(mob)




