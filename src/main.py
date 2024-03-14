import os
import shutil
from inline_nodes import text_node_to_html_node
from textnode import TextNode



def copy_directory_contents(source, target):
    print(f"Clearing the {target} directory")
    shutil.rmtree(target)
    os.mkdir(target)
    if not os.path.exists(source):
        raise Exception("Unable to access source directory")
    source_items = os.listdir(source)
    for item in source_items:
        print(f"Current item: {item}")
        if os.path.isfile(os.path.join(source, item)):
            print(f"{item} is a file. Copying to {target}")
            shutil.copy(os.path.join(source, item), os.path.join(target, item))
        else:
            print(f"{item} is a directory. Creating {os.path.join(target, item)}")
            os.mkdir(os.path.join(target, item))
            print(f"Copying the contents of {os.path.join(source, item)} to {os.path.join(target, item)}")
            copy_directory_contents(os.path.join(source, item), os.path.join(target, item))
def main():
    copy_directory_contents("static", "public")


main()