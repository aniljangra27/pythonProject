class TextAnalyzer(object):
    def __init__(self, text):
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')  # remove punctuation
        formattedText = formattedText.lower()  # make text lowercase
        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self, word):  # count the Frequency of a specific word
        dictMap = self.freqAll()
        if word in dictMap:
            return dictMap[word]
        else:
            return None


textAnalyze = TextAnalyzer("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
print(textAnalyze.freqAll())
print(textAnalyze.freqOf("diam"))