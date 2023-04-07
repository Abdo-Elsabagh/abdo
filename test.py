# print("test")
# a=" ####  L love python ##### "
# print(a.strip(" # "))
# print(a.rstrip(" # "))
# print(a.lstrip(" # "))
# a=" #@@  L love python ##@@# "
# print(a.strip(" #@ "))
# print(a.rstrip(" #@ "))
# print(a.lstrip(" #@ "))
# a="i love python and 3g  php flutter"
# print(a.title())
# b="i love python and 3g 2g php flutter"
# print(b.capitalize())
# zfill

# c, d, e, f = "1", "11", "111", "1111"

# print(c)
# print(d)
# print(e)
# print(f)

# print(c.zfill(4))
# print(d.zfill(4))
# print(e.zfill(4))
# print(f.zfill(4))
 
# g = "abdallah"
# print(g.upper())

# a = "I Love Python and PHP and MySQL"
# print(a.split())

# a = "I@ove@Python@and@PHP@and@MySQL"
# print(a.rsplit('@'))

# b = "I-Love-Python-and-PHP-and-MySQL"
# print(b.split("-"))

# c = "I-Love-Python-and-PHP-and-MySQL"
# print(c.split("-", 3))

# d = "I-Love-Python-and-PHP-and-MySQL"
# print(d.rsplit("-", 3))

# e = "Osama"
# print(e.center(9))  
# print(e.center(9, "#"))  
# print(e.center(15, "@"))  

# count()

# f = "I Love Python and PHP Because PHP is Easy" 
# print(f.count("PHP"))  # 2 PHP Words
# print(f.count("PHP", 0, 25))  # Only One PHP Word

# g = "I Love Python"
# h = "i lOVE pYTHON"

# print(g.swapcase())
# print(h.swapcase())

# i = "I Love Python"
# print(i.startswith("I"))
# print(i.startswith("S"))
# print(i.startswith("P", 7, 12))

# j = "I Love Python"
# print(j.endswith("n"))
# print(j.endswith("S"))
# print(j.endswith("e", 2, 6))


# age= input("entre your age").strip()
# unit=input("choose unit 'month', 'week' , 'days'").strip().lower()
# month =int(age)*12
# week=month*4
# days=int(age)*365

# if unit =="month": 
#     print("you choose print your age from month")
#     print(f"your age by month:{month}")
    
# elif unit == "week": 
#     print("you choose print your age from week")
#     print(f"your age by week:{week}")

# elif unit == "days":
#     print("you choose print your age from days")
#     print(f"your age by days:{days}")

myfav= [] 
maxfav= 5 
while maxfav > 0:
    web=input("inter sit name wihout http://")
    myfav.append(f"http:// {web.strip().lower()}.com")
    maxfav -=1
    print(f"web sit  add {maxfav} place left ")
    print(myfav)
else:
    print("list is full cannot add stor")    
 

 


