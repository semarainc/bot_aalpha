# -*- coding: utf-8 -*-
#Meteora Osterreich based on Chucky_bot

import LINETCR
import json
#from selenium.webdriver.firefox.options import Options
from linepy import *
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

global valid_load
valid_load = 0

client = LineClient('randi.verra@gmail.com','akugila344') #akun linebot
#client = LineClient(authToken='EqaT9nHiEWjcFQyrdjt5.pdzV2kqyPJaXDe5wmeMf5q.UEbsZ1QssEw7ix5lOa0+yJtOAzcTIHZ/zlbi0cTkeMg=')
client.log("Auth Token : " + str(client.authToken)) #debug token nya

#pembatas penggunaan linepy dengan linetcr
nadya = LINETCR.LINE()
#nadya.login(qr=True)
nadya.login(token=str(client.authToken))
nadya.loginResult()
print "Nadya-Login Success\n\n=====[Sukses Login]====="
print "[DEBUG] Membuka Webdriver sebagai Youtube_player [DISABLED] Reason: Some People may use mobile to run this bot"
#options = Options()
#options.add_argument("--headless")
#browser = webdriver.Firefox(firefox_options=options,executable_path='D:\\phantomjs\\bin\\geckodriver.exe')

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
╔═════════════════════════
║            ☆☞ S E L F ☜☆
╠═════════════════════════
╠➩〘Hi〙
╠➩〘Me〙
╠➩〘Mymid〙
╠➩〘Mid @〙
╠➩〘SearchID: (ID LINE)〙
╠➩〘Checkdate (DD/MM/YY)〙
╠➩〘Kalender〙
╠➩〘Steal contact〙
╠➩〘Pp @〙
╠➩〘Cover @〙
╠➩〘Auto like〙
╠➩〘Scbc Text〙
╠➩〘Cbc Text〙
╠➩〘Gbc Text〙
╠➩〘Getbio @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getvid @〙
╠➩〘Friendlist〙
╠═════════════════════════
║             💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""

