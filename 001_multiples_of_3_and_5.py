"""
    Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we
    get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

def calculate_sum_3_and_5(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum

def calculate_sum_to_n(n):
    return (n * (n+1))//2

def calculate_math_3_and_5(number):
    sum = 0
    if number < 3:
        return sum
    number -= 1
    sum += calculate_sum_to_n(number//3) * 3
    sum += calculate_sum_to_n(number//5) * 5
    sum -= calculate_sum_to_n(number//15) * 15
    return sum

if __name__ == "__main__":
    print(calculate_sum_3_and_5(1000))
    print(calculate_math_3_and_5(1000))
