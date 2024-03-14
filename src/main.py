import shutil
from copy_static_content import copy_directory_contents



def main():
    print(f"Clearing the public directory")
    shutil.rmtree("public")
    copy_directory_contents("static", "public")


main()