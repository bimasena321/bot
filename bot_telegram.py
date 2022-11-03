import os as a
import telebot
import datetime as date
import url as ad

a.system("clear")
api = "5569033372:AAFoIqF7K606cOA6AtlMmC0NVtWqbVRiy74"
bot = telebot.TeleBot(api)
    
@bot.message_handler(commands=['start'])
def mulai(pesan):
    bot.send_message(pesan.chat.id,"""
                     Halo selamat datang di bot bima sena
                     """)
    i = input("input: ")
    if bot.message_handler(commands=[f'start {i}']):
        bot.send_message(pesan.chat.id, i)
@bot.message_handler(commands=['bantuan'])
def help(bantu):
    bot.send_message(bantu.chat.id, """
                     perintah: 
                     /youtube => buka youtube
                     /cari => buka browser
                     /tanggal => melihat tanggal
                     /ig => buka instagram
                     /word => membuka word
                     /excel => membuka excel
                     /ppt => membuka ppt
                     """)
@bot.message_handler(commands=['youtube'])
def yt(y):
    b = str(ad.yt(y))
    bot.send_message(y.chat.id, "membuka Youtube",b)
   # bot.send_message(y.chat.id, b)
@bot.message_handler(commands=['cari'])
def cari(c):
    da = str(ad.cari(c))
    bot.send_message(c.chat.id, "membuka Browser",da)
    #bot.send_message(c.chat.id, da)
@bot.message_handler(commands=['tanggal'])
def time(t):
    ds = str(date.date.today()) 
    bot.send_message(t.chat.id, ds)
@bot.message_handler(commands=['ig'])
def ig(c):
    da = str(ad.ig(c))
    bot.send_message(c.chat.id, "membuka Instagram",da)
   # bot.send_message(c.chat.id, da)
@bot.message_handler(commands=['word'])
def word(c):
    da = str(ad.word(c))
    bot.send_message(c.chat.id, "Microsoft word dibuka",da)
@bot.message_handler(commands=['excel'])
def excel(c):
    da = str(ad.excel(c))
    bot.send_message(c.chat.id, "Microsoft excel dibuka",da)
@bot.message_handler(commands=['ppt'])
def ppt(c):
    da = str(ad.powerpoint(c))
    bot.send_message(c.chat.id, "Microsoft powerpoint dibuka",da)
@bot.message_handler(commands=['gtav'])
def gta5(c):
    da = str(ad.ytgame(c))
    bot.send_message(c.chat.id, "Video Gta v dibuka",da)
#print ("memulai bot....")
print("memuat bot....")
bot.polling()
    

    
    
    
    
    
    
    
    #def inputan(input1):
     #   ka = str(input1).lower()
      #  if ka in ("halo","p","s","siapa namamu","sopo seh kon iku"):
       #     return "Hai aku indonesia bot"
        #if ka in ("namamu siapa","jenengmu sopo"):
       #     return "aku indonesa bot salam kenal"
        #if ka in ("isok misuh a","isok mesoa","kon isok meso a cok"):
         #   return "isok, jancok raimu welek"
        #if ka in ("siapa pembuatmu"):
         #   return "rahasia, pokoknya inisialnya B dan A"
       # if ka in ("cok aku oleh takok a"):
        #    return "gk atek cok, gk isok a"
        #if ka in ("makanan kesukaan mu apa","panganan mu opo"):
         #   return "listrik"
        #if ka in ("takok mneh gpp a"):
         #   return "jancok,takok ae,mikir o dewe a ,ndas mu mumet iki lo"

    




