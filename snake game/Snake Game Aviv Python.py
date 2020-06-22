import turtle # for graphics
import time # for delay
import random # for apple location
import winsound # for sound
def normal_game():
    snake_bodys = []

    delay = 0.1 # the delay
    score = 0
    high_score = 0
    
    # set up window
    wn = turtle.Screen()
    wn.title("Hoitash Snake game")
    wn.bgcolor("green")
    wn.setup(width=2000, height=1400)
    wn.tracer(0)

    # the mouth or first segment of the snake
    snake_mouth = turtle.Turtle()
    snake_mouth.speed(0)
    snake_mouth.shape("square")
    snake_mouth.color("black")
    snake_mouth.penup()
    snake_mouth.goto(-325,0)
    snake_mouth.direction = "stop"
 

    # the apple
    apple = turtle.Turtle()
    apple.speed(0)
    apple.shape("circle")
    apple.color("red")
    apple.penup()
    apple.goto(0,0)


    # each of the borders for where the game is played
    left_border = turtle.Turtle()
    left_border.speed(0)
    left_border.shape("square")
    left_border.color("black")
    left_border.penup()
    left_border.goto(-412,-43)
    left_border.turtlesize(stretch_wid=34.8,stretch_len=1)

    right_border = turtle.Turtle()
    right_border.speed(0)
    right_border.shape("square")
    right_border.color("black")
    right_border.penup()
    right_border.goto(408,-43)
    right_border.turtlesize(stretch_wid=34.8,stretch_len=1)

    up_border = turtle.Turtle()
    up_border.speed(0)
    up_border.shape("square")
    up_border.color("black")
    up_border.penup()
    up_border.goto(-2,316)
    up_border.turtlesize(stretch_wid=1,stretch_len=42)

    down_border = turtle.Turtle()
    down_border.speed(0)
    down_border.shape("square")
    down_border.color("black")
    down_border.penup()
    down_border.goto(-1,-382)
    down_border.turtlesize(stretch_wid=1,stretch_len=42)

    # setting up the scoreboard
    scoreboard = turtle.Turtle()
    scoreboard.speed(0)
    scoreboard.shape("square")
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0,330)
    scoreboard.write("Score: 0  High Score: 0", align="center",font=("Courier", 24, "normal"))

    # functions for movment
    def go_up():
        if snake_mouth.direction != "down":
            snake_mouth.direction = "up"

    def go_down():
        if snake_mouth.direction != "up":
            snake_mouth.direction = "down"

    def go_left():
        if snake_mouth.direction != "right":
            snake_mouth.direction = "left"

    def go_right():
        if snake_mouth.direction != "left":
            snake_mouth.direction = "right"

    def move():
        if snake_mouth.direction == "up":
            snake_y = snake_mouth.ycor()
            snake_mouth.sety(snake_y + 20)

        if snake_mouth.direction == "down":
            snake_y = snake_mouth.ycor()
            snake_mouth.sety(snake_y - 20)

        if snake_mouth.direction == "left":
            snake_x = snake_mouth.xcor()
            snake_mouth.setx(snake_x - 20)

        if snake_mouth.direction == "right":
            snake_x = snake_mouth.xcor()
            snake_mouth.setx(snake_x + 20)

    #keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "a")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()
        
        global new_body
        
        if snake_mouth.xcor()<-391 or snake_mouth.xcor()>391 or snake_mouth.ycor()<-361 or snake_mouth.ycor()>295: # if the mouth goes outside the border
            time.sleep(1)
            snake_mouth.goto(-325,0) # reset snake
            snake_mouth.direction = "stop"

            for body in snake_bodys: # clears bodys
                body.goto(1000, 1000)

            snake_bodys.clear() # clears the bodys list

            score = 0 # resets the score

            delay = 0.1 # resets the delay

            apple.goto(0,0) # resets apple

            #resets scoreboard
            scoreboard.goto(0, 350)
            scoreboard.clear()
            scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # plays sound
            winsound.PlaySound("bullet_whizzing.wav",winsound.SND_ASYNC)

        # if the snake mouth eats the apple
        if snake_mouth.distance(apple) <20:
            apple_x = random.randint(-388, 388)
            apple_y = random.randint(-361, 295)
            apple.goto(apple_x,apple_y) # place apple at random position


            
            new_body = turtle.Turtle() # adds a body
            new_body.speed(0)
            new_body.shape("square")
            new_body.color("blue")
            new_body.penup()
            snake_bodys.append(new_body)
            delay -= 0.001  # make the delay smaller


            
            

            score += 1  # add 1 to the score
            if score > high_score: # if the score is bigger than the high score, that score is the high score
                high_score = score
            # reset the scoreboard
            scoreboard.clear()
            scoreboard.goto(0, 350)
            scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            winsound.PlaySound("aud_chomp.wav",winsound.SND_ASYNC) #play chomp sound



        # make each of the bodys follow the mouth and eachother
        for body in range(len(snake_bodys)-1, 0, -1):
            body_x = snake_bodys[body-1].xcor()
            body_y = snake_bodys[body-1].ycor()
            snake_bodys[body].goto(body_x, body_y)

        if len(snake_bodys) > 0:
            snake_x = snake_mouth.xcor()
            snake_y = snake_mouth.ycor()
            snake_bodys[0].goto(snake_x,snake_y)

        move() # call the move function to make the snake move

        # if the mouth touches the body
        for body in snake_bodys:
            if body.distance(snake_mouth) < 10:
                time.sleep(1)
                snake_mouth.goto(-325,0)
                snake_mouth.direction = "stop"

                for body in snake_bodys:
                    body.goto(1000, 1000) # clear the bodys

                snake_bodys.clear() # clear the list bodys

                score = 0 # reset the score

                delay = 0.1 # reset the delay

                apple.goto(0,0) # reset the apple

                # reset the scoreboard
                scoreboard.clear()
                scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

                winsound.PlaySound("bullet_whizzing.wav",winsound.SND_ASYNC) #play the sound
        time.sleep(delay) # delay the game
    wn.mainloop()
normal_game()