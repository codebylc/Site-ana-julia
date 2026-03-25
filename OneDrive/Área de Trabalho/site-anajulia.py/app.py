from flask import Flask, render_template
import random

app = Flask(__name__)

def gerar_os_motivos():
    # Seus 10 motivos especiais
    reais = [
        "O seu sorriso é meu lugar favorito.",
        "A forma como você cuida de mim.",
        "Sua paciência infinita.",
        "O brilho dos seus olhos quando está feliz.",
        "Você é minha melhor amiga.",
        "A paz que você me traz.",
        "O seu cheirinho.",
        "Seu apoio nos meus sonhos.",
        "A sorte de ter você na minha vida.",
        "Eu amo ser o dono do seu coração."
    ]
    
    # As 50 variações para completar os 1000
    bases = [
        "pelo jeito que você me olha quando está distraída.",
        "por cada detalhe único que só você tem.",
        "por me fazer sorrir mesmo nos dias mais difíceis.",
        "porque o meu mundo ganha cor quando você chega.",
        "pelos planos que fazemos para o nosso futuro juntos.",
        "pela nossa cumplicidade que não precisa de palavras.",
        "porque eu amo cada versão sua, das mais doces às mais bravas.",
        "por ser o meu porto seguro e meu lugar de paz.",
        "pela sua risada que é a minha música favorita.",
        "por me entender apenas com um olhar cúmplice.",
        "pelo carinho que você coloca em cada pequena coisa.",
        "pela sua inteligência que me admira todos os dias.",
        "pelo seu abraço que tem o poder de curar qualquer dor.",
        "por me aceitar exatamente como eu sou.",
        "por cada conversa que temos até o sol nascer.",
        "porque você é o melhor presente que a vida me deu.",
        "pelo seu coração gigante que transborda bondade.",
        "pela forma como você me faz sentir especial.",
        "simplesmente por você existir e estar na minha vida.",
        "pela sua determinação em conquistar os seus sonhos.",
        "por me fazer acreditar no amor verdadeiro.",
        "pelo toque das suas mãos que me acalma.",
        "por ser minha melhor amiga e namorada ao mesmo tempo.",
        "pelas mensagens de 'bom dia' que mudam o meu humor.",
        "por cada vez que você está do meu lado.",
        "pela forma como você fica linda até acordando.",
        "pelas nossas piadas internas que só a gente entende.",
        "por me ensinar a ser uma pessoa melhor.",
        "pela sua paciência quando eu sou difícil.",
        "por transformar momentos simples em memórias.",
        "pelo seu cheiro que fica na minha memória.",
        "porque ao seu lado posso enfrentar qualquer coisa.",
        "pela sua voz que me traz paz imediata.",
        "por ser a pessoa mais linda que já conheci.",
        "pela forma como você cuida de mim sem eu pedir.",
        "por me motivar a nunca desistir.",
        "pelas viagens que ainda vamos fazer.",
        "por cada beijo que parece o primeiro.",
        "pela segurança que sinto de mãos dadas com você.",
        "por ser o motivo do meu sorriso mais sincero.",
        "porque você é minha pessoa favorita no universo.",
        "pela sua força que me inspira.",
        "por cada detalhe do seu rosto que amo decorar.",
        "pela nossa história, minha favorita de contar.",
        "por você ser o meu sonho realizado.",
        "pela luz que você emana por onde passa.",
        "por me fazer sentir em casa em qualquer lugar.",
        "pela sua generosidade e cuidado.",
        "por ser meu primeiro e último pensamento.",
        "porque amar você é a coisa mais natural do mundo."
    ]
    
    lista_final = []
    
    # 1. Numerando os 10 motivos reais
    for i in range(len(reais)):
        numero = i + 1
        lista_final.append(f"Motivo {numero}: {reais[i]}")
    
    # 2. Gerando do 11 ao 1000 com sorteio
    for i in range(11, 1001):
        frase_sorteada = random.choice(bases)
        lista_final.append(f"Motivo {i}: Eu te amo {frase_sorteada}")
        
    return lista_final

@app.route('/')
def index():
    motivos = gerar_os_motivos()
    return render_template('index.html', motivos=motivos)

if __name__ == '__main__':
    app.run(debug=True)