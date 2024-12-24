def to_camel_case(s):
    words = s.split()  
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

input_string = "my name is may"
camel_case_string = to_camel_case(input_string)
print(camel_case_string)


# "my name is may" -> "myNameIsMay"
# " " -> None
# "MY NAME IS MAY" -> "myNameIsMay"
# "my Name Is May" -> "myNameIsMay"

