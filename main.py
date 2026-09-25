def generate_platform_password(platform_name):
    password = ""
    is_upper = True  # Tracks the alternating case state

    # Dictionary for the "letters up to i" rule
    number_map = {
        'b': '2', 'c': '3', 'd': '4', 
        'e': '5', 'f': '6', 'g': '7', 'h': '8'
    }

    for char in platform_name:
        if char == ' ':
            password += '_'
            continue

        if char.isalpha():
            # 1. Apply alternating case
            current_char = char.upper() if is_upper else char.lower()
            is_upper = not is_upper  # Toggle state for the next letter
            
            lower_check = current_char.lower()

            # 2. Apply symbol substitutions
            if lower_check == 'a':
                password += '@'
            elif lower_check == 'i':
                password += '!'
            elif lower_check == 'o':
                password += '0'
            elif lower_check == 's':
                password += '$'
            
            # 3. Apply number substitutions for letters B through H
            elif lower_check in number_map:
                password += number_map[lower_check]
            
            # 4. Keep remaining letters with their alternating case applied
            else:
                password += current_char
        else:
            # Append numbers or existing symbols as they are
            password += char

    return password

# --- Testing the Generator ---
platforms = ["google", "Bank of America", "instagram", "Netflix"]

for p in platforms:
    print(f"{p:<18} -> {generate_platform_password(p)}")
