import qrcode
qr = qrcode.QRCode(
version =1,
box_size =40,
border=6)
data = input("Enter data: ")
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color= "white")

image.save("data.png")
my_label.setText("Operation completed succesfully.")
