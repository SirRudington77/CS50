"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""
def fileExtensions():
    # prompt user for a name of a file
    fileType = input("What is the file name?: ").lower().strip()

    # output file name if the file name ends with the type
    if fileType.endswith(".gif"):
        print("image/gif")
    elif fileType.endswith(".jpg") or fileType.endswith(".jpeg"):
        print("image/jpeg")
    elif fileType.endswith(".png"):
        print("image/png")
    elif fileType.endswith(".pdf"):
        print("application/pdf")
    elif fileType.endswith(".txt"):
        print("text/plain")
    elif fileType.endswith(".zip"):
        print("application/zip")
    # else app/oct-stream is outputted as default
    else:
        print("application/octet-stream")

# Personally feel like there is a better way to tighten this up but at the moment I can not think of one

fileExtensions()