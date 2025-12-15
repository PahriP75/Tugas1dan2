import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    
    colors_config = [
        {
            "name": "Merah",
            "lower": np.array([0, 120, 70]), 
            "upper": np.array([10, 255, 255]),
            "bbox_color": (0, 0, 255) # Merah di BGR
        },
        {
            "name": "Hijau",
            "lower": np.array([40, 70, 70]),
            "upper": np.array([80, 255, 255]),
            "bbox_color": (0, 255, 0) # Hijau di BGR
        },
        {
            "name": "Biru",
            "lower": np.array([100, 150, 0]),
            "upper": np.array([140, 255, 255]),
            "bbox_color": (255, 0, 0) # Biru di BGR
        },
        {
            "name": "Kuning",
            "lower": np.array([20, 100, 100]),
            "upper": np.array([30, 255, 255]),
            "bbox_color": (0, 255, 255) # Kuning di BGR
        }
    ]


    kernel = np.ones((5, 5), np.uint8)

    print("Program Berjalan: Deteksi 4 Warna (Merah, Hijau, Biru, Kuning)")
    print("Tekan 'q' untuk keluar.")

    while True:
        ret, frame = cap.read()
        if not ret: break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        output_frame = frame.copy()


        for color in colors_config:

            mask = cv2.inRange(hsv_frame, color["lower"], color["upper"])
            
     
            if color["name"] == "Merah":
                lower_red2 = np.array([170, 120, 70])
                upper_red2 = np.array([180, 255, 255])
                mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
                mask = mask + mask2 


            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


            if contours:
        
                largest = max(contours, key=cv2.contourArea)
                area = cv2.contourArea(largest)

        
                if area > 500:
                    x, y, w, h = cv2.boundingRect(largest)
                    
              
                    cv2.rectangle(output_frame, (x, y), (x + w, y + h), color["bbox_color"], 2)
                    
   
                    label = color["name"]
                    cv2.putText(output_frame, label, (x, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color["bbox_color"], 2)


        cv2.imshow("Multi-Color Detection", output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()