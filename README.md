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



