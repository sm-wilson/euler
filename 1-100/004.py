# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def larrgestPalindrome(n):

    upper_limit = 0

    # Loop to calculate upper
    # bound(largest number
    # of n-digit)
    for i in range(1, n + 1):

        upper_limit = upper_limit * 10
        upper_limit = upper_limit + 9

    # largest number of n-1 digit.
    # One plus this number
    # is lower limit which is
    # product of two numbers.
    lower_limit = 1 + upper_limit // 10

    max_product = 0  # Initialize result
    for i in range(upper_limit, lower_limit - 1, -1):

        for j in range(i, lower_limit - 1, -1):

            # calculating product of
            # two n-digit numbers
            product = i * j
            if product < max_product:
                break
            number = product
            reverse = 0

            # calculating reverse of
            # product to check
            # whether it is palindrome or not
            while number != 0:

                reverse = reverse * 10 + number % 10
                number = number // 10

            # update new product if exist and if
            # greater than previous one
            if product == reverse and product > max_product:
                max_product = product

    return max_product


print(larrgestPalindrome(3))
