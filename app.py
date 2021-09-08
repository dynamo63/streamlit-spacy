# TEST MODEL with streamlit
import spacy, streamlit as st
from spacy import displacy
import streamlit.components.v1 as components

print('---------- Load Model ---------')
nlp2 = spacy.load('./spacy_ner_custom')
print('-------- Load Completed -------')

st.title('Text classification Topic with Spacy 3.0')
st.write('Here we use the framework spacy 3.0, especially the NER (Named Recognition) functionnality for classify the text content of activity')

content = st.text_area('Input a sample activity description based on walk')

# define options
colors = {'BALADE': "#048b9a"}
options = {"ents": ["BALADE"], 'colors': colors}

st.header('Preview')
components.html(displacy.render(nlp2(content), style='ent', page=True, options=options))
