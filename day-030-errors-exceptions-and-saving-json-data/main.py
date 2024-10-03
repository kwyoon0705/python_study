# try:
#     file = open("text.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("text.txt", "w")
#     file.write("thing")
# except KeyError as error_msg:
#     print(f"{error_msg}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed.")

height = float(input("Height is : "))
weight = int(input("Weight is : "))

if height > 3:
    raise ValueError("The human's height cannot be over 3 meters.")


bmi = weight / height ** 2
print(bmi)
