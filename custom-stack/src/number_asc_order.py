class NumberAscOrder:
    def sort(self, custom_stack) -> list:
        """
        Recebe uma CustomStack contendo os números sorteados,
        coleta os números e retorna uma lista ordenada ascendentemente.
        """
        if custom_stack is None:
            raise ValueError("custom_stack não pode ser nulo")

        numbers = []
        while not custom_stack.is_empty():
            numbers.append(custom_stack.pop())

        return sorted(numbers)

