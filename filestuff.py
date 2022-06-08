#Asha Blewett
#Prgram abt using File, 
# 'r' read 
# 'a' append 
# 'w' write open a file and make sure you close it 
# datetime
import random
import os, datetime

os.system('cls')

date=datetime.datetime.now()
print(date)
print(date.strftime("%m-%d-%Y"))

name="Asha"
sce=344
scrLine=str(sce)+"\t"+date.strftime("%m-%d-%Y")+ "\t"+name +"\n"

#create a file 
myFile = open("scre.txt", 'w')
myFile.write(scrLine)
myFile.close()
#Create new line
name="Peter"
sce=132
scrLine=str(sce)+"\t"+date.strftime("%m-%d-%Y")+ "\t"+name +"\n"
#Append to your file add lines the file
myFile = open("scre.txt", 'a')
myFile.write(scrLine)
myFile.close()
#Read the file 
myFile = open("scre.txt", 'r')
stuff=myFile.readlines()
myFile.close()
for line in stuff:
    print(line)