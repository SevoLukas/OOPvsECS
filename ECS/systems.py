from ECS.components import PriceComponent, PriceNumpyComponent, PriceArrayComponent


class DiscountSystem:
    def __init__(self, price_component: PriceComponent, discount_percentage: int):
        """
        Initializes the DiscountSystem.

        :param price_component: An instance of PriceComponent.
        :param discount_percentage: Integer representing the percentage discount to apply (e.g., 20 means 20% off).
        """
        self.price_component = price_component
        self.discount_multiplier = 100 - discount_percentage

    def update(self) -> None:
        """
        Discounts all prices in the PriceComponent by applying the discount percentage.
        """
        for entity_id, price in enumerate(self.price_component.prices):
            if price is not None:
                self.price_component.prices[entity_id] = price * self.discount_multiplier // 100


class DiscountNumpySystem:
    def __init__(self, price_component: PriceNumpyComponent, discount_percentage: int):
        """
        Initializes the DiscountNumpySystem.

        :param price_component: An instance of PriceNumpyComponent.
        :param discount_percentage: Integer representing the percentage discount to apply.
        """
        self.price_component = price_component
        self.discount_multiplier = 100 - discount_percentage

    def update(self) -> None:
        """
        Discounts all prices in the PriceNumpyComponent by applying the discount percentage.
        Iterates over the numpy-backed array and updates each non-None price.
        """
        for entity_id in range(self.price_component.prices.size):
            price = self.price_component.prices[entity_id]
            if price is not None:
                self.price_component.prices[entity_id] = price * self.discount_multiplier // 100


class DiscountVectorizedSystem:
    def __init__(self, price_component: PriceArrayComponent, discount_percentage: int):
        """
        System uses vectorized operations on the array of proper integer types.
        :param price_component: An instance of PriceArrayComponent.
        :param discount_percentage: Integer representing the discount percentage.
        """
        self.price_component = price_component
        self.discount_multiplier = 100 - discount_percentage

    def update(self) -> None:
        """
        Applies the discount using vectorized operations.
        """
        # Perform discount calculation in a vectorized manner.
        self.price_component.prices[:] = self.price_component.prices * self.discount_multiplier // 100

