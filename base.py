import time
import RPi.GPIO as GPIO
import font

GPIO.setmode(GPIO.BOARD)
cols = [15, 36, 32, 7, 35, 11, 16, 18]
rows = [29, 12, 31, 13, 40, 33, 38, 37]
state = []

for pin in cols+rows:
  GPIO.setup(pin, GPIO.OUT)

def output(pin, state):
  GPIO.output(pin, state)

def clear():
  state = [[0,0,0,0,0,0,0,0],\
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0]]
  for pin in cols+rows:
    output(pin, 0 if pin in cols else 1)

def dot(row, col):
  output(cols[col], GPIO.HIGH)
  output(rows[row], GPIO.LOW)

def matrix(matrix):
  transposed_matrix = zip(*matrix)

  try:
    while True:
      for col_id, col in enumerate(transposed_matrix):
        for row_id, cell in enumerate(col):
          if cell == 1:
            dot(row_id, col_id)
        time.sleep(1/960.0) # 120 Hz?
        clear()
  except KeyboardInterrupt:
    clear()
    raise

def draw(character):
  matrix(font.to_binary_matrix(character))

clear()

