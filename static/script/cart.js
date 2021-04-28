var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; ++i)
{
    updateBtns[i].addEventListener('click', UpdateCart)
    /* updateBtns[i].addEventListener('change', UpdateCart) */
}

function UpdateCart(event)
{
    var productId = this.dataset.product
    var action = this.dataset.action
    if (user === 'AnonymousUser')
    {
        console.log("User is not authenticated")
    }
    else
    {
        console.log("User:", user)
        UpdateUserOrder(productId, action)
    }
}

function UpdateUserOrder(productId, action)
{
    console.log("User is logged in, sending data...");
    var url = '/updateItem/'
    fetch(url, {
        method: 'POST', 
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log("Data:", data)
        location.reload()
    });
}