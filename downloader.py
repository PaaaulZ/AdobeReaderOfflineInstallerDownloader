import requests
from urllib.parse import urlparse
import os
import xml.etree.ElementTree as ET

XML_URL = "https://get.adobe.com/reader/webservices/adm/?cname=readerdc_it_xa_install.exe&bname=readerdc&site=live&type=install&language=it"


def get_manifest_url():

    r = requests.get(XML_URL)
    if r.status_code != 200:
        raise Exception("\t [-] Error retrieving XML from adobe.com")
    
    xml_root = ET.fromstring(r.content)
    
    for package in xml_root.findall('./packages/package'):
        if (len(package.attrib) > 0 and package.attrib['isPrimary'] == 'true'):
            xml_manifestUrl = package.find('./actions/download/manifestUrl')
            return xml_manifestUrl.text

    return None

def get_exe_url(manifest_url):

    r = requests.get(manifest_url)
    if r.status_code != 200:
        raise Exception("\t[-] Error retrieving exe from xml manifest")
    
    xml_root = ET.fromstring(r.content)
    return xml_root.find('assetPath').text

def save_exe_to_file(exe_url, file_name):

    r = requests.get(exe_url)

    if r.status_code != 200:
        raise Exception("\t[-] Error retrieving exe file")

    with open(file_name, 'wb') as f:
        f.write(r.content)

    return


def get_file_name_from_url(url):
    
    path = urlparse(url).path
    file_name = os.path.basename(path)

    return file_name


if __name__ == '__main__':

    print("[+] Fetching manifest url")
    manifest_url = get_manifest_url()
    if manifest_url is None:
        raise Exception("\t[-] Manfiest url not found")

    print("[+] Fetching exe url")
    exe_url = get_exe_url(manifest_url)
    file_name = get_file_name_from_url(exe_url)
    print(f"[+] Downloading {file_name}")
    save_exe_to_file(exe_url, file_name)