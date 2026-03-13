import tkinter as tk
import math
import speech_recognition as sr

# WINDOW
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("450x600")
root.configure(bg="white")

expression = ""
input_text = tk.StringVar()

# DISPLAY
display = tk.Entry(root, textvariable=input_text,
                   font=("Arial",22),
                   bd=10, relief="sunken",
                   justify="right")

display.pack(fill="both", padx=10, pady=10, ipady=15)

# FUNCTIONS
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# SCIENTIFIC FUNCTIONS
def sin_func():
    global expression
    input_text.set(math.sin(math.radians(float(expression))))

def cos_func():
    global expression
    input_text.set(math.cos(math.radians(float(expression))))

def tan_func():
    global expression
    input_text.set(math.tan(math.radians(float(expression))))

def log_func():
    global expression
    input_text.set(math.log10(float(expression)))

def ln_func():
    global expression
    input_text.set(math.log(float(expression)))

def sqrt_func():
    global expression
    input_text.set(math.sqrt(float(expression)))

def power2():
    global expression
    input_text.set(float(expression)**2)

def power_y():
    btn_click("**")

def insert_pi():
    btn_click(str(math.pi))

def insert_e():
    btn_click(str(math.e))

# VOICE INPUT
def voice_input():
    global expression
    r = sr.Recognizer()

    with sr.Microphone() as source:
        input_text.set("Speak...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()

        command = command.replace("plus","+")
        command = command.replace("minus","-")
        command = command.replace("times","*")
        command = command.replace("multiply","*")
        command = command.replace("divided by","/")

        expression = command
        result = str(eval(expression))
        input_text.set(result)

    except:
        input_text.set("Voice Error")

# BUTTON FRAME
frame = tk.Frame(root)
frame.pack()

# SCIENTIFIC BUTTONS
sci_buttons = [
("sin",sin_func),
("cos",cos_func),
("tan",tan_func),
("log",log_func),
("ln",ln_func),
("√",sqrt_func),
("x²",power2),
("xʸ",power_y),
("π",insert_pi),
("e",insert_e)
]

row = 0
col = 0

for (text,func) in sci_buttons:
    tk.Button(frame,text=text,width=7,height=2,
              bg="#4aa3df",fg="white",
              command=func)\
    .grid(row=row,column=col,padx=5,pady=5)

    col += 1
    if col > 4:
        col = 0
        row += 1

# NUMBER BUTTONS
buttons = [
('7',3,0),('8',3,1),('9',3,2),('/',3,3),
('4',4,0),('5',4,1),('6',4,2),('*',4,3),
('1',5,0),('2',5,1),('3',5,2),('-',5,3),
('0',6,0),('.',6,1),('(',6,2),(')',6,3),
('+',7,0),('=',7,1)
]

for b in buttons:
    if len(b) == 3:
        text,row,col = b
    else:
        text,row,col = b

    action = lambda x=text: btn_click(x)

    if text == "=":
        action = btn_equal

    tk.Button(frame,text=text,width=7,height=2,
              bg="#555555",fg="white",
              command=action)\
    .grid(row=row,column=col,padx=5,pady=5)

# CLEAR BUTTON
tk.Button(frame,text="C",
          bg="red",fg="white",
          width=7,height=2,
          command=btn_clear)\
.grid(row=7,column=2,padx=5,pady=5)

# VOICE BUTTON
tk.Button(root,text="VOICE INPUT",
          bg="lightblue",
          font=("Arial",12),
          width=20,
          command=voice_input)\
.pack(pady=15)

root.mainloop()