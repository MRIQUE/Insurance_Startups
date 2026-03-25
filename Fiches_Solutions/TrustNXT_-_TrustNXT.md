# TrustNXT par TrustNXT

## Identite
**Editeur** : TrustNXT GmbH
**Nom de la solution** : TrustNXT (produit phare : origo ; produit assurance : TrustNXT CAM)
**Date de mise a jour** : 2026-03-25
**Fondateurs** : Sebastian Adank (Managing Director), Ariane Scheer-Danielsson (Managing Director, Business Dev & Marketing), Andreas Reich (Managing Director, CTO)
**Annee de creation** : 2024
**Siege** : Hambourg, Allemagne
**Levees de fonds** : 1,6M EUR pre-seed (septembre 2025, D11Z.Ventures + High-Tech Grunderfonds / HTGF)
**Effectifs** : Equipe fondatrice de 3 cofondateurs + equipe en croissance (effectif exact non public, stade pre-seed)
**Origine** : Spin-off corporate de Basler AG (specialiste cameras industrielles et vision par ordinateur, cote en bourse, ~559 employes)

## Description
TrustNXT developpe une plateforme logicielle de protection et verification de l'authenticite des contenus visuels (photos et videos) dans les applications B2B critiques. La technologie combine cryptographie, vision par ordinateur et technologie de confiance brevetee pour generer une empreinte numerique unique et inviolable des donnees capteur a leur point d'origine, creant un jumeau numerique inalterable du contenu et fournissant une preuve technique de son authenticite.

**Proposition de valeur** : Protection des photos et videos contre la manipulation par IA et les cyberattaques, grace a des labels cryptographiques apposes a la source. En assurance, la solution detecte les photos de dommages manipulees et permet l'automatisation complete des processus de sinistres et de souscription -- sans revision humaine.

### Probleme adresse
Avec l'essor de l'IA generative (deepfakes, images synthetiques), la fiabilite des contenus visuels numeriques est fondamentalement menacee. Dans l'assurance, les photos de sinistres manipulees ou fabriquees par IA alimentent la fraude. Dans l'industrie et la securite video, des flux video peuvent etre compromis par des cyberattaques. TrustNXT repond au besoin croissant de garantir l'authenticite et la provenance des contenus visuels dans un monde ou "voir n'est plus croire".

### Produits
| Produit | Usage | Resultat cle |
|---------|-------|---------------|
| **origo** | Produit phare -- empreinte cryptographique inviolable generee au point de capture du contenu visuel | Preuve technique d'authenticite, jumeau numerique inalterable |
| **TrustNXT CAM** | Solution assurance -- verification de medias numeriques pour sinistres, inspections, souscription | Detection de fraude photo/video, automatisation des claims sans revision humaine |
| **Video Security** | Protection en temps reel des flux video contre les cyberattaques sur divers appareils camera | Securite temps reel et preservation des preuves legales |
| **c2pa-ts** | Bibliotheque open source TypeScript (licence Apache 2.0) -- implementation pure du standard C2PA v2.1 | Lecture, validation et creation de manifestes C2PA, independante de toute plateforme |

### Technologie et Standards
- Cryptographie appliquee aux donnees capteur a l'origine (empreinte unique liee physiquement au medium)
- Vision par ordinateur (heritage Basler AG)
- Technologie de confiance brevetee (brevets detenus, notamment via Sebastian Adank)
- Membre officiel de la **Content Authenticity Initiative (CAI)** et de la **Coalition for Content Provenance and Authenticity (C2PA)**
- Bibliotheque open source c2pa-ts : implementation TypeScript pure du standard C2PA 2.1, sans binaire natif ni WebAssembly, fonctionnelle en navigateur et Node.js

### Chiffres cles
- 1,6M EUR leves en pre-seed (septembre 2025)
- Solution deja deployee dans le secteur assurance (premiers clients)
- Premiers projets pilotes industriels (video) prevus pour 2026
- Spin-off de Basler AG, leader mondial des cameras industrielles

## Histoire et fondateurs

### Genese
TrustNXT est ne de l'expertise de Basler AG, entreprise allemande cotee en bourse specialisee dans les cameras numeriques industrielles et le traitement d'images. Sebastian Adank, alors employe de Basler AG, a identifie il y a plus de six ans l'importance cruciale de la confiance dans les donnees d'image et travaille sur ce sujet depuis. Le spin-off a ete officialise en 2024, combinant l'expertise technique en vision par ordinateur de Basler avec des competences en cryptographie, cybersecurite et developpement commercial.

