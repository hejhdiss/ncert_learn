import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize a variable to hold all text
        text = ""
        
        # Loop through all the pages and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
    return text

def save_text_to_file(text, output_file):
    # Save the extracted text to a text file with utf-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)


