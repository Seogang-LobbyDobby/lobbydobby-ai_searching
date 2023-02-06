import pandas as pd
import numpy as np
import faiss
import time
from sentence_transformers import SentenceTransformer


class Model():
    def __init__(self):
        self.df = pd.read_csv("./data/third_preprocessing.csv")
        self.data = self.df.title.to_list()
        self.model = SentenceTransformer('jhgan/ko-sroberta-multitask')
        # self.encoded_data = self.model.encode(self.data)
        #
        # self.index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
        # self.index.add_with_ids(self.encoded_data, np.array(range(0, len(self.data))))
        # faiss.write_index(self.index, 'now_index')

    def search(self, query, k=100):
        t = time.time()
        index = faiss.read_index('now_index')
        query_vector = self.model.encode([query])
        top_k = index.search(query_vector, k)
        temp = [self.data[_id] for _id in top_k[1].tolist()[0]]
        comparison, result = len(set(temp)), []
        for now in temp:
            if now not in result:
                result.append(now)
                if len(result) == comparison:
                    break
        print('Searching total-time: {}'.format(time.time() - t))

        return result