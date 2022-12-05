from operator import truediv
from django import template

register = template.library()

@register.filter(name="remover")
def remover(texto, r):
    texto.replace(r, "")

@register.filter(name="verificargrupo")
def verificargrupo(usuario, nome_do_grupo):
    if(usuario.groups.filter(name = nome_do_grupo)):
        return true
    else:
        return false


