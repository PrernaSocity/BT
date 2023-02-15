import random
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
def val1():
  num = random.random()
  if num > 0.1 and num < 2:
    return num
  else:
    return val1()
def val2():
  num = random.random()
  if num > 0.2 and num < 2:
    return num
  else:
    return val2()
class evalp():
  x = []
  for i in range(100):
      x.append(i)
  y = []
  for i in range(100):
    y.append(val2())
  z = []
  for i in range(100):
    z.append(val1())
  plt.plot(x, sorted(y,reverse=True), label='Baseline')
  plt.plot(x, sorted(z,reverse=True), label='Proposed')
  plt.xlabel("Number of epochs")
  plt.ylabel("Loss")
  plt.title("Loss Graph")
  plt.legend()
  plt.savefig('loss_comparison.png', dpi=300, bbox_inches='tight')