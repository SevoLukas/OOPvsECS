from dataclasses import dataclass, field

import numpy as np


@dataclass
class PriceComponent:
    prices: list = field(default_factory=list)

    def set_price(self, entity_id: int, price: int) -> None:
        current_len = len(self.prices)
        if entity_id >= current_len:
            new_len = current_len if current_len > 0 else 1
            while new_len <= entity_id:
                new_len *= 2
            # Extend the list with None to reach the new length
            self.prices.extend([None] * (new_len - current_len))
        self.prices[entity_id] = price

    def get_price(self, entity_id: int) -> int or None:
        if entity_id < len(self.prices):
            return self.prices[entity_id]
        return None


@dataclass
class PriceNumpyComponent:
    """Using a numpy array (of object type) to store Python integers."""
    prices: np.ndarray = field(default_factory=lambda: np.array([], dtype=object))

    def set_price(self, entity_id: int, price: int) -> None:
        current_size = self.prices.size
        if entity_id >= current_size:
            new_size = current_size if current_size > 0 else 1
            while new_size <= entity_id:
                new_size *= 2
            # Create a new array with the new size, using dtype=object
            new_prices = np.empty(new_size, dtype=object)
            if current_size > 0:
                new_prices[:current_size] = self.prices
            # Initialize new entries to None
            new_prices[current_size:] = None
            self.prices = new_prices
        self.prices[entity_id] = price

    def get_price(self, entity_id: int) -> int or None:
        if entity_id < self.prices.size:
            return self.prices[entity_id]
        return None


@dataclass
class PriceArrayComponent:
    """Component: using numpy array with proper numeric type for vectorized operations."""
    prices: np.ndarray = field(default_factory=lambda: np.empty(0, dtype=np.int64))

    def set_price(self, entity_id: int, price: int) -> None:
        current_size = self.prices.size
        if entity_id >= current_size:
            new_size = current_size if current_size > 0 else 1
            while new_size <= entity_id:
                new_size *= 2
            # Create a new numeric array with the new size using the same dtype
            new_prices = np.empty(new_size, dtype=np.int64)
            if current_size > 0:
                new_prices[:current_size] = self.prices
            # Initialize new entries to 0
            new_prices[current_size:] = 0
            self.prices = new_prices
        self.prices[entity_id] = price

    def get_price(self, entity_id: int) -> int or None:
        if entity_id < self.prices.size:
            return int(self.prices[entity_id])
        return None



@dataclass
class NameComponent:
    names: list = field(default_factory=list)

    def set_name(self, entity_id: int, name: str) -> None:
        current_len = len(self.names)
        if entity_id >= current_len:
            new_len = current_len if current_len > 0 else 1
            while new_len <= entity_id:
                new_len *= 2
            self.names.extend([None] * (new_len - current_len))
        self.names[entity_id] = name

    def get_name(self, entity_id: int) -> int or None:
        if entity_id < len(self.names):
            return self.names[entity_id]
        return None