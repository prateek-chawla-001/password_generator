Write a Python function that takes a string (a platform name) and converts it into a password based strictly on the following sequential rules.

Space Handling: Replace every space character with an underscore (_).

Alternating Case: For every alphabetical character encountered, alternate its casing before applying any further replacements. The first letter encountered must be UPPERCASE, the second lowercase, the third UPPERCASE, and so on. Non-alphabetical characters do not disrupt this alternating sequence.

Symbol Substitution: After determining the case, if the letter is 'A' (or 'a'), replace it with @. If 'I' (or 'i'), replace with !. If 'O' (or 'o'), replace with 0 (zero). If 'S' (or 's'), replace with $.

Number Substitution (Letters up to 'i'): For the remaining letters in the alphabet up to 'i' (which are B, C, D, E, F, G, H), replace them with their corresponding alphabetical number position: B=2, C=3, D=4, E=5, F=6, G=7, H=8.

Retention: Any letter that does not fall into the above substitution rules (from J to Z, excluding O and S) remains as a letter, retaining the uppercase or lowercase state assigned to it in Step 2.
