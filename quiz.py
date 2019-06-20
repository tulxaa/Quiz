WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["Die Haupstadt von Deutschland ist ...?",
      "London", "Paris", "Berlin", "Tokio", 3]

q2 = ["Was ist 5 + 7?",
      "12", "10", "14", "8", 1]

q3 = ["Was ist der siebte Monat?",
      "April", "Mai", "Juni", "Juli", 4]

q4 = ["Welcher Planet ist der kleinste?",
      "Saturn", "Merkur", "Neptun", "Venus", 2]

q5 = ["Wo steht der Eiffelturm?",
      "Rom", "Pisa", "Paris", "Hamburg", 3]

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0) 

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1
                        

def game_over():
    global question, time_left
    message = "Ende. Du hast %s von 5 Fragen richtig" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("Ende der Fragen")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Du hast angeklickt:" + str(index))
            if index == question[5]:
                print("Das ist richtig!")
                correct_answer()
            else:
                game_over()
        index = index + 1

    

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)
        
