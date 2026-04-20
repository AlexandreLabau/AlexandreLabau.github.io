#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""patch_v5.py — toutes les modifications demandées"""
import shutil, re

SRC = r'C:\Users\opspo\Desktop\Alexandre\Claude\site_perso_upgrade.html'
BAK = SRC + '.bak5'
shutil.copy2(SRC, BAK)
print(f'Backup : {BAK}')

with open(SRC, 'r', encoding='utf-8') as f:
    c = f.read()
orig = len(c)

def sub(label, old, new, text):
    if old not in text:
        print(f'  [WARN] NOT FOUND : {label}')
        return text
    print(f'  [OK]   {label}')
    return text.replace(old, new, 1)

# ─────────────────────────────────────────────────────────────
# 1. HERO DESCRIPTION
# ─────────────────────────────────────────────────────────────
c = sub('hero description',
    'Titulaire d\u2019un double dipl\u00f4me de master en G\u00e9nie M\u00e9canique et \u00c9nerg\u00e9tique (KTH Stockholm / Grenoble INP \u2013 ENSE3), je cherche \u00e0 mettre mes comp\u00e9tences en simulation, qualification d\u2019\u00e9quipements et r\u00e9daction technique au service de projets industriels exigeants dans l\u2019\u00e9nergie et l\u2019ing\u00e9nierie avanc\u00e9e.',
    'Titulaire d\u2019un double dipl\u00f4me international en M\u00e9canique et \u00c9nerg\u00e9tique entre KTH \u00c9cole Royale Polytechnique de Stockholm et Grenoble INP \u2013 ENSE3, je souhaite contribuer activement \u00e0 la transition \u00e9nerg\u00e9tique, plus sp\u00e9cifiquement dans le domaine de la production d\u2019\u00e9nergie nucl\u00e9aire.',
    c)

# ─────────────────────────────────────────────────────────────
# 2. LÉGENDE PHOTO ESTEC
# ─────────────────────────────────────────────────────────────
c = sub('légende photo ESTEC (alt)',
    'alt="Soutenance de th\u00e8se au Centre europ\u00e9en de recherche et de technologie spatiale (ESTEC)"',
    'alt="Pr\u00e9sentation de l\u2019application de Maintenance Pr\u00e9dictive devant des industriels lors d\u2019une conf\u00e9rence europ\u00e9enne \u00e0 l\u2019ESTEC"',
    c)
c = sub('légende photo ESTEC (figcaption)',
    'Soutenance de th\u00e8se au Centre europ\u00e9en de recherche et de technologie spatiale (ESTEC)',
    'Pr\u00e9sentation de l\u2019application de Maintenance Pr\u00e9dictive d\u00e9velopp\u00e9e devant des industriels et des experts du domaine lors d\u2019une conf\u00e9rence europ\u00e9enne aux Pays-Bas (ESTEC)',
    c)

# ─────────────────────────────────────────────────────────────
# 3. SABCA DANS ID:6 CLIENTS
# ─────────────────────────────────────────────────────────────
c = sub('SABCA client id6',
    '        { name: "SCADA", logo: "", initial: "SC", color: "#6B21A8" }\n      ]',
    '        { name: "SCADA", logo: "", initial: "SC", color: "#6B21A8" },\n        { name: "SABCA", logo: "logo_SABCA.png" }\n      ]',
    c)

# ─────────────────────────────────────────────────────────────
# 4. EDF IMAGES : object-fit cover → contain (voir toute l'image)
# ─────────────────────────────────────────────────────────────
c = sub('edf-img-wide object-fit',
    'width:100%; max-height:280px; object-fit:cover; border-radius:12px;',
    'width:100%; max-height:320px; object-fit:contain; border-radius:12px; background:#f8fbfc;',
    c)

