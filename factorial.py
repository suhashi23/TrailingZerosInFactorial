def factorial(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * factorial(num-1)
def factorialTrailingZeros(num):
    count = 0
    i = 5
    while(num//i != 0):
        count += int(num/i)
        i = i*5
    return count
    

if __name__ == '__main__':
    num = int(input("Enter a number: \n"))
    print(f"The number of trailing zeros in the given factorial is: {factorialTrailingZeros(num)}")