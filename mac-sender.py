import random
keys=[]

def Gen(klen):                                  
    global keys                                 
    for i in range(0,2**klen):                  
        key=str(bin(i).replace("0b",""))        
        key='0'*(klen-len(key))+key             
        keys.append(key)                        
    k=random.choice(keys)                       
    return k 

def Mac(k,m,tlen):                              
    mk=m+k                                     
    mk=int(mk,2)                                
    t=mk%(2**tlen)                              
    t=str(bin(t).replace("0b",""))              
    t='0'*(tlen-len(t))+t                       
    return t

def Sender():
    global m,k,t,klen,tlen,keys
    keys=[]
    f="-"*50
    s=" "*18
    print()
    print(f,"\n")
    print(s,"Sender's side",s)
    m=input("\nEnter the message:\t")           
    klen=int(input("Enter length of key:\t"))   
    k=Gen(klen)                                 
    tlen=int(input("Enter length of mac-code:\t"))  
    t=Mac(k,m,tlen)                             
    print()
    print("Msg:",m,"\t|\tKey:",k,"\t|\tmac-code:",t)

Sender()         
