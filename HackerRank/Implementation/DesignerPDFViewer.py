import sys
from string import ascii_lowercase


def designerPdfViewer(h, word):
    i = 0
    d = {}
    for c in ascii_lowercase:
        d[c] = h[i]
        i = i + 1

    wordh = d[word[0]]
    for c in word:
        if(d[c]>wordh):
            wordh = d[c]

    return str(wordh * word.__len__())

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)