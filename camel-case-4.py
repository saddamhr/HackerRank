import re

# def camel_case_4(s):
while True:
    try:
        s = input() 
        operation = s[0]
        method_or_class_variable = s[2]
        res = ''

        # split method or variable
        if operation == 'S' and (method_or_class_variable == 'M' or method_or_class_variable == 'V'):
            if method_or_class_variable == 'M':
                method = s[4:-2]
            if method_or_class_variable == 'V':
                method = s[4:]
            method_len = len(method)
            last_part_of_method = re.findall('[A-Z][^A-Z]*', method)[0]
            last_part_of_method_len = len(last_part_of_method)
            first_part_of_method = method[0:method_len-last_part_of_method_len]
            splitted_method = first_part_of_method + ' ' + last_part_of_method
            if method_or_class_variable == 'M':
                res = splitted_method.lower()
            if method_or_class_variable == 'V':
                res = splitted_method.lower()[:-1]

        elif operation == 'S' and method_or_class_variable == 'C':  # split class
            s_class = s[4:]
            splitted_s_class = re.findall('[A-Z][^A-Z]*', s_class)

            formatted_res = ''
            for ssc in splitted_s_class:
                formatted_res += ssc.lower() + ' '
            res = formatted_res[:-1]

        # combine method or variable
        elif operation == 'C' and (method_or_class_variable == 'M' or method_or_class_variable == 'V'):
            method = s[4:].split(' ')
            formatted_method = ''

            first_part = method[0]

            for m in method[1:]:
                formatted_method += m.title()

            if method_or_class_variable == 'M':
                res = first_part + formatted_method+'()'
            if method_or_class_variable == 'V':
                res = first_part + formatted_method[:-1]

        elif operation == 'C' and method_or_class_variable == 'C':  # combine class
            method = s[4:].split(' ')
            formatted_method = ''

            for m in method:
                formatted_method += m.title()

            res = formatted_method[:-1]

        print(res)
    except EOFError:
        break
