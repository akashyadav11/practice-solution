import spacy 
def main(input):
    l=[]
    nlp-spacy.load("en_core_web_sm")
    doc-nlp(input)
    for token in doc: 
        if token.lemma_=="sleep":
            l.append(str(token))
    print (l)
    return l
