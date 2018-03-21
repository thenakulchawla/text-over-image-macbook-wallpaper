from appscript import app, mactypes
import subprocess
import os
import textwrap
from random import randint
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def change_quote(quoteAddress, imageAddress, newImageAddress):
    img = Image.open(imageAddress)
    W, H = img.size
    font = ImageFont.truetype("/Library/Fonts/Times New Roman Italic.ttf", 35)
    draw = ImageDraw.Draw(img)
    msg = textwrap.fill(get_quote(quoteAddress),50)
    w, h = draw.textsize(msg)
    draw.text(((W-w)/3,(H-h)/4) , msg , (255 , 255 , 255) , font=font)
    img.save(newImageAddress)

def change_desktop_wallpaper(imageAddress):
    app('Finder').desktop_picture.set(mactypes.File(imageAddress))
    os.system("Killall Dock")
    #Script = ''' osascript -e 'tell application "System Events" to set picture of the current desktop to POSIX file "/Users/princechawla/timepass/quotesWall/myquotewallpaper.jpg" ' '''
    #os.system(Script)
    #os.system(''' osascript -e tell application "Finder" to set desktop picture to POSIX file "/Users/princechawla/timepass/quotesWall/myquotewallpaper.jpg" ''')
    #subprocess.Popen(Script , shell=True)
    #os.system("killall Dock")

def get_quote(quoteAddress):
    with open(quoteAddress) as quote_file:
        quotes=json.load(quote_file)
        numOfQuotes = int(quotes["quotes"][-1]["id"])
        randomNumber = randint(0,numOfQuotes)
        quoteToReturn = quotes["quotes"][randomNumber]["quote"]
    return quoteToReturn

if __name__ == "__main__":
    image_before = 'iu.jpeg'
    image_after= 'myQuoteWallpaper.jpg'
    quotes = 'cAndH.json'
    change_quote(quotes , image_before, image_after)
    change_desktop_wallpaper(image_after)
