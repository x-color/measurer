# Easy measuring a function

Measure run time of a function.

関数の実行時間を簡単に測定するためのモジュール。  
`Measurer`インスタンスを生成し、`measure`メソッドに測定したい関数を渡すだけで、指定回数実行した場合の総実行時間と一回当たりの平均実行時間を画面に出力する。  
また、返り値としてカンマ区切りの文字列`関数名,総実行時間,平均実行時間`を返す。


### How to use

```python
from measurer import Measurer

# This function is you want to measure.
def function():
  # Some processes..
  return

measurer = Measurer()
result = measurer.measure(function)
# [Completed] function()
#     Total  : xxx[sec]
#     Average: yyy[sec]
print(result)
# function,xxx,yyy
```

### Methods

```python
measurer.Measurer(self, repeat=100, color=True)
```

- Arguments
  - repeat (int): The number of executions of measured a function. This number must be larger than 1.
  - color (boolean): Coloring log messge.

```python
measurer.Measurer.measure(self, function, *args)
```

- Arguments
  - function (function): It is a function you want to measure.
  - args (tuple): This argument is passed to measured a funstion.

- Return
  - Message of result of measuring a function.
