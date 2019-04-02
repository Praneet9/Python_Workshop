def simpleGeneratorFun(): 
    print("First Print")
    yield 1
    print("Second Print")
    yield 2
    print("Third Print")
    yield 3

for value in simpleGeneratorFun():  
    print(value)