### Fondateurs
- **Sebastian Adank** (Co-fondateur & Managing Director) : Formation en informatique (Berner Fachhochschule BFH) et Executive MBA en Innovation Management. Ancien employe de Basler AG, porteur de plusieurs brevets lies a la technologie de confiance visuelle. Pionnier du sujet de l'authenticite des donnees image depuis 6+ ans.
- **Ariane Scheer-Danielsson** (Co-fondatrice & Managing Director, Business Dev & Marketing) : Diplomee de l'ESCP Business School (General Management). Expertise en economie, droit, innovation et digitalisation. Responsable du developpement commercial et marketing.
- **Andreas Reich** (Co-fondateur & Managing Director, CTO) : Leader technologique avec 20 ans d'experience. Ancien architecte d'infrastructure cloud chez AWS (workflows video automatises par IA, deploiement a grande echelle). Experience prealable chez ReichTech GmbH et FFG Finanzcheck.

## Clients
- Clients assurance (noms non publics au stade pre-seed, mais solution deja en production dans le secteur)
- Secteurs cibles : assurance, securite industrielle, securite publique, secteur juridique

## Traction et perspectives

### Traction
- Pre-seed de 1,6M EUR boucle en septembre 2025 aupres de D11Z.Ventures et HTGF (High-Tech Grunderfonds, l'un des plus grands fonds d'amorcage europeens)
- Solution assurance (TrustNXT CAM) deja en production avec des clients
- Bibliotheque open source c2pa-ts publiee sur GitHub et npm
- Membre CAI et C2PA, positionnement au coeur de l'ecosysteme de standards

### Perspectives
- Expansion vers la protection temps reel des flux video pour applications industrielles (premiers pilotes prevus 2026)
- Croissance du marche de la confiance numerique (481 Mds USD en 2025, projection 947 Mds USD en 2030 selon Mordor Intelligence)
- Adoption croissante du standard C2PA par les grandes plateformes (Google, Microsoft, Adobe, OpenAI, Meta, BBC, Sony)
- Positionnement unique a l'intersection cryptographie + vision par ordinateur + standards ouverts

## Concurrents directs
| Concurrent | Positionnement | Differentiation TrustNXT |
|-----------|---------------|--------------------------|
| **Truepic** (US) | Membre fondateur C2PA, authenticite des photos a la capture | TrustNXT couvre aussi la video temps reel et l'industriel ; ancrage europeen |
| **VAARHAFT** (Allemagne) | Detection de fraude image pour assurance, analyse C2PA | TrustNXT agit a la source (cryptographie capteur) vs detection a posteriori |
| **Reality Defender** (US) | Detection de deepfakes multi-medias (audio, video, image, texte) | TrustNXT mise sur la preuve d'authenticite a l'origine, pas uniquement la detection |
| **Digimarc** (US) | Filigranes numeriques durables + Content Credentials | TrustNXT combine capteur + cryptographie ; positionnement B2B assurance/industrie |
| **Inaza** (Irlande) | Detection d'images manipulees pour sinistres assurance | TrustNXT offre une approche plus large (video, industriel) avec brevets propres |
| **WeProov** (France) | Capture certifiee de preuves visuelles (constat, etat des lieux) | TrustNXT s'appuie sur la cryptographie capteur et les standards C2PA |

## Reputation
**Note de reputation** : 6/10
**Analyse** : TrustNXT est une startup en phase tres precoce (pre-seed, fondee en 2024) mais qui presente plusieurs atouts significatifs. L'origine en tant que spin-off de Basler AG, leader mondial reconnu des cameras industrielles, confere une credibilite technique rare pour une jeune pousse. La technologie brevetee combinant cryptographie et vision par ordinateur est differenciante. L'adhesion a la CAI et C2PA, ainsi que la contribution open source (c2pa-ts), temoignent d'un positionnement strategique au coeur des standards emergents d'authenticite numerique. L'equipe fondatrice est complementaire (technique/cloud, business, vision par ordinateur + brevets). Le financement par HTGF et D11Z.Ventures, deux fonds reputes dans l'ecosysteme allemand, est un signal positif. Cependant, la traction commerciale reste limitee et non quantifiee publiquement, les effectifs sont reduits, et la concurrence (Truepic, Reality Defender, VAARHAFT) est active sur ce marche en forte croissance. Le potentiel est eleve dans le contexte de l'explosion des deepfakes et de la fraude visuelle par IA, mais l'execution reste a demontrer a l'echelle. Pour l'assurance, le cas d'usage de detection de fraude photo est immediatement pertinent et deja en production.

## Tags & Categorisation

### Domaine & Perimetre
#auto #sinistres #fraude #authenticite #verification #cybersecurite #video-surveillance

### Acteurs & Roles
#assureur #assureur-auto #industrie #securite #juridique

### Cycle de vie
#fnol #expertise #detection-fraude #souscription #preuve-numerique

### Technologies
#computer-vision #cryptographie #c2pa #content-credentials #api #saas #open-source #typescript

### Geographie & Marche
#allemagne #europe #startup #pre-seed #deep-tech #spin-off
