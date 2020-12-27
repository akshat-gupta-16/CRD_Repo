import threading 
from threading import*
import time

dic={} 

#for create operation 

def create(key,value,timeout=0):
    if key in dic:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    t=[value,timeout]
                else:
                    t=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key name capped at 32 chars
                    dic[key]=t
            else:
                print("error: Memory limit exceeds! ")
        else:
            print("error: Invalind key name, key name can't consist of a number or any special character")

#for read operation
            
def read(key):
    if key not in dic:
        print("error: given key does not exist in database, please enter a valid key") 
    else:
        k=dic[key]
        if k[1]!=0:
            if time.time()<k[1]: #comparing the present time with expiry time
                s=str(key)+":"+str(k[0]) # format of JasonObject i.e.,"key_name:value"
                return s
            else:
                print("error: Time-To-Live of",key,"has expired") 
        else:
            s=str(key)+":"+str(k[0])
            return s

#for delete operation

def delete(key):
    if key not in dic:
        print("error: given key does not exist in database, please enter a valid key") 
    else:
        k=dic[key]
        if k[1]!=0:
            if time.time()<k[1]: 
                print("key is successfully deleted")
            else:
                print("error: Time-To-Live of",key,"has expired") 
        else:
            del dic[key]
            print("key is successfully deleted")