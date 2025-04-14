from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import *
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2 
        self.wrong3 = wrong3

qList = []
q1 = Question ('Wich language is spoken in Germany?','German','English','French','Portuguese')
qList.append(q1)
q2 = Question ('Wich language is spoken in the USA?','American English','English','British English','French')
qList.append(q2)
q3 = Question ('How many continents are there?','Seven','Two','Eight','Five')
qList.append(q3)
q4 = Question ('How many coutries are there in Europe?','Fourtyfour','Fiftyseven','Twentyfive','Twentyone')
qList.append(q4)
q5 = Question ('What language is the most spoken in the world?','English',"German","French","Russan")
qList.append(q5)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')

lb_Question = QLabel('Which nationality does not exist?')

RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chulyms')
rbtn_4 = QRadioButton('Aleuts')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
btn_OK = QPushButton('Answer')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Test result')
lb_Result = QLabel('Are you correct or not?')
lb_Correct = QLabel('The answer willbe here!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft|Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question,alignment=Qt.AlignHCenter|Qt.AlignVCenter)
layout_line2.addWidget(RadioGroupBox)

layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Correct!')
        window.score+=1
        print('Statistics\n-Total questions:',window.total, '\n-right answer: ',window.score)
        print('Rating: ',(window.score/window.total*100), '%')
    
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')
            print('Rating: ',(window.score/window.total*100), '%')
def next_question():
    window.total += 1
    print('Statistics\n-Total questions:',window.total, '\n-right answer: ',window.score)
    curr_question = randint(0,len(qList)-1)
   
    q = qList[curr_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()


btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_question()
window.setLayout(layout_card)
window.show()
app.exec()