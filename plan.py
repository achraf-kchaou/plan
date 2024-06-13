import pandas as pd

# Introduction data
intro_data = {
    "Rubrique": ["Objectif", "Durée Totale", "Ressources"],
    "Description": [
        "Maîtriser les concepts fondamentaux et avancés de IBM DataStage",
        "16 semaines",
        "Formations en ligne, tutoriels, documentation IBM, livres, projets pratiques, mentorat"
    ]
}
intro_df = pd.DataFrame(intro_data)

# Plan de Formation data
formation_data = {
    "Module": [
        "Introduction et Concepts de Base",
        "Développement de Jobs de Base",
        "Techniques Avancées de Développement",
        "Intégration et Administration"
    ],
    "Contenu": [
        "Introduction à ETL et IBM DataStage, Architecture, Environnement de développement, Concepts de base",
        "Création et exécution de Jobs simples, Utilisation des Stages, Gestion des métadonnées, Fonctions et expressions",
        "Paramétrage et séquences, Debugging, Optimisation, Stages avancés",
        "Gestion des projets, Sécurité, Migration, Surveillance"
    ],
    "Durée": ["2 semaines", "3 semaines", "4 semaines", "3 semaines"],
    "Ressources": [
        "Cours en ligne IBM, Documentation IBM",
        "Tutoriels vidéo IBM, Livres recommandés",
        "Formations avancées IBM, Documentation avancée",
        "Ateliers pratiques, Formations sur l'administration"
    ]
}
formation_df = pd.DataFrame(formation_data)

# Certifications data
certifications_data = {
    "Certification": [
        "IBM Certified Solution Developer",
        "IBM Certified Administrator"
    ],
    "Objectif": [
        "Valider les compétences de développement DataStage",
        "Valider les compétences d'administration DataStage"
    ],
    "Préparation": [
        "Guides de préparation, Examens blancs",
        "Guides de préparation, Examens blancs"
    ],
    "Durée": ["Variable", "Variable"]
}
certifications_df = pd.DataFrame(certifications_data)

# Projets Pratiques et Mentorat data
projets_data = {
    "Activité": [
        "Projets Pratiques",
        "Mentorat et Évaluation"
    ],
    "Description": [
        "Implémentation de projets réels, Évaluation, Optimisation, Documentation",
        "Sessions de mentorat, Revue des travaux, Feedback personnalisé"
    ],
    "Durée": ["4 semaines", "4 semaines"],
    "Ressources": [
        "Exemples de projets IBM, Supports pratiques",
        "Experts DataStage, Plan d'amélioration"
    ]
}
projets_df = pd.DataFrame(projets_data)

# Ressources Complémentaires data
ressources_data = {
    "Type": [
        "Forums et Communautés",
        "Livres et Guides",
        "Webinaires et Séminaires"
    ],
    "Détails": [
        "IBM Community, Stack Overflow",
        "IBM InfoSphere DataStage for Dummies, Data Integration with IBM InfoSphere DataStage",
        "Webinaires IBM, Séminaires en ligne"
    ]
}
ressources_df = pd.DataFrame(ressources_data)

# Create Excel writer object
with pd.ExcelWriter('/mnt/data/Plan_de_Montée_en_Compétences_IBM_DataStage.xlsx') as writer:
    intro_df.to_excel(writer, sheet_name='Introduction', index=False)
    formation_df.to_excel(writer, sheet_name='Plan de Formation', index=False)
    certifications_df.to_excel(writer, sheet_name='Certifications', index=False)
    projets_df.to_excel(writer, sheet_name='Projets Pratiques et Mentorat', index=False)
    ressources_df.to_excel(writer, sheet_name='Ressources Complémentaires', index=False)
