#Python based ATM's workflow
class Atm:

      # Total Atm Accounts.
      total_atm_holder = 0
      def __init__(self):
            # initializing file handling with  Account balance file and Password file
 
            self.bank_balance = "Atm Management Project/balance.txt"
            self.password = "Atm Management Project/password.txt"
            Atm.total_atm_holder +=1


      def check_balance(self):
            # check balance using file handling method.
            try:
                  with open(self.bank_balance, 'r') as f:
                        balance = f.read()
                  if not balance:
                        print("Your Account Is Empty.")
                  else:
                        return(f"current balance is : {balance}")
            except Exception as e:
                  print(f"An error occurred while checking balance: {e}")
                  return None


      def withdraw(self,withdraw_money):
            # withdraw money using file handling method. According to conditions used some if/else statement.
            try:
                  with open(self.bank_balance,'r') as b:
                        money = b.read()
                  if not money:
                        print("\bInsufficient Balance.\b")
                  else:
                        convertmoney = int(money)
                        if withdraw_money <= convertmoney:
                              saved_money1 = convertmoney - withdraw_money
                              with open(self.bank_balance,'w') as balance:
                                    balance.write(str(saved_money1))
                              return f"Your Money has Successfully Debited From Your Account.\nYour Current Ballance is {saved_money1}"
                        else:
                              return f"\bWithdraw money is more than your Balance.\nYour Balance is {money}.Try to add more.\b"
            except Exception as e:
                  return f'An error occurred while withdrawing money: {e}'


      def deposit(self,money):
            # deposit money using file handling method. According to conditions used some if/else statement.
            try:
                  with open(self.bank_balance,'r') as data:
                        ndata = data.read()
                  if not ndata:
                        with open(self.bank_balance,'w') as data:
                              data.write(str(money))
                        cur_balance = money
                        return f"your money {money} is successfully deposit.\nYour current balance is {cur_balance}."
                  else:
                        data1 = int(ndata)
                        available_balance = data1 + money
                        with open(self.bank_balance,'w') as data:
                              data.write(str(available_balance))
                        return f"your cash has successfully deposited in your account.\n Your Current Money Is {available_balance}"
            except Exception as e:
                  return f'An error occurred while depositing money: {e}'

      def atm_password(self,pass1):
            # Take input from user and check password if matched then perform all operations of atm.

            with open(self.password,'r') as f:
                  store_password = f.read()
                  if pass1 == int(store_password):
                        return True
                  else :
                        print("Wrong Password.")


      def reset_password(self,new_password):
            # reset password 
            try:  
                  with open(self.password,'w') as file_pass:
                        file_pass.write(new_password)
                  return "Your password has been successfully changed."
            except Exception as e:
                  return f"An error occurred while resetting password: {e}"

      def check(self): 
            # check password
            with open(self.password,'r') as file:
                  text = file.read()
            return f"your current password is {text}"

                  
atm = Atm()
def greet(fx):
      def welcome():
            print("welcom to ATM.")
            fx()
            print("Thanks for using ATM.")
      return welcome

@greet
def main():
      customer = str(input("enter your name:\n"))
      atm_pass = int(input("enter your password.\n"))
      if atm.atm_password(atm_pass):
            while True:
                  print("1. Check Balance.\n2. Withdraw Money.\n3. Deposit Money.\n4. Reset Your PASSWORD.\n5. Check your current PASSWORD.\n6. Exit.")
                  print("Select an option.")
                  choice = int(input("Enter Your Choice."))
                  if choice == 1:
                        print(atm.check_balance())
                        print("-"*60)

                  elif choice ==2:
                        try:
                              withdraw_money = int(input("Enter Amount.\n"))
                              print(atm.withdraw(withdraw_money))
                        except ValueError:
                              print("Please enter a valid number.")
                        print("-"*60)
                  elif choice ==3:
                        try:
                              money = int(input("Enter Your Amount."))
                              print(atm.deposit(money))
                        except ValueError:
                              print("Please enter a valid number.")
                        print("-"*60)
                  elif choice ==4:
                        new_password = str(input("Enter your new PIN."))
                        print(atm.reset_password(new_password))
                        print("-"*60)
                  elif choice ==5:
                        print(atm.check())
                        print("-"*60)
                  elif choice == 6:
                        break
main()