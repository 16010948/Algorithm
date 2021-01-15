fixed_cost, variable_cost, sales_cost = map(int, input().split())

if variable_cost >= sales_cost:
    print(-1)
else:
    print((fixed_cost // (sales_cost - variable_cost)) + 1)