import os
import requests


def download_pdf(download_link_a, storage_path, num_of_pdf_a):
    if download_link_a is not None:
        path_name = os.path.join(storage_path, r'{}.pdf'.format(str(num_of_pdf_a)))
        response = requests.get(download_link_a, stream="TRUE")
        with open(path_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
            print("Number of {} pdf is done".format(num_of_pdf_a))


# make a loop to read file by lines
with open(r"C:\Users\PC\Desktop\Paper_index.txt") as F:
    file_path = ""
    num_of_pdf = 0
    for line in F:
        line = line.strip('\n')

        # if starts with number 2, then make a file:
        if line.startswith('2'):
            file_path = os.path.join(r'C:\Users\PC\Desktop\Papers2Read', line)
            os.makedirs(file_path)
            print("{} file is done!".format(line))

        # deal with the links
        elif line.endswith("pdf"):
            download_link = line
            # download the files and give them names
            download_pdf(download_link, file_path, num_of_pdf)
            num_of_pdf += 1
        # change the special links
        elif "abs" in line and line.startswith("h"):
            download_link = line.replace("abs", "pdf") + r".pdf"
            # download the files and give them names
            download_pdf(download_link, file_path, num_of_pdf)
            num_of_pdf += 1
        else:
            download_link = None
