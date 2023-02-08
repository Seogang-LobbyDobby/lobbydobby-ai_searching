import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


# raw_data = {'button':[
#     '마이룸 이동, 월드 이동', '클럽월드 이동, 월드 이동', '광장 이동, 월드 이동',
#     '강의실 메뉴 열기', '클럽 메뉴 열기', '온라인 강의 메뉴 열기', '일정 메뉴 열기', '공지 메뉴 열기', '내정보 메뉴 열기', '메신저 메뉴 열기', '설정 메뉴 열기',
#     '클럽 검색, 기능', '일정 등록, 기능', '온라인 강의 검색, 기능', '강의실 입장, 기능', '클럽 회의실 입장, 기능',
#     '종료'
# ]}
# data = pd.DataFrame(raw_data)
# data.to_csv('button_data.csv', index=False)


class Model():
    def __init__(self):
        self.df = pd.read_csv("button_data.csv")
        self.data = self.df.button.to_list()
        self.model = SentenceTransformer('jhgan/ko-sroberta-multitask')
        # self.encoded_data = self.model.encode(self.data)
        #
        # self.index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
        # self.index.add_with_ids(self.encoded_data, np.array(range(0, len(self.data))))
        # faiss.write_index(self.index, 'button_index')

    def search(self, query, k=3):
        index = faiss.read_index('button_index')
        query_vector = self.model.encode([query])
        top_k = index.search(query_vector, k)

        return [self.data[_id] for _id in top_k[1].tolist()[0]]