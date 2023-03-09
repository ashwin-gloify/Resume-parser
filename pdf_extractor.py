from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io

def extract_text_from_pdf(pdf_path):
  with open(pdf_path, 'rb') as fh:
    # iterate over all pages of PDF document
    for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
      # creating a resoure manager
      resource_manager = PDFResourceManager()
      
      # create a file handle
      fake_file_handle = io.StringIO()
      
      # creating a text converter object
      converter = TextConverter(
        resource_manager, 
        fake_file_handle, 
        codec='utf-8', 
        laparams=LAParams()
      )

      # creating a page interpreter
      page_interpreter = PDFPageInterpreter(
        resource_manager, 
        converter
      )

      # process current page
      page_interpreter.process_page(page)
      
      # extract text
      text = fake_file_handle.getvalue()
      yield text

      # close open handles
      converter.close()
      fake_file_handle.close()

# calling above function and extracting text
text =''
for page in extract_text_from_pdf('./test_files/resume1.pdf'):
    text += ' ' + page
    print("text ====>", text)
    # text = text+''+page



# extract_text_from_pdf('./test_files/resume1.pdf');