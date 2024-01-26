# 1: capitalize() - Returns a copy of the string with the first character capitalized and the rest lowercased.
text_capitalize: str = "sanni"
print(text_capitalize.capitalize())

# 2: casefold() - Returns a casefolded copy of the string, removing all case distinctions.
text_casefold: str = "MaRiO"
print((text_casefold.casefold()))

# 3: center() - Returns a centered string of length `width`. Padding is done using the specified `fillchar`.
center_text: str = "Luigi"
print(center_text.center(40, "s"))

# 4: count() - Returns the number of occurrences of `substring` in the string.
count_text: str = "abc_abc_abc_abc"
print(count_text.count("ab"))

# 5: encode() - Returns the encoded version of the string as a bytes object.
encode_text: str = "Elon Musk"
print(encode_text.encode(encoding="UTF-8", errors="strict"))

# 6: endswith() - Returns `True` if the string ends with the specified `suffix`, otherwise `False`.
endswith_text: str = "apple"
print(endswith_text.endswith("e"))

# 7: expandtabs() - Returns a copy of the string where all tab characters are replaced by spaces.
expand_tabs: str = "text1\ttext2\ttext2"
print(expand_tabs.expandtabs(20))

# 8: find() - Returns the lowest index in the string where `substring` is found.
find_text: str = "Find the name (Sanni) in this sentence"
postion: int = find_text.find("sanni".capitalize())
print(postion)

# 9: format() - Formats the string using positional and keyword arguments.
format_text: str = "{subject} is doing: {action}"
print(format_text.format(subject="cat", action="meow"))
# or
format_text_2: str = "{} is doing: {}"
print(format_text_2.format("cat", "meow"))

# 10: format_map() - Similar to `format()` but accepts a mapping (dictionary) as its argument.
coordinates: dict = {"x": 10, "y": -5}
format_map: str = "Coordinates: ({x}, {y})"
print(format_map.format_map(coordinates))

# 11: index() - Returns the lowest index in the string where `substring` is found, raises ValueError if not found.
index_text: str = "Get the Index Positon of (1)"
print(index_text.index(("1")))
print(index_text[26])

# 12: isalnum() - Returns `True` if all characters in the string are alphanumeric, otherwise `False`.
check_alnum: str = "hello123"
print(check_alnum.isalnum())

# 13: isalpha() - Returns `True` if all characters in the string are alphabetic, otherwise `False`.
isalpha_text: str = "hellokitty"
print(isalpha_text.isalpha())

# 14: isascii() - Returns `True` if all characters in the string are ASCII, otherwise `False`.
isascii_text: str = "hello"
print(isascii_text.isascii())

# 15: isdecimal() - Returns `True` if all characters in the string are decimal characters, otherwise `False`.
check_if_decimal: str = "1113"
print(check_if_decimal.isdecimal())

# 16: isdigit() - Returns `True` if all characters in the string are digits, otherwise `False`.
check_if_digit: str = "sss"
print(check_if_digit.isdigit())

# 17: isnumeric() - Returns `True` if all characters in the string are numeric characters, otherwise `False`.
check_if_numeric: str = "111"
print(check_if_numeric.isnumeric())

# 18: isidentifier() - Returns `True` if the string is a valid Python identifier, otherwise `False`.
isidentifier_text: str = "my_name"
print(isidentifier_text.isidentifier())

# 19: islower() - Returns `True` if all characters in the string are lowercase, otherwise `False`.
islower_text: str = "WWW"
print(islower_text.islower())

# 20: isprintable() - Returns `True` if all characters in the string are printable, otherwise `False`.
isprintable_text: str = "text"
print(isprintable_text.isprintable())

# 21: isspace() - Returns `True` if all characters in the string are whitespace, otherwise `False`.
space_text: str = " "
print(space_text.isspace())

# 22: istitle() - Returns `True` if the string is titlecased, otherwise `False`.
istittle_text: str = "the Text"
print(istittle_text.istitle())

# 23: isupper() - Returns `True` if all characters in the string are uppercase, otherwise `False`.
isupperText: str = "Ww"
print(isupperText.isupper())

# 24: join() - Joins the elements of the iterable with the string as a separator.
join_text: str = "-"
print(join_text.join(["sanni", "bola"]))

# 25: ljust() - Returns a left-justified string of length `width`.
ljust_text: str = "text"
print(ljust_text.ljust(20, '-'))

# 26: lower() - Returns a copy of the string converted to lowercase.
lowerText: str = "WWWW"
print(lowerText.lower())

# 27: lstrip() - Returns a copy of the string with leading characters removed.
remove_text: str = "Some text"
print(remove_text.lstrip("Some "))

# 28: maketrans() & 29: translate() - Returns a translation table suitable for passing to the `translate()` method.
maketrans_text: str = "This is Banni"
table = maketrans_text.maketrans("B", "S")
print(table)
print(maketrans_text.translate(table))

# 30: partition() - Returns a tuple containing the original string and its partition.
split_text: str = "a+b=c"
print(split_text.partition("+"))

# 31: removeprefix() - Returns a copy of the string with the specified `prefix` removed.
remove_prefix: str = "What Up"
print(remove_prefix.removeprefix("What"))

# 32: removesuffix() - Returns a copy of the string with the specified `suffix` removed.
remove_suffix: str = "Mister Everyone"
print(remove_suffix.removesuffix("one"))

# 33: replace() - Returns a copy of the string with all occurrences of `old` replaced by `new`.
replace_text: str = "Replace W W"
print(replace_text.replace("W", "H", 1))

# 34: rfind() - Returns the highest index in the string where `substring` is found.
rfind_text: str = "A text A"
print(rfind_text.rfind("A"))
print(rfind_text[7])

# 35: rindex() - Returns the highest index in the string where `substring` is found, raises ValueError if not found.
rindex_text: str = "B text B"
print(rindex_text.rfind("B"))
print(rindex_text[7])

# 36: rjust() - Returns a right-justified string of length `width`.
just_text: str = "test"
print(just_text.rjust(20, "_"))

# 37: rpartition() - Returns a tuple containing the original string and its partition.
rpartition_text: str = "text=text2=text3"
print(rpartition_text.rpartition("="))


# 38: rsplit() & 39: split() - Splits the string at the specified separator and returns a list.
splitText: str = "This is some stuff"
print(splitText.split(sep=" "))
print(splitText.split(maxsplit=2))
print(splitText.rsplit(sep=" "))

# 40: rstrip() - Returns a copy of the string with trailing characters removed.
name: str = "Her Name is Mario Mario!"
print(name.rstrip("Mario!"))

# 41: splitlines() - Splits the string at line breaks and returns a list of lines.
line_text: str = "Coding is\n Sweet"
print(line_text.splitlines(keepends=True))
print(line_text.splitlines())

# 42: startswith() - Returns `True` if the string starts with the specified `prefix`, otherwise `False`.
start_text: str = "Luigi"
print(start_text.startswith("L"))

# 43: strip() - Returns a copy of the string with leading and trailing characters removed.
strip_text: str = "Luigig"
print(strip_text.strip("L"))

# 44: swapcase() - Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
swap_text: str = "Lugi has pasta"
print(swap_text.swapcase())

# 45: title() - Returns a titlecased version of the string, where words start with an uppercase character and the remaining characters are lowercase.
title_text: str = "this is a title"
print(title_text.title())

# 46: upper() - Returns a copy of the string converted to uppercase.
upper_text: str = "this is in capital letter"
print(upper_text.upper())

# 47: zfill() - Returns a copy of the string filled with '0' characters to make it a specified width.
fill_text: str = "text"
print(fill_text.zfill(20))
