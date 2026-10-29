
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 1', 'Carol': 'Sep 22'}

while True:
    print("Enter a name: (blank to exit)")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + " is the brithday for " + name)
    else:
        print('I do not have birthday information for ' + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated")