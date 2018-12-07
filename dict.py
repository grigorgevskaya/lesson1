answers = {
"Как дела?":"Хорошо","Что делаешь?": "Программирую", 
"Получается?":"Да", "Закончишь, пойдем гулять?":"Да"
}

def get_answer(question, answers):
    return answers.get(question)

    try:
        return (answers)
    except KeyboardInterrupt: 
        return "C ума сошли?"    


def ask_user(answers):
    
 
    while True:
        user_input = input("Привет:")
        answer = get_answer(user_input, answers)
        print(answer)
      
    
        if user_input == "Закончишь, пойдем гулять?":
            break 
    
ask_user(answers) 
        