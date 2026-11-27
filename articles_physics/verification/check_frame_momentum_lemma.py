"""Checks for 'The Primordial Force Law'.

Identity A:  U^dag (D_i Xi) U = d_i P + [Om_i, P],  Om_i = U^dag(d_i - i g A_i)U
Identity B:  d_j M_i = U^dag (D_j D_i Xi) U - [Om_j, M_i],  M_i := U^dag (D_i Xi) U
Identity C:  the (k,l) entry of the commutator is pair-supported when Om is.

Finite differences: centred, step 1e-4 for both nested levels.  A smaller inner
step makes the nested noise O(inner/outer) and swamps the check -- the residuals
below are 1e-7 or better on O(1) data.
"""
import numpy as np

rng = np.random.default_rng(7)
n = 4
g = 0.7
h = 1e-4

herm = lambda M: (M + M.conj().T) / 2
ah = lambda M: (M - M.conj().T) / 2


def mexp(M):
    w, V = np.linalg.eig(M)
    return (V * np.exp(w)) @ np.linalg.inv(V)


P0 = np.diag(rng.normal(size=n)).astype(complex)
P1 = np.diag(rng.normal(size=n)).astype(complex)
A0 = herm(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
A1 = herm(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
K = ah(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))

U = lambda t: mexp(t * K)
P = lambda t: P0 + t * P1
A = lambda t: A0 + t * A1
Xi = lambda t: U(t) @ P(t) @ U(t).conj().T
d = lambda f, t: (f(t + h) - f(t - h)) / (2 * h)
DtXi = lambda t: d(Xi, t) - 1j * g * (A(t) @ Xi(t) - Xi(t) @ A(t))
Om = lambda t: U(t).conj().T @ (d(U, t) - 1j * g * A(t) @ U(t))
M = lambda t: U(t).conj().T @ DtXi(t) @ U(t)
DD = lambda t: d(DtXi, t) - 1j * g * (A(t) @ DtXi(t) - DtXi(t) @ A(t))

t = 0.0
u, Om0, M0, Pt = U(t), Om(t), M(t), P(t)

print("A  ||M - (dP + [Om,P])||            = %.2e" % np.abs(M0 - (P1 + (Om0 @ Pt - Pt @ Om0))).max())
rhs = u.conj().T @ DD(t) @ u - (Om0 @ M0 - M0 @ Om0)
print("B  ||dM - (U^dag DDXi U - [Om,M])|| = %.2e   (scale %.2e)" % (np.abs(d(M, t) - rhs).max(), np.abs(d(M, t)).max()))

off = np.array([[Om0[k, l] * (Pt[l, l] - Pt[k, k]) for l in range(n)] for k in range(n)])
print("C  ||M - (diag dP + Om_kl(rho_l-rho_k))|| = %.2e" % np.abs(M0 - (np.diag(np.diag(M0)) + off)).max())

# --- pair support: the field is built from a frame that mixes only species (0,1)
pair = np.zeros((n, n), complex)
pair[0, 1], pair[1, 0] = 1.0, -1.0
Kp = 0.3 * (pair - pair.conj().T) + 0.2j * np.diag([1.0, -1.0, 0.0, 0.0])
Ap = np.zeros((n, n), complex)
Ap[0, 1] = Ap[1, 0] = 0.9                      # connection off-diagonal only on the pair


def sector_run(Kg, Ag):
    Ug = lambda s: mexp(s * Kg)
    Xg = lambda s: Ug(s) @ P(s) @ Ug(s).conj().T
    DtX = lambda s: d(Xg, s) - 1j * g * (Ag @ Xg(s) - Xg(s) @ Ag)
    Og = Ug(t).conj().T @ (d(Ug, t) - 1j * g * Ag @ Ug(t))
    Mg = Ug(t).conj().T @ DtX(t) @ Ug(t)
    return Og, Mg, Og @ Mg - Mg @ Og


def pair_part(Omx, Mx):
    out = np.zeros_like(Omx)
    for k in (0, 1):
        for l in (0, 1):
            if k != l:
                out[k, l] = (Omx[k, 0] * Mx[0, l] + Omx[k, 1] * Mx[1, l]
                             - Mx[k, 0] * Omx[0, l] - Mx[k, 1] * Omx[1, l])
    return out


Op, Mp, comp = sector_run(Kp, Ap)
PL = [(0, 1), (1, 0)]          # the pair entries only: the commutator's diagonal
                               # carries diagonal x diagonal pieces and is not the claim
print("D  pair frame:  ||[Om,M]_kl - (m in {k,l} only)|| = %.2e"
      % max(abs((comp - pair_part(Op, Mp))[k, l]) for k, l in PL))

K3 = Kp.copy()
K3[0, 2], K3[2, 0] = 0.4, -0.4
K3[1, 3], K3[3, 1] = 0.4, -0.4
A3 = Ap.copy()
A3[0, 2] = A3[2, 0] = 0.7
O3, M3, com3 = sector_run(K3, A3)
print("E  three species: ||[Om,M]_kl - (m in {k,l} only)|| = %.2e   (pair entries %.2e)"
      % (max(abs((com3 - pair_part(O3, M3))[k, l]) for k, l in PL),
         max(abs(com3[k, l]) for k, l in PL)))

# --- the differentiated guidance equation, entry (k,l), k != l.
# Omega is written analytically here: U = exp(t K) gives Gamma = K exactly, so
# Omega(t) = K - i g exp(-t K) A(t) exp(t K) and d_t Pi can be differenced cleanly.
k, l = 0, 1
OmA = lambda s: K - 1j * g * mexp(-s * K) @ A(s) @ mexp(s * K)
qs = lambda s, a, b: P(s)[a, a] - P(s)[b, b]
PiA = lambda s: np.array([[qs(s, kk, ll) * OmA(s)[kk, ll] for ll in range(n)] for kk in range(n)])

DDX = u.conj().T @ DD(t) @ u
dPi = (PiA(t + h) - PiA(t - h)) / (2 * h)
dq = np.array([(P(t + h)[m, m] - P(t - h)[m, m]) / (2 * h) for m in range(n)])
O, Pa = OmA(t), PiA(t)

pair_term = Pa[k, l] * (O[k, k] - O[l, l])          # m in {k,l} part of [Om,Pi]
conv = O[k, l] * (dq[k] - dq[l])                    # = [Om,D]_kl, D = diag(d_i rho)
three = sum(O[k, m] * Pa[m, l] - Pa[k, m] * O[m, l] for m in range(n) if m not in (k, l))
rhs = -DDX[k, l] - pair_term - conv - three
print("F  ||dPi_kl - (-[U D_j D_i Xi U]_kl - [Om,Pi]_kl - Om_kl d_i q_kl)|| = %.2e   (scale %.2e)"
      % (abs(dPi[k, l] - rhs), abs(dPi[k, l])))

# --- gauge invariance of the composite connection: U -> VU, A -> VAV^dag - (i/g) dV V^dag
def Vg(s):
    m = np.eye(4, dtype=complex)
    c, n = np.cos(0.4 * s), np.sin(0.4 * s)
    m[0, 0], m[0, 1], m[1, 0], m[1, 1] = c, n, -n, c
    m[2, 2] = np.exp(0.3j * s)
    m[3, 3] = np.exp(-0.2j * s)
    return m

Aq = lambda s: Vg(s) @ A(s) @ Vg(s).conj().T - (1j / g) * d(Vg, s) @ Vg(s).conj().T
Uq = lambda s: Vg(s) @ mexp(s * K)
Oq = Uq(t).conj().T @ (d(Uq, t) - 1j * g * Aq(t) @ Uq(t))
Oref = mexp(t * K).conj().T @ (d(lambda s: mexp(s * K), t) - 1j * g * A(t) @ mexp(t * K))
print("G  gauge invariance of Omega = U^dag D U: ||Omega' - Omega|| = %.2e   (scale %.2e)"
      % (np.abs(Oq - Oref).max(), np.abs(Oref).max()))

# --- H: the spectral face. In the eigenbasis of F, [F,X]_kl = (f_k-f_l) X_kl,
# so the force weight is the FIELD-STRENGTH splitting, not the density splitting.
rngH = np.random.default_rng(21)
fH = np.diag(rngH.normal(size=4))                 # diagonal F: entries are f_k
XH = rngH.normal(size=(4, 4)) + 1j * rngH.normal(size=(4, 4))
comH = fH @ XH - XH @ fH
specH = np.array([[(fH[k, k] - fH[l, l]) * XH[k, l] for l in range(4)] for k in range(4)])
print("H  spectral face: ||[F,X] - (f_k-f_l)X_kl|| = %.2e" % np.abs(comH - specH).max())

# --- I: the field strength built from the connection is Hermitian, the
#        antisymmetric second derivative is -ig[F,Xi] (adjoint action), and
#        in F's eigenbasis the commutator is the real eigenvalue splitting.
# Two directions (s,u); A_j Hermitian; D_j X = d_j X - i g [A_j, X].
rngI = np.random.default_rng(31)
rh = lambda: (lambda M: (M + M.conj().T) / 2)(rngI.normal(size=(4, 4)) + 1j * rngI.normal(size=(4, 4)))
A0c, A1c = rh(), rh()
B0, B1, C0, C1 = rh(), rh(), rh(), rh()
A0f = lambda s, u: A0c + s * B0 + u * C0
A1f = lambda s, u: A1c + s * B1 + u * C1
X0, Xs, Xu, Xsu = rh(), rh(), rh(), rh()
Xif = lambda s, u: X0 + s * Xs + u * Xu + s * u * Xsu
dsf = lambda fn, s, u: (fn(s + h, u) - fn(s - h, u)) / (2 * h)
duf = lambda fn, s, u: (fn(s, u + h) - fn(s, u - h)) / (2 * h)
s0 = u0 = 0.0

Fsu = (dsf(A1f, s0, u0) - duf(A0f, s0, u0)
       - 1j * g * (A0f(s0, u0) @ A1f(s0, u0) - A1f(s0, u0) @ A0f(s0, u0)))
print("I1 field strength Hermitian: ||F - F^dag|| = %.2e" % np.abs(Fsu - Fsu.conj().T).max())


def Dj(fn, j, s, u):
    Aj, dfn = (A0f, dsf) if j == 0 else (A1f, duf)
    X = fn(s, u)
    return dfn(fn, s, u) - 1j * g * (Aj(s, u) @ X - X @ Aj(s, u))


Dsu = Dj(lambda s, u: Dj(Xif, 1, s, u), 0, s0, u0)
Dus = Dj(lambda s, u: Dj(Xif, 0, s, u), 1, s0, u0)
comm = Dsu - Dus
Xv = Xif(s0, u0)
pred = -1j * g * (Fsu @ Xv - Xv @ Fsu)
print("I2 ||[D_s,D_u]Xi - (-ig[F,Xi])|| = %.2e   (scale %.2e)"
      % (np.abs(comm - pred).max(), np.abs(comm).max()))

fv, Vv = np.linalg.eigh(Fsu)                 # Hermitian => real f_k
Xe = Vv.conj().T @ Xv @ Vv
Fe = np.diag(fv)
spec = np.array([[(fv[k] - fv[l]) * Xe[k, l] for l in range(4)] for k in range(4)])
print("I3 spectral: ||[F,Xi] - (f_k-f_l)Xi_kl|| = %.2e ; max|Im f| = %.2e"
      % (np.abs(Fe @ Xe - Xe @ Fe - spec).max(), np.abs(fv.imag).max()))

