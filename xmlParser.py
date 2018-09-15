import os
from bs4 import BeautifulSoup

infile =open("current_work_snips/mail.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')

list=[]
list2=[]
allNames = soup.find_all('type')

for type_tag in allNames:
    identifier=str(type_tag.find_next_sibling("name").get_text())
    if identifier in list:
        list2.append(identifier)

    list.append(identifier)


print ("The indentifers are as follows\n\n"+str(list2))

print ("The indentifers statements are as follows\n")


infileProgram = open("current_work_snips/Mail.java","r")
with infileProgram as f:
    for line in f:
        currentLine = line.strip()
        for item in list2:
            if currentLine.find(item) > -1:
                print currentLine + "   : Found item "+item+" on this line"
