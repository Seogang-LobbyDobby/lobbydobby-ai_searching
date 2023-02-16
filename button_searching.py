from ButtonSearching import Model
from Symspell import Spell
from functools import cache


class Button():
   @cache
   def button(self, query):
      ssp = Spell()
      input_query = ssp.spell(query)
      base = Model()
      results = base.search(input_query)

      now = []
      DF = base.df
      for result in results:
         if result[-5:] == '월드 이동':
            result = result[:-7]
         elif result[-2:] == '기능':
            result = result[:-4]
         now.append(result)

      result = {'searchResult':now, 'editWord':input_query}
      return result