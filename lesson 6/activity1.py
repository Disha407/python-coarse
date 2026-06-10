# 1) Store values in `a`, `b`, and `c`.
a=10
b=12
c=-12
# 2) Check an AND condition using `a and b and c`:
if a and b and c :
    print("all are true") 
else:
    print("at leastone is false")
 
# - This becomes True only if all three values are treated as True.

# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a=10
b=-10
c=0
# 4) Check an OR condition: `a > 0 or b > 0`
if a>0 or b>0:
    print("either of them is greater than 0")
else:
    print ("no number is greater than 0" )
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`

# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

