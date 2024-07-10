# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:42:17 2024

@author: Yu-Chia
"""

import cv2
import matplotlib.pyplot as plt

# 圖像文件的相對路徑
image_file = "./teammates.jpg"

# 加載圖像
image = cv2.imread(image_file)

# 確保圖像成功加載
if image is None:
    print("Error: Unable to load image")
else:
    # 載入眼睛級聯分類器(eye cascade file)
    eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
    # 載入微笑級聯分類器(smile cascade file)
    smile_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    # 確保分類器成功加載
    if eye_classifier.empty():
        print("Error: Unable to load the classifier cascade file")
    elif smile_classifier.empty():
        print("Error: Unable to load the classifier cascade file")
    else:
        # 將圖像轉換為灰度圖像
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 偵測眼睛
        bboxes = eye_classifier.detectMultiScale(image)  
        # 將圖像從 BGR 轉換為 RGB（Matplotlib 需要 RGB 格式）
        im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 臉部加框
        for box in bboxes:
            # 取得框的座標及寬高
            x, y, width, height = box
            x2, y2 = x + width, y + height
            # 加白色框
            cv2.rectangle(im_rgb, (x, y), (x2, y2), (255,0,0), 1)           
        # 偵測微笑
        # scaleFactor=2.5：掃描時每次縮減掃描視窗的尺寸比例。
        # minNeighbors=20：每一個被選中的視窗至少要有鄰近且合格的視窗數
        bboxes = smile_classifier.detectMultiScale(image, 1.3,10)     
        #微笑加框
        for box in bboxes:
            # 取得框的座標及寬高
            x, y, width, height = box
            x2, y2 = x + width, y + height
            # 加白色框
            cv2.rectangle(im_rgb, (x, y), (x2, y2), (255,0,0), 1)
        #   break
        # 顯示圖像
        plt.imshow(im_rgb)
        plt.axis('off')
        plt.show()