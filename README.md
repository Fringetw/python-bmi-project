# BMI Calculator

一個使用 Python 製作的簡易 BMI 測量程式。

## 功能

* 計算 BMI
* 判斷 BMI 分類
* 顯示正常體重範圍
* 顯示目前體重與正常範圍的差距
* 防止錯誤輸入
* 支援重複測量

## 使用方法

### 方法 1：直接執行 EXE

如果不想安裝 Python，可以到 GitHub 的 **Releases** 下載：

`BMI-Calculator.exe`

下載後直接雙擊即可執行。

### 方法 2：使用 Python 執行

需要先安裝 Python。

下載專案後，在專案資料夾執行：

```bash
python main.py
```

如果 Windows 無法使用 `python`，可以嘗試：

```bash
py main.py
```

## 專案檔案

```text
BMI-Calculator
├── main.py
├── bmi.py
└── README.md
```

* `main.py`：主要執行程式
* `bmi.py`：BMI 計算與分類功能

## BMI 分類

| BMI         | 分類   |
| ----------- | ---- |
| < 18.5      | 體重過輕 |
| 18.5 - 23.9 | 體重正常 |
| 24 - 26.9   | 體重過重 |
| 27 - 29.9   | 輕度肥胖 |
| 30 - 34.9   | 中度肥胖 |
| ≥ 35        | 重度肥胖 |

## 注意

此專案主要用於 Python 程式設計練習，BMI 結果僅供參考。
