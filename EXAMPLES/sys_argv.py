import sys  # load a module named 'sys'

print(f"sys.argv: {sys.argv}\n")

script_name = sys.argv[0]
print(f"{script_name = }")

first_arg = sys.argv[1]  # First command line argument
print(f"first_arg: {first_arg}")

