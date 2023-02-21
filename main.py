try:
  import vk_api, os, re, json, random
  from vk_api.longpoll import VkLongPoll, VkEventType
  from paperscrollsdk import PaperScroll
  from config import *
except:
  quit("Проверьте, что вы установили все библиотеки!")
cp=0
cp1=0
owner = owner_1
owner2=0
owner3=0
adm1=0
adm2=0
adm3=0
adm4=0
adm5=0
adm6=0
adm7=0
adm8=0
admbd=0
admall=0
adma10=0
adma11=0
adma9=0
adma8=0
adma7=0
adma6=0
adma5=0
adma4=0
adma3=0
adma2=0
adma1=0

#АВТОРИЗАЦИЯ
paperClient = PaperScroll(int(idmPS), tokenPS)
paperApi = paperClient.getApi()
"""ПЕРЕИМЕНОВАТЬ БОТА
paperApi.editMerchant({
                "name": "название",
                "group_id": номер группы,
                "avatar": "ссылка на аватарку"
            })
"""
vk_session = vk_api.VkApi(token=tokenVK)
bal=0
st="False"
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def get_bal():
  global bal
  otvet = paperApi.getMerchants()
  otvet = str(otvet)
  otvet = otvet.replace(get_bal1,"")
  otvet = otvet.replace(get_bal2,"")
  otvet = otvet.replace("}]","")
  bal=int(otvet)//1000
  print(bal)
get_bal()
def sender_user(id,text,peer):
  vk_session.method("messages.send", {"peer_id":f"{peer}", "message":text,"random_id":0})
def reporto(id, otv,ido):
  try:
    otv1=f"✉ Администратор @id{id} ответил на ваше обращение: {otv}"
    vk_session.method("messages.send", {"user_id":ido, "message": otv1,"random_id":0})
    vk_session.method("messages.send", {"user_id":ido, "sticker_id":"70536","random_id":0})
    vk_session.method("messages.send", {"chat_id":1, "message": f"@id{id}, игрок получил ваш ответ, спасибо что помогаете игрокам.\n💬 Ваш ответ: {otv}","random_id":0})
  except:
    pass
def construct(id,name,money,bonus,lvl,warns,clik,kapca,kl,pr,idd,ban,vv,reg):
    p = {}
    p["name"] = name
    p["money"] = money
    p["bonus"] = bonus
    p["lvl"] = lvl
    p["warns"] = warns
    p["clik"] = clik
    p["kapca"] = kapca
    p["kl"] = kl
    p["pr"] = pr
    p["idd"] = idd
    p["ban"] = ban
    p["vv"] = vv
    p["reg"] = reg
    p["banr"] = ban
    p["br"] = vv
    p["rep"] = reg

    data[str(id)] = p
    

    return "normal"
def gen_c(id):
  global cp
  global cp1
  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  a=random.choice(list)
  list2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  s=random.choice(list)
  s1=random.choice(list)
  s2=random.choice(list)
  b=random.choice(list2)
  b1=random.choice(list2)
  b2=random.choice(list2)
  cp=f"{b}{s}{b1}{b2}{s1}{s2}"
  cp1=f"{b}.{s}{b1}.{b2}{s1}.{s2}"
  #kapca
  (data[str(id)]["kapca"])=cp
