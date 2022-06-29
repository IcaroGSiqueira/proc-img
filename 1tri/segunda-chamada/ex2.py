G =[[7.5, 8.0, 9.0],
    [6.7, 7.7, 5.4],
    [8.0, 9.2, 7.4],
    [6.6, 6.6, 6.6],
    [5.0, 8.0, 7.0]]

def average_a(m):
    g0 = float("{:.2f}".format((m[0][0] + m[0][1] + m[0][2])/3))
    g1 = float("{:.2f}".format((m[1][0] + m[1][1] + m[1][2])/3))
    g2 = float("{:.2f}".format((m[2][0] + m[2][1] + m[2][2])/3))
    g3 = float("{:.2f}".format((m[3][0] + m[3][1] + m[3][2])/3))
    g4 = float("{:.2f}".format((m[4][0] + m[4][1] + m[4][2])/3))
    return ({
        "aluno 1": g0,
        "aluno 2": g1,
        "aluno 3": g2,
        "aluno 4": g3,
        "aluno 5": g4,
        })

def average_b(m):
    g0 = float("{:.2f}".format((m[0][0] + m[0][1] + m[0][2]*2)/4))
    g1 = float("{:.2f}".format((m[1][0] + m[1][1] + m[1][2]*2)/4))
    g2 = float("{:.2f}".format((m[2][0] + m[2][1] + m[2][2]*2)/4))
    g3 = float("{:.2f}".format((m[3][0] + m[3][1] + m[3][2]*2)/4))
    g4 = float("{:.2f}".format((m[4][0] + m[4][1] + m[4][2]*2)/4))
    return ({
        "aluno 1": g0,
        "aluno 2": g1,
        "aluno 3": g2,
        "aluno 4": g3,
        "aluno 5": g4,
        })

def average_c(m):
    p0 = float("{:.2f}".format((m[0][0] + m[1][0] + m[2][0] + m[3][0] + m[4][0])/5))
    p1 = float("{:.2f}".format((m[0][1] + m[1][1] + m[2][1] + m[3][1] + m[4][1])/5))
    p2 = float("{:.2f}".format((m[0][2] + m[1][2] + m[2][2] + m[3][2] + m[4][2])/5))
    return ({
        "prova 1": p0,
        "prova 2": p1,
        "prova 3": p2,
        })

print("Médias A:\t", average_a(G))

print("Médias B:\t", average_b(G))

print("Médias C:\t", average_c(G))