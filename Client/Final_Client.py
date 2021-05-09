import socket
import json
#from Signup import student_Sign_up as Sup
from LoginGUI1 import loginGUI as Log
from SignUpGUIGVS11 import SignUpGUI as Sup
from ErrorGUI import Error as er
from MainGUI import Mainpage as mp
from Graph import Graph as gph
from OptionsGUI import Options as op
from CheckAverageGUI import Check_Average as cg
from SetPercent import Set_Percent as sp
from StatsGUI import Graph_It as sts
from Student_StatsGUI import Table as tb
from ExcelGUI import Excel as ex


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
    loop_flag = True
    role = ""

    while True:
        veri = " "
        login = Log()
        info = login.get_info()
        if(info[0] == "exit GVS"):
            data_send = {}
            data_send['command'] = "close" #send close command
            json_record = json.dumps(data_send)
            server.send(json_record.encode())
            break #close connection
        if(info[0] == "sign up"):
            signup = Sup()
            signup_info = signup.get_info()
            if(signup_info[0] == "back to login"):
                print("go back to login")
            if(signup_info[0] == "sign up"):
                data_send = {}
                data_send['command'] = signup_info[0]
                data_send['role'] = signup_info[1]
                del signup_info[0]
                del signup_info[0]
                data_send['info'] = signup_info
                
                json_record = json.dumps(data_send)
                server.send(json_record.encode())#sends all the information to the server
                
                #recieves the results of the check
                signindata = server.recv(2048)
                signindata = signindata.decode()

                if(int(signindata) == 0):
                    flag = 0
                    er(flag)
                else:
                    flag = 1
                    er(flag)
                    
                    
        if(info[0] == "log in"):
            data_send = {}
            data_send['command'] = info[0]
            data_send['role'] = info[1]
            role = info[1]
            del info[0]
            del info[0]
            data_send['info'] = info
            json_record = json.dumps(data_send)
            server.send(json_record.encode())#sends all the information to the server
            
            data = server.recv(2048)
            data = data.decode()
            data = json.loads(data) #if it accepts it sends a dictionary eith key = Classes with list of classes
            veri = data["verification"]
            if(veri == '0'):
                flag = 2
                er(flag)
               
            if(veri == '10'):
                flag = 3
                er(flag)
                
            if(veri == '1' and role == 'student'):
                ID = data['ID']#if role is teacher it says "welcome teacher" 
                print(f"\nWelcome student: {ID}")
                veri = int(veri)
                status = data["Status"]
                classes = data["Classes"]
            if(veri == '1' and role == 'teacher'):
                ID = data['ID']
                print(f"\nWelcome teacher: {ID}")
                veri = int(veri)
                status = data["Status"]
                classes = data["Classes"]
            
  ############################################################ REAL PROGRAM STARTS              
        if(veri == 1 and role == "student"):
            while(loop_flag):
                
                if(status == 'success'):
                    mainpage = mp(classes)
                    selected = mainpage.get_info()
                    if(selected == 'log out'):
                        break
                    else:
                        while(loop_flag):
                            
                            options = op(role)
                            info = options.get_info()
                            if(info == "go back"):
                                break
                            if(info == "check grades"):
                                data_send = {}
                                data_send['class'] = selected
                                data_send['command'] = info
                                data_send['student'] = ID
                                data_send['role'] = role
                                
                                json_record = json.dumps(data_send)
                                server.send(json_record.encode())
                                
                                data = server.recv(2048)
                                data = data.decode()
                                data = json.loads(data)
                                
                                grades = gph(data['Averages'],data['Grades'],data['Assignments'])
                                continue
                            
                            if(info == "check average"):
                                data_send = {}
                                data_send['class'] = selected
                                data_send['command'] = info
                                data_send['student'] = ID
                                data_send['role'] = role
                                
                                json_record = json.dumps(data_send)
                                server.send(json_record.encode())
                                
                                data = server.recv(2048)
                                data = data.decode()
                                data = json.loads(data)
                                
                                current_grade = cg(data['Percentages'],data['Grades'],data['Assignments'])
                                continue
                            if(info == "stats"):
                                data_send= {}
                                data_send['Class'] = selected
                                data_send['command'] = info
                                data_send['role'] = role
                                
                                json_record = json.dumps(data_send)
                                server.send(json_record.encode())
                                
                                data = server.recv(2048)
                                data = data.decode()
                                data = json.loads(data)
                                
                                table = tb(selected, data["mean"],data["min"],data["max"],data["count"]
                                           ,data["assignments"])
                                continue
                                #clas,mean,mins,maxs,counts,assign

                            
                else:
                    er(4)
                    mainpage = mp(['No Class'])
                    if(selected == 'log out'):
                        break
                    
                    
                    
                    
                    
                    
        if(veri == 1 and role == "teacher"):
            while(loop_flag):
                print("GOOD JOB GUYS")
                if(status == 'success'):
                    mainpage = mp(classes)
                    selected = mainpage.get_info()
                    if(selected == 'log out'):
                        break
                    else:
                        while(loop_flag):
                            options = op(role)
                            info = options.get_info()
                            if(info == "go back"):
                                break
                            if(info == "set percent"):
                                data_send = {}
                                data_send['class'] = selected
                                data_send['command'] = info
                                data_send['role'] = role
                                set_per = sp()
                                percentages = set_per.get_info()
                                if(percentages[0] == 0):
                                    continue
                                data_send['Percentages'] = percentages
                                
                                json_record = json.dumps(data_send)
                                server.send(json_record.encode())
                                
                                data = server.recv(2048)
                                data = data.decode()
                                data = json.loads(data)
                                
                                if (data['result'] == 'good'):
                                    er(5)
                                
                                continue
                            if(info == "stats"):
                                data_send= {}
                                data_send['Class'] = selected
                                data_send['command'] = info
                                data_send['role'] = role
                                
                                json_record = json.dumps(data_send)
                                server.send(json_record.encode())
                                
                                data = server.recv(2048)
                                data = data.decode()
                                data = json.loads(data)
                                
                                stats = sts(selected,data["mean"],data["min"],
                                            data["max"],data["count"],data["grade range"],data["assignments"])
                                continue
                                #role,clas,mean,mins,maxs,counts,grds_rg,assign
                                
                            if(info == "edit grades"):
                                data_send= {}
                                data_send['Class'] = selected
                                data_send['command'] = info
                                data_send['role'] = role
                                
                                json_record = json.dumps(data_send)
                                server.send(json_record.encode())
                                
                                data = server.recv(4096)
                                data = data.decode()
                                data = json.loads(data)
                                
                                
                                #list of the headers and list of lists of values
                                excel = ex(data["headers"],data["grades"])
                                to_save = excel.get_info()
                                
                                data_send= {}
                                data_send['class'] = selected
                                data_send['command'] = 'save'
                                data_send['role'] = role
                                data_send['save dict'] = to_save
                                
                                json_record = json.dumps(data_send)
                                server.send(json_record.encode())
                                
                                #get info and send to server to save with diff command
                                continue
                                
                                
                else:
                    er(4)
                    mainpage = mp(['No Class'])
                    if(selected == 'log out'):
                        break
        

