import json
def load_expenses():
   with open("expenses.json","r") as file :
      return json.load(file)
def save_expenses(expenses):
     with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)

def add_expense(expenses):
     print ("lets add your expense ")
     try:
        amount =  float(input (" enter the amount to add  "))
        if amount<=0 :
            print("please enter the valid amount")
            return
     except ValueError:
         print("please enter a valid number ")
         return
     category = input("enter the category of the expense  ").strip()
     description=input("enter the description of the expense   ").strip()
     if not category or not description:
         print("category and description cannot be empty")
         return
     expense  = {
         "amount":  amount,
         "category": category,
         "description": description,

      }
     expenses.append(expense)
     save_expenses(expenses)
     print("expense has been added   ")
 

def delete_expense(expenses):
      if len(expenses)==0:
         print("NO EXPENSE TO DELETE ")
      else:
          print("\n your expense ")
          for i , expense in enumerate(expenses, start=1):
              print(f"{i}.{expense['amount']}- {expense['category']}-{expense['description']}")
      
          try:
              delete =int(input("enter the expense number  to be delete" ))
              if delete <1 or delete > len(expenses):
                   print("invalid expense number ")
                   return
              expenses.pop(delete-1)
              save_expenses(expenses)
              print("expense deleted successfully")
          except ValueError:
              print("please enter valid value")

def view_expenses(expenses):
    print("you can view the expense")
    if len(expenses)==0:
       print("no expense found ")
       return

    else :
       print("\n your expenses")
       for i,expense in enumerate(expenses,start=1):
          print(f"\n{i}.amount : {expense['amount']}")
          print(f"category : {expense['category']}")
          print(f"description : {expense['description']}")

def total_spending(expenses):
    if len(expenses)==0:
       print("no expense found")
       return
    else :
       total = sum(expense["amount"]for expense in expenses)
       print(f"total spending is : {total}")
      
def category_summary(expenses):
    if len(expenses)==0:
       print ("no expense found")
       return
    
    else :
       category_total={}
       for expense in expenses:
          category = expense["category"]
          amount=expense["amount"]
          if category in category_total:
             category_total[category] +=amount
          else :
             category_total[category] =amount
       print("\n category summary")
       for category , total in category_total.items():
          print(f"{category}:{total}")
def main():
  expenses = load_expenses()
  while True:
      print("="*35)
      print("      Expense tracker")
      print("="*35)

      print("MENU")
      print("1. Add expense")
      print(" 2.delete the expense")
      print(" 3.view the expense")
      print("4. total spending ")
      print("5. category summary")
      print("6.exit")
      choice = input("enter your choice no   "  )
      if choice == "1":
            add_expense(expenses)

      elif choice == "2":
            delete_expense(expenses)

      elif choice == "3":
            view_expenses(expenses)

      elif choice == "4":
            total_spending(expenses)

      elif choice == "5":
            category_summary(expenses)

      elif choice == "6":
            print("=" * 35)
            print("        Thank you!")
            print("=" * 35)
            break

      else:
            print("Invalid choice. Please select 1-6.")
main()
     