# ─────────────────────────────────────────────────────────────
# 5. ORGANISATION : supprimer le bloc figure organigramme (qui ne fonctionne pas)
# ─────────────────────────────────────────────────────────────
old_orga_fig = (
    '\n        <figure class="edf-figure">\n'
    '          <img\n'
    '            src="organigramme.png"\n'
    '            alt="Nouvelle organisation nucl\u00e9aire EDF (avril 2024)"\n'
    '            class="edf-img-wide"\n'
    '          />\n'
    '          <figcaption class="edf-figcaption">Nouvelle architecture des activit\u00e9s nucl\u00e9aires EDF depuis le 1<sup>er</sup> avril 2024</figcaption>\n'
    '        </figure>'
)
c = sub('suppression figure organigramme', old_orga_fig, '', c)

# ─────────────────────────────────────────────────────────────
# 6. PENLY : remplacer URL Wikimedia par image locale
# ─────────────────────────────────────────────────────────────
c = sub('Penly image locale',
    'src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Centrale_nucl%C3%A9aire_de_Penly.jpg/640px-Centrale_nucl%C3%A9aire_de_Penly.jpg"',
    'src="centrale de penly.jpg"',
    c)

# ─────────────────────────────────────────────────────────────
# 7. LIENS : Grand Carénage, Organisation, SFEN NUWARD
# ─────────────────────────────────────────────────────────────
c = sub('lien Grand Carénage',
    'href="https://www.edf.fr/groupe-edf/produire-une-energie-respectueuse-du-climat/lenergie-nucleaire/notre-parc-nucleaire/le-grand-carenage"',
    'href="https://www.edf.fr/groupe-edf/innover/rd-un-savoir-faire-mondial/la-rd-et-le-grand-carenage"',
    c)

c = sub('lien Organisation prod nucl',
    'href="https://www.edf.fr/groupe-edf/notre-groupe/nos-metiers/production-nucleaire"',
    'href="https://www.edf.fr/edf-recrute/nos-metiers/decouvrez-les-metiers-du-groupe-edf/rejoignez-nos-equipes-de-la-production-et-de-l-ingenierie-nucleaire"',
    c)

# Supprimer le lien SFEN NUWARD (ligne entière)
c = sub('suppression lien SFEN NUWARD',
    '\n            <a class="edf-source-link" href="https://www.sfen.org/rgn/nuward-le-smr-francais/" target="_blank" rel="noopener">SFEN : NUWARD, le SMR fran\u00e7ais</a>',
    '',
    c)

# ─────────────────────────────────────────────────────────────
# 8. SUPPRIMER SECTION ILLUSTRATIONS (backgrounds-gallery)
#    On la masque via CSS (plus propre que supprimer le HTML)
# ─────────────────────────────────────────────────────────────
c = sub('masquer illustrations CSS',
    '#backgrounds-gallery { order: 80; }',
    '#backgrounds-gallery { display: none !important; }',
    c)

# Aussi masquer skate et trott galleries
c = sub('masquer skate-gallery CSS',
    '#skate-gallery { order: 90; }',
    '#skate-gallery { display: none !important; }',
    c)
c = sub('masquer trott-gallery CSS',
    '#trott-gallery { order: 95; }',
    '#trott-gallery { display: none !important; }',
    c)

# ─────────────────────────────────────────────────────────────
# 9. CSS ORDER : Formation (catalogue) juste avant Compétences
# ─────────────────────────────────────────────────────────────
c = sub('CSS order education avant skills',
    '#education { order: 15; }',
    '#education { order: 65; }',
    c)

