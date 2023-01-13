# teamNLPower

Methodology:

1: Sampling
Extract Data from top 20 publishers & the recent 3 years  (i.e., 2020-2022)

Please refer to Release: 2020to2022data
Download via:
https://github.com/kychunab/team2223/releases/download/2020to2022data/2020to2022data.csv

2: Translation and Combine
Split the Dataset into small parts and translate using google API.
Combine the translated files into one
Create Column "tran_headline" and "tran_content"

Please refer to Release: 2020to2022transdata
Download via:
https://github.com/kychunab/team2223/releases/download/trandata/real_2020_22tranfinal.csv

3: Data Cleansing
Remove null / poorly translated data and perform text preprocessing

4: ESG and Senti label Adding
Adding ESG categories and sentiment labels to the dataset
With reference to model:
Sentiment: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment
Esg Categories Classification: https://huggingface.co/yiyanghkust/finbert-esg-9-categories

Please refer to Release: 20_22ESGSentidata
Download via:
https://github.com/kychunab/team2223/releases/download/esgsentidata/20_22ESGsentidata.csv

5:Define keywords  and extract rows that contain that those keywords
Please check the folder "5_Code and Data for Keyword Extraction"
Code can be found in "5_Code and Data for Keyword Extraction/Code"
Dataset extracted by Keywords and Graphs can be found in "5_Code and Data for Keyword Extraction\Keyword datasets"

6:ESG & HSI ANALYSIS
Align the dataset with HSI index to generate further insight 
Please find the aligned dataset in folder "6_Groupby Dataset"

7:PREDICTIVE MODEL
Build regression and classification models with ESG sentiment and label counts.
We do it in 2 Approach:
For predicting close price using close price of HSI and senti label, check "7_Build Predictive Model\LSTM_Predict close price"

For predicting Daily Return and Classification of positive/negative return, check "7_Build Predictive Model\Predict Daily Return"


