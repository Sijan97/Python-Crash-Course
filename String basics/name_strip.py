name = "    Sijan Shrestha    "
print(f"whitespace{name}whitespace")
left_strip = name.lstrip()
right_strip = name.rstrip()
full_strip = name.strip()

"""
lstrip is used to remove white space in the beginning of string
rstrip is used to remove white space at the end of string
strip is used to remove white space in both sides of string
"""
#Using backslash"\" to begin coding in new line
print(f"Strip cases:\
	\n\tLeft Strip: no space in left{left_strip}Still space in right\
	\n\tRight Strip: Still space in left{right_strip}no space in right\
	\n\tFull Strip:no space at all{full_strip}no space at all")