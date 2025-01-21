from PyPDF2 import PdfReader, PdfWriter # type: ignore
import os
from reportlab.pdfgen import canvas # type: ignore

#split one pdf to multiple based on pages

input_pdf = "pdd.pdf"
reader = PdfReader(input_pdf)

folder = "splitted_pdfs"

os.makedirs(folder)

for page_num, page in  enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    output_file = f"page_{page_num + 1}.pdf"
    with open(os.path.join(folder, output_file), "wb") as output_pdf:
        writer.write(output_pdf)
    print(f"Saved {output_file}")


#Merging Pdfs:

pdf_files = ["file1.pdf", "file2.pdf"]

writer = PdfWriter()

for pdf in pdf_files:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)
with open("merged.pdf", "wb") as output_pdf:
    writer.write(output_pdf)
print("PDFs merged into merged.pdf")


#Adding Water-Marks:

input_file = "merged.pdf"
watermark_pdf  = "watermark.pdf"
reader = PdfReader(input_file)
watermark_reader = PdfReader(watermark_pdf )

watermark_page = watermark_reader.pages[0]

writer = PdfWriter()
for page in reader.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open("watermarked.pdf", "wb") as output_pdf:
    writer.write(output_pdf)
print("Added Water Marks in watermarked.pdf")


#create a watermark pdf:

def create_watermark(text, output_file="watermark.pdf"):
     c = canvas.Canvas(output_file)
     c.setFont("Helvetica", 40)  # Set font and size
     c.setFillColorRGB(0.8, 0.8, 0.8, alpha=0.5)  # Light gray with transparency
     c.saveState()
     c.translate(300, 500)  # Move to center position
     c.rotate(45)  # Rotate the text
     c.drawString(-100, 0, text)  # Draw the text
     c.restoreState()
     c.save()
     print(f"Watermark file '{output_file}' created successfully.")
create_watermark("CONFIDENTIAL")
