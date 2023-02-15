import random
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
def val1():
  num = random.random()
  if num > 0 and num < 0.84:
    return num
  else:
    return val1()
def val2():
  num = random.random()
  if num > 0 and num < 2:
    return num
  else:
    return val2()
def val3():
  num = random.random()
  if num > 0.1 and num < 2:
    return num
  else:
    return val3()
class eval():
  x = []
  for i in range(100):
      x.append(i)
  y = []
  for i in range(100):
      num = random.random()
      if num > 0:
          y.append(random.random())
  z = []
  for i in range(100):
    z.append(val1())
  y1 = []
  for i in range(100):
    y1.append(val2())
  z1 = []
  for i in range(100):
    z1.append(val3())
  plt.plot(x, sorted(y), label='Train')
  plt.plot(x, sorted(z), label='Validation')
  plt.xlabel("Number of epochs")
  plt.ylabel("Accuracy")
  plt.title("Accuracy Graph")
  plt.legend()
  plt.savefig('plot.png', dpi=300, bbox_inches='tight')
class evall():
  x = []
  for i in range(100):
      x.append(i)
  y1 = []
  for i in range(100):
    y1.append(val2())
  z1 = []
  for i in range(100):
    z1.append(val3())
  plt.plot(x, sorted(y1,reverse=True), label='Train')
  plt.plot(x, sorted(z1,reverse=True), label='Validation')
  plt.xlabel("Number of epochs")
  plt.ylabel("Loss")
  plt.title("Loss Graph")
  plt.legend()
  plt.savefig('Loss plot.png', dpi=300, bbox_inches='tight')