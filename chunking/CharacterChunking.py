from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
data = TextLoader("C:\\Users\\User\\Documents\\LangChain\\data\\sample.txt")
splitter = CharacterTextSplitter(separator="", chunk_size=20, chunk_overlap=1)
docs=data.load()
chunks = splitter.split_documents(docs)
# print(chunks)
for i in chunks:
    print(i.page_content)
    print()

# recursive text splitter-i can pass array of separators and it will split the text recursively based on the separators provided. It will first split the text based on the first separator, then it will split the resulting chunks based on the second separator, and so on. This is useful when you have a text that has multiple levels of structure, such as paragraphs, sentences, and words.

from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=20,
    chunk_overlap=1,
)