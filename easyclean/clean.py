import re
import nltk
from cleantext import clean
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#from flashtext import KeywordProcessor



def test(n):
    msg = 'your test is '+n
    return msg

#first filter
def rex(txt):
    txt = ' '.join(re.sub('(@[A-Za-z0-9]+)', ' ', txt).split())
    txt = ' '.join(re.sub('[\.\,\«\»\!\¡\[\]\_\{\}\`\~\?\<\>\/\¿\:\;\@\&\$\%\#\+\^\-\=\)\(\*]', ' ',txt).split())
    #txt = ' '.join(re.sub('[\:D\:)\:(\:-)\;-)\:<})\:-||\:-(\:-))\:-*\:-P~\:-O\:-o\:-0\:-|\:-\:-/\=:O\=:o\=:0]', ' ',txt).split())
    #txt = ' '.join(re.sub('[\:D]', ' ',txt).split())
    #txt = ' '.join(re.sub('(\s?[A-Z])', ' ', txt).split())
    #txt = ' '.join(re.sub('([a-z]\s)', ' ', txt).split())
    txt = ' '.join(re.sub('(\s[A-Z]\s)', ' ', txt).split())#
    txt = ' '.join(re.sub('(\s[a-z]\s)', ' ', txt).split())
    txt = ' '.join(re.sub('(\s[a-zA-Z0-9]\s)', ' ', txt).split())
    txt = ' '.join(re.sub('(\s[A-Z]\s)', ' ', txt).split())
    #txt = ' '.join(re.sub('(\s[a-z]\s)', ' ', txt).split())
    txt.strip()
    txt = clean(txt, no_emoji=True) #check additional parameters 
    return txt
#emoticons son quitados por la linea 2 de simbolos

def cstopwords(txt):
    nltk.download('stopwords')
    tokens = word_tokenize(txt.lower())
    english_stopwords = stopwords.words('english')
    tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]
    txt = ' '.join(tokens_wo_stopwords)
    return txt

#https://gist.github.com/sebleier/554280

def gethashtags(txt, hash=False):
    txt = txt.split()
    listHashtag = []
    for i in txt:
        if (i.startswith('#')):
            if hash:
                word = i.replace("#", '') 
                listHashtag.append(word)
            else:
                listHashtag.append(i)
    return listHashtag        
        

#number for text
def getnumbers(txt):
    reg =  r'\d+\.\d+|\d+'
    txt =  re.findall(reg, txt)
    return txt 

#get urls
def geturls(txt):
    reg = r'https?://\S+'
    txt = re.findall(reg, txt) 
    return txt

#get emails
def getemails(txt):
   reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
   txt = re.findall(reg, txt)
   return txt

#get users 
def getusers(txt):
    reg = r'@([A-Za-z0-9_]+)' 
    txt = re.findall(reg, txt)
    return txt

#repeated letters hello vs heloooo
def reducetext(txt):
    s = set()
    mlist = []
    for ch in txt:
        if ch not in s:
            s.add(ch)
            mlist.append(ch)
    
    txt = ' '.join(mlist) 
    return txt

#tokenizaacion
def toneniza(txt):
    return txt









