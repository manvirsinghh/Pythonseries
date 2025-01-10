from PyPDF2 import PdfReader,PdfWriter
import os
# this is program to merge  files that are in same folder
folder_path=r"c:\Users\Win\Documents"
# Alternatively, you can use forward slashes
# folder_path = "C:/Users/Win/Documents"

pdf_files=[f for f in os.listdir(folder_path) if f.endswith('.pdfs')]
pdf_files.sort()#optional ,sort the files alphabetically
pdf_writer = PdfWriter()
for pdf_file in pdf_files:
    file_path = os.path.join(folder_path, pdf_file)  # Full path to the file
    reader = PdfReader(file_path)
    for page in reader.pages:
        pdf_writer.add_page(page)

# Save the merged PDF
with open('merged.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)

print("PDFs merged successfully!")


#will take care of this error as this happen frequently in windows 
#The error you're encountering (SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes) happens because backslashes (\) 
# in Windows paths are treated as escape characters in Python strings. To avoid this issue, you can either:

# Use raw string literals (r"..."), which will treat backslashes as literal characters.
# Use forward slashes (/), which are also supported by Python in file paths.
# Escape backslashes manually by doubling them (\\).