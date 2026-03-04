import re

def normalitzar_espais(text: str) -> str:
    # Convertir múltiples espais en un i retallar
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def normalitzar_nom(nom: str) -> str:
    # Espais + format títol, respectant guions
    nom = normalitzar_espais(nom)
    nom = nom.title()
    return nom


def email_valid(email: str) -> bool:
    # Regex bàsica per validar email
    return re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email) is not None


def normalitzar_email(email: str) -> str:
    # strip + lower
    email = normalitzar_espais(email)
    email = email.lower()
    return email


def normalitzar_telefon(tel: str) -> str | None:
    # 1) quedar-se només amb dígits
    tel = normalitzar_espais(tel)
    digits = re.sub(r"\D", "", tel)

    # 2) gestionar prefixos
    if digits.startswith("0034"):
        digits = digits[4:]
    elif digits.startswith("34"):
        digits = digits[2:]

    # 3) validar 9 dígits
    if len(digits) == 9:
        return "+34" + digits
    else:
        return None


def cp_valid(cp: str) -> bool:
    # Exactament 5 dígits
    return re.fullmatch(r"^\d{5}$", cp) is not None


def netejar_comentari(com: str) -> str:
    # Espais + reduir !!! i ???
    com = normalitzar_espais(com)
    com = re.sub(r"!{2,}", "!", com)
    com = re.sub(r"\?{2,}", "?", com)
    return com


def processar_linia(linia: str) -> dict:
    parts = linia.split(";")

    nom = normalitzar_nom(parts[0])
    email = normalitzar_email(parts[1])
    telefon = normalitzar_telefon(parts[2])
    cp = normalitzar_espais(parts[3])
    comentari = netejar_comentari(parts[4])

    return {
        "nom": nom,
        "email": email,
        "telefon": telefon,
        "cp": cp,
        "comentari": comentari
    }


def validar_registre(reg: dict) -> list[str]:
    errors = []

    if not email_valid(reg["email"]):
        errors.append("email")

    if reg["telefon"] is None:
        reg["telefon"] = "Telèfon invàlid"
        errors.append("telefon")

    if not cp_valid(reg["cp"]):
        errors.append("cp")

    return errors


linies = [
    "  Ana-josé   López   ; ANA.LOPEZ@gmail.com  ; +34  612-34-56-78 ; 08001 ;  Hola!! Vull info  ",
    "pepe perez; pepe_perezcorreu.es; 612345678;28013;   m'encanta Python!!!   ",
    "MARÍA-josé ; maria.jose@correu ; 0034 611 22 33 44 ;  41001 ; Bones, truca'm.",
    "Juan; juan@gmail.com ; 123 ; 99999 ; ???"
]

ok_count = 0
error_count = 0

for i, linia in enumerate(linies, start=1):
    reg = processar_linia(linia)
    errors = validar_registre(reg)

    if not errors:
        print(f"Registre {i}: OK")
        ok_count += 1
    else:
        print(f"Registre {i}: ERRORS -> {', '.join(errors)}")
        error_count += 1

    print(
        "Nom: " + reg["nom"] + "\n" +
        "Email: " + reg["email"] + "\n" +
        "Telèfon: " + reg["telefon"] + "\n" +
        "CP: " + reg["cp"] + "\n" +
        "Comentari: " + reg["comentari"]
    )
    print("---")

print("Resum final:")
print("OK:", ok_count)
print("Amb errors:", error_count)