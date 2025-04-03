import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using PyMuPDF (does not require Poppler).
    """
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def save_text_to_file(text, file_path):
    """
    Save extracted text to a file.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"Error saving text to file: {e}")
