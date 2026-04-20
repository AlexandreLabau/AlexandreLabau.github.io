#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_all.py — Applique toutes les modifications demandées sur site_perso_upgrade.html
"""
import shutil, os

SRC = r'C:\Users\opspo\Desktop\Alexandre\Claude\site_perso_upgrade.html'
BAK = SRC + '.bak'

shutil.copy2(SRC, BAK)
print(f'Sauvegarde : {BAK}')

with open(SRC, 'r', encoding='utf-8') as f:
    c = f.read()

original_len = len(c)

# ============================================================
# PARTIE 1 : SUBSTITUTIONS TEXTE
# ============================================================

def sub(old, new, text, label=''):
    if old not in text:
        print(f'  [WARN] NOT FOUND : {label or old[:60]}')
        return text
    print(f'  [OK]   {label or old[:60]}')
    return text.replace(old, new, 1)

print('\n=== Substitutions texte ===')

# 1. Titre onglet
c = sub('<title>Buck Engineering website</title>',
        '<title>Alexandre Labau</title>', c, 'title')

# 2. Fresque -> Frise (commentaire HTML + texte visible)
c = sub('<!-- ====== Fresque chronologique : Section dédiée ====== -->',
        '<!-- ====== Frise chronologique : Section dédiée ====== -->', c, 'commentaire Fresque->Frise')
c = sub('Fresque chronologique : glissez pour parcourir.',
        'Frise chronologique : glissez pour parcourir.', c, 'texte Fresque->Frise')

# 3. Buck Engineering : titre dans DATA
c = sub('title: "Fondateur : Auto-entrepreneur"',
        'title: "Création auto-entreprise, gestion et prestation de services"', c, 'Buck title')

# 4. Pony : titre dans DATA
c = sub('title: "Prestataire de services"',
        'title: "Ingénieur mécanique et qualification"', c, 'Pony title')

# 5. ESA id:5 : supprimer image
c = sub('image: "photo_ESTEC.jpg"', 'image: ""', c, 'ESA id5 image')

# 6. ESA id:6 : enrichir clients (Airbus + MTA + AVIO + SCADA)
c = sub(
    'clients:[{name:"ArianeGroup",logo:"logo_arianegroup.png"},{name:"GKN",logo:"logo_gkn.png"},{name:"Airbus",logo:"",initial:"A",color:"#00205B"}]',
    'clients:[{name:"ArianeGroup",logo:"logo_arianegroup.png"},{name:"GKN",logo:"logo_gkn.png"},{name:"Airbus",logo:"logo_airbus.png"},{name:"MT Aerospace",logo:"Logo_MT_Aerospace.png"},{name:"AVIO",logo:"",initial:"AV",color:"#1D3C6E"},{name:"SCADA",logo:"",initial:"SC",color:"#6B21A8"}]',
    c, 'ESA id6 clients')

# 7. Recommandation Pony : logo + nom
old_pony_reco = (
    '      <div class="reco-logo reco-logo--text" aria-hidden="true" '
    'style="width:60px;height:60px;border-radius:12px;background:linear-gradient(135deg,#16A34A,#15803D);'
    'display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1.3rem;color:#fff;flex-shrink:0">P</div>\n'
    '      <div class="reco-content">\n'
    '        <div class="reco-title" id="reco-pony-title">Pony : Lettre de recommandation</div>\n'
    '        <div class="reco-sub">Prestation de services : diagnostics mécaniques et électroniques, gestion logistique, CAO</div>'
)
new_pony_reco = (
    '      <img class="reco-logo" src="logo_pony.png" alt="Pony" '
    'style="width:60px;height:60px;object-fit:contain;border-radius:12px;background:#f0fdf4;'
    'padding:6px;border:1px solid #bbf7d0;flex-shrink:0">\n'
    '      <div class="reco-content">\n'
    '        <div class="reco-title" id="reco-pony-title">Pony : Lettre de recommandation</div>\n'
    '        <div class="reco-sub">Quentin Gerald, responsable ingénierie mécanique de Pony</div>'
)
c = sub(old_pony_reco, new_pony_reco, c, 'reco Pony logo+nom')

# 8. Entretien heading -> Questions / Réponses
c = sub('<h2 id="entretien-title" style="margin-bottom:8px">Entretien</h2>',
        '<h2 id="entretien-title" style="margin-bottom:8px">Questions / Réponses</h2>', c, 'entretien heading')
c = sub('<!-- ======= Section Entretien ======= -->',
        '<!-- ======= Section Q/R ======= -->', c, 'entretien comment')

# 9. EDF Hercule : remplacer logo EDF SVG par image locale
old_hercule = (
    '        <!-- Image centrale + légende -->\n'
    '        <figure class="edf-figure">\n'
    '          <img\n'
    '            src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/EDF_logo.svg/320px-EDF_logo.svg.png"\n'
    '            alt="Logo EDF"\n'
    '            class="edf-img-logo"\n'
    '          />\n'
    '        </figure>'
)
new_hercule = (
    '        <!-- Image projet Hercule (locale) -->\n'
    '        <figure class="edf-figure">\n'
    '          <img\n'
    '            src="projet hercule.jpg"\n'
    '            alt="Illustration du projet Hercule de restructuration EDF"\n'
    '            class="edf-img-wide"\n'
    '          />\n'
    '          <figcaption class="edf-figcaption">Illustration du projet Hercule de restructuration d\'EDF (2019\u20132022)</figcaption>\n'
    '        </figure>'
)
c = sub(old_hercule, new_hercule, c, 'EDF Hercule image locale')

# 10. EDF Organisation : remplacer logo EDF SVG par organigramme local
old_orga = (
    '        <figure class="edf-figure">\n'
    '          <img\n'
    '            src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/EDF_logo.svg/320px-EDF_logo.svg.png"\n'
    '            alt="EDF"\n'
    '            class="edf-img-logo"\n'
    '          />\n'
    '        </figure>'
)
new_orga = (
    '        <figure class="edf-figure">\n'
    '          <img\n'
    '            src="organigramme.png"\n'
    '            alt="Nouvelle organisation nucléaire EDF (avril 2024)"\n'
    '            class="edf-img-wide"\n'
    '          />\n'
    '          <figcaption class="edf-figcaption">Nouvelle architecture des activités nucléaires EDF depuis le 1<sup>er</sup> avril 2024</figcaption>\n'
    '        </figure>'
)
c = sub(old_orga, new_orga, c, 'EDF Organisation organigramme')

# 11. EDF Nucléaire : remplacer l'URL Wikimedia Flamanville par l'image locale
old_flam = (
    '            src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Centrale_de_Flamanville.jpg/640px-Centrale_de_Flamanville.jpg"\n'
    '            alt="Vue aérienne de la centrale nucléaire de Flamanville avec l\'EPR en construction"\n'
    '            class="edf-img-wide"'
)
new_flam = (
    '            src="flamanville3.png"\n'
    '            alt="Vue aérienne de la centrale nucléaire de Flamanville 3 (EPR)"\n'
    '            class="edf-img-wide"'
)
c = sub(old_flam, new_flam, c, 'EDF Flamanville image locale')

# 12. EDF NUWARD : remplacer URL Wikimedia (souvent 404) par image locale
old_nuward = (
    '            src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/NUWARD_SMR_EDF.jpg/640px-NUWARD_SMR_EDF.jpg"\n'
    '            alt="Représentation du réacteur SMR NUWARD développé par EDF"\n'
    '            class="edf-img-wide"\n'
    '            onerror="this.style.display=\'none\'; this.nextElementSibling.style.display=\'block\'"'
)
new_nuward = (
    '            src="nuward.jpg"\n'
    '            alt="Représentation du réacteur SMR NUWARD développé par EDF"\n'
    '            class="edf-img-wide"'
)
c = sub(old_nuward, new_nuward, c, 'EDF NUWARD image locale')

# Supprimer le div fallback devenu inutile après NUWARD
old_fallback = (
    '\n            <!-- Fallback si image indisponible -->\n'
    '            <div style="display:none; background:#f8fbfc; border:1px solid #e6eef2; border-radius:10px; padding:20px; text-align:center; color:#64748b; font-size:.9rem">\n'
    '              Représentation du SMR NUWARD : <a href="https://www.nuward.com/" target="_blank" rel="noopener" style="color:#0ea5a4">nuward.com</a>\n'
    '            </div>'
)
c = c.replace(old_fallback, '', 1)

# 13. EDF DIPDE : remplacer l'URL Wikimedia Bugey par l'image locale
old_bugey = (
    '            src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Centrale_du_Bugey.jpg/640px-Centrale_du_Bugey.jpg"\n'
    '            alt="Centrale nucléaire du Bugey, l\'un des 11 sites couverts par la DIPDE"\n'
    '            class="edf-img-wide"'
)
new_bugey = (
    '            src="centrale du bugey.jpg"\n'
    '            alt="Centrale nucléaire du Bugey, l\'un des 11 sites couverts par la DIPDE"\n'
    '            class="edf-img-wide"'
)
c = sub(old_bugey, new_bugey, c, 'EDF DIPDE Bugey image locale')

# 14. EDF MCP : remplacer l'URL Wikimedia schema REP par image locale
old_rep = (
    '            src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Schema_Reacteur_a_Eau_Pressurisee.svg/640px-Schema_Reacteur_a_Eau_Pressurisee.svg.png"\n'
    '            alt="Schéma d\'un réacteur à eau pressurisée : circuit primaire et secondaire"\n'
    '            class="edf-img-wide"'
)
new_rep = (
    '            src="schémareactuereaupressurisé.jpg"\n'
    '            alt="Schéma d\'un réacteur à eau pressurisée (REP) : circuits primaire et secondaire"\n'
    '            class="edf-img-wide"'
)
c = sub(old_rep, new_rep, c, 'EDF MCP schema REP image locale')

# 15. EDF EPR2 Penly : remplacer URL Wikimedia (typo SVG fermante dans la source)
# Corriger aussi la balise </figuresec → </figure>
old_penly_close = '</figuresec'
if '</figuresec' in c:
    c = c.replace('</figuresec', '</figure', 1)
    print('  [OK]   Correction </figuresec -> </figure')
else:
    print('  [OK]   </figuresec déjà corrigé')

# ============================================================
# PARTIE 2 : REMPLACEMENT DU BLOC NAV
# ============================================================
print('\n=== Nav ===')

old_nav = (
    '<nav>\n'
    '  <a href="#fresque">Parcours</a>\n'
    '  <a href="#education">Formation</a>\n'
    '  <a href="#edf">EDF</a>\n'
    '  <a href="#software-skills">Compétences</a>\n'
    '  <a href="#recommandations">Recommandations</a>\n'
    '  <a href="#entretien">Entretien</a>\n'
    '  <a href="#rapports">Rapports</a>\n'
    '  <a href="#contact">Contact</a>\n'
    '</nav>'
)
new_nav = (
    '<nav>\n'
    '  <a href="#fresque">Parcours</a>\n'
    '  <a href="#edf">EDF</a>\n'
    '  <a href="#entretien">Q / R</a>\n'
    '  <a href="#rapports">Rapports</a>\n'
    '  <a href="#recommandations">Recommandations</a>\n'
    '  <a href="#projects">Projets</a>\n'
    '  <a href="#software-skills">Compétences</a>\n'
    '  <a href="#backgrounds-gallery">Illustrations</a>\n'
    '</nav>'
)
c = sub(old_nav, new_nav, c, 'nav update')

# ============================================================
# PARTIE 3 : RÉORDONNANCEMENT DES SECTIONS VIA CSS ORDER
# ============================================================
# Approche propre : on utilise display:flex + order sur <main>
# pour éviter de déplacer physiquement de gros blocs HTML
print('\n=== CSS order pour sections ===')

order_css = """
<style id="section-order">
  /* Réordonnancement visuel des sections via flexbox */
  main { display: flex; flex-direction: column; }
  section.hero,
  #home  { order: 0; }
  #fresque { order: 10; }
  #education { order: 15; }
  #edf { order: 20; }
  #entretien { order: 30; }
  #rapports { order: 40; }
  #recommandations { order: 50; }
  #projects { order: 60; }
  #software-skills { order: 70; }
  #backgrounds-gallery { order: 80; }
  #skate-gallery { order: 90; }
  #trott-gallery { order: 95; }
  /* les <style> et <script> directs de <main> sont invisibles, order 0 */
</style>
"""

# Insérer juste avant </head>
if '<style id="section-order">' in c:
    print('  [OK]   section-order CSS déjà présent')
else:
    c = c.replace('</head>', order_css + '</head>', 1)
    print('  [OK]   CSS section-order injecté')

# ============================================================
# ÉCRITURE
# ============================================================
print(f'\nLongueur avant : {original_len}  après : {len(c)}')
if len(c) < 1000:
    print('  [ERREUR] Fichier trop court ! Annulation.')
else:
    with open(SRC, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Fichier écrit : {SRC}')
