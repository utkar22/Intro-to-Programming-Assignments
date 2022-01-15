# Assignment - 2
# Name - 
# Roll No - 

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
    '''
    **** DO NOT modify this function ****
    Description: Reads the data.json file, and converts it into a dictionary.

    Parameters: 
    - file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

    Returns:
    - A dictionary containing the data read from the file
    '''
    
    with open(file_path, 'r') as data:
        records = json.load(data)

    return records


def filter_by_first_name(records, first_name):
    '''
    Description: Searches the records to find all persons with the given first name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - first_name (STRING): The first name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given first name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    first_name=first_name.lower()
    
    list_of_ids=[]

    for a in records:
        if a["first_name"].lower()==first_name:
            list_of_ids.append(a["id"])

    return (list_of_ids)
                


def filter_by_last_name(records, last_name):
    '''
    Description: Searches the records to find all persons with the given last name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - last_name (STRING): The last name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given last name
            Case 1: No person found => Returns an empty list
            Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    last_name=last_name.lower()
    
    list_of_ids=[]

    for a in records:
        if a["last_name"].lower()==last_name:
            list_of_ids.append(a["id"])

    return (list_of_ids)


def filter_by_full_name(records, full_name):
    '''
    Description: Searches the records to find all persons with the given full name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
            Case 1: No person found => Returns an empty list
            Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    full_name=full_name.lower()
    
    list_of_ids=[]

    for a in records:
        if a["first_name"].lower()+" "+a["last_name"].lower()==full_name:
            list_of_ids.append(a["id"])

    return (list_of_ids)


def filter_by_age_range(records, min_age, max_age):
    '''
    Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - min_age (INTEGER): The minimum age (inclusive)
    - max_age (INTEGER): The maximum age (inclusive)

    Note: 0 < min_age <= max_age

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
            Case 1: No person found => Returns an empty list
            Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    list_of_ids=[]

    for a in records:
        if a["age"]>=min_age:
            if a["age"]<=max_age:
                list_of_ids.append(a["id"])

    return (list_of_ids)


def count_by_gender(records):
    '''
    Description: Counts the number of males and females

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A dictionary with the following two key-value pairs:
            KEY        VALUE
            "male"     No of males (INTEGER)
            "female"   No of females (INTEGER)
    '''

    d={"male":0,"female":0}

    for a in records:
        if a["gender"]=="male":
            d["male"]+=1
        elif a["gender"]=="female":
            d["female"]+=1

    return (d)  
            


def filter_by_address(records, address):
    '''
    Description: Filters the person records whose address matches the given address. 

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
            Some examples are:
                    Case 1: {} 
                            => All records match this case
                    
                    Case 2: { "block": "AD", "city": "Delhi" } 
                            => All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
                    
                    Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

    Returns:
    - A LIST of DICTIONARIES with the following two key-value pairs:
            KEY            VALUE
            "first_name"   first name (STRING)
            "last_name"    last name (STRING)
    '''

    list_of_dictionaries=[]

    for a in records:
        f=1
        for b in address:
            if address[b]:
                if type(address[b])==int:
                    if a["address"][b]!=address[b]:
                        f=0
                else:
                    if a["address"][b].lower()!=address[b].lower():
                        f=0

        if f==1:
            list_of_dictionaries.append({"first_name":a["first_name"],"last_name":a["last_name"]})

    return (list_of_dictionaries)


def find_alumni(records, institute_name):
    '''
    Description: Find all the alumni of the given institute name (case-insensitive). 
    
    Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - institute_name (STRING): Name of the institute (case-insensitive)

    Returns:
    - A LIST of DICTIONARIES with the following three key-value pairs:
            KEY            VALUE
            "first_name"   first name (STRING)
            "last_name"    last name (STRING)
            "percentage"   percentage (FLOAT)
    '''
    institute_name=institute_name.lower()
    
    list_of_dictionaries=[]

    for a in records:
        for b in a["education"]:
            if b["institute"].lower()==institute_name:
                if not b["ongoing"]:
                    list_of_dictionaries.append({"first_name":a["first_name"],"last_name":a["last_name"],"percentage":b["percentage"]})
                    break

    return (list_of_dictionaries)


def find_topper_of_each_institute(records):
    '''
    Description: Find topper of each institute

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

    Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs.
    The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
    '''

    list_of_dictionaries={}

    for a in records:
        for b in a["education"]:
            if not b["ongoing"]:
                if b["institute"] in list_of_dictionaries:
                    if list_of_dictionaries[b["institute"]]["percentage"]<b["percentage"]:
                        list_of_dictionaries[b["institute"]]={"id":a["id"],"percentage":b["percentage"]}
                else:
                    list_of_dictionaries[b["institute"]]={"id":a["id"],"percentage":b["percentage"]}

    d={}

    for a in list_of_dictionaries:        
        d[a]=list_of_dictionaries[a]["id"]

    return (d)


