#Fetch .pdb, run Foldseek, fetch result .m8 file

#Fetching .pdb of the original input protein
import os

pdb_folder = "fold_tree/fromseq/structs"


identifiers_file = "identifiers.txt"
with open(identifiers_file, 'r') as f:
    first_line = f.readline().strip()  

pdb_file = os.path.join(pdb_folder, first_line + ".pdb")

if os.path.exists(pdb_file):
    print(f"Path to {first_line}.pdb:", pdb_file)
else:
    print(f"No .pdb file found for {first_line}.")


#Running Foldseek

import requests
import time

file_path = pdb_file

def submit_input_file(file_path):
    url = 'https://search.foldseek.com/api/ticket'
    files = {'q': open(file_path, 'rb')}
    data = {
        'mode': '3diaa',
        'database[]': ['afdb-swissprot']
    }
    response = requests.post(url, data=data, files=files)
    if response.status_code == 200:

        ticket_id = response.json()['id']
        return ticket_id
    else:
        print("Error submitting input file:", response.status_code)
        return None


def check_job_status(ticket):
    url = f'https://search.foldseek.com/api/ticket/{ticket}'
    response = requests.get(url)


    if response.status_code == 200:
        status = response.json()["status"]
        if status == "complete":
            return response.json()
        elif status == "error":
            print("Error occurred while processing job.")
            return None
        else:
            print(f"Job status: {status}. Waiting....")
            time.sleep(5)
    else:
        print("Error checking job status:", response.status_code)
        return None

#Parsing output file
import tarfile

def download_output_file(ticket):
    url = f'https://search.foldseek.com/api/result/download/{ticket}'
    response = requests.get(url)
#    filename = f"{ticket}.tar.gz"
    if response.status_code == 200:
        with open(f'{ticket}.tar.gz', 'wb') as f:
            f.write(response.content)
        print("Output file downloaded successfully,")
    else:
        print("Failed to download output file. Status code:", response.status_code)


def extract_m8_file(filename, extraction_path="."):
    with tarfile.open(filename, "r:gz") as tar:
         m8_file = tar.extractfile("alis_afdb-swissprot.m8") 
         if m8_file:
             print("Extracted:")
             m8_contents = m8_file.read().decode('utf-8')
             

             save_path = os.path.join(extraction_path,"alis_afdb-swissprot.m8")
             with open(save_path, "w") as f:
                 f.write(m8_contents)
         else:
             print("file not found")

if __name__ == "__main__":

    file_path = pdb_file


    ticket = submit_input_file(file_path)
    print("Ticket:", ticket)


    job_status = check_job_status(ticket)
    print("Job status:", job_status)


    download_output_file(ticket)
    print("Output file downloaded.")
    
    filename = f"{ticket}.tar.gz"
    print(filename)
    
    extraction_path = "pipeline/"

    extract_m8_file(filename)
    print("Result file is saved.")



