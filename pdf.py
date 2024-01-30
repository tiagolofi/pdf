
from pypdf import PdfReader, PdfWriter
from datetime import datetime

class Pdf():
    
    def __init__(self, file: str = None, list_files: list = None) -> None:
        '''
        Attributes:
            - file: .pdf file or path to file;
            - list_files: .pdf files or paths to files.
        '''
        self.file = file
        self.list_files = list_files
        if file is not None:
            self.length = len(PdfReader(self.file).pages) + 1

    def __call__(self) -> dict:
        if self.file is not None:
            return PdfReader(self.file).metadata
        else:
            return {'Message': 'its a list of files, no metadata available.'}

    def __timestamp(self) -> str:
        '''return a default filename.'''
        return 'file_' + str(int(datetime.now().timestamp())) + '.pdf'

    def join(self, filename: str = None) -> None:
        '''
        Parameters:
            - filename: new name for .pdf file, to default see: self.__timestamp.
        '''
        if filename is None:
            filename = self.__timestamp()
        pdf = PdfWriter()
        for i in self.list_files:
            pdf.append(i)
        pdf.write(filename)
        pdf.close()

    def reorder_resize(self, pages_order: list = None, filename: str = None) -> None:
        '''
        Parameters:
            - pages_order: a list with the new order of the pages, ex: [4, 3, 1, 2];
            - filename: new name for .pdf file, to default see: self.__timestamp.
        '''
        if filename is None:
            filename = self.__timestamp()
        if pages_order is None:
            pages_order = range(1, self.length)
        pdf_reader = PdfReader(self.file)
        pdf_writer = PdfWriter()
        for i in pages_order:
            pdf_writer.add_page(pdf_reader.pages[i - 1])
        pdf_writer.add_metadata(pdf_reader.metadata)
        pdf_writer.write(filename)
        pdf_writer.close()
