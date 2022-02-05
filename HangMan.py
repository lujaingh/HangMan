#!/usr/bin/env python
# coding: utf-8

# In[179]:


import random
listrandom=[]
def randIndex(length):
    
    random_number = int(random.randint(0, length))##to generate random index
    #print('rand',random_number)
    listrandom.append(random_number)
    


# In[100]:


"""This is hangman game, you have a sentance, there are some  hidden charachters, you have three levels to play, if easy there will be 10 letters displayed if medium then 7 if hard then 5, try to help the man and let him free, you have five trials if you want to enter alphabet each time or a full sentence """


# In[1]:


"""Note: I modified a little in the game logic i create my own logic in some cases"""


# In[180]:


from collections import OrderedDict

level = input("Hello player1 Welcome in Hangman Game,enter level please, easy ,medium,hard :) ").lower().strip().replace(" ", "").replace("\n", "")#to remove spaces and ignore cases and remove newline chars
levels=['easy', 'medium','hard']
while level not in levels:
    level = input("re-enter level please, easy medium,hard :) ").lower().strip().replace(" ", "").replace("\n", "")

#

sentence = input("Hello player1,enter a sentence please :) ").lower().strip().replace(" ", "").replace("\n", "")
specialCharacters = "\'!@#$%^&*()-+?_=,/\\<>\""

sentence=''.join(i for i in sentence if not i.isdigit() and i not in specialCharacters)

listOfsentence=list(sentence)


print(listOfsentence)

for i in listOfsentence:
    #print(i)
    if  i.isdigit()  :
        print(i)
        listOfsentence.remove(i)
    else:
        if i  in specialCharacters:
            print(i)
            listOfsentence.remove(i)
        else:
            continue
        
sentTrue="".join(listOfsentence)        

alphabets=[]

print(listOfsentence)
temp=[]
flag=False
flag2=False
listhidden=[]
#
counter=0
if level=='easy':
    temp.clear()
    listrandom.clear()
    for i in range(0,10):
        if flag2:
            break
        
        while len(listrandom)<10:
            randIndex(len(listOfsentence)-1) 

                
            for k in listrandom:
                if k  in temp:
                    continue
                else:
                    temp.append(k)#remove duplicates indecies
                    
            listrandom=list(OrderedDict.fromkeys(temp))
            

            if len(listrandom)>=10:
                flag2=True
                break
                    

                
    listind=range(0,len(listOfsentence))    
   
    for j in listind:


        if j not  in listrandom:
            listhidden.append(listOfsentence[j])
            listOfsentence[j]='_' 
            
      

        
elif  level=='medium':
    temp.clear()
    listrandom.clear()
    for i in range(0,7):
        if flag2:
            break
        #print('i',i)
        #print("#")       
        #randIndex(len(listOfsentence)-1)
        
        while len(listrandom)<7:
            randIndex(len(listOfsentence)-1) 

                
            for k in listrandom:
                if k  in temp:
                    continue
                else:
                    temp.append(k)#remove duplicates indecies
                    
            listrandom=list(OrderedDict.fromkeys(temp))
            

            if len(listrandom)>=7:
                flag2=True
                break
                    

                
    listind=range(0,len(listOfsentence))    
   
    for j in listind:


        if j not  in listrandom:
            listhidden.append(listOfsentence[j])
            listOfsentence[j]='_'         
    
else:
    temp.clear()
    listrandom.clear()
    for i in range(0,5):
        if flag2:
            break
        #print('i',i)
        #print("#")       
        #randIndex(len(listOfsentence)-1)
        
        while len(listrandom)<5:
            randIndex(len(listOfsentence)-1) 

                
            for k in listrandom:
                if k  in temp:
                    continue
                else:
                    temp.append(k)#remove duplicates indecies
                    
            listrandom=list(OrderedDict.fromkeys(temp))
            

            if len(listrandom)>=5:
                flag2=True
                break
                    

                
    listind=range(0,len(listOfsentence))    
   
    for j in listind:


        if j not  in listrandom:
            #print('j=',j)
            #print(listOfsentence[j])
            listhidden.append(listOfsentence[j])
            listOfsentence[j]='_'         
    
                    
                    
                    
print(listOfsentence)


# In[183]:


print("   _____ \n  |      \n  |      \n  |      \n  |      \n  |      \n  |      \n__|__\n")
print(listOfsentence)
alreadychars=dict()
listcommand=['allsentence','alphabet']
cmd = input("you have 5 trials, enter how you want to guess allsentence , alphabet :) ").lower().strip().replace(" ", "").replace("\n", "")#to remove spaces and ignore cases and remove newline chars
while cmd not in listcommand:
    cmd = input("re-enter  please, allsentence , alphabet :) ").lower().strip().replace(" ", "").replace("\n", "")
#
trials1=0    
trials2=0

#
sen=''
if cmd=='allsentence':
    while trials1 <5:
        trials1+=1
        sen = input("enter sentence  :) ").lower().strip().replace(" ", "").replace("\n", "")
        if sen == sentTrue:
            print('WOW you are brave, you got it right from the {0} trial'.format(trials1))
            break
        else:
            continue
    if sen!= sentTrue:
        print("WOW you are brave, but it was a wrong answer The right one is {0} ".format(sentTrue))
            

else:  
     while trials2 <5:

        alphabet = input("enter alphabet  :) ").lower().strip().replace(" ", "").replace("\n", "")
        while alphabet  in alreadychars.keys():
            print("You already entered this character and it was {0}".format(alreadychars[alphabet]))
            alphabet = input("enter alphabet  :) ").lower().strip().replace(" ", "").replace("\n", "")  
            
  
        
        while  alphabet.isdigit() and alphabet  in specialCharacters:
            
            print("You entered a non-alphabet character")
            alphabet = input("enter alphabet  :) ").lower().strip().replace(" ", "").replace("\n", "")
         

        if  alphabet in listhidden:
            for i in listOfsentence:
                ind=sentTrue.index(alphabet)
                listOfsentence[ind]=alphabet
                #print("ind=",ind,"alphabet=",alphabet)
            print("Greate Guess:","".join(listOfsentence))
            
            alreadychars[alphabet]='true'
                
            listhidden.remove(alphabet)
        else:
            print("Wrong Char:",alphabet)
            alreadychars[alphabet]='false'
            #print(alreadychars)
            trials2+=1#lose a trial
            if trials2==1:
                
                print("   _____ \n", "  |     | \n","  |     |\n","  |     | \n","  |     O \n","  |      \n","  |      \n","__|__\n")
            if trials2==2:
                
                print("   _____ \n","  |     | \n","  |     |\n","  |     | \n","  |     O \n","  |    /  \n","  |        \n","__|__\n")            
            
            if trials2==3:
                
                print("   _____ \n","  |     | \n","  |     |\n","  |     | \n","  |     O \n","  |    / \ \n","  |       \n","__|__\n")
                
            if trials2==4:
                
                print("   _____ \n","  |     | \n","  |     |\n","  |     | \n","  |     O \n","  |    /|\ \n","  |       \n", "__|__\n")          
            if trials2==5:    
                print("   _____ \n","  |     | \n","  |     |\n","  |     | \n","  |     O \n","  |    /|\ \n","  |    / \ \n"
                  ,"__|__\n")
                
        
        if trials2==5 and "".join(listOfsentence)!=sentTrue:
            print("You ran out of trials and Catched {0} The right sentence is {1}".format("".join(listOfsentence),sentTrue))
        if trials2<=5 and "".join(listOfsentence)==sentTrue:
            print('WOW you are brave, you got it right from the {0} trial'.format(trials2))

