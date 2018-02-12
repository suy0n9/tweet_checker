# coding: utf-8

import argparse
import csv
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from collections import Counter, defaultdict


def counter(texts):
    t = Tokenizer()
    words_count = defaultdict(int)
    words = []
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            pos = token.part_of_speech.split(',')[0]
            if pos == '名詞':
                words_count[token.base_form] += 1
                words.append(token.base_form)
    return words_count, words

def wordcloud(word, user_name):
    fpath = "/System/Library/Fonts/ヒラギノ明朝 ProN W3.ttc"
    p_name = "./wordcloud_{0}.png".format(user_name)
    wordcloud = WordCloud(background_color="white",
                          font_path=fpath,
                          width=800,
                          height=600).generate(word)

    wordcloud.to_file(p_name)

def execute(tweet):
    fname = tweet
    sp = tweet.split('_')
    spd = sp[1].split('.')
    user_name = spd[0]

    print(user_name)


    with open(fname, 'r') as f:
        reader = csv.reader(f)
        texts =[]
        for row in reader:
            text = row[0].split('http')
            print(text)
            texts.append(text[0])

    words_count, words = counter(texts)
    word = ' '.join(words)

    wordcloud(word, user_name)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('tweet',
            help='tweet file')

    args = parser.parse_args()

    execute(args.tweet)
