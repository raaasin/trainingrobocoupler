a="abcDEF"
z=set(a)
print("lenght = ",len(a))
print("lenght of smaller case = ",len(z-set(a.upper())))
print("Lenght of uppercase = ",len(z)-len(z-set(a.upper())))
