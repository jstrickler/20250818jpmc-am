fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for fruit in fruits:
    value = fruit.upper()
    f0.append(value)
print(f"{f0 = }\n")

f1 = [fruit.upper() for fruit in fruits]
print(f"{f1 = }\n")

f2 = [fruit.title() for fruit in fruits]
print(f"{f2 = }\n")

f3 = [fruit.title() for fruit in fruits if fruit.startswith('p')]
print(f"{f3 = }\n")

f4 = [fruit for fruit in fruits if fruit.startswith('a')]
print(f"{f4 = }\n")

f5 = [f.title() for f in fruits]
print(f"{sorted(f5) = }\n")

f6 = [f.title() for f in fruits]
print(f"{sorted(f6, reverse=True) = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', "abc", '1969-12-28'),
]

dobs = [person[-1] for person in people]
print(f"{dobs = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

squares = [n ** 2 for n in nums if n > 300]
print(f"{squares = }\n")

dobs_gen = (p[-1] for p in people) # generator expression (type of iterator) (VIRTUAL)
print(f"{dobs_gen = }")
for dob in dobs_gen:
    print(dob, end=" ")
print("\n\n")