#!/usr/bin/env python
# This utility is meant to allow some human anlysis during image processing
# tests.  The only dependency is the python 2.7 stdlib, so it should run on
# OSX and most linux distros.

# This is a very basic tool that just renders the two images given
# as paths on the command line, and presents buttons for the user to
# judge whether the second looks okay. This exits with 0 if the OK
# button is clicked, and with 1 otherwise.  255 exit and usage message
# to STDERR can be expected with the wrong number of CLI opts passed.
#
# EXAMPLE USAGE
# /bin/lilcritic img1.gif img2.gif && echo "Test passed!"
#
# Both images must be in either GIF or PPM format, and must be resized to
# the size at which they will appear in the GUI.  As the GUI contains no
# zooming or resizing capability, it is almost certainly a terrible idea to
# give it images > 500px square or so.
#
# To reiterate: All image resizing must be done on the input files before
#               this utility is invoked
import Tkinter
import sys
import random 

class Application(Tkinter.Frame):
    # We'll take one of these at random for the button that exits with non-zero
    BAD_MESSAGES = [
        "Certainly Not Good", "Atrocious", "Gross.",
        "Fuggin Awful", "Definitely the worst thing since hitler.",
        "Akin to Satan", "Bad", "Terribad", "Astoundingly Wretched",
        "It lacks imagination.", "This piece is uninspired.",
        "What did Notch write this?", "Looks like the work of Joe.",
        "Lousy", "Utterly Inferior", "Garbage I say!  Garbage!"]

    @staticmethod
    def run(originalPath, judgementPath):
        app = Application(originalPath, judgementPath)
        app.mainloop()

    def createOkayButton(self):
        self.__createBtn("Ok", color="green", func=self.success)

    def createFugginAwfulButton(self):
        msg = random.choice(self.BAD_MESSAGES) 
        self.__createBtn(msg, color="red", func=self.failure)
    
    def success(self):
        sys.exit(0)

    def failure(self):
        sys.exit(1)
    
    def createOriginalImage(self, path):
        self.__createImg(path, "Original", place="top")
        
    def createJudgementImage(self, path):
        self.__createImg(path, "vvvvv Judge This One vvvvv", place="bottom")

    def __createBtn(self, label, color="black", func=None):
        button = Tkinter.Button(self)
        button["text"] = label
        button["fg"] = color
        button["command"] = func
        button.pack({"side": "bottom"})

    def __createImg(self, path, caption, place="bottom"):
        image = Tkinter.PhotoImage(file = path)
        label = Tkinter.Label(self, image=image)
        caption = Tkinter.Label(self, text=caption)
        caption.pack({"side": "top"})
        label.pack({"side": place})
        # We need to keep the photoimage around, as the image
        # comes up blank if it gets GC'd
        self.imageObjects.append(image)

    def __init__(self, originalImagePath, judgeImagePath):
        Tkinter.Frame.__init__(self)
        self.pack()
        self.imageObjects = list()

        self.createOkayButton()
        self.createFugginAwfulButton()
        self.createOriginalImage(originalImagePath)
        self.createJudgementImage(judgeImagePath)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("USAGE: lilcritic.py "\
            "<original file path> <judgement file path>\n")
        sys.exit(255)
    Application.run(sys.argv[1], sys.argv[2])
