# CHEONG JIA YAO TP060827
# EMILY KUAN YU XUAN TP060808

def homePage():
    print("-------------------------------------------")
    print("Welcome to SUPER CAR RENTAL SERVICE")
    print("-------------------------------------------")
    print("Please choose to continue as a: ")
    print("1. Admin")
    print("2. Customer")
    option = int(input("Enter your option [1] OR [2]: " ))
    if (option == 1):
        print("You will be directed to Admin Login Page" + "\n")
        adminLogin()
    elif (option == 2):
        print("--------------------------------------------------------------------")
        print("Hi, have you registered as a member in Super Car Rental Service?")
        print("1. YES, I am a member")
        print("2. NO, I would like to continue as a guest")
        option = int(input("Enter your option [1] or [2] to continue: "))
        if (option == 1):
            print("\nYou will be directed to Login Page." + "\n")
            customerLogin()
        elif (option == 2):
            print("\nYou will be directed to next page." + "\n")
            unregisteredUserPage()
        else:
            print("\nInvalid Input ! Auto redirect back to Home Page." + "\n")
            homePage()
    else:
        print("\nInvalid Input ! Auto redirect back to Home Page." + "\n")
        homePage()


def adminPage():
    print('\nPlease choose an operation from option below:')
    print('--------------------------------------------------------------------------------------')
    print(f'(1) Add / Modify Car Details \t\t(2) View Car Available / Car Rented Out')
    print(f'(3) View Customer Bookings \t\t(4) Search Customer Bookings')
    print(f'(5) View Customer Payments Details \t(6) Search Customer Payments Details')
    print(f'(7) View Customer Personal Details \t(8) Exit')
    print('--------------------------------------------------------------------------------------')
    option = int(input('Enter your option to continue: '))
    print()
    if (option == 1):
        print("Choose an operation from choices below:")
        print('----------------------------------------------')
        print('(1) Add a New Car')
        print('(2) Modify Existing Car Details')
        print('----------------------------------------------')
        choice = int(input('Enter your option to continue: '))
        if (choice == 1):
            carDetails()
            adminPage()
        elif (choice == 2):
            modifyCarDetails()
            adminPage()
        else:
            print("Please choose a valid choice")
            adminPage()
    elif (option == 2):
        print("Choose one of the following choices: ")
        print('1. Display all Car Details')
        print('2. Display Car for Rent (Available)')
        print('3. Display Car Rented Out (Unavailable)')
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            printCarDetails()
            adminPage()
        elif (choice == 2):
            printAvailableCars()
            adminPage()
        elif (choice == 3):
            printRentedCars()
            adminPage()
        else:
            print("Please choose a valid choice.")
            adminPage()
    elif (option == 3):
        printCustomerBookings()
        adminPage()
    elif (option == 4):
        searchCustomerBookings()
        adminPage()
    elif (option == 5):
        printCustomerPayment()
        adminPage()
    elif (option == 6):
        searchCustomerPayment()
        adminPage()
    elif (option == 7):
        printCustomerDetails()
        adminPage()
    elif (option == 8):
        homePage()
    else:
        print("Please enter a valid option.")
        adminPage()


def registeredUserPage(username):
    print('Please choose an operation from options below:')
    print('--------------------------------------------------------------------------------------')
    print(f'(1) Modify Personal Details \t\t(2) View Cars for Rent')
    print(f'(3) Make Booking \t\t\t(4) Make Payment for Booking')
    print(f'(5) View Booking History \t\t(6) Exit')
    print('--------------------------------------------------------------------------------------')
    option = int(input('Enter your option to continue: '))
    if (option == 1):
        modifyCustomerDetails(username)
        registeredUserPage(username)
    elif (option == 2):
        printAvailableCars()
        registeredUserPage(username)
    elif (option == 3):
        customerBooking(username)
    elif (option == 4):
        saveCustomerPayment(username)
        registeredUserPage(username)
    elif (option == 5):
        customerBookings(username)
        registeredUserPage(username)
    elif (option == 6):
        homePage()
    else:
        print("Please enter a valid option")
        registeredUserPage(username)


