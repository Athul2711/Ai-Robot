import pygame
import sys
import random
from pygame.locals import *
import time
import requests



ipp="192.168.184.53"

def sad(screen):
    eye_state = {'pupil_position_y': 0, 'lid_position_y': -110}

    def update():
        eye_state['pupil_position_y'] += 1
        eye_state['lid_position_y'] += 1

    def draw(progress):
        screen.fill((0, 0, 0))

        def sad_eye(eye_x, eye_y, lid_x, lid_y, eye_state):
            eye_state['pupil_position_y'] = min(max(eye_state['pupil_position_y'], 0), 27)
            eye_state['lid_position_y'] = min(max(eye_state['lid_position_y'], -200), -80)

            pupil_x = eye_x
            pupil_y = eye_y + eye_state['pupil_position_y']
            lid_y = eye_y + eye_state['lid_position_y']

            pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 65)  # White circle
            pygame.draw.circle(screen, (0, 0, 0), (lid_x, lid_y - 5), 90)  # Dark circle
            pygame.draw.circle(screen, (0, 0, 100), (pupil_x, pupil_y), 20)  # Pupil

        sad_eye(150, 150, 150, eye_state['lid_position_y'], eye_state)
        sad_eye(330, 150, 330, eye_state['lid_position_y'], eye_state)
        
##        font = pygame.font.Font(None, 24)
##        text = font.render("Sad", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 24)
        text = font.render(read_state_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 18)
        text = font.render(read_last_line_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 260))  # Adjust the position as needed
        




        
    return update, draw

def happy(screen):
    eye_state = {'pupil_position_y': 0, 'lid_position_y': -110}

    def update():
        eye_state['pupil_position_y'] += 1
        eye_state['lid_position_y'] += 1


    def draw(progress):
        screen.fill((0,0,0))

        def happy_eye(eye_x, eye_y, lid_x, lid_y, eye_state):
            eye_state['pupil_position_y'] = min(max(eye_state['pupil_position_y'], 0), 10)
            eye_state['lid_position_y'] = min(max(eye_state['lid_position_y'], -200), -90)

            pupil_x = eye_x
            pupil_y = eye_y - eye_state['pupil_position_y']
            lid_y = eye_y - eye_state['lid_position_y']

            pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 65)  # White circle
            pygame.draw.circle(screen, (0, 0, 100), (pupil_x, pupil_y), 20)
            pygame.draw.circle(screen, (0, 0, 0), (lid_x, lid_y - 5), 90)  # Dark circle
              # Pupil

        happy_eye(150, 150, 150, eye_state['lid_position_y'], eye_state)
        happy_eye(330, 150, 330, eye_state['lid_position_y'], eye_state)
##        font = pygame.font.Font(None, 24)
##        text = font.render("Happy", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed
##
##        
        font = pygame.font.Font(None, 24)
        text = font.render(read_state_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 18)
        text = font.render(read_last_line_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 260))  # Adjust the position as needed
        

    return update, draw

def angry(screen):
    eye_states = {'triangle_coords1': [(85, 90), (215, 20), (250, 140)],
                  'triangle_coords2': [(270, 90), (400, 50), (250, 140)]}
    new_triangle_coords1 = [(85, 100), (215, 50), (250, 215)]
    new_triangle_coords2 = [(270,50), (430, 50), (260, 205)]
    animation_duration = 1000  # Adjusted for faster movement

    def update():
        pass

    def draw(progress):
        screen.fill((0,0,0))

        def angry_eye(eye_x, eye_y, triangle_coords1, triangle_coords2):
            interpolated_coords1 = [
                (
                    int(start[0] + (end[0] - start[0]) * progress),
                    int(start[1] + (end[1] - start[1]) * progress),
                )
                for start, end in zip(triangle_coords1, new_triangle_coords1)
            ]
            interpolated_coords2 = [
                (
                    int(start[0] + (end[0] - start[0]) * progress),
                    int(start[1] + (end[1] - start[1]) * progress),
                )
                for start, end in zip(triangle_coords2, new_triangle_coords2)
            ]

            pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 65)
            pygame.draw.circle(screen, (0, 0, 100), (eye_x, 160), 20)

            pygame.draw.polygon(screen, (0, 0, 0), interpolated_coords2)
            pygame.draw.polygon(screen, (0,0, 0), interpolated_coords1)

        angry_eye(150, 150, eye_states['triangle_coords1'], eye_states['triangle_coords2'])
        angry_eye(330, 150, eye_states['triangle_coords1'], eye_states['triangle_coords2'])
