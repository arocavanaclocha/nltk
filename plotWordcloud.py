from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plotWordcloud(remarks):
  complete_review_text= ""
  complete_review_text = remarks
  stop = "NaN"

  wordcloud = WordCloud(stopwords=stop, background_color="white").generate(complete_review_text)

  plt.imshow( wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.figure(figsize = (30,30))    
  plt.show()

def plotFreqDist(remarks):              
  stop = set(stopwords.words('english'))
  tokens = [t for t in remarks.split()]
  clean_tokens = tokens[:]
  sr = stopwords.words('english')

  for token in tokens:
      if token in stopwords.words('english'):
          clean_tokens.remove(token)

  freq = nltk.FreqDist(clean_tokens)
  freq.plot(20, cumulative=False)
  

def addStopwords( lang, stopwords):
  sess.Stopwords[0][lang]  += stopwords
