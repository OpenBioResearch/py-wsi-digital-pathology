# py-wsi-digital-pathology
Explore ML models for digital patholgy images using py_wsi

sudo apt-get install libopenslide0 openslide-tools

## Project Overview

This repo showcases Natural Language Processing (NLP) projects focused on  techniques to analyze clinical note dataset. BioBert, ClinicalBert and medacy are leveraged due to their biomedical domain specificity.

The notebooks are focused on gaining insights from clinician notes through entity recognition, sentiment analysis, relation extraction, and topic modeling and to a lesser extent of building a predictive model to detect sepsis

## Setup

Download the training and validation datasets and install the following packages with the command: 

```bash
!pip install -r requirements.txt
```

## License

Dataset Information
This project utilizes a digital pathology (histology) dataset consisting of .svs files. The dataset is sourced from the research article "[Multi-omic machine learning predictor of breast cancer therapy response]" (DOI: 10.5281/zenodo.6337925).

The dataset is licensed under a Creative Commons Attribution 4.0 International license (CC BY 4.0).
