#vim的使用

###TAB编辑

*gt* 下一个tab（goto next tab）
*gT* 前一个tab

关于*tabdo*
当需要更改多个tab中的文件的时候，可以用 :tabdo 这个指令 这个就相当于 loop 到你的所有的 tab 中然后运行指令。
例如有5个文件都在tab里面，需要更改一个变量名称：abc 到 def， 就可以用 :tabdo %s/abc/def/g 这样所有的5个tab里面的abc就都变成def了

### 注释
多行注释：
1. 进入命令行模式，按ctrl + v进入 visual block模式，然后按j, 或者k选中多行，把需要注释的行标记起来
2. 按大写字母I，再插入注释符，例如//
3. 按esc键就会全部注释了

取消多行注释：
1. 进入命令行模式，按ctrl + v进入 visual block模式，按字母l横向选中列的个数，例如 // 需要选中2列
2. 按字母j，或者k选中注释符号
3. 按d键就可全部取消注释
