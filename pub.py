# BOT LOGIN BY KHIE
# </> NOOB CODER 2K16
from linepy import *
from akad.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from KhieBots.thrift.protocol import TCompactProtocol
from KhieBots.thrift.transport import THttpClient
from KhieBots.ttypes import LoginRequest
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
khie = LINE() # LOGIN QR
#khie = LINE("YOUR TOKEN") # LOGIN TOKEN
#khie = LINE("YOUR EMAIL","YOUR PASSWORD") # EMAIL & PASS BOTS LOGIN
waitOpen = codecs.open("wait.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickerzOpen = codecs.open("stickerz.json","r","utf-8")
tokenOpen = codecs.open("toket.json","r","utf-8")
premiumOpen = codecs.open("user.json","r","utf-8")
#=====================================================================
#=====================================================================
khieProfile = khie.getProfile()
khieSettings = khie.getSettings()
khiePoll = OEPoll(khie)
khieMID = khie.getProfile().mid
#=====================================================================
#=====================================================================
loop = asyncio.get_event_loop()
admin =["u06090b28c2d014e95a0352cb0db47248"] # MID ADMIN FOR ADD CUSTOMER LOGIN
myAdmin = ["u06090b28c2d014e95a0352cb0db47248"] # MOD ADMIN FOR ADD CUSTOMER LOGIN
botStart = time.time()
msg_dict = {}
temp_flood = {}
groupName = {}
groupImage = {}
kuciyose = {}
protectname = []
wbanlist = []
protectinvite = []
protectkick = []
protectjoin = []
protectqr = []
protectantijs = []
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
images = json.load(imagesOpen)
stickers = json.load(stickersOpen)
stickerz = json.load(stickerzOpen)
token = json.load(tokenOpen)
premium = json.load(premiumOpen)
responsename = khie.getProfile().displayName
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

#=====================================================================
#=====================================================================
settings["myProfile"]["displayName"] = khieProfile.displayName
settings["myProfile"]["statusMessage"] = khieProfile.statusMessage
settings["myProfile"]["pictureStatus"] = khieProfile.pictureStatus
cont = khie.getContact(khieMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = khie.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open("temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = khie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = khie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

#=====================================================================
def headers():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "CHROMEOS\t5.5.1\tKhieBot-PCT\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers2():
    Headers = {
    'User-Agent': "Line/8.11.0",
    'X-Line-Application': "IOSIPAD\t6.9\tKhieBot-PC\t6.9",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers3():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "WIN10\t5.5.5\tKhieBot-PCT\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers4():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "DESKTOPMAC\t5.5.1\tKhieBot-PCT\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers

def headers5():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "DESKTOPWIN\t5.8.0\tKhieBot-PCT\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers6():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "WIN10\t5.5.5\tKhieBot-PCT\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
#def Template(to):
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    khie.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    khie.sendMessage(to, '', annda, 13)

def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            khie.sendMessage(to, text, {'MSG_SENDER_NAME': khie.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + khie.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            khie.sendMessage(to, text, {'MSG_SENDER_NAME': khie.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + khie.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@KhieGans  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    khie.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(khie.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + khie.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

#=====================================================================
#=====================================================================
#=====================================================================
def load():
    global images
    global stickers
    global stickerz
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
    with open("stickerz.json","r") as fp:
        stickerz = json.load(fp)
#=====================================================================

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
	
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        khie.sendMessage(to, textx, {'MSG_SENDER_NAME': client.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + khie.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================
def logError(text):
    khie.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickerz
        f = codecs.open('stickerz.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('user.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = khie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
async def khieBot(op):
    try:
        if settings["restartPoint"] != None:
            khie.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
                        
        if op.type in [22,24]:
            client.leaveRoom(op.param1)
#=====================================================================
        if op.type == 13:
            if khie.getProfile().mid in op.param3:
                G = khie.getCompactGroup(op.param1)
                if settings["autoJoin"] == True or settings['autoJoin'] == False:
                    if len(G.members) <= wait["Members"]:
                        khie.acceptGroupInvitation(op.param1)
                    else:
                        khie.acceptGroupInvitation(op.param1)
                if len(G.members) <= wait["Members"]:
                    khie.acceptGroupInvitation(op.param1)
                else:
                    if "u2cf74acf6ed04d122def4db8ffdd2e39" in op.param2:
                        khie.acceptGroupInvitation(op.param1)
#=====================================================================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != khieMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = khie.getContact(sender)
                        if msg.toType == 2:
                            anu = khie.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        khie.sendMessage(to, str(e))
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != khieMID: to = sender
                else: to = receiver
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = khie.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    khie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    khie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    khie.leaveGroup(group.id)
                    if text.lower() == "helper:listtoken" and to not in chatbot["botMute"]:
                        ret_ = "「 List Token 」\n"
                        ret_ += "\n1. CHROME OS"
                        ret_ += "\n2. IOS IPAD"
                        ret_ += "\n3. WIN 10"
                        ret_ += "\n4. MAC OS"
                        ret_ += "\n5. DESKTOP WIN"
                        ret_ += "\n\nUse : Logintoken <No>\nExample : Logintoken 1"
                        hello = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                "label": "List Token",
                                "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                            }
                        }
                        sendTemplate(to, data)
                    elif cmd == "about":
                        try:
                            arr = []
                            today = datetime.today()
                            thn = 2018 
                            bln = 8    #isi bulannya yg sewa
                            hr = 9   #isi tanggalnya yg sewa
                            future = datetime(thn, bln, hr)
                            days = (str(future - today))
                            comma = days.find(",")
                            days = days[:comma]
                            h = khie.getContact(khieMID)
                            groups = khie.getGroupIdsJoined()
                            contactlist = khie.getAllContactIds()
                            kontak = khie.getContacts(contactlist)
                            favorite = khie.getFavoriteMids()
                            fil = khie.getSettings().privacyReceiveMessagesFromNotFriend
                            seal = khie.getSettings().e2eeEnable
                            blockedlist = khie.getBlockedContactIds()
                            src = khie.getSettings().privacySearchByUserid
                            kontak2 = khie.getContacts(blockedlist)
                            status = {"kick": "", "invite": ""}
                            try:khie.kickoutFromGroup(to, [khieMID]);status["kick"] = "Normal"
                            except:status["kick"] = "Limit"
                            try:khie.inviteIntoGroup(to, [khieMID]);status["invite"] = "Normal"
                            except:status["invite"] = "Limit"
                            if src == True:alid = "Add From LineID : True"
                            else:alid = "Add From LineID : False"                            
                            if seal == True:letsel = "Letter Sealing : True"
                            if seal == False:letsel = "Letter Sealing : False"
                            if fil == True:fpes = "Filter Message : False"
                            if fil == False:fpes = "Filter Message : True"
                            ret_ = "About Bots :\n"
                            ret_ += "\nBots : {}".format(h.displayName)
                            ret_ += "\nGroup : {}".format(str(len(groups)))
                            ret_ += "\nFriend : {}".format(str(len(kontak)))
                            ret_ += "\nFavorite: {}".format(str(len(favorite)))
                            ret_ += "\nBlocked : {}".format(str(len(kontak2)))
                            ret_ += "\nChat send : {}".format(str(peler["sendcount"]))
                            ret_ += "\nChat received : {}".format(str(peler["receivercount"]))
                            ret_ += "\n{}".format(alid)
                            ret_ += "\n{}".format(letsel)
                            ret_ += "\n{}".format(fpes)
                            ret_ += "\nKick : %s" % status["kick"]
                            ret_ += "\nInvite : %s" % status["invite"]
                            ret_ += "\n\nType : Bot Login"
                            ret_ += "\nVersion : V..07"
                            hello = "{}".format(str(ret_))
                            data = {
                                "type": "text",
                                "text": "{}".format(str(ret_)),
                                "sentBy": {
                                    "label": "</> Noob Coder",
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                }
                            }
                            sendTemplate(to, data)
                        except Exception as e:
                            khie.sendMessage(to, str(e))
                    elif text.lower().startswith("logintoken") and to not in chatbot["botMute"]:
                        anu = msg.text.split(" ")
                        anu2 = msg.text.replace(anu[0] + " ","")
                        if anu2 == "1":
                            try:
                                a = headers()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='TeamAnuBot-PC')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 LOGIN QR 」\nType : GetAuthToken\n> Check your PM @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 LOGIN QR 」\nType : GetAuthToken\n> Click link qr for login @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                isi = "Get Token :\n\nAppName : CHROMEOS\n1. authToken : {}\n2. Certificate : {}".format(res.authToken, res.certificate)
                                os.system('cp -r anu.txt {}.txt'.format(msg._from))
                                os.system('echo -n "{}" > {}.txt'.format(isi, msg._from))
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nType [ Token ] to get your Token ',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nLink QR Expired, Not Found authToken And Certificate',' ', [msg._from])
                        if anu2 == "2":
                            try:
                                a = headers2()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='KhieBot-PC')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 LOGIN QR 」\nType : GetAuthToken\n> Check your PM @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 LOGIN QR 」\nType : GetAuthToken\n> Click link qr for login @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                isi = "Get Token :\n\nAppName : IOSIPAD\n1. authToken : {}\n2. Certificate : {}".format(res.authToken, res.certificate)
                                os.system('cp -r anu.txt {}.txt'.format(msg._from))
                                os.system('echo -n "{}" > {}.txt'.format(isi, msg._from))
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nType [ Token ] to get your Token ',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nLink QR Expired, Not Found authToken And Certificate',' ', [msg._from])
                        if anu2 == "3":
                            try:
                                a = headers3()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='KhieBot-PC')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 LOGIN QR 」\nType : GetAuthToken\n> Check your PM @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 LOGIN QR 」\nType : GetAuthToken\n> Click link qr for login @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                isi = "Get Token :\n\nAppName : WIN10\n1. authToken : {}\n2. Certificate : {}".format(res.authToken, res.certificate)
                                os.system('cp -r anu.txt {}.txt'.format(msg._from))
                                os.system('echo -n "{}" > {}.txt'.format(isi, msg._from))
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nType [ Token ] to get your Token ',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nLink QR Expired, Not Found authToken And Certificate',' ', [msg._from])
                        if anu2 == "4":
                            try:
                                a = headers4()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='KhieBot-PC')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 LOGIN QR 」\nType : GetAuthToken\n> Check your PM @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 LOGIN QR 」\nType : GetAuthToken\n> Click link qr for login @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                isi = "Get Token :\n\nAppName : MAC OS\n1. authToken : {}\n2. Certificate : {}".format(res.authToken, res.certificate)
                                os.system('cp -r anu.txt {}.txt'.format(msg._from))
                                os.system('echo -n "{}" > {}.txt'.format(isi, msg._from))
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nType [ Token ] to get your Token ',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nLink QR Expired, Not Found authToken And Certificate',' ', [msg._from])
                        if anu2 == "5":
                            try:
                                a = headers5()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='KhieBot-PC')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 LOGIN QR 」\nType : GetAuthToken\n> Check your PM @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 LOGIN QR 」\nType : GetAuthToken\n> Click link qr for login @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                isi = "Get Token :\n\nAppName : DESKTOPWIN\n1. authToken : {}\n2. Certificate : {}".format(res.authToken, res.certificate)
                                os.system('cp -r anu.txt {}.txt'.format(msg._from))
                                os.system('echo -n "{}" > {}.txt'.format(isi, msg._from))
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nType [ Token ] to get your Token ',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, 'Get Token :\n> @!\nLink QR Expired, Not Found authToken And Certificate',' ', [msg._from])
                        if anu2 == "":
                            khie.sendMessage(to, "[ ERROR ]")
                        if anu2 == " ":
                            khie.sendMessage(to, "[ ERROR ]")
                    elif text.lower() == "token" and to not in chatbot["botMute"]:
                        try:
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                isi = f.read()
                                if msg.toType == 2:khie.sendMention(msg.to, "Get Token :\n> @!\nCheck Your PM",' ', [msg._from])
                                else:pass
                                khie.sendMessage(msg._from, "{}".format(isi))
                                os.system('rm -r {}.txt'.format(msg._from))
                                f.close()
                        except:
                            khie.sendMessage(to, "[ ERROR ]\nToken Not Found")
                    elif cmd == ".help":
                        ret = "</> Help Message\n\n"
                        ret += "General Command :\n\n"
                        ret += "  • Helper:listtoken\n"
                        ret += "  • Helper @bye\n\n"
                        ret += "Service Command :\n\n"
                        ret += "  • Login sb\n"
                        ret += "  • Logout sb\n"
                        ret += "  • Restart sb\n"
                        ret += "  • Help login\n\n"
                        ret += "Owner Command :\n\n"
                        ret += "  • Adduser <@>\n"
                        ret += "  • Deluser <@>\n"
                        ret += "  • Remove < Name >\n"
                        ret += "  • List User"
                        hello = "{}".format(str(ret))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret)),
                            "sentBy": {
                                "label": "</> Noob Coder",
                                "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                            }
                        }
                        sendTemplate(to, data)
                    elif cmd == "helper:mention":
                        group = khie.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(khie.getProfile().mid)
                        khie.datamention(to,'Mention',nama)
                    elif cmd== 'helper @bye':
                        data = {
                            "type": "template",
                            "altText": "byebye",
                            "template": {
                                "type": "image_carousel",
                                "columns": [
                                    {
                                        "imageUrl":"https://stickershop.line-scdn.net/stickershop/v1/sticker/694837/IOS/sticker@2x.png",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                        }
                                    }
                                ]
                            }
                        }
                        sendTemplate(to, data)
                        khie.leaveGroup(to)
                    elif cmd.startswith("helper:skill "):
                        if msg._from in "u2cf74acf6ed04d122def4db8ffdd2e39":
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = khie.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = khie.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return khie.sendMessage(to,"not found name "+midn)
                           for target in targets:
                               khie.kickoutFromGroup(msg.to,[target])
                    elif cmd.startswith("helper:kick "):
                        if msg._from in "u2cf74acf6ed04d122def4db8ffdd2e39":
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        haha.kickoutFromGroup(to, [ls])
                                    except:
                                       haha.sendMessage(to, "Limited !")
                    elif cmd.startswith("helper:slain "):
                        if msg._from in "u2cf74acf6ed04d122def4db8ffdd2e39":
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = khie.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = khie.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return khie.sendMessage(to,"not found name "+midn)
                           for target in targets:
                               khie.kickoutFromGroup(msg.to,[target])
                               khie.findAndAddContactsByMid(target)
                               khie.inviteIntoGroup(msg.to, [target])
                               khie.cancelGroupInvitation(msg.to, [target])
                               time.sleep(5)
                               khie.inviteIntoGroup(msg.to, [target])
                    elif cmd == "helper:glist":
                       if msg._from in "u2cf74acf6ed04d122def4db8ffdd2e39":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = khie.getGroupIdsJoined()
                            sd = khie.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups\n".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                khie.generateReplyMessage(msg.id)
                                khie.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                    elif cmd.startswith("helper:broadcast"):
                      if msg._from in "u2cf74acf6ed04d122def4db8ffdd2e39":
                        tod = text.split(" ")
                        hey = text.replace(tod[0] + " ", "")
                        text = "{}".format(hey)
                        groups = khie.getGroupIdsJoined()
                        friends = khie.getAllContactIds()
                        for gr in groups:
                            data = {
                                "type": "text",
                                "text": "「 Group Broadcast 」\n\n{}".format(text),
                                "sentBy": {
                                    "label": "Group Broadcast",
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                }
                            }
                            bcTemplate(gr, data)
                            time.sleep(1)
                        khie.sendMessage(to, "Succes Group cast to {} group ".format(str(len(groups))))
                        for gr in friends:
                            data = {
                                "type": "text",
                                "text": "「 Friend Broadcast 」\n\n{}".format(text),
                                "sentBy": {
                                    "label": "Friend Broadcast",
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                }
                            }
                            bcTemplate(gr, data)
                            time.sleep(1)
                        khie.sendMessage(to, "Succes Friend cast to {} friend ".format(str(len(friends))))
                    elif text.lower() == "login sb" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            try:
                                a = headers6()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='KhieBot-PC')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 Request Login 」\nCheck your PM @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 Request Login 」\nClick link @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                if msg._from not in premium['listLogin']:
                                    premium['listLogin'][msg._from] =  '%s' % user
                                    isi = "{}".format(res.authToken)
                                    os.system('cp -r login {}'.format(user))
                                    os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                    os.system('screen -dmS {}'.format(user))
                                    os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))
                                    khie.sendMention(msg.to, '「 Login Succes 」\n> @!\n> User name : {}\n> Click link liff for access temp :\nline://app/1602687308-GXq4Vvk9?type=text&text=Gw%20Fans%20Khie'.format(user),' ', [msg._from])
                                else:
                                    khie.sendMention(msg.to, '「 Request Login 」\n@!\nLink QR Expired -_-',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, '「  ERROR 」\n@!\nPlease Nonactive Filter Chat Or Letter Sealing -_-',' ', [msg._from])
                    elif text.lower() == "login sb" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            khie.sendMention(msg.to, '「 Login SelfBot 」\nHello @!Sorry Please Logout First Log In With Type  < LogoutSb >\nBecause You Are Still Login',' ', [msg._from])
                    elif text.lower().startswith("adduser ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 not in premium['myService']:
                                    nama = str(text.split(' ')[1])
                                    premium['myService'][key1] =  '%s' % nama
                                    khie.sendMention(msg.to, '「 Add Service  」\nAdded @! to service','', [key1])
                                else:
                                    khie.sendMention(msg.to, '「 Add Service  」\nUser @! already in service','', [key1])
                    elif text.lower().startswith("deluser ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 in premium['myService']:
                                    del premium['myService'][key1]
                                    khie.sendMention(msg.to, '「 Del Service  」\nDeleted @! from service','', [key1])
                                else:
                                    khie.sendMention(msg.to, '「 Del Service  」\n\nUser @! not in service','', [key1])
                    elif text.lower() == "list user" and msg._from in myAdmin and to not in chatbot["botMute"]:
                        h = [a for a in premium['myService']]
                        k = len(h)//100
                        for aa in range(k+1):
                            msgas = '「 List Service 」\n'
                            no=0
                            for a in h:
                                no+=1
                                if premium['myService'][a] == "":cd = "None."
                                else:cd = premium['myService'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            msgas += "\n\n</> Noob Coder"
                            khie.sendMention(msg.to, msgas,'「 LIST USER SERVICE 」', h)
                    elif text.lower().startswith("addme ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                        if msg._from not in premium['myService']:
                            nama = str(text.split(' ')[1])
                            premium['myService'][msg._from] =  '%s' % nama
                            khie.sendMention(msg.to, "「 Add Me  」 \nAdd @! to Login..","",[msg._from])
                        else:
                            khie.sendMention(msg.to, "「Add Me 」\nOwner @! already in List..","",[msg._from])
                    elif text.lower() == "help login" and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            khie.sendMention(msg.to, 'Hai @!\n\n1. Type : Login Sb\n2. Check Personal Chat\n3. Press the Link Qr\n4. Type "Help" To see your command',' ', [msg._from])
                        khie.sendMention(msg.to, 'Type : LogOut selfbot\n\nHai @! Sorry You are not listed In List User',' ', [msg._from])
                        if msg._from in premium["myService"]:
                            del premium['listLogin'][msg._from]
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            khie.sendMention(msg.to, '「  Logout Sb  」\n> @! LogOut From Selfbot',' ', [msg._from])
                    elif text.lower() == "logout sb" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            khie.sendMention(msg.to, '「  Logout Sb  」\nHai @!Sorry Please You Login First By Type < Login Sb > Or Type < Help Login >',' ', [msg._from])
                    elif text.lower() == "restart sb" and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('screen -dmS {}'.format(user))
                            os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))
                            time.sleep(3)
                            khie.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
                    elif text.lower().startswith("remove") and msg._from in myAdmin and to not in chatbot["botMute"]:
                        sep = text.split(" ")
                        anu = text.replace(sep[0] + " ","")
                        os.system("screen -S {} -X quit".format(str(anu)))
                        os.system('rm -rf {}'.format(str(anu)))
                        time.sleep(2)
                        khie.sendMention(msg.to, '「 Remove 」\n> @!\nSucces remove file : {}'.format(str(anu)),' ', [msg._from])
                    elif text.lower() == "helper:reboot":
                        if msg._from in "u2cf74acf6ed04d122def4db8ffdd2e39":
                            khie.sendMention(to, "@! Brb , going to pee",' ', [msg._from])
                            restartBot()
                        else:pass
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoin"] == True or settings["autoJoin"] == False:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = khie.findGroupByTicket(ticket_id)
                                khie.acceptGroupInvitationByTicket(group.id,ticket_id)
        if op.type == 55:
            print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
    
def run():
    while True:
        try:
            ops = khiePoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(khieBot(op))
                   #clientBot(op)
                   khiePoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()