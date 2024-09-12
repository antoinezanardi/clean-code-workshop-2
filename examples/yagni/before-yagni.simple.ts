function calculateTotal(price: number, tax: number, discount: number, shipping: number): number {
  return price + tax - discount + shipping;
}

const totalPrice = calculateTotal(100, 10, 5, 7);