##        font = pygame.font.Font(None, 24)
##        text = font.render("Angry", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed
##        
        font = pygame.font.Font(None, 24)
        text = font.render(read_state_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 18)
        text = font.render(read_last_line_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 260))  # Adjust the position as needed
        

    return update, draw, animation_duration


def random_blink(screen):
    rect1_x, rect1_y = 0, 215
    rect2_x, rect2_y = 0, 0
    rect1_direction = 1

    def update():
        nonlocal rect1_y, rect2_y, rect1_direction

        # Randomize the duration of the blink
        rand = random.randint(2, 6)

        # Set initial positions and directions
        rect1_y = 215
        rect2_y = 0
        rect1_direction = -1
        rect2_direction = 1

        # Loop until the first rectangle completes the blink
        while rect1_y <= 215:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            # Update positions of both rectangles
            rect1_y += 2 * rect1_direction
            rect2_y += 2 * rect2_direction

            # Control the speed of the animation
            pygame.time.Clock().tick(60)

            # Change direction when reaching certain positions
            if rect1_y <= 150:
                rect1_direction = 1
            if rect2_y >= 65:
                rect2_direction = -1

            # Draw the current state of the animation
            draw(None)

        # Wait for a random time before repeating the animation
        pygame.time.delay(rand * 1000)

    def draw(progress):
        # Draw circles and rectangles after blink animation
        screen.fill((0, 0, 0))

        # Draw circles
        pygame.draw.circle(screen, (255, 255, 255), [150, 150], 65, 0)
        pygame.draw.circle(screen, (0, 0, 255), [150, 150], 20, 0)
        pygame.draw.circle(screen, (255, 255, 255), [330, 150], 65, 0)
        pygame.draw.circle(screen, (0, 0, 255), [330, 150], 20, 0)

        # Draw rectangles
        pygame.draw.rect(screen, (0, 0, 0), [rect1_x, max(rect1_y, 150), 480, 85], 0)
        pygame.draw.rect(screen, (0, 0, 0), [rect1_x, min(rect2_y, 150), 480, 85], 0)
##        font = pygame.font.Font(None, 24)
##        text = font.render("Default", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed
##        
        font = pygame.font.Font(None, 24)
        text = font.render(read_state_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 18)
        text = font.render(read_last_line_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 260))  # Adjust the position as needed
        

        # Update display
        pygame.display.flip()
##        font = pygame.font.Font(None, 24)
##        text = font.render("Default", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed
##        
    return update, draw

def fear(screen):
    eye_states = {'triangle_coords1': [(85, 90), (215, 20), (250, 140)],
                  'triangle_coords2': [(270, 90), (400, 50), (250, 140)]}
    new_triangle_coords1 = [(85, 70), (215, 150), (250, 140)]
    new_triangle_coords2 = [(270,50), (430, 50), (260, 205)]
    animation_duration = 1000

    def update():
        pass

    def draw(progress):
        screen.fill((0,0,0))

        def fear_eye(eye_x, eye_y, triangle_coords1, triangle_coords2):
            interpolated_coords1 = [
                (
                    int(start[0] + (end[0] - start[0]) * progress),
                    int(start[1] + (end[1] - start[1]) * progress),
                )
                for start, end in zip(triangle_coords1, new_triangle_coords1)
            ]

            pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 65)
            pygame.draw.circle(screen, (0, 0, 100), (eye_x, 160), 20)

            pygame.draw.polygon(screen, (0, 0, 0), interpolated_coords1)
            pygame.draw.polygon(screen, (0,0, 0), triangle_coords2)

        fear_eye(150, 150, eye_states['triangle_coords1'], eye_states['triangle_coords2'])
        fear_eye(330, 150, eye_states['triangle_coords1'], eye_states['triangle_coords2'])
##        font = pygame.font.Font(None, 24)
##        text = font.render("Fear", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed
##        
        font = pygame.font.Font(None, 24)
        text = font.render(read_state_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 18)
        text = font.render(read_last_line_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 260))  # Adjust the position as needed
        

    return update, draw, animation_duration

