from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

from configparser import ConfigParser
import os

config = ConfigParser()
config.read("config.ini")

DATA_PATH = config["faiss"]["data"]
FAISS_DATA_PATH = config["faiss"]["faiss_data_path"]
CHUNK_SIZE = int(config["faiss"]["chunk_size"])
CHUNK_OVERLAP = int(config["faiss"]["chunk_overlap"])

EMBEDDING_MODEL = config["huggingface"]["embedding_model"]

class VectorDataBase(FAISS):
    def __init__(self) -> None:
        self.embeddings_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL, model_kwargs={"device": "cpu"}
        )
        self.data_directory = os.path.join(DATA_PATH, "api_documentation")
        self.db = None
    
    def load_db(self):
        self.db = FAISS.load_local(FAISS_DATA_PATH, self.embeddings_model)

    def txt_loader(self) -> DirectoryLoader:
        loader = DirectoryLoader(
            path=self.data_directory, glob="*.txt", loader_cls=TextLoader
        )

        return loader

    def create_vector_db(self):
        loader = self.txt_loader()
        documents = loader.load()
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
        text = splitter.split_documents(documents)

        self.db = FAISS.from_documents(documents=text, embedding=self.embeddings_model)

        self.db.save_local(FAISS_DATA_PATH)

        return self.db

    def retrieve_using_similarity_search(self, query: str, top_k: int = 5):
        if self.db is not None:
            return self.db.similarity_search(query, k=top_k)

if __name__ == "__main__":
    vector_db = VectorDataBase()
    vector_db.create_vector_db()
    print(vector_db.retrieve_using_similarity_search("give me my id", 1))