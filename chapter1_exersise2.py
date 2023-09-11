#!.env/bin/ipython3

def lowerfunc(input: str):
	return (x.upper() for x in input)
	
lower = lowerfunc('abcde')
print(next(lower))
print(next(lower))
