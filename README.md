# reinforcement-learning-tic-tac-toe
強化学習を用いて三目並べAIを作成しました。

## 学習の実施方法
```shell
pythno3 ReinforcementLearning.py
```
Q学習により学習を行います。Q値の配列をバイナリファイル"q_table"に書き出します。

## 対戦方法
```shell
python3 Game.py
player o 's turn
1 0
```
`player o 's turn`が表示されたら` `(スペース)を挟んで駒をおく座標を0~2で指定します。