#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de signatures email ADN - Version avec assets hébergés sur GitHub
Compatible Gmail, Outlook et tous les clients email
"""

contacts = {
    "hamin": { "name": "Hamin TAHRI", "post": "Account Manager", "phone": "+33 6 95 09 66 72", "phoneRaw": "https://wa.me/+33695096672", "email": "hamin.tahri@adnumeric.net" },
    "muriel": { "name": "Muriel DE GERLACHE", "post": "Account Manager", "phone": "+33 6 70 49 63 58", "phoneRaw": "https://wa.me/+33670496358", "email": "muriel.degerlache@adnumeric.net" },
    "philippe_b": { "name": "Philippe BACHELIER", "post": "Responsable Achat", "phone": "+33 6 52 49 50 40", "phoneRaw": "https://wa.me/+33652495040", "email": "philippe.bachelier@adnumeric.net" },
    "philippe_d": { "name": "Philippe DORLÉAC", "post": "Responsable financier", "phone": "+33 6 87 22 81 50", "phoneRaw": "https://wa.me/+33687228150", "email": "philippe.dorleac@adnumeric.net" },
    "pauline": { "name": "Pauline VALTIER", "post": "Account Manager", "phone": "+33 6 18 34 03 10", "phoneRaw": "https://wa.me/+33618340310", "email": "pauline.valtier@adnumeric.net" },
    "patrick": { "name": "Patrick HUOT", "post": "Account Manager", "phone": "+33 7 49 03 84 80", "phoneRaw": "https://wa.me/+33749038480", "email": "patrick.huot@adnumeric.net" },
    "max": { "name": "Max PATON", "post": "Account Manager", "phone": "+33 7 45 04 11 77", "phoneRaw": "https://wa.me/+33745041177", "email": "max.paton@adnumeric.net" },
    "marielux": { "name": "Marie-Lux AMIAN", "post": "Responsable Marketing", "phone": "+33 6 49 56 11 47", "phoneRaw": "https://wa.me/+33649561147", "email": "marie-lux.amian@adnumeric.net" },
    "saloua": { "name": "Saloua SADDOUKI", "post": "Assistante Administrative et Logistique", "phone": "+33 7 65 60 61 01", "phoneRaw": "https://wa.me/+33765606101", "email": "saloua.saddouki@adnumeric.net" },
    "lionel": { "name": "Lionel TURQUIN", "post": "Directeur Général", "phone": "+33 6 65 44 75 98", "phoneRaw": "https://wa.me/+33665447598", "email": "lionel.turquin@adnumeric.net" },
    "guilhem": { "name": "Guilhem MARC", "post": "Responsable comptable", "phone": "+33 6 13 66 04 39", "phoneRaw": "https://wa.me/+33613660439", "email": "guilhem.marc@adnumeric.net" },
    "gaetan": { "name": "Gaetan MIRA", "post": "Coordinateur Logistique", "phone": "+33 6 49 72 22 02", "phoneRaw": "https://wa.me/+33649722202", "email": "gaetan.mira@adn-services.net" },
    "florence": { "name": "Florence O. TODEHOUN", "post": "Account Manager", "phone": "+229 67 84 86 55", "phoneRaw": "https://wa.me/+22967848655", "email": "florence.todehoun@adnwca.com" },
    "bettina": { "name": "Bettina ARMINGEAT", "post": "Assistante De Direction", "phone": "+33 6 68 77 57 80", "phoneRaw": "https://wa.me/+33668775780", "email": "bettina.armingeat@adnumeric.net" },
    "andre": { "name": "André TURQUIN", "post": "Gérant Associé", "phone": "+33 6 14 21 55 28", "phoneRaw": "https://wa.me/+33614215528", "email": "andre.turquin@adnumeric.net" },
    "cristina": { "name": "Cristina IENCULESCU", "post": "Account Manager", "phone": "+33 6 70 39 82 66", "phoneRaw": "https://wa.me/+33670398266", "email": "cristina.ienculescu@adnumeric.net" },
    "benoit": { "name": "Benoît BOSSI", "post": "Account Manager", "phone": "+33 6 70 43 71 87", "phoneRaw": "https://wa.me/+33670437187", "email": "benoit.bossi@adnumeric.net" },
    "achraf": { "name": "Achraf ABHILIL", "post": "Software Engineer", "phone": "+33 6 78 69 26 13", "phoneRaw": "https://wa.me/+33678692613", "email": "achraf.abhilil@adn-services.net" },
    "hassan": { "name": "Hassan AIT ININOU", "post": "Responsable SAV", "phone": "+33 7 64 43 01 92", "phoneRaw": "https://wa.me/+33764430192", "email": "hassan.aitininou@adn-services.net" },
    "mathieu": { "name": "Mathieu PIERRARD", "post": "Technicien SAV", "phone": "+33 7 45 04 11 77", "phoneRaw": "https://wa.me/+33745041177", "email": "mathieu.pierrard@adn-services.net" },
    "olena": { "name": "Olena SERDYUK", "post": "Account Manager", "phone": "+33 6 87 52 08 25", "phoneRaw": "https://wa.me/+33687520825", "email": "olena.serdyuk@adnumeric.net" }
}

adn_info = {
    "rue": "254 Avenue Victor Hugo",
    "code_postal": "34400",
    "ville": "Lunel",
    "pays": "France",
    "website": "https://www.adn-distribution.com",
    "linkedin": "https://www.linkedin.com/company/adn-action-pour-le-developpement-numerique/",
    "certifications": "assets/certifications.png"
}

# Configuration des liens d'assets
# Pour l'instant : liens locaux
# À remplacer par les liens GitHub une fois hébergé
ASSETS_CONFIG = {
    "logo_adn": "assets/ADN.png",
    "certifications": "assets/certifications.png",
    "brands": "assets/brands.png",
    "icon_map": "assets/icons/map-pin-2-line.png",
    "icon_whatsapp": "assets/icons/whatsapp-line.png",
    "icon_mail": "assets/icons/mail-line.png",
    "icon_global": "assets/icons/global-line.png",
    "icon_linkedin": "assets/icons/linkedin-fill.png"
}

# Exemple de liens GitHub (à utiliser une fois hébergé)
# ASSETS_CONFIG = {
#     "logo_adn": "https://raw.githubusercontent.com/votre-repo/main/assets/ADN.png",
#     "certifications": "https://raw.githubusercontent.com/votre-repo/main/assets/certifications.png",
#     "brands": "https://raw.githubusercontent.com/votre-repo/main/assets/brands.png",
#     "icon_map": "https://raw.githubusercontent.com/votre-repo/main/assets/icons/map-pin-2-line.png",
#     "icon_whatsapp": "https://raw.githubusercontent.com/votre-repo/main/assets/icons/whatsapp-line.png",
#     "icon_mail": "https://raw.githubusercontent.com/votre-repo/main/assets/icons/mail-line.png",
#     "icon_global": "https://raw.githubusercontent.com/votre-repo/main/assets/icons/global-line.png",
#     "icon_linkedin": "https://raw.githubusercontent.com/votre-repo/main/assets/icons/linkedin-fill.png"
# }

def generate_signature_html_github(contact_id, contact_data):
    """
    Génère une signature email HTML avec assets hébergés
    Compatible Gmail, Outlook et tous les clients email
    """
    # Adresse complète
    address = f"{adn_info['rue']}<br>{adn_info['code_postal']} {adn_info['ville']}, {adn_info['pays']}"
    
    # QR code (pour l'instant local, à remplacer par GitHub)
    qr_code = f"assets/qrcodes/{contact_id}_vcard.png"
    
    signature_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signature Email ADN - {contact_data['name']}</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #FFFFFF;">
    
    <!-- Signature Email ADN -->
    <table cellpadding="0" cellspacing="0" border="0" style="width: 650px; max-width: 650px; background-color: #FFFFFF; font-family: Arial, sans-serif;">
        
        <!-- Contenu principal -->
        <tr>
            <td style="padding: 20px 0;">
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                    <tr>
                        
                        <!-- Colonne gauche : Logo et certifications -->
                        <td style="width: 120px; vertical-align: top; padding-right: 20px;">
                            <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                                <!-- Logo principal -->
                                <tr>
                                    <td style="padding-bottom: 15px;">
                                        <img src="{ASSETS_CONFIG['logo_adn']}" alt="ADN" style="width: 100px; height: auto; display: block;">
                                    </td>
                                </tr>
                                <!-- Certifications -->
                                <tr>
                                    <td style="text-align: center;">
                                        <img src="{ASSETS_CONFIG['certifications']}" alt="Certifications Lenovo et ASUS" style="width: 100px; height: auto; display: block;">
                                    </td>
                                </tr>
                            </table>
                        </td>
                        
                        <!-- Colonne centrale : Informations personnelles -->
                        <td style="vertical-align: top; padding-right: 20px;">
                            <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                                <!-- Nom -->
                                <tr>
                                    <td style="padding-bottom: 5px;">
                                        <span style="font-size: 16px; font-weight: bold; color: #394827; font-family: Arial, sans-serif;">{contact_data['name']}</span>
                                    </td>
                                </tr>
                                <!-- Poste -->
                                <tr>
                                    <td style="padding-bottom: 15px;">
                                        <span style="font-size: 13px; color: #666666; font-family: Arial, sans-serif;">{contact_data['post']}</span>
                                    </td>
                                </tr>
                                <!-- Adresse -->
                                <tr>
                                    <td style="padding-bottom: 8px;">
                                        <table cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td style="width: 16px; vertical-align: top; padding-right: 8px;">
                                                    <img src="{ASSETS_CONFIG['icon_map']}" alt="Adresse" style="width: 14px; height: 14px; display: block;">
                                                </td>
                                                <td style="vertical-align: top;">
                                                    <span style="font-size: 12px; color: #869872; font-family: Arial, sans-serif; line-height: 1.4;">
                                                        {address}
                                                    </span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <!-- Téléphone -->
                                <tr>
                                    <td style="padding-bottom: 8px;">
                                        <table cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td style="width: 16px; vertical-align: top; padding-right: 8px;">
                                                    <img src="{ASSETS_CONFIG['icon_whatsapp']}" alt="Téléphone" style="width: 14px; height: 14px; display: block;">
                                                </td>
                                                <td style="vertical-align: top;">
                                                    <a href="{contact_data['phoneRaw']}" style="font-size: 12px; color: #305e37; text-decoration: none; font-family: Arial, sans-serif;">{contact_data['phone']}</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <!-- Email -->
                                <tr>
                                    <td style="padding-bottom: 8px;">
                                        <table cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td style="width: 16px; vertical-align: top; padding-right: 8px;">
                                                    <img src="{ASSETS_CONFIG['icon_mail']}" alt="Email" style="width: 14px; height: 14px; display: block;">
                                                </td>
                                                <td style="vertical-align: top;">
                                                    <a href="mailto:{contact_data['email']}" style="font-size: 12px; color: #305e37; text-decoration: none; font-family: Arial, sans-serif;">{contact_data['email']}</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <!-- Site web -->
                                <tr>
                                    <td style="padding-bottom: 8px;">
                                        <table cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td style="width: 16px; vertical-align: top; padding-right: 8px;">
                                                    <img src="{ASSETS_CONFIG['icon_global']}" alt="Site web" style="width: 14px; height: 14px; display: block;">
                                                </td>
                                                <td style="vertical-align: top;">
                                                    <a href="{adn_info['website']}" style="font-size: 12px; color: #305e37; text-decoration: none; font-family: Arial, sans-serif;">www.adn-distribution.com</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <!-- LinkedIn -->
                                <tr>
                                    <td>
                                        <table cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td style="width: 16px; vertical-align: top; padding-right: 8px;">
                                                    <img src="{ASSETS_CONFIG['icon_linkedin']}" alt="LinkedIn" style="width: 14px; height: 14px; display: block;">
                                                </td>
                                                <td style="vertical-align: top;">
                                                    <a href="{adn_info['linkedin']}" style="font-size: 12px; color: #305e37; text-decoration: none; font-family: Arial, sans-serif;">linkedin.com/company/adn-action-pour-le-developpement-numerique</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                        
                        <!-- Colonne droite : QR Code -->
                        <td style="width: 100px; vertical-align: top;">
                            <img src="{qr_code}" alt="QR Code vCard" style="width: 100px; height: 100px; display: block;">
                        </td>
                        
                    </tr>
                </table>
            </td>
        </tr>
        
        <!-- Bandeau inférieur avec ligne et logos partenaires -->
        <tr>
            <td style="padding-top: 20px;">
                <!-- Ligne horizontale -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%; margin-bottom: 15px;">
                    <tr>
                        <td style="height: 1px; background-color: #e0e0e0;"></td>
                    </tr>
                </table>
                
                <!-- Logos des partenaires -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%; text-align: center;">
                    <tr>
                        <td>
                            <img src="{ASSETS_CONFIG['brands']}" alt="Partenaires" style="width: 100%; max-width: 650px; height: auto; display: block; margin: 0 auto;">
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        
    </table>
    
</body>
</html>'''
    
    return signature_html

def generate_all_signatures_github():
    """
    Génère toutes les signatures email avec assets hébergés
    """
    import os
    
    # Créer le dossier signatures s'il n'existe pas
    if not os.path.exists('signatures_github'):
        os.makedirs('signatures_github')
    
    # Générer une signature pour chaque contact
    for contact_id, contact_data in contacts.items():
        signature_html = generate_signature_html_github(contact_id, contact_data)
        
        # Sauvegarder dans un fichier
        filename = f"signatures_github/signature_{contact_id}_github.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(signature_html)
        
        print(f"Signature GitHub générée pour {contact_data['name']}: {filename}")

def generate_signature_for_contact_github(contact_id):
    """
    Génère une signature avec assets hébergés pour un contact spécifique
    """
    if contact_id not in contacts:
        print(f"Contact '{contact_id}' non trouvé.")
        print("Contacts disponibles:", list(contacts.keys()))
        return None
    
    contact_data = contacts[contact_id]
    signature_html = generate_signature_html_github(contact_id, contact_data)
    
    # Sauvegarder dans un fichier
    filename = f"signature_{contact_id}_github.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(signature_html)
    
    print(f"Signature GitHub générée pour {contact_data['name']}: {filename}")
    return signature_html

def update_github_links(github_repo_url):
    """
    Met à jour les liens pour utiliser GitHub
    """
    global ASSETS_CONFIG
    
    # Extraire le nom du repo et de l'utilisateur
    # Exemple: https://github.com/username/repo-name
    parts = github_repo_url.rstrip('/').split('/')
    if len(parts) >= 2:
        username = parts[-2]
        repo_name = parts[-1]
        
        base_url = f"https://raw.githubusercontent.com/{username}/{repo_name}/main"
        
        ASSETS_CONFIG = {
            "logo_adn": f"{base_url}/assets/ADN.png",
            "certifications": f"{base_url}/assets/certifications.png",
            "brands": f"{base_url}/assets/brands.png",
            "icon_map": f"{base_url}/assets/icons/map-pin-2-line.png",
            "icon_whatsapp": f"{base_url}/assets/icons/whatsapp-line.png",
            "icon_mail": f"{base_url}/assets/icons/mail-line.png",
            "icon_global": f"{base_url}/assets/icons/global-line.png",
            "icon_linkedin": f"{base_url}/assets/icons/linkedin-fill.png"
        }
        
        print(f"✅ Liens GitHub mis à jour avec: {base_url}")
        return True
    else:
        print("❌ URL GitHub invalide")
        return False

# Exemple d'utilisation :
if __name__ == "__main__":
    print("=== Générateur de signatures email ADN - Version GitHub ===")
    print(f"Nombre de contacts: {len(contacts)}")
    print("\nContacts disponibles:")
    for contact_id, contact_data in contacts.items():
        print(f"  - {contact_id}: {contact_data['name']} ({contact_data['post']})")
    
    print("\nPour générer toutes les signatures GitHub:")
    print("  generate_all_signatures_github()")
    
    print("\nPour générer une signature spécifique GitHub:")
    print("  generate_signature_for_contact_github('achraf')")
    
    print("\nPour mettre à jour les liens GitHub:")
    print("  update_github_links('https://github.com/username/repo-name')")
    
    print("\n✅ Avantages de cette version:")
    print("   • Compatible Gmail, Outlook, tous les clients")
    print("   • Assets hébergés sur GitHub")
    print("   • Liens configurables facilement")
    print("   • Fichiers légers")
    print("   • Design complet avec vraies images")
