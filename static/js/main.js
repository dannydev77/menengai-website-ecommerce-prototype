// add to cart function
var updateButtons = document.getElementsByClassName('update-cart')
for (i = 0; i < updateButtons.length; i++) {
updateButtons[i].addEventListener('click',function(){
var productID = this.dataset.product
var action = this.dataset.action
console.log('productID: ',productID, 'action: ',action)

console.log('User:', user)
if (user == 'AnonymousUser') {
    console.log('User is not authenticated')
}else{
  updateUserOrder(productID, action)
}
})
}

function updateUserOrder(productID, action){
  console.log('User is authenticated, sending data..')

  var url = '/shop/update/'

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body:JSON.stringify({'productID': productID, 'action': action})
  })
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    
    console.log('data',data)
    location.reload()
  })
}

    // Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()