import numpy as np
import librosa
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from keras.models import Sequential
from keras.layers import LSTM, Dense
from collections import Counter


# Define the location of your .wav file
wav_file_location = 'C:\\Users\\zreba\\Downloads\\alright.wav'

# Load the audio file
audio, sample_rate = librosa.load(wav_file_location, sr=16000)

# Generate the mel-spectrogram
mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_mels=3, fmax=8000)
mel_spectrogram_reshaped = mel_spectrogram.T

# Perform K-means clustering
num_clusters = 6
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(mel_spectrogram_reshaped)
clustered_features = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Define your custom color library using HEX values (replace with your actual colors)
# For example, let's assume you have 1000 custom colors
custom_colors_hex = [
    "#FF0000",  # Red
    "#00FF00",  # Green
    "#0000FF",  # Blue
    "#00FFFF",  # Cyan
    "#FF00FF",  # Magenta
    "#FFFF00"   # Yellow
    "#A591B1",  # Purpurea/Hops
    "#6A7363",  # (Smart) Taupe
    "#F91E6C",  # (Smart) Emerald and Ruby
    "#722723",  # (Smart) Blue with Rust
    "#0A9879",  # Sky Green with a Hint of Purple
    "#D5FF95",
    "#65226F",  # Alexandria's Genesis
    "#25226F",  # Sega Genesis
    "#432125",  # Deathclocked
    "#127659",  # Gabriel
    "#D7866A",  # LCL
    "#017179",  # Fluke
    "#071797",  # Flukier
    "#8B4513",  # Emerald Brown
    "#BCACB0",  # Favoritism
    "#CFCD6C",  # True Citrine
    "#194127",  # Prime
    "#8B0008",  # Haunted
    "#1A0000",  # Thermal Vision
    "#006400",  # Jungle Green
    "#FFA500",  # Vibrant Orange
    "#4B5320",  # Camouflage Green
    "#EFE4B0",  # Cambrian Yellow
    "#C0C0C0",  # Reflective Gray
    "#FFFF00",  # Neuroplasticity Yellow
    "#87CEEB",  # Ozone Blue
    "#FF69B4",  # Gemstone Pink
    "#663399",  # Clematis Purple
    "#8B12A9",  # Machine Queen Purple
    "#874399",  # Myrmex Purple
    "#FF4500",  # Sound Wave Orange
    "#00BFFF",  # Sky Blue
    "#6495ED",  # Tranquil Blue
    "#8B4513",  # Warm Brown
    "#800000",  # Chaotic Red
    "#483D8B",  # Eerie Blue-Purple
    "#FFD700",  # Manic Yellow
    "#800080",  # Possession Purple
    "#9932CC",  # Hex Purple
    "#FF6347",  # Jinxed Orange-Red
    "#FFA07A",  # Warning Orange
    "#4B0082",  # Overdose Purple
    "#FF8C00",  # Energetic Orange
    "#000080",  # Profound Blue
    "#696969",  # Entropy Gray
    "#00FF00",  # Information Green
    "#336699",  # Community Blue-Purple
    "#333333",  # Deadlined Gray
    "#8B0000",  # Gremory Red
    "#808080",  # Zeta Gray
    "#8A2BE2",  # Clairvoyant Blue-Purple
    "#6495ED",  # Awareness Blue
    "#80FF00",  # Sour Green
    "#FFFF99",  # Phosphene Yellow
    "#996633",  # Antiquity Brown
    "#6699FF",  # Future Blue
    "#993399",  # Dissonance Purple
    "#99CC00",  # Harmony Green
    "#FF1493",  # Audicle Pink
    "#FF7F50",  # Resonance Coral
    "#2F4F4F",  # Primordial Gray
    "#4684B4",  # Octave Blue
    "#CD5C5C",  # Electrocuted Red
    "#2E2E2E",  # Eclipse Gray
    "#FF69B4",  # Aurora Pink
    "#32CD32",  # Miracle Green
    "#166633",  # Seasonal Depression Green
    "#4169E1",  # Internet Culture Blue
    "#ADD8E6",  # Zack's Blue
    "#228B22",  # Everything Green
    "#007FFF",  # Graphical Interface Blue
    "#00CED1",  # Synesthetic Turquoise
    "#40E0D0",  # Turquoise Gemstone
    "#6B8E23",  # Agate Green
    "#5A3442",  # Z4BKMU
    "#4B4D55",  # Smooth Stone Gray
    "#A84B00",  # Complex Orange
    "#0C2025",  # Pietersite Midnight Blue
    "#0066CC",  # Recycling Blue
    "#393A3C",  # Somber Gray-Blue
    "#726452",  # Sconce Coffee
    "#7BCC7F",  # Recording Lime Green
    "#A71747",  # Video Production Magenta-Ruby
    "#1AFFEA",  # Latent Recording Cyanaqua
    "#00555C",  # Low-Mid Deep Teal
    "#FF5733",  # High-Mid Red-Orange
    "#800020",  # Mid-Band Deep Red
    "#E6E6FA",  # Air-Band Lavender
    "#0A0A2E",  # Sub-Hertz Deep Blue-Purple
    "#2B0808",  # Infrared Maroon
    "#C3E3A3",  # Soft Lime
    "#008B8B",  # Deep Cyan
    "#190F38",  # Infrasonic
    "#127659",  # Limerick
    "#9ACD32",  # Great Green
    "#DAA520",  # True Gold
    "#FFD700",  # Canary
    "#DAE94F",  # Betaeyes
    "#DCE650",  # Polar Eyes
    "#DDCE46",  # Maple Eyes
    "#CCE689",  # Alphaeyes
    "#B5D79C"   # Albus Eyes


]

