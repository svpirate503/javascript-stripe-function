import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY



def create_checkout_session():
    try:
       session = stripe.checkout.Session.create(
          payment_method_types = ['card'],
            line_items=[
            
           
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1}]
                
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    context = {'session_id':session.id,'stripe_public_key':settings.STRIPE_PUBLISHABLE_KEY}
    return render(request,'index.html',context)
