"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

# global variables
lives = NUM_LIVES
score = 0                # game score


def main():
    """
    The break out game will show the rest of lives and score user gotten.
    Also,the difficulty of the game will increase as the score becomes higher
    """
    global lives
    live_label = GLabel('Lives: ' + str(lives))
    live_label.font = 'Verdana-20-bold'

    graphics = BreakoutGraphics()
    graphics.window.add(live_label, 0, graphics.brick_offset-graphics.ball_radius*2)
    # subtracting diameter of ball is to prevent ball from hitting the label
    graphics.score_board()
    while True:
        if graphics.get_start_signal():  # to determine whether to start game when users click mouse
            graphics.set_ball_velocity()
        else:
            graphics.ball.move(graphics.get_ball_dx(), graphics.get_ball_dy())
        graphics.handle_wall_collision()
        if graphics.handle_fall_off():   # when ball touches bottom
            lives -= 1
            if lives > 0:
                live_label.text = 'Lives: ' + str(lives)
                graphics.reset_ball()
                if graphics.get_start_signal():  # to determine whether to start game when users click mouse

                    graphics.reborn_velocity()
            else:
                live_label.text = 'Lives: 0'
        if graphics.touched_object() is not None:
            graphics.remove_and_bouncing()
            graphics.score_board()
            if graphics.num_removed_brick == graphics.brick_rows * graphics.brick_cols: # when all the bricks are removed
                graphics.when_clear_all()
                break
        graphics.faster_velocity()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
