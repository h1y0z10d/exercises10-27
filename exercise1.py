s = "### # ## #"
my_list = []

for char in s:
	if char=="#":
		my_list.append(1)
	elif char==" ":
		my_list.append(0)

print(my_list)