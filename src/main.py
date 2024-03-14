import os
import shutil
from copy_static_content import copy_directory_contents, generate_page, generate_pages_recursive



def main():
    print(f"Clearing the public directory")
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_directory_contents("static", "public")

    generate_pages_recursive("content", "template.html", "public")


main()