def loadam():#гкод, знаю.
  global admbd
  global admall
  global owner
  global owner2
  global owner3
  global adm1
  global adm2
  global adm3
  global adm4
  global adm5
  global adm6
  global adm7
  global adm8
  global adma10
  global adma11
  global adma9
  global adma8
  global adma7
  global adma6
  global adma5
  global adma4
  global adma3
  global adma2
  global adma1
  x = open('owner.txt','r+')
  owner=x.read()
  owner=int(owner)
  x.close()
  x = open('owner2.txt','r+')
  owner2=x.read()
  owner2=int(owner2)
  x.close()
  x = open('owner2.txt','r+')
  owner2=x.read()
  owner2=int(owner2)
  x.close()
  x = open('owner3.txt','r+')
  owner3=x.read()
  owner3=int(owner3)
  x.close()
  x = open('adm1.txt','r+')
  adm1=x.read()
  adm1=int(adm1)
  x.close()
  x = open('adm2.txt','r+')
  adm2=x.read()
  adm2=int(adm2)
  x.close()
  x = open('adm3.txt','r+')
  adm3=x.read()
  adm3=int(adm3)
  x.close()
  x = open('adm4.txt','r+')
  adm4=x.read()
  adm4=int(adm4)
  x.close()
  x = open('adm5.txt','r+')
  adm5=x.read()
  adm5=int(adm5)
  x.close()
  x = open('adm6.txt','r+')
  adm6=x.read()
  adm6=int(adm6)
  x.close()
  x = open('adm7.txt','r+')
  adm7=x.read()
  adm7=int(adm7)
  x.close()
  x = open('adm8.txt','r+')
  adm8=x.read()
  adm8=int(adm8)
  x.close()
  admbd=f"""[Owner:{owner},
Owner2:{owner2},
Owner3:{owner3},
Adm1:{adm1},
Adm2:{adm2},
Adm3:{adm3},
Adm4:{adm4},
Adm5:{adm5},
Adm6:{adm6},
Adm7:{adm7},
Adm8:{adm8}]
  """
  adma1=""
  adma2=""
  adma3=""
  adma4=""
  adma5=""
  adma6=""
  adma7=""
  adma8=""
  
  try:
    adma1=(data[str(adm1)]["name"])
  except:
    a=0
  try:
    adma2=(data[str(adm2)]["name"])
  except:
    a=0
  try:
    adma3=(data[str(adm3)]["name"])
  except:
    a=0
  try:
    adma4=(data[str(adm4)]["name"])
  except:
    a=0
  try:
    adma5=(data[str(adm5)]["name"])
  except:
    a=0
  try:
    adma6=(data[str(adm6)]["name"])
  except:
    a=0
  try:
    adma7=(data[str(adm7)]["name"])
  except:
    a=0
  try:
    adma8=(data[str(adm8)]["name"])
  except:
    a=0
  try:
    adma9=(data[str(owner)]["name"])
  except:
    a=0
  try:
    adma10=(data[str(owner2)]["name"])
  except:
    a=0
  try:
    adma11=(data[str(owner3)]["name"])
  except:
    a=0
  admall=f"""[⭐⭐] -> Создатели: {adma9} {adma10} {adma11}
[⭐] -> Администраторы: {adma1} {adma2} {adma3} {adma4} {adma5} {adma6} {adma7} {adma8}
"""
#------------------------

def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }
#------------------------



#------------------------Клавиатура

keyboardcmd = {
    "one_time" : True,
    "buttons" : [
        [get_but('Баланс', 'negative'),get_but('Профиль','primary')]
    ]
}
keyboardcmd = json.dumps(keyboardcmd, ensure_ascii = False).encode('utf-8')
keyboardcmd = str(keyboardcmd.decode('utf-8'))

keyboardinfo = {
    "one_time" : False,
    "buttons" : [
        [get_but('💎 клик', 'primary'),get_but('📒 профиль','secondary')],
        [get_but('🎁 статистика', 'secondary'),get_but('📚 команды','primary')],
        [get_but('💸 вывод', 'positive')]
    ]
}
keyboardinfo = json.dumps(keyboardinfo, ensure_ascii = False).encode('utf-8')
keyboardinfo = str(keyboardinfo.decode('utf-8'))
  
