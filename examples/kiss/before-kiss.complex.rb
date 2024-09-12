class PriceCalculator
  def calculate(price, tax, discount, shipping, coupon = nil)
    final_price = price

    if coupon
      if coupon.type == 'percentage'
        final_price -= (price * coupon.value / 100)
      elsif coupon.type == 'fixed'
        final_price -= coupon.value
      end
    end

    if discount > 0
        final_price -= (price * discount / 100)
      else
        final_price
    end

    final_price += tax
    final_price += shipping
    final_price
  end
end
