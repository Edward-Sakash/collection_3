# Exercise 3 (Collections - Digit Filter)
# Solution 1: Using a list comprehansion
def digit_filter(lst):
    return [s for s in lst if not any(c.isdigit() for c in s)]

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
print("> digit_filter(l33t)")
print(digit_filter(l33t))  # Output: ['DCI', 'Digital', 'Career']

print("-------------------------------------------")

# Solution 2: Using a For Loop
def digit_filter(lst):
    result = []
    for s in lst:
        if not any(c.isdigit() for c in s):
            result.append(s)
    return result

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
print("> digit_filter(l33t)")
print(digit_filter(l33t))  # Output: ['DCI', 'Digital', 'Career']

print("-------------------------------------------")