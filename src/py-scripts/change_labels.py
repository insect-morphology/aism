# /Users/taravser/opt/anaconda3/envs/PhenoScript/bin/python

from owlready2 import *

ontoFile="/Users/taravser/Documents/My_papers/AISM/GitHub/aism/src/ontology/aism-edit.owl"
saveFile="/Users/taravser/Documents/My_papers/AISM/GitHub/aism/src/ontology/aism-edit-2.owl"

onto = get_ontology(ontoFile).load(reload_if_newer=True, reload=True)
obo = onto.get_namespace("http://purl.obolibrary.org/obo/")

# 'OBO foundry unique label’
# - http://purl.obolibrary.org/obo/IAO_0000589
# obo.IAO_0000589.python_name

found_terms = onto.search(label='cuticle of*')
len(found_terms)

filename = '/Users/taravser/Documents/My_papers/AISM/GitHub/aism/src/py-scripts/found_terms.txt'
i=1
with open(filename, 'w') as f:
    for term in found_terms:
        old_label = term.label.first()
        print(i, old_label,  file=f)
        i=i+1
    f.close()


i=1
for term in found_terms:
    old_label = term.label.first()
    # new_label = old_label.replace('cuticle of ', '')
    print(i, old_label)
    i=i+1
    # term.label = new_label
    obo.IAO_0000589[term] = '--' + old_label

onto.save(file = saveFile, format = "rdfxml")

# Replace manually
# '"en">cuticle ' of TO '"en">'
# '--cuticle of' TO 'cuticle of'