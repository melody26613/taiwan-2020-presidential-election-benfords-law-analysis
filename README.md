# Analysis Taiwan 2020 presidential election by using Benford's law 用班佛定律分析台灣2020選舉


### Abstract 摘要

Some people in Taiwan consider there was electoral fraud of Taiwan 2020 presidential election, according to that, I decide to use Benford's law to check if there was electoral fraud in 2020 Taiwan election or not. Benford's law can identify data result, usually for accounting fraud detection and verify election data, number of data is bigger than 3000 as a presupposition.

I already checked that unit of row in election data from Central Election Commission is "village", total number of data is 7737, that means we can use Benford's law to verify election data.
    
有鑑於部分民眾對於台灣2020年選舉結果有疑慮、認為政府有作票嫌疑，作者也好奇是否存在這樣的可能性，所以決定使用班佛定律確認是否有作票，班佛定律可用來檢查數據是否造假，常被應用在查假帳、查作票，使用前提是資料筆數大於3000筆。

作者確認台灣選舉資料是以"村里"為單位，2020選舉資料裡總共有7737筆村里數據，可使用班佛定律做驗證。

### Environment 環境

* Ubuntu 18.04

* python3.6 + pip + virtual environment


### Preparation 準備工作

1. install pip 安裝pip

        sudo apt-get update

        sudo apt-get install python3-pip

2. install virtual environment command for python3 安裝python3的虛擬環境套件

        sudo apt-get install python3-venv

3. create virtual environment 建置虛擬環境

        python3 -m venv venv
        
        source venv/bin/activate # activate virtual environment
        
        pip install --upgrade pip
        
        deactivate # deactivate virtual environment

4. check your environment for needed packages 檢查環境必要套件

        ./0_check_environment.sh

### Visualize data 資料視覺化

1. execute script 執行指令

        source venv/bin/activate # activate virtual environment
        
        python3 ./visualize_data.py
        
        deactivate # deactivate virtual environment
        
2. see output result in output/ * 輸出結果放在 output/ 下

* graph of candidate 2 候選人2號韓國瑜的圖表

![image](https://github.com/melody26613/taiwan-2020-presidential-election-benfords-law-analysis/blob/master/output/Candidate2_韓國瑜.png)

* graph of candidate 3 候選人3號蔡英文的圖表

![image](https://github.com/melody26613/taiwan-2020-presidential-election-benfords-law-analysis/blob/master/output/Candidate3_蔡英文.png)

### Conclusion 結論

According to the output graph, data of three candidates followed Benford's law. It's theoretically that there was "no large scale of electoral fraud effected election results" in Taiwan 2020 presidential election.

Maybe people just not satisfied with the election results, so they claim there was electoral fraud in 2020 election. However, as the fact we can see, we still need to accept this result, and keep using our civil rights to supervise the government no matter what. We can still see that people in different opinions cannot accept each other's opinion even though election is over. I think verbal attack to each other is not helpful for Taiwan, we should put ourself in their shoes, find common in each other, together to make Taiwan a better place.

從最後結果來看，3位候選人的圖表都蠻符合班佛定律，理論上在這次 2020 台灣選舉中，並沒有「大規模到足以影響選舉結果」的作票行為。

宣稱政府有作票的民眾，可能對此次選舉結果不甚滿意，但結果已擺在眼前，我們還是得試著接受這樣的現實，在投票結束後還是可以繼續盡我們的公民權好好監督政府。雖然投票已結束，但可以感受到民眾間的分化還是持續著，作者希望不同立場的人們可以試著站著對方的立場思考，互相交流、接納彼此、找到共同點，互相謾罵並不會使台灣更進步，同心協力才有可能讓台灣更好。