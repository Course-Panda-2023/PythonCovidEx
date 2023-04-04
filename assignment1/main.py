import base64
import os


def main():
    path = "C:\\Users\\******Your_User*****\\Desktop\\python_assignment\\ex1"
    os.chdir(path)
    for encrypted_base32_filename in os.listdir(path):
        decrypted_filename = base64.b32decode(encrypted_base32_filename).decode('utf-8')
        source = path + "\\" + encrypted_base32_filename
        os.rename(source, decrypted_filename)


if __name__ == '__main__':
    main()