def surprised(screen):
    eye_states = {'triangle_coords1': [(85, 90), (215, 20), (250, 140)],
                  'triangle_coords2': [(270, 90), (400, 50), (250, 140)]}
    new_triangle_coords1 = [(85, 70), (215, 70), (250, 180)]
    new_triangle_coords2 = [(270,70), (430, 70), (260, 185)]
    animation_duration = 1000

    def update():
        pass

    def draw(progress):
        screen.fill((0,0,0))

        def surprised_eye(eye_x, eye_y, triangle_coords1, triangle_coords2):
            interpolated_coords1 = [
                (
                    int(start[0] + (end[0] - start[0]) * progress),
                    int(start[1] + (end[1] - start[1]) * progress),
                )
                for start, end in zip(triangle_coords1, new_triangle_coords1)
            ]
            interpolated_coords2 = [
                (
                    int(start[0] + (end[0] - start[0]) * progress),
                    int(start[1] + (end[1] - start[1]) * progress),
                )
                for start, end in zip(triangle_coords2, new_triangle_coords2)
            ]

            pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 65)
            pygame.draw.circle(screen, (0, 0, 100), (eye_x, 160), 20)

            pygame.draw.polygon(screen, (0, 0, 0), interpolated_coords1)
            pygame.draw.polygon(screen, (0,0, 0), interpolated_coords2)

        surprised_eye(150, 150, eye_states['triangle_coords1'], eye_states['triangle_coords2'])
        surprised_eye(330, 150, eye_states['triangle_coords1'], eye_states['triangle_coords2'])
##        font = pygame.font.Font(None, 24)
##        text = font.render("Surprised", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed
##        
        font = pygame.font.Font(None, 24)
        text = font.render(read_state_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 18)
        text = font.render(read_last_line_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 260))  # Adjust the position as needed
        

    return update, draw, animation_duration

def confused(screen):
    eye_states = {'eye_radius': [65, 55], 'pupil_position_x': 0, 'pupil_position_y': 0}

    def update():
        eye_states['pupil_position_x'] += random.randint(-2, 2)
        eye_states['pupil_position_y'] += random.randint(-2, 2)

    def draw(progress):
        screen.fill((0, 0, 0))

        def confused_eye(eye_x, eye_y, eye_radius, pupil_position_x, pupil_position_y):
            pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), eye_radius)  # White circle
            pygame.draw.circle(screen, (0, 0, 0), (eye_x + pupil_position_x, eye_y + pupil_position_y), 20)  # Pupil

        # Left eye with a smaller size
        confused_eye(150, 150, eye_states['eye_radius'][0], eye_states['pupil_position_x'], eye_states['pupil_position_y'])
        # Right eye with a regular size
        confused_eye(330, 150, eye_states['eye_radius'][1], 0, 0)
##        font = pygame.font.Font(None, 24)
##        text = font.render("Confused", True, (255, 255, 255))
##        screen.blit(text, (380, 20))  # Adjust the position as needed
##        
        font = pygame.font.Font(None, 24)
        text = font.render(read_state_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 20))  # Adjust the position as needed


        font = pygame.font.Font(None, 18)
        text = font.render(read_last_line_from_file(), True, (255, 255, 255))
        screen.blit(text, (20, 260))  # Adjust the position as needed
        

    return update, draw

def sleep(screen):
    eye_state = {'lid_position_y': -110, 'blink_duration': random.randint(200, 500), 'blink_interval': random.randint(3000, 6000),
                 'last_blink_time': pygame.time.get_ticks(), 'z_positions': [100, 100]}

    def update():
        current_time = pygame.time.get_ticks()
##        if current_time - eye_state['last_blink_time'] >= eye_state['blink_interval']:
##            eye_state['last_blink_time'] = current_time
##            eye_state['lid_position_y'] = 0  # Open eyes
##            eye_state['blink_duration'] = random.randint(200, 500)  # Randomize blink duration
##            eye_state['blink_interval'] = random.randint(3000, 6000)  # Randomize blink interval
##            pygame.time.set_timer(pygame.USEREVENT, eye_state['blink_duration'])  # Schedule close eyes event

        # Update Z's positions
        for i in range(2):
            eye_state['z_positions'][i] -= 1  # Move Z's upwards
            if eye_state['z_positions'][i] < 50:  # Reset position if out of bounds
                eye_state['z_positions'][i] = 150

    def close_eyes():
        eye_state['lid_position_y'] = -110  # Close eyes
        pygame.time.set_timer(pygame.USEREVENT, 0)  # Disable event

    def draw(progress):
        screen.fill((0, 0, 0))

        def sleep_eye(eye_x, eye_y, lid_y):
            pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 65)  # White circle
            pygame.draw.circle(screen, (0, 0, 0), (eye_x, eye_y + lid_y), 180)  # Dark circle

            # Draw sleepy pupil
            #pygame.draw.circle(screen, (0, 0, 100), (eye_x, eye_y + 20), 15)  # Brownish pupil
        # Draw eyes
        sleep_eye(150, 150, eye_state['lid_position_y']-25)
        sleep_eye(330, 150, eye_state['lid_position_y']-25)

        # Draw smaller Z's
        font = pygame.font.Font(None, 30)
        z_surface = font.render("Z", True, (255, 255, 255))
        screen.blit(z_surface, (170, eye_state['z_positions'][0]))
        screen.blit(z_surface, (340, eye_state['z_positions'][1]))

        # Draw stars
        star_positions = [(50, 50), (100, 100), (150, 150), (200, 200), (250, 250),
                          (300, 100), (350, 150), (400, 200), (450, 250),
                          (50, 200), (100, 250), (150, 300), (200, 100),
                          (250, 150), (300, 200), (350, 250), (400, 100),
                          (450, 150), (500, 200), (550, 250)]

        for pos in star_positions:
            pygame.draw.circle(screen, (255, 255, 255), pos, 2)  # Draw stars as circles

        # Draw moon
        pygame.draw.circle(screen, (255, 255, 255), (420, 60), 40)  # Large circle
        pygame.draw.circle(screen, (0, 0, 0), (450, 50), 35)  # Smaller circle to create crescent effect

    pygame.time.set_timer(pygame.USEREVENT, eye_state['blink_duration'])  # Start with a blink

    return update, draw


