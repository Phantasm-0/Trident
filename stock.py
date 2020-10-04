import urllib.parse,telebot,re,
from telebot import types


RoyalTrident_bot = telebot.AsyncTeleBot('1222435814:AAFPEFv8ad_2xBIuYUMc5aIDxqKGhAKRijo')
conn = psycopg2.connect(database='postgres', user='postgres', password='123Anapa2017', host='localhost',port = 5432)
db = conn.cursor()
resource_pack = {'Thread': '01',
'Stick': '02',
'Pelt': '03',
'Bone': '04',
'Coal': '05',
'Charcoal':'06',
'Powder': '07',
'Iron ore': '08',
'Cloth': '09',
'Silver ore':'10',
'Bauxite':'11',
'Cord':'12',
'Magic stone': '13',
'Wooden shaft': '14',
'Sapphire':'15',
'Solvent': '16',
'Ruby': '17',
'Hardener':'18',
'Steel':'19',
'Leather':'20',
'Bone powder':'21',
'String':'22',
'Coke':'23',
'Purified powder':'24',
'Silver alloy':'25',
'Steel mold':'27',
'Silver mold':'28',
'Blacksmith frame':'29',
'Artisan frame': '30',
'Rope': '31',
'Silver frame': '32',
'Metal plate': '33',
'Metallic fiber': '34',
'Crafted leather': '35',
'Quality Cloth': '36',
'Blacksmith mold': '37',
'Artisan mold': '38',
'Stinky Sumac': '39',
'Mercy Sassafras': '40',
'Cliff Rue': '41',
'Love Creeper': '42',
'Wolf Root': '43',
'Swamp Lavender': '44',
'White Blossom':'45',
'Ilaves': '46',
'Ephijora': '47',
'Storm Hyssop': '48',
'Cave Garlic':'49',
'Yellow Seed':'50',
'Tecceagrass':'51',
'Spring Bay Leaf':'52',
'Ash Rosemary': '53',
'Sanguine Parsley': '54',
'Sun Tarragon': '55',
'Maccunut': '56',
'Dragon Seed': '57',
"Queen's Pepper": '58',
'Plasma of abyss': '59',
'Ultramarine dust': '60',
'Ethereal bone': '61',
'Itacory': '62',
'Assassin Vine': '63',
'Kloliarway': '64',
'Astrulic': '65',
'Flammia Nut': '66',
'Plexisop': '67',
'Mammoth Dill': '68',
'Silver dust': '69',
'Hay': '618',
'Corn': '619',
'Hamsters': '620',
'Cheese':'621',
"🎟Gift Coupon 'Goose'":'pet613',
"🎟Gift Coupon 'Pig'": 'pet614',
"🎟Gift Coupon 'Horse'":'pet615',
"🎟Gift Coupon 'Owl'":'pet616',
"🎟Gift Coupon 'Mouse'":'pet617',
"🎟Gift Coupon 'Gopher'":'pet622',
"🎟Gift Coupon 'Ants'":'pet623',
"🎟Gift Coupon 'Spider'":'pet624',
"🎟Gift Coupon 'Haunted'":'pet625',
"🎟Gift Coupon 'Camel'":'pet626',
"📕Scroll of Rage":'s01',
"📕Scroll of Peace":'s02',
"📗Scroll of Rage":'s03',
"📗Scroll of Peace":'s04',
"📘Scroll of Rage":'s05',
"📘Scroll of Peace":'s06',
"📙Scroll of Rage":'s07',
"📙Scroll of Peace":'s08',
"📒Scroll of Rage":'s09',
"📒Scroll of Peace":'s10',
"📕Rare scroll of Rage":'s11',
"📕Rare scroll of Peace":'s12',
"📗Rare scroll of Rage":'s13',
"📗Rare scroll of Peace":'s14',
"📘Rare scroll of Rage":'s15',
"📘Rare scroll of Peace":'s16',
"📙Rare scroll of Rage":'s17',
"📙Rare scroll of Peace":'s18',
"📒Rare scroll of Rage":'s19',
"📒Rare scroll of Peace":'s20',
"🖋Scroll of Engraving":'s50',
"✒️Scroll of Engraving":'s51',
"🖋Rare scroll of Engraving":'s52',
"✒️Rare scroll of Engraving":'s53',
"Chain mail":'a03',
"Silver cuirass":'a04',
"Mithril armor":'a05',
"Steel helmet":'a08',
"Silver helmet":'a09',
"Mithril helmet":'a10',
"Silver boots":'a14',
"Mithril boots":'a15',
"Silver gauntlets":'a19',
"Mithril gauntlets":'a20',
"Bronze shield":'a23',
"Silver shield":'a24',
"Mithril shield":'a25',
"Royal Guard Cape":'a26',
"Order Armor":'a27',
"Order Helmet":'a28',
"Order Boots":'a29',
"Order Gauntlets":'a30',
"Order Shield":'a31',
"Hunter Armor":'a32',
"Hunter Helmet":'a33',
"Hunter Boots":'a34',
"Hunter Gloves":'a35',
"Clarity Robe":'a36',
"Clarity Circlet":'a37',
"Clarity Shoes":'a38',
"Clarity Bracers":'a39',
"Crusader Armor":'a45',
"Crusader Helmet":'a46',
"Crusader Boots":'a47',
"Crusader Gauntlets":'a48',
"Crusader Shield":'a49',
"Royal Armor":'a50',
"Royal Helmet":'a51',
"Royal Boots":'a52',
"Royal Gauntlets":'a53',
"Royal Shield":'a54',
"Ghost Armor":'a55',
"Ghost Helmet":'a56',
"Ghost Boots":'a57',
"Ghost Gloves":'a58',
"Lion Armor":'a59',
"Lion Helmet":'a60',
"Lion Boots":'a61',
"Lion Gloves":'a62',
"Demon Robe":'a63',
"Demon Circlet":'a64',
"Demon Shoes":'a65',
"Demon Bracers":'a66',
"Divine Robe":'a67',
"Divine Circlet":'a68',
"Divine Shoes":'a69',
"Divine Bracers":'a70',
"Storm Cloak":'a71',
"Durable Cloak":'a72',
"Blessed Cloak":'a73',
"Council Armor":'a78',
"Council Helmet":'a79',
"Council Boots":'a80',
"Council Gauntlets":'a81',
"Council Shield":'a82',
"Griffin Armor":'a83',
"Griffin Helmet":'a84',
"Griffin Boots":'a85',
"Griffin Gloves":'a86',
"Celestial Armor":'a87',
"Celestial Helmet":'a88',
"Celestial Boots":'a89',
"Celestial Bracers":'a90',
"Assault Cape":'a100',
"Craftsman Apron":'a101',
"Stoneskin Cloak":'a102',
"Manticore Armor":'a103',
"Overseer Armor":'a104',
"Discarnate Robe":'a105',
"Manticore Helmet":'a106',
"Overseer Helmet":'a107',
"Discarnate Circlet":'a108',
"Manticore Gloves":'a109',
"Overseer Gauntlets":'a110',
"Discarnate Bracers":'a111',
"Overseer Shield":'a113',
"Manticore Boots":'a114',
"Overseer Boots":'a115',
"Discarnate Shoes":'a116',
"Champion blade":'k01',
"Trident blade":'k02',
"Hunter shaft":'k03',
"War hammer head":'k04',
"Hunter blade":'k05',
"Order Armor piece":'k06',
"Order Helmet fragment":'k07',
"Order Boots part":'k08',
"Order Gauntlets part":'k09',
"Order shield part":'k10',
"Hunter Armor part":'k11',
"Hunter Helmet fragment":'k12',
"Hunter Boots part":'k13',
"Hunter Gloves part":'k14',
"Clarity Robe piece":'k15',
"Clarity Circlet fragment":'k16',
"Clarity Shoes part":'k17',
"Clarity Bracers part":'k18',
"Thundersoul blade":'k19',
"Doomblade blade":'k20',
"Eclipse blade":'k21',
"Guard's blade":'k22',
"King's Defender blade":'k23',
"Raging Lance blade":'k24',
"Composite Bow shaft":'k25',
"Lightning Bow shaft":'k26',
"Hailstorm Bow shaft":'k27',
"Imperial Axe head":'k28',
"Skull Crusher head":'k29',
"Dragon Mace head":'k30',
"Ghost blade":'k31',
"Lion blade":'k32',
"Crusader Armor piece":'k33',
"Crusader Helmet fragment":'k34',
"Crusader Boots part":'k35',
"Crusader Gauntlets part":'k36',
"Crusader shield part":'k37',
"Royal Armor piece":'k38',
"Royal Helmet fragment":'k39',
"Royal Boots part":'k40',
"Royal Gauntlets part":'k41',
"Royal shield part":'k42',
"Ghost Armor part":'k43',
"Ghost Helmet fragment":'k44',
"Ghost Boots part":'k45',
"Ghost Gloves part":'k46',
"Lion Armor part":'k47',
"Lion Helmet fragment":'k48',
"Lion Boots part":'k49',
"Lion Gloves part":'k50',
"Demon Robe piece":'k51',
"Demon Circlet fragment":'k52',
"Demon Shoes part":'k53',
"Demon Bracers part":'k54',
"Divine Robe piece":'k55',
"Divine Circlet fragment":'k56',
"Divine Shoes part":'k57',
"Divine Bracers part":'k58',
"Storm Cloak part":'k59',
"Durable Cloak part":'k60',
"Blessed Cloak part":'k61',
"Council Armor part":'k78',
"Council Helmet part":'k79',
"Council Boots part":'k80',
"Council Gauntlets part":'k81',
"Council Shield part":'k82',
"Griffin Armor part":'k83',
"Griffin Helmet part":'k84',
"Griffin Boots part":'k85',
"Griffin Gloves part":'k86',
"Celestial Armor part":'k87',
"Celestial Helmet part":'k88',
"Celestial Boots part":'k89',
"Celestial Bracers part":'k90',
"Griffin Knife part":'k91',
"Minotaur Sword part":'k92',
"Phoenix Sword part":'k93',
"Heavy Fauchard part":'k94',
"Guisarme part":'k95',
"Meteor Bow part":'k96',
"Nightfall Bow part":'k97',
"Black Morningstar part":'k98',
"Maiming Bulawa part":'k99',
"Assault Cape part":'k100',
"Craftsman Apron part":'k101',
"Stoneskin Cloak part":'k102',
"Poniard part":'k103',
"Lightbane Katana part":'k104',
"Doom Warglaive part": 'k105',
"Decimation Harpoon part":'k106',
"Sinister Ranseur part":'k107',
"Heartstriker Bow part":'k108',
"Windstalker Bow part":'k109',
"Malificent Maul part":'k110',
"Brutalizer Flail part":'k111',
"Manticore Armor part":'k112',
"Manticore Helmet part":'k113',
"Manticore Boots part":'k114',
"Manticore Gloves part":'k115',
"Overseer Shield part":'k116',
"Overseer Armor part":'k117',
"Overseer Helmet part":'k118',
"Overseer Boots part":'k119',
"Overseer Gauntlets part":'k120',
"Discarnate Robe part":'k121',
"Discarnate Circlet part":'k122',
"Discarnate Shoes part":'k123',
"Discarnate Bracers part":'k124',
"Mystery ring":'rng',
"Champion Sword recipe":'r01',
"Trident recipe":'r02',
"Hunter Bow recipe":'r03',
"War hammer recipe":'r04',
"Hunter Dagger recipe":'r05',
"Order Armor recipe":'r06',
"Order Helmet recipe":'r07',
"Order Boots recipe":'r08',
"Order Gauntlets recipe":'r09',
"Order shield recipe":'r10',
"Hunter Armor recipe":'r11',
"Hunter Helmet recipe":'r12',
"Hunter Boots recipe":'r13',
"Hunter Gloves recipe":'r14',
"Clarity Robe recipe":'r15',
"Clarity Circlet recipe":'r16',
"Clarity Shoes recipe":'r17',
"Clarity Bracers recipe":'r18',
"Thundersoul Sword recipe":'r19',
"Doomblade Sword recipe":'r20',
"Eclipse recipe":'r21',
"Guard's Spear recipe":'r22',
"King's Defender recipe":'r23',
"Raging Lance recipe":'r24',
"Composite Bow recipe":'r25',
"Lightning Bow recipe":'r26',
"Hailstorm Bow recipe":'r27',
"Imperial Axe recipe":'r28',
"Skull Crusher recipe":'r29',
"Dragon Mace recipe":'r30',
"Ghost dagger recipe":'r31',
"Lion Knife recipe":'r32',
"Crusader Armor recipe":'r33',
"Crusader Helmet recipe":'r34',
"Crusader Boots recipe":'r35',
"Crusader Gauntlets recipe":'r36',
"Crusader shield recipe":'r37',
"Royal Armor recipe":'r38',
"Royal Helmet recipe":'r39',
"Royal Boots recipe":'r40',
"Royal Gauntlets recipe":'r41',
"Royal shield recipe":'r42',
"Ghost Armor recipe":'r43',
"Ghost Helmet recipe":'r44',
"Ghost Boots recipe":'r45',
"Ghost Gloves recipe":'r46',
"Lion Armor recipe":'r47',
"Lion Helmet recipe":'r48',
"Lion Boots recipe":'r49',
"Lion Gloves recipe":'r50',
"Demon Robe recipe":'r51',
"Demon Circlet recipe":'r52',
"Demon Shoes recipe":'r53',
"Demon Bracers recipe":'r54',
"Divine Robe recipe":'r55',
"Divine Circlet recipe":'r56',
"Divine Shoes recipe":'r57',
"Divine Bracers recipe":'r58',
"Storm Cloak recipe":'r59',
"Durable Cloak recipe":'r60',
"Blessed Cloak recipe":'r61',
"Council Armor recipe":'r78',
"Council Helmet recipe":'r79',
"Council Boots recipe":'r80',
"Council Gauntlets recipe":'r81',
"Council Shield recipe":'r82',
"Griffin Armor recipe":'r83',
"Griffin Helmet recipe":'r84',
"Griffin Boots recipe":'r85',
"Griffin Gloves recipe":'r86',
"Celestial Armor recipe":'r87',
"Celestial Helmet recipe":'r88',
"Celestial Boots recipe":'r89',
"Celestial Bracers recipe":'r90',
"Griffin Knife recipe":'r91',
"Minotaur Sword recipe":'r92',
"Phoenix Sword recipe":'r93',
"Heavy Fauchard recipe":'r94',
"Guisarme recipe":'r95',
"Meteor Bow recipe":'r96',
"Nightfall Bow recipe":'r97',
"Black Morningstar recipe":'r98',
"Maiming Bulawa recipe":'r99',
"Assault Cape recipe":'r100',
"Craftsman Apron recipe":'r101',
"Stoneskin Cloak recipe":'r102',
"Poniard recipe":'r103',
"Lightbane Katana recipe":'r104',
"Doom Warglaive recipe":'r105',
"Decimation Harpoon recipe":'r106',
"Sinister Ranseur recipe":'r107',
"Heartstriker Bow recipe":'r108',
"Windstalker Bow recipe":'r109',
"Malificent Maul recipe":'r110',
"Brutalizer Flail recipe":'r111',
"Manticore Armor recipe":'r112',
"Manticore Helmet recipe":'r113',
"Manticore Boots recipe":'r114',
"Manticore Gloves recipe":'r115',
"Overseer Armor recipe":'r116',
"Overseer Helmet recipe":'r117',
"Overseer Boots recipe":'r118',
"Overseer Gauntlets recipe":'r119',
"Overseer Shield recipe":'r120',
"Discarnate Robe recipe":'r121',
"Discarnate Circlet recipe":'r122',
"Discarnate Shoes recipe":'r123',
"Discarnate Bracers recipe":'r124'}
res_list = resource_pack.keys()



