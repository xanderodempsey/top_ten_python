# Import the function for downloading web pages
from urllib2 import *

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser
from HTMLParser import *

# Import SQL Functions
from sqlite3 import *



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data = characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image, if possible
    try:
        pil_image = Image.open(image_chars)
    except:
        raise Exception, 'Cannot recognise image given to "image_to_Photoimage" function\n' + \
                         'Confirm that image was downloaded correctly'
    
    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



global string1
global string2
global string3
global string4
global string5
global string6
global string7
global string8
global string9
global string10

#Create the entire Top 10 Movie List into one function that can be called when button is pressed
def createWindowMovieList():
    #Set up the Screen
    theMovieWindow = Toplevel()
    theMovieWindow.resizable(0,0)
    theMovieWindow.title("Top Ten Movies")
    theMovieWindow.geometry("600x600")
    theMovieWindow.configure(background="white")
    #Main Title
    theMovieListTitle = Label(theMovieWindow, text = "Top 10 Movies:", font = ("Broadway", 22), bg="white")
    theMovieListTitle.pack()
    
    #Open the website, read and update HTML, and close connection
    webPage = urlopen("http://www.imdb.com/chart/top")
    htmlCode = webPage.read()
    webPage.close()
    sqlButton.configure(state=NORMAL)
    theList = findall('title=".*>(.+)</a>', htmlCode)
    #List the Top 10 movies
    global string1
    string1 = theList[1]
    global string2
    string2 = theList[2]
    global string3
    string3 = theList[3]
    global string4
    string4 = theList[4]
    global string5
    string5 = theList[5]
    global string6
    string6 = theList[6]
    global string7
    string7 = theList[7]
    global string8
    string8 = theList[8]
    global string9
    string9 = theList[9]
    global string10
    string10 = theList[10]
    
    theMovieLabel1 = Label(theMovieWindow, text = ("1. " + string1),font = ("Broadway") ,bg="white")
    theMovieLabel1.pack()
    theMovieLabel2 = Label(theMovieWindow, text = ("2. " + string2),font = ("Broadway") , bg="white")
    theMovieLabel2.pack()
    theMovieLabel3 = Label(theMovieWindow, text = ("3. " + string3),font = ("Broadway") , bg="white")
    theMovieLabel3.pack()
    theMovieLabel4 = Label(theMovieWindow, text = ("4. " + string4),font = ("Broadway") , bg="white")
    theMovieLabel4.pack()
    theMovieLabel5 = Label(theMovieWindow, text = ("5. " + string5),font = ("Broadway") , bg="white")
    theMovieLabel5.pack()
    theMovieLabel6 = Label(theMovieWindow, text = ("6. " + string6),font = ("Broadway") , bg="white")
    theMovieLabel6.pack()
    theMovieLabel7 = Label(theMovieWindow, text = ("7. " + string7),font = ("Broadway") , bg="white")
    theMovieLabel7.pack()
    theMovieLabel8 = Label(theMovieWindow, text = ("8. " + string8),font = ("Broadway") , bg="white")
    theMovieLabel8.pack()
    theMovieLabel9 = Label(theMovieWindow, text = ("9. " + string9),font = ("Broadway") , bg="white")
    theMovieLabel9.pack()
    theMovieLabel10 = Label(theMovieWindow, text = ("10. " + string10),font = ("Broadway") , bg="white")
    theMovieLabel10.pack()

    #Import a picture from the Internet
    imageURL = urlopen("http://cdn-9chat-fun.9cache.com/media/photo/aobDaXZM3_480w_v1.jpg")
    readImage = imageURL.read()
    imageURL.close()
    picture = image_to_PhotoImage(readImage, width = None, height = None)
    imageLabel = Label(theMovieWindow, image = picture, bg="white")
    imageLabel.photo = picture
    imageLabel.pack()

    #Label to give credit to the source material
    retrievalLabel = Label(theMovieWindow, text = "List retrieved from http://www.imdb.com/chart/top", bg="white")
    retrievalLabel.pack()

    theMovieWindow.mainloop()

