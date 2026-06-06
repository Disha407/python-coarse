# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
english=int(input("english:"))
hindi = int(input("hindi :"))
maths=int(input("maths:"))
sst=int(input("sst;"))

# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.
sum=maths+hindi+english+sst
# 3) Print the total marks stored in `sum`.
print("sum of all subjects",sum)
# 4) Calculate the percentage:


# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)

# - Multiply the result by 100

# Store the final value in `perc`.

perc = (sum/400)*100

# 5) Print the percentage stored in `perc`.

print("percentage of the student",perc)