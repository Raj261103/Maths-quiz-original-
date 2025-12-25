from tkinter import *
from random import randint, choice

root = Tk()
root.geometry("700x550")
root.title("Maths Quiz")
root.configure(bg="#121212")  # UI change (dark background)

question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()

# -------------------- STYLES (UI ONLY) --------------------
TITLE_FONT = ("Helvetica", 26, "bold")
QUESTION_FONT = ("Arial", 18)
NORMAL_FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 14, "bold")

BG_COLOR = "#121212"
CARD_COLOR = "#1e1e1e"
TEXT_COLOR = "#ffffff"
ACCENT = "#2196F3"
SUCCESS = "#4CAF50"
ERROR = "#F44336"
# ---------------------------------------------------------

# Main Card Frame (UI only)
card = Frame(root, bg=CARD_COLOR, padx=30, pady=25)
card.pack(pady=30)

# -------------------- FUNCTIONS (LOGIC UNCHANGED) --------------------
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
        card,
        text=f"Question : {question.get()}",
        font=QUESTION_FONT,
        bg=CARD_COLOR,
        fg=TEXT_COLOR
    )
    questionLabel.pack(pady=15)


def checkanswer():
    global scoreLabel, resultLabel

    if questionNumber.get() > 10:
        return

    if resultLabel:
        resultLabel.destroy()

    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 1)
        resultLabel = Label(card, text="Correct ✔", font=QUESTION_FONT, fg=SUCCESS, bg=CARD_COLOR)
    else:
        resultLabel = Label(card, text="Incorrect ✖", font=QUESTION_FONT, fg=ERROR, bg=CARD_COLOR)

    resultLabel.pack(pady=10)

    if questionNumber.get() == 10:
        scoreLabel.config(text=f"Final Score : {score.get()}")
    else:
        generateque()


def restart():
    score.set(0)
    questionNumber.set(0)
    scoreLabel.config(text="Score : 0")
    generateque()

# -------------------- GUI --------------------

headingLabel = Label(
    card,
    text="Maths Quiz",
    font=TITLE_FONT,
    bg=CARD_COLOR,
    fg=ACCENT
)
headingLabel.pack(pady=10)

questionScale = Scale(
    card,
    from_=0,
    to=10,
    orient=HORIZONTAL,
    length=400,
    variable=questionNumber,
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    troughcolor="#333333",
    highlightthickness=0
)
questionScale.pack(pady=10)

questionLabel = Label(card, text="", font=QUESTION_FONT, bg=CARD_COLOR, fg=TEXT_COLOR)
questionLabel.pack(pady=10)

answerEntry = Entry(
    card,
    textvariable=givenAnswer,
    font=QUESTION_FONT,
    width=20,
    bg="#2a2a2a",
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief="flat"
)
answerEntry.pack(pady=15)

submitButton = Button(
    card,
    text="Submit",
    font=BUTTON_FONT,
    bg=ACCENT,
    fg="white",
    relief="flat",
    padx=25,
    pady=8,
    command=checkanswer
)
submitButton.pack(pady=10)

scoreLabel = Label(
    card,
    text="Score : 0",
    font=NORMAL_FONT,
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)
scoreLabel.pack(pady=5)

resultLabel = Label(card, text="", bg=CARD_COLOR)
resultLabel.pack()

restartButton = Button(
    card,
    text="Restart Quiz",
    font=BUTTON_FONT,
    bg="#333333",
    fg=ERROR,
    relief="flat",
    padx=20,
    pady=8,
    command=restart
)
restartButton.pack(pady=15)

generateque()
root.mainloop()
