import requests

def get_core_web_vitals(url, api_key):

    # URL de l'API PageSpeed Insights
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}&strategy=mobile"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Récupère la partie 'loadingExperience' (données de terrain)

        loading_exp = data.get("loadingExperience", {})
        metrics = loading_exp.get("metrics", {})

        # Extrait LCP, FID et CLS depuis les données réelles (si présentes)

        lcp_data = metrics.get("LARGEST_CONTENTFUL_PAINT_MS", {})
        inp_data = metrics.get("INTERACTION_TO_NEXT_PAINT", {})
        cls_data = metrics.get("CUMULATIVE_LAYOUT_SHIFT_SCORE", {})

        lcp = lcp_data.get("percentile")  # exprimé en millisecondes
        inp = inp_data.get("percentile")  # exprimé en millisecondes
        cls = cls_data.get("percentile")  # score (généralement très petit, ex: 0.07)

        return {
            "LCP": lcp / 1000,            # conversion en secondes
            "INP": inp,                   # maintenu en ms
            "CLS": cls / 100              # score sur 100
        }
    else:
        return {"error": "Erreur lors de l'appel à l'API"}

# Exemple d'utilisation

url = "https://www.lemonde.fr/"

#  Obtenir une clé API depuis Google Cloud Console

api_key = "VOTRE_CLE_API"  

core_web_vitals = get_core_web_vitals(url, api_key)
print(core_web_vitals)