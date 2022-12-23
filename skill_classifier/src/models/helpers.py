import spacy

def load_model(name): 
    nlp = spacy.load(name)
    de_stop_words = nlp.Defaults.stop_words
    return nlp, de_stop_words

def len_doc(doc): 
    doc_length = len(doc)
    return doc_length

def len_doc_only_alpha(doc): 
    doc_length = sum([1 if token.is_alpha else 0 for token in doc])
    return doc_length

    