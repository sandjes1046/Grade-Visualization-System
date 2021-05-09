#import the socket programming library
import socket
#figure out if locking is neccessary
#import all thread modules
from _thread import *
import threading
import pandas as pd
import csv
import json
from pathlib import Path
import math

#locks are to make sure the thread doesnt get used by something else
print_lock = threading.Lock() 

def check_student_records_withID(ID):
        check = 1

        st_id = int(ID)
        student_check_df = pd.read_csv('Student_Info/Student_Login_Info.csv', index_col="ID")
        #throws an error, a 0,  if it does not exits
        try:student_check_df.loc[st_id]
        except: 
            check = 0
        return check
    
def check_student_records_withEmail(Email):
        check = 1

        st_mail = Email
        student_check_df = pd.read_csv('Student_Info/Student_Login_Info.csv', index_col="Email")
        #throws an error, a 0,  if it does not exits
        try:student_check_df.loc[st_mail]
        except: 
            check = 0
        return check
      
def check_student_password(Email, passwd):
        check = 0
        st_mail = Email
        student_check_df = pd.read_csv('Student_Info/Student_Login_Info.csv', index_col="Email")
        student_info = student_check_df.loc[st_mail]
        student_info_dict = student_info.to_dict()
        if (passwd != student_info_dict['Password']):
            #passw wrong
            return check
        else:
            check = 1
            return check
#########################################################################

def check_teacher_records_withID(ID):
        check = 1

        st_id = int(ID)
        student_check_df = pd.read_csv('Teacher_Info/Teacher_Login_Info.csv', index_col="ID")
        #throws an error, a 0,  if it does not exits
        try:student_check_df.loc[st_id]
        except: 
            check = 0
        return check   
        
def check_teacher_records_withEmail(Email):
        check = 1

        st_mail = Email
        student_check_df = pd.read_csv('Teacher_Info/Teacher_Login_Info.csv', index_col="Email")
        #throws an error, a 0,  if it does not exits
        try:student_check_df.loc[st_mail]
        except: 
            check = 0
        return check

def check_teacher_password(Email, passwd):
        check = 0
        st_mail = Email
        student_check_df = pd.read_csv('Teacher_Info/Teacher_Login_Info.csv', index_col="Email")
        student_info = student_check_df.loc[st_mail]
        student_info_dict = student_info.to_dict()
        if (passwd != student_info_dict['Password']):
            #passw wrong
            return check
        else:
            check = 1
            return check
def grade_range(num):
    if(90 <= num <= 100):
        return 'A'
    elif(80 <= num <= 89):
        return 'B'
    elif(70 <= num <= 79):
        return 'C'
    elif(60 <= num <= 69):
        return 'D'
    else:
        return 'F'
      
#function for thread
def threaded(c,con_num):
    
    
    #runs as long as the client sends something to the server
    while True:
        
        
        
        #data recieved from the client
        data = c.recv(4096)
        data = data.decode()
        data = json.loads(data)
        
        #closes the connection
        if (data['command'] == "close"):
            
            print(f"Connection: {con_num} has exited....BYE")
            break
###############################################################################   SIGN UP    
        #if it recieves the sign up command it checks to see if you exist, if you dont it adds the record    
        if (data['command'] == "sign up"):
            
            
            if (data['role'] == "student"):
                
                signup_info = data['info']
                if(check_student_records_withID(signup_info[0]) == 0):
                    with open('Student_Info/Student_Login_Info.csv', 'a', newline = '') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow(signup_info)
                    signindata_send = '1'
                    c.send(signindata_send.encode())
                else:
                    signindata_send = '0'
                    c.send(signindata_send.encode())
                    
            if (data['role'] == "teacher"):
                signup_info = data['info']
                if(check_teacher_records_withID(signup_info[0]) == 0):
                    with open('Teacher_Info/Teacher_Login_Info.csv', 'a', newline = '') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow(signup_info)
                    signindata_send = '1'
                    c.send(signindata_send.encode())
                else:
                    signindata_send = '0'
                    c.send(signindata_send.encode())
                
 ############################################################################## LOGIN   
        #if it recieves the log in command it will check if you exist if you dont, you have to go sign up 
        
        if (data["command"] == "log in"):
            
        
            if (data['role'] == "student"):
                
                login_info = data['info']
                if(check_student_records_withEmail(login_info[0]) == 0):
                    
                    #record doesn't exist
                    data_send = {}
                    data_send['verification'] = '0'
                    json_record = json.dumps(data_send)
                    c.send(json_record.encode())
                else:
                   
                    #record exists will verify the password
                    if(check_student_password(login_info[0],login_info[1]) == 0):
                        # password wrong
                        data_send = {}
                        data_send['verification'] = '10'
                        json_record = json.dumps(data_send)
                        c.send(json_record.encode())
                    else: 
                        #all was successful it logs you in
                        student_df = pd.read_csv('Student_Info/Student_Login_Info.csv', index_col="Email")
                        student_info = student_df.loc[login_info[0]]
                        student_dict = student_info.to_dict()
                        data_send ={}
                        data_send['verification'] = '1'
                        data_send['ID'] = str(student_dict['ID'])
                        ID = student_dict['ID']
                        try:
                          
                            with open(f'Student_Info/{ID}.txt', 'r') as Student_file:
                                for line in Student_file:
                                    currentline = line.split(',')
                            data_send['Classes'] = currentline
                            data_send['Status'] = 'success'
                        except:
                            data_send["Status"] = 'error'
                        json_record = json.dumps(data_send)
                        c.send(json_record.encode())
                    
            if (data['role'] == "teacher"):
                
                login_info = data['info']
                if(check_teacher_records_withEmail(login_info[0]) == 0):
                    
                    #record doesn't exist
                    data_send = {}
                    data_send['verification'] = '0'
                    json_record = json.dumps(data_send)
                    c.send(json_record.encode())
                else:
                   
                    #record exists will verify the password
                    if(check_teacher_password(login_info[0],login_info[1]) == 0):
                        # password wrong
                        data_send = {}
                        data_send['verification'] = '10'
                        json_record = json.dumps(data_send)
                        c.send(json_record.encode())
                    else: 
                        #all was successful it logs you in
                        student_df = pd.read_csv('Teacher_Info/Teacher_Login_Info.csv', index_col="Email")
                        student_info = student_df.loc[login_info[0]]
                        student_dict = student_info.to_dict()
                        data_send ={}
                        data_send['verification'] = '1'
                        data_send['ID'] = str(student_dict['ID'])
                        ID = student_dict['ID']
                        try:
                          
                            with open(f'Teacher_Info/{ID}.txt', 'r') as Student_file:
                                for line in Student_file:
                                    currentline = line.split(',')
                            data_send['Classes'] = currentline
                            data_send['Status'] = 'success'
                        except:
                            data_send["Status"] = 'error'
                        json_record = json.dumps(data_send)
                        c.send(json_record.encode())
                       
