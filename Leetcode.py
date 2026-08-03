'''#    1.Two Sum
def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
nums = [1,2,3,4,5,6,7,8,9]
target = int(input(f"nums: {nums}\nEnter target: "))
print(twoSum(nums,target))
'''

'''#   2. Palindrome Number and string
num = int(input("Enter a number: "))
if num < 0:
    print(num,"is not a Palindrome number")
else:
    n = num
    rev = 0
    while n!=0:
        digit = n%10
        rev=rev*10+digit
        n//=10
    print("Reverse: ",rev)
    if rev == num:
        print(num,"is a Palindrome number")
    else:
        print(num,"is not a Palindrome number")

num = input("Enter a string: ")
rev = num[::-1]
print("Reverse:",rev)
if rev == num:
    print(num,"is a Palindrome String")
else:
    print(num,"is not a Palindrome String")
'''

