# task 2
""" программа, позволяющая запись и чтение из файла .txt"""

with open('users_data.txt', 'w') as users_data:

    name = input("Enter your name: ") 
    print(name)
    age = input("Enter your age: ")
    print(age)
    city = input("Enter your city: ")
    print(city)

    data = f"{name}:{age}:{city}"
    users_data.write(data)

with open('my_file.txt', 'r') as user_file:
    
    for line in user_file:
        print(line)

