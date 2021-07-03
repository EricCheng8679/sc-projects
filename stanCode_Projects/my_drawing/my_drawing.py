"""
File: my_drawing.py
Name: Eric Cheng
----------------------
Draw a picture belonging to yourself by campy.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    MLB LOGO
    """
    window = GWindow(width=800, height=400, title='Logo of Major League Baseball')
    background = GRect(800, 400)
    background.filled = True
    background.fill_color = 'navy'
    window.add(background)
    frame = GRect(700, 320)
    frame.filled = True
    frame.fill_color = 'white'
    frame.color = 'white'
    window.add(frame, x=50, y=40)
    corner_upper_left = GArc(50, 50, 90, 90)
    corner_upper_left .filled = True
    corner_upper_left .fill_color = 'white'
    corner_upper_left .color = 'white'
    window.add(corner_upper_left, x=36, y=27)
    corner_bottom_left = GArc(50, 50, 180, 90)
    corner_bottom_left.filled = True
    corner_bottom_left.fill_color = 'white'
    corner_bottom_left.color = 'white'
    window.add(corner_bottom_left, x=36, y=348)
    corner_bottom_right = GArc(50, 50, 270, 90)
    corner_bottom_right.filled = True
    corner_bottom_right.fill_color = 'white'
    corner_bottom_right.color = 'white'
    window.add(corner_bottom_right, x=737, y=348)
    corner_upper_right = GArc(50, 50, 0, 90)
    corner_upper_right.filled = True
    corner_upper_right.fill_color = 'white'
    corner_upper_right.color = 'white'
    window.add(corner_upper_right, x=737, y=27)
    left_bar = GRect(13, 320)
    left_bar.filled = True
    left_bar.fill_color = 'white'
    left_bar.color = 'white'
    window.add(left_bar, x=36, y=40)
    right_bar = GRect(13, 320)
    right_bar.filled = True
    right_bar.fill_color = 'white'
    right_bar.color = 'white'
    window.add(right_bar, x=749, y=40)
    top_bar = GRect(700, 13)
    top_bar.filled = True
    top_bar.fill_color = 'white'
    top_bar.color = 'white'
    window.add(top_bar, x=50, y=27)
    bottom_bar = GRect(700, 13)
    bottom_bar.filled = True
    bottom_bar.fill_color = 'white'
    bottom_bar.color = 'white'
    window.add(bottom_bar, x=50, y=360)

    frame2 = GRect(660, 280)
    frame2.filled = True
    frame2.fill_color = 'navy'
    frame2.color = 'navy'
    window.add(frame2, x=68, y=60)
    corner_upper_left2 = GArc(50, 50, 90, 90)
    corner_upper_left2.filled = True
    corner_upper_left2.fill_color = 'navy'
    corner_upper_left2.color = 'navy'
    window.add(corner_upper_left2, x=55, y=47)
    corner_bottom_left2 = GArc(50, 50, 180, 90)
    corner_bottom_left2.filled = True
    corner_bottom_left2.fill_color = 'navy'
    corner_bottom_left2.color = 'navy'
    window.add(corner_bottom_left2, x=55, y=327)
    corner_bottom_right2 = GArc(50, 50, 270, 90)
    corner_bottom_right2.filled = True
    corner_bottom_right2.fill_color = 'red'
    corner_bottom_right2.color = 'red'
    window.add(corner_bottom_right2, x=716, y=327)
    corner_upper_right2 = GArc(50, 50, 0, 90)
    corner_upper_right2.filled = True
    corner_upper_right2.fill_color = 'red'
    corner_upper_right2.color = 'red'
    window.add(corner_upper_right2, x=716, y=47)
    left_bar2 = GRect(13, 280)
    left_bar2.filled = True
    left_bar2.fill_color = 'navy'
    left_bar2.color = 'navy'
    window.add(left_bar2, x=55, y=60)
    right_bar2 = GRect(13, 280)
    right_bar2.filled = True
    right_bar2.fill_color = 'red'
    right_bar2.color = 'red'
    window.add(right_bar2, x=728, y=60)
    top_bar_b = GRect(396, 13)
    top_bar_b.filled = True
    top_bar_b.fill_color = 'navy'
    top_bar_b.color = 'navy'
    window.add(top_bar_b, x=69, y=47)
    top_bar_r = GRect(262, 13)
    top_bar_r.filled = True
    top_bar_r.fill_color = 'red'
    top_bar_r.color = 'red'
    window.add(top_bar_r, x=466, y=47)
    bottom_bar_b = GRect(396, 13)
    bottom_bar_b.filled = True
    bottom_bar_b.fill_color = 'navy'
    bottom_bar_b.color = 'navy'
    window.add(bottom_bar_b, x=69, y=339)
    bottom_bar_r = GRect(262, 13)
    bottom_bar_r.filled = True
    bottom_bar_r.fill_color = 'red'
    bottom_bar_r.color = 'red'
    window.add(bottom_bar_r, x=466, y=339)
    frame2_r = GRect(262, 280)
    frame2_r.filled = True
    frame2_r.fill_color = 'red'
    frame2_r.color = 'red'
    window.add(frame2_r, x=466, y=60)

    frame3_b = GPolygon()
    frame3_b.filled = True
    frame3_b.fill_color = 'navy'
    frame3_b.color = 'navy'
    frame3_b.add_vertex((466, 115))
    frame3_b.add_vertex((540, 185))
    frame3_b.add_vertex((466, 185))
    window.add(frame3_b)

    frame3_r = GPolygon()
    frame3_r.filled = True
    frame3_r.fill_color = 'red'
    frame3_r.color = 'red'
    frame3_r.add_vertex((440, 47))
    frame3_r.add_vertex((480, 47))
    frame3_r.add_vertex((480, 96))
    window.add(frame3_r)

    ball = GOval(45, 45)
    ball.filled = True
    ball.fill_color = 'white'
    ball.color = 'white'
    window.add(ball, x=110, y=273)

    helmet = GArc(100, 170, 345, 200)
    helmet.filled = True
    helmet.color = 'white'
    helmet.fill_color = 'white'
    window.add(helmet, x=350, y=80)

    brim = GPolygon()
    brim.filled = True
    brim.fill_color = 'white'
    brim.color = 'white'
    brim.add_vertex((320, 148))
    brim.add_vertex((355, 148))
    brim.add_vertex((350, 134))
    window.add(brim)

    helmet2 = GRect(90, 20)
    helmet2.filled = True
    helmet2.fill_color = 'white'
    helmet2.color = 'white'
    window.add(helmet2, 350, 128)

    nose = GPolygon()
    nose.add_vertex((345, 173))
    nose.add_vertex((365, 173))
    nose.add_vertex((362, 143))
    nose.filled = True
    nose.fill_color = 'white'
    nose.color = 'white'
    window.add(nose)

    neck = GRect(80, 50)
    neck.filled = True
    neck.fill_color = 'white'
    neck.color = 'white'
    window.add(neck, 360, 148)

    shoulder_left = GArc(70, 480, 0, 180)
    shoulder_left.filled = True
    shoulder_left.color = 'white'
    shoulder_left.fill_color = 'white'
    window.add(shoulder_left, x=325, y=190)

    back = GPolygon()
    back.add_vertex((335, 300))
    back.add_vertex((360, 300))
    back.add_vertex((360, 353))
    back.filled = True
    back.fill_color = 'white'
    back.color = 'white'
    window.add(back)

    back2 = GRect(185, 53)
    back2.filled = True
    back2.fill_color = 'white'
    back2.color = 'white'
    window.add(back2, 360, 300)

    shoulder_right = GArc(340, 80, 0, 90)
    shoulder_right.filled = True
    shoulder_right.color = 'white'
    shoulder_right.fill_color = 'white'
    window.add(shoulder_right, x=355, y=170)

    body = GRect(158, 125)
    body.filled = True
    body.fill_color = 'white'
    body.color = 'white'
    window.add(body, 360, 185)

    elbow = GPolygon()
    elbow.add_vertex((517, 181))
    elbow.add_vertex((517, 310))
    elbow.add_vertex((610, 310))
    elbow.add_vertex((625, 280))
    elbow.filled = True
    elbow.fill_color = 'white'
    elbow.color = 'white'
    window.add(elbow)

    front_elbow = GOval(67, 67)
    front_elbow.filled = True
    front_elbow.fill_color = 'white'
    front_elbow.color = 'white'
    window.add(front_elbow, x=545, y=235)

    finger1 = GOval(30, 30)
    finger1.filled = True
    finger1.fill_color = 'white'
    finger1.color = 'white'
    window.add(finger1, x=545, y=210)

    finger2 = GOval(30, 30)
    finger2.filled = True
    finger2.fill_color = 'white'
    finger2.color = 'white'
    window.add(finger2, x=534, y=193)

    finger3 = GOval(32, 32)
    finger3.filled = True
    finger3.fill_color = 'white'
    finger3.color = 'white'
    window.add(finger3, x=520, y=178)

    bat = GPolygon()
    bat.add_vertex((400, 47))
    bat.add_vertex((450, 47))
    bat.add_vertex((545, 180))
    bat.add_vertex((525, 180))
    bat.filled = True
    bat.fill_color = 'white'
    bat.color = 'white'
    window.add(bat)

    label1 = GLabel('TAIPEI SC', x=380, y=235)
    label1.font = '-20'
    label1.color = 'red'
    window.add(label1)

    label2 = GLabel('101', x=410, y=300)
    label2.font = '-35'
    label2.color = 'navy'
    window.add(label2)


if __name__ == '__main__':
    main()
