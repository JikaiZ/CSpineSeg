# CSpineSeg

This repository contains sample code and scripts for the **Duke University Cervical Spine MRI Segmentation Dataset (CSpineSeg)**. The dataset and methods are described in the accompanying data descriptor (see below).

## Paper

The data descriptor of the CSpineSeg was published on Nature Scientifc Data:

**[The Duke University Cervical Spine MRI Segmentation Dataset (CSpineSeg)](https://www.nature.com/articles/s41597-025-05975-w)**  
Longfei Zhou, Walter Wiggins, Jikai Zhang, Roy Colglazier, Jay Willhite, Austin Dixon, Michael Malinzak, Hanxue Gu, Maciej A. Mazurowski & Evan Calabrese  
*Scientific Data* **12**, Article number: 1695 (2025)

The paper describes a publicly available dataset of 1,255 cervical spine T2-weighted MRI examinations from 1,232 patients, with expert manual segmentations of vertebral bodies and intervertebral discs for 481 patients. It also presents an nnU-Net–based segmentation model (Dice > 90%) and outlines data collection, annotation, and evaluation procedures. Segmentation models can be acquired via reasonable requests.

## Reference

If you use CSpineSeg or this code in your work, please cite:

```bibtex
@article{zhou2025cspineseg,
  title={The Duke University Cervical Spine MRI Segmentation Dataset (CSpineSeg)},
  author={Zhou, Longfei and Wiggins, Walter and Zhang, Jikai and Colglazier, Roy and Willhite, Jay and Dixon, Austin and Malinzak, Michael and Gu, Hanxue and Mazurowski, Maciej A. and Calabrese, Evan},
  journal={Scientific Data},
  volume={12},
  pages={1695},
  year={2025},
  publisher={Nature Publishing Group},
  doi={10.1038/s41597-025-05975-w},
  url={https://www.nature.com/articles/s41597-025-05975-w}
}
```

## Example

The repository includes an example from the CSpineSeg dataset in the `assets` folder:

![CSpineSeg example](assets/cspineseg_example.png)

*This figure illustrates a CSpineSeg example of sagittal T2 MRI for the c-spine with expert annotations of vertebral bodies (red) and IVDs (green). A zoomed-in view was provided.*

## Dataset Acquisition

The CSpineSeg dataset is hosted on the **Medical Imaging and Data Resource Center (MIDRC)**. To download the data:

1. **Create an account**  
   You must register and log in at [MIDRC](https://data.midrc.org) before you can access the data.

2. **Download the dataset**  
   Once logged in, go to:  
   **https://data.midrc.org/discovery/H6K0-A61V**

   The download includes:
   - *Structured Data TSVs* — metadata (demographics, imaging parameters)
   - *MRI Image Files* — de-identified DICOMs
   - *Annotation Files* — MRI in NIfTI format (from DICOM conversion)
   - *Segmentation Files* — manual segmentations in NIfTI format

Please comply with the [MIDRC Data Use Agreement](https://www.midrc.org/midrc-data-use-agreement) when using the data.

## Usage

### Environment setup

Install dependencies (e.g. in a virtual environment):

```bash
pip install -r requirements.txt
```
- **dcm2niix** is required for `dicom_nifti_dcm2niix.py` and must be installed separately (e.g. from [dcm2niix](https://github.com/rordenlab/dcm2niix)).
- For **nnU-Net** workflows, configure the nnU-Net environment variables (`nnUNet_raw`, `nnUNet_preprocessed`, `nnUNet_results`) and use the commands in `nnUnet_env_set.sh` as a reference.

Before running notebooks or scripts, replace each placeholder path (e.g. `<PATH_TO_PRED_ENSEMBLE_FOLDER>`, `<PATH_TO_STRUCTURED_DATA>`, `<PATH_TO_TEST_CSV>`) with your actual local path. Each placeholder is a single value; no path segments are implied.

### Notebooks and Scripts

| File | Description |
|------|-------------|
| **analyze_tabular_data.ipynb** | Explores the structured metadata (TSVs) from MIDRC: directory tree of the data folder, loading of case and MR series tables, and basic demographics and imaging-parameter summaries. |
| **DSC_analysis.ipynb** | Evaluates Dice similarity coefficient (DSC) for segmentation: cross-validation (2D, 3D, ensemble nnU-Net) and test-set evaluation, with statistical comparisons (e.g., Mann–Whitney U) and bootstrap confidence intervals. |
| **connected_component.ipynb** | Per-disc analysis using connected components on the mid-sagittal slice: labels intervertebral discs (e.g. C2/C3–C7/T1), computes per-level Dice, and visualizes true vs. predicted segmentations. |
| **dicom_nifti_dcm2niix.py** | Converts DICOM series to a single NIfTI file per series using **dcm2niix**. 
| **nnUNet_Setup.py** | Prepares NIfTI data for the nnU-Net pipeline: expects paths to TRAIN/VAL/TEST metadata CSVs, the NIfTI data directory, and the nnU-Net destination root. Copies and renames volumes into `imagesTr`, `labelsTr`, `imagesTs`, `labelsTs` and generates the dataset JSON for nnU-Net (e.g. Dataset108_CSpineSeg). |
| **nnUnet_env_set.sh** | Example bash commands for nnU-Net v2: setting `nnUNet_raw`, `nnUNet_preprocessed`, `nnUNet_results`, preprocessing (e.g. `nnUNetv2_plan_and_preprocess`), training 2D and 3D full-resolution models, prediction, ensemble, and model export. Uncomment and adjust paths as needed. |