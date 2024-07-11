import cv2
import matplotlib.pyplot as plt

#整張臉
# 圖像文件的相對路徑
image_file = "./teammates.jpg"

# 加載圖像
image = cv2.imread(image_file)

# 確保圖像成功加載
if image is None:
    print("Error: Unable to load image")
else:
    # 加載預訓練的人臉檢測分類器
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 確保分類器成功加載
    if classifier.empty():
        print("Error: Unable to load the classifier cascade file")
    else:
        # 將圖像轉換為灰度圖像
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 檢測人臉
        bboxes = classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # 將圖像從 BGR 轉換為 RGB（Matplotlib 需要 RGB 格式）
        im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 在圖像上繪製矩形框標記檢測到的人臉
        for box in bboxes:
            # 取得框的座標及寬高
            x, y, width, height = box
            x2, y2 = x + width, y + height
            # 加白色框
            cv2.rectangle(im_rgb, (x, y), (x2, y2), (255, 255, 255), 2)

        # 顯示圖像
        plt.imshow(im_rgb)
        plt.axis('off')
        plt.show()
