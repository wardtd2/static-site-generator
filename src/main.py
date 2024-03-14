import shutil
from copy_static_content import copy_directory_contents, generate_page



def main():
    print(f"Clearing the public directory")
    shutil.rmtree("public")
    copy_directory_contents("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")


main()