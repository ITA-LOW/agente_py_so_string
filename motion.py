from gpiozero import Servo

# Configuração dos motores
servo_x = Servo(17)  # Motor eixo X (horizontal)
servo_y = Servo(27)  # Motor eixo Y (vertical)

# Ângulos suaves (valores entre -0.5 e 0.5 no gpiozero)
position_to_angle = {
    "up_left": (-0.3, 0.3), "up_middle": (0.0, 0.3), "up_right": (0.3, 0.3),
    "middle_left": (-0.3, 0.0), "center": (0.0, 0.0), "middle_right": (0.3, 0.0),
    "down_left": (-0.3, -0.3), "down_middle": (0.0, -0.3), "down_right": (0.3, -0.3)
}

def move_eye(position):
    """Move os servos suavemente para a posição correspondente"""
    if position in position_to_angle:
        angle_x, angle_y = position_to_angle[position]
        servo_x.value = angle_x
        servo_y.value = angle_y
        print(f"Movendo olho para {position} -> X: {angle_x}, Y: {angle_y}")
