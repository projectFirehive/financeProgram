import os

dirName = 'financeProgram'
parentDir = 'C:\\Program Files (x86)'
path = os.path.join(parentDir, dirName)

os.mkdir(path)

#Change 'financeProgram.py' to 'financeProgram.exe' when complete and compiled
os.rename('financeProgram.py', r'C:\Program Files (x86)\financeProgram\financeProgram.py')

if not os.path.isfile(r'C:\Program Files (x86)\financeProgram\inboundMoney.json'):
    with open(r'C:\Program Files (x86)\financeProgram\inboundMoney.json', 'x') as inbound:
        pass
if not os.path.isfile(r'C:\Program Files (x86)\financeProgram\outboundMoney.json'):
    with open(r'C:\Program Files (x86)\financeProgram\outboundMoney.json', 'x') as outbound:
        pass
if not os.path.isfile(r'C:\Program Files (x86)\financeProgram\savingsContributions.json'):
    with open(r'C:\Program Files (x86)\financeProgram\savingsContributions.json', 'x') as savings:
        pass

#Add code to add shortcut to desktop to run financeProgram.exe

print('Installation Complete')
