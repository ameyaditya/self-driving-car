import RPi.GPIO as g
g.setmode(g.BOARD)
m1_f = 18
m1_b = 22
m2_f = 15
m2_b = 13
g.setup(m1_f, g.OUT)
g.setup(m1_b, g.OUT)
g.setup(m2_f, g.OUT)
g.setup(m2_b, g.OUT)

def move_forward():
    g.output(m1_b, False)
    g.output(m2_b, False)
    g.output(m1_f, True)
    g.output(m2_f, True)

def move_backward():
    g.output(m1_f, False)
    g.output(m2_f, False)
    g.output(m1_b, True)
    g.output(m2_b, True)

def stop():
    g.output(m1_f, False)
    g.output(m2_f, False)
    g.output(m1_b, False)
    g.output(m2_b, False)

def main():
    while True:
        a = input()
        if a == '1':
            move_forward()
        elif a == '2':
            move_backward()
        elif a == '0':
            stop()
main()