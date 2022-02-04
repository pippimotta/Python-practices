import turtle
import pandas
from answer import Answer
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
# all_states = data.state.tolist()
# guessed_states = []
#
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name").title()
#
#     if answer_state == 'Exit':
#         missing_states = [state for state in all states if state not in guessed_states]
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv('states_to_learn.csv')
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)

answer = Answer()
game_is_on = True


#將csv變成dic，state作為position的key
state_list = data.state.tolist()
xcor_list = data.x.tolist()
ycor_list = data.y.tolist()
position_list = list(zip(xcor_list, ycor_list))
state_dic = dict(zip(state_list, position_list))

## 以上這段可以簡化為
# state_data = data[data.state == state]
# answer.goto(int(state_data.x), int(state_data.y))

answer_state = screen.textinput(title='Guess a State', prompt="What's another state's name").title()
score = 0
guessed_states = []
while game_is_on:
    for state in state_list:
        if answer_state not in guessed_states:
            if answer_state == state:
                pos = state_dic[answer_state]
                answer.show_answer(position=pos, state=answer_state)
                score += 1
                guessed_states.append(state)
        else:
            break
    answer_state = screen.textinput(title=f'{score}/50 States Correct', prompt="What's another state's name").title()
    if score == 50:
        game_is_on = False

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop() #類似於exitonclick

