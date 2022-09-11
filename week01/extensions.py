def main():
    str = input("Input file type: ").lower().strip()
    if "." in str:
        str = str.rsplit(".", 1)
        if "gif" in str[1]:
            print("image/gif")
        elif "jpg" in str[1] or "jpeg" in str[1]:
            print("image/jpeg")
        elif "png" in str[1]:
            print("image/png")
        elif "pdf" in str[1]:
            print("application/pdf")
        elif "txt" in str[1]:
            print("text/plain")
        elif "zip" in str[1]:
            print("application/zip")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")

main()