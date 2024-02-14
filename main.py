from turtle import * # ПОДКЛЮЧАЕМ БИБЛТОТЕКУ
exitonclick() # СОХРАНЯЕМ РИСУНОК НА ЭКРАНЕ ПО ЗАВЕРШЕНИЮ ОТРИСОВКИ

'''
ЦВЕТА:
https://htmlcolorcodes.com/

Примеры цветов:
'#FF0000' - красный
'#FFFF00' - желтый
'#00FF00' - зеленый
'#0000FF' - синий
'''
# функция для отрисовки прямоугольников
def draw_rect(start_x, start_y, side_width, side_height, line_color = '#000000', line_width = 1, fill_color = None):
    penup()
    goto(start_x, start_y)
    pendown()
    width(1)
    if fill_color:
        color(fill_color)
        begin_fill()
        for i in range(2):
            forward(side_width)
            left(90)
            forward(side_height)
            left(90)
        end_fill()
    if line_color:
        width(line_width)
        color(line_color)
        for i in range(2):
            forward(side_width)
            left(90)
            forward(side_height)
            left(90)

# функция для отрисовки окружностей
def draw_circle(center_x = 0, center_y = 0, radius = 100, line_color = '#000000', line_width = 1, fill_color = None):
    penup()
    goto(center_x, center_y - radius)
    pendown()
    width(1)
    if fill_color:
        color(fill_color)
        begin_fill()
        circle(radius)
        end_fill()
    if line_color:
        width(line_width)
        color(line_color)
        circle(radius)

# функция для отрисовки правильного многоугольника (все углы и стороны равны)
def regular_polygon(start_x = 0, start_y = 0, sides_number = 3, side_seze = 100, line_color = '#000000', line_width = 1, fill_color = None):
    penup()
    goto(start_x, start_y)
    pendown()
    turn_angle = 360 / sides_number
    width(1)
    if fill_color:
        color(fill_color)
        begin_fill()
        for i in range(int(sides_number)):
            forward(side_seze)
            left(turn_angle)
        end_fill()
    if line_color:
        width(line_width)
        color(line_color)
        for i in range(int(sides_number)):
            forward(side_seze)
            left(turn_angle)

# функция для отрисовки многоугольника по набору точек points = ((x1,y1), (x2,y2), (x3,y3)...)
def draw_polygon(points, line_color = '#000000', line_width = 1, fill_color = None):
    penup()
    goto(points[0][0], points[0][1])
    pendown()
    width(1)
    if fill_color:
        color(fill_color)
        begin_fill()
        for i in range(1, len(points)):
            goto(points[i][0], points[i][1])
        end_fill()
    if line_color:
        width(line_width)
        color(line_color)
        for i in range(1, len(points)):
            goto(points[i][0], points[i][1])

# функция для отрисовки текста
def draw_text(text, start_x, start_y, fill_color = '#000000', font_size = 12, is_bold = False, is_italic = False):
    penup()
    goto(start_x, start_y)
    pendown()
    color(fill_color)
    font_style = 'normal'
    if is_bold and is_italic : font_style = 'bold italic'
    if is_bold : font_style = 'bold'
    if is_italic : font_style = 'italic'
    write(text, font=("Arial", font_size, font_style))

################################################################




################################################################
# ПРИМЕР ИСПОЛЬЗОВАНИЯ
################################################################

speed(10)

draw_text("Hello!", start_x = -200, start_y = 180, fill_color = '#00ff00', font_size = 24, is_bold = True, is_italic = False)
draw_rect(start_x = -150, start_y = -150, side_width = 50, side_height = 25, line_color = '#ff0000', line_width = 5, fill_color = '#ffff00')
draw_circle(center_x = 0, center_y = 0, radius = 50, line_color = None, line_width = 5, fill_color = '#0000ff')
regular_polygon(start_x = 150, start_y = 20, sides_number = 5, side_seze = 50, line_color = '#000000', line_width = 5, fill_color = '#0000ff')
points = ((20,-20), (120,-70), (100,-50), (50,-120), (20,-20))
draw_polygon(points, line_color = '#ff0000', line_width = 5, fill_color = '#ffff00')
draw_text("Great!", start_x = 0, start_y = 0, fill_color = '#000000', font_size = 12, is_bold = False, is_italic = False)

hideturtle()