def http_get_string(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("HTTP GET request failed with status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("HTTP GET request failed:", e)
        return None



def read_emotion_from_file():

    url = "http://"+ipp+"/shared_data.txt"  # Replace with the URL you want to request
    string_from_url = http_get_string(url)
    return string_from_url

def read_state_from_file():
    url = "http://"+ipp+"/status.txt"  # Replace with the URL you want to request
    string_from_url = http_get_string(url)
    return string_from_url



def read_last_line_from_file():
    return ""
    url = "http://192.168.82.53/conv.txt"  # Replace with the URL you want to request
    string_from_url = http_get_string(url)
    
    lines = string_from_url.split('\n')
    for line in reversed(lines):
        stripped_line = line.strip()
        if stripped_line:  # Check if the line is not empty
            return stripped_line
    return ""





def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 320))
    print("start")
    font = pygame.font.Font(None, 24)  # Choose a font and font size for the subtitle

    update_func = None
    draw_func = None
    animation_duration = None
    animation_start_time = None
    previous_emotion = None

    while True:
        emotion = read_emotion_from_file()

        

##
##        
##        rect1_x, rect1_y = 0, 215
##        rect2_x,rect2_y = 0,0
##    
##        rect1_direction = 1
        emotion = read_emotion_from_file()
        if emotion != previous_emotion:  # Check if the emotion has changed
            previous_emotion = emotion  # Update the previous emotion
            
            if 'sad' in emotion:
                update_func, draw_func = sad(screen)
                animation_duration = None
            elif 'happy' in emotion:
                update_func, draw_func = happy(screen)
                animation_duration = None
            elif 'angry' in emotion:
                update_func, draw_func, animation_duration = angry(screen)
                animation_start_time = pygame.time.get_ticks()
            elif 'fear' in emotion:
                update_func, draw_func, animation_duration = fear(screen)
                animation_start_time = pygame.time.get_ticks()
            elif 'surprised' in emotion:
                update_func, draw_func, animation_duration = surprised(screen)
                animation_start_time = pygame.time.get_ticks()
            elif 'confused' in emotion:
                update_func, draw_func = confused(screen)
                animation_duration = None
            elif 'sleep' in emotion:
                update_func, draw_func = sleep(screen)
                animation_duration = None
            else:
                update_func, draw_func = random_blink(screen)
                animation_duration = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    update_func, draw_func = sad(screen)
                    animation_duration = None
                elif event.key == pygame.K_h:
                    update_func, draw_func = happy(screen)
                    animation_duration = None
                elif event.key == pygame.K_a:
                    update_func, draw_func, animation_duration = angry(screen)
                    animation_start_time = pygame.time.get_ticks()
                elif event.key == pygame.K_r:
                    update_func, draw_func = random_blink(screen)
                    animation_duration = None
                elif event.key == pygame.K_f:
                    update_func, draw_func, animation_duration = fear(screen)
                    animation_start_time = pygame.time.get_ticks()
                elif event.key == pygame.K_p:
                    update_func, draw_func, animation_duration = surprised(screen)
                    animation_start_time = pygame.time.get_ticks()
                elif event.key == pygame.K_c:
                    update_func, draw_func = confused(screen)
                    animation_duration = None
                elif event.key == pygame.K_l:
                    update_func, draw_func = sleep(screen)
                    animation_duration = None

        if update_func is not None and draw_func is not None:
            update_func()
            if animation_duration is not None:
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - animation_start_time
                progress = elapsed_time / animation_duration
                if progress >= 1.0:
                    progress = 1.0
            else:
                progress = 0
            draw_func(progress)

        pygame.display.flip()
        pygame.time.delay(50)

if __name__ == "__main__":
    main()
