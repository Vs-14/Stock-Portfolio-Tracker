const symbol = document.querySelector('.symbol').value;
const priceInput = document.querySelector('.price');
const quantityInput = document.querySelector('.quantity');
const totalCost = document.querySelector('.total-cost')

// Calculate total cost whenever quantity changes
quantityInput.addEventListener('input', () => {
    const price = priceInput.value;
    const quantity = quantityInput.value;
    const cost = (price * quantity).toFixed(2);
    if(symbol.includes('BSE')){
        totalCost.textContent = `Total Cost: Rs${cost}`;
    }
    else{
        totalCost.textContent = `Total Cost: $${cost}`;
    }
});