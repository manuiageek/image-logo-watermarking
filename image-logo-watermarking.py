from PIL import Image
import os

def add_image_watermark(input_folder, output_folder, watermark_image_path, area_percent=5, transparency=128):
    # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Charger l'image du watermark
    watermark = Image.open(watermark_image_path).convert("RGBA")

    # Parcourir toutes les images du dossier d'entrée
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Ouvrir l'image d'origine
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path).convert("RGBA")

            # Dimensions de l'image
            width, height = image.size

            # Calculer la superficie totale de l'image
            total_area = width * height

            # Calculer la superficie désirée du watermark
            desired_watermark_area = (area_percent / 100) * total_area

            # Préserver le rapport d'aspect du watermark
            aspect_ratio = watermark.width / watermark.height

            # Calculer la largeur et la hauteur du watermark
            watermark_width = int((desired_watermark_area * aspect_ratio) ** 0.5)
            watermark_height = int(watermark_width / aspect_ratio)

            # Assurer que la hauteur calculée correspond bien à la superficie désirée
            # Si nécessaire, ajuster la largeur et la hauteur
            watermark_resized = watermark.resize((watermark_width, watermark_height), Image.LANCZOS)

            # Appliquer la transparence au watermark sans perdre la transparence existante
            alpha = watermark_resized.getchannel('A')
            transparency_factor = transparency / 255.0
            alpha = alpha.point(lambda p: int(p * transparency_factor))
            watermark_resized.putalpha(alpha)

            # Calculer la position (en bas à droite)
            position = (width - watermark_width - 10, height - watermark_height - 10)

            # Créer un calque pour le watermark
            watermark_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
            watermark_layer.paste(watermark_resized, position, watermark_resized)

            # Combiner l'image d'origine et le watermark
            watermarked_image = Image.alpha_composite(image, watermark_layer)

            # Convertir l'image en mode RGB avec un fond blanc
            background = Image.new('RGB', watermarked_image.size, (255, 255, 255))
            background.paste(watermarked_image, mask=watermarked_image.split()[3])  # Utiliser le canal alpha comme masque

            # Enregistrer l'image dans le dossier de sortie
            output_path = os.path.join(output_folder, filename)
            background.save(output_path, "JPEG")

    print(f"Watermark ajouté sur toutes les images du dossier {input_folder} et enregistrées dans {output_folder}.")

# Configurer les chemins et les paramètres
input_folder = r'T:\TMP_PHOTO_EXPORT\input'
output_folder = r'T:\TMP_PHOTO_EXPORT\output'
watermark_image_path = r'T:\TMP_PHOTO_EXPORT\watermark\manuia_big_fondblanc_alpha.png'  # Utiliser un fichier PNG pour la transparence
area_percent = 2  # Pourcentage de la superficie totale de l'image pour la superficie du watermark
transparency = 182  # Transparence du watermark (0 à 255)

# Appeler la fonction
add_image_watermark(input_folder, output_folder, watermark_image_path, area_percent, transparency)
