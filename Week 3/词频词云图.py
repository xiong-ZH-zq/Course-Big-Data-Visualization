import pandas as pd  
from wordcloud import WordCloud  
import matplotlib.pyplot as plt  
import numpy as np
from PIL import Image

# 读取词频文件  
df = pd.read_csv('Week 3\sitetotal_分词后_词频.tsv',delimiter='\t')  

text = ' '.join(df['word'])

mask = np.array(Image.open("Week 3/mask.png"))

# 创建词云对象  
wordcloud = WordCloud(
    width=500, 
    mask=mask,
    height=500, 
    background_color='white', 
    min_font_size=10,
    font_path=r"Week 3\SarasaFixedSC-Regular.ttf").generate(text)  
  
# 显示词云图  
plt.figure(figsize=(10, 5))  
plt.imshow(wordcloud, interpolation='bilinear')  
plt.axis('off')
plt.savefig("Week 3/Wordcloud.png",dpi=960)  
# plt.show()