from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Kindle Paper White Resolution
KINDLE_WIDTH = 658
KINDLE_HEIGHT = 905

# Space from side
KINDLE_LEFT = 30
KINDLE_TOP = KINDLE_HEIGHT - 70

# Number of lines in a page
LINE_MAX = 15
# Maxiumum length in a line
TEXT_MAX = 32

# Space between lines
TXT_LEADING = 50.0
# Font size in a textobject
FONT_SIZE = 30

# Length of separater
HYPHEN_LENGTH = 60

# Name of auhtor
AUTHOR = "JAPAN TODAY"

def addTextList(text_list, content, max_length):
    """
    devide content into a smaller text correspondent to max_length
    and return it as a list
    """
    line_word = 0 # total length of the line
    line_text = "" # text of the line

    #Split content. No args is fine
    words = content.split()
    for word in words:
        line_word += len(word) + 1 #Consider a blank as one char

        if line_word <= max_length:
            line_text += word + " "

        else:
            text_list.append(line_text)
            line_text = ""
            line_word = 0
            line_text += word + " "

    #Add a remained text into the list
    text_list.append(line_text)

def saveAsPdf(title, content):
    # Arial Font
    ARIAL_TTF = "./fonts/Arial.ttf"

    # filename
    filename = './pdfs/' + title + '.pdf'

    # Creat a canvas
    c = canvas.Canvas(filename)
    c.setAuthor(AUTHOR)
    c.setTitle(title)
    c.setPageSize((KINDLE_WIDTH, KINDLE_HEIGHT))

    # Register font and its size
    pdfmetrics.registerFont(TTFont('Arial', ARIAL_TTF))

    text_list = []
    # Store title and content into text_list
    addTextList(text_list, title, TEXT_MAX)
    text_list.append("-" * HYPHEN_LENGTH)
    addTextList(text_list, content, TEXT_MAX)

    # line counter
    line = 0

    # Creat a textobject
    textobject = c.beginText(KINDLE_LEFT, KINDLE_TOP) #座標を指定する。
    textobject.setFont("Arial", FONT_SIZE)
    textobject.setLeading(TXT_LEADING)

    # Write every single line to the Canvas
    # When num of lines exceeds the max, break a page
    for text in text_list:
        line += 1
        if line < LINE_MAX:
            textobject.textLine(text)
        else:
            c.drawText(textobject)
            c.showPage()
            del textobject

            textobject = c.beginText(KINDLE_LEFT, KINDLE_TOP) #座標を指定する。
            textobject.setFont("Arial", FONT_SIZE)
            textobject.setLeading(TXT_LEADING)
            textobject.textLine(text)
            line = 0

    # Write last page
    c.drawText(textobject)
    c.showPage()
    del textobject

    # Save the pdf
    c.save()

    # Return the filename of the saved
    return filename
