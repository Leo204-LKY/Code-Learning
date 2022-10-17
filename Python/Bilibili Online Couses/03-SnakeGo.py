# 编程步骤：
# 需求分析、程序设计、代码编写、测试与调试、实施与开发、维护优化
# -------------------------------------------------------------
# SnakeGo 贪吃蛇
# 本节用于体验 Python 的强大，后续会逐步学习语法等

# 模块调用
# 在命令行中使用 'pip install <板块名>' 来安装模块
# 之后(第8讲)会作详细介绍
import pygame
# pygame 是使用 Python 编写游戏的最佳解决方案
import time
# 用于在游戏中对事件追踪等
import random
# 用于食物的随机产生

# 关于 pygame
# - pygame.init()
# initiate (初始化) 的缩写，有了这行代码才能调用其他函数
# - Display.set_mode()
# 帮助进行游戏窗口的设置，包括大小、颜色等
# - Update()
# 刷新屏幕，每次完成操作后需要刷新以显示操作
# - Event_get()
# 用于追踪事件
# 对于贪吃蛇，蛇吃到食物、碰到墙壁都算是事件
# - Set_caption()
# 设置窗口的标题
# - Quit()
# 结束游戏

# 初始化游戏
pygame.init()

# 自定义颜色
white = (255, 255, 255)
yellow = (255, 255, 182)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 设置游戏界面
dis_width = 600                                           # 游戏窗口宽度
dis_height = 400                                          # 游戏窗口高度
dis = pygame.display.set_mode((dis_width, dis_height))    # 应用窗口宽度和高度设定
pygame.display.set_caption('SnakeGo!')                    # 设置窗口标题
font_style = pygame.font.SysFont("bahnschrift", 25)       # 设置游戏界面字体
score_font = pygame.font.SysFont("comicsansms", 35)       # 设置分数字体

# 其他设置
def your_score(score):                                    # 定义分数
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def message(msg, color):                                  # 定义信息内容
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6 , dis_height / 3])
# def = define(定义)，用于自定义函数(第7讲)

# 时钟设置
clock = pygame.time.Clock()

# 蛇的设置
snake_block = 10          # 设置蛇的宽度
snake_speed = 15          # 设置蛇的速度

# 绘制蛇的形状
#  - pygame.draw.rect(<1>, <2>, <3>)
# 用于绘制矩形，<1>：绘制在哪里(哪个窗口)；<2>：绘制线条的颜色；<3>：位置
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# 蛇的运动设置
def gameLoop():          # 构建一个循环函数用于蛇的捕食过程
    game_over = False    # 正常运行时为 True ，游戏结束或终止时为 False
    game_close = False

    # x1 和 y1 用于确定蛇的初始位置， x1_change 和 y1_change 用于记录蛇的位置变化
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    # 蛇的长度就是蛇头
    snake_list = []         # 列表用[](第4讲)
    length_of_snake = 1

    # 设置食物位置
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # round 代表四舍五入取整

    while not game_over:
        # 游戏终止时的界面显示，分数为蛇长度-1
        while game_close == True:
            dis.fill(blue)
            message("You Lose! Press C to play again or Q to quit.", red)
            your_score(length_of_snake - 1)
            pygame.display.update()
            # 检测 C 或 Q 键是否被按下
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if x1_change != snake_block: 
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        x1_change = -snake_block
                        y1_change = 0
                if x1_change != -snake_block:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        x1_change = snake_block
                        y1_change = 0
                if y1_change != snake_block:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        x1_change = 0
                        y1_change = -snake_block
                if y1_change != -snake_block:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        x1_change = 0
                        y1_change = snake_block
        
        # 撞墙判定
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # 蛇吃到食物，身体增加一节
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
    
        clock.tick(snake_speed)

    pygame.quit()

gameLoop()