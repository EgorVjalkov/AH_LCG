chaos_bag = [1, 2, 3, 3, 3, 3, 32,-1, -1, -2, -3]
for_cristal = [abs(i) for i in chaos_bag]
#print(for_cristal[1::2])

result = 0

add_point = input('Add any point(s) if you want to correct your skill ')
if add_point.isdigit(): add_point = int(add_point)
else: add_point = 0
print(add_point)
correction = int(add_point) + result
print(correction)