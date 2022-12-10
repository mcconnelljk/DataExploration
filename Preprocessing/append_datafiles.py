import pandas as pd
import glob
import os


def main_menu():
    path = os.getcwd()
    directories = print_directories(path)
    folder = print_menu(directories)
    folder_path = path + "/" + folder
    return folder_path


def print_directories(path):
    print('\n DIRECTORIES LIST')
    directories = os.listdir(path)
    for folder in directories:
        print(folder)
    return directories


def print_menu(directories):
    folder = input('\nType a folder name to merge its contents: \n')
    if folder in directories:
        return folder
    elif folder == 'q' or 'Q':
        return quit()
    else:
        print('\n* * *\nNo such folder\nEnter a folder in the directories list\n or \'q\' to Quit\n* * *')
        return print_menu(directories)


def merge_csv(folder):
    files = glob.glob(folder + "/*.csv")
    df = pd.concat((pd.read_csv(file) for file in files))
    df.to_csv(folder + "/master.csv", index=False)
    return print(df.info())


def merge_again():
    to_merge = input('Merge another folder? [Y/N]')
    if to_merge == 'Y' or 'y':
        return main_menu()
    elif to_merge == 'N' or 'n':
        return quit()
    else:
        print('Invalid input')
        return merge_again()


def main():
    folder_path = main_menu()
    merge_csv(folder_path)
    merge_again()
    return


if __name__ == '__main__':
    main()