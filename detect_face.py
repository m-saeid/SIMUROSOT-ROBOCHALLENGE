import cv2

def face(img,i):
	# Load the cascade
	face_cascade = cv2.CascadeClassifier('detect_face/haarcascade_frontalface_default.xml')

	# Read the input image
	#img = cv2.imread('test.jpg')

	#img = cv2.imread(img)

	# Convert into grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)

	# Draw rectangle around the faces
	for (x, y, w, h) in faces:
	    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
	try:	
	    print(x)
	except:
	    pass

	# Display the output
	#cv2.imshow('img', img)
	#cv2.waitKey()

	#cv2.imwrite(img, '/home/saeid/Documents/The last of Us/rescue/1.png')
	add = 'rescue/'+str(i)+'.png'
	cv2.imwrite(add, img)
	print('OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')


#img = cv2.imread('test.png')
#face(img,1)
