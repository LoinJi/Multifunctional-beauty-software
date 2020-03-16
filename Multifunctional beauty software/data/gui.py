import cv2
import tkinter as tk
import tkinter.font as tf
from PIL import Image, ImageTk
import local_args

#建立窗口window
window = tk.Tk()
#window = tk.Toplevel()
window.title('计算机视觉课设')

# 设定窗口的大小，并置于屏幕中央
width = 1320
height = 750
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(alignstr)

# 在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型
ft1 = tf.Font(family='微软雅黑', weight=tf.BOLD, size=12)
ft2 = tf.Font(family='华文行楷', weight=tf.BOLD, size=12)


bg = ImageTk.PhotoImage(file='./img/bg.jpg')
background_label = tk.Label(window, image=bg) 
background_label.place(x=0, y=0, relwidth=1, relheight=1) 



# 定义一个函数功能，供点击按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('袁永安\n\n江岱庭\n\n杨崇焕\n\n嵇龙寅\n\n张建欣')
    else:
        on_hit = False
        var.set('')

def function1():
	with open('gui_head.py', 'r', encoding='utf-8') as f:
		exec(f.read())

def function2():
	with open('em_gui.py', 'r', encoding='utf-8') as f:
		exec(f.read())

def function3():
	with open('repair_gui.py', 'r', encoding='utf-8') as f:
		exec(f.read())

def function4():
	with open('face_swap_gui.py', 'r', encoding='utf-8') as f:
		exec(f.read())

frame2 = tk.Frame(window)

b1 = tk.Button(frame2, text='查看小组成员', font=ft1, width=10, height=1, relief='solid', command=hit_me).pack(side=tk.TOP)
l = tk.Label(frame2, textvariable=var, fg='black', font=ft2, width=10, height=10, bg='gray', padx=0).pack(side=tk.TOP)

frame1 = tk.Frame(window)

b2 = tk.Button(frame1, text='头像特效', font=ft1, width=10, height=1, relief='solid', command=function1).pack(side=tk.TOP)
b3 = tk.Button(frame1, text='表情判断', font=ft1, width=10, height=1, relief='solid', command=function2).pack(side=tk.TOP)
b4 = tk.Button(frame1, text='去除水印', font=ft1, width=10, height=1, relief='solid', command=function3).pack(side=tk.TOP)
b5 = tk.Button(frame1, text='换    脸', font=ft1, width=10, height=1, relief='solid', command=function4).pack(side=tk.TOP)

photo = ImageTk.PhotoImage(file='./img/Portugal.jpg')
imgLabel = tk.Label(window, image=photo)
imgLabel.pack(side=tk.TOP)

frame1.pack(side=tk.TOP)
frame2.pack(side=tk.TOP)

# 主窗口循环显示
window.mainloop()