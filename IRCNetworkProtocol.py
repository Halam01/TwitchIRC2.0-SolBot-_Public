'''
Created on Sep 6, 2015
Updated on Dec 21, 2015

@author: Hanna Alam
'''

import socket

class IRC_Connect():
    #inits variables needed to connect to the twitch API, opens socket to twitch.tv and logs in
    def __init__(self):
        self.SERVER = "irc.twitch.tv"
        self.PORT = 6667
        self.NICK = ""
        #self.PASS = ""
        self.PASS = ""
        self.clientID = ""
        self.clientSecret = ""
        self.STATUS = "Offline"

        self.IRC_socket = socket.socket()

        print("Connecting to server...")
    
        self.IRC_socket.connect((self.SERVER,self.PORT))
        print("Connected.")
        print("Logging on...")
        
    #connects to specified chat channel
    def ConnectChannel(self, channel):
        self.CHANNEL = "#"+str(channel).strip()
        to_send = ("PASS " + self.PASS +'\r\n' + "NICK " + self.NICK + '\r\n').encode(encoding='utf-8')
        self.IRC_socket.send(to_send)

        to_send = ('JOIN ' + self.CHANNEL + '\r\n').encode(encoding='utf-8')
        self.IRC_socket.send(to_send)

        self.STATUS = "Online"
        
    #sends message to chat channel
    def SendMsg(self, text):
        to_send = ('PRIVMSG ' + self.CHANNEL + ' :' + text +'\r\n').encode(encoding='utf-8')
        self.IRC_soct.send(to_send)
        print("Message sent to channel: " + self.CHANNEL)

    