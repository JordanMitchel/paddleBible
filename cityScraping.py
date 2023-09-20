import spacy
from spacy.tokens import Span
nlp = spacy.load('en_core_web_sm')
# Text with nlp
doc = nlp("I will give to you and to your descendants after you, the land of your sojournings, all the land of Canaan, for an everlasting possession; and I will be their God.")
gpe = [] # countries, cities, states
loc = [] # non gpe locations, mountain ranges, bodies of water
for ent in doc.ents:
    if (ent.label_ == 'GPE'):
        gpe.append(ent.text)
    elif (ent.label_ == 'LOC'):
        loc.append(ent.text)

nlp2 = spacy.load('xx_ent_wiki_sm')
doc2 = nlp2("And He said to him, “I am the Lord who brought you out of Ur of the Chaldeans, to give you this land to possess it.")
gpe2 = [] # countries, cities, states
loc2 = [] # non gpe locations, mountain ranges, bodies of water
for ent2 in doc2.ents:
    if (ent2.label_ == 'GPE'):
        gpe2.append(ent2.text)
    elif (ent2.label_ == 'LOC'):
        loc2.append(ent2.text)
x=4