def find_blood_donors(records, receiver_person_id):
    '''
    Description: Find all donors who can donate blood to the person with the given receiver ID.

            Note: 
            - Possible blood groups are "A", "B", "AB" and "O".

            Rules:
            BLOOD GROUP      CAN DONATE TO
            A                A, AB
            B                B, AB
            AB               AB
            O                A, B, AB, O

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - receiver_person_id (INTEGER): The ID of the donee
            Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

    Returns:
    - A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
    '''

    for receiver in records:
        if receiver["id"]==receiver_person_id:
            break
    else:
        return ()

    blood_group=receiver["blood_group"]

    if blood_group=="AB":
        donor_groups=["AB","A","B","O"]
    elif blood_group=="A":
        donor_groups=["A","O"]
    elif blood_group=="B":
        donor_groups=["B","O"]
    else:
        donor_groups=["O"]

    donors={}

    for a in records:
        if a["id"]==receiver_person_id:
            continue
        if a["blood_group"] in donor_groups:
            donors[a["id"]]=a["contacts"]

    return (donors)

    


def get_common_friends(records, list_of_ids):
    '''
    Description: Find the common friends of all the people with the given IDs

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

    Returns:
    - A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
    '''

    list_of_lists=[]

    for a in records:
        if a["id"] in list_of_ids:
            list_of_lists.append(a["friend_ids"])

    common_friends=list_of_lists[0]

    for a in list_of_lists:
        cf2=[]

        for b in common_friends:
            if b in a:
                cf2.append(b)

        common_friends=cf2

    return (common_friends)


def is_related_recursion(r,p1,p2,ids_done):
    if p1["id"] in ids_done:
        pass
    elif p1==p2:
        return (True)
    else:
        ids_done.append(p1["id"])
        for a in p1["friend_ids"]:
            if a not in ids_done:
                for b in r:
                    if b["id"]==a:
                        p3=b
                        break
                return (is_related_recursion(r,p3,p2,ids_done))
    return (False)

    


def is_related(records, person_id_1, person_id_2):
    '''
    **** BONUS QUESTION ****
    Description: Check if 2 persons are friends

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id_1 (INTEGER): first person ID
    - person_id_2 (INTEGER): second person ID

    Returns:
    - A BOOLEAN denoting if the persons are friends of each other, directly or indirectly
    (if A knows B, B knows C and C knows D, then A knows B, C and D).
    '''

    for a in records:
        if a["id"]==person_id_1:
            p1=a
        elif a["id"]==person_id_2:
            p2=a

    return (is_related_recursion(records,p1,p2,[]))
    
    


def delete_by_id(records, person_id):
    '''
    Description: Given a person ID, this function deletes them from the records.
    Note that the given person can also be a friend of any other person(s),
    so also delete the given person ID from other persons friend list.
    If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    
    for a in records:
        if person_id==a["id"]:
            records.remove(a)
        elif person_id in a["friend_ids"]:
            a["friend_ids"].remove(person_id)

    return (records)


def add_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function makes them friends of each other.
    If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
    
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    f=0

    for a in records:
        if a["id"]==person_id:
            person=a["friend_ids"]
            f+=1
        elif a["id"]==friend_id:
            friend=a["friend_ids"]
            f+=1

    if f==2:
        if friend_id not in person:
            person.append(friend_id)
            person.sort()
        if person_id not in friend:
            friend.append(person_id)
            friend.sort()

    return (records)
    


def remove_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function removes them as friends of each other.
    If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
    
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    person=[]
    friend=[]

    for a in records:
        if a["id"]==person_id:
            person=a["friend_ids"]
            if friend_id not in person:
                return (records)
        elif a["id"]==friend_id:
            friend=a["friend_ids"]
            if person_id not in friend:
                return (records)
            
    if person and friend:
        person.remove(friend_id)
        friend.remove(person_id)

    return (records)


def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
    Description: Adds an education record for the person with the given person ID.
    The education record constitutes of insitute name, the person's percentage and
    if that education is currently ongoing or not. Please look at the format of an
    education field from the PDF. If the person ID is not available in the records,
    you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - institute_name (STRING): The institute name (case-insensitive)
    - ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
    - percentage (FLOAT): The person's score in percentage

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    if not ongoing:
        d={"institute": institute_name, "ongoing": ongoing, "percentage": percentage}
    else:
        d={"institute": institute_name, "ongoing": ongoing}

    for a in records:
        if a["id"]==person_id:
            a["education"].append(d)
            break

    return (records)
