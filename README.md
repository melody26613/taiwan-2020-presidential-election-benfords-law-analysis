# Analyzing the Taiwan 2020 presidential election using Benford's Law 用班佛定律分析台灣2020選舉


### Abstract 摘要

In light of concerns among some members of the public regarding the integrity of the 2020 Taiwan election results and suspicions of electoral fraud, I was curious about the possibility of such occurrences. To investigate this, the Benford's Law was chosen as a tool to examine whether there was any evidence of manipulation. Benford's Law is commonly utilized to check for data falsification and is often applied in auditing financial records and investigating electoral fraud. The prerequisite for its application is that the dataset should have more than 3000 entries.

I verified that the election data in Taiwan was organized based on the 'village' as the unit. In the 2020 election dataset, there were a total of 7737 entries representing village-level data, making it suitable for verification using Benford's Law.
    
有鑑於部分民眾對於台灣2020年選舉結果有疑慮、認為政府有作票嫌疑，作者也好奇是否存在這樣的可能性，所以決定使用班佛定律確認是否有作票，班佛定律可用來檢查數據是否造假，常被應用在查假帳、查作票，使用前提是資料筆數大於3000筆。

作者確認台灣選舉資料是以"村里"為單位，2020選舉資料裡總共有7737筆村里數據，可使用班佛定律做驗證。

### Prior knowledge 預備知識

* Benford's law 班佛定律

"Benford's law, also known as the Newcomb–Benford law, the law of anomalous numbers, or the first-digit law, is an observation that in many real-life sets of numerical data, the leading digit is likely to be small. In sets that obey the law, the number 1 appears as the leading significant digit about 30% of the time, while 9 appears as the leading significant digit less than 5% of the time. If the digits were distributed uniformly, they would each occur about 11.1% of the time. Benford's law also makes predictions about the distribution of second digits, third digits, digit combinations, and so on."

"It has been shown that this result applies to a wide variety of data sets, including electricity bills, street addresses, stock prices, house prices, population numbers, death rates, lengths of rivers, and physical and mathematical constants. Like other general principles about natural data—for example the fact that many data sets are well approximated by a normal distribution—there are illustrative examples and explanations that cover many of the cases where Benford's law applies, though there are many other cases where Benford's law applies that resist a simple explanation. It tends to be most accurate when values are distributed across multiple orders of magnitude, especially if the process generating the numbers is described by a power law (which is common in nature)."
-- from [wiki](https://en.wikipedia.org/wiki/Benford%27s_law)

「在數學中，班佛定律描述了真實數字數據集中首位數字的頻率分布。一堆從實際生活得出的數據中，以1為首位數字的數的出現機率約為總數的三成，接近直覺得出之期望值1/9的3倍。推廣來說，越大的數，以它為首幾位的數出現的機率就越低。它可用於檢查各種數據是否有造假。但要注意使用條件：1.數據至少3000筆以上。2.不能有人為操控。」 來源自 [wiki](https://zh.wikipedia.org/wiki/%E6%9C%AC%E7%A6%8F%E7%89%B9%E5%AE%9A%E5%BE%8B)

### Development environment 開發環境

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
        
deactivate # deactivate virtual environment
```

5. check your environment for needed packages 檢查環境必要套件
```
./check_environment.sh
```

### Visualize data 資料視覺化

1. execute script 執行指令
```
source venv/bin/activate # activate virtual environment
        
python3 ./visualize_data.py
        
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

According to the final results, the charts of the three candidates seem to fairly conform to Benford's Law. Theoretically, there doesn't appear to be any 'large enough to influence the election results' fraudulent activities in the 2020 Taiwan elections.

Individuals claiming government manipulation may be dissatisfied with the election outcome, but the results are in front of us, and we must try to accept this result. Even after the voting has ended, we can continue to exercise our civic rights to diligently supervise the government. Although the voting has ended, the divisions among the public are still evident. I hope that people with different perspectives can attempt to consider each other's viewpoints, engage in mutual communication, accept one another, find common ground, and realize that mutual criticism will not lead Taiwan to progress. It is through unity and cooperation that we can work towards a better Taiwan.

從最後結果來看，3位候選人的圖表都蠻符合班佛定律，理論上在這次 2020 台灣選舉中，並沒有「大規模到足以影響選舉結果」的作票行為。

宣稱政府有作票的民眾，可能對此次選舉結果不甚滿意，但結果已擺在眼前，我們還是得試著接受這樣的現實，在投票結束後還是可以繼續盡我們的公民權好好監督政府。雖然投票已結束，但可以感受到民眾間的分化還是持續著，作者希望不同立場的人們可以試著站著對方的立場思考，互相交流、接納彼此、找到共同點，互相謾罵並不會使台灣更進步，同心協力才有可能讓台灣更好。