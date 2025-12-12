import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def show_augmentation_preview(original_img):

    save_path='images/data_manipulation/four_augmentation/upper.jpg'
    # Se l'immagine è float (0-1), matplotlib la stampa bene.
    # Se fosse int (0-255), dovremmo convertirla, ma il tuo x_train è già / 255.0
    
    # --- A. FLIP ORIZZONTALE ---
    flip_img = np.flip(original_img, axis=1) # axis 1 è la larghezza
    
    rng = np.random.RandomState(39) 
    
    # 2. Generiamo il rumore usando il generatore bloccato (rng)
    noise = rng.normal(loc=0.0, scale=0.05, size=original_img.shape)
    # --- C. RUMORE GAUSSIANO (0.05) ---
    noise_img = original_img + noise
    noise_img = np.clip(noise_img, 0., 1.)

    factors = rng.uniform(0.1, 0.3)
    bright_img = np.clip(original_img + factors, 0.0, 1.0)

    factors_c = rng.uniform(0.4, 1.7)
    print(factors_c)

    mean = np.mean(original_img, axis=(1, 2), keepdims=True)
    
    x_contrast = (original_img - mean) * factors_c + mean
    x_contrast = np.clip(x_contrast, 0.0, 1.0)

    plt.figure(figsize=(16, 5))
    plt.suptitle("UPPER IMAGE", fontsize=20, weight='bold')
    # 1. Originale
    plt.subplot(1, 4, 1)
    plt.imshow(original_img)
    plt.title(f"Original")
    plt.axis('off')
    
    # 2. Flip
    plt.subplot(1, 4, 2)
    plt.imshow(x_contrast)
    plt.title("contrast")
    plt.axis('off')
    
    
    # 3. Noise
    plt.subplot(1, 4, 3)
    plt.imshow(noise_img)
    plt.title("Noise Gaussian 0.05")
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(bright_img)
    plt.title("add brightness")
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    
# LANCIA QUESTA FUNZIONE PIÙ VOLTE!
#img_path='dataset/images/lower_498895_jpg.rf.922d5ea4f740751115215aec15b9c23f.jpg'
img_path='dataset/images/upper_986458_jpg.rf.8045fd4d52f9b22231022cb9e7a1ec17.jpg'
image=cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype('float32') / 255.0
show_augmentation_preview(image)