# ─────────────────────────────────────────────────────────────
# 10. RAPPORTS : déplacer les 3 KTH à la fin
# ─────────────────────────────────────────────────────────────
# Extraire les 3 blocs KTH à déplacer
kth_aero = (
    '\n    <a class="report-card" href="https://github.com/AlexandreLabau/AlexandreLabau.github.io/releases/download/v2/report_kth_aeroelasticity.pdf" target="_blank">\n'
    '      <img class="report-logo" src="logo_kth.png" alt="KTH">\n'
    '      <span>A\u00e9ro\u00e9lasticit\u00e9 appliqu\u00e9e \u00e0 l\u2019avion Windex</span>\n'
    '    </a>\n'
)
kth_comp = (
    '\n    <a class="report-card" href="https://github.com/AlexandreLabau/AlexandreLabau.github.io/releases/download/v2/report_kth_fibre_composites.pdf" target="_blank">\n'
    '      <img class="report-logo" src="logo_kth.png" alt="KTH">\n'
    '      <span>Mat\u00e9riaux composites fibreux\xa0: Analyse et conception\xa0: Probl\u00e8me de conception\xa0: FEM &amp; Python</span>\n'
    '    </a>\n'
)
kth_fund = (
    '\n    <a class="report-card" href="https://github.com/AlexandreLabau/AlexandreLabau.github.io/releases/download/v2/report_kth_fundamentals.pdf" target="_blank">\n'
    '      <img class="report-logo" src="logo_kth.png" alt="KTH">\n'
    '      <span>\u00c9valuation comparative des lanceurs r\u00e9utilisables et \u00e0 usage unique</span>\n'
    '    </a>\n'
)

# Vérifier s'ils existent avec le format exact en cherchant des fragments clés
found_aero = 'report_kth_aeroelasticity.pdf' in c
found_comp = 'report_kth_fibre_composites.pdf' in c
found_fund = 'report_kth_fundamentals.pdf' in c
print(f'  KTH aero found: {found_aero}, comp: {found_comp}, fund: {found_fund}')

# Fin du rapport Hercule (ancre pour insérer après)
hercule_end = (
    '    <a class="report-card" href="https://github.com/AlexandreLabau/AlexandreLabau.github.io/releases/download/v2/report_ense3_Hercule.pdf" target="_blank">\n'
    '      <img class="report-logo" src="logo_ense3.png" alt="ENSE3">\n'
    '      <span>Energy Issues: Hercule Project</span>\n'
    '    </a>\n'
    '\n'
    '\n'
    '  </div>\n'
    '</section>'
)

# Approche robuste : extraire les blocs par regex et réordonner
# Chercher les 3 blocs KTH par leurs URLs uniques
def extract_report_block(text, url_fragment):
    """Extrait un bloc <a class="report-card"...> complet"""
    pattern = r'\n    <a class="report-card" href="[^"]*' + re.escape(url_fragment) + r'[^"]*"[^>]*>.*?</a>\n'
    m = re.search(pattern, text, re.DOTALL)
    if m:
        return m.group(0)
    return None

block_aero = extract_report_block(c, 'kth_aeroelasticity')
block_comp = extract_report_block(c, 'kth_fibre_composites')
block_fund = extract_report_block(c, 'kth_fundamentals')

print(f'  Extracted blocks: aero={bool(block_aero)}, comp={bool(block_comp)}, fund={bool(block_fund)}')

if block_aero and block_comp and block_fund:
    # 1. Retirer les 3 blocs de leur position actuelle
    c = c.replace(block_aero, '', 1)
    c = c.replace(block_comp, '', 1)
    c = c.replace(block_fund, '', 1)
    # 2. Les insérer après le rapport Hercule
    hercule_marker = '      <span>Energy Issues: Hercule Project</span>\n    </a>'
    insert_after = hercule_marker + '\n' + block_aero + block_comp + block_fund
    c = c.replace(hercule_marker, insert_after, 1)
    print('  [OK]   Rapports KTH déplacés en fin de liste')
else:
    print('  [WARN] Impossible d\'extraire les blocs KTH — vérifier le format')

# ─────────────────────────────────────────────────────────────
# 11. NETTOYER LES TIRETS VISIBLES dans les spans rapports
#     (remplacer " : " par " \u2013 " non, garder les ":")
#     Supprimer les double-points en série abusifs
# ─────────────────────────────────────────────────────────────
# Rapports : remplacer les patterns " : Problème de conception : FEM" par une formulation plus naturelle
c = sub('rapport KTH composites titre',
    '<span>Mat\u00e9riaux composites fibreux\xa0: Analyse et conception\xa0: Probl\u00e8me de conception\xa0: FEM &amp; Python</span>',
    '<span>Mat\u00e9riaux composites fibreux, analyse et conception (FEM &amp; Python)</span>',
    c)
