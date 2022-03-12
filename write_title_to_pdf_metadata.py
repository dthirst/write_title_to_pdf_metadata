#!/usr/bin/env conda run -n pdfrw python3
"""Written by Demian Keihsler at the Institute of Molecular Pathology, Vienna, Austria, 2022-03-10"""
import os, sys, argparse
from pdfrw import PdfReader, PdfWriter

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str)
args = parser.parse_args()

for root, dirs, files in os.walk(os.path.normpath(args.path)):
    for file in  files:
        if '.pdf' in file:
            try:
                pdffile = PdfReader(os.path.join(root, file))
                try:
                    pdffile.Info.Title = file.split(' - ')[2]
                    print(file.split(' - ')[2])
                except:
                    pdffile.Info.Title = file
                    print(f'fail: {file}')
                PdfWriter(os.path.join(root, file), trailer = pdffile).write()
            except Exception as e:
                print(e)
                pass
