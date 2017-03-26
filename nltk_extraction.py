import nltk

with open('text.txt', 'r') as f:
    sample = f.read()

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# if set to True, named entity is only tagged as NE, otherwise the classifier add labels onto every NE
# All Tags are in https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label():
        if t.label()=='NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names


entity_names = []
for tree in chunked_sentences:
    entity_names.extend(extract_entity_names(tree))

print(sample)
print(set(entity_names))