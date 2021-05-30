import random
import numpy as np

# Randomly select a defined number of image paires from a given dataset
def get_image_combinations(number_image_pairs_selected, image_data, image_labels):
    
    num_images_total = len(image_labels)
    
    image_combination_data = []
    image_combination_labels = []
    
    for i in range(number_image_pairs_selected):
        
        # Draw two image indices from a uniform random distribution
        random_index_A = random.randint(0, num_images_total-1)
        random_index_B = random.randint(0, num_images_total-1)
        
        # Randomly choose two images from the dataset
        image_A = image_data[random_index_A]
        image_B = image_data[random_index_B]
        
        # Merge images
        combined_images = np.hstack((image_A, image_B))
        
        # Find the minimum between the two labels
        label_A = image_labels[random_index_A]
        label_B = image_labels[random_index_B]
        minimum_label = min(label_A, label_B)
        
        # Append newly generated image combination and minimum label to list
        image_combination_data.append(combined_images)
        image_combination_labels.append(minimum_label)
        
    # Convert image data and labels lists to numpy arrays
    image_combination_data = np.array(image_combination_data)
    image_combination_labels = np.array(image_combination_labels)
    
    return image_combination_data, image_combination_labels



# Randomly select a defined number of image paires from a given dataset
# Always store the minimum image on the left
def get_left_min_image_combinations(number_image_pairs_selected, image_data, image_labels):
    
    num_images_total = len(image_labels)
    
    image_combination_data = []
    image_combination_labels = []
    
    for i in range(number_image_pairs_selected):
        
        # Draw two image indices from a uniform random distribution
        random_index_A = random.randint(0, num_images_total-1)
        random_index_B = random.randint(0, num_images_total-1)
        
        # Randomly choose two images from the dataset
        image_A = image_data[random_index_A]
        image_B = image_data[random_index_B]
        
        # Find the minimum between the two labels
        label_A = image_labels[random_index_A]
        label_B = image_labels[random_index_B]
        minimum_label = min(label_A, label_B)
        
        if label_A <= label_B:
            combined_images = np.hstack((image_A, image_B))
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data.append(combined_images)
            image_combination_labels.append(minimum_label)
        elif label_A > label_B: 
            combined_images = np.hstack((image_B, image_A))
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data.append(combined_images)
            image_combination_labels.append(minimum_label)
        
    # Convert image data and labels lists to numpy arrays
    image_combination_data = np.array(image_combination_data)
    image_combination_labels = np.array(image_combination_labels)
    
    return image_combination_data, image_combination_labels


# Randomly select a defined number of image paires from a given dataset
# Always store the minimum image on the left
def get_right_min_image_combinations(number_image_pairs_selected, image_data, image_labels):
    
    num_images_total = len(image_labels)
    
    image_combination_data = []
    image_combination_labels = []
    
    for i in range(number_image_pairs_selected):
        
        # Draw two image indices from a uniform random distribution
        random_index_A = random.randint(0, num_images_total-1)
        random_index_B = random.randint(0, num_images_total-1)
        
        # Randomly choose two images from the dataset
        image_A = image_data[random_index_A]
        image_B = image_data[random_index_B]
        
        # Find the minimum between the two labels
        label_A = image_labels[random_index_A]
        label_B = image_labels[random_index_B]
        minimum_label = min(label_A, label_B)
        
        if label_A > label_B:
            combined_images = np.hstack((image_A, image_B))
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data.append(combined_images)
            image_combination_labels.append(minimum_label)
        elif label_A <= label_B: 
            combined_images = np.hstack((image_B, image_A))
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data.append(combined_images)
            image_combination_labels.append(minimum_label)
        
    # Convert image data and labels lists to numpy arrays
    image_combination_data = np.array(image_combination_data)
    image_combination_labels = np.array(image_combination_labels)
    
    return image_combination_data, image_combination_labels


# Randomly select a defined number of image paires from a given dataset
# Always store the minimum image on the left
def get_left_min_image_combinations_separate(number_image_pairs_selected, image_data, image_labels):
    
    num_images_total = len(image_labels)
    
    image_combination_data_A = []
    image_combination_data_B = []
    
    image_combination_labels = []
    
    for i in range(number_image_pairs_selected):
        
        # Draw two image indices from a uniform random distribution
        random_index_A = random.randint(0, num_images_total-1)
        random_index_B = random.randint(0, num_images_total-1)
        
        # Randomly choose two images from the dataset
        image_A = image_data[random_index_A]
        image_B = image_data[random_index_B]
        
        # Find the minimum between the two labels
        label_A = image_labels[random_index_A]
        label_B = image_labels[random_index_B]
        minimum_label = min(label_A, label_B)
        
        if label_A < label_B:
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data_A.append(image_A)
            image_combination_data_B.append(image_B)
            
            image_combination_labels.append(minimum_label)
        elif label_A > label_B: 
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data_A.append(image_B)
            image_combination_data_B.append(image_A)
            image_combination_labels.append(minimum_label)
        
    # Convert image data and labels lists to numpy arrays
    image_combination_data_A = np.array(image_combination_data_A)
    image_combination_data_B = np.array(image_combination_data_B)
    
    image_combination_labels = np.array(image_combination_labels)
    
    return image_combination_data_A, image_combination_data_B, image_combination_labels


# Randomly select a defined number of image paires from a given dataset
# Always store the minimum image on the left
def get_right_min_image_combinations_separate(number_image_pairs_selected, image_data, image_labels):
    
    num_images_total = len(image_labels)
    
    image_combination_data_A = []
    image_combination_data_B = []
    
    image_combination_labels = []
    
    for i in range(number_image_pairs_selected):
        
        # Draw two image indices from a uniform random distribution
        random_index_A = random.randint(0, num_images_total-1)
        random_index_B = random.randint(0, num_images_total-1)
        
        # Randomly choose two images from the dataset
        image_A = image_data[random_index_A]
        image_B = image_data[random_index_B]
        
        # Find the minimum between the two labels
        label_A = image_labels[random_index_A]
        label_B = image_labels[random_index_B]
        minimum_label = min(label_A, label_B)
        
        if label_A > label_B:
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data_A.append(image_A)
            image_combination_data_B.append(image_B)
            
            image_combination_labels.append(minimum_label)
            
        elif label_A < label_B: 
            # Here we want to exclude the images where they are the same on both sides
            image_combination_data_A.append(image_B)
            image_combination_data_B.append(image_A)
            
            image_combination_labels.append(minimum_label)
        
    # Convert image data and labels lists to numpy arrays
    image_combination_data_A = np.array(image_combination_data_A)
    image_combination_data_B = np.array(image_combination_data_B)
    
    image_combination_labels = np.array(image_combination_labels)
    
    return image_combination_data_A, image_combination_data_B, image_combination_labels
