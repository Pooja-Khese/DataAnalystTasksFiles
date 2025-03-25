# Dictionary Compression Program

# Original data
data = [
    "apple", "banana", "apple", "orange", "banana", 
    "apple", "orange", "orange", "banana", "apple"
]

# Step 1: Create a dictionary mapping each unique word to a unique number
compression_dict = {word: idx for idx, word in enumerate(set(data))}

# Step 2: Compress the data using the dictionary
compressed_data = [compression_dict[word] for word in data]

# Step 3: Decompress the data back to original form using reverse mapping
decompression_dict = {idx: word for word, idx in compression_dict.items()}
decompressed_data = [decompression_dict[idx] for idx in compressed_data]

# Output
print("Original Data: ", data)
print("Compression Dictionary: ", compression_dict)
print("Compressed Data: ", compressed_data)
print("Decompressed Data: ", decompressed_data)

# Verify if decompression matches the original data
assert data == decompressed_data, "Decompressed data doesn't match the original!"
print("Compression and Decompression Successful!")
