import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk

def plotWordcloud(tokens):

  wordcloud = WordCloud(background_color="white").generate(str(tokens))

  plt.imshow( wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.figure(figsize = (30,30))    
  plt.show()

def plotFreqDist(tokens):    
  freq = nltk.FreqDist(tokens)
  freq.plot(20, cumulative=False)  
