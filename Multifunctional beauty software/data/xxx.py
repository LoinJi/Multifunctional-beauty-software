
import tkinter as tk
import tkinter.font as tf
 


# ��1����ʵ����object����������window
window = tk.Tk()
 
# ��2���������ڵĿ��ӻ�������
window.title('My Window')
 
# ��3�����趨���ڵĴ�С(�� * ��)
window.geometry('500x300')  # ����ĳ���Сx
# ��4������ͼ�ν������趨��ǩ
var = tk.StringVar()    # ��label��ǩ����������Ϊ�ַ�����
ft = tf.Font(family='΢���ź�', weight=tf.BOLD, size=10)
l = tk.Label(window, textvariable=var, fg='black', font=ft, width=50, height=100)


# ����һ���������ܣ����������ʱ���ã������������command=������
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('Ԭ����\n���ͥ\n����\n������\n�Ž���')
    else:
        on_hit = False
        var.set('')






 
# ��5�����ڴ��ڽ������÷���Button����
b1 = tk.Button(window, text='С���Ա', font=ft, width=10, height=1, command=hit_me)
b2 = tk.Button(window, text='����1', font=ft, width=10, height=1, command=hit_me)
b3 = tk.Button(window, text='����2', font=ft, width=10, height=1, command=hit_me)
b4 = tk.Button(window, text='����3', font=ft, width=10, height=1, command=hit_me)
b5 = tk.Button(window, text='����4', font=ft, width=10, height=1, command=hit_me)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
l.pack()
 
# ��6����������ѭ����ʾ
window.mainloop()


