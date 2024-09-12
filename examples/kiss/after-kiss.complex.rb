class PriceCalculator
  def calculate(price, tax, discount, shipping, coupon = nil)
    final_price = price
    final_price = apply_coupon(final_price, coupon)
    final_price = apply_discount(final_price, discount)
    final_price = add_tax(final_price, tax)
    final_price = add_shipping(final_price, shipping)
    final_price
  end

  private

  def apply_coupon(price, coupon)
    return price unless coupon

    case coupon.type
    when 'percentage'
      price - (price * coupon.value / 100)
    when 'fixed'
      price - coupon.value
    else
      price
    end
  end

  def apply_discount(price, discount)
    price - (price * discount / 100)
  end

  def add_tax(price, tax)
    price + tax
  end

  def add_shipping(price, shipping)
    price + shipping
  end
end
