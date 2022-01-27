# AdobeReaderOfflineInstallerDownloader
Adobe Reader DC offline installer downloader

# Requirements

Before use install requirements with

```
pip3 install -r requirements.txt
```

# Usage

```
python3 downloader.py
```

# Language

By default it downloads the offline installer for Italian language, to change this you must change this line:

```
XML_URL = "https://get.adobe.com/reader/webservices/adm/?cname=readerdc_it_xa_install.exe&bname=readerdc&site=live&type=install&language=it"
```

just change the "it" with your language code
