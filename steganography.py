from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="images/UG_encoded_image.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255,0,144)
    decoded_image.save("images/UG_decode.png")

def write_text(text_to_write, image_size):
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encode_image(text_to_encode, template_image="images/UG.png"):
    image = Image.open(template_image)
    red = image.split()[0]
    green = image.split()[1]
    blue = image.split()[2]
    x_size = image.size[0]
    y_size = image.size[1]
    image_text = write_text(text_to_encode, image.size)
    encode = image_text.convert('1')
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            red_pix = bin(red.getpixel((i,j)))
            pix = red.getpixel((i,j))
            encode_pix = bin(encode.getpixel((i,j)))
            if encode_pix[-1] == '1':
                red_pix = red_pix[:-1] + '1'
            else:
                red_pix = red_pix[:-1] + '0'
            pixels[i, j] = (int(red_pix, 2), green.getpixel((i,j)), blue.getpixel((i,j)))

    encoded_image.save("images/UG_encoded_image.png")

if __name__ == '__main__':
    print("Decoding the image...")
    decode_image()
    print("Encoding the image...")
    encode_image("Krypto is life, potrzebne 3 na koniec")