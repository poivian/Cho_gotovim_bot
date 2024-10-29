
from pathlib import Path
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


MODEL_NAME = "deepvk/USER-bge-m3"
FIASS_DB_PATH = Path(__file__).parent / 'faiss_db'


class Search():
    def __init__(self):
        self.hf_embeddings_model = HuggingFaceEmbeddings(
                model_name=MODEL_NAME, 
                model_kwargs={"device": "cpu"},
                cache_folder=str(Path(__file__).parent / 'model')
                # model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cuda"}
                # model_name="cointegrated/LaBSE-en-ru", model_kwargs={"device": "cpu"}
            )
        self.fiass_db = FAISS.load_local(folder_path=FIASS_DB_PATH, 
                            embeddings=self.hf_embeddings_model, 
                            allow_dangerous_deserialization=True)
        

    def search_relevant_id(self, words:str, k:int=5):
        documents:list[Document] = self.fiass_db.similarity_search_with_score(words,
                                                        k=k)
        return [doc[0].metadata['id'] for doc in documents]


if __name__ == '__main__':
    s = Search()
    s.search_relevant_id('')
