balence = 1000
pin_given = 5531
print("Welcome SBI")
pin = int(input("Enter your pin Number"))

if(pin == pin_given):
    print("Welcome Dharma Appana")
    print("Select the Options")
    print("Check balence = 1")
    options = int(input("Enter the  choice"))
    if options == 1 :
        print(balence)
    elif options == 2:
        widthdrawl = int(input("Enter the Amount to be withdraw"))
        if widthdrawl <= balence :
            print("krkrkrkrkrkrkr")
            print("Widthdraw Succesfull")
        else:
            print("Insufficient Funds")
else:
    print("Invalid Pin")