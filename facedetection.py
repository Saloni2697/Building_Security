import cv2 

#ph=387678
def fd(ph):
    print("ph",ph)
    if(ph==0):
        path=r'C:\\Users\\Saloni\\Desktop\\Building_Security\\'
    else:
        path=r'C:\\Users\\Saloni\\Desktop\\Building_Security\\Images\\'
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while 1: 
        ret, img = cap.read() 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces)>0 and len(faces)<2:
            print("xyz")       
        else:
            print("abc")
    
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 115:
            cv2.imwrite(path+str(ph)+'.jpg',img)
            break 
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


#fd(ph)
