# py-wsi-digital-pathology

## Project Overview

Segmentation: Identify and delineate different regions or structures within the image (e.g., identifying tumor regions, separating different tissue types).  Feature Extraction: Extract quantitative features such as texture, shape, color, and intensity.  Feature Extraction: Extract quantitative features such as texture, shape, color, and intensity.  Classification: Use machine learning or deep learning techniques to classify regions based on their appearance (e.g., normal vs. pathological tissue).  Stain Normalization: Normalize the staining to reduce variability and improve the consistency of analyses.

The Jupyter notebook wsi_svs_thumbnails.ipynb displays thumbnails of whole slide .svs images (WSI) discussed within the Nature publication "Multi-omic machine learning predictor of breast cancer therapy response".

## Setup

Download the training and validation datasets from https://zenodo.org/records/6337925 and then install the following packages with the command: 

sudo apt-get install libopenslide0 openslide-tools

```bash
!pip install -r requirements.txt
```

## License

Dataset Information
This project utilizes a digital pathology (histology) dataset consisting of .svs files. The dataset is sourced from the research article "[Multi-omic machine learning predictor of breast cancer therapy response]" (DOI: 10.5281/zenodo.6337925).

The dataset is licensed under a Creative Commons Attribution 4.0 International license (CC BY 4.0).