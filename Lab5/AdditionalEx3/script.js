let cart = [];

function addToCart(name, price) {
  const index = cart.findIndex(item => item.name === name);
  if (index !== -1) {
    cart[index].qty += 1;
  } else {
    cart.push({ name, price, qty: 1 });
  }
  renderCart();
}

function removeItem(name) {
  cart = cart.filter(item => item.name !== name);
  renderCart();
}

function renderCart() {
  const tbody = document.querySelector("#cart tbody");
  tbody.innerHTML = "";
  let grandTotal = 0;

  cart.forEach(item => {
    const total = item.qty * item.price;
    grandTotal += total;
    const row = `
      <tr>
        <td>${item.name}</td>
        <td>${item.qty}</td>
        <td>$${item.price}</td>
        <td>$${total}</td>
        <td><button onclick="removeItem('${item.name}')">Remove</button></td>
      </tr>
    `;
    tbody.innerHTML += row;
  });

  document.getElementById("grandTotal").innerText = `Grand Total: $${grandTotal}`;
}
