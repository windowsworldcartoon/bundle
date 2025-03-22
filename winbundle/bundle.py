import os

def main():
    while True:
        command = input("(WinBundle) ")

        if command == "help":
            print("help - Display this help message")
            print("exit - Exit the program")
            print("cd - Change the current directory")
            print("ls - List the contents of the current directory")
            print("mkdir - Create a new directory")
            print("rmdir - Remove a directory")
            print("rm - Remove a file")
            print("cat - Display the contents of a file")
            print("echo - Display a message")
            print("clear - Clear the screen")
            print("\033[90mhistory - Display the command history (coming soon)\033[0m")
            print("alias - Create an alias for a command")
            print("unalias - Remove an alias")
            print("\033[90mset - Set an environment variable (coming soon)\033[0m")
            print("\033[90munset - Unset an environment variable (coming soon)\033[0m")
            print("\033[90mexport - Export an environment variable (coming soon)\033")
            print("\033[90munsetenv - Unset an environment variable (coming soon)\033[0m")
            print("env - Display the environment variables")
            print("pwd - Display the current working directory")
            print("cdpath - Set the search path for the cd command")
            print("path - Set the search path for the command interpreter")
            print("hash - Display the hash table for the command interpreter")
        elif command == "exit":
            break
        elif command == "cd":
            while True:
             directory = input("Enter directory: ")
             try:
                os.chdir(directory)
                print(f"Current directory: {os.getcwd()}")
             except FileNotFoundError:
                print("Directory not found.")
             except NotADirectoryError:
                print(f"\033[91m'{directory}' is not a directory.\033[0m")


        elif command == "ls":
            print(os.listdir())

        elif command == "mkdir":
            directory = input("Enter directory name: ")
            try:
                os.mkdir(directory)
                print(f"Directory '{directory}' created.")
            except FileExistsError:
                print(f"Directory '{directory}' already exists.")

        elif command == "rmdir":
            directory = input("Enter directory name: ")
            try:
                os.rmdir(directory)
                print(f"Directory '{directory}' removed.")
            except FileNotFoundError:
                print(f"Directory '{directory}' not found.")

        elif command == "touch":
            filename = input("Enter filename: ")
            try:
                open(filename, 'w').close()
                print(f"File '{filename}' created.")
            except FileExistsError:
                print(f"File '{filename}' already exists.")

        elif command == "rm":
            filename = input("Enter filename: ")
            try:
                os.remove(filename)
                print(f"File '{filename}' removed.")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")

        elif command == "cat":
            filename = input("Enter filename: ")
            try:
                with open(filename, 'r') as file:
                    print(file.read())
            except FileNotFoundError:
                print(f"File '{filename}' not found.")

        elif command == "edit":
            filename = input("Enter filename: ")
            try:
                os.system(f'notepad {filename}')
            except FileNotFoundError:
                print(f"File '{filename}' not found.")

        

        elif command == "run":
            filename = input("Enter filename: ")

            if os.path.isfile(filename):
                if filename.endswith('.js'):
                    os.system(f'node {filename}')
                elif filename.endswith('.py'):
                    os.system(f'python {filename}')
                else:
                    print(f"Unsupported file type: {filename}")
            else:
                print(f"\033[91mFile '{filename}' not found.\033[0m")
                print(f"\033[91mPlease make sure the file exists and has the correct extension.\033[0m")
                print(f"\033[91mFor example, if you want to run a JavaScript file, make sure it has the .js extension.\033[0m")
            

        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()