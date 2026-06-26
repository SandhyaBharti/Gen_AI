# pyrefly: ignore [missing-import]
from langchain_community.document_loaders import TextLoader


loader = TextLoader("C:/Users/sandh/Downloads/summer-pep/DocumentLoader/notes.txt")
docs = loader.load()
print(docs[0].page_content)


