import time
from ButtonSearching import Model
# from Hanspell import Sspell
from Symspell import Spell


ssp = Spell()
# hsp = Sspell()
query = str(input())
t = time.time()
input_query = ssp.spell(query)
# for i in range(100):
#    print("------------------ {} ------------------".format(i+1))
#    query = str(input())
#    t = time.time()
#    input_query = ssp.spell(query)
#    print('SymSpell time :  {}'.format(time.time()-t))
#    print('SymSpell edit-word :  {}'.format(input_query))
#    t = time.time()
#    input_query = hsp.spell(query)
#    print('HanSpell time :  {}'.format(time.time()-t))
#    print('HanSpell edit-word :  {}\n'.format(input_query))
base = Model()
results = base.search(input_query)
print('Searching total-time: {}'.format(time.time() - t))

print('Searching results:')
DF = base.df
for result in results:
   if result[-5:] == '월드 이동':
      result = result[:-7]
   elif result[-2:] == '기능':
      result = result[:-4]
   print(result)