import sys
import subprocess
import os


args = sys.argv[1:]

if not args:
    print("no command provided")
    sys.exit()

command = args[0]
options = args[1:]

if not os.path.exists(".git"):
    print("Error: Not a git repository!")
    sys.exit()

match command:
    case "push":
        subprocess.run(["git", "push", *options])
    case "commit":
        if "-m" not in options:
            options.extend(["-m", input("Commit Message: ")])
        subprocess.run(["git", "commit", *options])
    case "add":
        subprocess.run(["git", "add", *options])
    case "remote":
        subprocess.run(["git", "remote", *options])
    case "init":
        subprocess.run(["git", "init", *options])
    case "pushup":
        subprocess.run(["git", "add", "."])
        if "-m" not in options:
            message = input("Commit Message: ")
            if not message:
                print("Aborted: Commit Message Cannot be empty")
                sys.exit()
            options.extend(["-m", message])
        subprocess.run(["git", "commit", *options])
        subprocess.run(["git", "push"])
    case _:
        subprocess.run(["git", command, *options])
