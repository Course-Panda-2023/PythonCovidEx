import base64
import os


# Function to rename multiple files
def main():
    path = "C:\\Users\\******Your_User*****\\Desktop\\python_assignment\\ex1"
    os.chdir(path)
    for filename in os.listdir(path):
        encrypted_base32_filename = filename
        decrypted_filename = base64.b32decode(encrypted_base32_filename).decode('utf-8')
        source = path + "\\" + filename
        os.rename(source, decrypted_filename)


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
