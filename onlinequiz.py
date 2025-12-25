from tkinter import *
from random import randint,choice

root = Tk()
root.geometry("600x500")
root.title("maths quiz")



question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()

#generateque
def generateque():

    global questionLabel

    questionNumber.set(questionNumber.get() + 1)

    number1= randint(1, 10)
    number2= randint(1, 10)

    operator = choice(['+' ,'-','*','/'])

    question.set( str(number1) + operator + str(number2))
    answer.set(eval(question.get()))

    if questionLabel:
        questionLabel.destroy()
    questionLabel= Label(root, text =f"Question : {question.get()}", font= ('arial',20))
    questionLabel.grid(row=2, column=0)





#checkingAnswer
def checkanswer():
    global scoreLabel

    if questionNumber.get() > 10 :
        return

    

    global resultLabel


    if resultLabel:
        resultLabel.destroy()
    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 1)
        print("correct")

        resultLabel = Label(root, text= "correct", font=('arial',20),fg="green")
        resultLabel.grid(row=4,column=0)
#score
        scoreLabel = Label(root, text= score.get(), font=('arial',20),fg= "black")
        scoreLabel.grid(row=5,column=0)

    
    else:
        print("your answer is incorrect")
        resultLabel = Label(root, text= "incorrect", font=('arial',20),fg= "red")
        resultLabel.grid(row=4,column=0)


    if questionNumber.get() == 10:
        scoreLabel.destroy()

        scoreLabel = Label(root, text=f"final score : {score.get()}" , font=('arial',20),fg= "black")
        scoreLabel.grid(row=5,column=0)
    else:
        generateque()

def restart():

    global scoreLabel
    scoreLabel.destroy()
    score.set(0)
    questionNumber.set(0)
    generateque()

    scoreLabel = Label(root, text= score.get(), font=('arial',20),fg= "black")
    scoreLabel.grid(row=5,column=0)


#gui
#question

headingLabel = Label(root, text= "Maths quiz",font =('arial', 25) )
headingLabel.grid(row=0,column=0)

questionScale = Scale(root, from_=0, to=10, orient= HORIZONTAL, length= 400, variable= questionNumber )
questionScale.grid(row=1,column= 0)

completeQuestionLabel = Label(root, text = "10th question", font= ('arial',10), fg= "purple")
completeQuestionLabel.grid(row=1, column=1)

questionLabel= Label(root, text =question.get(), font= ('arial',20))
questionLabel.grid(row=2, column=0)

#answer

answerEntry = Entry(root,textvariable= givenAnswer, font=('arial',20), width= 25)
answerEntry.grid(row=3,column=0)

#submit

submitButton = Button(root, text ="Submit", bg="#4CAF50",fg="white",activebackground="#45a049",relief="flat",padx=20,pady=8, font=('arial',15), command= checkanswer)
submitButton.grid(row=3, column=1)

#result
resultLabel = Label(root, text= "results", font=('arial',20),fg= "blue")
resultLabel.grid(row=5,column=0)

#restart
submitButton = Button(root, text ="Restart", bg="black", font=('arial',20), command= restart, width= 21, fg="red")
submitButton.grid(row=6, column=0)

generateque()


root.mainloop()