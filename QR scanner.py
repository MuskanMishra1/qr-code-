import qrcode

myqr = qrcode.make("https://www.youtube.com/watch?v=PyDn2gU9DJo")
myqr.save("myqr.png", scale= 8 )
