[![Build Status](https://travis-ci.org/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system.svg?branch=master)](https://travis-ci.org/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system)
[![DOI](https://zenodo.org/badge/13996/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system.svg)](https://zenodo.org/badge/latestdoi/13996/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system)

# Simple workflow for insect ontology development

Multispecies insect anatomy ontologies are used as bases for robust knowledge bases for specific anatomical terms ([Yoder et al. 2010](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015991), [HAO Portal](http://portal.hymao.org/projects/32/public/ontology/)), improve the accessibility of morphology descriptions ([Balhoff et al. 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094056)), and are useful for improving the modeling of discrete morphological characters in phylogenetic context ([Tarasov 2020](https://doi.org/10.1093/sysbio/syz050 )).

There are two major reasons why insects are poorly represented amongst multispecies anatomy ontologies: lack of a base insect anatomy ontology and the lack of infrastructure to build such resource.

In this document, we outline a simple workflow for creating/editing insect ontologies using  [Protégé](https://protege.stanford.edu/) and the [ontology development kit](https://github.com/INCATools/ontology-development-kit).

The first thing you need to do is to install the Ontology Development Kit. Instructions for this are in the README file at https://github.com/INCATools/ontology-development-kit.

Follow the steps carefully. This will create a file system in your computer with all the necessary files to create and run your ontology, ready to be uploaded to GitHub, in a mostly automated way. This process might require some preparation and troubleshooting, especially if you are installing the ODK on a Windows machine, and if you are not experienced with or set up for working on GitHub from your computer.
Once your files are created in your computer, it is important that you read the instructions on the README-editors.md file within your src/ontology/ folder.
You want to upload this initial version of your files into a GitHub repository and make a clone of it. You will be editing the cloned repository, specifically, the AISM-ODK/src/ontology/AISM-edit.owl file. Any edits should only be made to files within this particular folder.
You will be editing this owl file in your computer using Protégé, for which you need some initial settings:

Setup Protégé to auto generate IRI-s:

`File > Preferences > New entities`

Specified IRI: `http://purl.obolibrary.org/obo/`

Set language to ‘en’, digit count to 7

 <p align="left">
  <img src="https://github.com/insect-morphology/aism-ODK/blob/master/screenshots/Screen%20Shot%202020-11-11%20at%207.07.48%20AM.png" width="500" title="hover text">
</p>  

Start number should be the first number of the range that you have been assigned. If you don't have a range of designated numbers, contact the project manager.

Importing terms from existing ontologies:

Setup a new import

1. add imports to src/ontology/aism-odk.yaml

`import_group:
  products:
    - id: ro
    - id: uberon
    - id: pato
    - id: bspo`

2. in terminal `sh run.sh make update_repo` (in src/ontology)

`$ sh run.sh make update_repo`

3. open aism-edit.owl in text editor to add import statement:

`Prefix(:=<http://purl.obolibrary.org/obo/aism.owl#>)`

`Prefix(dce:=<http://purl.org/dc/elements/1.1/>)`

`Prefix(owl:=<http://www.w3.org/2002/07/owl#>)`

`Prefix(rdf:=<http://www.w3.org/1999/02/22-rdf-syntax-ns#>)`

`Prefix(xml:=<http://www.w3.org/XML/1998/namespace>)`

`Prefix(xsd:=<http://www.w3.org/2001/XMLSchema#>)`

`Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)`

`Prefix(dcterms:=<http://purl.org/dc/terms/>)`


`Ontology(<http://purl.obolibrary.org/obo/aism.owl>`
`Import(<http://purl.obolibrary.org/obo/aism/imports/bspo_import.owl>)`
`Import(<http://purl.obolibrary.org/obo/aism/imports/pato_import.owl>)`
`Import(<http://purl.obolibrary.org/obo/aism/imports/ro_import.owl>)`
`Import(<http://purl.obolibrary.org/obo/aism/imports/uberon_import.owl>)`
`Annotation(dce:description "Ontology about the skeletomuscular system of insects")`
`Annotation(dce:title "Anatomy Ontology of Insect Skeletomuscular System")`
`Annotation(dcterms:license <CC-BY>)`

4. open catalog-v001.xml in text editor and add import statement

`<?xml version="1.0" encoding="UTF-8" standalone="no"?>`
`<catalog prefer="public" xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">`


  `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/uberon_import.owl" uri="imports/uberon_import.owl"/>`
  `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/uberon_import.obo" uri="imports/uberon_import.obo"/>`
  `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/bspo_import.owl" uri="imports/bspo_import.owl"/>`
 `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/bspo_import.obo" uri="imports/bspo_import.obo"/>`
  `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/pato_import.owl" uri="imports/pato_import.owl"/>`
  `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/pato_import.obo" uri="imports/pato_import.obo"/>`
  `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/ro_import.owl" uri="imports/ro_import.owl"/>`
  `<uri id="User Entered Import Resolution" name="http://purl.obolibrary.org/obo/aism/imports/ro_import.obo" uri="imports/ro_import.obo"/>`


</catalog>


5. In the terminal `sh run.sh make imports/obi_import.owl`

`$ ./run.sh make all_imports`

6. open `maxo-edit.owl` in Protégé and run reasoner to look for unsatisfiable classes.


Once imports are set up

7. Find your term online and copy its IRI

In Protégé: add subclass

 <p align="left">
  <img src="https://github.com/insect-morphology/aism-ODK/blob/master/screenshots/Screen%20Shot%202020-11-11%20at%2010.44.20%20AM.png" width="500" title="hover text">
</p>  

Which opens a new window:

<p align="left">
  <img src="https://github.com/insect-morphology/aism-ODK/blob/master/screenshots/Screen%20Shot%202020-11-11%20at%2010.44.27%20AM.png" width="500" title="hover text">
</p>  

8. Paste your link to the Name field and click OK

<p align="left">
  <img src="https://github.com/insect-morphology/aism-ODK/blob/master/screenshots/Screen%20Shot%202020-11-11%20at%2010.44.34%20AM.png" width="500" title="hover text">
 </p>  
 
The term will now be listed under Thing. You don’t need to worry about annotations or placement of items newly added to your ontology, as the next step will take care of this for you. Keep adding a few more terms in this fashion. 

9. Save the `AISM.owl` file and run the following script in the terminal in the src/ontology folder:


`./run.sh make all_imports`


or

`sh run.sh make imports/cl_import.owl`

to import full specific ontologies. 

The latter is recommended if numerous ontologies, including bigger ones (like PR, protein ontology) are used, as the system will not import all but the selected ontology (in that case CL, the cell ontology).

If you try to import from a larger ontology (like PR, protein ontology) the process might take an extreme long time and might eventually be terminated (like when I tried to import resilin from PR). In this case, it is perhaps best to simply start with step 7 (importing only the specific term you need without importing the full ontology), so the term will have an IRI, but will just hang on Thing.



## Annotations

Each term should contain a series of annotations which will be the way to link the term to references, authors, and other sorts of information. These annotations are added using Protégé during the ontology editing process.

Each term should at least have an ‘rdfs: label’ and a ‘definition’. Ideally, each term should include a reference for the definition that is being used. AISM incorporates plenty of **Annotation properties** for these purposes.

To add annotations to an existing term click on the ‘@’ symbol on the right side of the annotations tab.


This will open a new window to choose what kind of annotation will be added. Click on the plus sign, which opens the ‘Create annotation’ window.

Choose ‘definition’ to add a natural language verbatim definition for the term. Type the definition in the white box on the right side panel, choose the appropriate language for it, and click OK.


Additional resources can be found at: [https://go-protege-tutorial.readthedocs.io/en/latest/](https://go-protege-tutorial.readthedocs.io/en/latest/)

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system/issues) to request new terms/classes or report errors or specific concerns related to the ontology.

## Acknowledgements

This ontology repository was created using the [ontology starter kit](https://github.com/INCATools/ontology-starter-kit)
