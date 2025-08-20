fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits = }\n")

print(f"{fruits[0] = }\n")  # first element, not a slice
print(f"{fruits[4] = }\n")  # fifth element, not a slice
print(f"{fruits[-1] = }\n") # last element

print(f"fruits[len(fruits)-1]")
print(f"{fruits[0:-10] = }")
print(f"{fruits[0:len(fruits)-10] = }")
print(f"{fruits[-10:] = }")
print(f"{fruits[len(fruits)-10:len(fruits)] = }")


#    LIST[start-at:stop-before:count-by]
print(f"{fruits[0:3] = }\n")  # first 3 elements (0, 1, 2)
print(f"{fruits[2:9] = }\n")  # elements from index 2 to 8
# [:3]  same as [0:3]
# [4:]  same as [4:len(LIST)]   # i.e., 4 through end
# [:]  entire list also [::]
start = 5
print(f"{start = }")
print(f"{fruits[start:start + 3] = }\n")  # 3 elements starting at 'start'

print(f"{fruits[10:] = }\n") # index 10 through end
print(f"{fruits[-5:] = }\n") # last 5 elements (index -5, -4, ...)

print(f"{fruits[1:-1] = }\n")  # all but first and last
print(f"{fruits[:-10] = }\n")  # all but last 10

