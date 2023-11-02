from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .forms import OrderPaymentForm
from eshofy.settings import *
client = razorpay.Client(auth=("rzp_test_5mqNYrna5GtgXH", "nff2jVAwFril2l4AgFX0hz4o"))

# Create your views here.
def home(request):
    # products = Product.objects.all().filter(is_available=True)[0:8]
    # context = {
    #     'products': products,
    # }

    return render(request, 'home.html')


@csrf_exempt
def coffee_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100

        # create Razorpay client
        client = razorpay.Client(auth=('rzp_test_5mqNYrna5GtgXH', 'nff2jVAwFril2l4AgFX0hz4o'))

        # create order
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            order = Order(
                name=name,
                amount=amount,
                order_id=order_id
            )
            order.save()
            response_payment['name'] = name

            form = OrderPaymentForm(request.POST or None)
            return render(request, 'coffee_payment.html', {'form': form, 'payment': response_payment})

    form = OrderPaymentForm()
    return render(request, 'coffee_payment.html', {'form': form})

@csrf_exempt
def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_5mqNYrna5GtgXH', 'nff2jVAwFril2l4AgFX0hz4o'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        order = Order.objects.get(order_id=response['razorpay_order_id'])
        order.razorpay_payment_id = response['razorpay_payment_id']
        order.paid = True
        order.save()
        return render(request, 'payment_status.html', {'status': True})
    except:
        return render(request, 'payment_status.html', {'status': False})