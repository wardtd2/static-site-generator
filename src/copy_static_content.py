import os
import shutil

from block_nodes import markdown_to_html_node



def copy_directory_contents(source, target):
    if not os.path.exists(target):
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


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("No h1 heading found")


def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        raise Exception(f"Unable to access source directory: {from_path}")
    if not os.path.exists(template_path):
        raise Exception(f"Unable to access template at {template_path}")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    input_content = None
    with open(from_path, 'r') as input_file:
        input_content = input_file.read()
    template = None
    with open(template_path, 'r') as template_file:
        template = template_file.read()
    
    converted_html = markdown_to_html_node(input_content).to_html()
    page_title = extract_title(input_content)

    dest_directory = os.path.dirname(dest_path)
    print(f"Destination directory: {dest_directory}")
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
    html_with_title = template.replace("{{ Title }}", page_title)
    html_with_body = html_with_title.replace("{{ Content }}", converted_html)
    with open(dest_path, 'w') as output_file:
        output_file.write(html_with_body)
    input_file.close()
    template_file.close()
    output_file.close()
    