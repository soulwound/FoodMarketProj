function show() {
    if (document.querySelector('#cart').style.display == 'none') {
        document.querySelector('#cart').style.display = 'block'
    } else {
        document.querySelector('#cart').style.display = 'none'
    }
}

let cart_list = {
    'roll-fila': 0,
    'sushi-shrimp': 0,
};

function addToCart(id) {
    cart_list[id]++;
    console.log(cart_list);
    document.querySelector("#"+id).setAttribute('disabled', '');
    document.querySelector("#"+id).textContent = 'В корзине';
    document.querySelector("#"+id).style.backgroundColor = '#C95C3F'
    updateCart(cart_list);
}

function updateCart(cart_list) {
    if (cart_list == 0) {
        document.querySelector('#if-cart-is-empty-img').style.display = 'block';
        document.querySelector('#if-cart-is-empty-alert').style.display = 'block';
    } else {
        document.querySelector('#if-cart-is-empty-img').style.display = 'none';
        document.querySelector('#if-cart-is-empty-alert').style.display = 'none';
    }
}

function showAuthorizationWindow() {
    if (document.querySelector('#authorization-window').style.display == 'none') {
        document.querySelector('#authorization-window').style.display = 'block'
    } else {
        document.querySelector('#authorization-window').style.display = 'none'
    }
}

function closeAuthorizationWindow() {
    document.querySelector('#authorization-window').style.display = 'none';
}