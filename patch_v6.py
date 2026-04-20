#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""patch_v6.py — Q/R enrichies + réordonnancement onglets EDF"""
import shutil

SRC = r'C:\Users\opspo\Desktop\Alexandre\Claude\site_perso_upgrade.html'
BAK = SRC + '.bak6'
shutil.copy2(SRC, BAK)

with open(SRC, 'r', encoding='utf-8') as f:
    c = f.read()
orig = len(c)

def sub(label, old, new, text):
    if old not in text:
        print(f'  [WARN] NOT FOUND : {label}')
        return text
    print(f'  [OK]   {label}')
    return text.replace(old, new, 1)

# ═══════════════════════════════════════════════════════════════
#  1. RÉORDONNANCEMENT ONGLETS EDF
# ═══════════════════════════════════════════════════════════════

# 1a. Boutons : Projets Nucléaires en premier (actif), Hercule en dernier
old_tabs = (
    '    <button class="edf-tab is-active" role="tab" aria-selected="true" aria-controls="edf-hercule" id="tab-edf-hercule">Projet Hercule</button>\n'
    '    <button class="edf-tab" role="tab" aria-selected="false" aria-controls="edf-nucleaire" id="tab-edf-nucleaire">Projets Nucléaires</button>\n'
    '    <button class="edf-tab" role="tab" aria-selected="false" aria-controls="edf-orga" id="tab-edf-orga">Organisation</button>\n'
    '    <button class="edf-tab" role="tab" aria-selected="false" aria-controls="edf-dipde" id="tab-edf-dipde">La DIPDE</button>'
)
new_tabs = (
    '    <button class="edf-tab is-active" role="tab" aria-selected="true" aria-controls="edf-nucleaire" id="tab-edf-nucleaire">Projets Nucléaires</button>\n'
    '    <button class="edf-tab" role="tab" aria-selected="false" aria-controls="edf-orga" id="tab-edf-orga">Organisation</button>\n'
    '    <button class="edf-tab" role="tab" aria-selected="false" aria-controls="edf-dipde" id="tab-edf-dipde">La DIPDE</button>\n'
    '    <button class="edf-tab" role="tab" aria-selected="false" aria-controls="edf-hercule" id="tab-edf-hercule">Projet Hercule</button>'
)
c = sub('onglets EDF réordonnés', old_tabs, new_tabs, c)

# 1b. Panneaux : edf-nucleaire visible (pas hidden), edf-hercule hidden
c = sub('panel nucleaire visible',
    '<div id="edf-nucleaire" class="edf-panel" role="tabpanel" aria-labelledby="tab-edf-nucleaire" hidden>',
    '<div id="edf-nucleaire" class="edf-panel" role="tabpanel" aria-labelledby="tab-edf-nucleaire">',
    c)
c = sub('panel hercule caché',
    '<div id="edf-hercule" class="edf-panel" role="tabpanel" aria-labelledby="tab-edf-hercule">',
    '<div id="edf-hercule" class="edf-panel" role="tabpanel" aria-labelledby="tab-edf-hercule" hidden>',
    c)

# ═══════════════════════════════════════════════════════════════
#  2. Q/R : RÉÉCRITURE COMPLÈTE ET ENRICHIE
# ═══════════════════════════════════════════════════════════════

