import itertools
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};:,.<>?'
min_length = 8
max_length = 15
def combination_to_string(combination):
    return ''.join(combination)
with open('combinations.txt', 'w') as file:
    for length in range(min_length, max_length + 1):
        combinations = itertools.product(characters, repeat=length)
        for combo in combinations:
            combo_str = combination_to_string(combo)
            file.write(combo_str + '\n')
print(f'All combinations from length {min_length} to {max_length} are being saved to combinations.txt (within practical limits).')