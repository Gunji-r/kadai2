import MeCab


def print_words_and_results(raw_text: str = 'すもももももももものうち'):
    m = MeCab.Tagger("-Ochasen")
    print(m.parse(raw_text))
#Mecabのインポートエラーが調べても原因がわからず修正できなかったため、検証できていません


def print_morpheme(raw_text: str = 'すもももももももものうち'):
    m = Mecab.Tagger.parseToNode(raw_text)
    while m:
        word = m.surface
        pos = m.feature.split(",")[1]
        print('{0},{1}'.format(word,pos))
        m=m.next
        #こちらも、Mecabのインポートエラーが調べても解決できなかったため検証できていません


if __name__ == '__main__':
    m = MeCab.Tagger("-Ochasen")
    print(m.parse("すもももももももものうち"))
