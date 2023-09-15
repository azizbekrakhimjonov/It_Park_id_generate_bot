from PIL import Image, ImageFont, ImageDraw
from fpdf import FPDF

def writer_func(id, fam, name, course, user_img):

    img1 = Image.open(r'pic.png')
    img2 = Image.open(f"{user_img}.png")

    width, height = img2.size
    left = 0
    top = width / 70
    right = width
    bottom = height
    m = img2.crop((left, top, right, bottom))

    img2 = m.resize((320, 370))

    hexagon_size = (320, 370)  # 320
    mask_im = Image.new("L", img2.size, 0)

    draw = ImageDraw.Draw(mask_im)
    draw.polygon([(hexagon_size[0] // 2, 0), (hexagon_size[0], hexagon_size[1] // 4),
                  (hexagon_size[0], 3 * hexagon_size[1] // 4), (hexagon_size[0] // 2, hexagon_size[1]),
                  (0, 3 * hexagon_size[1] // 4), (0, hexagon_size[1] // 4)], fill=255)

    kichik_rasim = Image.composite(img2, Image.new("RGBA", img2.size), mask_im)  # keraksiz tomonlarni olib tashlash
    img1 = img1.copy()
    img1.paste(kichik_rasim, (163, 164), mask_im)  # set hexagon avatar idCard


    draw = ImageDraw.Draw(img1)

    # image size
    W, H = img1.size

    # fullname
    font = ImageFont.truetype("bebas.TTF", 36)
    _, _, w0, h = draw.textbbox((0, 0), id, font=font)
    _, _, w, h = draw.textbbox((0, 0), fam, font=font)
    _, _, w1, h = draw.textbbox((0, 0), name, font=font)
    _, _, w2, h = draw.textbbox((0, 0), course, font=font)
    _, _, w3, h = draw.textbbox((0, 0), 'DEVELOPMENT', font=font)

    # set id
    draw.text(
        ((W - w0) / 2, 830),
        id, fill='black',
        font=font,
    ),

    # set fam
    draw.text(
        ((W - w) / 2, 550),
        fam.upper(), fill='black',
        font=font,
    ),

    # set name
    draw.text(
        ((W - w1) / 2, 600),
        name.upper(), fill='black',
        font=font,
    ),

    # set course
    draw.text(
        ((W - w2) / 2, 700),
        course.upper(), fill='black',
        font=font,
    ),

    # set course development text
    # draw.text(
    #     ((W - w3) / 2, 750),
    #     'development'.upper(), fill='black',
    #     font=font,
    # ),


    # img.show()
    img1.save(f'{name}.png')
    print('Successfully is cut and saved')

    class PDF(FPDF):
        def header(self):
            pass

        def footer(self):
            pass

    pdf = PDF()
    pdf.set_auto_page_break(auto=True)
    image_files = [f'{name}.png', "back.jpg"]
    x = 10
    y = 10
    w = 190
    h = 270

    for image_file in image_files:
        pdf.add_page()
        pdf.image(image_file, x=x, y=y, w=w, h=h)
    pdf_filename = f"{name}.pdf"
    pdf.output(pdf_filename)
    print(f"PDF generated as {pdf_filename}")



writer_func('011/321', 'Rahimjonov', "Azizbek", 'Backend development',  'user')