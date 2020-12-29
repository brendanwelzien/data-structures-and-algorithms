def multi_bracket_validation(string):
  stack = []
  for char in string:
    if char in ['(', '[', '{']:
      stack.append(char)
    elif char in [')', ']', '}']:
      if stack == []:
        return False
      elif char == ')' and '(' in stack:
        stack.remove('(')
      elif char == ']' and '[' in stack:
        stack.remove('[')
      elif char == '}' and '{' in stack:
        stack.remove('{')
      elif char == ')' and '(' not in stack:
        return False
      elif char == ']' and '[' not in stack:
        return False
      elif char == '}' and '{' not in stack:
        return False
  if stack == []:
    return True
  else:
    return False

print(multi_bracket_validation('(){[]}'))
print(multi_bracket_validation('(([]]}'))
print(multi_bracket_validation('{{{[[]]}}}()'))
print(multi_bracket_validation('[]()'))
