import os


def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    # list directory contents
    dir_list = os.listdir(abs_directory)
    content = format_report(dir_list, abs_directory)
    return "\n".join(content)


def format_report(list, directory):
    content = []
    for item in list:
        joined = os.path.join(directory, item)
        file_size = os.path.getsize(joined)
        is_dir = os.path.isdir(joined)

        content.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
    return content
