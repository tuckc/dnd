import os
import sys
import fdfgen

field_names = ["ChBx Persuasion"] 
all_fields = []

for i in range(len(field_names)):
    field_value = True 
    all_fields.append((field_names[i], field_value))
#Create FDF file with these fields
fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
fdf_file = open("file_fdf.fdf","w") 
fdf_file.write(fdf_data) 
fdf_file.close()
#Run pdftk system command to populate the pdf file. The file "file_fdf.fdf" is pushed in to "input_pdf.pdf" thats generated as a new "output_pdf.pdf" file.
pdftk_cmd = "pdftk charsheet.pdf fill_form file_fdf.fdf output output_pdf.pdf"
os.system(pdftk_cmd)