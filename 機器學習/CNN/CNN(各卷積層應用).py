# 卷積的影像轉換函數，padding='same'
from skimage.exposure import rescale_intensity
import skimage
import cv2
import numpy as np

def convolve(image, kernel):
    # 取得圖像與濾波器的寬高
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    # 計算 padding='same' 單邊所需的補零行數
    pad = int((kW - 1) / 2)
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

    # 卷積
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):            
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]  # 裁切圖像            
            k = (roi * kernel).sum()                               # 卷積計算
            output[y - pad, x - pad] = k                           # 更新計算結果的矩陣 

    # 調整影像色彩深淺範圍至 (0, 255)
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
   
    return output     # 回傳結果影像

#灰階
# 自 skimage 取得內建的圖像
image = skimage.data.chelsea()
cv2.imshow("original", image)

# 灰階化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

#按 Enter 關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------
# 小模糊 filter
smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))

# 卷積
convoleOutput = convolve(gray, smallBlur)
opencvOutput = cv2.filter2D(gray, -1, smallBlur)
cv2.imshow("little Blur", convoleOutput)

#----------------------------------------
# 大模糊
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

# 卷積
convoleOutput = convolve(gray, largeBlur)
opencvOutput = cv2.filter2D(gray, -1, largeBlur)
cv2.imshow("large Blur", convoleOutput)

# 按 Enter 關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------
# sharpening filter(銳利化)
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

# 卷積
convoleOutput = convolve(gray, sharpen)
opencvOutput = cv2.filter2D(gray, -1, sharpen)
cv2.imshow("sharpen", convoleOutput)

# 按 Enter 關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------
# Laplacian filter(拉普拉斯濾波器)
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

# 卷積
convoleOutput = convolve(gray, laplacian)
opencvOutput = cv2.filter2D(gray, -1, laplacian)
cv2.imshow("laplacian edge detection", convoleOutput)

# 按 Enter 關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
     
#----------------------------------------
# Sobel x-axis filter(X軸邊緣偵測)
sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

# 卷積
convoleOutput = convolve(gray, sobelX)
opencvOutput = cv2.filter2D(gray, -1, sobelX)
cv2.imshow("x-axis edge detection", convoleOutput)

# 按 Enter 關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------

# # Sobel y-axis filter(Y軸邊緣偵測)
sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

# 卷積
#convoleOutput = convolve(gray, sobelY)
opencvOutput = cv2.filter2D(gray, -1, sobelY)
#cv2.imshow("y-axis edge detection", convoleOutput)
cv2.imshow("y-axis edge detection", opencvOutput)

# 按 Enter 關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()