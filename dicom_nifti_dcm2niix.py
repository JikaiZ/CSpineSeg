###################################################################
# Conver RAW DICOMs into nifti
# Rename the files based on de-identifiers
###################################################################

import os
import glob

import numpy as np
import pandas as pd




if __name__ == "__main__":
	# METADATA FILE
	metadata_df = pd.read_csv("<PATH_TO_METADATA_CSV>")
	# OUTPUT FOLDER
	output_folder = "<PATH_TO_OUTPUT_FOLDER>"
	# FOLDER CONTAINS RAW DICOMS
	src_folder = "<PATH_TO_RAW_DICOMS>" 
	options = """ -b n -z y -m y -f '%i_%g' """

	for idx, row in metadata_df.iterrows():
		de_pid, de_eid = str(row["DEID Patient ID"]), str(row["DEID Exam ID"])
		series_id = row["Series ID"]
		pid, eid = row["MRN"], row["Accession Number"]
		sd = row["sagT2-SeriesDescription"]
		sd_bash = sd.replace(" ", "\ ")
		study_folder = os.path.join(src_folder, pid, eid, sd_bash)
		# subdirs = os.listdir(os.path.join(src_folder, pid, eid, sd))
		if os.path.exists(os.path.join(src_folder, pid, eid, sd)) == False:
			print("****** Null input info ******\n")
			continue
		### try to pass the entire folder as input
		# cmd = "for file in `ls " + study_folder + "`; do dcm2niix -o " + output_folder + options + study_folder + "/${file}; break; done" 
		cmd = "dcm2niix -o " + output_folder + options + study_folder 
		print(cmd)
		os.system(cmd)
		print("="*50 + "\n")

		# RENAME to deidentify

		src_fname = os.path.join(output_folder, "%s_%s.nii.gz" % (pid, eid))
		## Optional code to manually deal with edge cases from the dcm2niix outputs ##
		# if os.path.exists(src_fname) == False:
		# 	src_fname = os.path.join(output_folder, "%s_%s_phMag.nii.gz" % (pid, eid))
		# 	if os.path.exists(src_fname) == False:
		# 		src_fname = os.path.join(output_folder, "%s_%sa.nii.gz" % (pid, eid))
		##############################################################################
		rename_fname = os.path.join(output_folder, "%s_%s_%s.nii.gz" % (de_pid, de_eid, series_id))
		os.rename(src_fname, rename_fname)

		# break
		