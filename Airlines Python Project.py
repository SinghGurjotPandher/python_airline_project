# SEAT STATUS UPDATE
# First Class Seat Status Update
First_Class_Seat = ['OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN']
# Coach Class Seat Status Update
Coach_Class_Seat = ['OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN','OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN']

# UPDATING STATUS
# Update Status First Class Seat
def first_list(firstIndexNum, statusUpdate):
    First_Class_Seat[firstIndexNum] = statusUpdate
    return
# Update Status Coach Class Seat
def coach_list(coachIndexNum, updateStatus):
    Coach_Class_Seat[coachIndexNum] = updateStatus
    return

# APPLYING DISCOUNT TO TICKET COST BASED ON AGE
def discount_cost(userAge, ticketCost):
    # Discount for Young and Elderly
    if userAge < 7 or userAge > 64:
        discountApply = 20 / 100 * ticketCost
        ticketCost = ticketCost - discountApply
        return ticketCost
    # No Discount for Not Young and Elderly
    elif userAge > 6  and userAge < 65:
        return ticketCost
    return

# COMPUTE TAX PER SEAT
def ticket_tax(PRICE):
    CALIFORNIA_TAX = 9.0 # California Tax Application Rate
    seatTax = 9.0 / 100 * PRICE # Apply California Tax to the Ticket Price
    return seatTax

# PRINTING INFORMATION OF SUCCESSFUL BOOKING
def name_change(name, seatNumber, moneyChangeTaken):
    print("You booked seat",seatNumber,".") # Confirmation of Name and Seat Booked
    if moneyChangeTaken > 0:
        print(name,"received a change of $",moneyChangeTaken,".") # Displaying Change Taken if Extra Money Paid
        return
    return

# GIVING CHANGE
def monetary_change(moneyChangeTaken):
    hundredBills = int(moneyChangeTaken / 100) # 100 Bills
    print("\nHundred Bill(s):              ", hundredBills)
    twentyBills = int((moneyChangeTaken - (hundredBills * 100)) / 20) # 20 Bills
    print("Twenty Bill(s):               ", twentyBills)
    fiveBills = int(((moneyChangeTaken) - (hundredBills * 100) - (twentyBills * 20)) / 5) # 5 Bills
    print("Five Bill(s):                 ", fiveBills) 
    oneBill = int(((moneyChangeTaken) - (hundredBills * 100) - (twentyBills * 20) - (fiveBills * 5)) / 1) # 1 Bills
    print("One Bill(s):                  ", oneBill)
    quarterDollar = int(((moneyChangeTaken) - (hundredBills * 100) - (twentyBills * 20) - (fiveBills * 5) - (oneBill * 1)) / 0.25) # 0.25 Dollar
    print("Quarter(s):                   ", quarterDollar)
    dimesDollar = int(((moneyChangeTaken) - (hundredBills * 100) - (twentyBills * 20) - (fiveBills * 5) - (oneBill * 1) - (quarterDollar * 0.25)) / 0.10) # 0.10 Dollar
    print("Dime(s):                      ", dimesDollar)
    nickelsDollar = int(((moneyChangeTaken) - (hundredBills * 100) - (twentyBills * 20) - (fiveBills * 5) - (oneBill * 1) - (quarterDollar * 0.25) - (dimesDollar * 0.10)) / 0.05) # 0.05 Dollars
    print("Nickle(s):                    ", nickelsDollar)
    pennies = int(((moneyChangeTaken) - (hundredBills * 100) - (twentyBills * 20) - (fiveBills * 5) - (oneBill * 1) - (quarterDollar * 0.25) - (dimesDollar * 0.10) - (nickelsDollar * 0.05)) / 0.01) # 0.01 Dollars
    print("Penny or Pennies:             ", pennies, "\n")
    return

