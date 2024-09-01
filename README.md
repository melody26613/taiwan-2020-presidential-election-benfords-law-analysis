# An Analysis of the 2020 Taiwanese Presidential Election Using Benford's Law 用班佛定律分析台灣2020總統選舉


### Abstract 摘要

To investigate the claims of electoral fraud in the 2020 Taiwanese election, this study applied Benford's Law to the election data. Benford's Law is a statistical test that can be used to identify patterns in numerical data that are indicative of fraud or manipulation. The law requires a large dataset, typically with more than 3,000 data points.

The Taiwanese election data, which is organized at the village level, was found to be suitable for this analysis, with a total of 7,737 data points.
    
有鑑於部分民眾對於台灣2020年選舉結果有疑慮、認為政府有作票嫌疑，作者也好奇是否存在這樣的可能性，所以決定使用班佛定律確認是否有作票的可能。班佛定律可用來檢查數據是否造假，常被應用在查假帳、查作票，使用前提是資料筆數大於3000筆。

作者確認台灣選舉資料是以"村里"為單位，2020選舉資料裡總共有7737筆村里數據，可使用班佛定律做驗證。

### Prior Knowledge 預備知識

* Benford's law 班佛定律

"Benford's law, also known as the Newcomb–Benford law, the law of anomalous numbers, or the first-digit law, is an observation that in many real-life sets of numerical data, the leading digit is likely to be small. In sets that obey the law, the number 1 appears as the leading significant digit about 30% of the time, while 9 appears as the leading significant digit less than 5% of the time. If the digits were distributed uniformly, they would each occur about 11.1% of the time. Benford's law also makes predictions about the distribution of second digits, third digits, digit combinations, and so on."

"It has been shown that this result applies to a wide variety of data sets, including electricity bills, street addresses, stock prices, house prices, population numbers, death rates, lengths of rivers, and physical and mathematical constants. Like other general principles about natural data—for example the fact that many data sets are well approximated by a normal distribution—there are illustrative examples and explanations that cover many of the cases where Benford's law applies, though there are many other cases where Benford's law applies that resist a simple explanation. It tends to be most accurate when values are distributed across multiple orders of magnitude, especially if the process generating the numbers is described by a power law (which is common in nature)."
-- from [wiki](https://en.wikipedia.org/wiki/Benford%27s_law)

「在數學中，班佛定律描述了真實數字數據集中首位數字的頻率分布。一堆從實際生活得出的數據中，以1為首位數字的數的出現機率約為總數的三成，接近直覺得出之期望值1/9的3倍。推廣來說，越大的數，以它為首幾位的數出現的機率就越低。它可用於檢查各種數據是否有造假。但要注意使用條件：1.數據至少3000筆以上。2.不能有人為操控。」 來源自 [wiki](https://zh.wikipedia.org/wiki/%E6%9C%AC%E7%A6%8F%E7%89%B9%E5%AE%9A%E5%BE%8B)


### Election Data 選舉資料
You can download election data from [here](https://db.cec.gov.tw/ElecTable/Election/ElecTickets?dataType=tickets&typeId=ELC&subjectId=P0&legisId=00&themeId=1f7d9f4f6bfe06fdaf4db7df2ed4d60c&dataLevel=N&prvCode=00&cityCode=000&areaCode=00&deptCode=000&liCode=0000)

可以在[這裡](https://db.cec.gov.tw/ElecTable/Election/ElecTickets?dataType=tickets&typeId=ELC&subjectId=P0&legisId=00&themeId=1f7d9f4f6bfe06fdaf4db7df2ed4d60c&dataLevel=N&prvCode=00&cityCode=000&areaCode=00&deptCode=000&liCode=0000)下載選舉資料

### Development Environment 開發環境

* Ubuntu 18.04

* python3.6 + pip + virtual environment


### Preparation 準備工作

1. clone repo 複製程式碼

```
git clone git@github.com:melody26613/taiwan-2020-presidential-election-benfords-law-analysis.git

cd taiwan-2020-presidential-election-benfords-law-analysis
```

2. install pip 安裝pip

    [pip documentation v23.3.2](https://pip.pypa.io/en/stable/installation/)

    [AWS install pip on Linux](https://docs.aws.amazon.com/zh_tw/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html)

3. install virtual environment command for python3 安裝python3的虛擬環境套件
```
sudo apt-get install python3-venv
```

4. create virtual environment 建置虛擬環境
```
python3 -m venv venv
        
source venv/bin/activate # activate virtual environment
        
pip install --upgrade pip
pip install -r requirements.txt

deactivate # deactivate virtual environment
```

### Visualize Data 資料視覺化

1. execute script 執行指令
```
source venv/bin/activate # activate virtual environment
        
python3 visualize_data.py
        
deactivate # deactivate virtual environment
```

2. see output result in output/ * 輸出結果放在 output/ 下

* graph of candidate 1 Soong Chu-yu 候選人1號宋楚瑜的圖表

![image](https://github.com/melody26613/taiwan-2020-presidential-election-benfords-law-analysis/blob/master/output/Candidate1.png)

* graph of candidate 2 Han Kuo-yu 候選人2號韓國瑜的圖表

![image](https://github.com/melody26613/taiwan-2020-presidential-election-benfords-law-analysis/blob/master/output/Candidate2.png)

* graph of candidate 3 Tsai Ing-wen 候選人3號蔡英文的圖表

![image](https://github.com/melody26613/taiwan-2020-presidential-election-benfords-law-analysis/blob/master/output/Candidate3.png)

### Conclusion 結論

The application of Benford's Law to the 2020 Taiwanese presidential election data has yielded results that do not support claims of widespread electoral fraud. While some citizens may have expressed doubts about the integrity of the election process, the statistical analysis presented in this study suggests that the election results are reliable.

However, the persistence of political polarization within Taiwanese society is a matter of concern. It is crucial for individuals to engage in constructive dialogue and to seek common ground. By fostering a more inclusive and tolerant society, Taiwan can better address the challenges it faces.

從最後結果來看，3位候選人的圖表都蠻符合班佛定律，理論上在這次 2020 台灣選舉中，並沒有「大規模到足以影響選舉結果」的作票行為。

宣稱政府有作票的民眾，可能對此次選舉結果不甚滿意，但結果已擺在眼前，我們還是得試著接受這樣的現實，在投票結束後還是可以繼續盡我們的公民權好好監督政府。雖然投票已結束，但可以感受到民眾間的分化還是持續著，作者希望不同立場的人們可以試著站著對方的立場思考，互相交流、接納彼此、找到共同點，互相謾罵並不會使台灣更進步，同心協力才有可能讓台灣更好。