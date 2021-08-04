from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm

#function to show dashboard data
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'accounts/dashboard.html', context)





#function to get products
#Author : Chetan Dharmik
#Date : 21/05/2021
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})



#function to get customer details by id
#Author : Chetan Dharmik
#Date : 21/05/2021
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer.html',context)

#function to create order 
#Author : Chetan Dharmik
#Date : 21/05/2021
def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

#function to update order	
#Author : Chetan Dharmik
#Date : 21/05/2021
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)


#function to delete order
#Author : Chetan Dharmik
#Date : 21/05/2021 
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)