def oneDigitBirth():
    listDigit = []
    listTwoDigits = []
    sumNumbers = 0
    sumTwoNumbers = 0
    
    value = str(input("Enter you birth: "))
    
    for char in value:
        listDigit.append(int(char))
        
    for numbers in listDigit:
        sumNumbers += numbers
    
    for twoDigit in str(sumNumbers):
        listTwoDigits.append(int(twoDigit))
        
    if len(listTwoDigits) >= 2:
        for i in listTwoDigits:
            sumTwoNumbers += i
            print(sumTwoNumbers)
    else:
        print(sumNumbers)
    

            
oneDigitBirth()