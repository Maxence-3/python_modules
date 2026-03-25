import functools
import operator


def spell_reducer(spells: list, operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict:
    return {
        "fire_enchant": functools.partial(base_enchantment,
                                          power=50, element="Fire"),
        "ice_enchant": functools.partial(base_enchantment,
                                         power=50, element="Ice"),
        "lightning_enchant": functools.partial(base_enchantment,
                                               power=50, element="Lightning")
    }


@functools.lru_cache(maxsize=None)
def memorized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast_spell(target):
        return f"Unknown spell target type: {type(target)}"

    @cast_spell.register(int)
    def _(target):
        return f"Damage spell deals {target} damage!"

    @cast_spell.register(str)
    def _(target):
        return f"Enchantment cast on {target}!"

    @cast_spell.register(list)
    def _(target):
        return f"Multi-cast hits {len(target)} targets: \
{', '.join(str(t) for t in target)}!"

    return cast_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memorized fibonacci...")
    print(f"Fib(10): {memorized_fibonacci(10)}")
    print(f"Fib(15): {memorized_fibonacci(15)}")
