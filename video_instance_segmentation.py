import cv2
from yoloseg import YOLOSeg

# Initialize video
cap = cv2.VideoCapture(r"C:\Users\K3000\Videos\AI test videos\test (2).mp4")

model_path = "model/yolov12.onnx"
yoloseg = YOLOSeg(model_path, conf_thres=0.5, iou_thres=0.3)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
frame_countdown = 3
while cap.isOpened():

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

    # Read frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Update object localizer
    boxes, scores, class_ids, masks = yoloseg(frame)

    combined_img = yoloseg.draw_masks(frame, mask_alpha=0.4)
    # out.write(combined_img)
    cv2.imshow("Detected Objects", combined_img)

cap.release()