from hash import HashTable

class Celula:
    def __init__(self, id, largura, altura, x, linha):
        self.id = id
        self.largura = largura
        self.altura = altura
        self.x = x
        self.linha = linha

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