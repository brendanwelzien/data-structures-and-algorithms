def pascal_triangle(n):
    if n == 0:
        return [1]

    else:
        row = [1]
        line_behind = pascal_triangle(n - 1)
        for r in range(len(line_behind) - 1):
            row.append(line_behind[r] + line_behind[r + 1])
        row += [1]
    return row

print(pascal_triangle(4))
