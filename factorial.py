def factorial(num):
    a = 0
    b = 1 
    
    try:
        val = float(num)
    except:
        print('It must be a number!')
        return
    if (num) < 0:
        print('Positive numbers only!')
        return
    if num %1 != 0:
        print('Whole numbers only!')
        return
    

    while a < num - 1:
        b = b * (num - a)
        a = a + 1 
        print(b)
    return(b)

factorial()


