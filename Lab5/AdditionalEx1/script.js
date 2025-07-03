function calculate(operator) {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const resultEl = document.getElementById('result');
    let result;
  
    if (isNaN(num1) || isNaN(num2)) {
      resultEl.textContent = 'Please enter valid numbers.';
      return;
    }
  
    switch (operator) {
      case '+':
        result = num1 + num2;
        break;
      case '-':
        result = num1 - num2;
        break;
      case '*':
        result = num1 * num2;
        break;
      case '/':
        result = num2 === 0 ? 'Cannot divide by zero' : num1 / num2;
        break;
    }
  
    resultEl.textContent = `Result: ${result}`;
  }
  