#Create the entire Top 10 Music List into one function that can be called when button is pressed
def createWindowMusicList():
    #Set up the Screen
    theMusicWindow = Toplevel()
    theMusicWindow.resizable(0,0)
    theMusicWindow.title("Top Ten Songs")
    theMusicWindow.geometry("410x550")
    theMusicWindow.configure(background="#EC770E")

    #Main Title
    theMusicListTitle = Label(theMusicWindow, text = "Billboard's Top 10 Songs:", font = ("Magneto", 22), bg="#EC770E")
    theMusicListTitle.pack()

    #Import a picture from the Internet
    imageURL = urlopen("http://www.monitor.si/media/monitor/slike/novice/2015/september/__300/applemusic.jpg")
    readImage = imageURL.read()
    imageURL.close()
    picture = image_to_PhotoImage(readImage, width = None, height = None)
    imageLabel = Label(theMusicWindow, image = picture, bg="#EC770E")
    imageLabel.photo = picture
    imageLabel.pack()

    #Open the website, read the HTML (Update if need be), and close connection
    webPage = urlopen("http://www.billboard.com/charts/hot-100")
    htmlCode = webPage.read()
    webPage.close()
    sqlButton.configure(state=NORMAL)
    theList = findall('<h2 class="chart-row__song">(.+)</h2>', htmlCode)
    #List the Top 10 Songs
    global string1
    string1 = theList[0].replace('&#039;', "'")
    global string2
    string2 = theList[1].replace('&#039;', "'")
    global string3
    string3 = theList[2].replace('&#039;', "'")
    global string4
    string4 = theList[3].replace('&#039;', "'")
    global string5
    string5 = theList[4].replace('&#039;', "'")
    global string6
    string6 = theList[5].replace('&#039;', "'")
    global string7
    string7 = theList[6].replace('&#039;', "'")
    global string8
    string8 = theList[7].replace('&#039;', "'")
    global string9
    string9 = theList[8].replace('&#039;', "'")
    global string10
    string10 = theList[9].replace('&#039;', "'")
    
    theMusicLabel1 = Label(theMusicWindow, text = ("1. " + string1), font = ("Arial"), bg="#EC770E")
    theMusicLabel1.pack()
    theMusicLabel2 = Label(theMusicWindow, text = ("2. " + string2), font = ("Arial"), bg="#EC770E")
    theMusicLabel2.pack()
    theMusicLabel3 = Label(theMusicWindow, text = ("3. " + string3), font = ("Arial"), bg="#EC770E")
    theMusicLabel3.pack()
    theMusicLabel4 = Label(theMusicWindow, text = ("4. " + string4), font = ("Arial"), bg="#EC770E")
    theMusicLabel4.pack()
    theMusicLabel5 = Label(theMusicWindow, text = ("5. " + string5), font = ("Arial"), bg="#EC770E")
    theMusicLabel5.pack()
    theMusicLabel6 = Label(theMusicWindow, text = ("6. " + string6), font = ("Arial"), bg="#EC770E")
    theMusicLabel6.pack()
    theMusicLabel7 = Label(theMusicWindow, text = ("7. " + string7), font = ("Arial"), bg="#EC770E")
    theMusicLabel7.pack()
    theMusicLabel8 = Label(theMusicWindow, text = ("8. " + string8), font = ("Arial"), bg="#EC770E")
    theMusicLabel8.pack()
    theMusicLabel9 = Label(theMusicWindow, text = ("9. " + string9), font = ("Arial"), bg="#EC770E")
    theMusicLabel9.pack()
    theMusicLabel10 = Label(theMusicWindow, text = ("10. " + string10), font = ("Arial"), bg="#EC770E")
    theMusicLabel10.pack()
    
    #Label to give credit to source
    retrievalLabel = Label(theMusicWindow, text = "List retrieved from http://www.billboard.com/charts/hot-100", bg="#EC770E")
    retrievalLabel.pack()
    
    theMusicWindow.mainloop()

