import requests
import gzip
import xml.etree.ElementTree as ET
import pandas as pd
from io import BytesIO

def fetch_urls_from_sitemap(sitemap_url):
    urls = []
    response = requests.get(sitemap_url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch sitemap: {sitemap_url}")

    content = response.content

    if sitemap_url.endswith('.gz'):
        with gzip.GzipFile(fileobj=BytesIO(content)) as f:
            content = f.read()
    root = ET.fromstring(content)

    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    if root.tag.endswith('sitemapindex'):
        for sitemap in root.findall('ns:sitemap', namespace):
            loc = sitemap.find('ns:loc', namespace).text
            urls.extend(fetch_urls_from_sitemap(loc))
    elif root.tag.endswith('urlset'):
        for url in root.findall('ns:url', namespace):
            loc = url.find('ns:loc', namespace).text
            urls.append(loc)

    return urls

### Appel de la fonction dans Google Colab

sitemap_url = input("Entrer l'URL du sitemap : ")

try:
  extracted_urls = fetch_urls_from_sitemap(sitemap_url)
  print(f"Extraction de {len(extracted_urls)} URL.")

  df = pd.DataFrame(extracted_urls, columns=['URL'])

  output_file = "urls_sitemap.xlsx"
  df.to_excel(output_file, index=False)
  print(f"URL sauvegardées : {output_file}.")

except Exception as e:
  print(f"Error: {e}")