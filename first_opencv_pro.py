import cv2 as cv
#image = cv.imread('E:\Sagor Graduate CV\Final.png')

#cv.imshow('Final', image)

#cv.waitKey(0)

def rescaleFrame(frame, scale = 0.75):

    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture(r'C:\Users\janea\Downloads\spider.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)

    cv.imshow('Video Resize', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
         break
capture.release()
cv.destroyAllWindows()
 