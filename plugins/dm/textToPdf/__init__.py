file_name = "plugins/dm/textToPdf/__init__.py"
author_name = "telegram.dog/nabilanavab"
source_code = "https://github.com/nabilanavab/ilovepdf"

path = "plugins/dm/textToPdf"

# GLOBAL VARIABLES
# Just a DB Variable
TXT = {}

SCALE = {
        1 : "Landscape",
        2 : "Portrait"
    }

FONT = {
        1 : { "default" : True, "name" : "DejaVu" },
        2 : { "default" : False, "name" : "" },
        3 : { "default" : False, "name" : "" },
        4 : { "default" : False, "name" : "" },
        5 : { "default" : False, "name" : "" },
        6 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/3Dumb.ttf" },
        7 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/AlexBrush-Regular.ttf" },
        8 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/Archistico_Bold.ttf" },
        9 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/Archistico_Simple.ttf" },
        10 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/Calligraffiti.ttf" },
        11 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/DancingScript-Regular.otf" },
        12 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/FFF_Tusj.ttf" },
        13 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/GreatVibes-Regular.otf" },
        14 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/Kristi.ttf" },
        15 : { "default" : False, "name" : f"{path}/FONT_LIBRARY/Pacifico.ttf" },
    }

COLOR = {
        1 : { "color" : "white", "code" : (255, 255, 255) },
        2 : { "color" : "black", "code" : (0, 0, 0) },
        3 : { "color" : "grey", "code" : (128, 128, 128) },
        4 : { "color" : "red", "code" : (255, 0, 0) },
        5 : { "color" : "green", "code" : (0, 255, 0) },
        6 : { "color" : "blue", "code" : (0, 0, 255) }
}

BACKGROUND_L = {
        1 : { "isColor" : True, "code" : (255, 255, 255) },
        2 : { "isColor" : True, "code" : (0, 0, 0) },
        3 : { "isColor" : True, "code" : (128, 128, 128) },
        4 : { "isColor" : False, "code" : f"{path}/IMAGES/notebook.png" },
        5 : { "isColor" : False, "code" : f"{path}/IMAGES/sanscrit.png" },
        6 : { "isColor" : False, "code" : f"{path}/IMAGES/folded.png" },
        7 : { "isColor" : False, "code" : f"{path}/IMAGES/imageOne.png" },
        8 : { "isColor" : False, "code" : f"{path}/IMAGES/imageTwo.png" },
}

BACKGROUND_L = {
        1 : { "isColor" : True, "code" : (255, 255, 255) },
        2 : { "isColor" : True, "code" : (0, 0, 0) },
        3 : { "isColor" : True, "code" : (128, 128, 128) },
        4 : { "isColor" : False, "code" : f"{path}/IMAGES/notebook.png" },
        5 : { "isColor" : False, "code" : f"{path}/IMAGES/sanscrit.png" },
        6 : { "isColor" : False, "code" : f"{path}/IMAGES/folded.png" },
        7 : { "isColor" : False, "code" : f"{path}/IMAGES/imageOne.png" },
        8 : { "isColor" : False, "code" : f"{path}/IMAGES/imageTwo.png" },
}

# UPDATE CHANNEL: https://telegram.dog/ilovepdf_bot
