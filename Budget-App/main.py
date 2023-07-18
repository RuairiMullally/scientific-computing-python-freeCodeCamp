class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = list()

  def __str__(self):
    masterString = self.category.center(30, '*')

    for record in self.ledger:
      masterString += f"\n{record['description'][:23]:23}{record['amount']:7.2f}"
       
    masterString += f"\nTotal: {str(self.get_balance())}"
    return masterString

  
    
  def get_balance(self):
    balance = 0
    for element in self.ledger:
      balance = balance + element["amount"]
    return balance

  def check_funds(self, amount):
    count = self.get_balance()
    if amount > count:
      return False
    else: return True

  

  def deposit(self, amount, description=None):

    if description == None:
      description = ''
    dict = {"amount": amount, "description": description}
    self.ledger.append(dict)

  def withdraw(self, amount, description=None):
    if description == None:
      description = ''

    if self.check_funds(amount):
      amount = -amount
      dict = {"amount": amount, "description": description}
      self.ledger.append(dict)
      return True
    else: return False
      

  def transfer(self, amount, otherCat):
    if self.check_funds(amount):
      description = f"Transfer to "+otherCat.category
      self.withdraw(amount, description)
      description = "Transfer from "+self.category
      otherCat.deposit(amount, description)
      return True
    else: return False



def create_spend_chart(categories):
  masterString = "Percentage spent by category\n"
  values = list()
  total =0
  percentages = list()
  labels = list()

  for category in categories:
    labels.append(category.category)
    spent = 0
    for i in category.ledger:
      if i['amount'] <0:
        spent += i['amount']
      values.append(spent)

  for value in values:
    total += value

  for j in values:
    percentages.append(round((j/total)*100, -1))
    
  k = 100
  while k >=0 :
    masterString += f"{k:3}|"
    for elem in percentages:
      if elem >= k:
        masterString += ' o '
      else: masterString += '   '
    masterString += '\n'
    k-=10
  masterString += '    '
  for elem in percentages:
    masterString += '---'
  masterString += '-\n    '

  
  for p in range(len(max(labels , key = len))):
    for q in range(len(labels)):
      try: 
        masterString += f' {labels[q][p]} '
      except:
        masterString += f'   '
    masterString += '\n    '

  print(masterString)
  return masterString
      
