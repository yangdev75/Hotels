import os
import datetime
import shutil
import gzip

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


def extract_gz_file(folder: str, file:str, link, french_addresses_path, lieux_dits_path) -> None:
    """This function

    Args:
        folder (str): folder path to clean
    """

    last_update=link.find("span", attrs={'class': 'jsx-2832390685 explorer-link-date'}).text
    last_update = datetime.datetime.strptime(last_update, "%d/%m/%Y").date()
    print(f"\nlinks lastly updated on {last_update}\n")

    with gzip.open(folder + file, 'rb') as f_in:
        filename_without_ext = file.replace(".gz", "")
        brokenddown_filename_without_ext = filename_without_ext.split('.')
        print(brokenddown_filename_without_ext)
        filename_with_date = brokenddown_filename_without_ext[0] + "_" + last_update.strftime("%Y_%m_%d") +".csv"
        print(filename_with_date)

        # adresses and lieux-dits are stored in 2 folders
        if "adresses-" in file:
                target_path = french_addresses_path
        elif "lieux-dits-" in file:
            target_path = lieux_dits_path

        with open(target_path + filename_with_date, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            print(f"{filename_with_date} successfully created")

        # clean memory usage
        del f_in
        del f_out