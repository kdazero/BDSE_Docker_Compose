# Docker_Compose
利用 Docker Compose 將 CSV檔寫入 MySQL 再利用 Python 將內容讀取出來，透過 Flask 渲染後，在轉接給 ngnix 在網頁上做呈現 

# 使用教學
- docker download

    下載 docker 請先複製並執行下列全部的程式
    ```bash
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```

    上方段落執行完後再執行此行程式
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

- 本專案執行方式
    將本文件所有檔案複製到 Linux 中 (Use Filezilla)
    請不要變更任何檔名及檔案位置避免出錯

    請在本檔案主目錄下執行
    ```bash
    docker compose -build
    docker compose up -d
    ``` 

Created By BDSE_36_10 李柏毅