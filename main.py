import csv
import pyperclip

def extract_alpha2_codes(file_name: str, output_format):
    alpha2_codes = []

    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        next(csv_reader)

        for row in csv_reader:
            if len(row) >= 2:
                if output_format == "single":
                    alpha2_codes.append(row[1])
                elif output_format == "dual":
                    alpha2_codes.append(f'{row[1]} = "{row[1]}",')

    return "\n".join(alpha2_codes)


def output_csv_data(output_type: str, file_name: str, output_format: str):
    match output_type:
        case 'clipboard':
            pyperclip.copy(extract_alpha2_codes(file_name))
            print("Alpha-2 codes have been copied to clipboard!")
        case 'file':
            file = open("outputfile.txt", "w")
            file.write(extract_alpha2_codes(file_name))
            file.close()
            print("Output has been written to ./output.txt!")
        case _:
            print(extract_alpha2_codes(file_name, output_format))

if __name__ == "__main__":
    file_name = input("Enter the path of the CSV file: ")
    option = input("Choose an output type: ")
    format = input("Choose an output format: ")
    output_csv_data(option, file_name, format)
