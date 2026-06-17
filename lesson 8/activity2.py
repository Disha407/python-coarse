# 1) Ask the user to enter the numerator and store it in `numn`.

# 2) Ask the user to enter the denominator and store it in `numd`.

# 3) Check if `numn` is divisible by `numd`:

# - Find the remainder when `numn` is divided by `numd`.

# - If the remainder is 0, it means perfectly divisible.

#Example:if numn%numd==0:

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.
num=int(input("enter the numerator"))
den=int(input("enter the denominator"))
if num%den==0:
    print("the numerator is divisible by denominator")
else:
    print("the numerator is not divisible by denominator")
    


