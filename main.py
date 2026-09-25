def generate_robust_password(platform_name):
    password = ""
    is_upper = True  # Tracks the alternating case state

    # Dictionary for the "letters up to i" rule
    number_map = {
        'b': '2', 'c': '3', 'd': '4', 
        'e': '5', 'f': '6', 'g': '7', 'h': '8'
    }

    # --- PHASE 1: BASE GENERATION ---
    for char in platform_name:
        if char == ' ':
            password += '_'
            continue

        if char.isalpha():
            # Apply alternating case
            current_char = char.upper() if is_upper else char.lower()
            is_upper = not is_upper  # Toggle state for the next letter
            
            lower_check = current_char.lower()

            # Apply symbol and specific number substitutions
            if lower_check == 'a':
                password += '@'
            elif lower_check == 'i':
                password += '!'
            elif lower_check == 'o':
                password += '0'
            elif lower_check == 's':
                password += '$'
            elif lower_check in number_map:
                password += number_map[lower_check]
            else:
                # Keep remaining letters with their alternating case
                password += current_char
        else:
            # Append existing numbers or symbols exactly as they are
            password += char

    # --- PHASE 2: COMPLIANCE LAYER ---
    
    # 1. Length Guarantee (Force minimum 12 characters)
    pad_string = "_Xy9@"
    pad_index = 0
    while len(password) < 12:
        password += pad_string[pad_index % len(pad_string)]
        pad_index += 1

    # 2. Complexity Guarantee (Check for standard password requirements)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    # Inject missing requirements predictably
    if not has_upper:
        password += 'Z'
    if not has_lower:
        password += 'm'
    if not has_digit:
        password += '9'
    if not has_symbol:
        password += '#'

    return password


# --- Testing the Generator against Edge Cases ---
platforms = [
    "google",           # Standard lowercase input
    "Bank of America",  # Spaces and mixed casing
    "X",                # Too short (Length test)
    "github",           # Normal length test
    "mmmmmmmmmmmm"   , 
    "Linkedin"   # Long, but naturally lacks numbers and symbols
]

print("Platform           -> Generated Password")
print("-" * 45)
for p in platforms:
    print(f"{p:<18} -> {generate_robust_password(p)}")
