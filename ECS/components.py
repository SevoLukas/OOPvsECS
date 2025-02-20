from dataclasses import dataclass, field

import numpy as np


@dataclass
class PriceComponent:
    prices: list = field(default_factory=list)

    def set_price(self, entity_id: int, price: int) -> None:
        while len(self.prices) <= entity_id:
            self.prices.append(None)
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
        if entity_id >= self.prices.size:
            # Extend the array to have enough entries (filling with None).
            extension = np.full(entity_id - self.prices.size + 1, None, dtype=object)
            self.prices = np.concatenate((self.prices, extension))
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
        if entity_id >= self.prices.size:
            new_size = entity_id + 1
            new_prices = np.empty(new_size, dtype=np.int64)
            # preserve existing entries if any
            if self.prices.size > 0:
                new_prices[:self.prices.size] = self.prices
            # initialize new entries to 0 (or any default value)
            if new_size > self.prices.size:
                new_prices[self.prices.size:] = 0
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
        while len(self.names) <= entity_id:
            self.names.append(None)
        self.names[entity_id] = name

    def get_name(self, entity_id: int) -> int or None:
        if entity_id < len(self.names):
            return self.names[entity_id]
        return None