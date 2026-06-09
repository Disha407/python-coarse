cp=int(input("enter cost price"))
sp=int(input("enter selling price"))
if sp>cp:
    profit= sp-cp
    print ("profit",profit)
else: 
    loss=cp-sp
    print("loss is",loss)
print("thankyou for shopping")