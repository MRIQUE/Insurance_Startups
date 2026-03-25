# GEO (Global Events Observer) par McKenzie Intelligence Services

## Identite
**Editeur** : McKenzie Intelligence Services (MIS)
**Nom de la solution** : GEO (Global Events Observer)
**Date de mise a jour** : 2026-03-25
**Fondateurs** : Forbes McKenzie (CEO & Fondateur)
**Annee de creation** : 2011
**Siege** : Londres, Royaume-Uni
**Effectifs** : ~34 collaborateurs
**Levees de fonds** : ~3M$ au total (4 tours dont Seed en 2015 ; investissement Maven Capital Partners en 2023)
**Investisseurs** : Maven Capital Partners UK, Eden Rock Capital Management

## Description
McKenzie Intelligence Services (MIS) est une insurtech britannique specialisee dans le renseignement geospatial applique a l'assurance et la reassurance. La societe combine des techniques de renseignement militaire, des donnees satellitaires et de l'intelligence artificielle pour fournir aux assureurs une intelligence actionnable en temps quasi reel apres des catastrophes naturelles et des evenements de grande ampleur. Sa plateforme SaaS proprietaire, GEO (Global Events Observer), permet aux gestionnaires d'exposition, equipes sinistres et experts d'evaluer les dommages a l'echelle d'un batiment ou d'un portefeuille entier en 48 a 72 heures apres un evenement.

**Proposition de valeur** : Transformer la reponse des assureurs aux catastrophes naturelles en fournissant des evaluations de dommages fiables, a l'echelle du batiment individuel, en 48-72 heures grace a la fusion de donnees multi-sources (satellites, drones, capteurs au sol, imagerie aerienne) analysees par des ex-analystes du renseignement militaire et augmentees par l'IA.

## Le probleme adresse
Apres une catastrophe naturelle (ouragan, incendie, inondation, seisme, tornade), les assureurs font face a plusieurs defis majeurs :
- **Delai d'evaluation** : les inspections physiques traditionnelles prennent des semaines, voire des mois, retardant les indemnisations
- **Manque de visibilite** : absence de vue consolidee de l'impact reel sur le portefeuille assure
- **Cout des expertises terrain** : deploiement couteux et dangereux d'experts sur zone sinistree
- **Donnees fragmentees** : multiples sources de donnees non integrees (meteorologie, imagerie, capteurs) sans vision unifiee
- **Mise en reserve** : difficulte a estimer rapidement les reserves necessaires

MIS resout ces problemes en fournissant une representation numerique complete de l'impact d'une catastrophe sur les polices en cours, permettant des decisions de reservation et de couverture accelerees et basees sur les donnees.

## Histoire et fondateurs

### Forbes McKenzie -- Fondateur & CEO
Forbes McKenzie est un ancien officier du British Army (Intelligence Corps) decore pour bravoure et leadership au combat. Diplome en geographie de l'Universite de Glasgow (2001), il a integre la Royal Military Academy de Sandhurst puis effectue une carriere de 10 ans comme officier de renseignement en missions speciales, menant des operations strategiques a haut risque a travers le monde. Il a ete decore pour "Gallantry and Leadership in the face of the Enemy" et mentionne dans les depeches (Mentioned in Dispatches) en septembre 2009 pour bravoure exceptionnelle.

C'est au cours de sa carriere militaire, en utilisant les technologies geospatiales les plus avancees pour le compte de gouvernements, qu'il a identifie l'opportunite de transposer cette approche au secteur de l'assurance pour accelerer la reponse aux catastrophes.

### Dates cles
| Date | Evenement |
|------|-----------|
| 17 fevrier 2011 | Fondation de McKenzie Intelligence Services |
| 2011-2017 | Phase de consulting (clients : Google, Aon) -- autofinancement |
| 2015 | Premier tour de financement (Seed) |
| 2016 | Debut de la collaboration avec Lloyd's |
| 2017 | Lancement du developpement de la plateforme GEO, cofondee avec l'ESA (European Space Agency) |
| 2019 | Participation au Lloyd's Lab Accelerator ; demo pour le workstream "Future at Lloyd's - Next Generation Claims" |
| 2021 | Lancement officiel de la plateforme GEO |
| 2022 | Partenariat officiel avec Lloyd's (contrat 2 ans via LIMOSS) |
| 2023 | Investissement strategique de Maven Capital Partners ; partenariats Fugro, EagleView, Brush Claims |
| 2024 | Lancement du classificateur de dommages par IA ; renouvellement du contrat LIMOSS pour 2025 ; jalon des 200 evenements catastrophiques couverts via GEO |
| Janvier 2025 | Webinaire post-incendies de Los Angeles : 50 000+ evaluations de dommages en 72 heures |

