

name = ["Mayuan", "Lily", "Tom", "Jerry"]
age = [18, 20, 22, 24]

if __name__ == '__main__':
    for name, age in list(zip(name, age)):
        print(f"{name} is {age} years old.")

