is_number = lambda s: s.replace('.', '', 1).isdigit() if s.count('.') <= 1 else False
print(is_number("123"))
print(is_number("12.3"))
print(is_number("abc"))
