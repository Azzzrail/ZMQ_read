import PySimpleGUIQt as sgQT
#import PySimpleGUI as sg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
#from matplotlib.figure import Figure
#import matplotlib.pyplot as plt


input_field_1: int


def ask_port():
    global input_field_1
    sgQT.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sgQT.Text('TEST_TEST_TEST')],
              # кнопка для выбора папки с файлами
              #[sg.T('Source Folder')], [sg.In(key='input')], [sg.FolderBrowse(target='input')],
              # Поле для ввода номера канала
              [sgQT.Text('Enter port number'), sgQT.InputText()],

              #[sg.Text('Plot tools enable/disable')],
              # чербоксы для работы с нарисованной гистограммой
              # [sg.Checkbox('pan', default=True), sg.Checkbox('wheel_zoom', default=True),
              # sg.Checkbox('box_zoom', default=True), sg.Checkbox('reset', default=True),
              # sg.Checkbox('save', default=True), sg.Checkbox('box_select', default=True)],
              # [sg.Checkbox('lasso_select', default=True),
              # sg.Checkbox('crosshair', default=True), sg.Checkbox('hover', default=True)],
              # Конец чекбоксов
              [sgQT.Button('Ok'), sgQT.Button('Cancel')]
              ]
    # TODO: Добавить вычитку состояний чекбоксов
    # Create the Window
    window = sgQT.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break
        elif event in 'Ok':
            input_field_1 = int(values[0])
            break

    window.close()


    try:
        return input_field_1
    except NameError:
        return None


def dwraw_plot_window(fig):
    #print(fig)

    # ------------------------------- Beginning of Matplotlib helper code -----------------------

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ------------------------------- Beginning of GUI CODE -------------------------------

    # define the window layout
    layout = [[sg.Text('Plot test')],
              [sg.Canvas(key='-CANVAS-')],
              [sg.Button('Ok')]]

    # create the form and show it without the plot
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout, finalize=True,
                       element_justification='center', font='Helvetica 18')

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    #ani = animation.FuncAnimation(fig, draw_figure, frames=30)
    #window.close()
    return