##########################################################################################
        # #closes the connecction
        # if (message1 == "close"):
        #     if (ID == 0):
        #         print("Goodbye")
        #     else:
        #         print(f"Student: {ID} has exited...Goodbye")
                
        #     data_send = {}
        #     data_send['command'] = message1#send close command
        #     json_record = json.dumps(data_send)
        #     server.send(json_record.encode())
        #     break
        
        # #sends command to server to sign up
        # if (message1 == "sign up"):
            
            
        #     #calls sign up class
        #     signup = Sup()
        #     signup_info = signup.get_info()
            
        #     data_send = {}
        #     data_send['command'] = message1 
        #     data_send['role'] = signup_info[0]
        #     role = signup_info[0]
        #     del signup_info[0]
        #     data_send['info'] = signup_info
        #     json_record = json.dumps(data_send)
        #     server.send(json_record.encode())#sends all the information to the server
            
        #     #recieves the results of the check
        #     data = server.recv(2048)
        #     data = data.decode()
        #     data = json.loads(data)
        #     if(int(data) == 0):
        #         print("\n Record already exists")
        #     else:
        #         print("\n Record added successfully")
                
        #         ID = signup_info[1]
                
        # #sends command to server to log in  
        # if (message1 == "log in"):
        #     message2 = input('Role: ')
            
        #     #calls the login class
        #     role = message2
        #     data_send = {}
        #     veri = 0
        #     login = Login()
        #     while(veri != 1):
                
                
        #         login.Log_in()
        #         login_info = login.getInfo()
                
                
                
                
        #         data_send['command'] = message1
        #         data_send['role'] = role
        #         data_send['info'] = login_info
        #         json_record = json.dumps(data_send)
        #         server.send(json_record.encode())#sends all the information to the server
                
        #         data = server.recv(2048)
        #         data = data.decode()
        #         data = json.loads(data)
    
        #         #recives the results 
        #         veri = data['verification']
        #         if(veri == '0'):
        #             print("\nRecord doesn't exist, go signup")
        #         if(veri == '10'):
        #             print("\nPassword incorrect, try again")
        #         if(veri == '1' and role == 'student'):
        #             ID = data['ID']#if role is teacher it says "welcome teacher" 
        #             print(f"\nWelcome student: {ID}")
        #             veri = int(veri)
        #         if(veri == '1' and role == 'teacher'):
        #             ID = data['ID']
        #             print(f"\nWelcome teacher: {ID}")
        #             veri = int(veri)

            
        #    #if role is student gets it in a while loop to display class until they type exit  
        #    #if role is teacher they get stuck in a different while loop 
        #    #while(true):
        #     classgui = Cgui()
        #     classgui.gui(data['Classes'])
        #     selected_class = classgui.getInfo()#if this == exit close the while loop and kick to the login screen
        #     data_send={}                            #for now the only class available is CSCI 4345
        #     data_send['command'] = 'check grades'#different command for teacher's loop
        #     data_send['class']=selected_class
        #     data_send['student'] = ID
        #     data_send['role'] = role
        #     json_record = json.dumps(data_send)
        #     server.send(json_record.encode())
            
        #         #since this is meant to be a simple UI this command can only be done after a sign up/log in command
        #  #sends command to check grades 
               
        # # if (message1 == "check grades"):
        # #     message2 = input("Enter the class: ") # how a student chooses his class will be different in the end
        # #     data_send={}                            #for now the only class available is CSCI 4345
        # #     data_send['command'] = message1
        # #     data_send['class']=message2
        # #     data_send['student'] = ID
        # #     json_record = json.dumps(data_send)
        # #     server.send(json_record.encode())
            
        #     #recieves the grades and i print them
        #     data = server.recv(2048)
        #     data = data.decode()
        #     data = json.loads(data)
            
        #     if(role == "teacher"):
        #         print(data)
                
        #     if(role == "student"):
                
        #         grades = data['Grades']
        #         assignments = data['Assignments']
            
        #         for i in range(len(grades)):
        #             print(assignments[i],"- ",grades[i])
            
        
        
        
            
        
        
       
          
        #close connection to server
    server.close()
if __name__ == '__main__': 
    Main()         
                                   