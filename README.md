# 練習Google Cloud功能的專案
### 筆記連結: https://www.notion.so/GCP-11cac20b327e809f990df17d965e1f22

### 文件結構:
	GCP/
	├── app/				# 各項服務的code
	│   ├── CloudStorage/
	│   ├── BigQuery/
	│   ├── .../	
	│   ├── TopicResearch/	# 主題研究
	│   │   └──Option/		# 選擇權策略研究
	│   ├── *test*			# 帶有 test 字串的檔案為測試用無特別意義	
	│   │
	│   ├── ...				# 各項服務的dir	
	│   ├── config/
	│   │   └── settings.py
	│   └── modules/
	│       ├── __init__.py
	│       └── utils.py
	├── data/
	│   ├── sample/			# 範例資料資料夾
	│   └── sample_format_transform.py	# 轉換範例資料格式的腳本
	├── service_account/    # 服務帳戶私鑰
	├── requirements.txt	# Python 依賴檔
	├── .gitignore
	└── README.md
	
### 資料集
- Iris: https://www.kaggle.com/datasets/uciml/iris
- New_York_Stock_Exchange: https://www.kaggle.com/datasets/aadyasingh55/fake-news-classification
- New York Stock Exchange: https://www.kaggle.com/datasets/dgawlik/nyse
- Dog Emotions Prediction: https://www.kaggle.com/datasets/devzohaib/dog-emotions-prediction