import tkinter as tk
import tkinter.font as tf 
from PIL import Image, ImageTk 

# 建立窗口
window = tk.Toplevel()
window.title('头像特效')

# 设定窗口的大小，并置于屏幕中央
width = 300
height = 200
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(alignstr)

# 在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型
ft1 = tf.Font(family='微软雅黑', weight=tf.BOLD, size=12)
ft2 = tf.Font(family='华文行楷', weight=tf.BOLD, size=12)

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

# 拍照
def function1():
    with open('take_pics.py', 'r', encoding='utf-8') as f:
	    exec(f.read())

# 选取照片
def function2():
	with open('select_pic.py', 'r', encoding='utf-8') as f:
		exec(f.read())

# 处理照片
def function3():
    with open('head1.py', 'r', encoding='utf-8') as f:
        exec(f.read())

# 化妆
def function4():
    with open('make_up.py', 'r', encoding='utf-8') as f:
        exec(f.read())

frame1 = tk.Frame(window)

b1 = tk.Button(frame1, text='当场拍照', font=ft1, width=10, height=1, relief='solid', command=function1).pack(side=tk.TOP)
b2 = tk.Button(frame1, text='使用照片', font=ft1, width=10, height=1, relief='solid', command=function2).pack(side=tk.TOP)
b3 = tk.Button(frame1, text='戴帽子', font=ft1, width=10, height=1, relief='solid', command=function3).pack(side=tk.TOP)
b4 = tk.Button(frame1, text='化妆', font=ft1, width=10, height=1, relief='solid', command=function4).pack(side=tk.TOP)


frame1.pack(side=tk.TOP)

 
# 主窗口循环显示
window.mainloop()