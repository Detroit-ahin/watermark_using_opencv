import cv2
import numpy as np
import matplotlib.pyplot as plt

#read the original image 
img1 = cv2.imread('D:\\create_watermark\\reflexs.jpg')
img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

#ploting rgb of original image 
plt.imshow(img_rgb);
print('image dtype ',img_rgb.dtype)  

#create a blank image
blank_img = np.zeros(shape=(img_rgb.shape[0],img_rgb.shape[1],3), dtype=np.uint8)    

# notice flip of x and y or org with image shape
font = cv2.FONT_HERSHEY_SIMPLEX  

#cv2.putText() method is used to draw a text string on any image.
#cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
cv2.putText(blank_img,  
            text='Ahin photography',  
            org=(img_rgb.shape[1]//8, img_rgb.shape[0]//2),   
            fontFace=font,  
            fontScale= 2,color=(255,0,0),  
            thickness=10,  
            lineType=cv2.LINE_4)  

plt.imshow(blank_img);  

# blend two images original image is made a little light and watermark dark  
blended = cv2.addWeighted(src1=img_rgb,alpha=0.7,src2=blank_img,beta=1, gamma = 0)  
plt.imshow(blended);

#draw new image to our directory
cv2.imwrite('new_watermarked.jpg', cv2.cvtColor(blended, cv2.COLOR_RGB2BGR))  
