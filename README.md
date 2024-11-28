# 練習Google Cloud功能的專案
- 筆記連結: https://www.notion.so/GCP-11cac20b327e809f990df17d965e1f22
- 文件結構:
	GCP/
	├── app/				# 各項服務的code
	│   ├── ...				# 各項服務的dir		
	│   ├── config/
	│   │   └── settings.py
	│   └── modules/
	│       ├── __init__.py
	│       └── utils.py
	├── data/
	│   ├── sample/			# 範例資料夾
	│   └── sample_format_transform.py	# 轉換範例資料格式的腳本
	├── requirements.txt	# Python 依賴檔
	├── .gitignore
	└── README.md