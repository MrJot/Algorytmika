
ALPHABET=list("aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż")
def readFile():
    #Wczytywanie pliku ze zdefiniowanej ścieżki, kodowanie utf-8
    file = open("/Users/grzegorzjuszkiewicz/Desktop/Python/encode.txt",encoding="utf8")
    return file

def setMessage():
    return input("Podaj wiadomość do zaszyfrowania/zdeszyfrowania:")


def stringToChar():
    message=setMessage()
    chars=[]
    for word in message:
        for letter in word:
            chars.append(letter)
    return chars

def idItems(items):
    return items

def passwordPrep(code, message):
    code_list = list(str(code))
    psswd_list=[]
    nonalpha=[]
    nonalphaId=[]
    message_list=message
    for i in range(0,len(message_list)):
        if message_list[i].isalpha():
            psswd_list.append(int(code_list[i % len(code_list)]))
        else:
            nonalpha.append(message_list[i])
            nonalphaId.append(i)
    return psswd_list, nonalpha, nonalphaId



def whatToDo(status):
    if(status):
        return True
    else:
        return False
        


a=stringToChar()
b=passwordPrep(1,a)
print(list(b[0])[1])
ency_Id=[]
decy_Id=[]
encrypted_message=[]
decrypted_message=[]
test=[]
test2=[]
for i in range(0,len(a)):
    for j in range(0,len(ALPHABET)):
        if a[i]==ALPHABET[j]:
            ency_Id.append(j)
            print(ALPHABET[(j + list(b[0])[i]) % len(ALPHABET)])
#            encrypted_message.append(ALPHABET[(ency_Id[j] + b[i]) % len(ALPHABET)])
#            decrypted_message.append(ALPHABET[(ency_Id[i] - b[i]) % len(ALPHABET)])
            

#print(encrypted_message)
#print(decrypted_message)
print(ency_Id)
#print(decy_Id)
#print(encrypted_message)
#print(decrypted_message)
#    
    
    


#from string import ascii_lowercase
#for c in ascii_lowercase:
#    print(c)
#
#
#print(ALPHABET)        