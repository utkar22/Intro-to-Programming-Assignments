# Name - Utkarsh Arora
# Roll No - 2020143

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.

import a2



class Menu:
    def __init__(self):
        self.read_data_from_file()
        self.define_lists()

    def define_lists(self):
        self.display_list=[
            "read_data_from_file",
            "filter_by_first_name",
            "filter_by_last_name",
            "filter_by_full_name",
            "filter_by_age_range",
            "count_by_gender",
            "filter_by_address",
            "find_alumni",
            "find_topper_of_each_institute",
            "find_blood_donors",
            "get_common_friends",
            "is_related",
            "delete_by_id",
            "add_friend",
            "remove_friend",
            "add_education"
            ]

        self.functions_list=[
            self.read_data_from_file,
            self.filter_by_first_name,
            self.filter_by_last_name,
            self.filter_by_full_name,
            self.filter_by_age_range,
            self.count_by_gender,
            self.filter_by_address,
            self.find_alumni,
            self.find_topper,
            self.find_blood_donors,
            self.get_common_friends,
            self.is_related,
            self.delete_by_id,
            self.add_friend,
            self.remove_friend,
            self.add_education
            ]

    def read_data_from_file(self):
        self.records=a2.read_data_from_file()

    def take_name(self, s):
        while True:
            name=input(s)
            if name:
                return (name)

    def take_id(self, s, pct=False):
        while True:
            x=input(s)

            try:
                x=int(x)

                if pct:
                    if not 0<=x<=100:
                        print ("Enter a valid percentage.")
                        continue
                return (x)
            except:
                print ("Invalid input. (Give a numeric input)")

    def show_records(self):
        s=input("Would you like to see the updated records? (Warning: may crash your console.)")

        if s.lower() in ["yes","y","1","true"]:
            print (self.records)

    def show_list(self,list_of_ids,s):
        if list_of_ids:
            print (f"{s}:")
            for a in list_of_ids:
                print (a)
        else:
            print ("No IDs match your query.")


    def filter_by_first_name(self):
        name=self.take_name("Enter first name: ")
        
        list_of_ids=a2.filter_by_first_name(self.records,name)

        self.show_list(list_of_ids,"List of IDs with that first name")

    def filter_by_last_name(self):
        name=self.take_name("Enter last name: ")

        list_of_ids=a2.filter_by_last_name(self.records,name)

        self.show_list(list_of_ids,"List of IDs with that last name")

    def filter_by_full_name(self):
        name=self.take_name("Enter full name: ")

        list_of_ids=a2.filter_by_full_name(self.records,name)

        self.show_list(list_of_ids,"List of IDs with that name")

    def filter_by_age_range(self):
        min_age=self.take_id("Minimum age: ")
        max_age=self.take_id("Maximum age: ")

        list_of_ids=a2.filter_by_age_range(self.records,min_age,max_age)

        self.show_list(list_of_ids,"List of IDs within that age range")

    def count_by_gender(self):
        d=a2.count_by_gender(self.records)

        print (f"No of males: {d['male']}")
        print (f"No of females: {d['female']}")

    def filter_by_address(self):
        address={
            "house_no": input("House Number: "),
            "block": input("Block: "),
            "town": input("Town: "),
            "city": input("City: "),
            "state": input("State: "),
            "pincode": input("Pincode: ")
            }

        try:
            address["house_no"]=int(address["house_no"])
        except:
            address["house_no"]=None

        list_of_dictionaries=a2.filter_by_address(self.records,address)

        if list_of_dictionaries:
            print ("The following names fulfil the query:") 
            for a in list_of_dictionaries:
                print (f"{a['first_name']} {a['last_name']}")
        else:
            print ("None of the records fulfil that query.")

    def find_alumni(self):
        institute=self.take_name("Enter name of institute: ")

        list_of_dictionaries=a2.find_alumni(self.records,institute)

        if list_of_dictionaries:
            for a in list_of_dictionaries:
                print (f"{a['first_name']} {a['last_name']}: {a['percentage']}%")
        else:
            print ("None of the records fulfil that query.")
            
    def find_topper(self):
        d=a2.find_topper_of_each_institute(self.records)

        for a in d:
            print (f"{a}: {d[a]}")

    def find_blood_donors(self):
        receiver=self.take_id("Enter receiver ID: ")

        donors=a2.find_blood_donors(self.records,receiver)

        if donors:
            print ("The following records are valid donors:")
            for a in donors:
                print (f"Donor ID: {a}, Contact info: {donors[a]}")
        else:
            print ("None of the records fulfil that query.")
        
    def get_common_friends(self):
        list_of_ids=[]
        while True:
            x=input("Enter id (enter blank space to quit): ")

            if x=="":
                break

            try:
                x=int(x)
                list_of_ids.append(x)
            except:
                print ("Invalid Input!")

        common_friends=a2.get_common_friends(self.records,list_of_ids)

        if common_friends:
            print ("Common friends:")
            for a in common_friends:
                print (a)
        else:
            print ("There are no common friends.")

    def is_related(self):
        p1=self.take_id("Person 1: ")
        p2=self.take_id("Person 2: ")

        if a2.is_related(self.records,p1,p2):
            print ("Yes, they are related.")
        else:
            print ("No, they are not related.")

    def delete_by_id(self):
        print ("Warning: This cannot be undone.")

        x=self.take_id("ID of record to be deleted: ")

        self.records=a2.delete_by_id(self.records,x)

        print ("Done.")

        self.show_records()

    def add_friend(self):
        person_id=self.take_id("Enter the person's id: ")
        friend_id=self.take_id("Enter the friend's id: ")

        self.records=a2.add_friend(self.records,person_id,friend_id)

        print ("Done.")

        self.show_records()

    def remove_friend(self):
        person_id=self.take_id("Enter the person's id: ")
        friend_id=self.take_id("Enter the friend's id: ")

        self.records=a2.remove_friend(self.records,person_id,friend_id)

        print ("Done.")

        self.show_records()

    def add_education(self):
        person_id=self.take_id("Enter person id: ")
        institute_name=self.take_name("Enter institute name: ")

        while True:
            s=input("Is the course ongoing? (Y/N)")

            if s.lower()=="y":
                ongoing=True
                break
            elif s.lower()=="n":
                ongoing=False
                break

            print ("Enter only Y/N")

        if not ongoing:
            while True:
                pct=input("Enter percentage: ")

                try:
                    pct=float(pct)
                    break
                except:
                    print ("Invalid input.")
        else:
            pct=None

        self.records=a2.add_education(self.records,person_id, institute_name, ongoing, pct)

        print ("Done.")

        self.show_records()      
            
    
    def menu(self):
        print ("Greetings! Welcome to the interactive menu!")
        print ()

        for a in range(1,17):
            print (f"{a}) {self.display_list[a-1]}")
        
        while True:
            x=input("Which function would you like to use? (enter -1 to exit) ")

            try:
                x=int(x)
            except:
                print ("Wrong input!")
                continue

            if x==-1:
               break

            if x not in range(1,17):
                print ("Wrong input!")
                continue

            self.functions_list[x-1]()
            print ()

        print ("Thank you for using this system!")

menu=Menu()

menu.menu()
        
