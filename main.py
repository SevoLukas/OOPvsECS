import time
from OOP.oop import Product

from ECS.components import PriceComponent, PriceNumpyComponent, PriceArrayComponent
from ECS.registry import ComponentRegistry, EntityRegistry, ComponentType
from ECS.entities2 import EntityType
from ECS.systems import DiscountSystem, DiscountNumpySystem, DiscountVectorizedSystem

TEST_ECS = True
products_no = 7500000

if __name__ == "__main__":
    if TEST_ECS:
        entity_registry = EntityRegistry()
        component_registry = ComponentRegistry()
        price_component = PriceComponent()
        price_numpy_component = PriceNumpyComponent()
        price_array_component = PriceArrayComponent()
        component_registry.register_component(ComponentType.price, price_component)
        component_registry.register_component(ComponentType.price, price_numpy_component)
        component_registry.register_component(ComponentType.price, price_array_component)


        for i in range(products_no):
            entity = entity_registry.create_entity(EntityType.book)
            price_component.set_price(entity.entity_id, 100 + 10 * i)
            price_numpy_component.set_price(entity.entity_id, 100 + 10 * i)
            price_array_component.set_price(entity.entity_id, 100 + 10 * i)

        print("Starting discount computation")

        start_time = time.perf_counter()
        discount_system = DiscountSystem(price_component, 15)
        discount_system.update()
        end_time = time.perf_counter()
        print(f"DiscountSystem update took {end_time - start_time:.6f} seconds")

        start_time = time.perf_counter()
        discount_numpy_system = DiscountNumpySystem(price_numpy_component, 15)
        discount_numpy_system.update()
        end_time = time.perf_counter()
        print(f"DiscountNumpySystem update took {end_time - start_time:.6f} seconds")

        start_time = time.perf_counter()
        discount_vectorized_system = DiscountVectorizedSystem(price_array_component, 15)
        discount_vectorized_system.update()
        end_time = time.perf_counter()
        print(f"DiscountVectorizedSystem update took {end_time - start_time:.6f} seconds")
    else:
        products = []
        for i in range(products_no):
            products.append(Product(i, 100 + 10 * i))
        start_time = time.perf_counter()
        for product in products:
            product.price = product.price * 100 - 15 // 100
        end_time = time.perf_counter()
        print(f"OOP prices update took {end_time - start_time:.6f} seconds")


