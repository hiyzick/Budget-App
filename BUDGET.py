class Budget:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.expenditure = 0
    
  def get_balance(self):
    print(f"{self.name} has ₦{self.balance}.")
    return self.balance
   
  def deposit(self):
    amount = int(input("Enter amount: \n"))
    self.balance  += amount
    print(f"₦{amount} added to {self.name}.")
  
  def withdraw(self):
    amount = int(input("Enter amount:\n"))
    
    if self.balance >= amount:
      
      if amount >= 100:
        self.balance -= amount 
        self.expenditure += amount 
        
      else:
        print("You can't take less than ₦100.")
        exit() 
    else:
      print("Insufficient balance.")
  
  
class Food(Budget):
  def __init__(self):
    super().__init__("Food")
    
      
food = Food()
food.deposit()
food.get_balance()
  