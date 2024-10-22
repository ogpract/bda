def create_dgim_buckets(data, window_size):
    result = []
    power = 0

    # Keep only the last 'window_size' bits
    data = data[-window_size:]

    while data:
        # Remove trailing zeros
        while data and data[-1] == "0":
            data = data[:-1]

        if not data:
            break

        count = 0
        string = ""
        i = len(data) - 1

        while i >= 0 and count < 2 ** power:
            if data[i] == "1":
                count += 1
                string = data[i] + string  # Add bit to the string (to keep correct order)
            else:
                string = data[i] + string
            
            i -= 1

        if count >= 2 ** power:
            result.append((string, 2 ** power))  # Append (bit string, bucket size)
            power += 1
        else:
            result.append((string, 2 ** power))
            break

    print("Buckets:")
    for bucket in result:
        print(f"({bucket[0]}, Size: {bucket[1]})")

    print("\nVisual Representation:")
    if result:
        for bucket in result:
            print(f"({bucket[0]})", end=" ")

        print()

        for bucket in result:
            size = 2 ** (int(bucket[1]).bit_length() - 1)
            print(f"Size: {size} ({len(bucket[0])})", end=" ")

        print()
    else:
        print("No buckets created.")

    return result


data = input("Enter the binary data string: ")
window_size = int(input("Enter the window size: "))

if not all(c in '01' for c in data) or window_size <= 0:
    print("Invalid input. Please ensure the data string contains only binary digits and the window size is a positive integer.")
else:
    buckets = create_dgim_buckets(data, window_size)
