import PyPDF2

# Open the existing PDF file
with open('existing_file.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the first page of the PDF (index starts at 0)
    page = pdf_reader.pages[0]

    # Extract the header and footer content from the existing page
    header = page.extract_text()[:100]  # Assuming the header is the first 100 characters
    footer = page.extract_text()[-100:]  # Assuming the footer is the last 100 characters

    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Create a new page and add the header and footer content
    new_page = PyPDF2.pdf.PageObject.createBlankPage(page)
    new_page.mergeScaledTranslatedPage(page, 1, 0, 0)  # Merge the existing page without modifications
    new_page.drawText(10, 10, header)  # Add the header text
    new_page.drawText(10, 792, footer)  # Add the footer text (assuming page size is 8.5x11 inches)

    # Add the modified page to the writer object
    pdf_writer.addPage(new_page)

    # Save the modified PDF to a new file
    with open('edited_file.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)
