#!/bin/bash
## Customized nnUNet working directory
# export nnUNet_raw="../nnUNet_WORKDIR/nnUNet_raw"
# export nnUNet_preprocessed="../nnUNet_WORKDIR/nnUNet_preprocessed"
# export nnUNet_results="../nnUNet_WORKDIR/nnUNet_results"

## preprcess and verify
# nnUNetv2_plan_and_preprocess -d 108 --verify_dataset_integrity

## Training 2d and 3d full res model

# nnUNetv2_train 108 2d 0 --npz
# nnUNetv2_train 108 2d 1 --npz
# nnUNetv2_train 108 2d 2 --npz
# nnUNetv2_train 108 2d 3 --npz
# nnUNetv2_train 108 2d 4 --npz

# nnUNetv2_train 108 3d_fullres 0 --npz
# nnUNetv2_train 108 3d_fullres 1 --npz
# nnUNetv2_train 108 3d_fullres 2 --npz
# nnUNetv2_train 108 3d_fullres 3 --npz
# nnUNetv2_train 108 3d_fullres 4 --npz

## prediction based on 2d model
## assume images are saved in imagesTs folder and output is saved in predictTs_2d folder
## Trained model based on dataset id 108, unannotated data saved as dataset id 111
# nnUNetv2_predict -d Dataset108_CSpineSeg -i ../nnUNet_WORKDIR/nnUNet_raw/Dataset111_CSpineSeg_UNANNO/imagesTs -o ../nnUNet_WORKDIR/nnUNet_raw/Dataset111_CSpineSeg_UNANNO/predictTs_2d -f 0 1 2 3 4 -tr nnUNetTrainer -c 2d -p nnUNetPlans --save_probabilities --save_npz

# nnUNetv2_predict -d Dataset108_CSpineSeg -i ../nnUNet_WORKDIR/nnUNet_raw/Dataset111_CSpineSeg_UNANNO/imagesTs -o ../nnUNet_WORKDIR/nnUNet_raw/Dataset111_CSpineSeg_UNANNO/predictTs_3d -f 0 1 2 3 4 -tr nnUNetTrainer -c 3d_fullres -p nnUNetPlans --save_probabilities --save_npz

# nnUNetv2_ensemble -i ../nnUNet_WORKDIR/nnUNet_raw/Dataset111_CSpineSeg_UNANNO/predictTs_2d ../nnUNet_raw/Dataset111_CSpineSeg_UNANNO/predictTs_3d -o ../nnUNet_WORKDIR/nnUNet_raw/Dataset111_CSpineSeg_UNANNO/predictTs_ensemble

## Export model as a zip file (3d_fullres)
## cd to your destination folder first
# nnUNetv2_export_model_to_zip -d 108 -c 3d_fullres -o nnunet_3dfullres.zip
