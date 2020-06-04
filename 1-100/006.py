# sum square difference

# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+102=385

# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

# function to square a range of numbers
def sum_squares(up_limit):
    """finds the sum of the squares for a range of numbers

    Args:
        up_limit (int): end of the range of numbers
    """
    total = 0
    for num in range(1, up_limit + 1):
        sq = num * num
        total += sq
    return total


# add a range of numbers, then square the sum
def square_of_sums(up_limit):
    """squares the sum of a range of numbers

    Args:
        up_limit (int): end of the range of numbers
    """
    total = 0
    for num in range(1, up_limit + 1):
        total += num
    square = total * total
    return square


difference = square_of_sums(100) - sum_squares(100)
print(difference)
