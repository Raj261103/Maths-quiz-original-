from tkinter import *
from random import randint, choice

root = Tk()
root.geometry("700x600")
root.title("Maths Quiz")
root.config(bg="#f0f4f8")  # Light blue-gray background

# Variables
question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()

# Color scheme
PRIMARY_COLOR = "#4A90E2"
SUCCESS_COLOR = "#2ECC71"
ERROR_COLOR = "#E74C3C"
DARK_COLOR = "#2C3E50"
LIGHT_BG = "#f0f4f8"
WHITE = "#FFFFFF"

# Generate question
def generateque():
    global questionLabel

    questionNumber.set(questionNumber.get() + 1)

    number1 = randint(1, 10)
    number2 = randint(1, 10)

    operator = choice(['+', '-', '*', '/'])

    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))

    if questionLabel:
        questionLabel.destroy()
    
    questionLabel = Label(
        root, 
        text=f"Question {questionNumber.get()}: {question.get()}", 
        font=('Helvetica', 28, 'bold'),
        bg=WHITE,
        fg=DARK_COLOR,
        pady=20,
        padx=20,
        relief="flat",
        bd=2
    )
    questionLabel.grid(row=2, column=0, columnspan=2, pady=20, padx=40, sticky="ew")

# Checking Answer
def checkanswer():
    global scoreLabel, resultLabel

    if questionNumber.get() > 10:
        return

    if resultLabel:
        resultLabel.destroy()
    
    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 1)
        
        resultLabel = Label(
            root, 
            text="✓ Correct!", 
            font=('Helvetica', 20, 'bold'),
            fg=SUCCESS_COLOR,
            bg=LIGHT_BG
        )
        resultLabel.grid(row=4, column=0, columnspan=2, pady=10)
        
        scoreLabel = Label(
            root, 
            text=f"Score: {score.get()}/10", 
            font=('Helvetica', 18),
            fg=DARK_COLOR,
            bg=LIGHT_BG
        )
        scoreLabel.grid(row=5, column=0, columnspan=2, pady=5)
    else:
        resultLabel = Label(
            root, 
            text="✗ Incorrect", 
            font=('Helvetica', 20, 'bold'),
            fg=ERROR_COLOR,
            bg=LIGHT_BG
        )
        resultLabel.grid(row=4, column=0, columnspan=2, pady=10)

    if questionNumber.get() == 10:
        if scoreLabel:
            scoreLabel.destroy()
        
        # Calculate percentage
        percentage = (score.get() / 10) * 100
        grade = "Excellent!" if percentage >= 80 else "Good Job!" if percentage >= 60 else "Keep Practicing!"
        
        scoreLabel = Label(
            root, 
            text=f"🎯 Final Score: {score.get()}/10\n{grade}", 
            font=('Helvetica', 22, 'bold'),
            fg=DARK_COLOR,
            bg=WHITE,
            pady=15,
            padx=20,
            relief="ridge",
            bd=3
        )
        scoreLabel.grid(row=5, column=0, columnspan=2, pady=20)
    else:
        givenAnswer.set("")  # Clear the entry
        generateque()

def restart():
    global scoreLabel, resultLabel
    
    if scoreLabel:
        scoreLabel.destroy()
    if resultLabel:
        resultLabel.destroy()
    
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateque()
    
    scoreLabel = Label(
        root, 
        text=f"Score: {score.get()}/10", 
        font=('Helvetica', 18),
        fg=DARK_COLOR,
        bg=LIGHT_BG
    )
    scoreLabel.grid(row=5, column=0, columnspan=2, pady=5)

# GUI Components

# Heading
headingLabel = Label(
    root, 
    text="🧮 Maths Quiz", 
    font=('Helvetica', 32, 'bold'),
    bg=PRIMARY_COLOR,
    fg=WHITE,
    pady=15
)
headingLabel.grid(row=0, column=0, columnspan=2, sticky="ew", padx=40, pady=(20, 10))

# Progress Scale
questionScale = Scale(
    root, 
    from_=0, 
    to=10, 
    orient=HORIZONTAL, 
    length=500, 
    variable=questionNumber,
    bg=LIGHT_BG,
    fg=DARK_COLOR,
    highlightthickness=0,
    troughcolor=WHITE,
    font=('Helvetica', 10)
)
questionScale.grid(row=1, column=0, columnspan=2, pady=10, padx=40)

# Question label (initialized)
questionLabel = Label(
    root, 
    text=question.get(), 
    font=('Helvetica', 28, 'bold'),
    bg=WHITE,
    fg=DARK_COLOR,
    pady=20
)
questionLabel.grid(row=2, column=0, columnspan=2, pady=20, padx=40, sticky="ew")

# Answer Entry
answerEntry = Entry(
    root, 
    textvariable=givenAnswer, 
    font=('Helvetica', 24),
    width=15,
    justify='center',
    relief="solid",
    bd=2,
    fg=DARK_COLOR
)
answerEntry.grid(row=3, column=0, pady=20, padx=(40, 10), sticky="e")

# Submit Button
submitButton = Button(
    root, 
    text="Submit ➜", 
    bg=SUCCESS_COLOR,
    fg=WHITE,
    activebackground="#27AE60",
    activeforeground=WHITE,
    relief="flat",
    font=('Helvetica', 16, 'bold'),
    command=checkanswer,
    cursor="hand2",
    padx=25,
    pady=10
)
submitButton.grid(row=3, column=1, pady=20, padx=(10, 40), sticky="w")

# Result Label
resultLabel = Label(
    root, 
    text="", 
    font=('Helvetica', 20, 'bold'),
    bg=LIGHT_BG
)
resultLabel.grid(row=4, column=0, columnspan=2, pady=10)

# Score Label
scoreLabel = Label(
    root, 
    text=f"Score: {score.get()}/10", 
    font=('Helvetica', 18),
    fg=DARK_COLOR,
    bg=LIGHT_BG
)
scoreLabel.grid(row=5, column=0, columnspan=2, pady=5)

# Restart Button
restartButton = Button(
    root, 
    text="🔄 Restart Quiz", 
    bg=DARK_COLOR,
    fg=WHITE,
    activebackground="#1A252F",
    activeforeground=WHITE,
    font=('Helvetica', 16, 'bold'),
    command=restart,
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=12
)
restartButton.grid(row=6, column=0, columnspan=2, pady=30, padx=40, sticky="ew")

# Configure grid weights for centering
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

generateque()

root.mainloop()