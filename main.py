import cv2
import time
from agent import Agent
from vision import detect_face_position

def main():
    agent = Agent()
    
    plan_library = [
        ('adjust_vision', {'context': {'position': pos}, 'plan': [pos]}) for pos in [
            "up_left", "up_middle", "up_right",
            "middle_left", "center", "middle_right",
            "down_left", "down_middle", "down_right"
        ]
    ]
    
    agent.set_plan_library(plan_library)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Erro ao ler o frame.")
            break
        
        position = detect_face_position(frame)
        
        if position:
            agent.add_beliefs({'position': position})
            agent.add_desires("adjust_vision")
            goal = agent.get_desires()
            agent.update_intention(goal)
            agent.execute_intention()  # Agora já chama a movimentação
        
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        time.sleep(0.1)
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
