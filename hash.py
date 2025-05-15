class Nodo:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class HashTable:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.tabela = [None] * capacidade

    def hash(self, chave):
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        index = self.hash(chave)

        if self.tabela[index] is None:
            self.tabela[index] = Nodo(chave, valor)
            self.tamanho += 1
        else:
            atual = self.tabela[index]
            while atual is not None:
                if atual.chave == chave:
                    atual.valor = valor
                    return
                atual = atual.proximo
            novo_nodo = Nodo(chave, valor)
            novo_nodo.proximo = self.tabela[index]
            self.tabela[index] = novo_nodo
            self.tamanho += 1

    def buscar(self, chave):
        index = self.hash(chave)
        atual = self.tabela[index]
        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        raise KeyError(chave)

    def remover(self, chave):
        index = self.hash(chave)

        anterior = None
        atual = self.tabela[index]

        while atual is not None:
            if atual.chave == chave:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.tabela[index] = atual.proximo
                self.tamanho -= 1
                return
            anterior = atual
            atual = atual.proximo
        raise KeyError(chave)
