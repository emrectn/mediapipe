import cv2
import mediapipe as mp

def hands_detection(cap):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    IMAGE_FILES = []
    with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
        for idx, file in enumerate(IMAGE_FILES):
            image = cv2.flip(cv2.imread(file), 1)
            # Convert the BGR image to RGB before processing.
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            if results.multi_hand_landmarks:
                for i in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, i, hands.HAND_CONNECTIONS)

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

        cv2.imshow("Hands Detection", image)
        if cv2.waitkey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()

def pose_detection(cap):
    pass

def holistic_detection(cap):
    pass

if __name__ == '__main__':  # or def main()
    cap = cv2.VideoCapture(0)
    while True:
        choise = input()
        if choise == '1':
            hands_detection(cap)
        elif choise == '2':
            pose_detection(cap)
        elif choise == '3':
            holistic_detection(cap)
        else:
            break

    cv2.destroyAllWindows()
    cap.release()
