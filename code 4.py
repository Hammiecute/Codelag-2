count=0

while(count<=100):
    count+=1
    if(count%3==0 and count%5==0):
        print("Fizzbuzz")
    elif(count%3==0):
        print("fizz")
    elif(count%5==0):
        print("buzz")
    elif(count%4==0):
        print("cizz")
    else:
        print(count)
