The Upgraded Password Generator Rule Book (Master Prompt)
​Save this prompt. It will instruct any AI to perfectly recreate your logic, including the compliance checks.
​System Prompt: Robust Intelligent Password Generator
​Write a Python function that takes a string (a platform name) and converts it into a highly secure password based strictly on the following sequential rules.
​Phase 1: Base Generation
​Space Handling: Replace every space character with an underscore (_).
​Alternating Case: For every alphabetical character encountered, alternate its casing before applying any replacements. The first letter must be UPPERCASE, the second lowercase, the third UPPERCASE, and so on. Non-alphabetical characters do not disrupt this sequence.
​Symbol Substitution: If the letter is 'A' (or 'a'), replace it with @. If 'I' (or 'i'), replace with !. If 'O' (or 'o'), replace with 0 (zero). If 'S' (or 's'), replace with $.
​Number Substitution (Letters up to 'i'): For the remaining letters in the alphabet up to 'i' (B, C, D, E, F, G, H), replace them with their corresponding alphabetical number position: B=2, C=3, D=4, E=5, F=6, G=7, H=8.
​Retention: Any letter that does not fall into the above substitution rules remains a letter, retaining the alternating uppercase/lowercase state assigned in Step 2.
​Phase 2: The Compliance Layer
6.  Length Guarantee: Check the length of the generated base password. If it is less than 12 characters, pad the end of the password by repeating the string _Xy9@ character by character until the password reaches exactly 12 characters.
7.  Complexity Guarantee: Scan the entire password.
* If it lacks an Uppercase letter, append Z.
* If it lacks a Lowercase letter, append m.
* If it lacks a Number, append 9.
* If it lacks a Special Symbol (non-alphanumeric), append #.
