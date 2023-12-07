# Instalar:
#   pip install -U spacy
#   python -m spacy download pt_core_news_lg  # en_core_web_sm

import spacy

# Load English tokenizer, tagger, parser and NER

nlp = spacy.load("pt_core_news_lg")

# Process whole documents
text = """Quando o João Duarte chegou a Braga, alugou um enorme carro azul e
foi para a quinta do pai, em Terras de Bouro, tratar dos animais e 
dos apetrechos agrícolas."""
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
for token in doc:
    print(f'{token.text} {token.lemma_} {token.pos_}')

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
