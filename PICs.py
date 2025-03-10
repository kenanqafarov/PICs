import requests


def getPI(n):
    url = "https://dummyjson.com/c/85f3-0084-4a9a-b851"
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP error-ları avtomatik aşkar edir
        pi_str = response.json()["pi"]  
        pi_digits = [int(d) for d in pi_str.replace('.', '')[:n]]
        return pi_digits

    except requests.exceptions.RequestException as e:
        raise Exception(f"We got a problem!\nError: {e}")


def take(text):
    pi_digits = getPI(len(text))  
    encrypted_chars = []
    for i, char in enumerate(text):
        shift = pi_digits[i]  
        if i % 2 == 0:  
            new_char = chr(ord(char) + shift)
        else:  
            new_char = chr(ord(char) - shift)
        encrypted_chars.append(new_char)

    encrypted_chars.reverse()  
    return ''.join(encrypted_chars)

def shoot(encrypted_text):
    
    decrypted_chars = list(encrypted_text)
    decrypted_chars.reverse()  
    pi_digits = getPI(len(decrypted_chars))  
    
    original_chars = []
    for i, char in enumerate(decrypted_chars):
        shift = pi_digits[i]
        if i % 2 == 0:  
            new_char = chr(ord(char) - shift)
        else:  
            new_char = chr(ord(char) + shift)
        original_chars.append(new_char)

    return ''.join(original_chars)


