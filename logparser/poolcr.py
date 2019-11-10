import os, sys 
import random as rand


path = os.getcwd()
print("Current directory is %s" % path)

f = open('example.txt', 'tw', encoding='utf-8')
okMark = False

for i in range(100):
    f.write('<i guid='+ str(rand.randint(1, 55)) + '\n')
    f.write('   currentCuid=' + str(rand.randint(10000000, 99999999)) + '\n')
    f.write('   passport=' + str(rand.randint(1000000000, 9999999999)) + '\n')
    f.write('>\n')
    f.write('</i>\n\n')

    if i%2 == 0:
        f.write('<c wrapperUid='+ str(rand.randint(1, 55)) + ' /c>\n\n')
        okMark = True
        
    if i%4 == 0:
        f.write('<c wrapperUid='+ str(rand.randint(1, 55)) + ' /c>\n\n')
        okMark = True
        
    if i%3 == 0:
        f.write('<c wrapperUid='+ str(rand.randint(1, 55)) + ' /c>\n\n')
        okMark = True
        
    if okMark == False and i % rand.randint(1, 50) == 0:
        f.write('<b divisionId='+ str(rand.randint(1, 55)) + '\n')
        f.write('   CodeName: ololo\n')
        f.write('   Message: YOU VE FUCKED!\n')
        f.write('/b>\n\n')
        
    if okMark == True:
        okMark = False
        

f.close()