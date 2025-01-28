# iso2



import csv
import pyperclip

def extract_alpha2_codes(file_name):
    alpha2_codes = []
    
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header if present
        next(csv_reader)
        
        # Extract and store only the alpha-2 codes (second column)
        for row in csv_reader:
            if len(row) >= 2:
                alpha2_codes.append(row[1])  # row[1] is the alpha-2 code
    
    # Convert list of alpha-2 codes to a string
    result = "\n".join(alpha2_codes)
    
    # Copy the result to the clipboard
    pyperclip.copy(result)
    print("Alpha-2 codes have been copied to clipboard!")

if __name__ == "__main__":
    # Prompt user for the CSV file path
    file_name = input("Enter the path to the CSV file: ")
    extract_alpha2_codes(file_name)





import csv

def extract_alpha2_codes(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header if present
        next(csv_reader)
        
        # Extract and print only the alpha-2 codes (second column)
        for row in csv_reader:
            if len(row) >= 2:
                print(row[1])  # row[1] is the alpha-2 code

if __name__ == "__main__":
    # Prompt user for the CSV file path
    file_name = input("Enter the path to the CSV file: ")
    extract_alpha2_codes(file_name)




import csv

def extract_alpha2_codes(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header if present
        next(csv_reader)
        
        # Extract and print the alpha-2 codes in the required format
        for row in csv_reader:
            if len(row) >= 2:
                country_code = row[1]
                print(f'{country_code} = "{country_code}",')

if __name__ == "__main__":
    # Prompt user for the CSV file path
    file_name = input("Enter the path to the CSV file: ")
    extract_alpha2_codes(file_name)


    
