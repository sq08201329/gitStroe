#命令			#说明				#实例
:h vaimtutor 		#内置文档;
:h key-notation 	#键pan对照;
<C-]>			#tag跳转
<C-o>			#回跳
f{char}			#匹配右边第一个char		+ + +++++++
; | ,			#重复f
i<C-k>			#二合字母
<C-a><C-x>		#数字加减			138
:%s/char/chars/gc	#:help :s询问替换		charCharchar

# | *			#匹配				sun sun qi sun sun qi
cwsunqi qi[ESC]	 	#after *
:help :map-operator
:help g


<C-h>			#删除前一个字符
<C-w>			#单词
<C-u>			#行首
<Esc> <C-[>		] #切换到普通模式
<C-o>			#切换到 插入-普通模式
zz			#重绘屏幕
yt,	jA	<C-r>0	#在插入模式下 粘贴
i	<C-r>=	<CR>	#计算
i	<C-v>065	#ascii
i	<C-v>u00bf	#16进制 unicode
¿	
