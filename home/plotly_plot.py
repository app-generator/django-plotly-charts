import plotly.graph_objs as go
from plotly.offline import plot


def plot_barchart(x, y, title, x_label, y_label):
    fig = go.Figure(data=go.Bar(name='BarChart', x=x, y=y))

    fig.update_layout(
        title_text = title,
        xaxis_title = x_label,
        yaxis_title = y_label,
        # width=300,
        # height=300,
        template=None,
        margin=dict(l=40, r=20, t=30, b=40)
    )

    barchart = plot({'data': fig}, output_type='div')
    return barchart

def plot_linechart(x, y, title, x_label, y_label):
    fig = go.Figure(data=go.Line(name='LineChart', x=x, y=y))
    fig.update_layout(
        title_text = title,
        xaxis_title = x_label,
        yaxis_title = y_label,
        # width=300,
        # height=300,
        template=None,
        margin=dict(l=40, r=20, t=30, b=40),
    )

    linechart = plot({'data': fig}, output_type='div')
    return linechart

def plot_piechart(names, values, title, legend):
    fig = go.Figure(data=go.Pie(name='PieChart', values=values, labels=names))

    fig.update_layout(
        title_text = title,
        # width=300,
        # height=300,
        template=None,
        margin=dict(l=40, r=20, t=30, b=40),
    )

    piechart = plot({'data': fig}, output_type='div')
    return piechart