## Dirigeants
| Nom | Role | Profil |
|-----|------|--------|
| Forbes McKenzie | Fondateur & CEO | Ex-officier renseignement British Army (10 ans), decore pour bravoure, diplome geographie Univ. Glasgow |

Note : L'equipe fondatrice est composee a pres de 50% d'anciens membres de l'armee ou de la communaute du renseignement. Le CTO historique est Alfie Conetta.

## Solutions proposees

### Plateforme GEO (Global Events Observer)
Plateforme SaaS web de renseignement geospatial dediee a l'assurance, cofondee avec l'Agence Spatiale Europeenne (ESA) et developpee dans le cadre du programme "Future at Lloyd's".

#### Sources de donnees integrees
- Imagerie satellite tres haute resolution (y compris radar SAR, penetrant les nuages)
- Imagerie aerienne et par drone
- Donnees radar
- Capteurs au sol et IoT
- Donnees de telephonie mobile
- Imagerie street-level
- Donnees meteorologiques
- Donnees de tiers (partenaires comme Fugro, EagleView, ICEYE)

#### Fonctionnalites cles
| Fonctionnalite | Description |
|----------------|-------------|
| Analyse d'exposition | Croisement des donnees geospatiales avec les portefeuilles de polices (PIF) |
| Evaluation de dommages par batiment | Classification des dommages a l'echelle individuelle selon standards NATO |
| Classificateur IA de dommages | Modele ML entraine sur les evaluations d'analystes militaires, ~95% de precision |
| Analyse multi-perils | Couverture : ouragans, incendies, inondations, tornades, seismes, troubles civils |
| Policy Insights | Integration des conditions de police dans l'analyse |
| Rapports d'evenements | Rapports detailles post-evenement (200+ evenements couverts depuis 2021, ~66/an) |
| Imagerie en temps quasi reel | Visualisation cloud-penetrating en temps quasi reel de n'importe quel point du globe |

#### Technologie
- Intelligence artificielle et machine learning (classificateur de dommages, ~95% de precision)
- Techniques de renseignement militaire (analystes ex-OTAN)
- Apache Airflow & Astro pour l'orchestration des pipelines de donnees
- Architecture SaaS cloud, browser-based
- API pour integration aux systemes existants

### Approche hybride IA + Intelligence humaine
L'approche differenciante de MIS repose sur la combinaison :
1. **IA et ML** : traitement rapide a grande echelle des images et donnees
2. **Analystes humains** : ex-analystes du renseignement militaire (formes aux standards NATO) qui valident et enrichissent les resultats de l'IA

Cette approche hybride garantit a la fois la rapidite (traitement de dizaines de milliers de batiments) et la fiabilite (validation humaine experte).

## Traction

### Clients et partenaires
- **Lloyd's of London** : partenariat strategique depuis 2016, contrat via LIMOSS renouvele pour 2025 ; 80% des clients (par GWP) ont continue a utiliser le service apres transition vers service electif -- transfert le plus reussi de l'histoire de Lloyd's
- **Markel International** : partenariat pour l'acceleration des reponses sinistres (utilisateur depuis 2017 pour les syndicats Lloyd's)
- **LIMOSS / LMA** : contrat de fourniture d'intelligence geospatiale pour le marche Lloyd's
- **Fugro** : partenariat pour imagerie aerienne haute resolution post-catastrophe
- **EagleView** : collaboration pour imagerie et intelligence de pointe pour les catastrophes nord-americaines
- **Brush Claims** : partenariat avec cet insurtech US de gestion de sinistres
- **ICEYE** : accord pour l'analyse des risques d'inondation (donnees SAR)

### Chiffres cles
- 200+ evenements catastrophiques couverts depuis le lancement de GEO (2021)
- ~66 evenements catastrophiques analyses par an en moyenne
- 1 200+ utilisateurs issus des plus grandes compagnies d'assurance mondiales
- 50 000+ evaluations de dommages en 72 heures (incendies de Los Angeles, janvier 2025)
- ~95% de precision du classificateur IA de dommages
- Resolution des sinistres en 48-72 heures apres un evenement
- ~3M$ leves au total (4 tours de financement)
- ~34 collaborateurs

### Reconnaissance
- Alumni du Lloyd's Lab Accelerator
- Co-financement de l'Agence Spatiale Europeenne (ESA) pour le projet GEO
- Membre InsTech
- Programme "Future at Lloyd's - Next Generation Claims"

## Perspectives

