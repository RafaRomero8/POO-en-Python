from bokeh.plotting import figure, output_file, show

# importar de bokeh tres funciones figure,donde se va a graficar,
# output para generar un hatml
# show para generar un servidor que se muestra en el brouwser que se prende

if __name__ == '__main__':
    output_file('graficado_simple.html')  # generarun putput que se llame graficado...
    fig = figure()  # se genera una figura es una funcion

    total_vals = int(input('Cuantos valores quieres graficar?'))  # pedir al usuario cuantos valores quiere graficar..
    x_vals = list(range(total_vals))  # generar valores x en un rango del 0 a
    y_vals = []  # valores dpendientes

    for x in x_vals:  # recorre los valores
        val = int(input(f'Valor y para {x}'))  # genera un nuevo valor un valor y para x
        y_vals.append(val)  # funcion append

    fig.line(x_vals, y_vals, line_width=2)  # utiliza los valres de y y x ,pone una linea
    show(fig)  # muestra la grafica o figua
