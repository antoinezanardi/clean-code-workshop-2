function calculatePriceWithShipping(price: number, shipping: number): number {
  return price + shipping;
}

const totalPrice = calculatePriceWithShipping(100, 7);
