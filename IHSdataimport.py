#!/usr/bin/env python


import arcpy
import os
import shutil
import zipfile
import glob

print "making new IHSdump folder....."

dir = "U:\\IHSdump"
os.makedirs(dir)

print "Copying source files from E:......"

src_files = os.listdir("E:\\")
for file_name in src_files:
    full_file_name = os.path.join("E:\\", file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, "U:\\IHSdump")
                       

os.chdir('U:\\IHSdump')

print "Unzipping data......"

zip_file = glob.glob('*.zip')

for zip_filename in zip_file:
    zip_handler = zipfile.ZipFile(zip_filename, 'r')
    zip_handler.extractall()
    
import arcpy

arcpy.env.overwriteOutput=True
ShapefilesDirectory = r"U:\\IHSdump"
arcpy.env.workspace = ShapefilesDirectory
fldList = arcpy.ListWorkspaces('*','Folder')
datasets = arcpy.ListFeatureClasses()
for fld in fldList:
    print "Folders are shown below...."
    print fld
for datas in datasets:
    print "copying dataset:"
    print datas
    arcpy.FeatureClassToGeodatabase_conversion(datas, "G:\\Basedata\IHS.gdb")
    print "Success! File Copied to G:......."

print "All files succesfully copied......"
print "Deleting IHSdump folder from U:"

shutil.rmtree("/IHSdump")

print "script complete"
