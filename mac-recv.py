def Mac(k,m,tlen):
    mk=m+k                                      
    mk=int(mk,2)                                
    t=mk%(2**tlen)                              
    t=str(bin(t).replace("0b",""))              
    t='0'*(tlen-len(t))+t                       
    return t

def verifier(m,t,keys):                                             
    print("Msg:",m,"\t|\tKey:",keys,"\t|\tmac-code:",t)           
    if Mac(keys,m,len(t))==t:
        print("\t\tSuccess")               
    else:
        print("\t\tFailed")                     

def receiver():
    global m,t                                  
    f="-"*50
    s=" "*17
    print()
    print(f,"\n")
    print(s,"Receiver's side",s)
    print()
    m=input("\nEnter the message:\t") 
    k=input("\nEnter the key:\t") 
    t=input("\nEnter the mac-code:\t") 
    verifier(m,t,k)                                 
    print()
    print(f)
receiver()