content = open('C:/Users/opspo/Desktop/Alexandre/Claude/site_perso_upgrade.html', 'r', encoding='utf-8').read()

replacements = [

  # ── En-tête / Navigation ────────────────────────────────────────────────
  ('Alexandre Labau : Mechanical and energy engineer',
   'Alexandre Labau : Ingénieur en mécanique et énergétique'),

  ('>Education<', '>Formation<'),
  ('>Software Skills<', '>Compétences<'),
  ('>Recommendations<', '>Recommandations<'),
  ('>Reports<', '>Rapports<'),

  # ── Hero — description ──────────────────────────────────────────────────
  ("Holder of a double master's degree in Mechanical and Energy Engineering from KTH Royal Institute of Technology in Stockholm and Grenoble INP – ENSE3, I aspire to apply my skills within an international organization.",
   "Titulaire d'un double diplôme d'ingénieur en mécanique et énergétique entre KTH École Royale Polytechnique de Stockholm et Grenoble INP – ENSE3, je souhaite mettre mes compétences au service d'une organisation internationale."),

  # ── Hero — boutons ──────────────────────────────────────────────────────
  ('>Download my CV<', '>Télécharger mon CV (EN)<'),
  ('aria-label="Download my CV (EN)"', 'aria-label="Télécharger mon CV (EN)"'),
  ('>ESA - Appraisal<', ">ESA — Fiche d'appréciation<"),
  ('>ESA - Reference letter<', '>ESA — Lettre de recommandation<'),
  ('>KTH - Reference letter<', '>KTH — Lettre de recommandation<'),
  ('>Grenoble INP - ENSE3 - Reference letter<', '>Grenoble INP — ENSE3 — Lettre de recommandation<'),
  ('>UPC - Reference letter<', '>UPC — Lettre de recommandation<'),

  # ── Hero — légende photo ────────────────────────────────────────────────
  ("Master's thesis defense at the European Space Research and Technology Center",
   "Soutenance de thèse au Centre européen de recherche et de technologie spatiale (ESTEC)"),

  # ── Section Formation ───────────────────────────────────────────────────
  ('<h2 id="formation-title" style="margin-bottom:8px">Education</h2>',
   '<h2 id="formation-title" style="margin-bottom:8px">Formation</h2>'),
  ('Main schools, programs and industrial experiences.',
   'Principales écoles, programmes et expériences industrielles.'),

  # KTH
  ('KTH Royal Institute of Technology — Double-degree program',
   'KTH École Royale Polytechnique de Stockholm — Double diplôme'),
  ('Mechanical &amp; Energy Engineering • focus on structural mechanics and heat transfer',
   'Génie mécanique et énergétique • spécialisation mécanique des structures et transferts thermiques'),
  ('Coursework &amp; projects across mechanics, thermal sciences and simulations.',
   'Cours et projets en mécanique, sciences thermiques et simulations.'),
  ('Ranked #7 worldwide in Mechanical Engineering (Shanghai Ranking 2024).',
   'Classée #7 mondial en génie mécanique (Shanghai Ranking 2024).'),
  ('>Open reference PDF<', '>Ouvrir la lettre de recommandation<'),
  ('>Program page<', '>Page du programme<'),
  ('>Ranking<', '>Classement<'),

  # ENSE3
  ('Grenoble INP – ENSE3 — Mechanical &amp; Energy Engineering',
   'Grenoble INP – ENSE3 — Ingénierie mécanique et énergétique'),
  ('Engineering degree (ME track) • multiphysics approach',
   "Diplôme d'ingénieur (filière ME) • approche multiphysique"),
  ('Courses : Solid Mechanics (materials strength, elasticity), Structures and materials (fatigue, failure), FEM (plastic &amp; elastic deformation, buckling local &amp; global instability, modal analysis vibrations on ANSYS and Abaqus), Thermohydraulic, Heat and mass transfers (heat exchangers), Modelling and analysis of flows, Lightweight structures, Industrial Design and Mechanical modeling (CAD with ISO GPS compliance).',
   "Cours : Mécanique des solides (résistance des matériaux, élasticité), Structures et matériaux (fatigue, rupture), EF (déformation plastique et élastique, flambement local et global, analyse modale sur ANSYS et Abaqus), Thermo-hydraulique, Transferts de chaleur et de masse (échangeurs), Modélisation et analyse d'écoulements, Structures légères, Conception mécanique et modélisation (CAO avec conformité ISO GPS)."),
  ('Team projects and industrial problem-solving across semesters.',
   'Projets en équipe et résolution de problèmes industriels tout au long des semestres.'),
  ('>Program page (EN)<', '>Page du programme (EN)<'),

  # ESA éducation
  ("European Space Agency (ESA) — Master's thesis internship (extended)",
   "Agence Spatiale Européenne (ESA) — Stage de fin d'études (prolongé)"),
  ('Mechanical engineering • CAD &amp; Digital Twin enablement',
   'Ingénierie mécanique • CAO et jumeaux numériques'),
  ('Mechanical design of ESA systems (sensor housing), from 2D and 3D CAD modeling to manufacturing and assembly. Reference letter attached.\n</li>',
   "Conception mécanique d'équipements ESA (boîtiers de capteurs), de la modélisation CAO 2D/3D jusqu'à la fabrication et l'assemblage. Lettre de recommandation jointe.\n</li>"),
  ('Reducing the operational costs and downtime of mechanical equipment through predictive maintenance thanks to the digitalization of manufacturing lines via digital twins, AI, and smart sensors. Follow up implemetation of new technologies for digitalization within industries.',
   "Réduction des coûts opérationnels et des arrêts imprévus des équipements mécaniques grâce à la maintenance prédictive, via la numérisation des lignes de production (jumeaux numériques, IA, capteurs intelligents)."),
  ('Development of a Machine Learning application in Python for this predictive maintenance. Application validated during a European conference and now under ESA licensed registration.',
   "Développement d'une application Python de Machine Learning pour la maintenance prédictive. Application validée lors d'une conférence européenne et désormais sous licence ESA."),
  ('Daily collaboration with international companies and space agencies to ensure an optimized integration of the new technologies.',
   "Collaboration quotidienne avec des entreprises et agences spatiales internationales pour une intégration optimisée des nouvelles technologies."),
  ('Project extended and presented to experts at a conference in the Netherlands.',
   'Stage prolongé et présenté devant des experts lors d\'une conférence aux Pays-Bas.'),
  ('>Appraisal Master Thesis<', ">Fiche d'appréciation stage<"),
  ('>Poster Master Thesis<', '>Poster de thèse<'),
  ('>Report<', '>Rapport<'),
  ('>ESA website<', '>Site ESA<'),

  # UPC éducation
  ('Universitat Politècnica de Catalunya (UPC) — ESEIAAT',
   'Université Polytechnique de Catalogne (UPC) — ESEIAAT'),
  ('CFD, FEM &amp; CAD • mechanical engineering applications',
   'CFD, EF & CAO • applications en ingénierie mécanique'),
  ('Multidisciplinary resolution of outstanding issues for pantograph-catenary interaction from CAD (CATIA V5 in 2D and 3D) to Finite Element Analysis (ANSYS). Reference attached.',
   "Résolution multidisciplinaire des problèmes d'interaction pantographe-caténaire, de la CAO (CATIA V5 2D/3D) jusqu'à l'analyse par éléments finis (ANSYS). Lettre de recommandation jointe."),
  ('>UPC website<', '>Site UPC<'),

  # Caterpillar éducation
  ('First-year industrial experience',
   'Expérience industrielle de première année'),
  ('Gained practical mechanical experience on industrial assembly lines for heavy systems.',
   "Acquisition d'une expérience mécanique pratique sur les lignes d'assemblage industrielles pour systèmes lourds."),
  ('Developed hands-on skills in mechanical assembly and production workflows on manufacturing lines.',
   "Développement de compétences pratiques en assemblage mécanique et flux de production sur lignes de fabrication."),
  ('>Business unit<', '>Unité commerciale<'),

  # ── Section Compétences logicielles ────────────────────────────────────
  ('<h2>Software Skills</h2>',
   '<h2>Compétences logicielles</h2>'),
  ('Here are the main tools I use, grouped by category.',
   'Les principaux outils que j\'utilise, regroupés par catégorie.'),

  # ── Section Recommandations ─────────────────────────────────────────────
  ('>Recommendations and appraisal<', '>Recommandations et appréciations<'),
  ('Download the following documents or read them online.',
   'Téléchargez les documents suivants ou consultez-les en ligne.'),
  ('European Space Agency : Reference Letter and Appraisal',
   "Agence Spatiale Européenne : Lettre de recommandation et fiche d'appréciation"),
  ('9 months at the European Space Agency',
   "9 mois à l'Agence Spatiale Européenne"),
  ('Nicoletta Wagner, Space Project Manager &amp; Michael Mallon, Dr.-Ing., Supervisor',
   'Nicoletta Wagner, Space Project Manager & Michael Mallon, Dr.-Ing., Superviseur'),
  ('Universitat Politècnica de Catalunya (UPC) : Reference Letter',
   'Université Polytechnique de Catalogne (UPC) : Lettre de recommandation'),
  ('Robert Arcos, Associate Professor',
   'Robert Arcos, Professeur associé'),
  ('KTH Royal Institute of Technology : Reference Letter',
   'KTH École Royale Polytechnique de Stockholm : Lettre de recommandation'),
  ('Professor Christer Fuglesang, Former ESA Astronaut',
   'Professeur Christer Fuglesang, ancien astronaute ESA'),
  ('Grenoble - INP - ENSE3 : Reference Letter',
   'Grenoble INP – ENSE3 : Lettre de recommandation'),
  ('Olivier Métais, President of the French Hydrotechnical Society',
   'Olivier Métais, Président de la Société Hydrotechnique de France'),
  ('>Report - Industrial Design<', '>Rapport — Conception industrielle<'),
  ('Report – Compressible flow in a nozzle on Fluent',
   'Rapport — Écoulement compressible dans une tuyère (Fluent)'),
  ('Report – Turbulent Jet on Fluent',
   'Rapport — Jet turbulent (Fluent)'),
  ('Report – Flowmeter',
   'Rapport — Débitmètre'),

  # ── Section Projets ─────────────────────────────────────────────────────
  ('>Projects &amp; Experiences<', '>Projets &amp; Expériences<'),
  ('ESA — Digital Twins &amp; Predictive Maintenance',
   'ESA — Jumeaux numériques &amp; Maintenance prédictive'),
  ('Development of a Python-based ML application to reduce equipment downtime through digital twin enablement and smart sensors. Work presented to experts at ESTEC in the Netherlands and under ESA license registration.',
   "Développement d'une application Python de Machine Learning pour réduire les arrêts imprévus grâce aux jumeaux numériques et capteurs intelligents. Travail présenté devant des experts à l'ESTEC (Pays-Bas) et déposé sous licence ESA."),
  ('>Appraisal<', ">Fiche d'appréciation<"),
  ('>Reference letter<', '>Lettre de recommandation<'),
  ('>Poster<', '>Poster<'),

  ('UPC BarcelonaTech - CFD &amp; Meshing on Fluent',
   'UPC BarcelonaTech — CFD &amp; Maillage sur Fluent'),
  ('From CAD to CFD : meshing strategies, solver setup and validation on industrial-like cases.',
   'De la CAO au CFD : stratégies de maillage, paramétrage du solveur et validation sur des cas industriels.'),
  ('>Internship report<', '>Rapport de stage<'),

  (' Industrial DesignSolidWorks — Space Vehicle',
   'Conception industrielle SolidWorks — Véhicule spatial'),
  ('Concept design and assembly for a space vehicle.',
   "Conception et assemblage d'un véhicule spatial."),
  ('>Report<\n\t<a class="project-link" href="reco_kth.pdf"',
   '>Rapport<\n\t<a class="project-link" href="reco_kth.pdf"'),

  ('Industrial design and mechanical modeling projects',
   'Projets de conception industrielle et modélisation mécanique'),
  ('CAD, FEM (Catia, SolidWorks, Abaqus, ANSYS).',
   'CAO, EF (Catia, SolidWorks, Abaqus, ANSYS).'),
  ('>Report Hydraulic Verlinde Motor<', '>Rapport — Moteur hydraulique Verlinde<'),
  ('>Report Fan Blade CAD SolidWorks<', '>Rapport — Pale de ventilateur CAO SolidWorks<'),
  ('>Report Mechanical Modeling Skate Abaqus<', '>Rapport — Modélisation mécanique Skate (Abaqus)<'),
  ('>Report Mechanical Modeling Scooter Abaqus<', '>Rapport — Modélisation mécanique Trottinette (Abaqus)<'),

  # figcaptions projets
  ('<figcaption>Predictive Maintenance (PdM)</figcaption>', '<figcaption>Maintenance prédictive (PdM)</figcaption>'),
  ('<figcaption>Final presentation</figcaption>', '<figcaption>Présentation finale</figcaption>'),
  ('<figcaption>Arduino sensor on asset</figcaption>', '<figcaption>Capteur Arduino sur équipement</figcaption>'),
  ('<figcaption>3D Digital Twin</figcaption>', '<figcaption>Jumeau numérique 3D</figcaption>'),
  ('<figcaption>ABB orga folders</figcaption>', '<figcaption>Dossiers organisation ABB</figcaption>'),
  ('<figcaption>Temperature analysis</figcaption>', '<figcaption>Analyse de température</figcaption>'),
  ('<figcaption>Statistical panel</figcaption>', '<figcaption>Tableau de bord statistique</figcaption>'),
  ('<figcaption>3D Panel</figcaption>', '<figcaption>Panneau 3D</figcaption>'),
  ('<figcaption>Frequency detection 1</figcaption>', '<figcaption>Détection fréquence 1</figcaption>'),
  ('<figcaption>Frequency detection 2</figcaption>', '<figcaption>Détection fréquence 2</figcaption>'),
  ('<figcaption>Frequency detection 3</figcaption>', '<figcaption>Détection fréquence 3</figcaption>'),
  ('<figcaption>Frequency detection 4</figcaption>', '<figcaption>Détection fréquence 4</figcaption>'),
  ('<figcaption>Frequency panel</figcaption>', '<figcaption>Panneau fréquences</figcaption>'),
  ('<figcaption>Mean panel</figcaption>', '<figcaption>Panneau moyennes</figcaption>'),
  ('<figcaption>Fluent simulation</figcaption>', '<figcaption>Simulation Fluent</figcaption>'),
  ('<figcaption>Space vehicle assembly</figcaption>', '<figcaption>Assemblage véhicule spatial</figcaption>'),
  ('<figcaption>Vehicle view (2)</figcaption>', '<figcaption>Vue véhicule (2)</figcaption>'),
  ('<figcaption>Vehicle view (3)</figcaption>', '<figcaption>Vue véhicule (3)</figcaption>'),
  ('<figcaption>ISS docking port</figcaption>', '<figcaption>Port d\'amarrage ISS</figcaption>'),
  ('<figcaption>Assembly view</figcaption>', '<figcaption>Vue assemblage</figcaption>'),
  ('<figcaption>Velocity field</figcaption>', '<figcaption>Champ de vitesse</figcaption>'),
  ('<figcaption>Pressure contours</figcaption>', '<figcaption>Contours de pression</figcaption>'),
  ('<figcaption>Profile</figcaption>', '<figcaption>Profil</figcaption>'),

  # ── Section Rapports ────────────────────────────────────────────────────
  ('<h2 id="rapports-title">Reports</h2>',
   '<h2 id="rapports-title">Rapports</h2>'),
  ('Please note: this work was carried out with the persons mentioned in the reports.',
   'Note : ces travaux ont été réalisés avec les personnes mentionnées dans les rapports.'),
  ('Download the reports or read them online.',
   'Téléchargez les rapports ou consultez-les en ligne.'),

  ("Report Master's thesis with extension : Engineer at the European Space Agency",
   "Rapport de stage de fin d'études (prolongé) : Ingénieur à l'Agence Spatiale Européenne"),
  ('Engineering internship at the Polytechnic University of Catalonia (CFD, FEM &amp; CAD)',
   "Stage ingénieur à l'Université Polytechnique de Catalogne (CFD, EF &amp; CAO)"),
  ('First-year internship report at Caterpillar',
   'Rapport de stage de première année chez Caterpillar'),
  ('Aeroelasticity applied to the Windex aircraft',
   "Aéroélasticité appliquée à l'avion Windex"),
  ('Fibre Composites - Analysis and design : Design Problem - FEM &amp; Python',
   'Composites fibreux — Analyse et conception : problème de design EF &amp; Python'),
  ('Comparative Evaluation of Reusable Launch Vehicles and Expendable Launch Vehicles',
   'Évaluation comparative des lanceurs réutilisables et à usage unique'),
  ('Heat Exchangers : Refrigeration system',
   'Échangeurs de chaleur : système de réfrigération'),
  ('Heat Exchangers : Tubular System',
   'Échangeurs de chaleur : système tubulaire'),
  ('Flow modeling and analysis : Turbulent Jet on Fluent',
   "Modélisation et analyse d'écoulements : Jet turbulent sur Fluent"),
  ('Flow modeling and analysis : Compressible flow in a nozzle on Fluent',
   "Modélisation et analyse d'écoulements : Écoulement compressible dans une tuyère (Fluent)"),
  ('Flow modeling and analysis : Flowmeter',
   "Modélisation et analyse d'écoulements : Débitmètre"),
  ('Fluids and Thermal Simulations : Overset meshing on Fluent',
   'Simulations fluides et thermiques : Maillage Overset sur Fluent'),
  ('Fluids and Thermal Simulations : Mesh Generation on Fluent',
   'Simulations fluides et thermiques : Génération de maillage sur Fluent'),
  ('Pressurized Flow Hydraulics Project: Water Hammer and Resonance',
   'Hydraulique en charge : Coup de bélier et résonance'),
  ('Pressurized Flow Hydraulics Lab: Water Hammer',
   'TP Hydraulique en charge : Coup de bélier'),
  ('Mechanical Design Project: Hydraulic Motor Verlinde',
   'Projet de conception mécanique : Moteur hydraulique Verlinde'),
  ('Industrial Design : Fan Blade on SolidWorks',
   'Conception industrielle : Pale de ventilateur (SolidWorks)'),
  ('Vehicle Design : A space taxi for two people - Human Spaceflight',
   'Conception de véhicule : Taxi spatial pour deux personnes — Vol habité'),
  ('Mechanical modeling on Abaqus',
   'Modélisation mécanique sur Abaqus'),
  ('Mechanical Design and Modeling : Skateboard',
   'Conception et modélisation mécanique : Skateboard'),
  ('Mechanical Design and Modeling : Scooter',
   'Conception et modélisation mécanique : Trottinette'),
  ('Structures and materials : Free cantilever beam',
   'Structures et matériaux : Poutre en porte-à-faux'),
  ('Structures and materials : Two-story portico',
   'Structures et matériaux : Portique à deux niveaux'),

  # ── Fresque — bouton Fermer reste en français ───────────────────────────
  # (déjà en français)
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
    else:
        print(f'  ⚠ NON TROUVÉ : {old[:60]}...' if len(old) > 60 else f'  ⚠ NON TROUVÉ : {old}')

open('C:/Users/opspo/Desktop/Alexandre/Claude/site_perso_upgrade.html', 'w', encoding='utf-8').write(content)
print(f'\nOK — {count}/{len(replacements)} remplacements effectués.')