# Convert HEX colors to RGB
custom_colors_rgb = [tuple(int(hex[i:i+2], 16) for i in (1, 3, 5)) for hex in custom_colors_hex]
# Count the frequency of each cluster label
cluster_label_counts = Counter(clustered_features)

# Sort the cluster labels by frequency in descending order
sorted_cluster_labels = [label for label, _ in cluster_label_counts.most_common()]

# Map cluster labels to colors based on frequency
color_mapping_rgb = np.array([custom_colors_rgb[label % len(custom_colors_rgb)] for label in sorted_cluster_labels], dtype=np.uint8)

# Map clustered features to RGB colors based on the sorted cluster labels
color_mapping_rgb_expanded = np.array([color_mapping_rgb[label] for label in clustered_features], dtype=np.uint8)

# Assign each cluster the closest color from the custom color library
distances = euclidean_distances(cluster_centers, custom_colors_rgb)
closest_color_indices = np.argmin(distances, axis=1)
color_mapping_rgb = np.array(custom_colors_rgb)[closest_color_indices]

# Check if the number of clusters exceeds the number of available colors
if np.max(clustered_features) >= len(custom_colors_rgb):
    raise ValueError("Number of clusters exceeds the number of available colors.")

# Map clustered features to RGB colors
color_mapping_rgb = np.array([custom_colors_rgb[label] for label in clustered_features], dtype=np.uint8)

# Repeat each color for the number of samples assigned to that cluster
color_mapping_rgb_expanded = np.repeat(color_mapping_rgb, mel_spectrogram_reshaped.shape[1], axis=0)

# Prepare data for LSTM (reshape as needed for LSTM input)
X = np.reshape(clustered_features, (clustered_features.shape[0], 1, 1))

# Define hyperparameters
num_units = 50
batch_size = 32
epochs = 40

# Define the LSTM model
model = Sequential()
model.add(LSTM(num_units, input_shape=(1, 1)))
model.add(Dense(3, activation='linear'))  # Assuming RGB color prediction
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the LSTM model
model.fit(X, color_mapping_rgb_expanded, batch_size=batch_size, epochs=epochs, validation_split=0.2)

# Function to predict color based on Mel-scale features
def predict_color(features, model):
    features = np.reshape(features, (features.shape[0], 1, 1))
    predictions = model.predict(features)
    return predictions

# Predict colors for the audio features
predicted_colors_rgb = predict_color(clustered_features, model)
predicted_colors_hex = ['#%02x%02x%02x' % tuple(color.astype(int)) for color in predicted_colors_rgb]
print(predicted_colors_hex)

# Save the model to a file
model.save('my_model.keras')

