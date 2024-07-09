from googletrans import Translator
import random
import sys
from pyfiglet import Figlet

def main():

    figlet = Figlet()
    selected_font = 'starwars'
    figlet.setFont(font=selected_font)
    print(figlet.renderText('Olootu'))
    print("E ka a bo! \n")
    while True:
        print("1. Translation to Yoruba")
        print("2. Word Game")
        print("3. OWe ati Itumo(Proverbs and meaning)")
        print("4. Exit")
        try:
            user_put = int(input(">>>: "))
            if user_put == 1:
                while True:
                    user_input = input("English: ")
                    gan = function_yoruba(user_input)
                    print("Yoruba: ", gan)
                    if user_input.lower()== "exit":  
                     break
            elif user_put == 2:
                score = function_2()
                while True:
                    print("Game over! Your score is:", score, "out of 10 \n")
                    print("Play Again? Yes/No")
                    play = input(">> ")
                    if play.lower() =="yes":
                        score = function_2()
                    elif play.lower() == "no":
                        break
            elif int(user_put) == 3:
                while True:
                    user_in = input()
                    if user_in.lower() == "exit":
                        break
                    proverb, translation, meaning = proverbs()
                    print(f"Yoruba Proverb: {proverb}\nTranslation: {translation}\nMeaning: {meaning}")
            elif user_put == 4:
                sys.exit("Exiting the program. O daabo!")

        except ValueError:
            print("Invalid input")

def function_yoruba(word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest='yo')
    return translation.text

def function_2():
    yoruba_dict = {
        'ọjọ': 'day', 'iroyin': 'news', 'omode': 'child', 'baba': 'father', 'iya': 'mother',
        'orukọ': 'name', 'ounjẹ': 'food', 'ipo': 'position', 'owo': 'money', 'ile-iwe': 'school',
        'Ade': 'crown', 'irun': 'hair', 'ọwọ': 'hand', 'ẹ́hìn': 'behind', 'àgbà': 'old',
        'Àṣà': 'culture', 'Àṣàájú': 'leader', 'Àfiyèsí': 'observation', 'Àrídájú': 'confirmation',
        'itúmọ̀': 'meaning', 'Àjọṣe': 'cooperation', 'Àkóso': 'administration', 'Òfin': 'law', 'Àjọṣe-pọ̀': 'collaboration',
        'Àbájáde': 'result', 'Ìyàlẹ̀nu': 'surprise', 'Ìtàn': 'history', 'Ìgbàgbó': 'belief',
        'Àgbẹ̀yẹ̀wò': 'review', 'Ìṣirò': 'calculation', 'Àgbẹ̀dẹ́': 'blacksmith', 'Ìdàjọ́': 'judgment',
        'Ìṣirò': 'calculation', 'Òpó': 'widow', 'Ìṣòro': 'difficulty', 'Àkíyèsí': 'notice', 'Ìṣàkóso': 'governance',
        'Ìdúróṣinṣin': 'stability', 'Ìmọ̀': 'knowledge'
    }

    score = 0
    keys = list(yoruba_dict.keys())  # Create a list of the keys

    for _ in range(10):  # Play the game 10 times
        random_key = random.choice(keys)  # Choose a random key
        correct_answer = yoruba_dict[random_key]
        user_answer = input("What is " + random_key + "?: ").lower()
        keys.remove(random_key)  # Remove the key from the list to prevent repetition

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Try again")
            user_answer = input("What is " + random_key + "?: ").lower()
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print("Wrong! The correct answer is:", correct_answer)

    return score


def proverbs():
    yoruba_proverbs = {
        "Adìẹ funfun kò mọ ara rẹ̀lágbà": {
            "translation": "The white chicken does not realise its age",
            "meaning": "Respect yourself"
        },
        "Ọbẹ̀ kìí gbé inú àgbà mì": {
            "translation": "The soup does not move round in an elder's belly",
            "meaning": "You should be able to keep secrets"
        },
        "À ń pe gbẹ́nàgbẹ́nà ẹyẹ àkókó ń yọjú": {
            "translation": "A sculptor is summoned and the woodpecker shows up",
            "meaning": "Never think too highly of yourself"
        },
        "Díẹ̀ díẹ̀ nimú ẹlẹ́dẹ̀ẹ́ fi ń wọgbà": {
            "translation": "Little by little is how the pig's nose enters the yard",
            "meaning": "Attend to a small problem before it becomes uncontrollable"
        },
        "Ilé ọba tójó ẹwà ló bùsi": {
            "translation": "The king's palace that got burnt added beauty to it",
            "meaning": "Every cloud has a silver lining"
        },
        "Bami na omo mi o de inu olomo": {
            "translation": "A parent who wants you to beat their child doesn't mean it",
            "meaning": "Don't go around disciplining other people's kids"
        },
        "Iku npa alagemo to yole nrin, ambelete opolo to ngbe ra re sonle": {
            "translation": "A chameleon that approaches with caution dies, talk more of a toad that slams its body with every step.",
            "meaning": "Tread carefully"
        },
        "Omi titun ti ru, eja titun ti wonu e": {
            "translation": "It's a new season, a new era",
            "meaning": "It is a new dawn"
        },
        "Eni bama m'obo akoko se bi obo": {
            "translation": "To catch a monkey, you must do like a monkey",
            "meaning": "To get something from people, you need to come down to their level"
        },
        "Gbogbo alangba lo d'anu dele, a ko mo eyi t'inu nrun": {
            "translation": "All lizards lie flat on their stomach and it is difficult to determine which has a stomach ache",
            "meaning": "Everyone looks the same on the outside but everyone has problems that are invisible to outsiders"
        },
        "Ile la ti n ko eso re ode": {
            "translation": "Charity begins at Home",
            "meaning": "A man cannot give what he does not have good or bad behavior is a reflection of one's background"
        },
        "A pę ko to jęun, ki ję ibaję": {
            "translation": "The person that eat late, will not eat spoiled food",
            "meaning": "It is more profitable to exercise patience while seeking a durable solution, in difficult situations than to hastily accept an ill-conceived/prepared solution"
        },
        "Eewu bę loko Longę, Longę fun ara rę eewu ni": {
            "translation": "There is danger at Longę's farm (Longę is a name of a Yoruba Legend), Longę himself is danger",
            "meaning": "You should be extremely careful of situations that have a past history of danger"
        },
        "Bí abá so òkò sójà ará ilé eni ní bá": {
            "translation": "He who throws a stone in the market will hit his relative",
            "meaning": "Be careful what you do unto others it may return towards you or someone close to you"
        },
        "A ki binu aatan ka dale sigbee": {
            "translation": "One does not get angry with the rubbish dump and discard one's rubbish into the bush",
            "meaning": "One should not act in unreasonable and harmful ways because of anger"
        },
        "A ki binu ori ka fi fila de ibadi": {
            "translation": "One does not get angry with one's head and therefore wears one's cap on the buttocks",
            "meaning": "Do not cut your nose to spite your face"
        },
        "Igi gogoro ma gun mi loju, ati okere laati wo": {
            "translation": "One avoids danger at the early stage",
            "meaning": ""
        }
    }
    proverb, details = random.choice(list(yoruba_proverbs.items()))
    translation = details["translation"]
    meaning = details["meaning"]
    return proverb, translation, meaning



if __name__ == "__main__":
    main()
