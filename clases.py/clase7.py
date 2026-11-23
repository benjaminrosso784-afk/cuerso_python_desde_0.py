tiene_invitacion = True
tiene_entrada = True
esta_bloqueada = True
puede_entrar = (tiene_entrada or tiene_invitacion) and esta_bloqueada
print(puede_entrar)