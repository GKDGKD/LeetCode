import math

def tfidf(article):
    # 计算tfidf
    D = len(article)  # 文章数
    W = len(article[0]) # 每篇文章单词数
    
    words = {} # 第i个单词在所有文章中出现的次数
    for i in range(D):
        a = article[i]
        for word in a:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    tf = {}
    for word in words:
        tf[word] = words[word] / (W * D)

    # 包含第i个单词的文章数量
    f = {i: 0 for i in words}
    for word in words:
        for a in article:
            if word in a:
                f[word] += 1

    idf = {}
    for word in words:
        idf[word] = math.log(D / (f[word] + 1))

    tfidf = {}
    for word in words:
        tfidf[word] = tf[word] * idf[word]

    return tfidf
        
T = int(input())
for _ in range(T):
    # D：文章总数；W：每篇文章的单词数；t：阈值
    D, W, t = map(float, input().split())
    article = []
    for _ in range(int(D)):
        article.append(input().split())
    
    # print(f'{D} {W} {t}, {article}')
    res = tfidf(article)
    if max(res.values()) > t:
        print(1)
    else:
        print(0)
    # print(tfidf)
    

"""
in:
2
3 3 0.3
df df rtfds
fsaf fg df
oo df df
3 3 0.6
fsdfa fasdfsfsdfsf tetaszgag
sssssssssssssss fdsfsaf gsagfsafasdfgasge
hahahahah ewrsafadfad sssssssssssssss

out:
0
0

[['df', 'df', 'rtfds'], ['fsaf', 'fg', 'df'], ['oo', 'df', 'df']]
{'df': -0.15982337358432272, 'rtfds': 0.04505167867868493, 'fsaf': 0.04505167867868493, 'fg': 0.04505167867868493, 'oo': 0.04505167867868493}
"""