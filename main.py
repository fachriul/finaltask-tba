import token
import lexical_analysis

case_one = "p anda q or r"
case_two = "if p then ( not q s )"
case_three = "p xor ( q and not ( p and q ) )"
case_four = "( p and q ifg ( r or s )"

my_case = "( p and q ifg ( r or s )"

if __name__ == '__main__':

    print case_one.split()
    tokens = []
    for case in case_one.split():
        if case != ' ':
            # print case
            tokens.append(lexical_analysis.get_lexic_token(case))

    print tokens

    # print lexical_analysis.get_lexic_token('and')
    # TODO: fungsi tiap lexic masing masing
    # TODO: kasus huruf kurang masih error