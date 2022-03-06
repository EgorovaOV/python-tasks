import model_mult
import view
def button_click():
    #model.init(get_value()) можем инициализировать нач значения получив их из метода в модели
    value_a = view.get_value()    # в модели должен быть этот метод
    value_b = view.get_value()
    model_mult.init(value_a, value_b)#надо произвести инициализацию начальных значений
    result = model_mult.mult()
    view.view_data(result)
