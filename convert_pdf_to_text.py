import fitz  # PyMuPDF
import os

def convert_pdf_to_text(pdf_path, text_file_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Initialize an empty string to store the text
    text = ""
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    # Save the extracted text to a text file
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)
    
    print(f"Text has been saved to {text_file_path}")

# Path to the PDF file
pdf_path = "/path_here.pdf"

# Path to the text file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
text_file_path = os.path.join(desktop_path, "output_text.txt")

# Convert PDF to text
convert_pdf_to_text(pdf_path, text_file_path)
