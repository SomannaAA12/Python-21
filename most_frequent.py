X = input("Please enter a string: ")
def most_frequent(string):
    y = dict()
    for key in string:
        if key not in y:
            y[key] = 1
        else:
            y[key] += 1
    return y
print(most_frequent(X))
