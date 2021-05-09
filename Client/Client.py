import socket
import json
from Signup import student_Sign_up as Sup
from Login import student_Log_in as Login
from ClassGUI import main as Cgui
#from SignUpGUIGVS11 import SignUpGUI as Sup



def Main():
    #connects to servers IP
    host = "localhost"
    #connect to servers PORT
    port = 12345
    
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    
    # make connection to server on host&port
    server.connect((host,port))
    
    #include what you are going to do with server
    ID = 0
    while True:
        
        message1 = input('Enter action: ')
       
        #closes the connecction
        if (message1 == "close"):
            if (ID == 0):
                print("Goodbye")
            else:
                print(f"Student: {ID} has exited...Goodbye")
                
            data_send = {}
            data_send['command'] = message1#send close command
            json_record = json.dumps(data_send)
            server.send(json_record.encode())
            break
        
        #sends command to server to sign up
        if (message1 == "sign up"):
            message2 = input('Role: ')
            
            #calls sign up class
            signup = Sup()
            signup.sign_up()
            signup_info = signup.getInfo()
            
            data_send = {}
            data_send['command'] = message1 
            data_send['role'] = message2
            data_send['info'] = signup_info
            json_record = json.dumps(data_send)
            server.send(json_record.encode())#sends all the information to the server
            
            #recieves the results of the check
            data = server.recv(2048)
            data = data.decode()
            data = json.loads(data)
            if(int(data) == 0):
                print("\n Record already exists")
            else:
                print("\n Record added successfully")
                
                ID = signup_info[0]
                
        #sends command to server to log in  
        if (message1 == "log in"):
            message2 = input('Role: ')
            
            #calls the login class
            role = message2
            data_send = {}
            veri = 0
            login = Login()
            while(veri != 1):
                
                
                login.Log_in()
                login_info = login.getInfo()
                
                
                
                
                data_send['command'] = message1
                data_send['role'] = role
                data_send['info'] = login_info
                json_record = json.dumps(data_send)
                server.send(json_record.encode())#sends all the information to the server
                
                data = server.recv(2048)
                data = data.decode()
                data = json.loads(data)
    
                #recives the results 
                veri = data['verification']
                if(veri == '0'):
                    print("\nRecord doesn't exist, go signup")
                if(veri == '10'):
                    print("\nPassword incorrect, try again")
                if(veri == '1' and role == 'student'):
                    ID = data['ID']#if role is teacher it says "welcome teacher" 
                    print(f"\nWelcome student: {ID}")
                    veri = int(veri)
                if(veri == '1' and role == 'teacher'):
                    ID = data['ID']
                    print(f"\nWelcome teacher: {ID}")
                    veri = int(veri)

            
           #if role is student gets it in a while loop to display class until they type exit  
           #if role is teacher they get stuck in a different while loop 
           #while(true):
            classgui = Cgui()
            classgui.gui(data['Classes'])
            selected_class = classgui.getInfo()#if this == exit close the while loop and kick to the login screen
            data_send={}                            #for now the only class available is CSCI 4345
            data_send['command'] = 'check grades'#different command for teacher's loop
            data_send['class']=selected_class
            data_send['student'] = ID
            data_send['role'] = role
            json_record = json.dumps(data_send)
            server.send(json_record.encode())
            
                #since this is meant to be a simple UI this command can only be done after a sign up/log in command
         #sends command to check grades 
               
        # if (message1 == "check grades"):
        #     message2 = input("Enter the class: ") # how a student chooses his class will be different in the end
        #     data_send={}                            #for now the only class available is CSCI 4345
        #     data_send['command'] = message1
        #     data_send['class']=message2
        #     data_send['student'] = ID
        #     json_record = json.dumps(data_send)
        #     server.send(json_record.encode())
            
            #recieves the grades and i print them
            data = server.recv(2048)
            data = data.decode()
            data = json.loads(data)
            
            if(role == "teacher"):
                print(data)
                
            if(role == "student"):
                
                grades = data['Grades']
                assignments = data['Assignments']
            
                for i in range(len(grades)):
                    print(assignments[i],"- ",grades[i])
            
        
        
        
            
        
        
       
          
        #close connection to server
    server.close()
if __name__ == '__main__': 
    Main()         
                                   