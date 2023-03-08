import os, base64

hi = base64.b32decode("IFRXI2LWMU======")
print(str(hi)[2:-1])

path = "C:/Users/User/Desktop/C#/Python/ex1/"
for filename in os.listdir(path):
    my_source = path + filename
    my_dest = path + (str(base64.b32decode(filename))[2:-1])
    os.rename(my_source, my_dest)