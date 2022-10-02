import os
import argparse
from dotenv import load_dotenv

help_dict = {
    "user":         "User to check",
    "multiuser":    "Users to check seperated by , - usr1,usr2,usr3",
    "env":          "Users to check from .env",
    "input":        "Users to check from user entry (in program)",
    "headless":     "Run in headless mode"
}

class Util:
    @staticmethod
    def get_args() -> dict[str, str|list|bool]:
        parser = argparse.ArgumentParser(description='Tiktok clone checker')
        parser.add_argument('-u', '--user',         action='append',        help=help_dict["user"],         required=False)
        parser.add_argument('-m', '--multiuser',                            help=help_dict["multiuser"],    required=False)
        parser.add_argument('-e', '--env',          action='store_true',    help=help_dict["env"],          required=False)
        parser.add_argument('-i', '--input',        action='store_true',    help=help_dict["input"],        required=False)
        parser.add_argument('-s', '--show_browser', action='store_true',    help=help_dict["headless"],     required=False)
        args = vars(parser.parse_args())
        return args

    @staticmethod
    def get_usernames_from_input() -> list:
        usernames = []
        
        while True:
            if len(usernames) > 0:
                print("Press enter to continue...")

            tmp = input("Enter in a username to check: ")

            if tmp == "":
                break
            
            usernames.append(tmp)

            print("Usernames loaded: " + ", ".join(usernames))

        return usernames
        
    @staticmethod
    def get_usernames_from_env() -> list:
        usernames = []

        load_dotenv()

        if os.getenv('USERNAMES'):
            usernames = os.getenv('USERNAMES').split(",")

        return usernames

    @staticmethod
    def get_usernames_from_multiuser(users) -> list:
        return users.split(",")

    @staticmethod
    def get_usernames(args) -> list:
        usernames                   = []
        usernames_from_env          = []
        usernames_from_input        = []
        usernames_from_user         = []
        usernames_from_multiuser    = []
        usernames_full_list         = []

        if args["user"]:
            usernames_from_user         = args["user"]
        
        if args["multiuser"]:
            usernames_from_multiuser    = Util.get_usernames_from_multiuser(args["multiuser"])

        if args["input"]:
            usernames_from_input        = Util.get_usernames_from_input()

        if args["env"]:
            usernames_from_env          = Util.get_usernames_from_env()

        tmp = [usernames_from_user, usernames_from_multiuser, usernames_from_input, usernames_from_env]

        for n in tmp:
            for i in n:
                usernames_full_list.append(i.lower())

        usernames = list(set(usernames_full_list))

        return usernames