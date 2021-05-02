n = int(input('give me an integer greater or less than zero'));

def getFib(n):
    #return array of numbers in fibonnoci sequence leading up to n
    fibList = [];
    currentNum = 1;
    prevNum = 0;
    while currentNum < n:
        currentSum = currentNum + prevNum;
        fibList.append(currentSum);
        prevNum = currentNum;
        currentNum = currentSum;
    return fibList;

print(getFib(n));

        
