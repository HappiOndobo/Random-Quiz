questions = ["what is the capital of France? ","what is the capital of France? ",
             "what is the capital of France? ","what is the capital of France? ",
             "what is the capital of France? ","what is the capital of France? ",
             "what is the capital of France? ","what is the capital of France? ",
             "what is the capital of France? ","what is the capital of France? ",
             "what is the capital of France? ","what is the capital of France? ",
             "what is the capital of France? ","what is the capital of France? "]

Answers = ['Paris']*13

num_rigth = 0
for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower() == Answers[i].lower():
        num_rigth = num_rigth + 1
    else:
        print('wrong. The anwser is', Answers[i])
    print("**********************************************************************")
    print('Youhave', num_rigth, 'right out of', i+1, 'Questions.')