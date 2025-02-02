# CSV Alpha-2 Code Extractor

This Python script extracts Alpha-2 country codes from a CSV file (https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv) and provides different ways to output them, either to the clipboard, a text file, or directly to the console. The script supports two output formats: "single" (just the country code) and "dual" (country code in a formatted `key = "value"` style).

## Requirements
- Python 3.x
- `pyperclip` library for clipboard functionality

You can install the required library using pip:
```bash
pip install -r requirements.txt
```

## Usage

1. **Input CSV File**  
   The script requires a CSV file.

2. **Output Type**  
   You will be prompted to choose the type of output:
   - `clipboard`: Copies the extracted Alpha-2 codes to your clipboard.
   - `file`: Writes the extracted Alpha-2 codes to an output text file (`output.txt`).
   - `console`: Prints the extracted Alpha-2 codes to the console.

3. **Output Format**  
   You will also be prompted to select the format of the output:
   - `single`: Extracts just the Alpha-2 country code.
   - `dual`: Outputs the Alpha-2 codes in a formatted style, e.g., `US = "US",`.
