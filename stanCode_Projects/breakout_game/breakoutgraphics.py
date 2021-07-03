"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10      # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7   # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'slate gray'
        self.paddle.color = 'slate gray'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'steel blue'
        self.ball.color = 'steel blue'
        self.window.add(self.ball, x=((window_width-(ball_radius*2))/2), y=((window_height-(ball_radius*2))/2))
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.shift_paddle)
        self.start_game = True

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i % 10 <= 1:
                    self.brick.fill_color = 'black'
                    self.brick.color = 'black'
                elif i % 10 <= 3:
                    self.brick.fill_color = 'dark grey'
                    self.brick.color = 'dark grey'
                elif i % 10 <= 5:
                    self.brick.fill_color = 'dim gray'
                    self.brick.color = 'dim gray'
                elif i % 10 <= 7:
                    self.brick.fill_color = 'grey'
                    self.brick.color = 'grey'
                elif i % 10 <= 9:
                    self.brick.fill_color = 'light gray'
                    self.brick.color = 'light gray'
                self.window.add(self.brick, x=(brick_width+brick_spacing)*j, y=(brick_offset + (brick_height +
                                                                                                brick_spacing)*i))

        self.brick_offset = brick_offset
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_spacing = brick_spacing
        self.window_width = window_width
        self.window_height = window_height
        self.ball_radius = ball_radius

        self.obj = None                                          # record the object hit by the ball
        self.fall_off = False                                    # if the ball fall to bottom

        self.num_removed_brick = 0                               # to record the number of removed bricks
        self.score = 0                                           # to record score

        self.score_label = GLabel('Scores: ' + str(self.score))  # score board
        self.score_label.font = 'Verdana-20-bold-italic'

        self.switch_increase_velocity = True                     # for determining whether to accelerate or not
        self.times_accelerating = 0                              # to record how many times ball have accelerated

    def shift_paddle(self, mouse):
        """
        The paddle was shifted as users move mouse.
        :param mouse:
        :return:
        """
        if self.paddle.width/2 <= mouse.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width/2

    def handle_click(self, m):
        """
        A switch to record whether game was started.
        """
        if self.start_game:
            self.start_game = False

    def get_start_signal(self):
        """
        getter of signal of start game.
        :return: a boolean result
        """
        return self.start_game

    def set_ball_velocity(self):
        """
        To set an initial velocity of ball.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx *= -1
        self.__dy = INITIAL_Y_SPEED

    def reborn_velocity(self):
        """
        To set an random horizontal velocity and direction of ball
        """
        self.__dx = random.randint(1+self.times_accelerating, MAX_X_SPEED+self.times_accelerating)
        if random.random() > 0.5:
            self.__dx *= -1

    def faster_velocity(self):
        """
        This method makes the game more difficult as the score increases.
        :return:
        """
        if 0 <= self.score < 200 and self.switch_increase_velocity:
            if random.random() > 0.5:
                self.__dx += 2
            else:
                self.__dx -= 0.5
            if random.random() > 0.5:
                self.__dx *= -1
            self.__dy += 1
            self.switch_increase_velocity = False
            self.times_accelerating += 1

        if 200 <= self.score < 400 and not self.switch_increase_velocity:
            if random.random() > 0.5:
                self.__dx += 1
            else:
                self.__dx -= 0.5
            if random.random() > 0.5:
                self.__dx *= -1
            self.__dy += 2
            self.switch_increase_velocity = True
            self.times_accelerating += 1

        if 400 <= self.score < 600 and self.switch_increase_velocity:
            if random.random() > 0.5:
                self.__dx += 1.5
            else:
                self.__dx -= 1
            if random.random() > 0.5:
                self.__dx *= -1
            self.__dy += 1.5
            self.switch_increase_velocity = False
            self.times_accelerating += 1

        if 600 <= self.score < 800 and not self.switch_increase_velocity:
            if random.random() > 0.5:
                self.__dx += 1.5
            else:
                self.__dx -= 1
            if random.random() > 0.5:
                self.__dx *= -1
            self.__dy += 1.5
            self.switch_increase_velocity = True
            self.times_accelerating += 1

        if 800 <= self.score < 1000 and self.switch_increase_velocity:
            if random.random() > 0.5:
                self.__dx += 2
            else:
                self.__dx -= 2
            if random.random() > 0.5:
                self.__dx *= -1
            self.__dy += 2
            self.switch_increase_velocity = False
            self.times_accelerating += 1


    def handle_wall_collision(self):
        """
        The ball will bounce when hitting top , right or left side.
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx *= -1
        if self.ball.y <= self.brick_offset:
            self.__dy *= -1

    def handle_fall_off(self):
        """
        :return: whether the ball falls to the bottom.
        """
        fall_off = self.ball.y >= self.window.height - self.ball.height
        return fall_off

    def reset_ball(self):
        """
        To put the ball at middle position of the window.
        """
        self.window.add(self.ball, x=((self.window_width - (self.ball_radius * 2)) / 2),
                        y=((self.window_height - (self.ball_radius * 2)) / 2))
        self.__dx = 0
        self.__dy = 0
        self.start_game = True

    def get_ball_dx(self):
        """
        :return: a value of horizontal velocity
        """
        return self.__dx

    def get_ball_dy(self):
        """
         :return: a value of vertical velocity
        """
        return self.__dy

    def touched_object(self):
        """
        detecting objects touched by the ball
        :return a detected object or None
        """
        upper_left_x = self.ball.x
        upper_left_y = self.ball.y
        upper_right_x = self.ball.x + self.ball.width
        upper_right_y = self.ball.y
        bottom_left_x = self.ball.x
        bottom_left_y = self.ball.y + self.ball.height
        bottom_right_x = self.ball.x + self.ball.width
        bottom_right_y = self.ball.y + self.ball.height
        while True:
            self.obj = self.window.get_object_at(upper_left_x, upper_left_y)
            if self.obj is not None:
                break
            self.obj = self.window.get_object_at(upper_right_x, upper_right_y)
            if self.obj is not None:
                break
            self.obj = self.window.get_object_at(bottom_left_x, bottom_left_y)
            if self.obj is not None:
                break
            self.obj = self.window.get_object_at(bottom_right_x, bottom_right_y)
            if self.obj is not None:
                break
            else:
                break
        return self.obj

    def remove_and_bouncing(self):
        """
        This method is about removing bricks and rebounding from bricks and the paddle.
        """
        if self.ball.y < self.brick_offset + self.brick_rows * (self.brick.height+self.brick_spacing) - \
                self.brick_spacing:  # when ball touches bricks
            self.ball.y = self.obj.y + self.obj.height
            self.window.remove(self.touched_object())
            self.num_removed_brick += 1
            self.score += 10
            if self.__dy < 0:  # ball bounce only when it moves up
                self.__dy = -self.__dy

        elif self.window.height - self.paddle_offset -self.paddle_height < self.ball.y + self.ball_radius*2 < \
                self.window.height - self.paddle_offset:
            # the ball will bounce if it hits the paddle (the score board doesn't make ball bounce)
            self.ball.y = self.paddle.y - self.ball.height
            self.__dy = -self.__dy

    def when_clear_all(self):
        """
        congratulatory label.
        """
        win_label = GLabel('PERFECT!')
        win_label.font = 'Verdana-40-bold-italic'
        win_label.color = 'magenta'
        self.window.add(win_label, x=((self.window_width - win_label.width) / 2), y=((self.window_height - win_label.height) / 2))

    def score_board(self):
        """
        label of score board.
        """
        self.score_label.text = 'Score: ' + str(self.score)
        self.window.add(self.score_label, x=0, y=self.window.height)








