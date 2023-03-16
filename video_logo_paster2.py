from moviepy.editor import *
import numpy as np

def createOrgVideo(logoNumber):
    video = VideoFileClip('movie.mp4')

    logosPath = "C:\\Users\\User\\Documents\\הודעות לגזברים\\orgDATA\\logos\\"
    logo = logosPath + 'logo'+ str(logoNumber) +'.png'
    patch = 'patch.png'
    patch2 = 'patch2.png'

    def addImg(logoName, duration, position,size, startTime):
        img = ImageClip(logoName, duration=duration)
        img = img.set_position(position).resize(size)
        img = img.set_start(startTime)
        return img

    img1 = addImg(logo, 2,("center", 580), (300,300), 2)
    img2 = addImg(logo, 0.25,("center", 770), (170,170), 11.38)
    img3 = addImg(logo, 0.31,("center", 770), (170,170), 13.00)
    img4 = addImg(logo, 0.48,("center", 710), (220,220), 16.02)
    img5 = addImg(logo, 4.20,("center", 710), (220,220), 20.20)
    img6 = addImg(logo, 0.84,("center", 710), (220,220), 26.28)
    img7 = addImg(logo, 0.67,("center", 710), (220,220), 28.86)
    img8 = addImg(patch, 4.40,(183, 71), (105,65), 32.85)
    img9 = addImg(patch2, 1.31,(390, 785), (105,35), 34.15)
    img10 = addImg(logo, 3.17,("center", 730), (190,190), 42.82)


    result = CompositeVideoClip([video, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10])
    # result.write_videofile("VideoOutput\\orgVideo"+ str(logoNumber) +".mp4")

    result1 = result.subclip(0, 23.5)
    result2 = result.subclip(23, 47)

    result1.write_videofile("VideoOutput\\splited\\orgVideo"+ str(logoNumber+1) +"A.mp4")
    result2.write_videofile("VideoOutput\\splited\\orgVideo"+ str(logoNumber+1) +"B.mp4")


# orgsLogos = [26, 156, 194, 3, 5, 174, 129, 45, 207, 89, 189, 95, 203, 158, 60, 159, 195, 111, 85, 27, 210, 54, 98, 13, 130]
# for n in orgsLogos:
#     createOrgVideo(int(n)-1) 

#  # single video
createOrgVideo(int(186)-1) 