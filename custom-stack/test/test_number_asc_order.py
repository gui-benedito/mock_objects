import pytest
from unittest.mock import Mock
from src.number_asc_order import NumberAscOrder
from src.custom_stack_class import CustomStack

class TestNumberAscOrder:

    def test_sort_six_random_drawn_numbers_using_mock(self):
        # Cenário 1: Pilha de 6 posições, contendo os 6 números sorteados (aleatoriamente)
        # Usando Mock para simular a CustomStack e isolar a unidade NumberAscOrder
        drawn_numbers = [53, 10, 42, 5, 27, 35]
        
        mock_stack = Mock(spec=CustomStack)
        
        # Simula is_empty retornando False por 6 vezes e True no final
        mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]
        # Simula o pop() desempilhando na ordem (LIFO)
        mock_stack.pop.side_effect = list(reversed(drawn_numbers))
        
        order_service = NumberAscOrder()
        result = order_service.sort(mock_stack)
        
        # Verificações
        assert result == [5, 10, 27, 35, 42, 53]
        assert mock_stack.pop.call_count == 6
        assert mock_stack.is_empty.call_count == 7

    def test_sort_empty_stack_of_six_positions_using_mock(self):
        # Cenário 2: Pilha de 6 posições, vazia
        mock_stack = Mock(spec=CustomStack)
        mock_stack.is_empty.return_value = True
        
        order_service = NumberAscOrder()
        result = order_service.sort(mock_stack)
        
        # Verificações
        assert result == []
        mock_stack.pop.assert_not_called()
        mock_stack.is_empty.assert_called_once()

    def test_sort_six_random_drawn_numbers_with_real_stack(self):
        # Cenário complementar de integração: Pilha real de 6 posições preenchida
        stack = CustomStack(6)
        drawn_numbers = [53, 10, 42, 5, 27, 35]
        for num in drawn_numbers:
            stack.push(num)

        order_service = NumberAscOrder()
        result = order_service.sort(stack)

        assert result == [5, 10, 27, 35, 42, 53]
        assert stack.is_empty() is True

    def test_sort_empty_real_stack(self):
        # Cenário complementar de integração: Pilha real de 6 posições vazia
        stack = CustomStack(6)
        order_service = NumberAscOrder()
        result = order_service.sort(stack)

        assert result == []
        assert stack.is_empty() is True

    def test_sort_none_stack_raises_value_error(self):
        # Tratamento de parâmetro inválido
        order_service = NumberAscOrder()
        with pytest.raises(ValueError):
            order_service.sort(None)

