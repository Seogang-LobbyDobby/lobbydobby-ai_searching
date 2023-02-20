from lecture.LectureSearching import Model
from spell.SYM.Symspell import Spell
from functools import cache


@cache
class LectureRs():
   def __init__(self):
      self.base = Model()
      self.ssp = Spell()

   def lectureSc(self, query):
      input_query = self.ssp.spell(query)
      results = self.base.search(input_query)

      DF = self.base.df
      rs = {}
      for result in results:
         idx = DF[DF['title']==result].index
         if result[-3:] != '예체능':
            result = result[:-4]
         else:
            result = result[:-5]

         if len(idx) == 1:
            rs[result] = {
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": f"{DF['img_url'][idx[0]]}"
            }
         else:
            rs[result] = {
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": f"{DF['img_url'][idx[0]]}"
            }
            rs[result+'__'] = {
               "수강 가능 여부": f"{DF['condition'][idx[1]]}",
               "URL 강좌 링크": f"{DF['url'][idx[1]]}",
               "이미지 url": f"{DF['img_url'][idx[1]]}"
            }

      RESULT = {'searchResult':[]}
      RESULT['searchResult'] = rs
      RESULT['editWord'] = input_query
      return RESULT

   def LRS(self, name, aff):
      results = self.base.lecturers(name, aff)

      DF = self.base.df
      rs = {}
      for result in results:
         idx = DF[DF['title']==result].index
         if result[-3:] != '예체능':
            result = result[:-4]
         else:
            result = result[:-5]

         if len(idx) == 1:
            rs[result] = {
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": f"{DF['img_url'][idx[0]]}"
            }
         else:
            rs[result] = {
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": f"{DF['img_url'][idx[0]]}"
            }
            rs[result+'__'] = {
               "수강 가능 여부": f"{DF['condition'][idx[1]]}",
               "URL 강좌 링크": f"{DF['url'][idx[1]]}",
               "이미지 url": f"{DF['img_url'][idx[1]]}"
            }

      RESULT = {'searchResult':[]}
      RESULT['searchResult'] = rs
      return RESULT