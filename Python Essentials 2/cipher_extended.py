def caesar_cipher():
    text = input("Enter text: ")

    while True:
        try:
            value = int(input("Enter shift value (1-25): "))
            if 1 <= value <= 25:
                break
        except ValueError:
            print("Please enter an integer.")

    msg = ''
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            code = (ord(ch) - base + value) % 26 + base
            
            msg += chr(code)
        else:
            msg += ch
    print(msg)

caesar_cipher()
    