def unregisteredUserPage():
    print('Please choose an operation from options below:')
    print('1. View Cars for Rent')
    print('2. Register as a Member')
    print('3. Exit')
    print()
    option = int(input("Enter your option to continue: "))
    if (option == 1):
        printAvailableCars()
        unregisteredUserPage()
    elif (option == 2):
        customerDetails()
    elif (option == 3):
        homePage()
    else:
        print("Please enter a valid option")
        unregisteredUserPage()


def adminLogin():
    adminUsername = "admin"
    adminPassword = "admin"
    print("You need to enter your username and password to continue.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if (username == adminUsername) and (password == adminPassword):
        print("\n" + "-------------------------- Login Successfully! --------------------------")
        print()
        adminPage()
    else:
        print("Invalid input ! Please login again." + "\n")
        adminLogin()


def customerLogin():
    print(f'Please enter your login USERNAME and PASSWORD')
    username = input(f'\nEnter your username: ')
    password = input(f'Enter your password: ')
    found = False
    try:
        fileHandler = open('customer_details.txt', 'r')
        lines = fileHandler.readlines()
        for line in lines:
            info = line.rstrip().split('\t')
            if username == info[4] and password == info[5]:
                found = True
        if (found == True):
            print("\nLogin Successful")
            print("You will be directed to MAIN PAGE." + '\n')
            registeredUserPage(username)
        else:
            print("Invalid Username or Password ! Please login again." + "\n")
            customerLogin()
        fileHandler.close()
    except:
        print("Customer Details file cannot be opened")
        customerLogin()
    return username


def customerDetails():
    print("--------------- Please enter your  personal details --------------")
    customerList = []
    info = []
    name = input('Enter your name: ')
    contactNumber = input('Enter your contact number [10digits]: ')
    identityNumber = input('Enter your identification card number [ without [-] ]: ')
    email = input('Enter your email address: ')
    loginUsername = input('Enter your username: ')
    loginPassword = input('Enter your password: ')
    info.append(name.capitalize())
    info.append(contactNumber)
    info.append(identityNumber)
    info.append(email)
    info.append(loginUsername)
    info.append(loginPassword)
    customerList.append(info)
    
    add = open('customer_details.txt', 'a')
    for customer in customerList:
        for info in customer:
            add.write(str(info))
            add.write('\t')
        add.write('\n')
    add.close()
    print("--------------------- Congratulations! You have been registered as a member! ---------------------- ")
    print("You are required to login before proceeding to next page" + '\n')
    customerLogin()


def carDetails():
    carList = []
    info = []
    carID = input('Enter carID: ')
    carName = input('Enter name of car: ')
    carBrand = input('Enter brand of car: ')
    carCapacity = (input('Enter the capacity of car: '))
    carCost = input('Enter cost of car per day [RM]: ')
    carStatus = 'Available'
    info.append(carID.capitalize())
    info.append(carName.capitalize())
    info.append(carBrand.capitalize())
    info.append(carCapacity)
    info.append(carCost)
    info.append(carStatus.capitalize())
    carList.append(info)

    car = open('car_details.txt', 'a')
    for info in carList:
        for details in info:
            car.write(str(details))
            car.write('\t')
        car.write('\n')
    car.close()
    print('--------------------- Car Added Successful ! ---------------------\n')

    choice = int(input('Enter [1] to CONTINUE add new car OR [0] to back to MAIN PAGE: '))
    if choice == 1:
        carDetails()
    elif choice == 2:
        adminPage()
    else:
        adminPage()


def customerBooking(username):
    printAvailableCars()
    print('--------------------------------------------------------------------------------------')
    bookings = []
    details = []
    print("\nEnter Car Booking Details: ")
    carID = input("Enter Car ID you would like to book: ")
    bookingDate = input("Enter today's date [YYYY/MM/DD]: ")
    duration = int(input("Enter duration you would like to book [DAYS]: "))
    print("----------------------------------------------------------")
    details.append(username)
    details.append(carID.capitalize())
    details.append(bookingDate)
    details.append(duration)
    bookings.append(details)

    try:
        newbooking = open('customer_bookings.txt', 'a')
        for booking in bookings:
            for details in booking:
                newbooking.write(str(details))
                newbooking.write('\t')
            newbooking.write('\n')
        newbooking.close()
        print("\nBooking has been made. Please proceed to checkout and make payment." +'\n')
    except:
        print("This file cannot be opened")

    con = int(input('Enter [1] to CONTINUE make booking OR [ENTER} to back to MAIN PAGE: '))
    c = False
    if con == 1:
        c = True
    if (c == True):
        customerBooking(username)
    else:
        registeredUserPage(username)


def printCustomerDetails():
    try:
        fileHandler = open('customer_details.txt', 'r')
        lines = fileHandler.readlines()
        for line in lines:
           info = line.rstrip().split('\t')
           print("\nName: ", info[0], "\nContact Number: ", info[1], "\nIdentification Number: ", info[2], "\nEmail: ", info[3], "\nUsername: ", info[4], "\nPassword: ", info[5])
        fileHandler.close()
    except:
        print("This file cannot be opened")


def modifyCustomerDetails(username):
    try:
        cust = open('customer_details.txt', 'r')
        newCust = open('temp.txt', 'w')
        lines = cust.readlines()
        for line in lines:
            info = line.rstrip().split('\t')
            if (username == info[4]):
                print("--------------------------------------------------------")
                print('Old Personal Details:')
                print("Name: ", info[0], "\nContact Number: ", info[1], "\nIdentification Number: ", info[2], "\nEmail: ", info[3], "\nUsername: ", info[4], "\nPassword: ", info[5])
                print(f'\nSelect personal details you would like to modify: ')
                print('--------------------------------------------------------------------------------------')
                print(f'(1) Name \t\t\t(2) Contact Number')
                print(f'(3) Identification Number \t(4) Email')
                print(f'(5) Username \t\t(6) Password')
                print('--------------------------------------------------------------------------------------')
                choice = int(input('Enter your choice: '))
                if choice == 1:
                    if username == info[4]:
                        newName = input("\nEnter New Name: ")
                        newCust.write(newName.capitalize() + '\t' + info[1] + '\t' + info[2] + '\t' + info[3] + '\t' + info[4] + '\t' + info[5] + '\n')
                    else:
                        newCust.write(line)
                elif choice == 2:
                    if (username == info[4]):
                        contanctNum = input("\nEnter New Contact Number: ")
                        newCust.write(info[0] + '\t' + str(contactNum) + '\t' + info[2] + '\t' + info[3] + '\t' + info[4] + '\t' + info[5] + '\n')
                    else:
                        newCust.write(line)
                elif choice == 3:
                    if (username == info[4]):
                        identificationNum = input("\nEnter New Identification Number: ")
                        newCust.write(info[0] + '\t' + info[1]+ '\t' + str(identificationNum) + '\t' + info[3] + '\t'+ info[4]+ '\t'+ info[5]+ '\n')
                    else:
                        newCust.write(line)
                elif choice == 4:
                    if (username == info[4]):
                        newEmail = input("\nEnter New Email: ")
                        newCust.write(info[0]+ '\t'+ info[1]+ '\t'+ info[2]+ '\t'+ newEmail.capitalize() + '\t'+ info[4]+ '\t'+ info[5]+ '\n')
                    else:
                        newCust.write(line)
                elif choice == 5:
                    if (username == info[4]):
                        newUsername = input("\nEnter New Username: ")
                        newCust.write(info[0]+ '\t' + info[1] + '\t' + info[2] + '\t' + info[3] + '\t' + newUsername + '\t' +  info[5] + '\n')
                    else:
                        newCust.write(line)
                elif choice == 6:
                    if (username == info[4]):
                        newPassword = input("\nEnter New Password: ")
                        newCust.write(info[0] + '\t' + info[1] + '\t' +  info[2] + '\t' + info[3] + '\t' + info[4] + '\t' + newPassword + '\n')
                    else:
                        newCust.write(line)
                else:
                    print('Please enter a valid option')
                    con = input("Press 'X' to back to main menu or 'C' to continue modify")
                    if (con == 'x' or con == 'X'):
                        registeredUserPage(username)
                    elif (con == 'c' or con == 'C'):
                        modifyCustomerDetails(username)
                    else:
                        registeredUserPage(username)
        else:
            print('User not found in system')
            registeredUserPage(username)
        newCust.close()
        cust.close()
        
        newCust = open('temp.txt', 'r')
        cust = open('customer_details.txt', 'w')
        for line in newCust:
            cust.write(line)
        print("\nYour personal details has been updated successfully! ")
        cust.close()
        newCust.close()   
    except:
        print("This file is not accessible")
        registeredUserPage(username)


### This function is used to save all car details inserted
##def newCarDetails():
##    # Open car_details file as append mode
##    try:
##        fileHandler = open('car_details.txt', 'a')
##    except:
##        print("This file cannot be opened.")
##        adminPage()
##    lines = carDetails()
##    # Append every details into car_details file
##    for car in lines:
##        for info in car:
##            # write information into the file
##            fileHandler.write(str(info))
##            fileHandler.write('\t')
##        fileHandler.write('\n')
##        # Close file after used
##        fileHandler.close()


def printCarDetails():
    try:
        fileHandler = open('car_details.txt', 'r')
    except:
        print("This file cannot be opened")
        adminPage()
    lines = fileHandler.readlines()
    for line in lines:
        info = line.rstrip().split('\t')
        print("Car ID:", info[0], "\tName:", info[1], "\tBrand:", info[2], "\tCapacity:", info[3], "\tCost(per day):", info[4], "\tStatus:", info[5])
        fileHandler.close()
        print()


def printAvailableCars():
    try:
        fileHandler = open('car_details.txt', 'r')
    except:
        print('This file cannot be opened')
    lines = fileHandler.readlines()
    for line in lines:
        info = line.rstrip().split('\t')
        if info[-1] == "Available":
            print("Car ID:", info[0], "\tName:", info[1], "\tBrand:", info[2], "\tCapacity:", info[3], "\tCost(per day):", info[4], "\tStatus:", info[5])
        elif info[-1] != "Available":
            continue
        else:
            print('There is no car available for rent now. Please visit next time.')
        fileHandler.close()
        print()


def printRentedCars():
    try:
        fileHandler = open('car_details.txt', 'r')
    except:
        print('This file cannot be opened')
    lines = fileHandler.readlines()
    for line in lines:
        info = line.rstrip().split('\t')
        if info[-1] == "Unavailable":
            print("Car ID:", info[0], "\tName:", info[1], "\tBrand:", info[2], "\tCapacity:", info[3], "\tCost(per day):", info[4], "\tStatus:", info[5])
        elif info[-1] != "Unavailable":
            continue
        else:
            print('There is no car rent out for now.')
        fileHandler.close()
        print()


def modifyCarDetails():
    found = False
    carID = input("Provide respective CarID you would like to modify: ")
    try:
        car = open("car_details.txt", "r")
        newCar = open("tempCar.txt", "w")
        lines = car.readlines()
        for line in lines:
            info = line.rstrip().split('\t')
            if carID == info[0]:
                found = True
        if (found == True):
            print("\nCar ID:", info[0], "\tName:", info[1], "\tBrand:", info[2], "\tCapacity:", info[3], "\tCost(per day):", info[4], "\tStatus:", info[5])
            print("\nChoose details you would like to modify:")
            print('--------------------------------------------------------------------------------------')
            print(f'(1) Car ID \t\t(2) Name \t\t(3) Brand')
            print(f'(4) Capacity \t(5) Cost \t\t(6) Status')
            print('--------------------------------------------------------------------------------------')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                if carID == info[0]:
                    newID = input("\nEnter modified carID: ")
                    newCar.write(newID.capitalize() + "\t" + info[1] + "\t" + info[2] + "\t" + info[3] + "\t" + info[4] + "\t" + info[5] + "\n")
                else:
                    newCar.write(line)
            elif choice == 2:
                if carID == info[0]:
                    name = input("\nEnter modified name of car: ")
                    newCar.write(info[0] + '\t' + name.capitalize() + '\t' + info[2] + '\t' + info[3] + '\t' + info[4] + '\t' + info[5] + '\n')
                else:
                    newCar.write(line)
            elif choice == 3:
                if carID == info[0]:
                    brand = input("\nEnter modified brand of car: ")
                    newCar.write(info[0] + '\t' + info[1]+ '\t' + brand.capitalize() + '\t' + info[3] + '\t'+ info[4]+ '\t'+ info[5]+ '\n')
                else:
                    newCar.write(line)
            elif choice == 4:
                if carID == info[0]:
                    capacity = input("\nEnter capacity of car: ")
                    newCar.write(info[0]+ '\t'+ info[1]+ '\t'+ info[2]+ '\t'+ capacity+ '\t'+ info[4]+ '\t'+ info[5]+ '\n')
                else:
                    newCar.write(line)
            elif choice == 5:
                if carID == info[0]:
                    cost = input("\nEnter modified cost of car per day: RM ")
                    newCar.write(info[0]+ '\t' + info[1] + '\t' + info[2] + '\t' + info[3] + '\t' + cost + '\t' +  info[5] + '\n')
                else:
                    newCar.write(line)
            elif choice == 6:
                if carID == info[0]:
                    status = input("\nEnter the modified status of car [Available] OR [Unavailable]: ")
                    newCar.write(info[0] + '\t' + info[1] + '\t' +  info[2] + '\t' + info[3] + '\t' + info[4] + '\t' + status.capitalize() + '\n')
                else:
                    newCar.write(line)
            else:
                print('Please enter a valid option')
                modifyCarDetails()
        else:
            print('Car ID not found in system')
            modifyCarDetails()
        car.close()
        newCar.close()
        newCar = open('tempCar.txt', 'r')
        car = open('car_details.txt', 'w')
        for line in newCar:
            car.write(line)
        print("\nDetail has been updated!")
        car.close()
        newCar.close()   
    except:
        print("This file is not able to be opened")

    con = int(input('Enter [1 to CONTINUE editing] OR [0 to back to ADMIN PAGE]: '))
    if con == 1:
        modifyCarDetails()
    elif con == 2:
        adminPage()
    else:
        adminPage()


##def saveCustomerBookings(username):
##    try:
##        booking = open('customer_bookings.txt', 'a')
##        for booking in bookings:
##            for details in booking:
##                fileHandler.write(str(details))
##                fileHandler.write('\t')
##            fileHandler.write('\n')
##        fileHandler.close()
##        print("Booking has been made. Please proceed to checkout and make payment." +'\n')
##    except:
##        print("This file cannot be opened")



def printCustomerBookings():
    try:
        fileHandler = open('customer_bookings.txt', 'r')
        lines = fileHandler.readlines()
        for line in lines:
            info = line.rstrip().split('\t')
            print("\nCustomer Username:", info[0], "\nCarID:", info[1], "\nPrice:", info[2], "\nBookingDate:", info[3], "\nDurationBooked:", info[4])
            print('\n')
        fileHandler.close()
    except:
        print("This file cannot be opened")


def searchCustomerBookings():
    search = input("Enter customer USERNAME to search customer bookings: ")
    try:
        find = open('customer_bookings.txt', 'r')
        lines = find.readlines()
        for line in lines:
                    info = line.rstrip().split('\t')
                    if search.capitalize() != info[0]:
                        continue
                    elif search.capitalize() == info[0]:
                        print("\Customer Username:", info[0], "\nCar ID:", info[1], "\nPrice:", info[2], "\nBooking Date:", info[3], "\nDuration Booked:", info[4])
                    else:
                        print("No booking history found.")
        find.close()
    except:
        print("This file cannot be opened")


def customerBookings(username):
    try:
        find = open('customer_bookings.txt', 'r')
        lines = find.readlines()
        for line in lines:
                    info = line.rstrip().split('\t')
                    if username != info[0]:
                        continue
                    elif username == info[0]:
                        print("\nCar ID:", info[1], "\nPrice:", info[2], "\nBooking Date:", info[3], "\nDuration Booked:", info[4])
                    else:
                        print("No booking history found.")
        find.close()
    except:
        print("This file cannot be opened")


def saveCustomerPayment(username):
    found = False
    total = 0
    try:
        booking = open('customer_bookings.txt', 'r')
        car = open('car_details.txt', 'r')
        lines = booking.readlines()
        cars = car.readlines()
        for line in lines:
             for details in cars:
                 info = line.rstrip().split('\t')
                 detail = details.rstrip().split('\t')
                 if username == info[0]:
                    found = True
        if (found == True):
            price = int(detail[4])
            duration = int(info[4])
            amount = int(price * duration)
            total += amount
        else:
            print("No booking found")
            registeredUserPage(username)
        car.close()
        booking.close()
        print('Total: RM', total)
        
        print("Enter (1) to continue proceed to payment")
        print("Enter (0) to back to main oage")
        con = int(input("Enter your choice: "))

        if con == "":
            return False
        else:
            if con == 1:
                print("Please make your payment to this bank account.")
                print("---------------------------------------------------------")
                print("Bank: Maybank")
                print("Bank Account Number: 1290 1382 8210")
                print("Account Holder Name: Super Car Rental Service")
                print("---------------------------------------------------------")

                payment = open('customer_payments.txt', 'a')
                bankNum = input("Enter your bank account number: ")
                exp = input("Enter expired date: ")
                cvv = input("Enter CVV: ")
                date = input("Enter today's date [YYYY/MM/DD]: ")
                payment.write(username + '\t' + total + '\t' + bankNum + '\t' + exp + '\t' + cvv + '\t' + date + '\n')     
                payment.close()
    except:
        print('This file cannot be opened')


def printCustomerPayment():
    try:
        payment = open('customer_payments.txt', 'r')
        lines = payment.readlines()
        for line in lines:
            info = line.rstrip().split('\t')
            print("\nCustomer Username:", info[0], "\nTotal:", info[1], "\nBank Number:", info[2], "\nExpired Date:", info[3], "\nCVV:", info[4], "\nDate:", info[5])
            print("\n")
        payment.close()
    except:
        print("This file cannot be opened")


def searchCustomerPayment():
    search = input("Enter customer USERNAME to start searching: ")
    try:
        fhand = open('customer_payments.txt', 'r')
        lines = fhand.readlines()
        for line in lines:
            info = line.rstrip().split('\t')
            if search != info[0]:
                continue
            elif search == info[0]:
                print("\nCustomer Username:", info[0], "\nTotal:", info[1], "\nBank Number:", info[2], "\nExpired Date:", info[3], "\nCVV:", info[4], "\nDate:", info[5])
            else:
                print("Information NOT FOUND in customer payment.")
                option = input("[Press 'X' to terminate and back to admin page] or [Press 'ENTER' to continue]")
                if (option == 'X' or option == 'x'):
                    print('\n-------------------You will be leaving customer payment searching page ------------------- ')
                    adminPage()
                elif (option == ''):
                    searchCustomerPayment()
                else:
                    adminPage()
        fhand.close()
    except:
        print("This file cannot be opened")


##def userRegistrationPage():
##    print("Please enter following personal details to register as a member in Super Car Rental Service")
##    customerDetails()
##    print()
##    print("************ Congratulations! You have been registered as a member now! *************")
##    print("You are required to login before proceeding to next page")
##    print()
##    customerLogin()

homePage()
