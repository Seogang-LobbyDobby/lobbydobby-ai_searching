import numpy as np
import pandas as pd
import faiss
import time
from sentence_transformers import SentenceTransformer


df = pd.read_csv("./data/third_preprocessing.csv")
data = df.title.to_list()
model = SentenceTransformer('jhgan/ko-sroberta-multitask')
encoded_data = model.encode(data)

index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
index.add_with_ids(encoded_data, np.array(range(0, len(data))))

def search(query, k=100):
   t = time.time()
   query_vector = model.encode([query])
   top_k = index.search(query_vector, k)
   temp = [data[_id] for _id in top_k[1].tolist()[0]]
   comparison, result = set(temp), []
   for now in temp:
      if now not in result:
         result.append(now)
         if len(result) == len(comparison):
            break
   print('Searching total-time: {}'.format(time.time() - t))
   return result

query = str(input())
results = search(query)

print('Searching results:')
for result in results:
   idx = df[df['title']==result].index
   if len(idx) == 1:
      print(f'\t강좌명: {result[:-4]}')
      print(f"\t-> 수강 가능 여부: {df['condition'][idx[0]]} / 강좌 계열: {df['kind'][idx[0]]} / URL 강좌 링크: {df['url'][idx[0]]}\n")
   else:
      print(f'\t강좌명: {result[:-4]}')
      print(f"\t-> 수강 가능 여부: {df['condition'][idx[0]]} / 강좌 계열: {df['kind'][idx[0]]} / URL 강좌 링크: {df['url'][idx[0]]}\n")
      print(f'\t강좌명: {result[:-4]}')
      print(f"\t-> 수강 가능 여부: {df['condition'][idx[1]]} / 강좌 계열: {df['kind'][idx[1]]} / URL 강좌 링크: {df['url'][idx[1]]}\n")