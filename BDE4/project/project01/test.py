phone = input("phone number: ")
#if '-' in phone:
#    phone = "".join(phone.split('-'))
print(phone)

print("".join(list(map(lambda x: x != '-', phone))))