###############################################################################
        
        
                       # in the final project to make it to this point students must have signed in or logged in
                       #in the final version it will display the students classes based on what is in there sheet
                       #add command options to exit
 ######################################################################################################################                      
        if(data["command"] == "check grades" and data["role"] == "student"):
            gradebook = data['class'] + ".csv"
            student = int(data['student'])
            grades_check_df = pd.read_csv(f'Classes/{gradebook}', index_col="ID")
            mygrades = grades_check_df.loc[student]
            mygrades_dict = mygrades.to_dict()
            
            data_grades = {}
            
            grades_list = list(mygrades_dict.values())
            assignment_list = list(mygrades_dict.keys())
            grades_list.remove(mygrades_dict['Name'])
            assignment_list.remove('Name')
            data_grades['Assignments'] = assignment_list
            grades = []
            for i in range(len(grades_list)):
                grades.append(grades_list[i].item())
            
            data_grades['Grades'] = grades
            
            avg_check_df = grades_check_df = pd.read_csv(f'Classes/{gradebook}')
            avg_check_dict = avg_check_df.to_dict()
            raw_vals = list(avg_check_dict.values())
            del raw_vals[0]
            del raw_vals[0]
            
            avg = []
            for i in range(len(raw_vals)):
                sums = 0
                for j in range(len(raw_vals[i])):
                    sums += raw_vals[i][j]
                avg.append(sums/len(raw_vals[i]))
                
            data_grades['Averages'] = avg
            
            json_record = json.dumps(data_grades)
            c.send(json_record.encode())
            
        
#################################################################################################     
        if(data["command"] == 'check average' and data["role"] == "student"):
            
            gradebook = data['class'] + ".csv"
            student = int(data['student'])
            grades_check_df = pd.read_csv(f'Classes/{gradebook}', index_col="ID")
            mygrades = grades_check_df.loc[student]
            mygrades_dict = mygrades.to_dict()
            
            data_grades = {}
            
            grades_list = list(mygrades_dict.values())
            assignment_list = list(mygrades_dict.keys())
            grades_list.remove(mygrades_dict['Name'])
            assignment_list.remove('Name')
            data_grades['Assignments'] = assignment_list
            grades = []
            for i in range(len(grades_list)):
                grades.append(grades_list[i].item())
            
            data_grades['Grades'] = grades
            
            
            with open(f'Classes/{data["class"]}.txt', 'r') as class_file:#Assign,Quiz,Test
                for line in class_file:
                    currentline = line.split(',')
            del currentline[0]#delete the teacher
        
            data_grades['Percentages'] = currentline
            
            json_record = json.dumps(data_grades)
            c.send(json_record.encode())
            
            
            
        if(data["command"] == 'set percent' and data["role"] == "teacher"):
            newfile = []
            new_percents = []
            with open(f'Classes/{data["class"]}.txt', 'r') as class_file:#Assign,Quiz,Test
                for line in class_file:
                    currentline = line.split(',')
            newfile.append(currentline[0])#move teacher
            new_percents = data['Percentages']
            for i in range(len(new_percents)):
                newfile.append(new_percents[i])
            
            with open(f'Classes/{data["class"]}.txt', 'w') as class_file:
                class_file.write(newfile[0])
                del newfile[0]
                for i in range(len(newfile)):
                    class_file.write(f",{newfile[i]}")
            data_send = {}
            data_send['result'] = 'good'
            
            json_record = json.dumps(data_send)
            c.send(json_record.encode())
