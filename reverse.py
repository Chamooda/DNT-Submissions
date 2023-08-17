
import cv2
cap = cv2.VideoCapture("Wide.mp4")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)

check , vid = cap.read()


counter = 0


check = True

frame_list = []


while(check == True):
    
    
    cv2.imwrite("frame%d.jpg" %counter , vid)
    check , vid = cap.read()
    

    frame_list.append(vid)
    
    counter += 1


frame_list.pop()

frame_list.reverse()

cap.release()
cv2.destroyAllWindows()



path = "Hehe.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(path, fourcc, 1.5,(width, height))

for frame in frame_list:
	cv2.imshow("frame", frame)
	output.write(frame)
	k = cv2.waitKey(24)
	if k == ord("q"):
		break

cap.release()
output.release()
cv2.destroyAllWindows()