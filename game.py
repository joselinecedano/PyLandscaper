print('HW #24 Python Landscaper')

bank = 0
my_tools = [ {'tool': "Teeth", 'cost': 0, 'earn': 1, } ]
tool_shop = [
  {'tool': "Rusty Scissors", 'cost': 5, 'earn': 5,},    
  {'tool': "Old Timey Push Lawnmower", 'cost': 25, 'earn': 50,},
  {'tool': "Fancy Battery-Powered Lawnmower", 'cost': 250, 'earn': 100,},
  {'tool': "Starving Students", 'cost': 500, 'earn': 250}
]
  
''' section 1: Shop or Work prompt '''
def main_prompt():
  print('\n\nWelcome to Landscaper : Python Edition!\n\nWould you like to: \na) work to earn money \n          OR \nb) go to the Tool Shop and buy tools')
  main_resp = input("\nAnswer : ").lower()
  return main_resp

# this will handle the response to the main prompt
def landscaper_mp():
  prompt_answer = main_prompt()
  if prompt_answer == 'a': 
    # put a function here that will deal with a player wanting to work
    toolToUse()
  elif prompt_answer == 'b':
    # put a function here that will deal with user wanting to buy a tool
    toolToBuy()
  else:
    # error handling in case the put an invalid response and have them to try again
    print('Your answer was not valid. \nPlease try again ')
    landscaper_mp()
    
''' Work / Money++ '''

''' section 2: User wants to work '''
def workTool():
  print('\n\nWhat tool would you like to use today? \na) Teeth \nb) Rusty Scissors \nc) Old Timey Push Lawnmower \nd) Fancy Battery-Powered Lawnmower \ne) Starving Students ') 
  tool_resp = input('\nAnswer : ').lower() 
  return tool_resp 
  
def toolToUse(): 
  tool_choice = workTool()
  if tool_choice == 'a' and 'Teeth'in [tool['tool'] for tool in my_tools]: 
    # function for earning money using teeth
    oneDollar()
    landscaper_mp()
  elif tool_choice == 'b' and 'Rusty Scissors'in [tool['tool'] for tool in my_tools]:
    fiveDollars()
    landscaper_mp()
  elif tool_choice == 'c' and 'Old Timey Push Lawnmower'in [tool['tool'] for tool in my_tools]: 
   fiftyDollars()
   landscaper_mp()
  elif tool_choice == 'd' and 'Fancy Battery-Powered Lawnmower'in [tool['tool'] for tool in my_tools]: 
    hundredDollars()
    landscaper_mp()
  elif tool_choice == 'e' and 'Starving Students'in [tool['tool'] for tool in my_tools]: 
    twoFiftyDollars()
  else: 
    print('\nYour answer was not valid OR you do not currently own the tool you have chosen! \nPlease try again. ')
    landscaper_mp()


''' section 3: Making money '''
def oneDollar():
  # use global so Python knows to use the bank variable we defined above rather than creating a new local one here
  global bank
  global my_tools
  while True:
    bank +=1
    print(f'\nYou have worked hard today earning $1 cutting grass with your Teeth. \nYou now have ${bank} in your account.')
    if bank >= 5:
      print('\nRusty Scissors are now available! Upgrade your tools to earn money faster! ')
      break
      
def fiveDollars():
  global bank
  while True:
    bank +=5
    print(f'\nYou have worked hard today earning $5 cutting grass with your Rusty Scissors. \nYou now have ${bank} in your account.')
    if bank >= 25:
      print('\nOld Timey Lawnmower is now available! Upgrade your tools to earn money faster! ')
      break
      
def fiftyDollars():
  global bank
  while True:
    bank +=50
    print(f'\nYou have worked hard today earning $25 cutting grass with your Old Timey Push Lawnmower. \nYou now have ${bank} in your account.')
    if bank >= 250:
      print('\nFancy Battery Powered Lawnmower is now available! Upgrade your tools to earn money faster! ')
      break
      
def hundredDollars():
  global bank
  while True:
    bank +=100
    print(f'\nYou have worked hard today earning $100 cutting grass with your Fancy Battery-Powered Lawnmower. \nYou now have ${bank} in your account.')
    if bank >= 500:
      print('\nStarving Students is now available! Upgrade your tools to earn money faster! ')
      break
      
def twoFiftyDollars():
  global bank
  while True:
    bank +=250
    print(f'\nYou have worked hard today earning $250 cutting grass with your Starving Students. \nYou now have ${bank} in your account.')
    if bank >= 1000:
      print('\nCongrats!!! You have just beat Landscaper : Python Edition! ')
      break

''' Buy / Money-- '''

''' section 4: User wants to buy tools '''
def buyTool():
  print('\n\nWhat tool would you like to buy today? \na) Teeth \nb) Rusty Scissors \nc) Old Timey Push Lawnmower \nd) Fancy Battery-Powered Lawnmower \ne) Starving Students ') 
  tool_resp = input('\nAnswer : ').lower() 
  return tool_resp 

def toolToBuy():
  global bank
  purch_choice = buyTool()
  if purch_choice == 'a' and bank >= 0:
    print("\nYou have chosen Teeth! Mow lawns and earn more money to upgrade your tools!")
    landscaper_mp()
  elif purch_choice == 'b' and bank >= 5:
    my_tools.append(tool_shop[0])
    bank -=5
    print(f"\nYou have bought Rusty Scissors! Mow lawns and earn more money to upgrade your tools! \nYour account is now at ${bank}.")
    landscaper_mp()
  elif purch_choice == 'c' and bank >= 25:
    my_tools.append(tool_shop[1])
    bank -=25
    print(f"\nYou have bought Old Timey Push Lawnmower! Mow lawns and earn more money to upgrade your tools! \nYour account is now at ${bank}.")
    landscaper_mp()
  elif purch_choice == 'd' and bank >= 250:
    my_tools.append(tool_shop[2])
    bank -=250
    print(f"\nYou have bought Fancy Battery-Powered Lawnmower! Mow lawns and earn more money to upgrade your tools! \nYour account is now at ${bank}.")
    landscaper_mp()
  elif purch_choice == 'e' and bank >= 500:
    my_tools.append(tool_shop[3])
    bank -=500
    print(f"\nYou have bought Starving Students! Mow lawns and earn more money to upgrade your tools! \nYour account is now at ${bank}.")
    landscaper_mp()
  else:
    print('\nYour answer was not valid OR you do not currently have the funds to buy this item! Please try again.')
    toolToBuy()

landscaper_mp()
