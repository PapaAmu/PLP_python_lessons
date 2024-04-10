try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, my name is Themba.\n")
        file.write("I have created this file using python\n")
        file.write("I am currently learning coding with PLP\n")
except PermissionError:
    print("Permission denied to create or write to the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File reading process completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("And I am currently enoying Python\n")
        file.write("Upon completion with PLP, I intend to design amazing things\n")
        file.write("We will talk some other time, bye and thank you for your time\n")
except PermissionError:
    print("Permission denied to append to the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process completed.")