botMessage ="""
╔═════════════════════════
║             ☆☞ B O T ☜☆
╠═════════════════════════
╠➩〘Absen〙
╠➩〘Respon〙
╠➩〘Runtime〙
╠➩〘Mycopy @〙
╠➩〘Mybackup〙
╠➩〘Mybio (Text)〙
╠➩〘Myname (Text)〙
╠➩〘@bye〙
╠═════════════════════════
║             💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""

mediaMessage ="""
╔═════════════════════════
║           ☆☞ M E D I A ☜☆
╠═════════════════════════
╠➩〘Gift〙
╠➩〘Gift1 @ s/d Gift10 @〙
╠➩〘Giftbycontact〙
╠➩〘Gif gore〙
╠➩〘Google: (Text)〙
╠➩〘Playstore NamaApp〙
╠➩〘Fancytext: Text〙
╠➩〘/musik Judul-Penyanyi〙
╠➩〘/lirik Judul-Penyanyi〙
╠➩〘/musrik Judul-Penyanyi〙
╠➩〘/ig UrsnameInstagram〙
╠➩〘Checkig UrsnameInstagram〙
╠➩〘/apakah Text (Kerang Ajaib)〙
╠➩〘/kapan Text (Kerang Ajaib)〙
╠➩〘/hari Text (Kerang Ajaib)〙
╠➩〘/berapa Text (Kerang Ajaib)〙
╠➩〘/berapakah Text〙
╠➩〘Youtubelink: Judul Video〙
╠➩〘Youtubevideo: Judul Video〙
╠➩〘Youtubesearch: Judul Video〙
╠➩〘Image NamaGambar〙
╠➩〘Say-id Text〙
╠➩〘Say-en Text〙
╠➩〘Say-jp Text〙
╠➩〘Image NamaGambar〙
╠➩〘Tr-id Text (Translate En Ke ID〙
╠➩〘Tr-en Text (Translate ID Ke En〙
╠➩〘Tr-th Text (Translate ID Ke Th〙
╠➩〘Id@en Text (Translate ID Ke En〙
╠➩〘Id@th Text (Translate ID Ke TH〙
╠➩〘En@id Text (Translate En Ke ID〙
╠═════════════════════════
║             💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""

groupMessage ="""
╔═════════════════════════
║           ☆☞ G R O U P ☜☆
╠═════════════════════════
╠➩〘Welcome〙
╠➩〘Say welcome〙
╠➩〘Invite creator〙
╠➩〘Setview〙
╠➩〘Viewseen〙
╠➩〘Gn: (NamaGroup)〙
╠➩〘Tag all〙
╠➩〘Recover〙
╠➩〘Cancel〙
╠➩〘Cancelall〙
╠➩〘Gcreator〙
╠➩〘Ginfo〙
╠➩〘Gurl〙
╠➩〘List group〙
╠➩〘Pict group: (NamaGroup)〙
╠➩〘Spam: (Text)〙
╠➩〘Add all〙
╠➩〘Kick: (Mid)〙
╠➩〘Invite: (Mid)〙
╠➩〘Invite〙
╠➩〘Memlist〙
╠➩〘Getgroup image〙
╠➩〘Urlgroup Image〙
╠═════════════════════════
║            💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""
tjia="u46c5a7fc7e5c65bc38a1954aeacb8942"

setMessage ="""
╔═════════════════════════
║              ☆☞ S E T ☜☆
╠═════════════════════════
╠➩〘Sambutan on/off〙
╠➩〘Url on/off〙
╠➩〘Alwaysread on/off〙
╠➩〘Sider on/off〙
╠➩〘Contact on/off〙
╠➩〘Simisimi on/off〙
╠═════════════════════════
║             💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""

creatorMessage ="""
╔═════════════════════════
║         ☆☞ C R E A T O R ☜☆
╠═════════════════════════
╠➩〘Admin add @〙
╠➩〘Admin remove @〙
╠➩〘Crash〙
╠➩〘Kickall〙
╠➩〘Bc: (Text)〙
╠➩〘Join group: (NamaGroup〙
╠➩〘Leave group: (NamaGroup〙
╠➩〘Leave all group〙
╠➩〘Tag on/off〙
╠➩〘Bot restart〙
╠➩〘Turn off〙
╠═════════════════════════
║             💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""

adminMessage ="""
╔═════════════════════════
║            ☆☞ A D M I N ☜☆
╠═════════════════════════
╠➩〘Admin list〙
╠➩〘Allprotect on/off〙
╠➩〘Ban〙
╠➩〘Unban〙
╠➩〘Ban @〙
╠➩〘Unban @〙
╠➩〘Ban list〙
╠➩〘Clear ban〙
╠➩〘Kill〙
╠➩〘Kick @〙
╠➩〘Set member: (Jumblah)〙
╠➩〘Ban group: (NamaGroup〙
╠➩〘Del ban: (NamaGroup〙
╠➩〘List ban〙
╠➩〘Kill ban〙
╠➩〘Glist〙
╠➩〘Glistmid〙
╠➩〘Details group: (Gid)〙
╠➩〘Cancel invite: (Gid)〙
╠➩〘Invitemeto: (Gid)〙
╠➩〘Acc invite〙
╠➩〘Removechat〙
╠➩〘Qr on/off〙
╠➩〘Autokick on/off〙
╠➩〘Ghost on/off〙
╠➩〘Autocancel on/off〙
╠➩〘Invitepro on/off〙
╠➩〘Join on/off〙
╠➩〘Joincancel on/off〙
╠➩〘Respon on/off〙
╠➩〘Responkick on/off〙
╠═════════════════════════
║            💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""

helpMessage ="""
╔═════════════════════════
║              ☆☞ H E L P ☜☆
╠═════════════════════════
╠➩〘Help 1〙
╠➩〘Help 2〙
╠➩〘Help 3〙
╠➩〘Help 4〙
╠➩〘Help 5〙
╠➩〘Help 6〙
╠➩〘Help 7〙
╠➩〘Owner〙
╠➩〘Pap owner〙
╠➩〘Admin〙
╠➩〘Speed〙
╠➩〘Speed test〙
╠➩〘Status〙
╠═════════════════════════
║             💠 By : Meteora 💠
║    〽️ Based On Chucky Bot By Nadya 〽️
╚═════════════════════════
"""


KAC=[nadya]
mid = nadya.getProfile().mid
Bots=[mid]
Creator=["u46c5a7fc7e5c65bc38a1954aeacb8942","u3c366fd8a418a63031744e56304985e5"]
admin=["u46c5a7fc7e5c65bc38a1954aeacb8942","u3c366fd8a418a63031744e56304985e5","ud0a76b9d9f80b4f6ed331ad45f204f93"]

contact = nadya.getProfile()
backup1 = nadya.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = nadya.getProfile().displayName


wait = {
    "LeaveRoom":False,
    "AutoJoin":True,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":True,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'likeOn':{},
    'detectMention':True,
    'kickMention':False,      
    'timeline':True,
    "Timeline":True,
    "comment":"Liked, Keren Deh bang :v",    
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":True,
    "Ghost":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def isstatus(paramser):
  #0=privatechat, 1=multichat, 2=groupchat
  konter = str(paramser)
  if "toType=0" in konter:
    return 0
  elif "toType=1" in konter:
    return 1
  elif "toType=2" in konter:
    return 2

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    #browser.quit()
    os.execl(python, python, * sys.argv)


def bot(op):
    #global valid_load
    #valid_load = 0
    try:
        print op.type
        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              nadya.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                sendPesan(op,op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = nadya.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendPesan(op,op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        sendPesan(op,op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                else:
                                    sendPesan(op,op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            pass
            #nadya.leaveRoom(op.param1)

        if op.type == 21:
            pass
            #nadya.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    nadya.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = nadya.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        nadya.acceptGroupInvitation(op.param1)
                        sendPesan(op,op.param1,"Maaf " + nadya.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        nadya.leaveGroup(op.param1)                        
		    else:
                        nadya.acceptGroupInvitation(op.param1)
			sendPesan(op,op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = nadya.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        nadya.rejectGroupInvitation(op.param1)
		    else:
                        nadya.acceptGroupInvitation(op.param1)
			sendPesan(op,op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        nadya.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			nadya.cancelGroupInvitation(op.param1, [op.param3])
			sendPesan(op,op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    nadya.cancelGroupInvitation(op.param1,[op.param3])
                    nadya.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               nadya.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    nadya.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        nadya.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        nadya.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        nadya.kickoutFromGroup(op.param1,[op.param2])
			nadya.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    nadya.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        nadya.kickoutFromGroup(op.param1,[op.param2])
			nadya.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                nadya.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        nadya.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    nadya.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    nadya.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            sendPesan(op,op.param1,"Hallo " + nadya.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            nadya.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            sendPesan(op,op.param1,"Good Bye " + nadya.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            nadya.inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP"

        if op.type == 26 or op.type == 22 or op.type == 25 or op.type == 23:
          msg = op.message
          print msg
          temp = str(msg.contentMetadata)
          #kont_json = eval(msg.contentMetadata["GC_EVT_TYPE"])
          print temp
          if "'GC_EVT_TYPE':" in temp:
            print("kontoru")
            kont_json = str(msg.contentMetadata)
            kont_json = kont_json.replace("'",'"')
            #print "replaced"
            kont = json.loads(kont_json)
            #print "kontorunn"
            #print kont['GC_EVT_TYPE']
            if kont['GC_EVT_TYPE'] == 'S':
              print "GC Started"
              sendPesan(op,kont['GC_CHAT_MID'].encode('utf-8'),"Group Call Started")
            if kont['GC_EVT_TYPE'] == 'E':
              print "GC Ended"
              sendPesan(op,kont['GC_CHAT_MID'].encode('utf-8'),"Group Call Ended")

        if op.type == 26 or op.type == 22 or op.type == 25 or op.type == 23:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                sendPesan(op,msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = nadya.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  sendPesan(op,msg.to,ret_)
                                  nadya.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = nadya.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  sendPesan(op,msg.to,ret_)
                                  break              


        if op.type == 26 or op.type == 22 or op.type == 25 or op.type == 23:
            msg = op.message


            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    nadya.sendChatChecked(msg.from_,msg.id)
                else:
                    nadya.sendChatChecked(msg.to,msg.id)
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     nadya.like(url[25:58], url[66:], likeType=1005)
                     nadya.comment(url[25:58], url[66:], wait["comment"])
                     sendPesan(op,msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            sendPesan(op,msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            sendPesan(op,msg.to,"Ditambahkan")
		    else:
			sendPesan(op,msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendPesan(op,msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        sendPesan(op,msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     sendPesan(op,msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = nadya.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = nadya.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         sendPesan(op,msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = nadya.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = nadya.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         sendPesan(op,msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = nadya.getGroup(msg.to)
                    print ginfo
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        sendPesan(op,msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        sendPesan(op,msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        sendPesan(op,msg.to,"Can not be used outside the group")
                    else:
                        sendPesan(op,msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                if isstatus(str(op.message)) == 0:
                  msg.to = msg.from_
                else:
                  pass
                nadya.sendMessage(msg)
		sendPesan(op,msg.to,"Itu Creator Saya(^_^)")
		
            elif msg.text in ["Admin","admin"]:
                msg.contentType = 13
                if isstatus(str(op.message)) == 0:
                  msg.to = msg.from_
                else:
                  pass
                admin1 = "u46c5a7fc7e5c65bc38a1954aeacb8942"
                admin2 = "ud0a76b9d9f80b4f6ed331ad45f204f93"
                admin3 = "u3c366fd8a418a63031744e56304985e5"
                msg.contentMetadata = {'mid': tjia}
                nadya.sendMessage(msg)
                msg.contentMetadata = {'mid': admin1}
                nadya.sendMessage(msg)
                msg.contentMetadata = {'mid': admin2}
                nadya.sendMessage(msg)
                msg.contentMetadata = {'mid': admin3}
                nadya.sendMessage(msg)                
		sendPesan(op,msg.to,"Itu Admin Saya (^_^)")	
		
 
                
            elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = nadya.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   sendPesan(op,msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            sendPesan(op,msg.to,"Admin Meteora Ditambahkan")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                sendPesan(op,msg.to,"Command Denied.")
                sendPesan(op,msg.to,"Creator Permission Required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = nadya.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   sendPesan(op,msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            sendPesan(op,msg.to,"Admin Meteora Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                sendPesan(op,msg.to,"Command Denied.")
                sendPesan(op,msg.to,"Creator Permission Required.")
                
            elif msg.text in ["Admin list","admin list","List admin"]:
              if admin == []:
                  sendPesan(op,msg.to,"The Admin List Is Empty")
              else:
                  sendPesan(op,msg.to,"Tunggu...")
                  mc = "╔═════════════════════════\n║        ☆☞ ADMIN Meteora-Framework ☜☆\n╠═════════════════════════\n"
                  for mi_d in admin:
                      mc += "╠••> " +nadya.getContact(mi_d).displayName + "\n"
                  sendPesan(op,msg.to,mc + "╚═════════════════════════")
                  print "[Command]Admin List executed"
                 

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = nadya.getGroup(msg.to)
          #print ginfo
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                nadya.sendMessage(msg)
    #print (ginfo)
		sendPesan(op,msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    sendPesan(op,msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.findAndAddContactsByMid(target)
                                contact = nadya.getContact(target)
                                cu = nadya.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                sendPesan(op,msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                sendPesan(op,msg.to,"Profile Picture " + contact.displayName)
                                nadya.sendImageWithURL(msg.to,image)
                                sendPesan(op,msg.to,"Cover " + contact.displayName)
                                nadya.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                sendPesan(op,msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                nadya.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = nadya.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             sendPesan(op,msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 nadya.findAndAddContactsByMid(target)
                                 nadya.inviteIntoGroup(msg.to,[target])
                                 sendPesan(op,msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      sendPesan(op,msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Kagi 1"]:
                #sendPesan(op,msg.to,creatorMessage)
                nadya.sendText(msg.to,creatorMessage)

            elif msg.text in ["Kagi 2"]:
                #sendPesan(op,msg.to, msg,groupMessage)
                nadya.sendText(msg.to,groupMessage)

            elif msg.text in ["Kagi"]:
                #sendPesan(op,msg.to,helpMessage)
                nadya.sendText(msg.to,helpMessage)

            elif msg.text in ["Kagi 3"]:
                #sendPesan(op,msg.to, msg,selfMessage)
                nadya.sendText(msg.to,selfMessage)

            elif msg.text in ["Kagi 4"]:
                #sendPesan(op,msg.to,botMessage)
                nadya.sendText(msg.to,botMessage)

            elif msg.text in ["Kagi 5"]:
                #sendPesan(op,msg.to,setMessage)
                nadya.sendText(msg.to,setMessage)

            elif msg.text in ["Kagi 6"]:
#                sendPesan(op,msg.to,mediaMessage)
                nadya.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Kagi 7"]:
#                sendPesan(op,msg.to,adminMessage)
                nadya.sendText(msg.to,adminMessage)                
                

 
            elif msg.text in ["List group"]:
                    gid = nadya.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = nadya.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    sendPesan(op,msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = nadya.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    sendPesan(op,msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    sendPesan(op,msg.to, "Khusus Owner")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        sendPesan(op,msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +nadya.getGroup(gid).name + "\n"
                        sendPesan(op,msg.to,"===[Ban Group]===\n"+mc)
		else:
		    sendPesan(op,msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if nadya.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    sendPesan(op,msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    sendPesan(op,msg.to, "Khusus Owner")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = nadya.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = nadya.getGroup(i).name
		            if h == ng:
		                nadya.inviteIntoGroup(i,[Creator])
			        sendPesan(op,msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        sendPesan(op,msg.to,"Khusus Owner")
		except Exception as e:
		    sendPesan(op,msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = nadya.getGroup(i).name
		        if h == ng:
			    sendPesan(op,i,"Bot Di Paksa Keluar Oleh Owner!")
		            nadya.leaveGroup(i)
			    sendPesan(op,msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    sendPesan(op,msg.to,"Khusus Owner")
 
	    elif "Leave all group" == msg.text:
		gid = nadya.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			sendPesan(op,i,"Bot Di Paksa Keluar Oleh Owner!")
		        nadya.leaveGroup(i)
		    sendPesan(op,msg.to,"Success Leave All Group")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = nadya.getGroupIdsJoined()
                for i in gid:
                    h = nadya.getGroup(i).name
                    gna = nadya.getGroup(i)
                    if h == saya:
                        nadya.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        nadya.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        sendPesan(op,msg.to,"Tidak Ada Yang Pending")
                else:
                    sendPesan(op,msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    nadya.updateGroup(X)
                    sendPesan(op,msg.to,"Url Sudah Aktif")
                else:
                    sendPesan(op,msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    nadya.updateGroup(X)
                    sendPesan(op,msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    sendPesan(op,msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    sendPesan(op,msg.to,"Auto Join Sudah Aktif")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    sendPesan(op,msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    sendPesan(op,msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    sendPesan(op,msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")		    
		    
 
            elif msg.text in ["Respon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    sendPesan(op,msg.to,"Auto Respon Sudah Aktif")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")

            elif msg.text in ["Respon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    sendPesan(op,msg.to,"Auto Respon Sudah Off")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")	
		    
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    sendPesan(op,msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    sendPesan(op,msg.to,"Auto Respon Kick Sudah Off")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                sendPesan(op,msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    sendPesan(op,msg.to,"Khusus Owner")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                sendPesan(op,msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    sendPesan(op,msg.to,"Khusus Owner")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                sendPesan(op,msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    sendPesan(op,msg.to,"Khusus Owner")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                sendPesan(op,msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    sendPesan(op,msg.to,"Khusus Owner")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	sendPesan(op,msg.to,"QR Protect Sudah Aktif")
	     else:
		    sendPesan(op,msg.to,"Khusus Owner")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	sendPesan(op,msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    sendPesan(op,msg.to,"Khusus Owner")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     sendPesan(op,msg.to,"Auto Kick Sudah Aktif")
	     else:
	        sendPesan(op,msg.to,"Khusus Owner")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     sendPesan(op,msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        sendPesan(op,msg.to,"Khusus Owner")	     

	    elif "Ghost on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = True
		     sendPesan(op,msg.to,"Ghost Sudah Aktif")
	     else:
	        sendPesan(op,msg.to,"Khusus Owner")		     

	    elif "Ghost off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = False
		     sendPesan(op,msg.to,"Ghost Sudah Di Nonaktifkan")
	     else:
	         sendPesan(op,msg.to,"Khusus Owner")		     

            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    wait["Ghost"] = True                     
                    sendPesan(op,msg.to,"All Protect Sudah Aktif Semua")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    wait["Ghost"] = False                    
                    sendPesan(op,msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    sendPesan(op,msg.to,"Khusus Owner")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                sendPesan(op,msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                sendPesan(op,msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                sendPesan(op,msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                sendPesan(op,msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        sendPesan(op,msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        sendPesan(op,msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        sendPesan(op,msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        sendPesan(op,msg.to,"Sudah Off(p′︵‵。)")
                        
                        
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                sendPesan(op,msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    sendPesan(op,msg.to, "Cek Sider Off")
                else:
                    sendPesan(op,msg.to, "Heh Belom Di Set")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠➩✔️ Sambutan : On\n"
		else:md+="╠➩❌ Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                else: md +="╠➩❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                else: md +="╠➩❌ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
		else: md+="╠➩❌ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                else: md+= "╠➩❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                else: md+= "╠➩❌ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
		else:md+="╠➩❌ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
		else:md+="╠➩❌ Auto Kick : Off\n"
		if wait["Ghost"] == True: md+="╠➩✔️ Ghost : On\n"
		else:md+="╠➩❌ Ghost : Off\n"
		if wait["alwaysRead"] == True: md+="╠➩✔️ Always Read : On\n"
		else:md+="╠➩❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠➩✔️ Auto Respon : On\n"
		else:md+="╠➩❌ Auto Respon : Off\n"		
		if wait["kickMention"] == True: md+="╠➩✔️ Auto Respon Kick : On\n"
		else:md+="╠➩❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠➩✔️ Auto Sider : On\n"
		else:md+="╠➩❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠➩✔️ Simisimi : On\n"
		else:md+="╠➩❌ Simisimi: Off\n"		
                sendPesan(op,msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                nadya.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    sendPesan(op,msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)
                
        


            elif msg.text in ["Tagall","Tag all"]:
                  konter = str(msg)
                  print (konter)
                  if isstatus(konter) == 0:
                    sendPesan(op,msg.to,"Command Ini Tidak Bisa Digunakan di Private Chat")
                  if "toType=1" in konter:
                    group = nadya.getRoom(msg.to)
                    nama = [contact.mid for contact in group.contacts]
                  else:
                    group = nadya.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                  print group
                  print ("\n batas")
                  print(group.contacts)
                  

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      nadya.sendMessage(msg)
                  except Exception as error:
                      print error


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                sendPesan(op,msg.to, "☆Checkpoint Checked☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = nadya.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        sendPesan(op,msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        sendPesan(op,msg.to, "☆Auto Checkpoint☆")                        
                    else:
                        sendPesan(op,msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    nadya.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    sendPesan(op,msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = nadya.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    nadya.findAndAddContactsByMids(mi_d)
		    sendPesan(op,msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                sendPesan(op,msg.to,"Send Contact")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                sendPesan(op,msg.to,"Shere Post Kamu Yang Mau Di Like!")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                sendPesan(op,msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                sendPesan(op,msg.to,"Send Contact") 
                

	    elif "Recover" in msg.text:
		thisgroup = nadya.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		nadya.createGroup("Recover", mi_d)
		sendPesan(op,msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    nadya.updateGroup(X)
                else:
                    sendPesan(op,msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    nadya.kickoutFromGroup(msg.to,[midd])
		else:
		    sendPesan(op,msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                nadya.findAndAddContactsByMid(midd)
                nadya.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "u14f64e139a3817afaabe27d237afb36b"
                nadya.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                msg_meta = str(msg)
                if "toType=1" in msg_meta:
                  msg_meta = str(msg)
                  gs = nadya.getRoom(msg.to)
                  sendPesan(op,msg.to,"Selamat Datang Di Multi Chat dengan Kode: " + msg.to)
                else:
                  gs = nadya.getGroup(msg.to)
                  sendPesan(op,msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			sendPesan(op,i,"=======[BROADCAST]=======\n\n"+bc+"\n\nTerima Kasih Atas Perhatiannya")
		    sendPesan(op,msg.to,"Success BC BosQ")
		else:
		    sendPesan(op,msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = nadya.getGroupIdsInvited()
                for i in gid:
                    nadya.rejectGroupInvitation(i)
                sendPesan(op,msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = nadya.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        nadya.updateGroup(x)
                    gurl = nadya.reissueGroupTicket(msg.to)
                    sendPesan(op,msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        sendPesan(op,msg.to,"Can't be used outside the group")
                    else:
                        sendPesan(op,msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = nadya.activity(limit=5)
		    sendPesan(op,msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    nadya.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		sendPesan(op,msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                sendPesan(op,msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		sendPesan(op,msg.to, "Progress...")
                sendPesan(op,msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                sendPesan(op,msg.to, "Progress...")
                elapsed_time = time.time() - start
                sendPesan(op,msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    sendPesan(op,msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    sendPesan(op,msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendPesan(op,msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    sendPesan(op,msg.to,"Succes BosQ")
                                except:
                                    sendPesan(op,msg.to,"Error")
			    else:
				sendPesan(op,msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    sendPesan(op,msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +nadya.getContact(mi_d).displayName + "\n"
                    sendPesan(op,msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendPesan(op,msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                sendPesan(op,msg.to,"Succes BosQ")
                            except:
                                sendPesan(op,msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    sendPesan(op,msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

            elif msg.text.lower() in ["bot","meteora","osterreich"]:
                sendPesan(op,msg.to,"Apa Manggil~Manggil Aku!?") 
                sendPesan(op,msg.to,"☆Ketik ☞Help☜ Untuk Bantuan☆") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            sendPesan(op,msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            nadya.kickoutFromGroup(msg.to,[jj])
                        sendPesan(op,msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    sendPesan(op,msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            sendPesan(op,msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                nadya.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall-Restict" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = nadya.getGroup(msg.to)
                        sendPesan(op,msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            sendPesan(op,msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        nadya.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        sendPesan(op,msg.to,str(e))
			    nadya.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    sendPesan(op,msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    sendPesan(op,msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "NADYA,'"}
                nadya.sendMessage(msg)

 
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = nadya.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       sendPesan(op,msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               nadya.CloneContactProfile(target)
                               sendPesan(op,msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    nadya.updateDisplayPicture(backup1.pictureStatus)
                    nadya.updateProfile(backup1)
                    sendPesan(op,msg.to, "Done (^_^)")
                except Exception as e:
                    sendPesan(op,msg.to, str(e))

 
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						sendPesan(op,msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						sendPesan(op,msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						nadya.sendAudioWithURL(msg.to,abc)
						sendPesan(op,msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        sendPesan(op,msg.to, hasil)
                except Exception as wak:
                        sendPesan(op,msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						sendPesan(op,msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						nadya.sendAudioWithURL(msg.to,abc)
						sendPesan(op,msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						sendPesan(op,msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    nadya.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendPesan(op,msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                sendPesan(op,msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendPesan(op,msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                sendPesan(op,msg.to,"Upload image failed.")
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendPesan(op,msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.getContact(target)
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                sendPesan(op,msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendPesan(op,msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.getContact(target)
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                sendPesan(op,msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hNPsZWL9WEX9OIz0lhyFuKHJmHxI5DRc3NkJaETwkRklqGwQoJkNbTGklHRo2G1B7cxFXH2NxSU03"]
                                pilih = random.choice(link)
                                nadya.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    sendPesan(op,msg.to, bctxt)
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = nadya.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      sendPesan(op,manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = nadya.getAllContactIds()
                  for manusia in orang:
                    sendPesan(op,manusia, (broadcasttxt))

 
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    sendPesan(op,msg.to, detail + user + user1 + followers + following + post + link + details)
                    nadya.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	sendPesan(op,msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                nadya.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                nadya.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    sendPesan(op,msg.to,'https://www.youtube.com' + results['href'])
                except:
                    sendPesan(op,msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        valid_load = 0
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        #browser.get('https://www.youtube.com/'+ results['href'])
                        valid_load = 1
                        nadya.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                        sendPesan(op,msg.to,'Memainkan Video Dalam Bentuk Stream Apabila Group Call Aktif, Dan Bot Tergabung(seijin admin)')
                        #sendPesan(op,msg.to,'Untuk Mengetahui Judul Lagu Yang Sedang Dimainkan, Gunakan Command "Currentsong')
                    except:
                        sendPesan(op,msg.to, "Could not find it")                    
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = nadya.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +nadya.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    sendPesan(op,msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                sendPesan(op,msg.to,"Sedang Mencari...")
                sendPesan(op,msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                sendPesan(op,msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = nadya.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        sendPesan(op,msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = nadya.getProfile()
                        profile.statusMessage = string
                        nadya.updateProfile(profile)
                        sendPesan(op,msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = nadya.getProfile()
                        profile.displayName = string
                        nadya.updateProfile(profile)
                        sendPesan(op,msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +nadya.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                sendPesan(op,msg.to,middd)
                nadya.sendText(msg.from_,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["profil"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u3c366fd8a418a63031744e56304985e5"}
                nadya.sendMessage(msg)
                sendPesan(op,msg.to,"Nama: Nano\nUmur: 69\nHobi: ikkeh")

            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")                


            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                if isstatus(msg) == 0:
                  sendPesan(op,msg.from_," Simisimi Di Aktifkan")
                else:
                  sendPesan(op,msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                if isstatus(msg) == 0:
                  sendPesan(op,msg.from_,"Simisimi Di Nonaktifkan")
                else:
                  sendPesan(op,msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                temps = msg
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    if isstatus(temps) == 0:
                      nadya.sendImageWithURL(msg.from_,path)
                    else:
                      nadya.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        sendPesan(op,msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                sendPesan(op,msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                sendPesan(op,msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                sendPesan(op,msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                sendPesan(op,msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                sendPesan(op,msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                sendPesan(op,msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                sendPesan(op,msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = nadya.getAllContactIds()
                kontak = nadya.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                sendPesan(op,msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = nadya.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                sendPesan(op,msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = nadya.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendPesan(op,msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = nadya.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            nadya.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = nadya.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                nadya.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = nadya.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                sendPesan(op,msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    sendPesan(op,msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    sendPesan(op,msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    sendPesan(op,msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    sendPesan(op,msg.to,"Profile Picture " + contact.displayName)
                    nadya.sendImageWithURL(msg.to,image)
                    sendPesan(op,msg.to,"Cover " + contact.displayName)
                    nadya.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = nadya.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                nadya.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    sendPesan(op,msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    sendPesan(op,msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    sendPesan(op,msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    sendPesan(op,msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                sendPesan(op,msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                sendPesan(op,msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                sendPesan(op,msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = nadya.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                nadya.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = nadya.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                nadya.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        nadya.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        sendPesan(op,msg.to,"Done")
                    except Exception as error:
                        print error
                        sendPesan(op,msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        sendPesan(op,msg.to,"Invalid group id")
                    else:
                        try:
                            nadya.findAndAddContactsByMid(msg.from_)
                            nadya.inviteIntoGroup(gid,[msg.from_])
                        except:
                            sendPesan(op,msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                sendPesan(op,msg.to, "Tunggu Sebentar. . .")                    
                gid = nadya.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (nadya.getGroup(i).name +" ~> ["+str(len(nadya.getGroup(i).members))+"]")
                sendPesan(op,msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = nadya.getGroupIdsJoined()
                kontak = nadya.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                sendPesan(op,msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    sendPesan(op,msg.to,"Sedang Mencari...")
                    sendPesan(op,msg.to, "https://www.google.com/" + b)
                    sendPesan(op,msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        sendPesan(op,msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = nadya.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            sendPesan(op,msg.to,h)
                        except Exception as error:
                            sendPesan(op,msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = nadya.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                nadya.rejectGroupInvitation(i)
                            except:
                                sendPesan(op,msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        sendPesan(op,msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        sendPesan(op,msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = nadya.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = nadya.getGroup(i)
                            _list += gids.name
                            nadya.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        sendPesan(op,msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        sendPesan(op,msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                nadya.sendGifWithURL(msg.to,gore)




        if op.type == 59:
            print op
        if op.type == 26:
            msg = op.message
            konter = str(msg)
            if "'Call History :" in konter:
              print "[INFO] Incoming Call From Someone, Sending Preventive Message"
              sendPesan(op,msg.to, "Saya Tidak Bisa Menerima Call, karena saya bot")


    except Exception as error:
        print error

def sendPesan(op, ke, pesan):
  msg = op.message
  konter = str(msg)
  if isstatus(konter) == 0:
    nadya.sendText(msg.from_, pesan)
  else:
    nadya.sendText(ke, pesan)

while True:
    try:
        Ops = nadya.fetchOps(nadya.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(nadya.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            nadya.Poll.rev = max(nadya.Poll.rev, Op.revision)
            bot(Op)

