def is_palindrome(num):
    return str(num) == str(num)[::-1]


def all_palindromes(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True

arr = list(map(int, input("Enter array: ").split()))

result = all_palindromes(arr)

if result:
    print("True (All elements are palindrome)")
else:
    print("False (Not all elements are palindrome)")