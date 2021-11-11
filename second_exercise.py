counter = 0
# Set puzzle range, example with adventofcode given values
from_number = 372037
to_number = 905158
for i in range(from_number,to_number):
    splitted_number = list(map(int, str(i)))
    current_digit = None
    match_double_rule = False
    violate_keep_increase_rule = False
    for index, digit in enumerate(splitted_number):
        if current_digit and current_digit==digit:
            match_double_rule = True
        if current_digit and current_digit>digit:
            violate_keep_increase_rule = True
        current_digit = digit
    if match_double_rule and not violate_keep_increase_rule:
        counter+=1

print(counter)
