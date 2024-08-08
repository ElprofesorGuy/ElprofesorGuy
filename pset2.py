"""print("Hello world!!!")
print("Is very too strong")"""

s="6.00 is 6.0001 and 6.002"
string=""
string += s[-1]
string += s[0]
string += s[4::30]
string += s[13:10:-1]
print(string)