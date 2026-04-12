# GFT (Generative Forecasting Transformer) par Silurian

## Identite
**Editeur** : Silurian (Silurian AI)
**Nom de la solution** : GFT (Generative Forecasting Transformer) / Earth API
**Date de mise a jour** : 2026-04-12
**Fondateurs** : Jayesh K. Gupta (CEO, ex-Microsoft Research, co-auteur du modele Aurora), Cristian Bodnar (ex-Senior Researcher Microsoft Research, co-lead Aurora, PhD Cambridge, ex-Google Brain/Google X/Twitter Cortex), Nikhil Shankar (Co-fondateur, Chief Engineer)
**Annee de creation** : 2024
**Siege** : Kirkland, Washington, Etats-Unis
**Batch YC** : S24
**Levees de fonds** : Pre-Seed $500K (Y Combinator, 2024). Autres investisseurs : Incubateur HEC Paris, Exitfund, Nivesha Ventures, Pioneer Fund, SurgePoint Capital (11 investisseurs au total)

## Description
Silurian developpe des modeles de fondation (foundation models) pour simuler les systemes terrestres, en commencant par la meteo. Le produit phare, GFT (Generative Forecasting Transformer), est un modele de 1,5 milliard de parametres capable de simuler la meteo mondiale jusqu'a 14 jours a l'avance avec une resolution d'environ 11 km. Le modele surpasse les systemes de prevision numerique des agences americaine (NOAA) et europeenne (ECMWF) jusqu'a 30% sur plusieurs variables.

L'entreprise a ete fondee en juin 2024 par d'anciens chercheurs de Microsoft Research qui ont co-developpe Aurora, le modele de fondation de 1,3 milliard de parametres de Microsoft pour le systeme terrestre. Cette expertise unique en IA climatique leur permet de proposer des previsions meteorologiques de nouvelle generation, alimentees par l'intelligence artificielle generative.

La pertinence pour le secteur de l'assurance est directe : les modeles de Silurian permettent une modelisation climatique avancee pour la tarification des risques, l'evaluation des risques catastrophes naturelles (cat-nat), la gestion des sinistres lies aux evenements meteorologiques extremes, et l'optimisation des portefeuilles exposes aux aleas climatiques. Un article publie dans Nature a demontre que les technologies de Silurian ameliorent la precision du suivi des cyclones tropicaux atlantiques d'environ 20%.

Silurian cible les secteurs de l'energie, de l'assurance, de l'agriculture et de la logistique. L'entreprise commercialise ses previsions via une API (Earth API) et des modeles specialises comme GFT-C pour les cyclones tropicaux.

## Produits et fonctionnalites
| Fonctionnalite | Description |
|----------------|-------------|
| GFT (Generative Forecasting Transformer) | Modele de fondation de 1,5B parametres simulant la meteo mondiale a 14 jours, resolution ~11 km, surpassant NOAA et ECMWF de 30% |
| Earth API | API operationnelle permettant d'acceder aux previsions GFT en temps reel (earth.weather.silurian.ai) |
| GFT-C (Cyclones) | Version fine-tunee de GFT specialisee pour les cyclones tropicaux, combinant vitesse du ML et suivi des tempetes a long horizon |
| Prevision d'ouragans | Premier API basee sur l'IA pour la prevision operationnelle des ouragans, avec suivi ensembliste et analytique predictive |
| Previsions hyper-locales | Fine-tuning sur observations locales pour des previsions au niveau des actifs : temperature, precipitation, vent, risque de givrage |
| Variables etendues | Vitesse du vent a 100m, radiation solaire, couverture nuageuse, probabilite de precipitation, humidite |
| Prevision energie renouvelable | Previsions specialisees pour l'eolien (vitesse du vent a hauteur de moyeu, risque de givrage des turbines) et le solaire |

## Clients
- **Disaster Tech** : Integration de GFT-C dans la plateforme PRATUS pour la prevision des ouragans et l'aide a la decision en gestion de crise (partenariat annonce en juin 2025)
- Secteurs cibles : energie, assurance, agriculture, logistique
- Cas d'usage demontre : prevision correcte de l'atterrissage de l'ouragan Beryl au Texas alors que NOAA et ECMWF predisaient un atterrissage au Mexique

## Reputation
**Note de reputation** : 8/10
**Analyse** : Silurian beneficie d'une credibilite scientifique exceptionnelle grace au pedigree de ses fondateurs (co-auteurs d'Aurora chez Microsoft Research) et a une publication dans Nature validant leurs resultats. Le modele GFT represente une avancee significative par rapport aux methodes traditionnelles de prevision meteorologique. La startup est encore jeune (fondee mi-2024) et en phase de commercialisation, mais les resultats techniques sont impressionnants et la trajectoire est prometteuse. Le partenariat avec Disaster Tech valide l'applicabilite operationnelle de la technologie.

## Tags & Categorisation
### Domaine & Perimetre
`Assurance IARD` `Reassurance` `Cat-Nat` `Risques climatiques` `Modelisation des risques` `Tarification` `Agriculture`
### Acteurs & Roles
`Assureurs` `Reassureurs` `Courtiers` `Risk Managers` `Actuaires` `Souscripteurs`
### Cycle de vie
`Souscription` `Tarification` `Gestion des risques` `Modelisation` `Prevision`
### Capacites metier
`Modelisation climatique` `Evaluation des risques cat-nat` `Prevision meteorologique` `Scoring de risque` `Surveillance de portefeuille` `Aide a la decision`
### Technologie & IA
`Foundation Model` `Deep Learning` `Transformers` `IA generative` `Modele de 1.5B parametres` `API REST` `Fine-tuning` `Prevision ensembliste`

## Ressources
**Site officiel** : https://silurian.ai/
**Y Combinator** : https://www.ycombinator.com/companies/silurian
**Earth API** : https://earth.weather.silurian.ai/
**Publication Nature** : Amelioration de 20% de la precision du suivi des cyclones tropicaux atlantiques
