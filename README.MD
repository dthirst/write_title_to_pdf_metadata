# a simple tool that sets (parts of) the filename as title for PDFs
********
If your PDF filenames are formatted as `<author> - <year> - <title>.pdf`, this tool will put `<title>` in the title metadata field of your pdf. Otherwise it will just put the whole filename as title.
usage:<br/>
* download script<br/>
* `conda install pdfrw` or `pip install pdfrw`<br/>
* run `python write_title_to_pdf_metadata.py -p <PATH_TO_YOUR_PDFs>`
WARNING: this will overwrite your PDF files. Make a backup before you use this. The tool is provided as it is. I do not assume any liability for lost data.