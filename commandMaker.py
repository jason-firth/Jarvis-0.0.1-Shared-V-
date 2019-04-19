import os
print("Simple Jarvis Command Maker")

''' Respond Only Commands '''

checkFor = input("What do you want Jarvis to check For?: ")
returnCom = input("What do you want Jarvis to say?: ")
os.system(''' echo '\tif ''' + '''"''' +  str(checkFor) + '''"''' + ''' in command: \t return("''' + str(returnCom) + '''") \n' >> commands.py ''')