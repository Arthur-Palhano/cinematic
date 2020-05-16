import pygame, math, matplotlib.pyplot as plt

width = 600
height = 600
screen = pygame.display.set_mode((900, height))
pygame.display.set_caption("Cinematics")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")
bricks = pygame.image.load("bricks.png")

clock = pygame.time.Clock()

font_color = (7, 0, 161)
pygame.font.init()
font_header = pygame.font.SysFont("Arial", 30)
font_index = pygame.font.SysFont("Arial", 20)
header = font_header.render("Choose a vehicle:", True, font_color)
car_index = font_index.render("Car [1]", True, font_color)
car_speed = font_index.render("60km/h", True, font_color)
motor_index = font_index.render("Motorcycle [2]", True, font_color)
motor_speed = font_index.render("40km/h", True, font_color)
bike_index = font_index.render("Bike [3]", True, font_color)
bike_speed = font_index.render("20km/h", True, font_color)
person_index = font_index.render("Person [4]", True, font_color)
person_speed = font_index.render("6km/h", True, font_color)
credit = font_index.render("Created by Nikrsz", True, font_color)

class vehicle:
    def __init__(self, image1, image2, speed):
        self.image1 = pygame.image.load(image1)
        self.image2 = pygame.image.load(image2)
        self.width = self.image1.get_width()
        self.height = self.image1.get_height()
        self.x = (width - self.width)/2
        self.y = (height - self.height - 63)
        self.speed_init = speed
        self.speed = 0
        self.choice = 0
    def run(self):
        if self.choice == 0:
            screen.blit(self.image1, (self.x, self.y))
        else:
            screen.blit(self.image2, (self.x, self.y))

car = vehicle("car1.png", "car2.png", 9)
motor = vehicle("motor1.png", "motor2.png", 6)
bike = vehicle("bike1.png", "bike2.png", 3)
person = vehicle("person1.png", "person2.png", 0.9)
vehicles = [car, motor, bike, person]
choice = 0

running = True
while running:

    screen.blit(background, (0, 0))
    screen.blit(bricks, (600, 0))

    screen.blit(header, (626, 33))

    screen.blit(car.image1, (626, 133))
    screen.blit(car_index, (636 + car.width, 133))
    screen.blit(car_speed, (636 + car.width, 163))

    screen.blit(motor.image1, (626, 233))
    screen.blit(motor_index, (636 + motor.width, 233))
    screen.blit(motor_speed, (636 + motor.width, 263))

    screen.blit(bike.image1, (626, 333))
    screen.blit(bike_index, (636 + bike.width, 333))
    screen.blit(bike_speed, (636 + bike.width, 363))

    screen.blit(person.image1, (626, 433))
    screen.blit(person_index, (636 + person.width, 433))
    screen.blit(person_speed, (636 + person.width, 463))

    screen.blit(credit, (730, 570))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for auto in vehicles:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    auto.speed = auto.speed_init
                    auto.choice = 0
                if event.key == pygame.K_LEFT:
                    auto.speed = -auto.speed_init
                    auto.choice = 1
                if event.key == pygame.K_1:
                    choice = 0
                if event.key == pygame.K_2:
                    choice = 1
                if event.key == pygame.K_3:
                    choice = 2
                if event.key == pygame.K_4:
                    choice = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    auto.speed = 0
                if event.key == pygame.K_LEFT:
                    auto.speed = 0

    for auto in vehicles:
        auto.x += auto.speed
        if auto.x >= (width - auto.width) or auto.x <= 0:
            auto.speed = 0

    for i in range(0, 5):
        if choice == i:
            vehicles[i].run()

    clock.tick(60)
    pygame.display.update()
