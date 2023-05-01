from django.shortcuts import render
from django.http import HttpResponse

from .models import Sales

from .plotly_plot import plot_barchart, plot_linechart, plot_piechart

# Create your views here.

def index(request):
    sales_query = Sales.objects.values('product', 'price', 'purchase_date')

    total_sales_per_product = {}
    total_sales_per_day = {}
    for result in sales_query:
        product_name = result['product']
        day = result['purchase_date'].strftime('%a')

        # total sales by product
        if total_sales_per_product.get(product_name):
            total_sales_per_product[product_name] += result['price']
        else:
            total_sales_per_product[product_name] = result['price']

        if day in total_sales_per_day:
            total_sales_per_day[day] += result['price']
        else:
            total_sales_per_day[day] = result['price']


    # sales per day
    key = {
        'Mon': 1,
        'Tue': 2,
        'Wed': 3,
        'Thu': 4,
        'Fri': 5,
        'Sat': 6,
        'Sun': 7
    }
    days = sorted(total_sales_per_day, key=key.get) # sorting by days, so the result shows in order of days of the week
    sales_day, labels_day = [], []
    for k in days:
        sales_day.append(total_sales_per_day[k])
        labels_day.append(k)

    products = list(total_sales_per_product.keys())
    product_sales = list(total_sales_per_product.values())
    bar_chart = plot_barchart(
        products,
        product_sales,
        'Sales per product',
        'Product',
        'Sales'
        )

    line_chart = plot_linechart(
        labels_day,
        sales_day,
        "Total sales per day",
        "Days",
        "Sales"
        )

    pie_chart = plot_piechart(
        products,
        product_sales,
        "Product sales distribution",
        total_sales_per_product
        )

    # Page from the theme 
    return render(request, 'index.html', {
        'barchart': bar_chart,
        'linechart': line_chart,
        'piechart': pie_chart
        })
