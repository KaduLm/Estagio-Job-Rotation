# 3* questão
import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

dias_com_faturamento = [f for f in faturamento if f > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
dias_acima_da_media = sum(1 for f in dias_com_faturamento if f > media_mensal)
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
