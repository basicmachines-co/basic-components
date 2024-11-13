from basic_components.utils.tailwind import tw


def test_basic_merge():
    result = tw("p-4 bg-red-500", "p-8")
    assert result == "bg-red-500 p-8"


def test_with_modifiers():
    result = tw("sm:p-4 bg-red-500", "sm:p-8")
    assert result == "bg-red-500 sm:p-8"


def test_with_arbitrary_values():
    result = tw("grid grid-cols-[1fr,auto] p-4", "p-8")
    assert result == "grid p-8 grid-cols-[1fr,auto]"


def test_multiple_conflicts():
    result = tw(
        "block sm:flex lg:grid p-4 bg-red-500",
        "hidden md:block sm:grid p-8 bg-blue-500",
    )
    assert "hidden" in result
    assert "sm:grid" in result
    assert "p-8" in result
    assert "bg-blue-500" in result