def savebd():
    with open("data.txt", "w") as file:
        for  i in data:
            p = str(i) + " " +str(data[i]["name"]) +" " +str(data[i]["money"])+ " " +str(data[i]["bonus"])+ " " +str(data[i]["lvl"]) + " " +str(data[i]["warns"]) +" " +str(data[i]["clik"])+ " " +str(data[i]["kapca"])+ " " +str(data[i]["kl"])+ " " +str(data[i]["pr"])+ " " +str(data[i]["idd"])+ " " +str(data[i]["ban"])+ " " +str(data[i]["vv"])+ " " +str(data[i]["reg"])+ " " +str(data[i]["banr"])+ " " +str(data[i]["br"])+ " " +str(data[i]["rep"])
            
            file.write(p + '\n')
        
def loadbd():
    file = open("data.txt","r") 
    datas= file.read()
    datas = datas.splitlines()
    file.close()
    data = {}
    for i in datas:
        i = i.split()
        if len(i)>16:
            data[str(i[0])] = {}
            data[str(i[0])]["name"] = i[1]
            data[str(i[0])]["money"] = i[2]  
            data[str(i[0])]["bonus"] = i[3]   
            data[str(i[0])]["lvl"] = i[4]
            data[str(i[0])]["warns"] = i[5] 
            data[str(i[0])]["clik"] = i[6]  
            data[str(i[0])]["kapca"] = i[7]   
            data[str(i[0])]["kl"] = i[8]
            data[str(i[0])]["pr"] = i[9] 
            data[str(i[0])]["idd"] = i[10] 
            data[str(i[0])]["ban"] = i[11] 
            data[str(i[0])]["vv"] = i[12] 
            data[str(i[0])]["reg"] = i[13] 
            data[str(i[0])]["banr"] = i[14] 
            data[str(i[0])]["br"] = i[15] 
            data[str(i[0])]["rep"] = i[16] 
    return(data)





data =loadbd()
def pay_user(id,am):
  get_bal()
  global status
  status="False"
  am1=f"{am}000"
  if int(am1)<int(bal) and int(am1)!=0:
    try:
        
        status=paperApi.createTransfer({
                  "peer_id": int(id),
                  "object_type": "balance",
                  "object_type_id": 0,
                  "amount": int(am1)
                  })
        (data[str(id)]["money"])=0
        (data[str(id)]["vv"])=int((data[str(id)]["vv"]))+int(am)
        vk_session.method("messages.send", {"user_id":owner, "message":f"Вывод:\nИд:{id}\nСумма:{am}","random_id":0})
        text=f"""🧻 | Вам успешно было отправлено {am} PS.
🙏 | Пожалуйста, оставьте отзыв, чтобы люди поверили в нашу честность: https://vk.cc/cljVsK"""
    except:
        text=f"ПРОИЗОШЛА ОШИБКА! СРОЧНО ОБРАТИТЕСЬ К АДМИНИСТРАЦИИ (@id{owner})"
    vk_session.method("messages.send", {"peer_id":peer, "message":text,"random_id":0})
  elif int(am1)>=int(bal):
    text=f"""🧻 | Баланс бота мал. Дождитесь пополнения."""
    vk_session.method("messages.send", {"peer_id":peer, "message":text,"random_id":0})
  elif int(am1)==0:
    text=f"""🧻 | Ваш баланс равен 0!"""
    vk_session.method("messages.send", {"peer_id":peer, "message":text,"random_id":0})

  
