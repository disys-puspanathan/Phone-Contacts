contacts = {"Anu":9087014956,"Aswath":8569587420,"Aravindh":6398527414,"Ajay kumar":7878794561,"Anjana":9520147963,"Ajith":9994744562,
            "Abbhas":8968745213,"Banu":7419630025,"Barath":7788994455,"Brindha":9876543210,"Brindhesh":6563646768,"Chandru":9998813452,
            "Cibi":9000554987,"Dhinesh":8886612345,"Gowtham":9952684128,"Guna":9943030973,"Hari":8610408567,"Harish":6383866533,
            "Indhu":6382621190,"Jaison":8220132890,"Jayanth":8883396779,"Kamalesh":6379935955,"Karthick":7868802316,"Kavin":8428434362,
            "Kiruba":6383114399,"Kovai":809691000,"Krishna":7708101333,"Loki":8770832705}
def createnewcontact():
    phonenumber = input("___Enter phone number___:")
    if(len(phonenumber) == 10):
            print("Phone number created")
        else:
            raise TypeError("Phone number should contain only integers")
    else:
        raise ValueError("Phone Number should contain 10 numbers only")
    yesno=input("continue y/n ?")
    if(yesno == 'y'):
           menu()
    else:
            exit()

def viewcontact():
    for i,j in contacts.items():
        print("",i,":",j)
        print("\n")


def menu():
    print("""
    1.Create New Contact
    2.View Contact
    3.Exit Contact App
    """)

    select = int(input("_____________________________________Select options________________________________"))
    print("\n")
    if(select == 1):
        pc = createnewcontact()
    elif(select == 2):
        viewcontact()
    elif(select == 3):
        print("___Left___")
        exit()

menu()
    
    
