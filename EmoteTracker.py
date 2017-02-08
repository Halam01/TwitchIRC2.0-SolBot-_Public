'''
Created on Jan 8, 2016

@author: Hanna
'''
import IRCNetworkProtocol
import time


class EmoteBins():
    def __init__(self):
        self.bins = {}
    
    #adds an emote to track and inits its value to 0
    def add_emote(self, emote : str):
        self.bins[emote] = 0
    
    #removes the emote from the bins dict
    def rmv_emote(self, emote : str):
        self.bins.pop(emote)
        
    #returns the number of emotes currently being tracked
    def len(self):
        return len(self.bins)
    
    #increments the count of the specified emote by 1
    def incr_emote(self, emote : str):
        self.bins[emote] += 1
    
    #returns all values in bins
    def values(self):
        to_return = []
        for i in self.bins:
            to_return.append(self.bins[i])
        return to_return
        
    #writes all data collected to a txt file. Automatically titles and time stamps the txt file in the first line.
    def write_data_file(self, afile : str, starttime : float):
        file = open(afile, 'w')
        date = time.asctime(time.localtime(time.time()))
        file.write("Tracked data for " + str(int(time.time() - starttime)) + " seconds. " + "Date: " + str(date) + "\n")
        for i in self.bins:
            file.write(i + ' ' + str(self.bins[i]) + '\n')
        file.close()
        
    #overloaded print function for EmoteBins class
    def print(self):
        print(self.bins)
    
    #collects data for specified duration, contains twitch IRC protocol handlers   
    def track(self, start_time, end_time):    
        while(time.time() < end_time):
            to_recv = Connection.IRC_socket.recv(4096)
            message = to_recv.decode(encoding='utf-8').rstrip()
            if (message == 'PING tmi.twitch.tv'):
                #print("PING received, sending response PONG")
                to_send = ('PONG tmi.twitch.tv').encode(encoding='utf-8')
                Connection.IRC_socket.send(to_send)
            else:
                if(message != ""):
                    text = message.split(":")[-1]
                    words_list = text.split(" ")
                    for i in words_list:
                        if i in twitch_emotes:
                            self.incr_emote(i)

if __name__ == '__main__':
          
    twitch_emotes = ['4Head', 'ANELE', 'BabyRage', 'BibleThump', 'DatSheffy', 'FeelsBadMan', 'FailFish', 'HeyGuys', 'Kappa', 'PogChamp', 'WutFace', 'EleGiggle', 'MingLee', 'SMOrc']
    
    duration = 60 * 1
    end_loop = time.time() + duration #duration to run tracker, adjust minute factor to adjust duration
    start_time = end_loop - duration
    emote_tracker = EmoteBins()
    for i in twitch_emotes:
        emote_tracker.add_emote(i)
    
    #opens connection to chat in specified twitch channel
    Connection = IRCNetworkProtocol.IRC_Connect()
    Connection.ConnectChannel('nl_kripp')
     
    emote_tracker.track(start_time, end_loop)
    
    emote_tracker.print()
    emote_tracker.write_data_file('EmoteData', start_time)

