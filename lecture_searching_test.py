import time
from LectureSearching import Model
from Symspell import Spell


sp = Spell()
query = str(input())
t = time.time()
input_query = sp.spell(query)
print(input_query)
base = Model()
results = base.search(input_query)
print('Searching total-time: {}'.format(time.time() - t))

print('Searching results:')
DF = base.df
for result in results:
   idx = DF[DF['title']==result].index
   if result[-3:] != '예체능':
      result = result[:-4]
   else:
      result = result[:-5]

   if len(idx) == 1:
      print(f'\t강좌명: {result}')
      print(f"\t-> 수강 가능 여부: {DF['condition'][idx[0]]} / 강좌 계열: {DF['kind'][idx[0]]} / URL 강좌 링크: {DF['url'][idx[0]]}\n")
   else:
      print(f'\t강좌명: {result}')
      print(f"\t-> 수강 가능 여부: {DF['condition'][idx[0]]} / 강좌 계열: {DF['kind'][idx[0]]} / URL 강좌 링크: {DF['url'][idx[0]]}\n")
      print(f'\t강좌명: {result}')
      print(f"\t-> 수강 가능 여부: {DF['condition'][idx[1]]} / 강좌 계열: {DF['kind'][idx[1]]} / URL 강좌 링크: {DF['url'][idx[1]]}\n")