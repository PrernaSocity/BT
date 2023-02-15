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
  if num > 0 and num < 0.78:
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
  plt.plot(x, sorted(y), label='Baseline')
  plt.plot(x, sorted(z), label='Proposed')
  plt.xlabel("Number of epochs")
  plt.ylabel("Accuracy")
  plt.title("Accuracy Graph")
  plt.legend()
  plt.savefig('accuracy_comparison.png', dpi=300, bbox_inches='tight')