# py_copy_files
Write something in python 3.4, just have a try.
-----------------------------------------------
用 python3.4 写点东西，只是尝试一下。
-----------------------------------

## How to use: 
## 如何使用：
		put all the name of file you wanted in the "book.txt" one in a line,
		put all your files in folder "kindle/", then run cpfiles.py, 
		you will get the files in the folder "youneededbook/". 
		It is stupid, but it happens.
		
		把你需要文件的全名包括后缀名放在book.txt这个文件里，
		每行一个，把你所有的文件放在kindle这个文件夹中，
		运行cpfiles.py，所有你需要的文件将出现在“youneededbook”这个文件夹中。
		这样很蠢不是吗，可是出现了这样的事情。
	
	
	
## method:
## 程序方法：
		detectcode:Analyzing book.txt encodeing format with
		 chardet (chardet.universaldetector), 
		so you need install chardet with "pip install chardet" 
		or "easy_install chardet". Txt file can be save in
		 assii or utf-8 or others.
		
		detectcode:使用chardet这个包分析book.txt这个文件的编码格式，
		所以你需要安装chardet这个包， "pip install chardet"
		 或者"easy_install chardet"。txt文件通常使用assii或者utf-8格式编码
		，也可能使用其他格式。
		
		listbookfile:list all files your have in  folder "kindle", 
		and put all names in a dict.
		listbookfile:把kindle文件夹中所有的文件名及路径存储到一个字典中。
		findbook:open the file book.txt and read lines, 
		analyz whether the file name is in the dict.
		findbook:打开book.txt这个文件并且逐行读取，
		判断这行中的文件名是否在字典中，
		如果在的话就返回这个文件夹的相对路径。
		
		direxist:analyz whether folder "youneededbook/" is exist, 
		if not create one
		
		direxist:判断youneededbook/这个文件夹是否存在，
		它用来存放稍后拷贝来的文件。
		
		cpbooks:copy files with shutil.copy2. 
		cpbooks:使用shutil.copy2拷贝文件。
		## bugs：
## 缺陷:		
		1. it can not sovle some special symbol such like		
		middle dot(·)(not . or ',just ·), and
		some others. and i don't know why.
		1.不能出来一些带特殊符号的文件名，比如中点（·），
		甚至书名号《》，或者其他的，我不知道原因呢。

	
## ps:
		I don't want to update the codes.
		我不想更新了。