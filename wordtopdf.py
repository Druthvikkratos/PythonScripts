import os
from docx2pdf import convert # type: ignore

def convert_word_to_pdf(word_file_path):
    try:
         output_pdf_path = os.path.splitext(word_file_path)[0] + ".pdf"
         convert(word_file_path, output_pdf_path)
         print("Conversion successful. PDF saved")
    except Exception as e:
         print(f"Error occurred during conversion: {e}")
if __name__ == "__main__":
     """
     word_files = [
        r"C:\Angular\my_django_project\pythonscripts\da.docx",
    ]
    
     for word_file_path in word_files:
        convert_word_to_pdf(word_file_path)
    """
        
     word_file = 'da.docx'
     convert_word_to_pdf(word_file)