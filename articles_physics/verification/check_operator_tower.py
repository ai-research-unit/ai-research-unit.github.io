"""
Checks for "Operators on B: End_C and End_B, the Two Unitary Towers".

Everything here is a statement about the algebra and is independent of the
primordial action.  Each check prints a residual; a residual at the noise
floor is the evidence, and an O(1) residual is a failure.  See AGENTS.md:
any check that asserts invariance or covariance must assert the
transformation law itself, not only the object.

Run:  python3 check_operator_tower.py
"""
import numpy as np

np.set_printoptions(precision=3, suppress=True)
I2 = np.eye(2, dtype=complex)
S = [np.array([[0, 1], [1, 0]], complex),
     np.array([[0, -1j], [1j, 0]], complex),
     np.array([[1, 0], [0, -1]], complex)]


def herm(n=4, seed=None):
    rng = np.random.default_rng(seed)
    M = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (M + M.conj().T) / 2


def herm_basis(n=4):
    """Real basis of Herm(n) with unit trace-norm, diagonals first."""
    B = []
    for i in range(n):
        E = np.zeros((n, n), complex); E[i, i] = 1; B.append(E)
        for j in range(i + 1, n):
            E = np.zeros((n, n), complex); E[i, j] = E[j, i] = 1; B.append(E)
            E = np.zeros((n, n), complex); E[i, j] = 1j; E[j, i] = -1j; B.append(E)
    return B


def su4_basis():
    B = []
    for i in range(4):
        for j in range(i + 1, 4):
            E = np.zeros((4, 4), complex); E[i, j] = 1; B.append(E - E.T)
            E = np.zeros((4, 4), complex); E[i, j] = E[j, i] = 1; B.append(1j * E)
    for i in range(3):
        D = np.zeros((4, 4), complex); D[i, i] = 1; D[i + 1, i + 1] = -1
        B.append(1j * D)
    return B


def real_mat(Fr, basis):
    """Matrix of X -> i[Fr,X] on Herm(4) in the given real basis."""
    ip = lambda X, Y: np.trace(X.conj().T @ Y).real
    M = np.zeros((len(basis), len(basis)))
    for c, Y in enumerate(basis):
        Z = 1j * (Fr @ Y - Y @ Fr)
        M[:, c] = [ip(B, Z) / ip(B, B) for B in basis]
    return M


def rank(A, tol=1e-8):
    return np.linalg.matrix_rank(A, tol=tol)


Hb = herm_basis(4)
print("0  Herm(4) real dimension = %d (expect 16)\n" % len(Hb))

# --- 1. the commutant of the left B-action is 1 (x) M2 --------------------
# rho(M) = M (x) 1 on C^4 = C^2 (x) C^2.  Solve [X, rho(M)] = 0 for X.
rows = []
for M in [I2] + S:
    L = np.kron(M, I2)
    for a in range(4):
        for b in range(4):
            row = np.zeros((4, 4), complex)
            for c in range(4):
                row[a, c] += L[c, b]
                row[c, b] -= L[a, c]
            rows.append(row.reshape(-1))
u, s, vh = np.linalg.svd(np.array(rows))
N = vh[s < 1e-9].conj().T
print("1  commutant of the left B-action: complex dim = %d (expect 4 = 1 (x) M2)"
      % N.shape[1])
resid = 0.0
for M in [I2] + S:
    b = np.kron(I2, M).reshape(-1)
    resid = max(resid, np.abs(N @ (N.conj().T @ b) - b).max())
print("   1 (x) M2 lies inside it: residual %.2e" % resid)
print("   => the unitaries of the commutant are 1 (x) U(2), real dim 4:")
print("      the electroweak group, not a hand-picked SU(2)\n")

# --- 2. Herm(4) = (1,1) + (3,1) + (1,3) + (3,3) under su(2)_L + su(2)_R --
blocks = {
    "1":        [np.eye(4, dtype=complex) / 2],
    "su(2)_L":  [np.kron(s, I2) / 2 for s in S],
    "su(2)_R":  [np.kron(I2, s) / 2 for s in S],
    "(3,3)":    [np.kron(s, t) / 2 for s in S for t in S],
}
flat = sum(blocks.values(), [])
print("2  Herm(4) under su(2)_L (+) su(2)_R")
for k, v in blocks.items():
    print("   %-8s dim %2d" % (k, len(v)))
G = np.array([[np.trace(A.conj().T @ B).real for B in flat] for A in flat])
print("   total %d (expect 16); cross-terms %.2e; rank %d"
      % (len(flat), np.abs(G - np.diag(np.diag(G))).max(), rank(G, 1e-10)))
