from PIL import Image

# mac = Image.open('Images/example.jpg')

# mac.show()
# print(mac.size)

# newmac = mac.crop((0,0,100,100))  # the first two digits (0,0 talks about the starting place to crop from and the last two 100,100) talks about where to stop
# newmac = mac.crop((900,900,1200,1200))
# newmac.show()

# pencils = Image.open("Images/pencils.jpg")
# pens = pencils.crop((0,0,pencils.size[0]/3,pencils.size[1]/4))
# pens.show()
'''
    Pasting an image to another
'''
# pencils.paste(im=pens,box=(500,500))
# pencils.show()


# pencils.resize((3500,500)).show() ##not in place
# print(pencils.size)
# pencils.show()


'''
    Color Transparency
'''

# red = Image.open('Images/red_color.jpg')
# blue = Image.open('Images/blue_color.png')
## the alpha variable represents the transperancy of the image
# blue.show()
# red.putalpha(100) ## totall transparent (0-255),, in Place
# red.show()

# blue.paste(im=red,box=(0,0),mask=red) ## happends in place,, to merge two images
# blue.show()
# red.putalpha(90)
#
# red.save("Images/light red.png")

'''
    Challenge
'''


matrix = Image.open("Images/word_matrix.png")
mask = Image.open("Images/mask.png")
mask = mask.resize(matrix.size)
mask.putalpha(80)
matrix.paste(im=mask,box=(0,0),mask=mask)
matrix.show()