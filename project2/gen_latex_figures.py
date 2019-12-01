
print("\n\n\n")
ls = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
for i in range(0, len(ls), 2):
    print (f"""\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.495\\linewidth]{{figures/{str(ls[i])}.png}}
    \\includegraphics[width=0.495\\linewidth]{{figures/{str(ls[i+1])}.png}}
\\end{{figure}}""")
    print()
