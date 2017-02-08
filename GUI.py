'''
Created on Sep 6, 2015
Updated on December 21, 2015

@author: Hanna Alam
'''
import tkinter
import IRCNetworkProtocol


#updates the tkinter frame with new messages
def repeater(root):
    try:  
        parsed = ChatHandler()
        if parsed == "NO MESSAGE":
            root.after(10,repeater,root)
        else:
            ChatLog.configure(state="normal")
            ChatLog.insert("end",parsed)
            message = parsed.split(":")
            if(nickname.lower() in message[1].lower()):
                EgoLog.configure(state="normal")
                EgoLog.insert("end",parsed)
                EgoLog.configure(state="disabled")
            if(ScrollBar.get()[1] == 0.0):
                ChatLog.see(tkinter.END)
            elif (ScrollBar.get()[1] == 1.0):
                ChatLog.see(tkinter.END)
            ChatLog.configure(state="disabled")
            root.after(10,repeater,root)
    except tkinter.TclError:
        print("Message contained character above the range allowed by Tcl. Message not displayed.")
        root.after(10,repeater,root)
        
    
#grabs chat messages from socket and handles IRC protocol requests
def ChatHandler():
    to_recv = Connection.IRC_socket.recv(4096)
    message = to_recv.decode(encoding='utf-8').rstrip()
    if (message == 'PING tmi.twitch.tv'):
        print("PING received, sending response PONG")
        to_send = ('PONG tmi.twitch.tv').encode(encoding='utf-8')
        Connection.IRC_socket.send(to_send)
    else:
        if(message != ""):
            user = message.split("!")[0].strip(":")
            text = message.split(":")[-1]
            return (user + ": " + text + "\n")
        else:
            return "NO MESSAGE"
        
    #helper funcs for sending messages to chat
# def ChatSend(to_send : str, channel : str):
#     to_send = ("PRIVMSG #" + channel + " :" + to_send).encode(encoding='utf-8')
#     Connection.IRC_socket.send(to_send)
#     print("worked")
#     SendMsgBox.delete(tkinter.FIRST, tkinter.LAST)
#     
# def EventHandler(event):
#     ChatSend(SendMsgBox.get(), channel_name)
 
    
if __name__ == '__main__':
    #prompt for user input to sign on
    nickname = input("Enter your twitch nickname: ")
    channel_name = input("Enter channel name to join: ")
    
    
    #root window
    root = tkinter.Tk()
    root.title("SolBot 1.0")
     
    frame = tkinter.Frame(root, width=1200, height=700)
    frame.pack(fill="both", expand=True)
    frame.grid_propagate(True)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
     
    ChatLog = tkinter.Text(frame, borderwidth=3, relief="sunken")
    ChatLog.config(font=("consolas", 12), undo=True, wrap='word', state="disabled")
    ChatLog.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
         
    ScrollBar = tkinter.Scrollbar(frame, command=ChatLog.yview)
    ScrollBar.grid(row=0, column=1, sticky='nsew')
    ChatLog['yscrollcommand'] = ScrollBar.set
    
    
    EgoLog = tkinter.Text(frame, borderwidth=3, relief="sunken")
    EgoLog.config(font=("consolas", 12), undo=True, wrap='word', state="disabled")
    EgoLog.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
    EgoLog.config(state="normal")
    EgoLog.insert("end", "Welcome to Ego Filter! All messages that contain your twitch nickname will be displayed here." + "\r\n")
    EgoLog.config(state="disabled")
    
    
    

     
     
    Connection = IRCNetworkProtocol.IRC_Connect()
    Connection.ConnectChannel(channel_name.lower())
    
#     SendMsgBox = tkinter.Entry(frame)
#     SendMsgBox.grid(row=1, column=0, sticky="nsew")
#     SendMsgBox.bind('<Enter>', EventHandler)
    
     
    repeater(root)
    root.mainloop()
    
