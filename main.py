from Models import Model


query = str(input())
base = Model()
results = base.search(query)

print('Searching results:')
DF = base.df
for result in results:
   idx = DF[DF['title']==result].index
   if len(idx) == 1:
      print(f'\t강좌명: {result[:-4]}')
      print(f"\t-> 수강 가능 여부: {DF['condition'][idx[0]]} / 강좌 계열: {DF['kind'][idx[0]]} / URL 강좌 링크: {DF['url'][idx[0]]}\n")
   else:
      print(f'\t강좌명: {result[:-4]}')
      print(f"\t-> 수강 가능 여부: {DF['condition'][idx[0]]} / 강좌 계열: {DF['kind'][idx[0]]} / URL 강좌 링크: {DF['url'][idx[0]]}\n")
      print(f'\t강좌명: {result[:-4]}')
      print(f"\t-> 수강 가능 여부: {DF['condition'][idx[1]]} / 강좌 계열: {DF['kind'][idx[1]]} / URL 강좌 링크: {DF['url'][idx[1]]}\n")