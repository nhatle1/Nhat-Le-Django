var inputValue = document.getElementsByClassName('quantity-input')
var decreaseBtn = document.getElementsByClassName('quantity-decrease')
for (var i = 0; i < inputValue.length; ++i)
{
    if (parseInt(inputValue[i].value) === 1)
    {
        decreaseBtn[i].className += "-disabled"
    }
}

function dropdownmenu() {
    var x = document.getElementById("navbar");
    if (x.className === "topnav") {
        x.className += " responsive";        
    } else {
        x.className = "topnav";

    }
}
