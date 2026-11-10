class Head:
    def __init__(self,face,eyes,mouth,hair,nose):
        self.face = face
        self.eyes = eyes
        self.mouth = mouth
        self.hair = hair
        self.nose = nose

    def __str__(self):
        return (f" cabeza {self.face}, ojos {self.eyes}, boca {self.mouth},cabello {self.hair} y nariz {self.nose}")
class Body:
    def __init__(self,head,left_hand, right_hand, left_arm, right_arm, left_feet, right_feet):
        self.head = head
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_feet = right_feet
        self.left_feet = left_feet
        # self.left_leg_1 = left_leg_1
        # self.right_leg_1 = right_leg_1
    
    def __str__ (self):
        return (f"{self.head}, una mano izquierda con {self.left_hand}, una mano derecha con {self.right_hand}, un brazo izquierdo con una mano con {self.left_arm}, un brazo derecho con una mano con {self.right_hand}, pie izquierdo con {self.left_feet}, pie derecho con {self.right_feet}")

class Arm:
    def __init__(self,hand):
        self.hand = hand

    def __str__(self):
        return (f"{self.hand}")

class Hand:
    def __init__(self,fingers):
        self.fingers = fingers

    def __str__(self):
        return (f"{self.fingers} dedos ")

# class Leg:
#     def __init__(self,foot):
#         self.foot = foot
        
#     def __str__(self):
#         return (f"Esta pierna tiene {self.foot} ")
class Feet:
    def __init__(self,foot_fingers):
        self.foot_fingers = foot_fingers

    def __str__(self):
        return (f"{self.foot_fingers} dedos ")

class Human:
    def __init__(self,body):
        self.body = body

    def __str__(self):
        return (f"Este cuerpo tiene {self.body}")

head_1 = Head("circular","azules","grande","largo","fina")
left_hand_1 = Hand(5)
right_hand_1 = Hand(4)
left_arm_1 = Arm(left_hand_1)
right_arm_1 = Arm(right_hand_1)
left_feet_1 = Feet(5)
right_feet_1 = Feet(3)
# left_leg_1 = Leg(left_feet_1)
# right_leg_1 = Leg(right_feet_1)

body_1 = Body(head_1,left_hand_1,right_hand_1,left_arm_1,right_arm_1,left_feet_1,right_feet_1)
human = Human(body_1)

print(human)
