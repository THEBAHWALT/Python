import pydicom
import cv2
import numpy as np
import matplotlib.pyplot as plt

dicom_data = pydicom.dcmread("D:\\Python learning\\Project\\HandBoneXRay\\22b63b2c78bc96711c0af031585f327874f56f18a5f42a6a7f004b8ce4a8ed26.dcm", force=True)
#dicom_data = pydicom.dcmread("D:\\Python learning\\Project\\HandBoneXRay\\processed_image.dcm", force=True)
pixel_data = dicom_data.pixel_array
original_bit_store = dicom_data.BitsStored
original_bit_allocated = dicom_data.BitsAllocated
original_high_bit = dicom_data.HighBit
original_photometric_interpretation = dicom_data.PhotometricInterpretation
original_pixel_representation = dicom_data.PixelRepresentation
original_transfer_syntax_uid = dicom_data.file_meta.TransferSyntaxUID
original_rows = dicom_data.Rows
original_columns = dicom_data.Columns
original_samples_per_pixel = dicom_data.SamplesPerPixel
print("original_bit_store: ", original_bit_store)
print("original_bit_allocated: ", original_bit_allocated)
print("original_high_bit: ", original_high_bit)
print("original_photometric_interpretation: ", original_photometric_interpretation)
print("original_pixel_representation: ", original_pixel_representation)
print("original_transfer_syntax_uid: ", original_transfer_syntax_uid)
print("original_rows: ", original_rows)
print("original_columns: ", original_columns)
print("original_samples_per_pixel: ", original_samples_per_pixel)

# 資料轉CV_8UC1格式
threshold = cv2.convertScaleAbs(pixel_data)

# 找輪廓
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 畫輪廓
contour_image = np.zeros_like(pixel_data)
cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 1)
c = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(c)
cv2.rectangle(contour_image, (x, y), (x + w, y + h), (255, 255, 255), 1)
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(contour_image, [box], 0, (0, 0, 255), 1)

# 取得紅色方框的旋轉角度
angle = rect[2]
if angle < -45:
  angle = 90 + angle

# 以影像中心為旋轉軸心
(h, w) = pixel_data.shape[:2]
center = (w // 2, h // 2)

# 計算旋轉矩陣
M = cv2.getRotationMatrix2D(center, angle, 1.0)

# 旋轉圖片
rotated = cv2.warpAffine(contour_image, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)
img_final = cv2.warpAffine(pixel_data, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)

# 選轉紅色方框座標
pts = np.int0(cv2.transform(np.array([box]), M))[0]

# 計算旋轉後的紅色方框範圍
y_min = min(pts[0][0], pts[1][0], pts[2][0], pts[3][0])
y_max = max(pts[0][0], pts[1][0], pts[2][0], pts[3][0])
x_min = min(pts[0][1], pts[1][1], pts[2][1], pts[3][1])
x_max = max(pts[0][1], pts[1][1], pts[2][1], pts[3][1])

# 裁切影像
img_crop = rotated[x_min:x_max, y_min:y_max]
img_final = img_final[x_min:x_max, y_min:y_max]

# 呈現影像
plt.subplot(1, 2, 1)
plt.imshow(rotated, cmap=plt.cm.gray)
plt.title('Rotated Image')

plt.subplot(1, 2, 2)
plt.imshow(img_final, cmap=plt.cm.bone)
plt.title('Rotated img_final')
"""
plt.subplot(1, 2, 1)
plt.imshow(pixel_data, cmap=plt.cm.gray)
plt.title('original Image')

plt.subplot(1, 2, 2)
plt.imshow(threshold, cmap=plt.cm.bone)
plt.title('contour_image')
"""
plt.show()

# 保存處理後的DICOM文件
new_dicom_data = pydicom.Dataset()

# 設置DICOM屬性（根據需要調整這些值）
new_dicom_data.Rows = img_final.shape[0]
new_dicom_data.Columns = img_final.shape[1]
new_dicom_data.BitsStored =  original_bit_store
new_dicom_data.BitsAllocated = original_bit_allocated
new_dicom_data.SamplesPerPixel = original_samples_per_pixel
new_dicom_data.PhotometricInterpretation = original_photometric_interpretation
new_dicom_data.HighBit = original_high_bit

# 設置PixelRepresentation（0表示無符號整數）
new_dicom_data.PixelRepresentation = original_pixel_representation

# 設置Transfer Syntax UID（根據需要調整）
new_dicom_data.file_meta = pydicom.Dataset()
new_dicom_data.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

# 將像素數據轉換為字節數據
pixel_data_bytes = img_final.tobytes()
new_dicom_data.PixelData = pixel_data_bytes

# 設置字節序和VR類型
new_dicom_data.is_little_endian = True
new_dicom_data.is_implicit_VR = False  # 通常使用Explicit VR Little Endian

# 保存為DICOM文件
new_dicom_data.save_as("D:\\Python learning\\Project\\HandBoneXRay\\processed_image.dcm")


# 顯示處理後的影像
processed_data = pydicom.dcmread("D:\\Python learning\\Project\\HandBoneXRay\\processed_image.dcm", force=True)


processed_pixel_data = processed_data.pixel_array
plt.imshow(processed_pixel_data, cmap=plt.cm.bone)
plt.title('processed_pixel_data')
plt.show()






