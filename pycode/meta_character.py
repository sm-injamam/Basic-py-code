import re
print("..................1.........................")
pattern = r"^colo..r$" #.(dot), ^(start), $(end)

if re.match(pattern,"coloufr"):
    print("Matched")
else:
    print("Not matched")

print("..................2.........................")
if re.match(pattern, "voloufr"): #^,$
        print("Matched")
else:
        print("Not matched")

print("..................3.........................")
pattern2 = r"a*" # *
if re.match(pattern2,"coloufr"):
    print("Matched")
else:
    print("Not matched")
print("....................4.......................")
pattern2 = r"a+" # +
if re.match(pattern2,"acoloufr"):
    print("Matched")
else:
    print("Not matched")
print("...................5........................")
pattern2 = r"a+b" # +
if re.match(pattern2,"abcoloufr"):
    print("Matched")
else:
    print("Not matched")

print(".....................6......................")
pattern3 = r"ice(-)?cream" # ?
if re.match(pattern3,"icecream"):
    print("Matched")
else:
    print("Not matched")

print(".....................7......................")
pattern4 = r"a{1,3}$" # { }
if re.match(pattern4,"aaaa"): # It will be not matched for more than 3 times
    print("Matched")
else:
    print("Not matched")

print(".....................8......................")
pattern4 = r"[A-Z].[a-z][0-9]"  # character class
if re.match(pattern4, "Vc7aaa"):  # It will be not matched for more than 3 times
    print("Matched")
else:
    print("Not matched")





