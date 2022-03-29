# 项目执行方法

## 一键测试

**在当前目录**执行script.py脚本即可测试内置的测试案例

## 文件测试

### 小明玩球

在本地**当前目录**使用命令行输入：

```
python ./klotski.py ./input/klotski_input.txt 123804765 3 3
```

然后在output文件夹中的klotski_output.txt中即可查看测试案例的测试结果（可以在input文件夹中修改klotski_input.txt案例）

### 爱跑步的小明

在本地**当前目录**使用命令行输入：

```
python ./hillrun.py ./input/hillrun_input.txt
```

然后在output文件夹中的hillrun_output.txt中即可查看测试案例的测试结果（可以在input文件夹中修改hillrun_input.txt案例）

## 命令行测试

### 小明玩球

在本地**当前目录**使用命令行输入：

```
python ./klotski.py 起始状态 终止状态 长 宽
```

即可在命令行中得到输出结果（无解的除外）

### 爱跑步的小明

在本地**当前目录**使用命令行输入：

```
python ./hillrun.py
```

然后根据命令行提示逐步输入 N M K以及路径即可
