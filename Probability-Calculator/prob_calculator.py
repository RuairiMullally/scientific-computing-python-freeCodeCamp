import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num):
    if num > len(self.contents):
      return self.contents
    else:
      drawn = []
      for i in range(num):
        drawn.append(random.choice(self.contents))
        self.contents.remove(drawn[i])
      return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  expected_no_of_balls = []
  for key in expected_balls:
      expected_no_of_balls.append(expected_balls[key])
  successes = 0

  print(expected_no_of_balls)

  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls = new_hat.draw(num_balls_drawn)

    no_of_balls = []
    for key in expected_balls:
      no_of_balls.append(balls.count(key))

    if no_of_balls >= expected_no_of_balls:
      successes += 1

  return successes/num_experiments