# CALLING CHANGE MODULE, BOOKING SEAT, OR DISPLAYING REFUSAL FOR FIRST CLASS
def monetary_processing_first(moneyPaid, orderTotal, name, seatNumber):
    if moneyPaid > orderTotal: # Statements for People who Paid More Than Needed
        openSeat = seatNumber - 1
        first_list(openSeat, name)
        print("\nCongratulations, seats booked.\nThank you for choosing Chaffey Airlines!")
        moneyChange = moneyPaid - orderTotal
        monetary_change(moneyChange)
        name_change(name, seatNumber, moneyChange)
        option_chosen_four()
        return
    elif moneyPaid == orderTotal: # Statements for People who Paid Equal Ammount to that of Needed
        openSeat = seatNumber - 1
        first_list(openSeat, name)
        print("\nCongratulations, seats booked.\nThank you for choosing Chaffey Airlines!")
        name_change(name, seatNumber, 0)
        option_chosen_four()
        return
    elif moneyPaid < orderTotal: # Statements for People who did not Paid Enough Money Needed for Booking
        print ("\nSorry, ticket cannot be given to you because the money you gave was less than that of required. Try again.\n")
        option_chosen_one()
    return
def monetary_processing_coach(moneyPaid, orderTotal, name, seatNumber):
    if moneyPaid > orderTotal: # Statements for People who Paid More Than Needed
        openSeat = seatNumber - 1
        coach_list(openSeat, name)
        print("Congratulations, seats booked.\nThank you choosing Chaffey Airlines!")
        moneyChange = moneyPaid - orderTotal
        monetary_change(moneyChange)
        name_change(name, seatNumber, moneyChange)
        option_chosen_four()
        return
    elif moneyPaid == orderTotal: # Statements for People who Paid Equal Ammount to that of Needed
        openSeat = seatNumber - 1
        coach_list(openSeat, name)
        print("Congratulations, seats booked.\nThank you choosing Chaffey Airlines!")
        name_change(name, seatNumber, 0)
        option_chosen_four()
        return
    elif moneyPaid < orderTotal: # Statements for People who did not Paid Enough Money Needed for Booking
        print ("\nSorry, ticket cannot be given to you because your money given was less than that of required. Try again.\n")
        option_chosen_two()
        return
    return

# OPTION 1 CHOSEN
# First-Class Reservation
def option_chosen_one():
    userName = str(input("Enter your name: "))
    see_options()
    seatFirst = int(input("Seat to book: "))
    seatBook = seatFirst - 1
    PRICE = 500
    if First_Class_Seat[seatBook] == "OPEN": # If seat is open, then follow these statements
        taxApplied = ticket_tax(PRICE)
        ticketCost = taxApplied + PRICE
        userAge = int(input("Enter your age: "))
        ticketCostFinal = discount_cost(userAge, ticketCost)
        print("Total cost: ", ticketCostFinal,"\n")
        moneyGiven = float(input("Enter the money for paying: "))
        monetary_processing_first(moneyGiven, ticketCostFinal, userName, seatFirst)
    else: # If the seat is not open, then display refusal
        print("Sorry, seat already booked.\n")
        againTry = input("Do you want to still try to book for option 1 or do you want to get more options? For more options, type More Options, and for trying again for option 1, type Still Option 1.")
        if againTry == "More Options":
            main_module()
        elif againTry == "Still Option 1":
            option_choosen_one()
    return

