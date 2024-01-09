import qrcode
qr = qrcode.QRCode(
#VERSION IS SIZE OF MATRIX BTN 1 & 40, 1 IS SMALLEST(21x21)
    version=1,
#ERROR CORRECTION  L=7% M=15%  Q=25% H=30%
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
#DATA TO PUT IN QR,ALSO FIT DATA IN THE MATRIX
qr.add_data('We love group projects')
qr.make(fit=True)

#CHANGE BACKGROUND & PAINTING OF QR, THEN SAVE.
img = qr.make_image(fill_color="black", back_color="white")
img.save("QR.png")
#NOT SPECIFYING A SAVING DIRECTORY MEANS IMAGE IS SAVED IN THE
#CURRENT WORKING DIRECTORY OF THE PROJECT
