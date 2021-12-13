class phone_contacts:

    def __init__(self, Firstname, Lastname, Phone_number, Email_ID, Groups, DOB):
        self.firstname = Firstname
        self.lastname = Lastname
        self.phonenumber = Phone_number
        self.emailid = Email_ID
        self.groups = Groups
        self.dob = DOB

    def open_phcontacts(self):
        print("Phone Contacts")

    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <=15:
                print("Firstname verified")
            else:
                raise ValueError("Firstname should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")

    def lastname_verification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <=15:
                print("Lastname verified")
            else:
                raise ValueError("Lastname should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Lastname should contain letters only")

    def phonenumber_verification(self):
        if(len(self.phonenumber)==10):
            if type(self.phonenumber) == str:
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers")
        else:
            raise ValueError("Phone number should not be greater or lesser than 10")

    def emailid_verification(self):
        if type(self.emailid) == str:
            if len(self.emailid) <=30:
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 30 values")
        else:
            raise TypeError("Invalid email ID")

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <=10:
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Group should contain letters only")

    def dob_verification(self):
        if isinstance(self.dob,str):
            if len(self.dob) <= 10:
                print("Date Of Birth Verified")
            else:
                raise ValueError("DOB should contain numbers and symbols only")


puspanathan = phone_contacts("Puspanathan","G","8637635446","puspanathang@gmail.co","Home","13/10/2000")
puspanathan.open_phcontacts()
puspanathan.firstname_verification()
puspanathan.lastname_verification()
puspanathan.phonenumber_verification()
puspanathan.emailid_verification()
puspanathan.groups_verification()
puspanathan.dob_verification()


phone = [{"Firstname":"Aravindh","Lastname":"M.P","Phno":9994734456,"Email_id":"aravindh@gmail.com","Groups":"Home","DOB":"16/10/2000"},
         {"Firstname":"Siva","Lastname":"J","Phno":9876543210,"Email_id":"siva@gmail.com","Groups":"Friends","DOB":"16/08/2000"},
         {"Firstname":"Aswath","Lastname":"G","Phno":9823568941,"Email_id":"aswathg@gmail.com","Groups":"Office","DOB":"29/08/2000"},
         {"Firstname":"Indhu","Lastname":"mathi","Phno":9123659800,"Email_id":"indhu@gmail.com","Groups":"Friends","DOB":"06/09/2000"},
         {"Firstname":"Roshni","Lastname":"P","Phno":9864658764,"Email_id":"Roshni@gmail.com","Groups":"Friends","DOB":"28/05/2000"}]

for i in phone:
    for j,k in i.items():
        print(f"{j}:{k}")
    





