#Create the entire Top 10 Game List into one function that can be called when button is pressed
def createWindowGameList():
    #Set up screen
    theGameWindow = Toplevel()
    theGameWindow.resizable(0,0)
    theGameWindow.title("Top Ten PC Games")
    theGameWindow.geometry("510x590")
    theGameWindow.configure(background="#FFD306")

    #Import picture from the Internet
    imageURL = urlopen("http://static.endgame.vn/tinmoi/store/gameportal/images/thumb/news/0/11/11273/1.jpg")
    readImage = imageURL.read()
    imageURL.close()
    picture = image_to_PhotoImage(readImage, width = None, height = None)
    imageLabel = Label(theGameWindow, image = picture, bg="#FFD306")
    imageLabel.photo = picture
    imageLabel.pack()
    
    #Main Title
    theGameListTitle = Label(theGameWindow, text = "Top 10 Best Selling PC Games:", font = ("Razer Header Regular Oblique", 22), bg="#FFD306")
    theGameListTitle.pack()

    #Open the website, read the HTML (Update if need be), and close connection
    webPage = urlopen("http://www.statista.com/statistics/275226/best-selling-pc-games-of-all-time-worldwide/")
    htmlCode = webPage.read()
    webPage.close()
    sqlButton.configure(state=NORMAL)
    theList = findall('<td>(.*)</td>', htmlCode)
    #List the Top 10 Games
    global string1
    string1 = theList[0].replace('&#039;', "'")
    global string2
    string2 = theList[1].replace('&#039;', "'")
    global string3
    string3 = theList[2].replace('&#039;', "'")
    global string4
    string4 = theList[3].replace('&#039;', "'")
    global string5
    string5 = theList[4].replace('&#039;', "'")
    global string6
    string6 = theList[5].replace('&#039;', "'")
    global string7
    string7 = theList[6].replace('&#039;', "'")
    global string8
    string8 = theList[8].replace('&#039;', "'")
    global string9
    string9 = theList[9].replace('&#039;', "'")
    global string10
    string10 = theList[10].replace('&#039;', "'")

    theGameLabel1 = Label(theGameWindow, text = ("1. " + string1), bg="#FFD306")
    theGameLabel1.pack()
    theGameLabel2 = Label(theGameWindow, text = ("2. " + string2), bg="#FFD306")
    theGameLabel2.pack()
    theGameLabel3 = Label(theGameWindow, text = ("3. " + string3), bg="#FFD306")
    theGameLabel3.pack()
    theGameLabel4 = Label(theGameWindow, text = ("4. " + string4), bg="#FFD306")
    theGameLabel4.pack()
    theGameLabel5 = Label(theGameWindow, text = ("5. " + string5), bg="#FFD306")
    theGameLabel5.pack()
    theGameLabel6 = Label(theGameWindow, text = ("6. " + string6), bg="#FFD306")
    theGameLabel6.pack()
    theGameLabel7 = Label(theGameWindow, text = ("7. " + string7), bg="#FFD306")
    theGameLabel7.pack()
    theGameLabel8 = Label(theGameWindow, text = ("8. " + string8), bg="#FFD306")
    theGameLabel8.pack()
    theGameLabel9 = Label(theGameWindow, text = ("9. " + string9), bg="#FFD306")
    theGameLabel9.pack()
    theGameLabel10 = Label(theGameWindow, text = ("10. " + string10), bg="#FFD306")
    theGameLabel10.pack()


    #Give credit to source
    retrievalLabel = Label(theGameWindow, text = "List retrieved from http://store.steampowered.com/search/?filter=topsellers", bg="#FFD306")
    retrievalLabel.pack()
   

    theGameWindow.mainloop()

#Function that saves most recent Top Ten List into SQLite
def saveToSQL():
    connection = connect(database= 'top_ten.db')
    top_ten_db = connection.cursor()
    top_ten_db.execute("DELETE FROM Top_Ten")
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(1, ?)""", (string1,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(2, ?)""", (string2,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(3, ?)""",(string3,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(4, ?)""", (string4,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(5, ?)""", (string5,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(6, ?)""", (string6,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(7, ?)""", (string7,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(8, ?)""", (string8,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(9, ?)""", (string9,))
    top_ten_db.execute("""INSERT INTO Top_Ten VALUES(10,?)""", (string10,))
    connection.commit()
    top_ten_db.close()
    connection.close()

#Create the Splash (or Main) screen
theMainWindow = Tk()
theMainWindow.resizable(0,0)
theMainWindow.title("Top Ten Entertainment")
theMainWindow.geometry("400x400")
theMainWindow.configure(background="#0E80FB")


#Create the Main title
theLabel = Label(theMainWindow, text="Entertainment Top Ten Lists", font=("Arial", 22), bg="#0E80FB", fg="white")
theLabel.pack()

#Import a Top 10 picture from the Internet
imageURL = urlopen("http://i.imgur.com/giWb6m4.gif?1")
readImage = imageURL.read()
imageURL.close()
picture = gif_to_PhotoImage(readImage)
imageLabel = Label(theMainWindow, image = picture, bg="#0E80FB")
imageLabel.photo = picture
imageLabel.pack()


#Set up button
sqlButton = Button(theMainWindow, text="Save latest selection", state=DISABLED, width=20, command=saveToSQL)
sqlButton.pack(side="bottom", padx=5,pady=5)
#Set up button
theMovieButton = Button(theMainWindow, text="Top 10 Movies", width=20, bg="white", command=createWindowMovieList)
theMovieButton.pack(side="bottom",padx=5,pady=5)
#Set up button
theMusicButton = Button(theMainWindow, text="Top 10 Songs", width=20, bg="#EC770E", command=createWindowMusicList)
theMusicButton.pack(side="bottom",padx=5,pady=5)
#Set up button
theGameButton = Button(theMainWindow, text="Top 10 PC Games", width=20, bg="#FFD306", command=createWindowGameList)
theGameButton.pack(side="bottom",padx=5,pady=5)



theMainWindow.mainloop()
