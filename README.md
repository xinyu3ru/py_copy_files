# py_copy_files
Write something in python 3.4, just have a try.
-----------------------------------------------
�� python3.4 д�㶫����ֻ�ǳ���һ�¡�
-----------------------------------

## How to use: 
## ���ʹ�ã�
		put all the name of file you wanted in the "book.txt" one in a line,
		put all your files in folder "kindle/", then run cpfiles.py, 
		you will get the files in the folder "youneededbook/". 
		It is stupid, but it happens.
		
		������Ҫ�ļ���ȫ��������׺������book.txt����ļ��
		ÿ��һ�����������е��ļ�����kindle����ļ����У�
		����cpfiles.py����������Ҫ���ļ��������ڡ�youneededbook������ļ����С�
		�����ܴ������𣬿��ǳ��������������顣
	
	
	
## method:
## ���򷽷���
		detectcode:Analyzing book.txt encodeing format with
		 chardet (chardet.universaldetector), 
		so you need install chardet with "pip install chardet" 
		or "easy_install chardet". Txt file can be save in
		 assii or utf-8 or others.
		
		detectcode:ʹ��chardet���������book.txt����ļ��ı����ʽ��
		��������Ҫ��װchardet������� "pip install chardet"
		 ����"easy_install chardet"��txt�ļ�ͨ��ʹ��assii����utf-8��ʽ����
		��Ҳ����ʹ��������ʽ��
		
		listbookfile:list all files your have in  folder "kindle", 
		and put all names in a dict.
		listbookfile:��kindle�ļ��������е��ļ�����·���洢��һ���ֵ��С�
		findbook:open the file book.txt and read lines, 
		analyz whether the file name is in the dict.
		findbook:��book.txt����ļ��������ж�ȡ��
		�ж������е��ļ����Ƿ����ֵ��У�
		����ڵĻ��ͷ�������ļ��е����·����
		
		direxist:analyz whether folder "youneededbook/" is exist, 
		if not create one
		
		direxist:�ж�youneededbook/����ļ����Ƿ���ڣ�
		����������Ժ󿽱������ļ���
		
		cpbooks:copy files with shutil.copy2. 
		cpbooks:ʹ��shutil.copy2�����ļ���
		## bugs��
## ȱ��:		
		1. it can not sovle some special symbol such like		
		middle dot(��)(not . or ',just ��), and
		some others. and i don't know why.
		1.���ܳ���һЩ��������ŵ��ļ����������е㣨������
		���������š��������������ģ��Ҳ�֪��ԭ���ء�

	
## ps:
		I don't want to update the codes.
		�Ҳ�������ˡ