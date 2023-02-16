from LectureSearching import Model
from Hanspell import Spell


class LectureRs():
   def lectureSc(self, query):
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
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": "http://www.kmooc.kr/asset-v1:EwhaK+EW22003M+2023_S15+type@asset+block@융합교육.png"
            }
         else:
            rs[result] = {
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": "http://www.kmooc.kr/asset-v1:EwhaK+EW22003M+2023_S15+type@asset+block@융합교육.png"
            }
            rs[result+'__'] = {
               "수강 가능 여부": f"{DF['condition'][idx[1]]}",
               "URL 강좌 링크": f"{DF['url'][idx[1]]}",
               "이미지 url": "http://www.kmooc.kr/asset-v1:EwhaK+EW22003M+2023_S15+type@asset+block@융합교육.png"
            }

      RESULT = {'searchResult':[]}
      RESULT['searchResult'] = rs
      RESULT['editWord'] = input_query
      return RESULT

   def LRS(self, name, aff):
      base = Model()
      results = base.lecturers(name, aff)

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
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": "http://www.kmooc.kr/asset-v1:EwhaK+EW22003M+2023_S15+type@asset+block@융합교육.png"
            }
         else:
            rs[result] = {
               "수강 가능 여부": f"{DF['condition'][idx[0]]}",
               "URL 강좌 링크": f"{DF['url'][idx[0]]}",
               "이미지 url": "http://www.kmooc.kr/asset-v1:EwhaK+EW22003M+2023_S15+type@asset+block@융합교육.png"
            }
            rs[result+'__'] = {
               "수강 가능 여부": f"{DF['condition'][idx[1]]}",
               "URL 강좌 링크": f"{DF['url'][idx[1]]}",
               "이미지 url": "http://www.kmooc.kr/asset-v1:EwhaK+EW22003M+2023_S15+type@asset+block@융합교육.png"
            }

      RESULT = {'searchResult':[]}
      RESULT['searchResult'] = rs
      return RESULT