### Axes de croissance
- **Expansion geographique** : penetration accrue des marches nord-americain (via EagleView, Brush Claims) et europeen, au-dela du marche Lloyd's historique
- **Enrichissement IA** : amelioration continue du classificateur de dommages, extension a de nouveaux types de perils et de donnees
- **Couverture de perils elargie** : ajout de perils supplementaires et analyse multi-perils renforcee
- **Partenariats data** : multiplication des sources de donnees via partenariats (Fugro, ICEYE, EagleView)
- **Monetisation SaaS** : transition d'un modele Lloyd's centralise vers un modele SaaS ouvert a l'ensemble du marche de l'assurance et de la reassurance

### Marches vises
- Marche Lloyd's et London Market (base historique)
- Marche de l'assurance et reassurance nord-americain
- Marche europeen de l'assurance
- Grands resequeurs mondiaux
- Potentiel dans les secteurs adjacents : gouvernements, aide humanitaire, securite

## Concurrents directs
| Concurrent | Specialite | Pays |
|------------|-----------|------|
| ICEYE | Donnees SAR satellitaires, analyse d'inondations et catastrophes pour assureurs | Finlande |
| Floodbase | Donnees d'inondation parametrique pour assurance | USA |
| Arturo | Intelligence immobiliere par imagerie aerienne et IA pour assurance | USA |
| Geollect | Renseignement geospatial maritime et terrestre | Royaume-Uni |
| Skyline Partners | Modelisation des catastrophes et conseil | Royaume-Uni |
| Descartes Underwriting | Assurance parametrique climatique (donnees satellites, IA) | France |
| One Concern | Modelisation du risque catastrophique par IA | USA |
| Cape Analytics | Analyse de proprietes par imagerie aerienne et IA | USA |

Note : MIS se distingue de la plupart de ses concurrents par son approche hybride IA + renseignement humain militaire, et par son ancrage historique dans le marche Lloyd's. Contrairement a des acteurs purement technologiques, MIS valide systematiquement ses evaluations par des analystes formes aux standards OTAN, ce qui constitue un facteur de confiance aupres des assureurs.

## Reputation
**Note de reputation** : 8/10
**Analyse** : McKenzie Intelligence Services occupe une position unique dans l'ecosysteme insurtech grace a sa combinaison distinctive de renseignement militaire et de technologie geospatiale. Le partenariat strategique avec Lloyd's of London -- ou MIS a realise le transfert vers service electif le plus reussi de l'histoire du marche -- constitue une validation institutionnelle majeure. Le co-financement par l'ESA et la participation au Lloyd's Lab renforcent la credibilite technologique. Les performances operationnelles (50 000 evaluations en 72h lors des incendies de LA) demontrent une capacite reelle et differenciante. Toutefois, l'entreprise reste de taille modeste (~34 personnes) avec des levees de fonds limitees (~3M$) comparees a des concurrents comme ICEYE (300M$+) ou Descartes Underwriting (120M$). L'expansion hors du marche Lloyd's et vers l'Amerique du Nord sera determinante pour confirmer le potentiel de croissance.

## Tags & Categorisation

### Domaine & Perimetre
#cat-nat #grands-risques #professionnel #reassurance #multi-perils

### Acteurs & Roles
#assureur #reassureur #gestionnaire-sinistres #gestionnaire-exposition #expert #loss-adjuster

### Cycle de vie
#qualification #evaluation-dommages #indemnisation #gestion-reserves

### Capacites metier
#evaluation-dommages #gestion-reserves #analyse-portefeuille #analyse-exposition #reporting #aide-decision

### Technologie & IA
#ia #machine-learning #vision-par-ordinateur #classification-automatique #imagerie-satellite #donnees-geospatiales #sar #drone #iot #capteurs

### Autres Tags
#saas #cloud #api #renseignement-militaire #temps-reel #multi-pays #multi-perils #scalabilite #lloyd-s #london-market #esa #kpi #tableaux-de-bord

## Ressources
**Presentation produit** : https://mckenzieintelligence.com
**Plateforme GEO** : https://mckenzieintelligence.com/geo
**Blog & Ressources** : https://resources.mckenzieintelligence.com/blog
**Autres ressources** :
- Lloyd's Lab Alumni : https://www.lloyds.com/insights/lloyds-lab/programmes-and-initiatives/lloyds-lab-accelerator/alumni/mckenzie-intelligence-services
- InsTech profile : https://www.instech.co/member-profiles/mckenzie-intelligence-services/
- Interview fondateur (Insurtech Insights) : https://www.insurtechinsights.com/meet-the-founder-from-battlefield-to-breakthroughs-forbes-mckenzie-pioneers-at-mis/
