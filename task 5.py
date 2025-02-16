contact= {}
def display_contact():
    print("Name\t\tContact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice =int(input("1: Add new contact\n2: Search contact\n3: Display contact\n4: Update contact\n5: Delete contact\n6:Exit\nEnter your choice "))
    if choice==1:
        name=input("Enter the name = ")
        mobile_number=input("Enter the mobile_name = ")
        contact[name]=mobile_number
    elif choice==2:
        search_name=input("Enter the name = ")
        if search_name in contact:
            print(search_name,"'s contact is",contact[search_name])
        else:
            print("Name not found in contact book")    
    elif choice==3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choice==4:
        update_contact= input("Enter the contact to be updated = ")  
        if update_contact in contact:
           mobile_number=input("enter contact number")
           contact[update_contact]=mobile_number
           print("Contact updated")
           display_contact()
        else:
             print("Name not found in contact book")    
    elif choice==5:
        del_contact= input("Enter the contact to be deleted = ") 
        if del_contact in contact:
            confirm=input("Do you want to delete this number y/n = ")   
        if confirm=='y' or confirm=='Y':
            contact.pop(del_contact)
            display_contact()
        else:
             print("Name not found in contact book")   
    else:
        break






