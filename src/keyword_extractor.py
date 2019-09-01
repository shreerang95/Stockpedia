from __future__ import absolute_import
from __future__ import print_function
import six

import rake
import operator
import io

def findKeywords(company_news):
    stoppath = "../Data/data/stoplists/SmartStoplist.txt"

    rake_obj = rake.Rake(stoppath, 5, 3, 4)

    sample_file = io.open("../Data/data/docs/fao_test/w2167e.txt", 'r',encoding="iso-8859-1")
    text = sample_file.read()
    
    keywords = rake_obj.run(text)

    rake_obj = rake.Rake(stoppath)
    
    text = company_news  

    sentences = rake.split_sentences(text)
    
    stop_words = rake.load_stop_words(stoppath)
    stop_pattern = rake.build_stop_word_regex(stoppath)
    phraseList = rake.generate_candidate_keywords(sentences, stop_pattern, stop_words)

    wscores = rake.calculate_word_scores(phraseList)

    keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wscores)
    keywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
    totalKeywords = len(keywords)
    

    keyword_list = rake_obj.run(text)[0:10]
    keyword_list1 = []
    for i in keyword_list:
        keyword_list1.append(i[0])

    return keyword_list1
