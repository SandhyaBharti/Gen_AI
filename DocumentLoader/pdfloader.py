# pyre
from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("C:\Users\sandh\Downloads\summer-pep\DocumentLoader\GenAI.pdf")

docs = data.load()
print(docs[0].page_content)

