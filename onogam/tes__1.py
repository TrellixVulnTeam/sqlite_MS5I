import tempfile
import cv2

#img = cv2.imread(r"C:\Users\onoga\Desktop\MyDocker\Git\origin\test\pos\2.png")
#cv2.imshow("",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

with tempfile.NamedTemporaryFile(delete=False) as tf:
    
    #print(tf.name)
    #with open(tf.name) as f:
    #    f.write(img)
    #    print(f.read())
        
tf.close()