#Cash Register Program in Python
#Author: Ja'Quis Franklin
#Date: 02/14/2025
import math as Math
import time as Time
import getpass as Password

#Function to process payments
#Returns an The amount of change left
def processPayments(total: float) -> float:
    payment_Done = False
    while not payment_Done:
        print("Select Payment Type: ")
        print("[1]Cash")
        print("[2]Card")
        print("[3]Check")
        selection = input(("Make your selection: "))

        match selection :
            case "1":
                print("Enter Amount of cash given: ")
                print(f"[1]: ${total:.2f}")
                print(f"[2]: ${Math.ceil(total) + 10:.2f}")
                print(f"[3]: Custom Amount")
                
                cash_process = False
                while not cash_process:
                    select = input("Select: ")
                    match select:
                        case "1":
                            cash_process = True
                            payment_Done = True 
                            return total - total
                        case "2":
                            cash_process = True
                            payment_Done = True
                            return (Math.ceil(total) + 10) - total
                        case "3":
                            custom_amount = int(input("Enter Change: "))
                            if(custom_amount > total):
                                cash_process = True
                                payment_Done = True
                                return custom_amount - total
                            else:
                                payment_Done = True
                                cash_process = True
                                return total - custom_amount
                        case _:
                            print("Please Enter a 1 , 2,or 3")
                            continue
            case "2":
                selected = False
                while not selected:
                    select = input(("[D]ebit or [C]redit: "))
                    match select.lower().strip():
                        case "d":
                            Password.getpass("Enter your pin: ")
                            Time.sleep(1)
                            print("Processing...")
                            Time.sleep(2)
                            selected = True
                            payment_Done = True
                            return total - total
                        case "c":
                            Time.sleep(1)
                            print("Processing...")
                            Time.sleep(2)
                            selected = True
                            payment_Done = True
                            return total - total
                        case _:
                            print("Please Select C or D")
                            continue
            case "3":
                print("Entering Check...")
                Time.sleep(2)
                print("Check Read succesfully!!")
                Time.sleep(1)
                input("Sign your signature: ")
                Time.sleep(2)
                payment_Done = True
                return total - total
            case _:
                print("Please try again.")
                continue

#Main Function
def main():
    processed = False
    
    while not processed:
            #Error handling for the total
        try:
            total = float(input("Enter total: "))
            if total < 1:
                print("Total cannot be less than $1. Try again.")
                continue
        except:
            print("Value must be a number")
            
        change_left = processPayments(total)
        if change_left >= 1:
            print(f"Change = ${change_left:.2f}")
            print("Returning change...")
            Time.sleep(2)
            print("Payment Complete!! Have a Nice Day!!")
            processed = True
        else:
            print("Approved")
            Time.sleep(2)
            print("Payment Complete!! Have a Nice Day!!")
            processed = True

if __name__ == "__main__":
    main()