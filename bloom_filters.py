import pyhash
#Bloom filters is a probablistic data structure which may give a false positive but never gives the fals  negative

bit_vector = [0] * 20

# Non cryptographic hash functions (FNV, Murmur)

fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

#calculate the output of FNV and Murmur hash functions for Pikachu and Charmander
fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1
bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1

# A wild Bulbasaur appears!

fnv_bulb = fnv("Bulbasaur") % 20
murmur_bulb = murmur("Bulbasaur") % 20

print(bit_vector[fnv_bulb])
print(bit_vector[murmur_bulb])