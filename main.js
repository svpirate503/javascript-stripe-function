


<script src="https://js.stripe.com/v3/"></script>

<script>
   var stripe = Stripe('{{ stripe_public_key }}');
   
   const buy_now_button = document.querySelector('#button_id')
   
   buy_now_button.addEventListener('click',event=>{
   
   
   stripe.redirectToCheckout({
   
   sessionId: '{{ session_id }}'}).then(function(result){
   
   
   
   });
   })
   
   </script>
   
   
   
   
   
   