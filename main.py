import json

def save():
    global inboundMoney
    global outboundMoney
    global savingsContributions
    with open('inboundMoney.json', 'w') as inbound:
        json.dump(inboundMoney, inbound)
    with open('outboundMoney.json', 'w') as outbound:
        json.dump(outboundMoney, outbound)
    with open('savingsContributions.json', 'w') as savings:
        json.dump(savingsContributions, savings)

def load():
    global inboundMoney
    global outboundMoney
    global savingsContributions
    with open('inboundMoney.json', 'r') as inbound:
        inboundMoney = json.load(inbound)
    with open('outboundMoney.json', 'r') as outbound:
        outboundMoney = json.load(outbound)
    #with open('savingsContributions.json', 'r') as savings:
        #savingsContributions = json.load(savings)

inboundMoney = {}
outboundMoney = {}

load()

totalMoneyIn = (sum(inboundMoney.values()))
totalMoneyOut = (sum(outboundMoney.values()))
savingsContributions = {'Savings Account': 100, 'ISA': 50, 'Premium Bonds': round(((totalMoneyIn - totalMoneyOut) / 3))}
print(list(savingsContributions.values()))