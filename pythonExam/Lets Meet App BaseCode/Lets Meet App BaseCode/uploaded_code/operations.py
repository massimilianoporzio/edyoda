import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    '''Create an Event with the details entered by organizer'''
    #org is the Full Name of the organizer

    f=open(events_json_file,'r+')
    event = {
        "ID" : Event_ID,
        "Name":Event_Name,
        "Organizer": org,
        "Start Date": Start_Date,
        "Start Time": Start_Time,
        "End Date": End_Date,
        "End Time": End_Time,
        "Users Registered":Users_Registered,
        "Capacity":Capacity,
        "Seats Available":Availability
    }
    try:
        content=json.load(f)
        content.append(event)
        f.seek(0)
        f.truncate()
        json.dump(content,f)
    except JSONDecodeError:
        print("\u26D4 - Something went wrong")
        l=[]
        l.append(event)
        json.dump(l,f)
    f.close()

    

def View_Events(org,events_json_file):
    '''Return a list of all events created by the logged in organizer'''
    result = []
    
    try:
        f=open(events_json_file,'r+')
        content=json.load(f)
        
                
    except JSONDecodeError:
        f.close()
    for i in range(len(content)):
            if(content[i]["Organizer"]==org):
               result.append(content[i])
              
    return result

    

def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    try:
        f=open(events_json_file,'r+')
        content=json.load(f)
        
                
    except JSONDecodeError:
        f.close()
    result = []
    for i in range(len(content)):
        if(content[i]["ID"]==Event_ID):
            result.append( content[i] )
    return result
    

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    ##
    try:
        if(detail_to_be_updated  in ["Name" , "Start Date" , "Start Time" , "End Time" , "End Date"]):
            data_to_update = View_all_events(events_json_file)
            event_to_update = next((x for x in data_to_update if x['ID'] == event_id), None)
            #NOT SURE IF AN ORGANIZER CAN UPDATE if organized by other organized
            if event_to_update["Organizer"]!=org:
                return False
            index_of_event_to_update = data_to_update.index(event_to_update)
            event_to_update[detail_to_be_updated]=updated_detail
            data_to_update[index_of_event_to_update]=event_to_update
            f=open(events_json_file,'r+')
            f.seek(0)
            f.truncate()
            json.dump(data_to_update,f)
            
            return True
    except:
        return False
    return False
    

def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    try:
        data_to_update = View_all_events(events_json_file)
        event_to_delete = next((x for x in data_to_update if x['ID'] == event_ID), None)
        if event_to_delete["Organizer"]!=org:
                return False
        index_of_user_to_delete = data_to_update.index(event_to_delete)
        data_to_update.pop(index_of_user_to_delete)
        f=open(events_json_file,'r+')
        f.seek(0)
        f.truncate()
        json.dump(data_to_update,f)
        return True

    except:
        return False
    


def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    try:
        data_to_update = View_all_events(events_json_file)
        event_to_register_for = next((x for x in data_to_update if x['ID'] == event_id), None)
        #create datetime based on event Start Date and Start Time
        start_datetime_str = event_to_register_for["Start Date"]+" "+event_to_register_for["Start Time"]
        start_datetime = datetime.strptime(start_datetime_str,"%Y-%m-%d %H:%M:%S")
        end_datetime_str = event_to_register_for["End Date"]+" "+event_to_register_for["End Time"]
        end_datetime = datetime.strptime(end_datetime_str,"%Y-%m-%d %H:%M:%S")
        if end_datetime < now:
            print("Please notice: the event is ended")
        if event_to_register_for["Seats Available"]==0:
            return False
        index_of_event = data_to_update.index(event_to_register_for)
        users_already_registered = event_to_register_for["Users Registered"]
        if Full_Name in users_already_registered:
            print("Please notice: you are already registered")
            return True
        else:
            updated_users_registered = [user for user in users_already_registered]
            updated_users_registered.append(Full_Name)
            event_to_register_for["Users Registered"] = updated_users_registered
            event_to_register_for["Seats Available"] = event_to_register_for["Seats Available"] -1
            data_to_update[index_of_event]=event_to_register_for
            try:

                f=open(events_json_file,'r+')
                f.seek(0)
                f.truncate()
                json.dump(data_to_update,f)
                return True
            except:
                f.close()
                return False
    except:
        return False

       

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    try:
       data_to_update = View_all_events(events_json_file)
       for event in data_to_update:
            start_datetime_str = event["Start Date"]+" "+event["Start Time"]
            start_datetime = datetime.strptime(start_datetime_str,"%Y-%m-%d %H:%M:%S")
            end_datetime_str = event["End Date"]+" "+event["End Time"]
            end_datetime = datetime.strptime(end_datetime_str,"%Y-%m-%d %H:%M:%S")
            if( (start_datetime<now and end_datetime>now) or (start_datetime>now)):
                upcoming_ongoing.append(event)
            
       
       
       print(upcoming_ongoing)
       print("ciao")
    except:
        print("something went wrong")
        return



    

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    try:
        f = open(members_json_file,'r+')
        users=json.load(f)
        user_to_update = next((x for x in users if x['Full Name'] == Full_Name), None)
        index_of_user_to_update = users.index(user_to_update)
        user_to_update['Password']=new_password
        users[index_of_user_to_update]=user_to_update
        f.seek(0)
        f.truncate()
        json.dump(users,f)
        return True
    except:
        f.close()
        return False

def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