# OPTION 2 CHOSEN
# Second-Class Reservation
def option_chosen_two():
    yourName = str(input("Enter your name: "))
    see_options()
    seatCoach = int(input("Seat to book: "))
    paraBook = seatCoach - 1
    COACH_PRICE = 199
    if Coach_Class_Seat[paraBook] == "OPEN": # If seat is open, then follow these statements
        applyTax = ticket_tax(COACH_PRICE)
        costTicket = applyTax + COACH_PRICE
        ageUser = int(input("Enter your age: "))
        finalTicketCost = discount_cost(ageUser, costTicket)
        print("Total cost: ", finalTicketCost,"\n")
        givenMoney = float(input("Enter the money for paying: "))
        monetary_processing_coach(givenMoney, finalTicketCost, yourName, seatCoach)
    else: # If seat not open, then follow these statements
        print("Sorry, seat already booked. Try again.\n")
        tryAgain = input("Do you want to still try to book for option 2 or do you want to get more options? For more options, type More Options, and for trying again for option 2, type Still Option 2. ")
        if tryAgain == "More Options":
            main_module()
        elif tryAgain == "Still Option 2":
            option_chosen_two
    return

# Ask the User to See or Not See the Available and Booked Seats          
def see_options():
    seeSeats = input("Before booking a seat, do you want to see the available and booked seats? Type See or Not See ")
    if seeSeats == "See":
        option_chosen_four()
    return

# OPTION 3 CHOSEN
# Change-Existing Reservation
def option_chosen_three():
    classChange = str(input("Which reservation option would you like to change? First Class Seat or Coach Class Seat "))
    if classChange == "First Class Seat": #Replacing Requested First Class Seat to Open Status
        see_options()
        changeSeat = int(input("Enter the seat number to change from: "))
        openSeat = changeSeat - 1
        first_list(openSeat, "OPEN")
    elif classChange == "Coach Class Seat": #Replacing Requested Coach Class Seat to Open Status
        see_options()
        openSeat = int(input("Enter the seat number to change from: "))
        seatOpen = openSeat - 1
        coach_list(seatOpen, "OPEN")
    else:
        option_chosen_three()
    rebooking()
    return

# Rebooking 
def rebooking():
    choiceRebook = str(input("Do you want to rebook for First Class Seat or Coach Class Seat? "))
    if choiceRebook == "First Class Seat": #Rebooking for First Class Seat
        first_reservation_check()
    elif choiceRebook == "Coach Class Seat": #Rebooking for Coach Class Seat
        coach_reservation_check()
    else:
        rebooking()
    return
        

