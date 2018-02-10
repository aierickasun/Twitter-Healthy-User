import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        pos_fin = open(positives, "r");
        neg_fin = open(negatives, "r");
        pos_list = pos_fin.readlines();#could also use readline()
                #But readlines returns a list of everyline separated properly.
        neg_list = neg_fin.readlines();
        self.negatives = []
        self.positives = []
        #get rid of newline, lines starting with ;, and turn all to lower
        #case.
        for i in pos_list:
            if not(i[0]==';' or i[0]=='\n'):#could use startswith
                filtered = i.lower()[:-1]
                self.positives.append(filtered)
        for i in neg_list:
            if not(i[0]==';' or i[0]=='\n'):
                filtered = i.lower()[:-1]
                self.negatives.append(filtered)

        pos_fin.close()
        neg_fin.close()
        return None;

    """Analyzes the emotions of a word.
    @returns An integer: -1 if word has a bad meaning.
                          1 if word has good meaning.
                          0 if word's meaning can't be inferred.
    """
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        moral = 0
        text_list = nltk.tokenize.TweetTokenizer().tokenize(text);
        for i in text_list:
            if (i.lower() in self.positives):
                moral+=1
            elif (i.lower() in self.negatives):
                moral-=1
        return moral