c = sub('rapport KTH composites titre v2',
    '<span>Mat\u00e9riaux composites fibreux : Analyse et conception : Probl\u00e8me de conception : FEM &amp; Python</span>',
    '<span>Mat\u00e9riaux composites fibreux, analyse et conception (FEM &amp; Python)</span>',
    c)
c = sub('rapport skate tiret',
    '<span>Conception et mod\u00e9lisation m\u00e9canique : Skateboard</span>',
    '<span>Conception et mod\u00e9lisation m\u00e9canique d\u2019un skateboard</span>',
    c)
c = sub('rapport trott tiret',
    '<span>Conception et mod\u00e9lisation m\u00e9canique : Trottinette</span>',
    '<span>Conception et mod\u00e9lisation m\u00e9canique d\u2019une trottinette</span>',
    c)
c = sub('rapport KTH taxi tiret',
    '<span>Conception de v\u00e9hicule : Taxi spatial pour deux personnes : Vol habit\u00e9</span>',
    '<span>Conception d\u2019un taxi spatial pour deux personnes (vol habit\u00e9)</span>',
    c)

# ─────────────────────────────────────────────────────────────
# 12. Q/R : RÉÉCRITURE COMPLÈTE
# ─────────────────────────────────────────────────────────────
old_qa_list = c[c.find('<div class="qa-list"'):c.find('</div>\n</section>\n\n<style>\n  .qa-list')+6]

