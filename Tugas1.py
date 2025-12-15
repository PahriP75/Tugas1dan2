import cv2
import numpy as np

current_mode = '0' 
buttons = []       

def draw_buttons(frame):
    """Fungsi untuk menggambar tombol pada frame"""
    global buttons
    buttons = []
    btn_defs = [
        ("Normal", '0'),
        ("Avg Blur", '1'),
        ("Gaussian", '2'),
        ("Sharpen", '3')
    ]
    
    height, width, _ = frame.shape
    

    btn_height = 40
    btn_width = 100
    margin = 20
    start_x = 20
    start_y = height - 60 
    
    for i, (label, mode) in enumerate(btn_defs):
        x1 = start_x + (i * (btn_width + margin))
        y1 = start_y
        x2 = x1 + btn_width
        y2 = y1 + btn_height
        
        buttons.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'mode': mode})
        
        if current_mode == mode:
            color = (0, 255, 0) 
        else:
            color = (100, 100, 100) 
        

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

        text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
        text_x = x1 + (btn_width - text_size[0]) // 2
        text_y = y1 + (btn_height + text_size[1]) // 2
        
        cv2.putText(frame, label, (text_x, text_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

def mouse_callback(event, x, y, flags, param):
    """Fungsi yang dipanggil saat mouse diklik"""
    global current_mode
    
    if event == cv2.EVENT_LBUTTONDOWN: 
        for btn in buttons:
            if btn['x1'] < x < btn['x2'] and btn['y1'] < y < btn['y2']:
                current_mode = btn['mode']
                print(f"Mode changed to: {current_mode}")

def main():
    global current_mode
    
    cap = cv2.VideoCapture(0)

    window_name = "Tugas 1 - GUI Buttons"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)


    kernel_sharpen = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    k_size = 15
    gauss_1d = cv2.getGaussianKernel(k_size, 0)
    kernel_gaussian_2d = gauss_1d @ gauss_1d.T 

    while True:
        ret, frame = cap.read()
        if not ret: break
        

        filtered_frame = frame.copy()
        
        if current_mode == '1': # Average
            filtered_frame = cv2.blur(frame, (9, 9))
        elif current_mode == '2': # Gaussian
            filtered_frame = cv2.filter2D(frame, -1, kernel_gaussian_2d)
        elif current_mode == '3': # Sharpen
            filtered_frame = cv2.filter2D(frame, -1, kernel_sharpen)
            

        draw_buttons(filtered_frame)
        

        cv2.putText(filtered_frame, f"Active Mode: {current_mode}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow(window_name, filtered_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): break
        elif key in [ord('0'), ord('1'), ord('2'), ord('3')]:
            current_mode = chr(key)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()