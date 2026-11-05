import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException

def test_push_one_element_in_stack():
    element_value = 5.0
    cut = CustomStack(5)
    cut.push(element_value)
    
    assert cut.is_empty() is False
    assert cut.top() == element_value
    assert cut.size() == 1

def test_stack_is_empty_on_creation():
    cut = CustomStack(5)
    assert cut.is_empty() is True
    assert cut.size() == 0

def test_push_until_full_raises_stack_full_exception():
    cut = CustomStack(2)
    cut.push(10)
    cut.push(20)
    
    with pytest.raises(StackFullException):
        cut.push(30)

def test_pop_element_success():
    cut = CustomStack(3)
    cut.push(10)
    cut.push(20)
    
    popped = cut.pop()
    assert popped == 20
    assert cut.size() == 1
    assert cut.top() == 10

def test_pop_empty_stack_raises_stack_empty_exception():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.pop()

def test_top_empty_stack_raises_stack_empty_exception():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.top()
