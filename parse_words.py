import re
import typing


def parse_numbers(raw: typing.AnyStr):
    one_line = raw.replace("\n", "")
    pattern = re.compile(r'=(\d+)')

    return [int(element) for element in pattern.findall(one_line)]


def parse_words(raw: typing.AnyStr, threshold: int):
    pattern = re.compile('[A-Z[65]+')
    one_line = raw.replace("\n", "")
    result = []
    accumulated = ''

    for index, start_char in enumerate(one_line):
        start_match = pattern.match(start_char)

        if start_match is None:
            accumulated = ''

            continue

        if start_char == '[':
            accumulated += 'C'
        elif start_char == '5':
            accumulated += 'S'
        elif start_char == '6':
            accumulated += 'G'
        else:
            accumulated += start_char

        for cont_char in one_line[index + 1:len(one_line)]:
            cont_match = pattern.match(cont_char)

            if cont_match is None:
                accumulated = ''

                break

            if cont_char == '[':
                accumulated += 'C'
            elif cont_char == '5':
                accumulated += 'S'
            elif cont_char == '6':
                accumulated += 'G'
            else:
                accumulated += cont_char

            if len(accumulated) == threshold:
                result.append(accumulated)

                accumulated = ''

                break

    return result
