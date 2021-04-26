from flask import Flask
import request

app = Flask(__name__)

game = [
    {
        'id': 1,
        'name': 'Overwatch',
        'describe': 'Overwatch é um jogo de tiro em equipe que conta com um elenco diversificado de heróis poderosíssimos. Viaje pelo mundo, monte uma equipe e dispute objetivos em combates 6v6 de tirar o fôlego.',
        'link_image': 'https://upload.wikimedia.org/wikipedia/pt/b/bf/Overwatch_logo.jpg',
        'valor': 'R$ 160,00',
        'plataforma':'PC/PS4/XBoxOne/Switch' 
    },
    {
        'id': 2,
        'name': 'Spider-Man',
        'describe': 'Spider-Man é um jogo eletrônico de ação-aventura desenvolvido pela Insomniac Games e publicado pela Sony Interactive Entertainment. É baseado nos personagens, mitologia e adaptações em outras mídias do super-herói de histórias em quadrinhos Homem-Aranha da Marvel Comics, tendo sido lançado exclusivamente para PlayStation 4 em 7 de setembro de 2018. Na história, o criminoso super-humano Senhor Negativo organiza um plano para se vingar do prefeito Norman Osborn e assumir o controle do submundo criminal de Nova Iorque. O Homem-Aranha precisa proteger a cidade assim que o Senhor Negativo ameaça lançar um vírus mortal por toda a área, ao mesmo tempo que é forçado a lidar com seus problemas pessoais como Peter Parker.',
        'link_image': 'https://upload.wikimedia.org/wikipedia/pt/7/78/Spider-Man_jogo_2018_capa.png'
        'valor': 'R$ 116,90',
        'plataforma':'PS4' 
    },
    {
        'id': 3,
        'name': 'God Of War',
        'describe': 'É um novo começo para Kratos. Vivendo como um homem longe da sombra dos deuses, ele se aventura pelas selvagens florestas nórdicas com seu filho Atreus, lutando para cumprir uma missão profundamente pessoal. O Santa Monica Studio e o diretor de criação Cory Barlog lançam um novo começo para um dos personagens mais conhecidos dos jogos. Vivendo como um homem, fora da sombra dos deuses, Kratos deve se adaptar a terras desconhecidas, ameaças inesperadas e a uma segunda oportunidade de ser pai. Junto ao seu filho, Atreus, os dois vão se aventurar pelas selvagens florestas nórdicas e lutar para cumprir uma missão profundamente pessoal.',
        'link_image': 'https://upload.wikimedia.org/wikipedia/pt/8/82/God_of_War_2018_capa.png',
        'valor': 'R$ 69,90',
        'plataforma':'PS4' 
    },
    {
        'id': 4,
        'name': 'Ghost of Tsushima',
        'describe': 'No final do século XIII, o império mongol devastou nações inteiras durante sua campanha para conquistar o Oriente. A Ilha de Tsushima é tudo o que está entre o Japão continental e uma enorme frota invasora mongol comandada pelo implacável e sagaz general Khotun Khan. À medida que a ilha queima na esteira da primeira onda do assalto mongol, o guerreiro samurai Jin Sakai mantém-se como um dos último membros sobreviventes de seu clã. Ele está decidido a proteger seu povo e recuperar seu lar, independente do que aconteça, custe o que custar. Será preciso romper com as tradições que o tornaram um guerreiro para forjar um novo caminho do Fantasma e declarar uma guerra incomum pela liberdade de Tsushima.',
        'link_image': 'https://upload.wikimedia.org/wikipedia/pt/thumb/d/dc/Ghost_of_Tsushima_capa.png/270px-Ghost_of_Tsushima_capa.png',
        'valor': 'R$ 249,00',
        'plataforma':'PS4' 
    },
    {
        'id': 5,
        'name': 'Tom Clancy s Splinter Cell: Double Agent',
        'describe': 'Vivencie a tensão incessante e os dilemas da vida de um agente duplo. Minta. Mate. Prejudique. Traia. Tudo para proteger os inocentes. Até onde você iria para ganhar a confiança do inimigo? Como o agente secreto Sam Fisher, você deve se infiltrar num grupo terrorista cruel e destruí-lo internamente. Você precisará ponderar muito bem as consequências dos seus atos. Mate terroristas demais e estragará seu disfarce. Hesite e milhões morrerão. Faça o que for preciso para completar a missão, mas procure sobreviver.',
        'link_image': 'https://store.ubi.com/dw/image/v2/ABBS_PRD/on/demandware.static/-/Sites-masterCatalog/default/dwb3dccb35/images/large/56c4948a88a7e300458b482c.jpg?sw=341&sh=450&sm=fit',
        'valor': 'R$ 36,00',
        'plataforma':'XBOX/PS2/PS3/PC' 
    },
    {
        'id': 6,
        'name': 'God of War III',
        'describe': 'Kratos está devolta, ainda com a vingança pulsando forte em suas veias. O Olimpo e seus deuses é o seu alvo, não importa o preço que o Deus da Guerra irá pagar. Neste terceiro e épico capítulo você irá controlar Kratos através de batalhas celestiais contra os deuses mais poderosos de todo o Olimpo – inclusive voltará ao inferno e acertar as contas com seu pai colossal e poderoso, Kronos. Deuses como Hermes e Hades não serão páreo para seu poder, os olhos ardentes daquele que busca vingança que nem a mais cruel das mortes pode deter. Enfrente desafios arrasadores e enfrente monstros poderosos como a Quimera, o Cérberus e muitos outros seres místicos que estão ali apenas para acabar com sua existência. Não pare por nada até enfrentar o deus dos deuses: Zeus, e acabar com isso de uma vez por todas.',
        'link_image': 'https://s3.amazonaws.com/comparegame/thumbnails/41421/large.jpg',
        'valor': 'R$ 50,00',
        'plataforma':'PS3/PS4' 
    },
    {
        'id': 7,
        'name': 'Watch Dogs 2',
        'describe': 'Junte-se ao Dedsec, um grupo notório de hackers, para executar o maior hack da história; Derrube o ctOS 2.0, um sistema operacional invasivo que está sendo usado por um gênio do crime para monitorar e manipular os cidadãos em uma escala massiva.',
        'link_image': 'https://s3.amazonaws.com/comparegame/thumbnails/42209/large.jpg',
        'valor': 'R$ 60,00',
        'plataforma':'PC/PS4/XBoxOne' 
    },
    {
        'id': 8,
        'name': 'Batman arkham city',
        'describe': 'Batman: Arkham City é um jogo eletrônico de Ação-Aventura e Stealth, baseado na série de quadrinhos Batman da DC Comics. O jogo é distribuído para: PlayStation 3, Xbox 360 e Microsoft Windows. Foi desenvolvido pela Rocksteady Studios e foi publicado pela Warner Bros. Interactive Entertainment e DC Entertainment.',
        'link_image': 'https://upload.wikimedia.org/wikipedia/pt/thumb/f/f0/Batman_arkham_city_logo.jpg/200px-Batman_arkham_city_logo.jpg',
        'valor': 'R$ 31,00',
        'plataforma':'Xbox/PC/WiiU' 
    },
    }

]

@app.route('/game', methods=['GET'])
def home():
    return jsonify(game), 200


@app.route('/game/<string:describe>', methods=['GET'])
def gameper_plataforma(plataforma):
    game_per_plataforma = [dev for dev in game if dev['plataforma'] == describe]
    return jsonify(game_per_plataforma), 200


@app.route('/game/<int:id>', methods=['PUT'])
def change_plataforma(id):
    for dev in game:
        if dev['id'] == id:
            dev['plataforma'] = request.get_json().get('plataforma')

            return jsonify(dev), 200

    return jsonify({'error': 'dev not found'}), 404


@app.route('/game/<int:id>', methods=['GET'])
def game_per_id(id):
    for dev in game:
        if dev['id'] == id:
            return jsonify(dev), 200

    return jsonify({'error': 'not found'}), 404


@app.route('/game', methods=['POST'])
def save_dev():
    data = request.get_json()
    game.append(data)
    
    return jsonify(data), 201


@app.route('/game/<int:id>', methods=['DELETE'])
def remove_dev(id):
    index = id - 1
    del game[index]

    return jsonify({'message': 'Dev is no longer alive'}), 200


if __name__ == '__main__':
    app.run(debug=True)