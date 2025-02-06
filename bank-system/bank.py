import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your mysql workbench password",
    database="bank_system"
)
cursor = conn.cursor()

# Create account
def create_account():
    name = input("Enter your name: ")
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, 0))
    conn.commit()
    print("Account created successfully!")

# Deposit money
def deposit():
    acc_no = input("Enter your account number: ")
    amount = float(input("Enter deposit amount: "))
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, acc_no))
    conn.commit()
    print(f"Successfully deposited {amount}")

# Withdraw money
def withdraw():
    acc_no = input("Enter your account number: ")
    amount = float(input("Enter withdrawal amount: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (acc_no,))
    balance = cursor.fetchone()[0]

    if amount > balance:
        print("Insufficient funds!")
    else:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, acc_no))
        conn.commit()
        print(f"Successfully withdrawn {amount}")

# Check balance
def check_balance():
    acc_no = input("Enter your account number: ")
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (acc_no,))
    balance = cursor.fetchone()
    if balance:
        print(f"Your balance: {balance[0]}")
    else:
        print("Account not found!")

# Transfer money
def transfer():
    sender = input("Enter your account number: ")
    receiver = input("Enter recipient's account number: ")
    amount = float(input("Enter amount to transfer: "))

    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (sender,))
    sender_balance = cursor.fetchone()[0]

    if sender_balance < amount:
        print("Insufficient balance!")
    else:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, sender))
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, receiver))
        conn.commit()
        print(f"Successfully transferred {amount}")

# Main menu
def main():
    while True:
        print("\nBANK MANAGEMENT SYSTEM")
        print("1️. Create Account")
        print("2️. Deposit Money")
        print("3️. Withdraw Money")
        print("4️. Check Balance")
        print("5️. Transfer Money")
        print("6️. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer()
        elif choice == "6":
            print("Thank you for using the bank system!")
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
