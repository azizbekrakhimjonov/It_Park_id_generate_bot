from PIL import Image, ImageFont, ImageDraw


def writer_func(id, fam, name, course):
    picID = id.replace('/', '_')

    img1 = Image.open(r'pic.png')
    img2 = Image.open(f"{picID}.png")

    width, height = img2.size
    left = 0
    top = width / 70
    right = width
    bottom = height
    m = img2.crop((left, top, right, bottom))

    weight = 320
    aspect_ratio = m.width / m.height
    new_height = int(weight / aspect_ratio)
    img2 = m.resize((weight, new_height))

    hexagon_size = (320, 370)  # 320
    mask_im = Image.new("L", img2.size, 0)

    draw = ImageDraw.Draw(mask_im)
    draw.polygon([(hexagon_size[0] // 2, 0), (hexagon_size[0], hexagon_size[1] // 4),
                  (hexagon_size[0], 3 * hexagon_size[1] // 4), (hexagon_size[0] // 2, hexagon_size[1]),
                  (0, 3 * hexagon_size[1] // 4), (0, hexagon_size[1] // 4)], fill=255)

    kichik_rasim = Image.composite(img2, Image.new("RGBA", img2.size), mask_im)  # keraksiz tomonlarni olib tashlash
    img1 = img1.copy()
    img1.paste(kichik_rasim, (156, 159), mask_im)  # set hexagon avatar idCard

    draw = ImageDraw.Draw(img1)

    # image size
    W, H = img1.size

    # fullname
    font = ImageFont.truetype("bebas.TTF", 39)
    _, _, w0, h = draw.textbbox((0, 0), f"ID: {id}", font=ImageFont.truetype("bebas_regular.ttf", 39))
    _, _, w, h = draw.textbbox((0, 0), fam, font=font)
    _, _, w1, h = draw.textbbox((0, 0), name, font=font)
    _, _, w2, h = draw.textbbox((0, 0), course, font=ImageFont.truetype("bebas_regular.ttf", 39))


    # set id
    draw.text(
        ((W - w0) / 2, 839),
        f"ID: {id}", fill='black',
        font=ImageFont.truetype("bebas_regular.ttf", 39),
    ),

    # set fam
    draw.text(
        ((W - w) / 2, 555),
        fam.upper(), fill='black',
        font=font,
    ),

    # set name
    draw.text(
        ((W - w1) / 2, 605),
        name.upper(), fill='black',
        font=font,
    ),

    # set course
    draw.text(
        ((W - w2) / 2, 730),
        course.upper(), fill='black',
        font=ImageFont.truetype("bebas_regular.ttf", 39),
    ),

    # img.show()
    img1.save(f'{picID}.png')
    print('Successfully is cut and saved')




# writer_func('Image', 'Rahimjonov', "Azizbek", 'Backend development')
