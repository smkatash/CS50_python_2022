import sys
from PIL import Image, ImageOps

def main():
    check_arguments()
    get_input_photos(sys.argv[1], sys.argv[2])
    sys.exit(0)

def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format1 = sys.argv[1].split(".")[-1]
        format2 = sys.argv[2].split(".")[-1]
        if format1 != "jpg" and format1 != "jpeg" and format1 != "png":
            sys.exit("Invalid output1")
        if format2 != "jpg" and format2 != "jpeg" and format2 != "png":
            sys.exit("Invalid output2")
        if format1 != format2:
            sys.exit("Input and output have different extensions")

def get_input_photos(f1, f2):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        before = Image.open(f1)
        after = ImageOps.fit(before, size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        after.paste(shirt, box=None, mask=shirt)
        after.save(f2)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()