######################################################################################            
            
        if(data["command"] == 'stats' and data["role"] == "student"):
            max_A=[]
            min_A=[]
            mean=[]
            count = []
            df = pd.read_csv(f'Classes/{data["Class"]}.csv')
            class_dict = df.to_dict()
            assign = list(class_dict.keys())
            vals = list(class_dict.values())
            del assign[0]
            del assign[0]
            del vals[0]
            del vals[0]
            
            for i in range(len(assign)):
              mean.append(math.ceil(df[assign[i]].describe()['mean']))
            for i in range(len(assign)):
              min_A.append(df[assign[i]].describe()['min'])
            for i in range(len(assign)):
              max_A.append(df[assign[i]].describe()['max'])
            for i in range(len(assign)):
                count.append(df[assign[i]].describe()['count'])
            data_send = {}
            data_send["min"] = min_A
            data_send["max"] = max_A
            data_send["mean"] = mean
            data_send["count"] = count
            data_send["assignments"] = assign
            
            json_record = json.dumps(data_send)
            c.send(json_record.encode())
            
        if(data["command"] == 'stats' and data["role"] == "teacher"):
            max_A=[]
            min_A=[]
            mean=[]
            count = []
            df = pd.read_csv(f'Classes/{data["Class"]}.csv')
            class_dict = df.to_dict()
            assign = list(class_dict.keys())
            vals = list(class_dict.values())
            del assign[0]
            del assign[0]
            del vals[0]
            del vals[0]
            
            for i in range(len(assign)):
              mean.append(math.ceil(df[assign[i]].describe()['mean']))
            for i in range(len(assign)):
              min_A.append(df[assign[i]].describe()['min'])
            for i in range(len(assign)):
              max_A.append(df[assign[i]].describe()['max'])
            for i in range(len(assign)):
              count.append(df[assign[i]].describe()['count'])
              
            grades = [0,0,0,0,0]
            count_grades = []
            for j in range(len(assign)):
                for i in range(len(vals[j])):
                    grade = grade_range(vals[j][i])
                    if(grade == 'A'):
                        grades[0]+=1
                    elif(grade == 'B'):
                        grades[1]+=1
                    elif(grade == 'C'):
                        grades[2]+=1
                    elif(grade == 'D'):
                        grades[3]+=1
                    else:    
                         grades[4]+=1

                count_grades.append(grades)
                grades = [0,0,0,0,0]
                  
            data_send = {}
            data_send["min"] = min_A
            data_send["max"] = max_A
            data_send["mean"] = mean
            data_send["count"] = count
            data_send["assignments"] = assign
            data_send["grade range"] = count_grades
            
            json_record = json.dumps(data_send)
            c.send(json_record.encode())
        
            
        if(data["command"] == "edit grades" and data["role"] == "teacher"):  
            
            df = pd.read_csv(f'Classes/{data["Class"]}.csv')
            class_dict = df.to_dict()
            
            data_send = {}
            
            headers = list(class_dict.keys())
            grades = list(class_dict.values())
            
            data_send["headers"] = headers
            data_send["grades"] = grades
            
            json_record = json.dumps(data_send)
            c.send(json_record.encode())
            
        if(data["command"] == 'save' and data["role"] == "teacher"):  
            new_class_grades = data['save dict']
            new_headers = list(new_class_grades.keys())
            new_grades = list(new_class_grades.values())
            row_grades = []
            with open(f"Classes\{data['class']}.csv", 'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(new_headers)
                for i in range (len(new_grades[0])):
                    for j in range(len(new_grades)):
                        row_grades.append(new_grades[j][i])
                        
                    writer.writerow(row_grades)
                    row_grades = []
                    
    #close the connection
    c.close()
    
def Main():
    #this is the ip address of the server
    #to run on same computer use localhost or ""
    #to run in same network use 0.0.0.0 and to run across network google my network IP and use that one
    host = ""
    
    
    # port can be anything 
    
    port = 12345 #to run on networks use a port allowed by router
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the address of the server
    s.bind((host, port)) 
    print("server binded to port: ",port)
    con_num = 0
   
    
    # a forever loop until client wants to exit
    while True:
        
        #listen for connections
        #server.listen(max number of queued connections)
        s.listen(1)
        print("server is waiting for a connection...")
    
        
        #connect with client
        c, addr = s.accept()
        con_num += 1
        try:
            
            # lock acquired by client
            #client's thread
            #print_lock.acquire()
            print('Connected to: ', addr[0], ':', addr[1])
            print(f'{con_num}')
            #start a new thread and return identifier
            start_new_thread(threaded, (c,con_num,))
                             
        except:
            print('Server Error...')
    #for actual server it should close here
    s.close()
    
#run the main
if __name__ == '__main__': 
    Main() 

