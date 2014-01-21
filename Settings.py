def main():
    print "Mandelbrot Set - Version 2.0.0 - Ian Mallett - March 2008"
    print "Ian Mallett"
    print ""
    print "A good setting for the screen's size is 800x600."
    print "A good setting for the image's size is 400x300 for speed and 1600x1200 for nice."
    print ""
    while True:
        width = raw_input("Enter the Screen's Width: ")
        try:
            width = abs(int(width))
            break
        except:
            print "Well now, let's try that again, shall we?"
    while True:
        height = raw_input("Enter the Screen's Height: ")
        try:
            height = abs(int(height))
            break
        except:
            print "Well now, let's try that again, shall we?"
    while True:
        width2 = raw_input("Enter the Mandelbrot Set Image Width: ")
        try:
            width2 = abs(int(width2))
            break
        except:
            print "Well now, let's try that again, shall we?"
    while True:
        height2 = raw_input("Enter the Mandelbrot Set Image Height: ")
        try:
            height2 = abs(int(height2))
            break
        except:
            print "Well now, let's try that again, shall we?"
    return width, height, width2, height2
