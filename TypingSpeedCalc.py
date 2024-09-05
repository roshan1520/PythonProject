from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest:
                error=error+1
        except :
            error=error+1
    return error
    
def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s

    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)





test=["A specific vaccine for humans that is effective in preventing avian influenza is not yet readily available. Based upon limited data, the CDC has suggested that the anti-viral medication Oseltamivir may be effective in treating avian influenza. Using this input, the Department of State has decided to pre-position the drug Tamiflu at its Embassies and Consulates worldwide, for eligible U.S.","A paragraph is a collection of words combined together to make a longer unit than a sentence. It's a set of sentences that are well-organized and coherent, and they're all about the same thing. Several sentences often make up a paragraph. There are normally three to eight sentences in a paragraph. Almost all of the writing one reads in a textbook or an article can be grouped into paragraphs if it is longer than a few sentences.","Dog is a pet animal. It is the oldest friend of human beings. It watches our house. It is very faithful animal and never left his master. It is used by police to fight crime. Sheep- rearers also use them. Thus it is useful for us in many ways.","Morning walk is good for health. I daily go for morning walk. I get up at 5am. I go to the park near my house. First of all I do jogging and complete two rounds of the park. After this warm up I either do yoga or play volleyball with my friends. Morning air is always refreshing. I love the chirping of the birds, coolness of the breeze and calmness in the atmosphere. This prepares me for the whole day."]

test1=r.choice(test)
print("-------Typing Speed--------")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter: ")
time_2=time()

print('Speed: ',speed_time(time_1,time_2,testinput)," w/sec")

print("Error: ",mistake(test1,testinput))



