vs = 5
vt = 1
vp = 1

def transition(starve, temperature, power, health):
	starve -= vs
	temperature -= vt
	power -= vp
	
	if starve < 0 or temperature < 0 or power < 0:
		return 0
	else:
	   return 1

print(transition(10, 10, 10, 10))
print(transition(1, 1, 1, 1))
print(transition(10, 10, 10, 0))