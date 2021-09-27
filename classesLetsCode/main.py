class Comida:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

    def apresentacao(self):
        print(f'Receita de {self.nome}.')

    def promocao(self, desconto):
        self.preco -= desconto
        print(f'O preço com desconto é R$ {self.preco}.')


hamburguer = Comida('cheeseburguer', 20, ['pão', 'carne', 'queijo'])
pizza = Comida('pizza', 40, ['massa', 'molho', 'queijo'])

print(f'O nome dessa comida é: {hamburguer.nome}.')
print(f'O nome dessa comida é: {pizza.nome}.')

print()

hamburguer.apresentacao()
pizza.apresentacao()

print()

Comida.apresentacao(hamburguer)
Comida.apresentacao(pizza)

hamburguer.promocao(12)
