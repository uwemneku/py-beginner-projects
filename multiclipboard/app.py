import sys
import clipboard
from items import load_items, save_items


CLI_COMMANDS = ["save", "load", "list", "about", "del"]
SAVED_DATA = "savedClipboard.json"
data = load_items(SAVED_DATA)


def start(cmd: str):
    match cmd:
        case "save":
            key = input("Enter a key : ")
            current_clipboard_content = clipboard.paste()
            data[key] = current_clipboard_content
            save_items(SAVED_DATA, data)
        case "load":
            key = input("Enter a key : ")
            if key in data:
                clipboard.copy(data[key])
                print(f"{data[key]} has been copied to your keyboard")
            else:
                print(f"{key} is not saved")
        case "del":
            key = input("Enter a key : ")
            if key in data:
                del data[key]
                save_items(SAVED_DATA, data)
                print(f"{data[key]} has been deleted")
            else:
                print(f"{key} is not saved")
        case "list":
            print(data)
            ""
        case _:
            print("Invalid Command")


if len(sys.argv) == 2:
    cli_args = sys.argv[1:]
    command = cli_args[0]
    if command in CLI_COMMANDS:
        print("Starting cli app")
        start(command)
    else:
        print("Invalid Command")
