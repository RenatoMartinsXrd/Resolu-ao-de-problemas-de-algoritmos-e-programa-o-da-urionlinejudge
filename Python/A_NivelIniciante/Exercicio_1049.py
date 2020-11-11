# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1049
class animal():
    def __init__(self,vertebra,tipo,comida):
        self.vertebra = vertebra
        self.tipo = tipo
        self.comida = comida
    def animal(self):
        if self.vertebra=="vertebrado":
            if tipo=="ave":
                if self.comida == "carnivoro":
                    return "aguia"
                elif self.comida == "onivoro":
                    return "pomba"
            elif self.tipo=="mamifero":
                if self.comida == "onivoro":
                    return "homem"
                elif self.comida == "herbivoro":
                    return "vaca"            
        elif self.vertebra == "invertebrado":
            if self.tipo=="inseto":
                if self.comida == "hematofago":
                    return "pulga"
                elif self.comida == "herbivoro":
                    return "lagarta"
            elif self.tipo=="anelideo":
                if self.comida == "hematofago":
                    return "sanguessuga"
                elif self.comida == "onivoro":
                    return "minhoca"

vertebra = raw_input()
tipo = raw_input()
comida = raw_input()
animalzin = animal(vertebra,tipo,comida)
print(animalzin.animal())
        
