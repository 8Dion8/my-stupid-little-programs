#массив из букв слова
word = list('javascript')
#массив из черточек количества букв
guessed = ['-' for i in range(len(word))]
#основной цикл
while True:
    #ввод буквы от пользователя
    letter = input('Enter your letter\n')
    #если буква есть в слове...
    if letter in word:
        #...то перебираем все буквы в слове
        for i in range(len(word)):
            #если буквы совпадают...
            if word[i] == letter:
                #...то меняем черточку на букву
                guessed[i] = letter

        #если не осталось черточек...
        if '-' not in guessed:
            #...то ты выиграл
            print('You won')
            break
    #печатаем массив тире как строку
    print("".join(guessed))