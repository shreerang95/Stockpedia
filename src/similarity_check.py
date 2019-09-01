import gensim
from nltk.tokenize import word_tokenize
# import nltk
# nltk.download()


def generate_similar_words(raw_documents, words_compare):
    gen_docs = [[w.lower() for w in word_tokenize(text)]
                for text in raw_documents]

    dictionary = gensim.corpora.Dictionary(gen_docs)

    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

    tf_idf = gensim.models.TfidfModel(corpus)

    s = 0
    for i in corpus:
        s += len(i)

    sims = gensim.similarities.Similarity('',tf_idf[corpus],num_features=len(dictionary))
    indices = []
    for words in words_compare:
        sums=0
        query_doc = [w.lower() for w in word_tokenize(words)]

        query_doc_bow = dictionary.doc2bow(query_doc)

        query_doc_tf_idf = tf_idf[query_doc_bow]
        # print(query_doc_tf_idf)

        for indexes in query_doc_tf_idf:
            sums = sums + indexes[1]
        if(sums>0 and sums/len(query_doc_tf_idf)>0.1):
            indices.append(words)
    return indices