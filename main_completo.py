class Celula:
    def __init__(self, id, largura, altura, x, linha):
        self.id = id
        self.largura = largura
        self.altura = altura
        self.x = x
        self.linha = linha

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

class Circuito:
    def __init__(self, linhas=145, largura_linha=2500, altura_linha=504):
        self.linhas = [[] for _ in range(linhas)]
        self.largura_linha = largura_linha
        self.altura_linha = altura_linha
        self.celulas = HashTable(12028)

    def inserir_celula(self, id, largura, altura):
        for idx, linha in enumerate(self.linhas):
            x = 0
            for i, celula in enumerate(linha):
                if x + largura <= celula.x:
                    nova_celula = Celula(id, largura, altura, x, idx)
                    linha.insert(i, nova_celula)
                    self.celulas.inserir(id, nova_celula)
                    return
                x = celula.x + celula.largura
            
            if x + largura <= self.largura_linha:
                nova_celula = Celula(id, largura, altura, x, idx)
                linha.append(nova_celula)
                self.celulas.inserir(id, nova_celula)
                return

    def buscar_celula(self, id):
        try:
            celula = self.celulas.buscar(id)
            return (celula.linha, celula.x)
        except KeyError:
            return None

    def remover_celula(self, id):
        try:
            celula = self.celulas.buscar(id)
            self.linhas[celula.linha].remove(celula)
            self.celulas.remover(id)
            return True
        except KeyError:
            return False

    def carregar_arquivo(self, arquivo):
        with open(arquivo) as f:
            for linha in f:
                partes = linha.strip().split()
                if len(partes) == 3 and partes[0].startswith('a'):
                    id, largura, altura = partes
                    self.inserir_celula(id, float(largura), float(altura))

if __name__ == "__main__":
    circuito = Circuito()
    circuito.carregar_arquivo("bookshelf.nodes")
    print(circuito.buscar_celula("a0"))
    print(circuito.buscar_celula("a1"))
    print(circuito.buscar_celula("a100"))
    print(circuito.buscar_celula("a1000"))
    print(circuito.buscar_celula("a10000"))
    print(circuito.buscar_celula("a10001"))
    print(circuito.buscar_celula("a10002"))
    print(circuito.buscar_celula("a10003"))
    print(circuito.buscar_celula("a10004"))
    print(circuito.buscar_celula("a10005"))
    print(circuito.buscar_celula("a10006"))
    print(circuito.buscar_celula("a10007"))
    print(circuito.buscar_celula("a10008"))
    print(circuito.buscar_celula("a10009"))
    print(circuito.buscar_celula("a10010"))
    print(circuito.buscar_celula("a10011"))
    print(circuito.buscar_celula("a10013"))

    

