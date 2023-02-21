try:
  from paperscrollsdk import PaperScroll
  from config import *
except:
  quit("Проверьте, что вы установили все библиотеки!")

try:
  paperClient = PaperScroll(int(idmPS), tokenPS)
  paperApi = paperClient.getApi()
  otvet = paperApi.getMerchants()
  otvet = str(otvet)
  print(otvet)
except:
  quit("Произошла ошибка, проверьте конфиг на верность данных, либо обратитесь к кодеру.")