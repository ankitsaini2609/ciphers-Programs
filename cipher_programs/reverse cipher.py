print("Enter the text which you want in reverse cipher")
s = input()
a = ''
for i in range(len(s)-1,-1,-1):
    a += s[i]
print ("original ",s)
print("Revrse cipher ",a) 
