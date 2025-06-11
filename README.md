# 🌐 Projecte Django - Marc Gómez

## 📌 Introducció
Aquest projecte ha estat creat com a pràctica de Django dins del mòdul de Programació.

## ⚙️ Instal·lació

```bash
#1. Clonar el repositori
git clone https://github.com/MarcGomezRufas/projecte-django.git

#2. Instal·lar les dependències crea aquest fitxer si cal
pip install -r requirements.txt

#3. Executar les migracions
python manage.py migrate 
```

## Execució
Per probar la seva execució necesites fer: python manage.py runserver

Visitar http://127.0.0.1:8000/ per accedir-hi.


## 📚 Documentació automàtica

La documentació dels fitxers `.py` es genera automàticament amb `pydoc` mitjançant un workflow de GitHub Actions. Pots consultar-la aquí:

🔗 [Veure documentació generada](https://marcgomezrufas.github.io/projecte-django/)

## GitHub Actions
Fitxer de CI ubicat a .github/workflows/docs.yml.

## Documentació Generada Enllaços
[models.py](https://marcgomezrufas.github.io/projecte-django/blog.models.html)
[views.py](https://marcgomezrufas.github.io/projecte-django/blog.views.html)
