from logging import exception
from pyfiglet import Figlet
from cryptography.fernet import Fernet
import time
import os

os.system("")
#Color Class

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
#Encryption Functions

def encrypt():
    key=Fernet.generate_key()
    keyfile=input("Enter File Name You want to Save Key PLease Make Sure Adding Extention with (.enc)")
# Creating File To Save Key 
    with open(keyfile,'wb') as filekey:
        filekey.write(key)
#Reading Kkey String From File and SaveKey Into File  
#C:\Users\Abdullah\Desktop\Main Encryption {roogram\TKfont.py
    with open(keyfile,"rb") as filekey:
        keyData=filekey.read()
        print(keyData.decode())
        
    fernet =Fernet(key)
    #a=input("Input File name:")
   
    try:
        a=input("Input File name or Path replace \ with /:")
        with open(a,'rb') as orFile:
            orF=orFile.read()
        encFile=fernet.encrypt(orF)
        
    except:
        print("File Does Not Exist! Try Again")
        time.sleep(2)
        return encrypt()
    encFile=fernet.encrypt(orF)           
        

        
   
    # encFile=fernet.encrypt(orF)
    try:
        encFilee=input("Enter Encrypted File Name To Save (Warning! Make Sure adding Extention at the End with File Type :) ")
        with open(encFilee,"wb") as enc_file:
            enc_file.write(encFile)
    except:
        print("Error Found :) ")
        time.sleep(3)

def dec():
    key=input("Enter Your Key:")    
    fernet_key=Fernet(key)
    
    a=input("Enter File Name Or Path:")
    with open(a,'rb') as enc_file:

        encrypted=enc_file.read()
        if encrypted:
            print(" File Found :)")
        else:
            print("File Not Found Try Again")
            return dec()
    decrypt=fernet_key.decrypt(encrypted)

        
    
    with open(a,'wb') as dec_file:
        dec_file.write(decrypt)

def close():
    exit()

 




def option():
#bANNER
    banner ='''

    ███████  █████  ███████ ███████    ██████ ██ ██████  ██   ██ ███████ ██████  
    ██      ██   ██ ██      ██        ██      ██ ██   ██ ██   ██ ██      ██   ██ 
    ███████ ███████ █████   █████     ██      ██ ██████  ███████ █████   ██████ 
         ██ ██   ██ ██      ██        ██      ██ ██      ██   ██ ██      ██   ██ 
    ███████ ██   ██ ██      ███████    ██████ ██ ██      ██   ██ ███████ ██   ██ 
    
                                                                               

                                          Developed By : MrBlackX
                                          Version      :  1.0.0
                                         Facebook:  https://www.facebook.com/Mr.BlackX1/

                                                                                                                   


'''
    choose='''
    Please Choose an Option
    
    1. Encrypt
    2. Decrypt
    3. Exit
    '''
    print(style.YELLOW+ banner)
  
    print(style.GREEN+choose)
option()


inP = ""
while inP !="Exit":
    
    inP=input("") 
    #e=""
    
    if inP=="1":
        
        encrypt()
        time.sleep(1)
        print("File Encrypted Successfully !")
        time.sleep(2)
        option()

    elif inP =="2":
        
        dec()
        time.sleep(1)
        print("File Decrypted SuccessFully !")
        time.sleep(1)
        option()
    elif inP =="3":
        print("Thanks For Using SAFE CIPHER")
        time.sleep(1)
        exit()
        
        

   

    else:
      
         print("You Typed Invaild Option Please Choose a Vaild Option!")




