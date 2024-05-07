def SkatGen():
    values = ['7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    colours = ['Kreuz','Pik','Herz','Karo']
    for colour in colours:
        for value in values:
            yield colour, value
            
iterator = SkatGen()
for i in iterator:
    print(i)
    
def range(start, stop = None, step = 1):
    if step == 0:
            raise ValueError("range() arg 3 must not be zero")
    if stop == None:
        stop = start
        start = 0
    while start > stop and step < 0 or start < stop and step > 0:
        yield start
        start += step

print(list(range(10)))
print(list(range(20,2,-2)))
print(list(range(-20)))