w=1
for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if w==1:
            loadam()
            msg = event.text.lower()
            id = event.user_id
            peer=event.peer_id
            lenn=len(str(msg))
            lenn=int(lenn)
            n = 0
            for i in data:
              if str(id) == i :
              
                n = 1
            
            if n == 0:
                          name="user"
                          construct(id , name, 0, 0, 1, 0, 15, 0, 0, 0, id, 0, 0, 0)
                          x = open('users.txt','r+')
                          x1=x.read()
                          x2=int(x1)
                          x.seek(0)
                          a=int(x2)+1
                          x.write(f'{a}')
                          x.close()
                          #vk_session.method("messages.send", {"user_id": owner, "message":f"Регистрация!\nВсего людей зарегано: {a}\nЗарегался: {id}","random_id":0})
            bansee=(data[str(id)]["ban"])
            print(f"✉ @id{id} написал {msg}")
            bansee=int(bansee)
            reg=(data[str(id)]["reg"])
            if int(reg)==0:
              
              bal1=re.sub(r'(?<!^)(?=(\d{3})+$)', '.', str(bal))
              (data[str(id)]["reg"])=1
              get_bal()
              x = open('users.txt','r+')
              x1=x.read()
              id1=str(id)
              if id1[0]=="-":
                
                vk_session.method("messages.send", {"peer_id":peer, "message":f"🤩 Беседа успешно зарегистрирована.\n 📚 Что бы получить список команд напишите <<команды>>. \n 🔒 Пользовательское соглашение: {user_agreement}\n💳 Баланс бота на данный момент: {bal1}","dont_parse_links":1,"keyboard":keyboardinfo, "random_id":0})
              else:
                
                vk_session.method("messages.send", {"peer_id":peer, "message":f"🤩 Привет! Ты стал {x1} пользователем бота!\n 🔒 Пользовательское соглашение: {user_agreement}\n💳 Баланс бота на данный момент: {bal1}","dont_parse_links":1,"keyboard":keyboardinfo, "random_id":0})
            if event.from_chat:
              cid=event.chat_id
            else:
              cid=0
            if (msg.startswith("бан") or msg.startswith("разбан") or msg.startswith("id") or msg=="администрация" or msg.startswith("отв") or msg.startswith("бр")) and cid!=1:
              sender_user(id, "⚡ | Команда не доступна.",peer)
            elif bansee==1 and (msg=="[club218479839|@clickerpscroll] 💸 вывод" or msg=="[club218479839|@clickerpscroll] 🎁 статистика" or msg=="ник" or msg=="[club218479839|@clickerpscroll] 📚 команды" or msg=="[club218479839|@clickerpscroll] 📒 профиль" or msg=="[club218479839|@clickerpscroll] 💎 клик" or msg=="💎 клик" or msg=="клик" or msg=="📒 профиль" or msg=="🎁 статистика" or msg== "📚 команды" or msg=="профиль" or msg=="💸 вывод" or msg=="статистика"):
              banr=(data[str(id)]["banr"])
              
              if banr=="1":
                banreason="Попытка взлома"
              
              elif banr=="2":
                banreason="Оскорбление пользователя/администрации/сообщества/игры"
                              
              elif banr=="3":
                banreason="Неадекватное поведение"              
              elif banr=="4":
                banreason="Багоюз"              
              elif banr=="5":
                banreason="Использование авто-кликера"
              else:
                banreason="Решение администрации"
              text=f"[⛔] @id{id}, к сожалению, ваш аккаунт заблокирован навсегда.\n[❗] Причина блокировки: {banreason}.\n[🔔] Вы можете обратиться в репорт."
              sender_user(id, text, peer)
            elif cid!=1 and (msg=="ид" or msg=="adm 0 0"):
              text="нельзя"
              sender_user(id, text, peer)
            elif id==-218479839:
              a=0
            elif msg=="статистика" or msg=="[club218479839|@clickerpscroll] 🎁 статистика" or msg=="🎁 статистика":
              get_bal()
              bal1=re.sub(r'(?<!^)(?=(\d{3})+$)', '.', str(bal))
              usr=(data[str(id)]["name"])
              f = open('users.txt','r')
              f1 = open('clall.txt','r')
              f2 = open('klikbal.txt','r')
              
              fa=f.readline()
              fa1=f1.readline()
              fa2=f2.readline()

              fa2==re.sub(r'(?<!^)(?=(\d{3})+$)', '.', str(fa2))
              fa1==re.sub(r'(?<!^)(?=(\d{3})+$)', '.', str(fa1))
              f.close()
              f1.close()
              f2.close()
              text= f"""{usr}, статистика бота:

👥 | Игроков: {fa}
✈ | Всего кликов: {fa1}
👾 | Всего заработано: {fa2} PS

🧻 | Баланс бота: {bal1} PS"""
              sender_user(id, text, peer)
            elif msg=="команды" or msg=="📚 команды" or msg=="[club218479839|@clickerpscroll] 📚 команды":
              text= f"""❗ Список моих команд:
              
[💎] клик
[🎁] статистика
[💡] ник <<ник>>
[💸] вывод

[❗] Репорт
"""
              sender_user(id, text, peer)
            elif msg=="профиль" or msg=="📒 профиль" or msg=="[club218479839|@clickerpscroll] 📒 профиль":
              
              ownerka=""
              adminka=""
              
              loadam()
              if owner==id or owner2==id or owner3==id:
                ownerka="\n⚡ | Вы являетесь владельцем бота"
              if adm1==id or adm2==id or adm3==id or adm4==id or adm5==id or adm6==id or adm7==id or adm8==id:
                adminka="\n⭐ | Вы являетесь администратором бота"
              usr=(data[str(id)]["name"])
              i=(data[str(id)]["idd"])
              balans=(data[str(id)]["money"])
              clik=(data[str(id)]["clik"])
              kl=(data[str(id)]["kl"])
              lvl=(data[str(id)]["lvl"])
              vv=(data[str(id)]["vv"])
              lvl11=int(kl)//200+1
              if int(lvl11)>=int(lvl) and int(lvl)<4:
                if lvl11>=4:
                  lvl11=4
                (data[str(id)]["lvl"])=int(lvl11)
                (data[str(id)]["clik"])=15*int(data[str(id)]["lvl"])
              clik=(data[str(id)]["clik"])
              lvl=(data[str(id)]["lvl"])
              balans=re.sub(r'(?<!^)(?=(\d{3})+$)', '.', str(balans))
              text=f"""{usr}, Ваш профиль:

🆔 | Игровой ID: {i}
🧻 | Баланс: {balans} PS
✈ | Всего кликов: {kl}
🤑 | Всего выведено: {vv} PS
🤑 | За клик: {clik} PS
📈 | Коэффициент клика: {lvl}x{ownerka}{adminka}

💡 | Чтобы сменить ник, напишите <<Ник [текст]>>."""
              vk_session.method("messages.send", {"peer_id":peer, "message":text,"keyboard":keyboardinfo,"random_id":0})
            elif (msg=="клик" or msg=="[club218479839|@clickerpscroll] 💎 клик" or msg=="💎 клик") and event.from_chat:
              usr=(data[str(id)]["name"])
              vk_session.method("messages.send", {"peer_id":peer, "message":f"😒 {usr}, кликать можно только в личных сообщениях.","random_id":0})
            elif (msg=="клик" or msg=="[club218479839|@clickerpscroll] 💎 клик" or msg=="💎 клик"):
              if int(data[str(id)]["kl"])%50==0 and int(data[str(id)]["kl"])!=0:
                gen_c(id)
                print()
                sender_user(id,f"""🤖 | Бип-буп, буп-бип?
⚠⚠⚠
Защита от автокликера, введите: {cp1} без кавычек и точек!
⚠⚠⚠
🤖 | Бип-буп, буп-бип?""", peer)
              else:
                usr=(data[str(id)]["name"])
                i=(data[str(id)]["idd"])
                clik=(data[str(id)]["clik"])
                lvl=(data[str(id)]["lvl"])
                (data[str(id)]["kl"])=int(data[str(id)]["kl"])+1
                clik=int(clik)
                (data[str(id)]["money"])=int((data[str(id)]["money"]))+int(clik)
                balans=(data[str(id)]["money"])
                kl=(data[str(id)]["kl"])
                balans=re.sub(r'(?<!^)(?=(\d{3})+$)', '.', str(balans))
                text=f"""💸 | Получено за клик: {clik} PS
🧻 | Баланс: {balans} PS
🖱 | Кликнуто: {kl}"""
                x = open('klikbal.txt','r+')
                x1=x.read()
                x2=int(x1)
                x.seek(0)
                a=int(x2)+int(clik)
                x.write(f'{a}')
                x.close()
                x = open('clall.txt','r+')
                x1=x.read()
                x2=int(x1)
                x.seek(0)
                a=int(x2)+1
                x.write(f'{a}')
                x.close()
                vk_session.method("messages.send", {"peer_id":peer, "message":text,"random_id":0})
            elif (msg=="вывод" or msg=="[club218479839|@clickerpscroll] 💸 вывод") and event.from_chat:
              usr=(data[str(id)]["name"])
              vk_session.method("messages.send", {"peer_id":peer, "message":f"😒 {usr}, команда активна только в личных сообщениях.","random_id":0})
            elif msg==(data[str(id)]["kapca"]):
              sender_user(id, "✅ | Вы прошли капчу, можете продолжать кликать!",peer)
              (data[str(id)]["kl"])=int(data[str(id)]["kl"])+1
            elif msg=="вывод" or msg=="💸 вывод":
              am=int((data[str(id)]["money"]))
              pay_user(id,am)
              
            elif msg.startswith("Репорт") or msg.startswith("репорт") and msg!="репорт" and lenn>=11 and int(data[str(id)]["br"])!=1 and int(data[str(id)]["rep"])!=1:
                rep=msg.replace("Репорт","")
                rep=msg.replace("репорт","")
                text=f"[РЕПОРТ]\n\n[👤] ID: @id{id}\n[🔈] Текст: {rep}\n[✉] Для ответа напишите «отв {id} (Ваш текст)»\n[🗯]#id{id} #репорт"
                vk_session.method("messages.send", {"chat_id":1, "message":text,"random_id":0})
                text=f"✉ Ваш репорт принят!"
                (data[str(id)]["rep"])=1

                sender_user(id,text,peer)
            elif msg.startswith("Репорт") or msg.startswith("репорт") and msg!="репорт" and lenn>=11 and (int(data[str(id)]["br"])==1 or int(data[str(id)]["rep"]==1)):
              text="⚡ | Не удалось отправить репорт. Возможно вы не давно отправляли репорт."
              sender_user(id,text, peer)
            elif msg.startswith("Репорт") or msg.startswith("репорт") and msg!="репорт" and lenn<11:
                text=f"✉ Минимальная длина репорта - 4 символа !"

                sender_user(id,text,peer)
            elif msg=="репорт":
                text=f"✉ Используйте: <<репорт [сообщение]>>!"

                sender_user(id,text,peer)
            
            elif (msg.split(' ', 1)[0])=="ник" and lenn>3 and lenn<=13:
              nk=msg.split(' ')[1]
              data[str(id)]["name"] = msg.split(' ')[1]
              vk_session.method("messages.send", {"peer_id": peer, "message": nk + ", прикольный ник! 🙂", "random_id": 0})
              vk_session.method("messages.send", {"peer_id": peer, "sticker_id":"4282", "random_id": 0})
            elif (msg.split(' ', 1)[0])=="ник" and lenn<= 3:
              nikk=data[str(id)]["name"]
              vk_session.method("messages.send", {"peer_id": peer, "message": f"{nikk}, используте: <<Ник [ник]>>", "random_id": 0})
            elif (msg.split(' ', 1)[0])=="ник" and lenn> 13:
              nikk=data[str(id)]["name"]
              vk_session.method("messages.send", {"peer_id": peer, "message": f"{nikk}, вы указали слишком длинный ник. 🤔", "random_id": 0})
            elif msg=="администрация" and (adm1==id or adm2==id or adm3==id or adm4==id or adm5==id or adm6==id or adm7==id or adm8==id or owner==id or owner2==id or owner3==id):
            #admall
              loadam()
              vk_session.method("messages.send", {"peer_id": peer, "message": admall, "disable_mentions": 1, "random_id": 0})
            elif (msg.split(' ', 1)[0])=="кик" and (adm1==id or adm2==id or adm3==id or adm4==id or adm5==id or adm6==id or adm7==id or adm8==id or owner==id or owner2==id or owner3==id):
              nikk=data[str(id)]["name"]
              msg=msg.replace("кик ","")
              try:
                
                
                vk_session.method("messages.removeChatUser", {"chat_id": 1, "user_id": str(msg), "random_id": 0})
                text=f"⚡ | Пользователь @id{msg} исключен из беседы."
                sender_user(id, text, peer)
              except:
                text=f"⚡ | Проверьте верность id, введеное в формате числа"
                sender_user(id, text, peer)
            elif (msg.split(' ', 1)[0])=="кик":
              nikk=data[str(id)]["name"]
              text=f"⚡ | {nikk}, Вы не являетесь администратором бота."
              sender_user(id, text, peer)
            elif msg=="adm.load" and int(id)==int(owner):
              loadam()
              
              nikk=data[str(id)]["name"]
              vk_session.method("messages.send", {"peer_id": peer, "message": f"{nikk}, данные от сервера:\n{admbd}", "random_id": 0})
            elif msg.startswith("бан") :
                nikk=data[str(id)]["name"]
                loadam()
                if owner==id or owner2==id or owner3==id or adm1==id or adm2==id or adm3==id or adm4==id or adm5==id or adm6==id or adm7==id or adm8==id:
                  def ban(user, rea):
                    try:
                      user=int(user)
                    except:
                      user=0
                      sender_user(id,"⛔ | Произошла ошибка! Нужно вводить цифровой ID. \n✅ | Используйте: <<ID @пользователь>>",peer)
                    try:
                      if user==owner:
                        sender_user("⛔ | Произошла ошибка при блокировки владельца бота!")
                      elif data[str(user)]["ban"]=="1":
                        sender_user("⛔ | Произошла ошибка! У пользователя уже блокировка.")
                        
                      else:
                        
                        user=int(user)
                        data[str(user)]["ban"]="1"
                        data[str(user)]["banr"]=rea
                        sender_user(id,f"✅ | @id{user} успешно заблокирован.",peer)
                    except:
                      sender_user(id,f"⛔ | Произошла ошибка! Проверьте аргументы.",peer)
                  msg=msg.replace("бан ","")
                  rea=msg[-1]
                  user=msg[:-1]
                  ban(user,rea)
                else:
                  a=0
                  sender_user(id,"⚡ | У вас нет прав на данную команду",peer)
            elif msg.startswith("разбан") :
                nikk=data[str(id)]["name"]
                loadam()
                if owner==id or owner2==id or owner3==id or adm1==id or adm2==id or adm3==id or adm4==id or adm5==id or adm6==id or adm7==id or adm8==id:
                  def unban(user):
                    try:
                      user=int(user)
                    except:
                      user=0
                      sender_user(id,"⛔ | Произошла ошибка! Нужно вводить цифровой ID. \n✅ | Используйте: <<ID @пользователь>>",peer)
                    try:
                      user=int(user)
                      data[str(user)]["ban"]="0"
                      sender_user(id,f"✅ | @id{user} успешно разблокирован.",peer)
                    except:
                      sender_user(id,f"⛔ | Произошла ошибка! Проверьте аргументы.",peer)
                  msg=msg.replace("разбан ","")
                  user=msg
                  unban(user)
                else:
                  sender_user(id,"⚡ | У вас нет прав на данную команду",peer)
            elif msg.startswith("adm 0") :
                loadam()
                if owner==id or owner2==id or owner3==id and cid==1:
                  msg=msg.replace("adm 0 ","")
                  bb=len(msg)
                  try:
                    
                    msg=int(msg)
                  except:
                    text="⛔ | Произошла ошибка. Проверьте верность данных."
                  nul='0'
                  def cc(file):
                    x = open(f"{file}.txt", "w").close()
                    x = open(f"{file}.txt","r+")
                    x.write(nul)
                    x.close()
                  if adm1==msg:
                    
                    file="adm1"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки."
                  elif adm2==msg:
                    
                    file="adm2"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки."
                  elif adm3==msg:
                    
                    file="adm3"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки."
                  elif adm4==msg:
                    
                    file="adm4"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки."
                  elif adm5==msg:
                    
                    file="adm5"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки."
                  elif adm6==msg:
                    
                    file="adm6"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки.."
                  elif adm7==msg:
                    
                    file="adm7"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки."
                  elif adm8==msg:
                    
                    file="adm8"
                    cc(file)
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} снят с админки."
                  else:
                    text=f"⛔ | Пользователь с введеным ID не является администратором.."
                  sender_user(id, text, peer)
            elif msg.startswith("adm 1") :
                loadam()
                if owner==id or owner2==id or owner3==id:
                  msg=msg.replace("adm 1 ","")
                  if adm1==0:
                    
                    x = open('adm1.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm2==0:
                    
                    x = open('adm2.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm3==0:
                    
                    x = open('adm3.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm4==0:
                    
                    x = open('adm4.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm5==0:
                    
                    x = open('adm5.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm6==0:
                    
                    x = open('adm6.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm7==0:
                    
                    x = open('adm7.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm8==0:
                    
                    x = open('adm8.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  else:
                    text=f"⛔ | Произошла ОШИБКА ПАМЯТИ. Обратитесь к @wtop4ike."
                  sender_user(id, text, peer)
                else:
                  text="У вас нет прав на команду"
                  sender_user(id, text, peer)
            elif msg.startswith("отв") :
                loadam()
                if owner!=id and owner2!=id and owner3!=id and adm1!=id and adm2!=id and adm3!=id and adm4!=id and adm5!=id and adm6!=id and adm7!=id and adm8!=id:
                  text="У вас нет прав на данную команду"
                  sender_user(id, text, peer)
                else:
                  ido=re.findall(r'\w+', msg)[1]
                  if int((data[str(ido)]["rep"]))==1:
                    
                    ido=re.findall(r'\w+', msg)[1]
                    ido=int(ido)
                    otv=msg.replace(f"отв {ido}","")
                    try:
                      (data[str(ido)]["rep"])=0
                    except:
                      
                      pass
                    reporto(id, otv,ido)
                  else:
                    sender_user(id, f"Репорт от пользователя не найден.",peer)
            elif msg.startswith("adm 0") :
                loadam()
                if owner==id or owner2==id or owner3==id:
                  msg=msg.replace("adm 0 ","")
                  if adm1==0:
                    
                    x = open('adm1.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm2==0:
                    
                    x = open('adm2.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm3==0:
                    
                    x = open('adm3.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm4==0:
                    
                    x = open('adm4.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm5==0:
                    
                    x = open('adm5.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm6==0:
                    
                    x = open('adm6.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm7==0:
                    
                    x = open('adm7.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  elif adm8==0:
                    
                    x = open('adm8.txt','r+')
                    x1=x.read()
                    x.seek(0)
                    x.write(f'{msg}')
                    x.close()
                    nikk=data[str(id)]["name"]
                    text=f"✅ | {nikk}, user - @id{msg} назначен администратором."
                  else:
                    text=f"⛔ | Произошла ОШИБКА ПАМЯТИ. Обратитесь к @wtop4ike."
                  sender_user(id, text, peer)
                else:
                  text="У вас нет прав на команду"
                  sender_user(id, text, peer)
            elif msg.startswith("id"):
              try:
                  ido=re.findall(r'\w+', msg)[1]
                  infoe=vk_session.method("users.get", {"user_id":ido, "fields":"domain"})

                  text=str(infoe)
                  text=text.replace("[{'id':","")
                  text=re.findall(r'\w+', text)[0]
                  
              
                  sender_user(id, text, peer)
              
              except:
                text='⛔ | Произошла ошибка. Проверьте верность данных.'
                sender_user(id, text, peer)
            elif msg==("off") and id==owner:
                break

          

        savebd()
      