new_qa_list = '''<div class="qa-list" style="margin-top:20px">

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi EDF ?</button>
      <div class="qa-a" hidden>
        <p>Ce qui me parle vraiment chez EDF, c'est l'échelle et la rigueur. Gérer 56 réacteurs qui couvrent 70 % de la production électrique française, avec des enjeux de sûreté qui imposent de travailler bien plutôt que vite, c'est un environnement qui correspond à ce que je cherche. À l'ESA, j'ai découvert ce type de culture : chaque document compte, chaque décision technique est tracée et justifiée. Je veux retrouver exactement ça, et EDF est probablement l'endroit en France où cette exigence existe le plus dans la production d'énergie.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi le nucléaire ?</button>
      <div class="qa-a" hidden>
        <p>C'est une question que je me suis posée sincèrement en sortant de mes études. J'aurais pu partir dans le renouvelable, l'automobile ou l'aéronautique. Mais j'ai regardé les chiffres : si l'objectif est de décarboner le mix énergétique sérieusement et rapidement, le nucléaire est incontournable. Ce n'est pas une position idéologique, c'est une conclusion technique. Et honnêtement, la complexité des systèmes me fascine : un réacteur REP c'est de la thermodynamique, de la mécanique des fluides, des matériaux sous contraintes sévères, de la sûreté, de la réglementation. Il y a de quoi apprendre pendant toute une carrière.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi la DIPDE ?</button>
      <div class="qa-a" hidden>
        <p>La DIPDE travaille sur le parc en exploitation, pas sur de la construction neuve. Ce que j'aime là-dedans, c'est que les décisions ont un impact direct et immédiat sur la production. Quand on qualifie un équipement de remplacement, c'est une tranche qui peut continuer à tourner. Ce lien entre le travail d'ingénierie et le résultat concret, c'est quelque chose qui me motive. La DIPDE gère aussi des sujets de prolongation de durée de vie et de conformité réglementaire, ce qui rejoint directement la culture de rigueur que j'ai développée à l'ESA.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi le service MCP ?</button>
      <div class="qa-a" hidden>
        <p>Robinetterie, production de froid, moto-ventilateurs : ce sont des systèmes mécaniques et thermiques que je connais bien. Ma formation en thermo-hydraulique, mécanique des fluides, échangeurs de chaleur et modélisation mécanique s'applique directement là. Je n'arrive pas sans bagages. Et la qualification de ces équipements, démontrer qu'ils tiennent en conditions accidentelles, c'est exactement la démarche que j'ai pratiquée à l'ESA avec les normes ECSS. C'est le service où je peux être opérationnel rapidement tout en apprenant le référentiel nucléaire.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi la qualification ?</button>
      <div class="qa-a" hidden>
        <p>Ce qui me plaît dans la qualification, c'est qu'il n'y a pas d'ambiguïté : à la fin d'un dossier, soit l'équipement est qualifié soit il ne l'est pas. Il faut démontrer, pas seulement affirmer. À l'ESA, j'ai travaillé avec les normes ECSS : analyses FEM sous ANSYS, enveloppes thermiques et vibratoires, rédaction de rapports techniques structurés. C'est la même logique transposée au référentiel nucléaire. Et franchement, le fait que l'enjeu soit la sûreté d'un réacteur en exploitation rend ça encore plus sérieux et stimulant.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Quels sont vos projets à long terme ?</button>
      <div class="qa-a" hidden>
        <p>Honnêtement, je veux rester à EDF. Ce n'est pas une réponse de façade. Dans le nucléaire, la maîtrise du contexte réglementaire et des systèmes prend des années, ça n'a pas de sens de changer d'entreprise tous les trois ans. Ce qui m'intéresse, c'est d'évoluer à l'intérieur : devenir référent technique sur un type d'équipement au MCP, élargir vers d'autres services de la DIPDE ou de la DISC, et peut-être prendre des responsabilités de coordination un jour. Je suis aussi prêt à bouger géographiquement si un poste ou une mission l'exige.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Quelle est l'expérience qui vous a le plus marqué ?</button>
      <div class="qa-a" hidden>
        <p>Mon stage à l'ESA, sans hésiter. Pas parce que c'est impressionnant sur un CV, mais parce que c'est là où j'ai travaillé comme ingénieur avec de vraies contraintes. J'ai développé une application Python de maintenance prédictive aujourd'hui en production chez eux, conduit des études thermo-hydrauliques et appris à fonctionner dans un cadre normatif strict. Le stage a été prolongé, ce qui voulait dire quelque chose sur la qualité du travail fourni. C'est là aussi que j'ai compris que le type d'environnement rigoureux et technique avec des livrables qui comptent est exactement celui dans lequel je veux travailler.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Comment décririez-vous votre profil en quelques mots ?</button>
      <div class="qa-a" hidden>
        <p>Ingénieur mécanique avec une vraie base en simulation numérique et thermo-hydraulique, capable de rédiger des dossiers techniques et de travailler sur des problèmes complexes en autonomie. J'ai fait de la CFD, de la FEM, du Python, de la CAO. J'ai travaillé en équipe internationale à l'ESA et géré des projets en auto-entrepreneur. Ce qui me distingue peut-être, c'est que je ne suis pas seulement à l'aise avec les outils : j'aime comprendre pourquoi les choses fonctionnent ou pas, et j'ai un intérêt sincère pour la démarche documentaire et normative, ce qui est directement utile pour la qualification.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi un double diplôme franco-suédois ?</button>
      <div class="qa-a" hidden>
        <p>Je voulais voir comment on enseigne et travaille ailleurs. KTH est l'une des meilleures écoles techniques d'Europe du Nord, avec une approche très orientée recherche et projets pratiques. Combiner ça avec la rigueur thermique et mécanique de Grenoble INP m'a donné une formation vraiment solide et complémentaire. Sur le plan personnel, vivre à Stockholm pendant un an, travailler en anglais au quotidien et comprendre d'autres façons d'aborder les problèmes d'ingénierie, c'était aussi ça l'objectif. Je ne regrette pas.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Parlez-moi de votre expérience chez Buck Engineering.</button>
      <div class="qa-a" hidden>
        <p>J'ai créé une auto-entreprise pour proposer des prestations d'ingénierie à des clients professionnels et des particuliers. Ce qui m'a le plus appris, c'est la rédaction de cahiers des charges, le cadrage du besoin et le suivi des exigences quand le besoin évolue. Ce n'est pas le même contexte que le nucléaire, évidemment. Mais la rigueur dans la rédaction technique, la gestion des écarts par rapport aux spécifications et la relation client, ça s'est construit en conditions réelles. C'est une expérience qui complète bien ma formation académique.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Comment démontrez-vous la tenue d'un équipement en conditions accidentelles ?</button>
      <div class="qa-a" hidden>
        <p>La démarche passe par plusieurs étapes. D'abord, définir les conditions enveloppantes : séismes selon la carte sismique du site, accidents de perte de réfrigérant primaire, variations de température et de pression. Ensuite, mobiliser les leviers de démonstration selon le type d'équipement : calcul analytique ou par éléments finis pour les contraintes mécaniques, essais de qualification sous conditions LOCA, ou retour d'expérience sur des équipements similaires déjà qualifiés. À l'ESA j'ai appliqué une logique comparable sur des équipements spatiaux : enveloppes thermiques et vibratoires, analyses FEM sous ANSYS, rapports de qualification en anglais. La transposition au référentiel nucléaire est une continuité directe.</p>
      </div>
    </div>

  </div>'''

