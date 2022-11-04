#Navy Nabian ©2020
#To use this script, copy and paste from discord into the input file
#and then click run. Then copy directly from the output file into
#Obsidian Portal for a beautiful, ready to post log.


'''To put an image in, just write img on its own line in your post.'''

'''Set this to True if you want img to be converted to a new bbcode'''
CollectBBCODE=True
'''after you run the script, upload the pictures you want in the
log to the site in the order they appear, then they should be solid.'''




import re
with open('input', 'r+') as f:
  strin=f.read()


def bbnew():
  return add_image_embed_bbcode_unique(None)

def image_ready():
  re.sub(r"img",'<img>',strin)
  with open('input','w+') as f2:
    f2.write(strin)


def add_image_embed_bbcode_unique(inp):
  count=0
  ret=""
  with open('counter', 'r+') as f3:
    count = int(f3.read())
    ret="[[File:{0}  | class=media-item-align-center |navywashere]]".format(count+1)
  with open('counter','w') as f3:
    f3.write(str(count+1))
  return ret

names = {'Navy':'Emil','Calder':'GM','Izzy':'Emmett','Pete':'Caroline','Emily':'Celia','Sam':'Jean'}

if re.search(r'Jon ',strin):
  names['Pete']='Jon'

if re.search(r'Lamarck',strin):
  names['Navy']='Support'

if re.search(r'Sterling',strin):
  names['Izzy']= 'Sterling'
  
if re.search(r'Randy',strin):
  names['Izzy']='Support'

if re.search(r'Gen |Genevieve',strin):
  names['Emily']='Support'

if re.search(r'Nylea',strin):
  names['Emily']= 'Nylea'

if strin.count(r'Ayame') > strin.count(r'Celia'):
  names['Emily']= 'Ayame'

charnames = {'Cecilia':'Cécilia','Abelia':'Abélia','Melissaire':'Mélissaire','Barthelemy': 'Barthélemy',
'Cafe Soule': 'Cafe Soulé',
'Eleonore': 'Éléonore',
'Giselle': 'Gisèlle',
'Kamil': 'Kâmil',
'Philemon': 'Philémon',
'Poincare': 'Poincaré',
'Rene': 'René',
'Seyres': 'Seyrès',
'Vieux Carre': 'Vieux Carré'}


strin= re.sub(r"\d{2}\/\d{2}\/\d{4}\n",'⌀PM\n',strin)
strin= re.sub(r"(A|P)M\n([^<>0123456789*])((?!((A|P)M\n)).|\n)*?(?=(A|P)M\n<rep>)",'',strin)
strin= re.sub(r"<rep>",'',strin)
if CollectBBCODE:
  strin= re.sub(r'img',add_image_embed_bbcode_unique,strin)
strin= re.sub(r"(Navy|Calder|Izzy|Pete|Emily|Sam).*?(A|P)M\n<add>",'',strin)

for key,val in charnames.items():
  strin=re.sub(key,val,strin)

def rep_with_dict(dictio,strin):
  for key,val in dictio.items():
    strin=re.sub(key+r"(?= —)","*"+key+":*",strin)
  return strin




strin=rep_with_dict(names,strin)

for key,val in names.items():
  strin=re.sub(r"(?<=\*)"+ key + r"(?=:\*)",val,strin)


strin= re.sub(r"(?<=:\*).*(\s|⌀)(P|A)M\n",' ',strin)
strin= re.sub(r"\n","\n\n",strin)
strin= re.sub(r"\(edited\)","",strin)
strin= re.sub(r"(?<=.)\n\*(?=\w*:\*)",'\n\n*',strin)
strin= re.sub(r"\n{3,}","\n\n",strin)
strin= re.sub(r"\n*\* ?\* ?\* ?\n*",'''\n</p>

__________________

<p style="font-size:0.8em;">\n\n''',strin)
strin= re.sub(r"\~",r"_",strin)


with open('output','w+') as f2:
  f2.write(strin)