# OPTION 4 CHOSEN
# View Available and Booked Seats
def option_chosen_four():
    print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> | FIRST CLASS SEATS | <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>") # First Class Seats
    print("SEAT 1: ",First_Class_Seat[0][0:12], "     ", "SEAT 3: ",First_Class_Seat[2][0:12], "     ", "SEAT 5: ",First_Class_Seat[4][0:12], "    ", "SEAT 7: ",First_Class_Seat[6][0:12])
    print("SEAT 2: ",First_Class_Seat[1][0:12], "     ", "SEAT 4: ",First_Class_Seat[3][0:12], "     ", "SEAT 6: ",First_Class_Seat[5][0:12], "    ", "SEAT 8: ",First_Class_Seat[7][0:12],"\n")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> | COACH CLASS SEATS | <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>") # Coach Class Seats
    print("SEAT 1: ",Coach_Class_Seat[0][0:12], "              ", "SEAT 11: ",Coach_Class_Seat[10][0:12], "              ", "SEAT 21: ",Coach_Class_Seat[20][0:12], "              ", "SEAT 31: ",Coach_Class_Seat[30][0:12])
    print("SEAT 2: ",Coach_Class_Seat[1][0:12], "              ", "SEAT 12: ",Coach_Class_Seat[11][0:12], "              ", "SEAT 22: ",Coach_Class_Seat[21][0:12], "              ", "SEAT 32: ",Coach_Class_Seat[31][0:12])
    print("SEAT 3: ",Coach_Class_Seat[2][0:12], "              ", "SEAT 13: ",Coach_Class_Seat[12][0:12], "              ", "SEAT 23: ",Coach_Class_Seat[22][0:12], "              ", "SEAT 33: ",Coach_Class_Seat[32][0:12])
    print("SEAT 4: ",Coach_Class_Seat[3][0:12], "              ", "SEAT 14: ",Coach_Class_Seat[13][0:12], "              ", "SEAT 24: ",Coach_Class_Seat[23][0:12], "              ", "SEAT 34: ",Coach_Class_Seat[33][0:12])
    print("SEAT 5: ",Coach_Class_Seat[4][0:12], "              ", "SEAT 15: ",Coach_Class_Seat[14][0:12], "              ", "SEAT 25: ",Coach_Class_Seat[24][0:12], "              ", "SEAT 35: ",Coach_Class_Seat[34][0:12])
    print("SEAT 6: ",Coach_Class_Seat[5][0:12], "              ", "SEAT 16: ",Coach_Class_Seat[15][0:12], "              ", "SEAT 26: ",Coach_Class_Seat[25][0:12], "              ", "SEAT 36: ",Coach_Class_Seat[35][0:12])
    print("SEAT 7: ",Coach_Class_Seat[6][0:12], "              ", "SEAT 17: ",Coach_Class_Seat[16][0:12], "              ", "SEAT 27: ",Coach_Class_Seat[26][0:12], "              ", "SEAT 37: ",Coach_Class_Seat[36][0:12])
    print("SEAT 8: ",Coach_Class_Seat[7][0:12], "              ", "SEAT 18: ",Coach_Class_Seat[17][0:12], "              ", "SEAT 28: ",Coach_Class_Seat[27][0:12], "              ", "SEAT 38: ",Coach_Class_Seat[37][0:12])
    print("SEAT 9: ",Coach_Class_Seat[8][0:12], "              ", "SEAT 19: ",Coach_Class_Seat[18][0:12], "              ", "SEAT 29: ",Coach_Class_Seat[28][0:12], "              ", "SEAT 39: ",Coach_Class_Seat[38][0:12])
    print("SEAT 10: ",Coach_Class_Seat[9][0:12], "              ", "SEAT 20: ",Coach_Class_Seat[19][0:12], "              ", "SEAT 30: ",Coach_Class_Seat[29][0:12], "              ", "SEAT 40: ",Coach_Class_Seat[39][0:12],"\n")
    return

# OPTION 6 CHOSEN
# Display the First Available Option
def option_chosen_six():
    optionSearch = str(input("Do you want to search for First Class Seat or Coach Class Seat? "))
    if optionSearch == "First Class Seat":
        openSeatNum = First_Class_Seat.index("OPEN")
        numSeatOpen = openSeatNum + 1
        print("The first open seat is: ", numSeatOpen)
    elif optionSearch == "Coach Class Seat":
        seatOpenNum = Coach_Class_Seat.index("OPEN")
        numOpenSeat = seatOpenNum + 1
        print("The first open seat is: ", numOpenSeat)
    else:
        print("INVALID VALUE ENTERED. Try again.")
        option_chosen_six()
    return

# FIRST CLASS RESERVATIONS FILL CHECK MODULE
# Refuse Reservations if all Seats are Full for First-Class Seats
def first_reservation_check():
    if First_Class_Seat[0] != "OPEN" and First_Class_Seat[1] != "OPEN" and First_Class_Seat[2] != "OPEN" and First_Class_Seat[3] != "OPEN" and First_Class_Seat[4] != "OPEN" and First_Class_Seat[5] != "OPEN" and First_Class_Seat[6] != "OPEN" and First_Class_Seat[7] != "OPEN":
        print("No reservations can be made for first class because all seats are full.")
    else:
        option_chosen_one()
    return

