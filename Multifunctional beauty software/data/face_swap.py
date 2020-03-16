from face_swap_h import *

FEATHER_AMOUNT = 23

Base_path = local_args.filename
cover_path = local_args.filename2
output_im = Switch_face(Base_path,cover_path)

cv2.imwrite(local_args.save_name, output_im)  # 换脸数据保存
im = cv2.imread(local_args.save_name)
cv2.imshow("img", im) 
cv2.waitKey(0)
cv2.destroyAllWindows()