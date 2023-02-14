from LectureSearching import Model
from Symspell import Spell


class LectureRs():
   def lectureRs(self, query):
      sp = Spell()
      input_query = sp.spell(query)
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
            rs[result] = [f"수강 가능 여부: {DF['condition'][idx[0]]} / 강좌 계열: {DF['kind'][idx[0]]} / URL 강좌 링크: {DF['url'][idx[0]]}"]
         else:
            rs[result] = [f"수강 가능 여부: {DF['condition'][idx[0]]} / 강좌 계열: {DF['kind'][idx[0]]} / URL 강좌 링크: {DF['url'][idx[0]]}"]
            rs[result].append(f"수강 가능 여부: {DF['condition'][idx[1]]} / 강좌 계열: {DF['kind'][idx[1]]} / URL 강좌 링크: {DF['url'][idx[1]]}")

      return rs