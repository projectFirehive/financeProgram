import json

def save():
    global inboundMoney
    global outboundMoney
    #global savingsContributions
    with open('inboundMoney.json', 'w') as inbound:
        json.dump(inboundMoney, inbound)
    with open('outboundMoney.json', 'w') as outbound:
        json.dump(outboundMoney, outbound)
    #with open('savingsContributions.json', 'w') as savings:
        #json.dump(savingsContributions, savings)

def load():
    global inboundMoney
    global outboundMoney
    #global savingsContributions
    with open('inboundMoney.json', 'r') as inbound:
        inboundMoney = json.load(inbound)
    with open('outboundMoney.json', 'r') as outbound:
        outboundMoney = json.load(outbound)
    #with open('savingsContributions.json', 'r') as savings:
        #savingsContributions = json.load(savings)

inboundMoney = {}
outboundMoney = {}

load()

#totalMoneyIn = (sum(inboundMoney.values()))
#totalMoneyOut = (sum(outboundMoney.values()))
#savingsContributions = {'Savings Account': 100, 'ISA': 50, 'Premium Bonds': round(((totalMoneyIn - totalMoneyOut) / 3))}
#netMoney = (totalMoneyIn-totalMoneyOut)

def topMenuFunc():
    topMenu = input('What would you like to do?\n1. Manage Inbound Money\n2. Manage Outbound Money\n3. Manage Savings\n4. Exit Program\n')
    if topMenu == '1':
        inboundMenuFunc()
    elif topMenu == '2':
        outboundMenuFunc()
    #elif topMenu == '3':
        #savingsMenuFunc()
    elif topMenu == '4':
        exit(0)
    else:
        print('Invalid entry, please try again')
        topMenuFunc()


def inboundMenuFunc():
    inboundMenu = input('What would you like to do?\n1. View Inbound Money\n2. Add Inbound Money\n3. Remove Inbound Money\n4. Modify Inbound Money\n5. Back\n')
    if inboundMenu == '1':
        print(inboundMoney.items())
        inboundMenuFunc()
    elif inboundMenu == '2':
        inboundMoney.update({input('Please enter the name of the new item: '): int(input('Please enter the value of the new item: '))})
        save()
        inboundMenuFunc()
    elif inboundMenu == '3':
        inboundMoney.pop(input('Please enter the name of the item you wish to remove: '))
        save()
        inboundMenuFunc()
    elif inboundMenu == '4':
        item = input('Please enter the name of the item you wish to modify: ')
        value = int(input('Please enter the new value of the item: '))
        inboundMoney[item] = value
        save()
        inboundMenuFunc()
    elif inboundMenu == '5':
        topMenuFunc()
    else:
        print('Invalid entry, please try again')
        inboundMenuFunc()


def outboundMenuFunc():
    outboundMenu = input('What would you like to do?\n1. View Expenses\n2. Add Expense\n3. Remove Expense\n4. Modify Expense\n5. Back\n')
    if outboundMenu == '1':
        print(outboundMoney.items())
        outboundMenuFunc()
    elif outboundMenu == '2':
        outboundMoney.update({input('Please enter the name of the new item: '): int(input('Please enter the value of the new item: '))})
        outboundMenuFunc()
        save()
    elif outboundMenu == '3':
        outboundMoney.pop(input('Please enter the name of the item you wish to remove: '))
        save()
        outboundMenuFunc()
    elif outboundMenu == '4':
        item = input('Please enter the name of the item you wish to modify: ')
        value = int(input('Please enter the new value of the item: '))
        outboundMoney[item] = value
        save()
        outboundMenuFunc()
    elif outboundMenu == '5':
        topMenuFunc()
    else:
        print('Invalid entry, please try again')
        outboundMenuFunc()



topMenuFunc()