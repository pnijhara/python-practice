
minpay =10
while True:
    def lowest(balance,minpay,rate,month):
        if month <12:
            unpaidb = balance - minpay
            balance = unpaidb + rate*unpaidb
            month+=1
            return lowest(balance,minpay,rate,month)
        else:
            return(balance,minpay)
    tup = lowest(1000,minpay,0.2/12,month = 0)
    if tup[0]<= 0:
        break
    else:
        minpay+=0.01
print(tup[1])
    
