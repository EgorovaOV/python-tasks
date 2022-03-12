import view
import rational_num
import complex_num
def button_click():
    num_a = view.get_value()
    num_b = view.get_value()
    rational_num.init(num_a, num_b)
    result = rational_num.sum()
    view.calc_res(result)

