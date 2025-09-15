# class Auth:
#     def __init__(self):
#         self.filename = "auth.txt"
#     def register(self, username, password):
#         file=open(self.filename, "r")
#         lines = file.readlines()\
#         # print(lines)
#         file.close()
#         for line in lines:
#             if line.startswith(username + ":"):
#                 print("Username already exists.")
#                 return
#         file=open(self.filename, "a")
#         file.write(f"{username}:{password}\n")   
#         file.close()
# a=Auth()
# a.register("sai", "pass1")
# a.register("sai2", "pass2")
# a.register("sai1", "pass1")

n=int(input("Enter a number: "))
for x in range(1,n+1):
    print(f"{n} x {x} = {n*x}")
