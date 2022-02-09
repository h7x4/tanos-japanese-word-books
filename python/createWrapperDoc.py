from sys import argv

from PyPDF2 import PdfFileReader

def inject_into_template(
  output_file,
  string,
  template='tex/doc.tex.template',
  replacement_char='###'
):
  with open(template) as file:
    content = file.read().replace(replacement_char, string)
  
  with open(output_file, 'w') as file:
    file.write(content)

if __name__ == "__main__":
  pdfPath, outputPath = argv[1:3]
  pdf = PdfFileReader(open(f'build/{pdfPath}','rb'))
  pageNum = pdf.getNumPages()

  inject_into_template(
    f'build/{outputPath}',
    f'\\includepdf[pages=-,nup=1x2,signature={pageNum},landscape,booklet=true]{{{pdfPath}}}',
    template="tex/wrapper.tex.template"
  )