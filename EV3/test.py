import time

from ev3dev.ev3 import Sound

c = 261
d = 294
e = 329
f = 349
g = 391
gS = 415
a = 440
aS = 455
b = 466
cH = 523
cSH = 554
dH = 587
dSH = 622
eH = 659
fH = 698
fSH = 740
gH = 784
gSH = 830
aH = 880


def firstSection():
    Sound.tone(a, 500).wait()
    Sound.tone(a, 500).wait()
    Sound.tone(a, 500).wait()
    Sound.tone(f, 350).wait()
    Sound.tone(cH, 150).wait()
    Sound.tone(a, 500).wait()
    Sound.tone(f, 350).wait()
    Sound.tone(cH, 150).wait()
    Sound.tone(a, 650).wait()

    time.sleep(0.5)

    Sound.tone(eH, 500).wait()
    Sound.tone(eH, 500).wait()
    Sound.tone(eH, 500).wait()
    Sound.tone(fH, 350).wait()
    Sound.tone(cH, 150).wait()
    Sound.tone(gS, 500).wait()
    Sound.tone(f, 350).wait()
    Sound.tone(cH, 150).wait()
    Sound.tone(a, 650).wait()

    time.sleep(0.5)


def secondSection():
    Sound.tone(aH, 500).wait()
    Sound.tone(a, 300).wait()
    Sound.tone(a, 150).wait()
    Sound.tone(aH, 500).wait()
    Sound.tone(gSH, 325).wait()
    Sound.tone(gH, 175).wait()
    Sound.tone(fSH, 125).wait()
    Sound.tone(fH, 125).wait()
    Sound.tone(fSH, 250).wait()

    time.sleep(0.325)

    Sound.tone(aS, 250).wait()
    Sound.tone(dSH, 500).wait()
    Sound.tone(dH, 325).wait()
    Sound.tone(cSH, 175).wait()
    Sound.tone(cH, 125).wait()
    Sound.tone(b, 125).wait()
    Sound.tone(cH, 250).wait()

    time.sleep(0.350)

Sound.beep()
time.sleep(1)
# Play first section
firstSection()

# Play second section
secondSection()

# Variant 1
Sound.tone(f, 250).wait()
Sound.tone(gS, 500).wait()
Sound.tone(f, 350).wait()
Sound.tone(a, 125).wait()
Sound.tone(cH, 500).wait()
Sound.tone(a, 375).wait()
Sound.tone(cH, 125).wait()
Sound.tone(eH, 650).wait()

time.sleep(500)

# Repeat second section
secondSection()

# Variant 2
Sound.tone(f, 250).wait()
Sound.tone(gS, 500).wait()
Sound.tone(f, 375).wait()
Sound.tone(cH, 125).wait()
Sound.tone(a, 500).wait()
Sound.tone(f, 375).wait()
Sound.tone(cH, 125).wait()
Sound.tone(a, 650).wait()

time.sleep(0.650)
