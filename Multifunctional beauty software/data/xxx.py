
import tkinter as tk
import tkinter.font as tf
 


# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
# 第4步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型
ft = tf.Font(family='微软雅黑', weight=tf.BOLD, size=10)
l = tk.Label(window, textvariable=var, fg='black', font=ft, width=50, height=100)


# 定义一个函数功能，供点击按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('袁永安\n江岱庭\n杨崇焕\n嵇龙寅\n张建欣')
    else:
        on_hit = False
        var.set('')






 
# 第5步，在窗口界面设置放置Button按键
b1 = tk.Button(window, text='小组成员', font=ft, width=10, height=1, command=hit_me)
b2 = tk.Button(window, text='功能1', font=ft, width=10, height=1, command=hit_me)
b3 = tk.Button(window, text='功能2', font=ft, width=10, height=1, command=hit_me)
b4 = tk.Button(window, text='功能3', font=ft, width=10, height=1, command=hit_me)
b5 = tk.Button(window, text='功能4', font=ft, width=10, height=1, command=hit_me)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
l.pack()
 
# 第6步，主窗口循环显示
window.mainloop()


