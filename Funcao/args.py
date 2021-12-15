def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total


def resultado_final(**kwargs):
    status = 'APROVADO(A)!!!' if kwargs['nota'] >= 7 else 'Reprovado'
    return f'{kwargs["nome"]} foi {status}'