# Trouver le bloc à remplacer
qa_start_marker = '<div class="qa-list" style="margin-top:20px">'
qa_end_marker = '  </div>\n</section>\n\n<style>\n  .qa-list'

idx_start = c.find(qa_start_marker)
idx_end   = c.find(qa_end_marker)

if idx_start >= 0 and idx_end >= 0:
    c = c[:idx_start] + new_qa_list + c[idx_end + len('  </div>'):]
    print('  [OK]   Q/R réécrit')
else:
    print(f'  [WARN] Q/R bloc non trouvé (start={idx_start}, end={idx_end})')

# ─────────────────────────────────────────────────────────────
# 13. SUPPRESSION DES EM DASHES ET TIRETS LONGS dans texte visible
#     (déjà fait pour les nouvelles Q/R, vérifier le reste)
# ─────────────────────────────────────────────────────────────
# Dans les réponses déjà écrites et ailleurs : remplacer — et – par des virgules ou espaces
# On cible uniquement le HTML visible (pas dans href, src, etc.)
c_lines = c.split('\n')
cleaned = []
for line in c_lines:
    stripped = line.strip()
    # Ne pas toucher aux attributs href, src, class, id, etc.
    if stripped.startswith('href=') or stripped.startswith('src=') or stripped.startswith('class=') or '//' in stripped[:4]:
        cleaned.append(line)
        continue
    # Remplacer em dash (—) par virgule+espace ou juste espace selon contexte
    line = line.replace('\u2014', ',')   # em dash → virgule
    # Ne pas remplacer en-dash dans les dates/chiffres (ex: 2019–2022 → OK)
    # Mais remplacer en-dash utilisé comme séparateur avec espaces
    line = re.sub(r' \u2013 ', ', ', line)  # " – " → ", "
    cleaned.append(line)
c = '\n'.join(cleaned)
print('  [OK]   Nettoyage em/en dashes dans le texte')

# ─────────────────────────────────────────────────────────────
# 14. NAV : supprimer le lien "Illustrations" devenu inutile
# ─────────────────────────────────────────────────────────────
c = sub('nav illustrations retrait',
    '\n  <a href="#backgrounds-gallery">Illustrations</a>',
    '',
    c)

# ─────────────────────────────────────────────────────────────
# ÉCRITURE
# ─────────────────────────────────────────────────────────────
print(f'\nLongueur avant : {orig}  après : {len(c)}')
if len(c) < 100000:
    print('[ERREUR] Fichier trop court ! Annulation.')
else:
    with open(SRC, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Fichier écrit : {SRC}')
