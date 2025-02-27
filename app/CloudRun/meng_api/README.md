# meng_api
GCP部署API的測試範例

# 測試
- local端執行api，在terminal執行以下指令，不要直接用python執行
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

- 瀏覽器前往
http://localhost:8080/sample/hello

# 打包 docker
- build
docker build --platform linux/amd64 -t asia-east1-docker.pkg.dev/data-sandbox-344301/meng-workspace/meng_api .
- local 測試 docker image
docker run -p 8080:8080 asia-east1-docker.pkg.dev/data-sandbox-344301/meng-workspace/meng_api:latest

# 上傳 AR
- 設定專案
gcloud init
- 先登入自己帳號才能上傳
gcloud auth login
- 第一次上傳要key這串指令
gcloud auth configure-docker asia-east1-docker.pkg.dev
- push to Artifacts Registry
docker push asia-east1-docker.pkg.dev/data-sandbox-344301/meng-workspace/meng_api:latest