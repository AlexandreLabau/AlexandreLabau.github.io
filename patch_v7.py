#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_v7.py — Enrichissement complet des réponses Q/R (language professionnel, contenu détaillé)
"""
import shutil

SRC = r'C:\Users\opspo\Desktop\Alexandre\Claude\site_perso_upgrade.html'
BAK = SRC + '.bak_v7'

shutil.copy2(SRC, BAK)
print(f'Sauvegarde : {BAK}')

with open(SRC, 'r', encoding='utf-8') as f:
    c = f.read()

# -----------------------------------------------------------------------
# REMPLACEMENT : bloc qa-list complet
# -----------------------------------------------------------------------

old_qa = '''  <div class="qa-list" style="margin-top:20px">

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

new_qa = '''  <div class="qa-list" style="margin-top:20px">

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi EDF ?</button>
      <div class="qa-a" hidden>
        <p>Mon intérêt pour EDF ne découle pas d\'une candidature de convenance : il est le prolongement logique d\'un parcours qui m\'a progressivement orienté vers les systèmes énergétiques critiques. Durant mon stage à l\'ESA, j\'ai évolué dans une organisation où chaque décision technique était documentée, tracée et justifiable devant un comité d\'experts. Cette culture de la rigueur, que certains pourraient percevoir comme une contrainte administrative, est en réalité ce qui confère aux livrables une robustesse durable. EDF est l\'organisation qui pousse cette exigence à son niveau le plus élevé dans le secteur de l\'énergie : 56 réacteurs en exploitation, une surveillance permanente de l\'ASNR, des référentiels techniques (RCC-M, RCC-E, RCC-CW) qui encadrent chaque acte d\'ingénierie du dimensionnement à la maintenance.</p>
        <p>Au-delà du cadre réglementaire, c\'est la profondeur des enjeux qui me motive. EDF est au centre de la décision énergétique française pour les quarante prochaines années : la prolongation du parc existant dans le cadre du Grand Carénage, la conception des EPR2, la montée en puissance des SMR, la gestion du combustible et des déchets. Contribuer à ces sujets en tant qu\'ingénieur de qualification, c\'est participer à des décisions qui ont un impact mesurable sur la disponibilité du parc, sur la sûreté des installations, et in fine sur la production d\'une énergie bas carbone à grande échelle.</p>
        <p>C\'est aussi un employeur qui permet de construire une expertise sur la durée. Dans un secteur aussi technique et réglementé, la valeur d\'un ingénieur ne se révèle pas en quelques mois. Elle se construit au fil des dossiers, des retours d\'expérience et de la maîtrise progressive des référentiels. Je cherche précisément ce type d\'environnement, celui où la profondeur prime sur la rapidité de rotation, et où le travail bien fait laisse une trace dans la vie du parc.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi le nucléaire ?</button>
      <div class="qa-a" hidden>
        <p>A l\'issue de mon double diplôme en mécanique et énergétique, plusieurs secteurs m\'étaient accessibles : l\'aéronautique, l\'industrie automobile, les énergies renouvelables. J\'ai pris le temps d\'analyser chacun en fonction de critères précis : la complexité technique des systèmes, l\'impact réel sur la transition énergétique, et la profondeur d\'expertise que le secteur permet de développer sur le long terme. Le nucléaire s\'est imposé au terme de cette réflexion pour des raisons que je peux défendre avec des données.</p>
        <p>Sur la question de la transition énergétique d\'abord : si l\'objectif est de produire massivement une énergie décarbonée, pilotable et disponible en base, le nucléaire est, à ce jour, la seule technologie mature capable de répondre à cette exigence à grande échelle. Ce n\'est pas une position idéologique, c\'est le constat que font les scénarios de l\'IPCC, de RTE et de l\'Agence internationale de l\'énergie. Dans ce contexte, le travail d\'un ingénieur nucléaire n\'est pas dissociable des enjeux climatiques : contribuer à la disponibilité d\'un réacteur, c\'est contribuer à une production d\'énergie sans émissions de CO2.</p>
        <p>Sur la dimension technique ensuite : un réacteur à eau pressurisée est un système d\'une complexité remarquable, à la jonction de la thermo-hydraulique, de la mécanique des structures, de la chimie des fluides primaires, des matériaux sous irradiation, de la sûreté-sûreté et de la réglementation. Ces disciplines sont précisément celles que j\'ai étudiées et pratiquées. Je sais que je n\'en ferai pas le tour en deux ans, et c\'est exactement ce que je recherche dans un environnement professionnel : la certitude qu\'il restera encore beaucoup à apprendre dans dix ans.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi la DIPDE ?</button>
      <div class="qa-a" hidden>
        <p>La DIPDE (Direction Ingénierie du Parc en Exploitation) est la direction qui gère techniquement le parc nucléaire en fonctionnement, depuis la modification des équipements jusqu\'à la qualification des matériels de remplacement, en passant par la gestion des obsolescences et la prolongation de durée de vie dans le cadre des réexamens périodiques. C\'est une direction où l\'ingénierie produit des résultats tangibles sur le parc existant, avec un impact direct et mesurable sur la disponibilité des tranches.</p>
        <p>Ce qui me distingue d\'un profil purement académique, c\'est une culture de la traçabilité et de la documentation rigoureuse, acquise à l\'ESA dans un contexte normatif exigeant (normes ECSS). La DIPDE fonctionne dans un cadre similaire : chaque modification, chaque qualification, chaque dérogation s\'appuie sur un dossier structuré, soumis à revue technique et validé selon des processus définis. Les référentiels sont différents (RCC-M, RCC-E, guides ASNR), mais la logique de démonstration, de traçabilité et de validation est identique à celle que j\'ai pratiquée.</p>
        <p>La diversité des sujets traités à la DIPDE est également un facteur déterminant : gestion des obsolescences matérielles, qualifications initiales ou de remplacement suite à modification, travaux de Grand Carénage, préparation des Visites Décennales. Cette variété garantit une montée en compétences progressive et multidimensionnelle, évitant l\'enfermement dans un périmètre trop restreint dès les premières années. C\'est le type d\'environnement dans lequel je suis le plus efficace : exigeant techniquement, diversifié dans les sujets, et porteur d\'une responsabilité réelle sur des installations en exploitation.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi le service MCP ?</button>
      <div class="qa-a" hidden>
        <p>Le service MCP (Mécanique, Climatisation et Production de froid) couvre la robinetterie de sûreté, les groupes moto-ventilateurs et les systèmes de production de froid pour l\'ensemble du parc REP en exploitation. Ce périmètre d\'équipements est, par nature, au coeur de mes compétences de formation : mécanique des fluides, transferts thermiques, simulation thermo-hydraulique, modélisation mécanique des structures. Je ne découvre pas les phénomènes physiques en jeu, ce qui me permettra de me concentrer plus rapidement sur la maîtrise des processus de qualification propres au nucléaire.</p>
        <p>La qualification des équipements MCP représente un enjeu technique particulièrement élevé. Démontrer qu\'une vanne de sûreté ou qu\'un groupe moto-ventilateur remplit sa fonction en conditions normales, mais aussi incidentelles et accidentelles (APRP, LOCA, séisme de niveau VD3 ou VD4, transitoires thermiques) exige une démarche rigoureuse, combinant analyse des sollicitations enveloppantes, choix de la méthode de démonstration (calcul, essai, similitude), constitution du dossier justificatif et validation par les parties prenantes. C\'est précisément ce type de démarche structurée que j\'ai pratiqué à l\'ESA, dans un cadre normatif différent (ECSS) mais fondé sur les mêmes principes méthodologiques.</p>
        <p>Enfin, travailler au MCP sur des équipements appartenant aux systèmes de sauvegarde ou aux circuits primaires implique un niveau d\'exigence maximal en matière de sûreté. Je ne perçois pas cela comme une difficulté supplémentaire, mais comme la garantie que le travail produit a une signification réelle et que la qualité de chaque dossier compte véritablement. C\'est dans ce type de contexte que je suis le plus motivé pour travailler.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi la qualification ?</button>
      <div class="qa-a" hidden>
        <p>La qualification d\'équipements est, à mon sens, l\'une des disciplines les plus rigoureuses de l\'ingénierie industrielle. Elle consiste à établir, de manière formelle et traçable, la preuve qu\'un équipement est apte à remplir sa fonction de sûreté dans les conditions les plus sévères de son environnement d\'exploitation. Cette démarche requiert une maîtrise simultanée des phénomènes physiques en jeu, des méthodes de calcul et d\'essai, et des référentiels normatifs applicables. C\'est précisément cette combinaison entre rigueur technique et rigueur documentaire qui m\'attire dans ce métier.</p>
        <p>Mon expérience à l\'ESA m\'a exposé à une logique très proche, appliquée aux équipements spatiaux selon les normes ECSS. Pour chaque sujet traité, la démarche imposait d\'identifier les conditions enveloppantes (thermiques, vibratoires, mécaniques), de définir les critères d\'acceptation, de choisir la méthode de démonstration appropriée (analyse par éléments finis sous ANSYS, simulation thermique sous Fluent, essais de validation), puis de constituer un rapport justificatif complet, soumis à revue par des ingénieurs seniors. Cette ossature méthodologique se transpose directement à la qualification nucléaire. Les référentiels diffèrent (RCC-M, RCC-E, guides de l\'ASNR), mais la logique de démonstration reste identique.</p>
        <p>Ce qui me convainc définitivement, c\'est que la qualification ne laisse pas de place à l\'approximation. Soit la démonstration est établie conformément au référentiel applicable, soit elle ne l\'est pas. Cette absence d\'ambiguïté est, selon moi, ce qui confère au métier sa valeur et sa crédibilité. Travailler dans un cadre où la qualité du raisonnement et la solidité du dossier sont les seuls critères d\'évaluation, c\'est un environnement dans lequel je me retrouve pleinement.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Quels sont vos projets à long terme ?</button>
      <div class="qa-a" hidden>
        <p>Mon projet professionnel s\'inscrit dans une perspective de long terme au sein du groupe EDF. Ce positionnement n\'est pas une réponse de circonstance : dans un secteur aussi technique et réglementé que le nucléaire, la valeur d\'un ingénieur est indissociable de la profondeur de l\'expertise accumulée au fil des années. Construire cette expertise prend du temps, et elle ne prend toute sa valeur que si l\'on reste suffisamment longtemps pour la mettre au service de projets complexes.</p>
        <p>A moyen terme, mon objectif est d\'atteindre une autonomie réelle sur les processus de qualification au service MCP : maîtriser les référentiels applicables (RCC-M, RCC-E, guides ASNR), conduire des analyses de qualification avec rigueur, et contribuer activement à des dossiers sur des projets de modification ou de remplacement d\'équipements. Sur un horizon de cinq à dix ans, j\'aspire à prendre une responsabilité technique plus large : référent sur un domaine d\'équipement, coordination de qualifications dans le cadre de programmes pluriannuels tels que le Grand Carénage ou les Visites Décennales, ou encore participation à des sujets transverses impliquant plusieurs services de la DIPDE ou de la DISC.</p>
        <p>Je suis également disponible géographiquement et ouvert à la mobilité interne, qu\'il s\'agisse d\'un changement de service, de direction ou de site. Ce qui oriente mes choix sur le long terme, c\'est la nature des sujets traités et le niveau d\'exigence technique de l\'environnement. EDF offre, à cet égard, une variété de trajectoires professionnelles que peu d\'entreprises peuvent proposer dans le secteur industriel.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Quelle est l\'expérience qui vous a le plus marqué ?</button>
      <div class="qa-a" hidden>
        <p>Mon stage de fin d\'études à l\'ESA (Agence Spatiale Européenne) au centre ESTEC, aux Pays-Bas, est l\'expérience qui a le plus structuré ma façon d\'aborder le travail d\'ingénieur. Pendant neuf mois, j\'ai conduit deux sujets simultanément dans le département des systèmes de test au sol. Le premier concernait des études thermo-hydrauliques sur des équipements de conditionnement thermique pour satellites : modélisation des échanges de chaleur et des écoulements sous ANSYS Fluent, confrontation des résultats aux données expérimentales, rédaction de rapports justificatifs structurés. Le second consistait à développer une application Python de maintenance prédictive, basée sur des algorithmes de machine learning, pour surveiller et anticiper les défaillances des équipements mécaniques rotatifs de l\'ESTEC. Cette application est aujourd\'hui utilisée en production par l\'équipe.</p>
        <p>Ce que j\'ai retiré de cette expérience dépasse la dimension technique. Travailler dans une organisation où chaque livrable est soumis à revue par des ingénieurs expérimentés, où les hypothèses doivent être justifiées et les résultats tracés, m\'a profondément ancré dans une culture de la rigueur documentaire que je n\'envisage plus comme une contrainte, mais comme une exigence naturelle de sérieux. J\'ai également appris à fonctionner efficacement dans un environnement multiculturel, en produisant l\'intégralité de mes livrables en anglais, dans un contexte où la précision du langage technique est aussi importante que la justesse du calcul.</p>
        <p>Le stage a été prolongé de plusieurs semaines à la demande de mon équipe, en raison de l\'avancement des deux sujets. C\'est la confirmation qui m\'a convaincu que j\'étais capable de répondre aux attentes d\'un environnement d\'ingénierie exigeant, et que la rigueur que j\'apporte au travail était non seulement attendue, mais reconnue. C\'est cette même exigence que je souhaite apporter à EDF, dans un contexte où les enjeux de sûreté lui confèrent une dimension encore plus critique.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Comment décririez-vous votre profil en quelques mots ?</button>
      <div class="qa-a" hidden>
        <p>Je suis ingénieur en mécanique et énergétique, avec une formation duale (Grenoble INP ENSE3 et KTH Stockholm) qui m\'a exposé à des approches complémentaires : thermo-hydraulique, transferts thermiques et mécanique des fluides à Grenoble ; mécanique des structures, aéroélasticité et simulation avancée à Stockholm. Sur le plan des outils, j\'ai pratiqué la modélisation par éléments finis sous ANSYS, la simulation CFD sous Fluent, et le développement Python dans un cadre industriel. Ce sont des compétences que j\'ai appliquées à des problèmes concrets, pas seulement exercées en travaux pratiques.</p>
        <p>Ce qui me différencie pour un poste d\'ingénieur qualification, c\'est avant tout une culture documentaire naturelle. A l\'ESA, je n\'ai jamais produit un résultat sans le justifier dans un rapport structuré, conforme aux exigences du référentiel applicable. Pour moi, un calcul sans dossier associé n\'est pas un livrable, c\'est une note de travail. Cette façon d\'aborder les choses est fondamentale dans le contexte de la qualification nucléaire, où la traçabilité des décisions techniques est une exigence réglementaire non négociable.</p>
        <p>Je n\'ai pas encore l\'expérience des référentiels nucléaires (RCC-M, RCC-E, guides de l\'ASNR). Je le dis sans ambiguïté, parce que je pense qu\'il est contre-productif de prétendre à une maîtrise que l\'on n\'a pas. En revanche, j\'ai prouvé à l\'ESA que je suis capable de m\'approprier rapidement un cadre normatif exigeant depuis zéro, d\'en intégrer la logique, et de produire des dossiers de qualité dans ce cadre. C\'est précisément ce que je m\'engage à faire pour les référentiels nucléaires, avec la conviction que les bases techniques et la culture du travail sont déjà là.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Pourquoi un double diplôme franco-suédois ?</button>
      <div class="qa-a" hidden>
        <p>Le choix du double diplôme entre Grenoble INP ENSE3 et KTH (Kungliga Tekniska Högskolan, Stockholm) répondait à une volonté délibérée d\'élargir le spectre de ma formation au-delà de ce que proposait un seul établissement. Grenoble INP ENSE3 offre une excellente formation en mécanique des fluides, transferts thermiques et énergétique, avec une culture très appliquée et orientée vers les problèmes industriels. KTH, classée parmi les premières écoles polytechniques d\'Europe du Nord, développait des modules en aéroélasticité, mécanique des structures avancée, composites structuraux et dynamique des lanceurs spatiaux. Ces deux enseignements sont complémentaires et leur combinaison m\'a permis d\'acquérir une vision à la fois thermique et structurelle des systèmes mécaniques complexes.</p>
        <p>Sur le plan académique, le parcours m\'a également conduit à produire trois rapports de recherche approfondis à KTH, sur des sujets allant de l\'aéroélasticité des structures ailaires à l\'évaluation comparative des performances des lanceurs européens, en passant par la mécanique des matériaux composites fibreux. Ces travaux m\'ont appris à mener une analyse rigoureuse sur un sujet ouvert, à identifier les hypothèses structurantes, à sélectionner les méthodes appropriées et à présenter des conclusions justifiées devant des enseignants-chercheurs exigeants. Ces compétences sont directement transférables à la rédaction de dossiers de qualification.</p>
        <p>L\'expérience d\'une année à Stockholm, dans un environnement académique et multiculturel où l\'anglais est la langue de travail exclusive, a également renforcé mon aisance à évoluer dans des contextes internationaux et à collaborer avec des ingénieurs de formations et de cultures très diverses. Dans un groupe comme EDF, qui entretient des relations avec des partenaires européens et internationaux dans le cadre de projets comme le programme EPR2, cette dimension est, à mon sens, un atout complémentaire non négligeable.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Parlez-moi de votre expérience chez Buck Engineering.</button>
      <div class="qa-a" hidden>
        <p>J\'ai fondé Buck Engineering en septembre 2025 afin de proposer des prestations d\'ingénierie à des clients professionnels et des particuliers : études de conception assistée par ordinateur, analyses mécaniques, conseils techniques et gestion de projets d\'ingénierie. Cette démarche entrepreneuriale m\'a exposé à une réalité que les stages en entreprise n\'offrent pas toujours : la responsabilité pleine et entière d\'un livrable devant un client, depuis la définition du besoin jusqu\'à la livraison finale.</p>
        <p>L\'une des leçons les plus importantes que j\'en ai tirées concerne la gestion des exigences. Rédiger un cahier des charges n\'est pas une formalité : c\'est l\'acte fondateur du projet. Il s\'agit de formaliser avec précision le besoin du client, d\'identifier les contraintes fonctionnelles et techniques, de définir les critères d\'acceptation du livrable et de documenter les hypothèses retenues. Lorsque le besoin évolue en cours d\'intervention, il faut gérer l\'écart par rapport au cahier des charges initial, produire une note de modification, et valider les changements avec le client avant de les intégrer. Ce processus est structurellement analogue à la gestion des modifications d\'équipements en contexte nucléaire, où chaque évolution par rapport à la configuration de référence doit être instruite, justifiée et validée.</p>
        <p>Cette expérience m\'a également confronté à la dimension de la conformité en fin de projet : est-ce que le livrable répond point par point aux exigences spécifiées dans le cahier des charges ? Cette vérification systématique, que j\'effectuais naturellement à la clôture de chaque prestation, est la transposition directe de ce qu\'un ingénieur de qualification applique à ses dossiers. Avoir intégré cette culture en situation réelle, avec les conséquences concrètes qu\'implique la satisfaction ou l\'insatisfaction d\'un client, me semble une préparation pertinente à l\'environnement de rigueur d\'un service comme le MCP.</p>
      </div>
    </div>

    <div class="qa-item">
      <button class="qa-q" aria-expanded="false">Comment démontrez-vous la tenue d\'un équipement en conditions accidentelles ?</button>
      <div class="qa-a" hidden>
        <p>La démarche commence par la constitution du dossier de base de qualification : identification précise de l\'équipement et de sa fonction de sûreté, recensement de l\'environnement d\'installation (zone sismique, température ambiante, humidité, rayonnement), et définition des sollicitations enveloppantes à démontrer. Dans le cadre du parc REP français, ces sollicitations couvrent classiquement le séisme de dimensionnement (niveaux VD1 à VD4 selon la criticité de la fonction), les sollicitations thermiques et de pression liées à un accident de perte de réfrigérant primaire (APRP ou LOCA), les effets d\'un accident de Masse Froide (AMF), et les sollicitations combinées lorsque ces événements surviennent simultanément. Chaque enveloppe doit être justifiée et approuvée par les parties prenantes avant le lancement de la démonstration.</p>
        <p>La stratégie de démonstration est ensuite choisie en fonction des caractéristiques de l\'équipement, de son historique de qualification et des données disponibles. La qualification par le calcul (méthode par éléments finis ou analytique) est privilégiée pour les composants dont le comportement est bien modélisable, comme les structures métalliques ou les tuyauteries. La qualification par essais est retenue lorsque le comportement de l\'équipement est difficile à simuler numériquement : c\'est le cas des joints, des matériaux polymères, des actionneurs électromécaniques ou de tout équipement dont la défaillance dépend de phénomènes couplés complexes (vibrations, vieillissement thermique, irradiation). La qualification par similitude permet de s\'appuyer sur un dossier existant pour un équipement de même famille, sous réserve de démontrer que les différences sont non pénalisantes. En pratique, une qualification complète combine souvent ces trois approches de façon complémentaire.</p>
        <p>J\'ai appliqué une démarche méthodologiquement très proche à l\'ESA : analyse par éléments finis sous ANSYS pour démontrer la tenue structurelle d\'équipements de test au sol sous charges vibratoires et thermiques, définition des conditions enveloppantes conformément aux normes ECSS-E-ST-32, et rédaction de rapports de qualification structurés incluant la description du modèle, les hypothèses retenues, les résultats commentés et la conclusion de qualification. La structure d\'un tel rapport est identique à celle d\'un dossier de qualification nucléaire régi par les référentiels RCC-M ou les guides de l\'ASNR. La transposition est directe, même si l\'approfondissement des référentiels nucléaires constitue naturellement la première étape de ma montée en compétences au sein du service MCP.</p>
      </div>
    </div>

  </div>'''

if old_qa in c:
    c = c.replace(old_qa, new_qa, 1)
    print('[OK]   Bloc qa-list remplacé avec succès')
else:
    print('[WARN] Bloc qa-list INTROUVABLE — vérifier les espaces/apostrophes')

# -----------------------------------------------------------------------
# ÉCRITURE
# -----------------------------------------------------------------------
print(f'\nLongueur avant : —  après : {len(c)}')
if len(c) < 1000:
    print('[ERREUR] Fichier trop court ! Annulation.')
else:
    with open(SRC, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Fichier écrit : {SRC}')
