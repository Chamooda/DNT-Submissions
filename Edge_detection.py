import cv2

def canny_edge_detection(frame):
	# Convert the frame to grayscale for edge detection
    cv2.convertScaleAbs(frame, 10,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Apply Gaussian blur to reduce noise and smoothen edges
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5)
        
	

	# Perform Canny edge detection
    edges = cv2.Canny(blurred, 70, 135)
	
    return edges



if __name__ == '__main__':
    img = cv2.imread("thug duck.jpeg", cv2.IMREAD_COLOR)

    newimg = canny_edge_detection(img)
    cv2.imshow("Edge Detection", newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()