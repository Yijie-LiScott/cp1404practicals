"""
a. Print numbers from 0 to 100 stepping by 10
    for i from 0 to 100 step 10
     print i, (no newline)  // print i followed by a space
    print newline

b. Print numbers from 20 down to 1
    for a from 20 down to 1 step -1
     print a, (no newline)  // print a followed by a space
    print newline

c. Print a specified number of stars on one line (stars separated by spaces)
    get n  // prompt: "number of stars :"
    for count from 1 to n
     print "", (no newline)  // print "" followed by a space
    print newline

d. Print increasing lines of stars (line 1 has 1 star, line 2 has 2, ..., line n has n)
    get n  // prompt: "number of stars :"
    for i from 1 to n
     for _ from 1 to i
      print "*", (no newline)
       print newline
"""
# print odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a.
for i in range(0,101,10):
    print(i, end=' ')
    print()
#b.
for a in range(20,0,-1):
    print(a, end=' ')
    print()

#c.
n = int(input("number of stars :"))
for _ in range(0,n):
    print("*", end=' ')

#d.
n = int(input("number of stars :"))
for i in range(1,n+1):
    for _ in range(i):
     print("*", end='')
    print()
