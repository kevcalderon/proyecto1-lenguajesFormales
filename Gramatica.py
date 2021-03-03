class Gramatica:
    def __init__(self, nombre, noTerminal, terminales, noTerminalInicial, producciones):
        self.nombre = nombre
        self.noTerminal = noTerminal
        self.terminales = terminales
        self.noTerminalInicial = noTerminalInicial
        self.producciones = producciones