new_qa = '''<div class="qa-list" style="margin-top:20px">

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi EDF ?</button>
      <div class="qa-a" hidden>
        <p>Pendant mon stage à l\'ESA, j\'ai travaillé dans une organisation où chaque décision technique avait une trace documentaire, où la rigueur n\'était pas optionnelle. Au début ça peut sembler lourd, mais très vite on comprend pourquoi : quand les systèmes sont critiques, on n\'a pas le droit à l\'improvisation. EDF, c\'est exactement cette culture poussée à son niveau maximal. 56 réacteurs en exploitation, des exigences de sûreté pilotées par l\'ASNR, des référentiels techniques qui couvrent chaque aspect de la conception et de la maintenance.</p>
        <p>Ce qui m\'attire aussi, c\'est la pérennité. Dans le nucléaire, on parle d\'horizons à 40, 60 ans. On peut construire une vraie expertise, pas juste passer d\'un projet à l\'autre tous les deux ans. Et EDF est l\'acteur central de la production électrique française dans un contexte où la question énergétique devient de plus en plus critique. C\'est un endroit où le travail d\'ingénieur a un impact réel et durable.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi le nucléaire ?</button>
      <div class="qa-a" hidden>
        <p>J\'avais le choix en sortant du double diplôme. Avec une formation en mécanique et énergétique, l\'automobile, l\'aéronautique, les renouvelables étaient tous accessibles. J\'ai pris le temps d\'y réfléchir vraiment. Ce qui m\'a convaincu, c\'est d\'abord la question de fond sur la transition énergétique. Si l\'objectif est de produire massivement une énergie décarbonée et pilotable, le nucléaire est la seule technologie mature à grande échelle aujourd\'hui. Ce n\'est pas une position idéologique, c\'est une lecture des données.</p>
        <p>Ensuite, il y a la complexité des systèmes. Un réacteur REP, c\'est de la thermo-hydraulique, de la mécanique des structures, de la chimie des fluides, des matériaux sous irradiation, de la sûreté, de la réglementation. J\'ai des bases solides dans ces domaines, et je sais que je n\'en ferai pas le tour en deux ans. La profondeur technique disponible est exactement ce que je cherche dans un poste. Et le fait que la dimension sûreté soit structurelle, non négociable, c\'est quelque chose qui me convient. Je n\'ai pas besoin qu\'on me rappelle pourquoi il faut bien travailler.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi la DIPDE ?</button>
      <div class="qa-a" hidden>
        <p>La DIPDE opère là où l\'ingénierie a un impact direct : le parc en exploitation. Quand on travaille sur la modification ou la qualification d\'un équipement pour une tranche en fonctionnement, le résultat est concret et mesurable. Ce n\'est pas de la R&amp;D qui aboutira dans dix ans, c\'est un dossier qui conditionne la disponibilité d\'un réacteur aujourd\'hui ou dans six mois.</p>
        <p>Ce qui me plaît aussi, c\'est la diversité des sujets au sein de la DIPDE : gestion des obsolescences, modifications matérielles, qualification initiale ou de remplacement, prolongation de durée de vie dans le cadre du Grand Carénage et des visites décennales. Il y a une profondeur technique réelle sur le long terme. La DIPDE est aussi le lien opérationnel entre les exigences de l\'exploitant, les référentiels de conception comme les RCC-M et RCC-E, et les prescriptions de l\'ASNR. Pour quelqu\'un qui arrive avec une culture de documentation et de traçabilité forgée à l\'ESA, c\'est un environnement qui fait immédiatement sens.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi le service MCP ?</button>
      <div class="qa-a" hidden>
        <p>Le MCP gère la robinetterie, la production de froid et les moto-ventilateurs pour l\'ensemble des tranches REP en exploitation. Ce sont des équipements mécaniques et thermiques, c\'est-à-dire précisément le périmètre de ma formation : thermo-hydraulique, mécanique des fluides, transferts thermiques, modélisation mécanique. Je ne pars pas de zéro sur la compréhension des systèmes physiques impliqués.</p>
        <p>La qualification de ces équipements représente un enjeu fort : démontrer qu\'une vanne ou un moto-ventilateur remplit sa fonction de sûreté en conditions normales, incidentelles et accidentelles (LOCA, séisme, transitoires thermiques) demande une démarche rigoureuse combinant calcul, essais et retour d\'expérience. C\'est exactement le type de travail que j\'ai pratiqué à l\'ESA sur des équipements spatiaux avec les normes ECSS. Le MCP est aussi l\'un des services où la rigueur de la qualification est la plus exigeante, précisément parce que les équipements concernés sont sur les circuits primaires. C\'est là que je veux commencer.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi la qualification ?</button>
      <div class="qa-a" hidden>
        <p>La qualification est une démarche de preuve : on prend un équipement, on définit ses conditions d\'emploi et ses sollicitations enveloppantes, et on démontre de façon structurée et traçable qu\'il peut remplir sa fonction dans ces conditions. Ce qui m\'attire dans cette approche, c\'est l\'absence d\'ambiguïté. Soit la démonstration est faite selon les critères du référentiel, soit elle ne l\'est pas. On ne peut pas contourner.</p>
        <p>À l\'ESA, j\'ai travaillé avec les normes ECSS qui imposent exactement cette logique sur les équipements spatiaux : analyses FEM sous ANSYS pour la tenue structurelle, enveloppes thermiques et vibratoires, rédaction de rapports justificatifs en anglais. Le cœur de la démarche (identifier les sollicitations, définir les critères d\'acceptation, choisir la méthode de démonstration entre calcul, essai et retour d\'expérience, puis constituer le dossier) se transpose directement au nucléaire. Les référentiels sont différents (RCC-M, RCC-E, guides ASNR), mais la logique est identique. Et l\'enjeu, la sûreté d\'un réacteur en exploitation, donne encore plus de sens à chaque dossier.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Quels sont vos projets à long terme ?</button>
      <div class="qa-a" hidden>
        <p>Je veux rester à EDF. Ce n\'est pas une réponse calculée pour l\'entretien, c\'est ma position réelle. Dans le nucléaire, l\'expertise ne se construit pas vite. Comprendre les référentiels en profondeur, maîtriser les processus de qualification, connaître les systèmes et leur historique d\'exploitation, ça prend plusieurs années et ça n\'a de valeur que si on reste assez longtemps pour en faire quelque chose d\'utile.</p>
        <p>À moyen terme, ce qui m\'intéresse c\'est de devenir autonome et compétent sur les processus de qualification au MCP, puis d\'élargir progressivement vers d\'autres équipements ou d\'autres services de la DIPDE et de la DISC. À plus long terme, j\'aimerais prendre une forme de responsabilité technique, référent sur un domaine, coordination de qualifications sur des projets de modification. Je suis aussi mobile géographiquement. Si une opportunité intéressante se présente sur un autre site ou dans une autre direction, je suis prêt à bouger. Ce qui compte, c\'est de continuer à progresser sur des sujets techniquement exigeants au sein du groupe EDF.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Quelle est l\'expérience qui vous a le plus marqué ?</button>
      <div class="qa-a" hidden>
        <p>Mon stage à l\'ESA, sans hésiter. Pas parce que c\'est impressionnant sur un CV, mais parce que c\'est là où j\'ai vraiment travaillé comme ingénieur avec des contraintes réelles et des livrables qui comptaient. J\'y ai mené deux sujets en parallèle pendant neuf mois. Le premier, des études thermo-hydrauliques sur des équipements de test au sol pour satellites, en modélisant les échanges thermiques et les écoulements avec Fluent et ANSYS. Le deuxième, le développement d\'une application Python de maintenance prédictive pour les équipements mécaniques de l\'ESTEC, aujourd\'hui utilisée en production par l\'équipe.</p>
        <p>Ce que j\'ai surtout appris, c\'est la rigueur documentaire : chaque résultat devait être tracé et justifié dans un rapport structuré conforme aux standards internes. Et j\'ai appris à fonctionner dans un environnement technique très exigeant avec des ingénieurs de nationalités différentes. Le stage a été prolongé parce que les deux sujets avançaient bien. C\'est là aussi que j\'ai compris que la dimension normative et documentaire d\'un travail d\'ingénieur n\'est pas une contrainte, c\'est ce qui lui donne de la solidité et de la valeur.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Comment décririez-vous votre profil en quelques mots ?</button>
      <div class="qa-a" hidden>
        <p>Ingénieur mécanique avec une formation solide en simulation numérique, thermo-hydraulique et mécanique des structures. J\'ai fait de la CFD, de la FEM, du Python appliqué à des problèmes industriels réels. J\'ai travaillé dans un cadre normatif strict à l\'ESA et géré des projets d\'ingénierie de A à Z en auto-entrepreneur.</p>
        <p>Pour un poste de qualification, ce que je dirais de spécifique : j\'ai une culture naturelle de la rigueur documentaire. Pour moi, un calcul sans rapport justificatif n\'existe pas vraiment. J\'aime comprendre les systèmes en profondeur plutôt qu\'appliquer des méthodes mécaniquement. Et j\'apprends vite dans un nouveau cadre normatif, ce que j\'ai prouvé à l\'ESA en prenant en main les normes ECSS depuis zéro. Je n\'ai pas encore l\'expérience des référentiels nucléaires (RCC-M, RCC-E, guides ASNR), je ne vais pas prétendre le contraire. Mais les compétences techniques et la culture de travail sont là. Le reste s\'acquiert.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi un double diplôme franco-suédois ?</button>
      <div class="qa-a" hidden>
        <p>C\'est une décision réfléchie. Je savais que ma formation à Grenoble était solide sur la mécanique et l\'énergétique, mais je voulais une perspective complémentaire. KTH est classée parmi les meilleures écoles d\'ingénieurs d\'Europe du Nord et propose des cours en aéroélasticité, composites structuraux et dynamique des lanceurs que je ne traitais pas à Grenoble. Combiner les deux m\'a donné une formation vraiment complète : la rigueur thermique et mécanique des fluides de Grenoble INP plus l\'approche très structurale et orientée simulation de KTH.</p>
        <p>Sur le plan humain, un an à Stockholm dans une équipe internationale où toutes les interactions techniques se font en anglais, c\'est quelque chose qui change la façon de travailler. On apprend autant des autres façons d\'aborder les problèmes que des cours eux-mêmes. Et avoir réussi dans deux environnements académiques très différents dit quelque chose sur la capacité d\'adaptation, ce qui est utile quand on arrive dans un nouveau secteur avec ses propres référentiels.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Parlez-moi de votre expérience chez Buck Engineering.</button>
      <div class="qa-a" hidden>
        <p>J\'ai créé Buck Engineering en septembre 2025 pour proposer des prestations d\'ingénierie à des clients professionnels et des particuliers : CAO, études mécaniques, conseils techniques. Ce qui m\'a le plus appris, c\'est la confrontation avec les exigences réelles d\'un client. Rédiger un cahier des charges ne s\'improvise pas : il faut poser les bonnes questions, formaliser le besoin, définir les critères d\'acceptation et documenter les hypothèses clairement.</p>
        <p>Quand le besoin évolue en cours de projet (et ça arrive systématiquement), il faut gérer l\'écart par rapport aux spécifications initiales, produire une note de modification et valider les changements avec le client. Ce cycle ressemble structurellement à la gestion des modifications en ingénierie nucléaire. Il y a aussi la dimension de suivi de la conformité : est-ce que le livrable répond bien à ce qui était demandé ? C\'est une culture que j\'ai intégrée en conditions réelles. Pour un ingénieur qui va rédiger des dossiers de qualification, savoir cadrer un besoin et suivre des exigences du début à la fin, c\'est directement utile.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Comment démontrez-vous la tenue d\'un équipement en conditions accidentelles ?</button>
      <div class="qa-a" hidden>
        <p>La première étape, c\'est de constituer le dossier de qualification : identifier l\'équipement, sa fonction de sûreté, et les sollicitations enveloppantes à démontrer. Dans le nucléaire, ces sollicitations couvrent typiquement le séisme (niveaux VD1 à VD4), l\'APRP avec les profils de température et pression associés, l\'AMF, et les sollicitations combinées. La sélection des conditions enveloppantes doit être justifiée et approuvée.</p>
        <p>Ensuite, on choisit la stratégie de démonstration selon l\'équipement et son historique : qualification par calcul (FEM, analytique) pour les équipements modélisables, qualification par essais pour ceux dont le comportement est difficile à simuler (joints, matériaux d\'étanchéité, actionneurs), ou qualification par similitude avec un équipement déjà qualifié. En pratique, on combine souvent les trois approches. J\'ai appliqué une démarche très proche à l\'ESA : analyses FEM sous ANSYS pour démontrer la tenue structurelle sous charges vibratoires et thermiques, rapports de qualification structurés avec conditions enveloppantes, critères d\'acceptation, méthode de démonstration et conclusion. C\'est la même ossature qu\'un dossier de qualification nucléaire. Les référentiels changent (RCC-M, guides ASNR plutôt qu\'ECSS), mais la logique reste identique.</p>
      </div>
    </div>

  </div>'''

# Remplacer le bloc qa-list
qa_start_marker = '<div class="qa-list" style="margin-top:20px">'
qa_end_marker = '  </div>\n</section>\n\n<style>\n  .qa-list'

idx_s = c.find(qa_start_marker)
idx_e = c.find(qa_end_marker)
if idx_s >= 0 and idx_e >= 0:
    c = c[:idx_s] + new_qa + c[idx_e + len('  </div>'):]
    print('  [OK]   Q/R enrichies')
else:
    print(f'  [WARN] Q/R bloc non trouvé (s={idx_s}, e={idx_e})')

# ═══════════════════════════════════════════════════════════════
#  ÉCRITURE
# ═══════════════════════════════════════════════════════════════
print(f'\nLongueur : {orig} -> {len(c)}')
if len(c) < 100000:
    print('[ERREUR] Trop court, annulation.')
else:
    with open(SRC, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Fichier écrit : {SRC}')
