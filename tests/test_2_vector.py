from itertools import tee
from math import isnan

from hypothesis import assume, given, strategies as st

from hypothesis_demo.vector import Vector


# Two identical vectors are equal
# Adding vectors Vector(x1, x2, x3, ...)+Vector(y1, y2, y3, ...) of equal length
#        produces a new vector Vector(x1+y1, x2+y2, x3+y3, ...)
# Vector is true if any of it's components is != 0
# Vector is false if all of it's components are == 0
# Length (magnitude) of a unit vector is always 1
# Length (magnitude) of a zero vector is always 0
# Vector(x1, x2, x3, ...) * N is Vector(x1 * N, x2 * N, x3 * N, ...)
# Vector(x1, x2, x3, ...) * Vector(y1, y2, y3, ...) is Vector(x1 * y1, x2 * y2, x3 * y3, ...)
# Vector(x1, x2, x3, ...) @ Vector(y1, y2, y3, ...) is x1*y1 + x2*y2 + x3*y3 + ...
# Slice [:] of a vector is equal to the vector
# Slice [x:y] of a vector is still a vector
# Slice [n] of a vector is a single value


@given(st.iterables(st.floats()))
def test_two_identical_vectors_are_equal(components):
    components_left, components_right = tee(components)
    assume(not any(isnan(x) for x in components))
    assert Vector(components_left) == Vector(components_right)


same_len_lists = st.integers(min_value=1, max_value=100).flatmap(
    lambda n: st.lists(
        st.lists(st.integers(), min_size=n, max_size=n), min_size=2, max_size=2
    )
)


@given(same_len_lists)
def test_adding_two_vectors(components):
    components_left, components_right = components
    assert Vector(components_left) + Vector(components_right) == Vector(
        a + b for a, b in zip(components_left, components_right)
    )


@given(st.lists(st.just(0)))
def test_vector_is_false(components):
    assert bool(Vector(components)) is False


@given(st.lists(st.integers()))
def test_vector_is_true(components):
    assume(any(x for x in components))
    assert bool(Vector(components)) is True


@st.composite
def unit_vector_list(draw, elements=st.just(0)):
    xs = draw(st.lists(elements, min_size=1))
    i = draw(st.integers(min_value=0, max_value=len(xs) - 1))
    xs[i] = 1
    return xs


@given(unit_vector_list())
def test_unit_vector_length_is_1(components):
    assert abs(Vector(components)) == 1


@given(st.lists(st.just(0)))
def test_zero_vector_length_is_0(components):
    assert abs(Vector(components)) == 0


@given(st.lists(st.integers()), st.integers())
def test_vector_times_number(components, number):
    assert Vector(components) * number == Vector(comp * number for comp in components)


@given(same_len_lists)
def test_vector_times_vector(components):
    components_left, components_right = components
    assert Vector(components_left) * Vector(components_right) == Vector(
        a * b for a, b in zip(components_left, components_right)
    )


@given(same_len_lists)
def test_vector_dot_vector(components):
    components_left, components_right = components
    assert Vector(components_left) @ Vector(components_right) == sum(
        a * b for a, b in zip(components_left, components_right)
    )


@given(st.lists(st.integers()))
def test_vector_full_slice(components):
    assert Vector(components)[:] == Vector(components)


@st.composite
def vector_slice(draw):
    length = draw(st.integers(min_value=0, max_value=100))
    comp_slice = draw(st.slices(size=length))
    components = draw(st.lists(st.integers(), min_size=length+1, max_size=length+1))
    return components, comp_slice


@given(vector_slice())
def test_vector_slice_is_vector(args):
    components, comp_slice = args
    assert Vector(components)[comp_slice] == Vector(components[comp_slice])


@st.composite
def vector_element(draw):
    length = draw(st.integers(min_value=0, max_value=100))
    index = draw(st.integers(min_value=0, max_value=length))
    components = draw(st.lists(st.integers(), min_size=length + 1, max_size=length + 1))
    return components, index


@given(vector_element())
def test_vector_slice_single_element(args):
    components, index = args
    assert Vector(components)[index] == components[index]