# COACH CLASS RESERVATIONS FILL CHECK MODULE
# Refuse Reservations if all Seats are Full for Coach-Class Seats
def coach_reservation_check():
    if Coach_Class_Seat[0] != "OPEN" and Coach_Class_Seat[1] != "OPEN" and Coach_Class_Seat[2] != "OPEN" and Coach_Class_Seat[3] != "OPEN" and Coach_Class_Seat[4] != "OPEN" and Coach_Class_Seat[5] != "OPEN" and Coach_Class_Seat[6] != "OPEN" and Coach_Class_Seat[7] != "OPEN" and Coach_Class_Seat[8] != "OPEN" and Coach_Class_Seat[9] != "OPEN" and Coach_Class_Seat[10] != "OPEN" and Coach_Class_Seat[11] != "OPEN" and Coach_Class_Seat[12] != "OPEN" and Coach_Class_Seat[13] != "OPEN" and Coach_Class_Seat[14] != "OPEN" and Coach_Class_Seat[15] != "OPEN" and Coach_Class_Seat[16] != "OPEN" and Coach_Class_Seat[17] != "OPEN" and Coach_Class_Seat[18] != "OPEN" and Coach_Class_Seat[19] != "OPEN" and Coach_Class_Seat[20] != "OPEN" and Coach_Class_Seat[21] != "OPEN" and Coach_Class_Seat[22] != "OPEN" and Coach_Class_Seat[23] != "OPEN" and Coach_Class_Seat[24] != "OPEN" and Coach_Class_Seat[25] != "OPEN" and Coach_Class_Seat[26] != "OPEN" and Coach_Class_Seat[27] != "OPEN" and Coach_Class_Seat[28] != "OPEN" and Coach_Class_Seat[29] != "OPEN" and Coach_Class_Seat[30] != "OPEN" and Coach_Class_Seat[31] != "OPEN" and Coach_Class_Seat[32] != "OPEN" and Coach_Class_Seat[33] != "OPEN" and Coach_Class_Seat[34] != "OPEN" and Coach_Class_Seat[35] != "OPEN" and Coach_Class_Seat[36] != "OPEN" and Coach_Class_Seat[37] != "OPEN" and Coach_Class_Seat[38] != "OPEN" and Coach_Class_Seat[39] != "OPEN":
        print("No reservations can be made for coach class because all seats are full.")
    else:
        option_chosen_two()
    return

# Display Company's Information, Give Options, Call Modules, and Repeat until Option 5 Chosen (QUIT)
def main_module(): #MAIN
    print("                                 WELCOME TO CHAFFEY AIRLINES                               \n")
    print("         California Travel System 1.0 by Gurjot Singh Pandher, Himself, & Other Self         ") 
    # Available Options for Choosing
    print("\nOPTION 1: First Class Seat Reservation")
    print("OPTION 2: Coach Class Seat Reservation")
    print("OPTION 3: Existing Reservation Change")
    print("OPTION 4: Available and Booked Seat Display")
    print("OPTION 5: QUIT")
    print("OPTION 6: Search for First Open Seat")
    # Input the Choosen Option
    choosenOption = input("Enter an option as 1 or 2 or 3 or 4 or 5 or 6: ")
    # Run the loop until the user enters option 5.
    while choosenOption != "5":
        if choosenOption == "1":
            first_reservation_check()
        elif choosenOption == "2":
            coach_reservation_check()
        elif choosenOption == "3":
            option_chosen_three()
        elif choosenOption == "4":
            option_chosen_four()
        elif choosenOption == "6":
            option_chosen_six()
        else:
            print("\nINVALID OPTION. Option can be 1 or 2 or 3 or 4 or 5 or 6 only.\n")
        print("\n         California Travel System 1.0 by Gurjot Singh Pandher, Himself, & Other Self         \n")
        print("\nOPTION 1: First Class Seat Reservation")
        print("OPTION 2: Coach Class Seat Reservation")
        print("OPTION 3: Existing Reservation Change")
        print("OPTION 4: Available and Booked Seat Display")
        print("OPTION 5: QUIT")
        print("OPTION 6: Search for First Open Seat")
        choosenOption = input("Enter an option as 1 or 2 or 3 or 4 or 5 or 6: ")
    return

main_module() # Call the main module, which calls subsequent modules.
