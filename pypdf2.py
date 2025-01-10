# # import PyPDF2
# # #1)reading the pdf file

# # #open a pdf file
# # f= open("manvir.pdf","rb")
# # reader=PyPDF2.PdfReader(f)
# # #count total pages in pdf
# # total_pages=len(reader.pages)
# # print(f"total pages are: {total_pages}")

# # #read content of first page of pdf file
# # firstpage=reader.pages[0]
# # text=firstpage.extract_text()
# # print(text)
# # f.close()


# #2) extracting text from pdf files:-  We can easily extract text from PDF files using the extract_text() function.
# #  This can be useful for parsing large documents.
# # import PyPDF2

# # with open('manvir.pdf', 'rb') as pdf_file:
# #     reader = PyPDF2.PdfReader(pdf_file)

# #     for page in reader.pages:
# #         print(page.extract_text())

# # #3 extract metadata from pdf files
# # with open('manvir.pdf','rb') as pdf_file:
# #     reader=PyPDF2.PdfReader(pdf_file)
# #     metadata=reader.metadata
# #     print(f"author name:{metadata.author}")
# #     print(f"Title:{metadata.title}")
# #     print(f"creation date:{metadata.creation_date}")

# # import os

# # if os.path.exists(r"c:\Users\Win\Documents\intro.pdf"):
# #     print("file exists")
# # else:
# #     print("file does not exist")
# #merging two pdfs
# from PyPDF2 import PdfReader, PdfWriter

# # Specify the absolute paths to your PDF files
# pdf_files = [ r"c:\Users\Win\Desktop\manvir.pdf",   r"c:\Users\Win\Desktop\intro.pdf"]

# pdf_writer = PdfWriter()

# # Add PDFs to merge
# for pdf_file in pdf_files:
#     reader = PdfReader(pdf_file)
#     for page in reader.pages:
#         pdf_writer.add_page(page)

# # Save the merged PDF
# with open(r"c:\Users\Win\Desktop\merged.pdf", 'wb') as output_file:
#     pdf_writer.write(output_file)

# print("PDFs merged successfully!")


# #3)Splitting PDF Files into Individual Pages
# import PyPDF2

# with open('merged.pdf', 'rb') as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)

#     for i, page in enumerate(reader.pages):
#         writer = PyPDF2.PdfWriter()
#         writer.add_page(page)

#         # Save each page as a new file
#         with open(f'page_{i+1}.pdf', 'wb') as output_pdf:
#             writer.write(output_pdf)

#4)encryt pdf with password################
from PyPDF2 import PdfReader, PdfWriter

# Specify the path to the PDF you want to encrypt
input_pdf_path = r"c:\Users\Win\Desktop\manvir.pdf"  # Path to the existing PDF
output_pdf_path = r"c:\Users\Win\Desktop\manvir_encrypted_v2.pdf"  # Path for the encrypted PDF

# Set a password for the PDF
password = "abc"  # Replace with your desired password

# Open the existing PDF
with open(input_pdf_path, "rb") as input_pdf_file:
    reader = PdfReader(input_pdf_file)
    writer = PdfWriter()

    # Add all pages from the existing PDF to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Encrypt the PDF with the password
    writer.encrypt(password)

    # Save the encrypted PDF
    with open(output_pdf_path, "wb") as output_pdf_file:
        writer.write(output_pdf_file)

print(f"PDF encrypted successfully! Encrypted PDF saved as {output_pdf_path}")








