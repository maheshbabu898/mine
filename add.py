import this

print("hello world")


def helloworld(text):
    print(text)
    for i in range(len(text)):
        print(text[i])


dict = {"apple": 2, "banana": 3}


class ILOVEDOGS:
    def __init__(self, name):
        self.name = name

    def f(self, x):
        return x ^ 2 + 3


# Python Debugging Exercise 1
def minimum(some_list):
    a = 0
    for x in range(1, len(some_list)):
        if some_list[x] < a:
            a = some_list[x]
    return a


# Python Debugging Exercise 2
# The goal of this function is to add up all the even numbers and return the number
## Question
def add_even(some_list):
    a = 0
    x = some_list[a]
    return sum([x for x in some_list if a % 2 == 0])


## Answer
def add_even_ans(some_list):
    a = 0
    return sum([x for x in some_list if x % 2 == 0])


# Python Debugging Exercise 3
# def bad_add_up(number):
#     i = 1

#     while i < nomber:
#         if number % 2 = 0:
#             total = total + number
#         i = i + 1
#         print(total)


def pseudo_good_add_up(number):
    if number % 2 == 0:
        return sum(list(range(0, number + 2, 2)))
    else:
        return sum(list(range(1, number + 2, 2)))


def actual_good_add_up(number):
    # If Even Number
    if number % 2 == 0:
        return (
            sum(list(range(0, number + 2, 2)))
            if number >= 0
            else sum(list(range(number - 2, 0, 2)))
        )
    # If Odd Number
    return (
        sum(list(range(1, number + 2, 2)))
        if number >= 0
        else sum(list(range(number - 2, 1, 2)))
    )


if __name__ == "__main__":
    # new_list = [30, 40, 8, 9, 20, 15]
    # print(minimum(new_list))
    # print(f"Add Even: {add_even(new_list)}")
    # print(actual_good_add_up(5))
    test_value = int(input("input a number"))
    print(actual_good_add_up(test_value))
