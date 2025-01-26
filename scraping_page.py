import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        # Effectuer une requête HTTP GET
        response = requests.get(url, timeout=10)
        status_code = response.status_code

        # Vérifier si la requête a réussi
        if status_code != 200:
            return {
                "url": url,
                "status_code": status_code,
                "title": None,
                "h1": None,
                "meta_description": None,
                "canonical": None,
            }

        # Analyser le contenu HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Récupérer le title
        title = soup.title.string.strip() if soup.title else None

        # Récupérer le premier H1
        h1 = soup.find('h1').get_text(strip=True) if soup.find('h1') else None

        # Récupérer la meta description
        meta_description_tag = soup.find('meta', attrs={'name': 'description'})
        meta_description = meta_description_tag['content'].strip() if meta_description_tag else None

        # Récupérer la balise canonical
        canonical_tag = soup.find('link', attrs={'rel': 'canonical'})
        canonical = canonical_tag['href'].strip() if canonical_tag else None

        return {
            "url": url,
            "status_code": status_code,
            "title": title,
            "h1": h1,
            "meta_description": meta_description,
            "canonical": canonical,
        }

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return {
            "url": url,
            "status_code": None,
            "title": None,
            "h1": None,
            "meta_description": None,
            "canonical": None,
        }


url = "https://www.matthieucasiez.com/fr/"
result = scrape_page(url)
for key, value in result.items():
  print(f"{key}: {value}")