import emoji
n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
n3 = float(input('Digite a terceira nota do aluno:'))

media = (n1 + n2 + n3) / 3

print('A media do aluno é {:.2f}' .format(media))

if media >= 7:
    print(emoji.emojize('Voce passou! :sunglasses:', language='alias'))
else:
    print(emoji.emojize('Voce reprovou! :cry:', language='alias'))
