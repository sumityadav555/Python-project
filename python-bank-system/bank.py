import json
import os

BANK_FILE = 'bank_data.json'

def load_data():
    if not os.path.exists(BANK_FILE):
        return {}
    
    with open(BANK_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(BANK_FILE, 'w') as file:
        json.dump(data, file, indent = 4)

def create_account():
    data = load_data()
    name = input("Enter your name: ")
    account_number = input("Enter a unique account number: ")

    if account_number in data:
        print("Account number already exists. Try again!")
        return 

    data[account_number] = {
        'name' : name,
        'balance' : 0
    }
    save_data(data)
    print(f"Account created successfully for {name}!")

def deposit():
    data = load_data()
    account_number = input("Enter your account number: ")

    if account_number not in data:
        print("Account not found!")
        return
    
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Invalid deposit amount!")
        return 

    data[account_number]['balance'] += amount
    save_data(data)
    print(f" successfully depsited {amount}. New Balance: {data[account_number]['balance']}")

def withdraw():
    data = load_data()
    account_number = input("Enter your account number: ")

    if account_number not in data:
        print("Account not found!")
        reutrn 

    amount = float(input("Enter withdrawl amount: "))
    if amount <= 0 or amount > data[account_number]['balance']:
        print("Invalid withdrawl amount!")
        return

    data[account_number]['balance'] -= amount
    save_data(data)
    print(f"Suceessfully withdrawl {amount}. New Balance: {data[account_number]['balance']}")

def check_balance():
    data = load_data()
    account_number = input("Enter your account number: ")

    if account_number not in data:
        print("Account not found!")

    print(f"Account Balance: {data[account_number]['balance']}")

def transfer_money():
    data = load_data()
    sender = input("Enter account number: ")
    receiver = input("Enter recipient's account number: ")

    if sender not in data or receiver not in data:
        print("One or both account numbers are invalid!")
        return 

    amount = float(input("Enter amount to transfer: "))
    if amount <= 0 or amount > data[sender]['balance']:
        print("Invalid transfer amount!")

    data[sender]['balance'] -= amount
    data[receiver]['balance'] += amount
    save_data(data)
    print(f"Suceesfully transfered {amount} from {sender} to {receiver}")

def main():
    while True:
        print("\n Bank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdrawl Money")
        print("4. Check Balance")
        print("5. Transfer Balance")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            transfer_money()
        elif choice == '6':
            print("Thank you for using the bank system!")
            break
        else:
            print("Invalid option, Try again!")

if __name__ == "__main__":
    main()







