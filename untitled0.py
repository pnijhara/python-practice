string = 'Wheresoever you go, go with all your heart'   # or you can get an input from user
lstring = string.lower()				# for converting string characters to lowercase
l= lstring.split()					# spliting string on behalf of spaces, split() will convert string to list of string
s = ''							# empty string 
for i in range(0, len(l)):
    if  l[i].isalpha():
        s = s+l[i]
        if s[0]>"g":
            print(s.upper())
            s = ""
        else:
            s = ""
    else:
        s = ""