# Week 1 Homework ：大数据可视化第一周作业目录及代码解析
## 任务步骤

1. 让 Datasaurus 数据集经过默认次数的扰动，变化为其他形状（比如说 circle）
2. 使用网址 [DrawMyData](http://robertgrantstats.co.uk/drawmydata.html) 生成任意形状的点阵数据集，让他经过有限次扰动变成其他的形状.
3. 简单评价一下程序的性能，即扰动次数和目标形状完美程度的关系。

## 解决方案
### 第一步
这个部分比较简单，直接在命令行运行即可：
```shell
python run dino circle
```
有些需要注意的问题：
- 由于 Seaborn 的版本更新，原代码当中的 `regplot` 在更新之后位置参数发生了变化，此时需要对每个参数都进行位置的声明：

```python
 sns.regplot(x="x", y="y", data=df, ci=None, fit_reg=reg_fit, marker=marker,
           scatter_kws={"s": 50, "alpha": 0.7, "color":color},
                line_kws={"linewidth":4, "color":"red"})
```
- 该程序只能用命令行方式运行，不建议使用 Jupyter Notebook ，图片较多，数据也较多。
- 如果图片的比例出现问题，更改 `figsize` 为 `(19,5)` 较好.

### 第二步