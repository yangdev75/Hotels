import os
import datetime
import shutil

def get_date_in_filename(folder: str):
    pass
    file_breakdown = os.listdir(folder)[0].split("_")
    file_year=file_breakdown[1]
    file_month=file_breakdown[2]
    file_day=file_breakdown[-1].split('.')[0]
    filedate = datetime.datetime.strptime(f"{file_day} {file_month} {file_year}", "%d %m %Y")
    # print(f"current file date is {filedate.date()}")
    return filedate.date()




def delete_files_or_folder(folder: str) -> None:
    """This function remove all files into specific folder

    Args:
        folder (str): folder path to clean
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    print(f"The folder {folder} is clean")