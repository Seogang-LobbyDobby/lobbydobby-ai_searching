from LectureSearching import Model
from Hanspell import Spell


class LectureRs():
   def lectureRs(self, query):
      hsp = Spell()
      input_query = hsp.spell(query)
      base = Model()
      results = base.search(input_query)

      DF = base.df
      rs = {}
      for result in results:
         idx = DF[DF['title']==result].index
         if result[-3:] != '예체능':
            result = result[:-4]
         else:
            result = result[:-5]

         if len(idx) == 1:
            rs[result] = {
               0: f"수강 가능 여부: {DF['condition'][idx[0]]}",
               1: f" 강좌 계열: {DF['kind'][idx[0]]}",
               2: f"URL 강좌 링크: {DF['url'][idx[0]]}"
            }
         else:
            rs[result] = {
               0: f"수강 가능 여부: {DF['condition'][idx[0]]}",
               1: f"강좌 계열: {DF['kind'][idx[0]]}",
               2: f"URL 강좌 링크: {DF['url'][idx[0]]}",
               3: f"수강 가능 여부: {DF['condition'][idx[1]]}",
               4: f"강좌 계열: {DF['kind'][idx[1]]}",
               5: f"URL 강좌 링크: {DF['url'][idx[1]]}"
            }

      RESULT = {'searchResult':[]}
      RESULT['searchResult'] = rs
      RESULT['editWord'] = input_query
      return RESULT