print("   => Xi contains two su(2) adjoints as blocks; the weak index is in the")
print("      multiplet, not manufactured by the breaking\n")

# --- 3. vacuum patterns and their stabilisers in su(4) -------------------
Bs = su4_basis()
print("3  su(4) basis size %d (expect 15)" % len(Bs))


def stab_dim(P):
    cols = []
    for X in Bs:
        C = P @ X - X @ P
        cols.append(np.concatenate([C.real.reshape(-1), C.imag.reshape(-1)]))
    return 15 - rank(np.array(cols).T)


pats = [("diag(v,v,v,-3v)   3+1", np.diag([1., 1, 1, -3])),
        ("diag(a,a,b,b)     2+2", np.diag([1., 1, -1, -1])),
        ("diag(a,a,b,c)   2+1+1", np.diag([1., 1, 2, 3])),
        ("diag(a,b,c,d)  generic", np.diag([1., 2, 3, 4]))]
for name, P in pats:
    d = stab_dim(P)
    print("   %-24s dim Stab = %2d   broken = %2d" % (name, d, 15 - d))
print("   => SU(3)_c x U(1) needs 3+1 (9); SU(2) x SU(2) x U(1) needs 2+2 (7)\n")

# --- 4. ad_F: image 15, kernel the centre, force Hermitian ---------------
F = herm(seed=3)
M = real_mat(F, Hb)
X = herm(seed=4)
C = F @ X - X @ F
print("4  [F,X] anti-Hermitian, i[F,X] Hermitian:")
print("   ||[F,X]+[F,X]^dag|| = %.2e   ||i[F,X]-(i[F,X])^dag|| = %.2e"
      % (np.abs(C + C.conj().T).max(), np.abs(1j * C - (1j * C).conj().T).max()))
print("   => the force term -i g4 [F,Xi] is Hermitian")
A = np.array([real_mat(1j * Xg, Hb).reshape(-1) for Xg in Bs]).T
print("   dim of {i ad_F : F in su(4)} on Herm(4) = %d (expect 15)" % rank(A))
print("   central F acts as zero: ||M_c|| = %.2e\n"
      % np.abs(real_mat(1.7 * np.eye(4), Hb)).max())

# --- 5. the spectral face: -i g [F,Xi]_kl = -i g (f_k - f_l) Xi_kl -------
rng = np.random.default_rng(9)
D = np.diag(rng.normal(size=4))            # diagonal, so f_k are the entries
Y = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
lhs = D @ Y - Y @ D
rhs = np.array([[(D[k, k] - D[l, l]) * Y[k, l] for l in range(4)] for k in range(4)])
print("5  spectral face: ||[D,Y] - (f_k-f_l)Y_kl|| = %.2e" % np.abs(lhs - rhs).max())
q = np.array([1.0, 2.0, 3.0, -6.0])
print("   density splitting q_kl / field splitting f_k-f_l are DIFFERENT objects")
print("   q = %s  vs  f = %s\n" % (q, np.diag(D)))

# --- 6. B-linearity forbids the 3+1 vacuum ------------------------------
# P must commute with 1 (x) U(2) for that group to survive unbroken.
def commutes_with_Blinear(P, tol=1e-9):
    """max over a spanning set of 1 (x) u(2) of ||[P, 1 (x) A]||, normalised."""
    worst = 0.0
    for A in [1j * I2] + [1j * s for s in S]:
        L = np.kron(I2, A)
        worst = max(worst, np.abs(P @ L - L @ P).max() / max(1.0, np.abs(P).max()))
    return worst


print("6  does P commute with the B-linear u(2)?  (0 = it survives unbroken)")
for name, P in [("diag(a,a,b,b) 2+2", np.diag([1., 1, -1, -1])),
                ("diag(v,v,v,-3v) 3+1", np.diag([1., 1, 1, -3])),
                ("diag(a,a,b,c) 2+1+1", np.diag([1., 1, 2, 3]))]:
    print("   %-22s  ||[P, 1(x)u(2)]|| = %.2e" % (name, commutes_with_Blinear(P)))
print("   => only the 2+2 vacuum preserves the full B-linear U(2); on 3+1 its")
print("      SU(2) part is broken (only the diagonal U(1) survives).")
print("      The colour stabiliser and the B-linear U(2) cannot both survive.\n")

# --- 7. pairing vs commutator: the output dimensions ---------------------
print("7  tr(F Xi) is a SCALAR (dim 1); [F, Xi] is a MATRIX (dim 16)")
print("   => a pairing cannot produce the object the balance needs;\n"
      "      the commutator is the only canonical bilinear Mat x Mat -> Mat.")
