# Utils for PDF files

## Installation

```
pip install pypdf
```

## How to Use

```python
from pdf import Pdf

pdf = Pdf(file = 'File.pdf')

print(pdf.__call__()) # metadata file
```

#### Juntar PDFs

```python
list_pdfs = Pdf(list_files = ['File 1.pdf', 'File 2.pdf'])

list_pdfs.join(filename = 'New Name.pdf') # create new file called 'New Name.pdf' (filename parameter)
```

#### Reordenar/Excluir Páginas

```python
pdf = Pdf(file = 'File.pdf')

pdf.reorder(pages_order=[3, 2, 4, 1]) # filename is default
```

#### Cortar

_Soon_