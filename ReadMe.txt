This project is aimed to creating a software which can generate a ppt out of hand noted points. 
Idea is to use a python ocr (pytesseract) to read the notes and use the wikipedia database to generate ppt using python-pptx( a library to create and update powerpoint(.pptx) files)   

# Dependencies 
pytesserect
python-pptx
stop-words
nltk
PyQt4

# Important Links 
Link to python-pptx documentation- https://python-pptx.readthedocs.io/en/latest/
Link to pytesseract documentation- https://pypi.python.org/pypi/pytesseract
Link to wikipedia pyton api documentation- https://pypi.python.org/pypi/wikipedia/
Link to PyQt - http://zetcode.com/gui/pyqt4/firstprograms/

# Rough outline of steps  
Preprocess images for ocr. 
Extract meaningful data using ocr.
Information retrieval techniques are needed to be used for relevent searching in the offline wikipedia database. 
The text extracted from ocr has to be checked for spelling errors, word accuracy etc. 
Text normalization has to be done, stop words have to be removed if required.
Search results need to be ranked 

#GUI 
PyQt is a possible option for creating the gui 

#OCR 
A typical OCR system consists of the following steps:
• image preprocessing, e.g. noise attenuation, correction of image orientation;
• image binarization, usually performed adaptively [2];
• segmentation [3], usually hierarchical (recognizing page layout, detecting text areas (and tables, figures etc.), then text paragraphs, individual lines, then segmenting lines into words, and finally words into characters);
• actual recognition (supervised or unsupervised) [4, 5];
• spellchecker-guided postprocessing;
• saving output in some popular format (html, PDF, LaTeX)