from Question import Question

question_prompts = [
    "how many letters inside DNA molecule?\n(a) 3\n(b) 4\n(c) 6\n ==> ",
    "where are DNA in animal cells?\n(a) Core\n(b) Mitochondria\n(c) Both\n ==> ",
    "how many caracters inside ASSCI encoding?\n(a) 204\n(b) 100\n(c) 255\n ==> "
]

questions_list = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions_list:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got "+ str(score) + "/"+ str(len(questions_list))+" Correct")

run_test(questions_list)