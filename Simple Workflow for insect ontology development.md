[![Build Status](https://travis-ci.org/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system.svg?branch=master)](https://travis-ci.org/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system)
[![DOI](https://zenodo.org/badge/13996/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system.svg)](https://zenodo.org/badge/latestdoi/13996/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system)

# Simple workflow for insect ontology development

Multispecies insect anatomy ontologies are used as bases for robust knowledge bases for specific anatomical terms ([Yoder et al. 2010](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015991), [HAO Portal](http://portal.hymao.org/projects/32/public/ontology/)), improve the accessibility of morphology descriptions ([Balhoff et al. 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094056)), and are useful for improving the modeling of discrete morphological characters in phylogenetic context ([Tarasov 2020](https://doi.org/10.1093/sysbio/syz050 )).

There are two major reasons why insects are poorly represented amongst multispecies anatomy ontologies: lack of a base insect anatomy ontology and the lack of infrastructure to build such resource.

In this document, we outline a simple workflow for creating/editing insect ontologies using  [Protégé](https://protege.stanford.edu/) and the [ontology development kit](https://github.com/INCATools/ontology-development-kit).

The first thing you need to do is to install the Ontology Development Kit. Instructions for this are in the README file on https://github.com/INCATools/ontology-development-kit.

Follow the steps carefully. This will create a file system on your computer with all the necessary files to create and run your ontology, ready to be uploaded to GitHub, in a mostly automated way. This process might require some preparation and troubleshooting, especially if you are installing the ODK on a Windows machine, and if you are not experienced or set up for working on GitHub from your computer.
Once your files are created in your computer, it is important that you read the instructions on the README-editors.md file within your src/ontology/ folder.
You want to upload this initial version of your files into a GitHub repository and make a clone of it. You will be editing the cloned repository, specifically, the AISM-ODK/src/ontology/AISM-edit.owl file. Any edits should only be made to files within this particular folder.
You will be editing this owl file in your computer using Protégé, for which you need some initial settings:

Setup Protégé to auto generate IRI-s:

File > Preferences > New entities

Specified IRI: http://purl.obolibrary.org/obo/

Set language to ‘en’, digit count to 7

https://github.com/insect-morphology/aism-ODK/blob/master/screenshots/Screen%20Shot%202020-11-11%20at%207.07.48%20AM.png

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/obophenotype/anatomy_ontology_of_insect_skeletomuscular_system/issues) to request new terms/classes or report errors or specific concerns related to the ontology.

## Acknowledgements

This ontology repository was created using the [ontology starter kit](https://github.com/INCATools/ontology-starter-kit)
