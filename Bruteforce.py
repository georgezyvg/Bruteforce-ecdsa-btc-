# Import the necessary libraries


# Define the public key as a point (x, y)
public_key = (583172140663506365468311725350684620856667941011815418814442280429179668350561770026510604113021686089777374557608174938587526483912023179154647723408296)

# Define the values of generator_x, generator_y, and p
generator_x = 55066263022277343669578718895168534326250603453777594175500187360389116729240
generator_y = 32670510020758816978083085130507043184471273380659243275938904335757337482424
p = 115792089237316195423570985008687907852837564279074904382605163141518161494336

def find_public_key_x_public_key_y_and_private_key(public_key, generator_x, generator_y, p):
  # Initialize the result point (result_x, result_y) to the point at infinity (0, 0)
  result_x, result_y = 0, 0

  # Initialize the scalar value private_key to 0
  private_key_min = 1
  private_key = private_key_min

  counter = 0

  # Perform scalar multiplication using the binary representation of T
  while (result_x, result_y) != public_key:
    # Double the result point (result_x, result_y)
    result_x, result_y = (result_x * 2) % p, (result_y * 2) % p

    # Increment the scalar value private_key
    private_key += 1

    
    # Increment the counter
    counter += 1

    print("Counter:", counter)
    

    # If the result point equals public_key, return the values of x, y, and private_key
    if (result_x, result_y) == public_key:
      return result_x, result_y, private_key

    # Add the generator point (generator_x, generator_y) to the result point (result_x, result_y)
    result_x, result_y = (result_x + generator_x) % p, (result_y + generator_y) % p

# Find x, y, and private_key using the public key
public_key_x, public_key_y, private_key = find_public_key_x_public_key_y_and_private_key(public_key, generator_x, generator_y, p)

# Print the values of x, y, and private_key
print("x:", public_key_x)
print("y:", public_key_y)
print("T:", private_key)



