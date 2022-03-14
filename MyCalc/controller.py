import view
import rational_num
#import complex_num
def button_click():
    num_a = view.get_value()
    num_b = view.get_value()
    rational_num.init(num_a, num_b)
    action = view.get_action()
    rational_num.init_ac(action)
    if action == 1:
          result = rational_num.sum(num_a, num_b)
          view.calc_res(result)
    elif action == 2:
          result = rational_num.dif(num_a, num_b)
          view.calc_res(result)
    elif action == 3:
          result = rational_num.mult(num_a, num_b)
          view.calc_res(result)
    elif action == 4:
          result = rational_num.div(num_a, num_b)
          view.calc_res(result)

    #view.calc_res(result)



