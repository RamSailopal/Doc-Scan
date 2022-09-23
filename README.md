# Doc-Scan

A demonstration of document QR Code/text scanning using Tesseract and opencv

This demonstration first builds a jpg version of the following pdf document:

https://www.va.gov/vaforms/va/pdf/VA0730b.pdf

This jpg version is then used to display a web form along with a QR code for a unique document reference.

Once the web form is then printed, filled out by hand and scanned as a jpg, it is then processed to extract the printed/handwritten text along with the text associated with the QR code.

# Deployment

    git clone https://github.com/RamSailopal/Doc-Scan.git
    
    cd Doc-Scan
    
    docker-compose up
    

The script **pdfconvert/convert.py** is used to generate the initial jpeg.

The web form and then be viewed in a browser by navigating to:

http:dockerserveraddress:8080?ref=testref

Where **testref** is the reference to be translated into a QR code.

# Demonstration

This demonstration takes the following jpg:

https://github.com/RamSailopal/Doc-Scan/blob/main/pdfscan/FilledOut.jpg

It then processes the file to generate the following text

https://github.com/RamSailopal/Doc-Scan/blob/main/pdfscan/pdfscanout.txt

# Findings

The initial web form had to scaled out to display on one page and this effected the quality of the jpeg and subsequently the OCR results. Printed text was fine, but had written text proved difficult to process acccurates. QR codes were not processes at all.

As a comparison, A "screen grab" of part of the web form was taken and then the mouse used to add text (as if it were a pen). The resulting jgg can be viewed here:

https://github.com/RamSailopal/Doc-Scan/blob/main/pdfscan/doc-out1.png

The processed output can be seen here:

https://github.com/RamSailopal/Doc-Scan/blob/main/pdfscan/pdfscanout1.txt

With original scaling and no loss of quality, the QR code is processed correctly as well as the printed text. The mouse written text is again "patchy"