def stock(message):
  text = message.text
  give_all = str()
  g_withdraw = "/g_withdraw "
  g_deposit = "/g_deposit "
  answer = ""
  result_list = []
  html_start_string = '<a href="https://t.me/share/url?url='

  if((re.search("Встреча",text) is not None) or(re.search("Deposited",text) is not None) or (re.search("Ты заметил враждебных существ",text) is not None) or (re.search("Получено:",text) is not None)):
    return

  if(re.search("На верстаке ты видишь:",text) is not None): #с верстака
    result_list = re.findall(".{1,40}",text)
    for i in result_list: 
       for g  in res_list:
        full_search = g + "\sx\s\d{1,4}$"
        if(re.search(full_search,i)):
          result = re.search(full_search,i)
          result_answer = result.group(0)
          res_name = g
          res_id = resource_pack.get(res_name)
          amount = re.search("\d{1,3}",result_answer)
          amount_answer = amount.group(0)
          answer_url = g_deposit  + str(res_id) + " " + amount_answer
          answer_url = urllib.parse.quote(answer_url)
          answer_name = g + "(" +  amount_answer +")"
          answer += html_start_string + answer_url + '">'+ answer_name + '</a>'+ '\n'


  elif((re.search("Не хватает материалов для крафта",text) is not None)): #реинфорс и крафт
      result_list = re.findall(".{1,40}",text)
      give_all = give_all_("\d{1,4}\sx\s",result_list)

  elif(re.search("Not enough materials",textis not None):
  	  result_list = re.findall(".{1,40}",text)
	  list_for_deposit = list()
      for element in result_list:
        list_for_deposit.append(element)
        if(str(element)== "In your stock:"):
			break
      answer = give_all_("\d{1,4}\sx\s",list_for_deposit,"g_deposit ")
      give_all = give_all_("\d{1,4}\sx\s",result_list,"g_withdraw ")





  else:
       result_list = re.findall(".{1,40}",text)
       for i in result_list: 
           for g in res_list:
             full_search = g +"\s\(\d{1,4}\)"     
             if(re.search(full_search,i)):
              result = re.search(full_search,i)
              result_answer = result.group(0)
              res_name = g
              res_id = resource_pack.get(res_name)
              amount = re.search("\d{1,4}",result_answer)
              amount_answer = amount.group(0)
              answer_url = g_deposit  + str(res_id) + " " + amount_answer
              answer_url = urllib.parse.quote(answer_url)
              answer_name = g + "(" +  amount_answer +")"
              answer += html_start_string + answer_url + '">'+ answer_name + '</a>'+ '\n'

  RoyalTrident_bot.send_message(message.chat.id,str(answer+'/n/n'+give_all),parse_mode = 'HTML')


def give_any(message):
  text = message.text
  g_withdraw ="/g_withdraw"
  answer = g_withdraw
  additional_any = []
  amount = "1"
  if(re.search("\d{1,100}",text)):
     result = re.search("\d{1,100}",text)
     amount = result.group(0)
  if(re.search("\s[Фф][Дд]($|\s)",text)):
            answer += " p04 " + amount +  " p05 " +  amount + " p06 " +  amount
  if(re.search("\s[Фф][Рр]($|\s)",text)):
            answer += " p01 " + amount +  " p02 " +  amount + " p03 " +  amount
  if(re.search("\s[Мм][Оо][Рр][Фф]([Ыы]|$|\s)",text)) :
            answer += " p19 " + amount +  " p20 " +  amount + " p21 " +  amount
  if(re.search("\s[Мм][Аа][Нн][ЫыУу]($|\s)",text)):
            answer += " p13 " + amount +  " p14 " +  amount + " p15 " +  amount
  if(re.search("\s[Нн][Аа][Тт][Уу][Рр]([Ыы]|$|\s)",text)):
            answer += " p10 " + amount +  " p11 " +  amount + " p12 " +  amount

  if(answer == g_withdraw):
    if(re.search("\s\w{1,100}",text)):
      result = re.findall("\s\w{1,100}",text)
      while(len(result)>18):
         while (len(additional_any) != 18): 
               additional_any.insert(0, result.pop(0))
         give_additional_any(additional_any,message)
         additional_any.clear()
      for element in result:
            if(element != ("дай" or "Дай" )):
              answer += element 
  if(answer == g_withdraw):
    return          
  answer_url = urllib.parse.quote(answer,)
  answer_html = '<a href="https://t.me/share/url?url=' + answer_url +  '">'+ answer + '</a>'
  RoyalTrident_bot.send_message(message.chat.id,answer_html,parse_mode = 'HTML')

def give_additional_any(result,message):
    g_withdraw ="/g_withdraw"
    answer = g_withdraw
    for i in result:
            if(i != ("дай" or "Дай" )):
              answer += i 
    answer_url = urllib.parse.quote(answer,)
    answer_html = '<a href="https://t.me/share/url?url=' + answer_url +  '">'+ answer + '</a>'
    RoyalTrident_bot.send_message(message.chat.id,answer_html,parse_mode = 'HTML')



def give_additional_all(regex,list_for_search,g_what):
    answer_name = "Дать все"
    g_withdraw =  urllib.parse.quote("/g_withdraw ")
    answer_for_send = str()
    html_start_string = '<a href="https://t.me/share/url?url='
    for i in list_for_search: 
        for g in res_list:
             full_search = regex + g + "$"
             if(re.search(full_search,i)):
                  result = re.search(full_search,i)
                  result_answer = result.group(0)
                  res_name = g
                  res_id = resource_pack.get(res_name)
                  amount = re.search("\d{1,4}",result_answer)
                  amount_answer = amount.group(0)
                  answer_url = str(res_id) + " " + amount_answer + " "
                  answer_url = urllib.parse.quote(answer_url)
                  answer_for_send += answer_url
    return(html_start_string + g_withdraw + answer_for_send + '">'+ answer_name + '</a>'+ '\n')

def give_all_(regex,list_for_search,g_what):
    g_withdraw =  urllib.parse.quote(g_what)
    answer = str()
    answer_for_send = str()
    html_start_string = '<a href="https://t.me/share/url?url='
    additional_any = list()
    while(len(list_for_search)>18):
        while (len(additional_any) != 18): 
               additional_any.insert(0, list_for_search.pop(0))
        answer+=give_additional_all(regex,additional_any,g_what)
        additional_any.clear()
    for i in list_for_search: 
          for g in res_list:
             full_search = regex + g + "$"
             if(re.search(full_search,i)):
                  result = re.search(full_search,i)
                  result_answer = result.group(0)
                  res_name = g
                  res_id = resource_pack.get(res_name)
                  amount = re.search("\d{1,4}",result_answer)
                  amount_answer = amount.group(0)
                  answer_url = str(res_id) + " " + amount_answer + " "
                  answer_url = urllib.parse.quote(answer_url)
                  answer_for_send += answer_url
    return (answer+html_start_string + g_withdraw + answer_for_send + '">'+ "Дать все" + '</a>'+ '\n')