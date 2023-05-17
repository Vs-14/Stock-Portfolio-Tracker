const label = document.querySelector("label[for='quantity']");
const p_price = document.querySelector('.p_price');
const cp_price = document.querySelector('.cp_price');
const quantityInput = document.querySelector('.quantity');
const totalval = document.querySelector('.change');

// Calculate total cost whenever quantity changes
quantityInput.addEventListener('input', () => {
    const price = p_price.value;
    const cprice = cp_price.value;
    const quantity = quantityInput.value;
    label.textContent = 'No. Of Shares To Sell:' + quantity
    const val = ((cprice-price) * quantity).toFixed(2);
    if(cp_price >= p_price){
        totalval.textContent = `Profit: $${val}`;
    }
    else{
        totalval.textContent = `Loss: $${val}`;
    }
});