new_dict ={"A":23, "B":56, "C":29, "D":42, "E":29}
max = max(new_dict.values())
max2 = 0
for v in new_dict.values():
     if(v>max2 and v<max):
            max2 = v
print(max2)