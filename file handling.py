



def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is line 2 with a number: 123\n")
            file.write("Mixing strings and numbers: 456, Python is fun!\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied to create file.")
    except Exception as e:
        print(f"Error creating file: {e}")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appended line 1: This is new content.\n")
            file.write("Appended line 2 with number: 789\n")
            file.write("Appended line 3: More content added.\n")
        print("File updated successfully.")
    except PermissionError:
        print("Permission denied to update file.")
    except Exception as e:
        print(f"Error updating file: {e}")


def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Display updated contents


if __name__ == "__main__":
    main()
