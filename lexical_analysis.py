import token


def get_lexic_token(chars):

    # len() return total length list/array
    # check berapa total lexic
    total_lexic = len(token.lexic)

    # check satu satu lexic yang tersedia
    idx_lexic = 0

    # variable temp untuk cek apakah input lexic atau bukan
    check = False

    # loop mengecek semua lexic

    while idx_lexic <= total_lexic:

        idx_char = 0

        #chars = 'xor', char = [x,o,r]
        for char in chars:

            # Exception buat check invalid string
            try:

                # check per character
                if char == token.lexic[idx_lexic][idx_char]:
                    check = True
                else:
                    check = False

            except IndexError:
                check = False

            idx_char += 1

        if check:
            return token.lexic_token[chars]

        idx_lexic += 1

    return False
