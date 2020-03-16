import win32ui
import local_args

dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
#dlg.SetOFNInitialDir('')  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()

local_args.filename2 = dlg.GetPathName()  # 获取选择的文件名称
#print(local_args.filename)
