import customtkinter
from Application import Application
from Utility import print_default_error_message

def main():
    try:
        root = customtkinter.CTk()
        app = Application(root)
        try:
            root.mainloop()
        except Exception as e:
            print_default_error_message(e)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")


if __name__ == '__main__':
    main()
