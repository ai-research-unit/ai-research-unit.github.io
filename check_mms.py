import numpy as np, itertools

I = np.eye(4, dtype=complex)
EX = np.array([[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,-1,0,0]], dtype=complex)  # placeholder, filled below

# basis e_t=0, ex=1, ey=2, ez=3 with ek^2=-1, ex ey = ez (cyclic)
def mul(a, b):
    at, ax, ay, az = a
    bt, bx, by, bz = b
    t = at*bt - ax*bx - ay*by - az*bz
    x = at*bx + ax*bt + ay*bz - az*by
    y = at*by - ax*bz + ay*bt + az*bx
    z = at*bz + ax*by - ay*bx + az*bt
    return np.array([t, x, y, z], dtype=complex)

E = {0: np.array([1,0,0,0], complex), 1: np.array([0,1,0,0], complex),
     2: np.array([0,0,1,0], complex), 3: np.array([0,0,0,1], complex)}

def Lmat(a):  # left multiplication matrix
    return np.column_stack([mul(a, E[k]) for k in range(4)])
def Rmat(a):  # right multiplication matrix
    return np.column_stack([mul(E[k], a) for k in range(4)])

def act(f):  # action written as coefficient matrix
    return np.column_stack([f(E[k]) for k in range(4)])

ii = 1j
Ct   = act(lambda p: ii*mul(p, E[1]))
Ck = {k: act(lambda p, k=k: ii*mul(mul(E[k], p), E[2])) for k in (1,2,3)}
C = [Ct, Ck[1], Ck[2], Ck[3]]
chi  = act(lambda p: -ii*mul(p, E[3]))
eps = [1,-1,-1,-1]

def chk(name, M, expect):
    err = np.max(np.abs(M-expect))
    print(f"{name:52s} err={err:.3e} {'OK' if err<1e-10 else 'FAIL'}")

print("=== frame actions C_mu, chi ===")
for mu in range(4):
    chk(f"C_{mu}^2 = {eps[mu]}*1", C[mu]@C[mu], eps[mu]*I)
chk("chi^2 = +1", chi@chi, I)
for mu in range(4):
    chk(f"chi C_{mu} + C_{mu} chi = 0", chi@C[mu]+C[mu]@chi, 0*I)
for mu in range(4):
    for nu in range(4):
        tgt = 2*eps[mu]*I if mu==nu else 0*I
        chk(f"{{C_{mu},C_{nu}}} = 2 eps delta", C[mu]@C[nu]+C[nu]@C[mu], tgt)

print("=== C_munu = 1/2 [C_mu,C_nu] ===")
Cmn = {(m,n): 0.5*(C[m]@C[n]-C[n]@C[m]) for m in range(4) for n in range(4)}
for m in range(4):
    for n in range(4):
        if m<n:
            chk(f"C_{m}{n} = C_{m}C_{n} (distinct)", Cmn[(m,n)], C[m]@C[n])

print("=== trace identity Tr[chi C_rho C_lam C_munu] = -4 i eps(rho,lam,mu,nu) ===")
def lev(a,b,c,d):
    p=[a,b,c,d]
    if len(set(p))<4: return 0
    inv=sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])
    return (-1)**inv
bad=[]
for r,l,m,n in itertools.product(range(4),repeat=4):
    val=np.trace(chi@C[r]@C[l]@Cmn[(m,n)])
    tgt=-4j*lev(r,l,m,n)
    if abs(val-tgt)>1e-9: bad.append((r,l,m,n,val,tgt))
print("mismatches:",len(bad), bad[:3])

print("=== C_0 C_01 == C_1 ===")
chk("C_0 C_01 = C_1", C[0]@Cmn[(0,1)], C[1])

print("=== source generators G_mu ===")
G0 = act(lambda p: ii*mul(E[1], p))
Gx = act(lambda p: -mul(mul(E[2], p), E[1]))
Gy = act(lambda p:  mul(mul(E[2], p), E[2]))
Gz = act(lambda p: -mul(mul(E[2], p), E[3]))
G=[G0,Gx,Gy,Gz]
for mu in range(4):
    chk(f"G_{mu}^2 = +1 (as printed, q_k^2=-1)", G[mu]@G[mu], I)
for mu in range(4):
    for nu in range(4):
        print(f"  {{G_{mu},G_{nu}}} =", np.round((G[mu]@G[nu]+G[nu]@G[mu])[0,0].real,6),
              " "*3, end="")
    print()

print("=== right multiplication and the letter (L=-1, R=+1 of chi) ===")
rng=np.random.default_rng(0)
def letter(p):
    v=chi@p
    return -1 if np.allclose(v,-p) else (+1 if np.allclose(v,p) else 0)
p=rng.normal(size=4)+1j*rng.normal(size=4)
chi_p = chi@p
pL = 0.5*(p - chi_p)   # chi eigenvalue -1
pR = 0.5*(p + chi_p)   # chi eigenvalue +1
print("  letter(pL)=",letter(pL)," letter(pR)=",letter(pR))
for k,name in [(0,'e_t'),(1,'e_x'),(2,'e_y'),(3,'e_z')]:
    print(f"  R_{name}: L->{letter(mul(pL,E[k])):+d}  R->{letter(mul(pR,E[k])):+d}"
          f"   |  L_{name}: L->{letter(mul(E[k],pL)):+d}  R->{letter(mul(E[k],pR)):+d}")

print("=== zero action / source operator square ===")
Z=np.zeros((4,4),complex)
print("all-zero check:", np.max(np.abs(Z)))

print("=== bilinear rule ReTr<psi, q_k psi> = 0 ===")
def pair(a,b):  # <a,b> = a^dagger i b e_x
    return np.conj(a)@ (ii*mul(b,E[1]))
vals=[]
for _ in range(5):
    a=rng.normal(size=4)+1j*rng.normal(size=4)
    for k in (1,2,3):
        v=pair(a,mul(E[k],a))
        vals.append(abs(v.real))
print("max |Re<psi,q_k psi>|:", max(vals))

print("=== source Dirac operator square ===")
for k0,k1,k2,k3 in [(1.3,0.4,0.7,1.1),(0,1,0,0),(2,0,0,0)]:
    M = 1j*C[0]*k0 + 1j*C[1]*k1 + 1j*C[2]*k2 + 1j*C[3]*k3
    chk("(iC^a k_a)^2 = -k0^2+k^2", M@M, (-k0**2+k1**2+k2**2+k3**2)*I)

print("=== bilinear parity ===")
rng=np.random.default_rng(7)
a=rng.normal(size=4)+1j*rng.normal(size=4)
for (m,n) in itertools.combinations(range(4),2):
    v=pair(a, Cmn[(m,n)]@a)
    print(f"  <psi,C_{m}{n} psi> real={v.real:+.2e} imag={v.imag:+.4f}")
print("  <psi,C_k psi> imag parts:", [f"{pair(a,C[k]@a).imag:+.1e}" for k in (1,2,3)])
b=pair(a, C[0]@Cmn[(0,1)]@a); print("  B_001 =", b)
