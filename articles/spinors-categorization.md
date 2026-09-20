
# __Spinors categorization__

## Introduction

This article gives a classification of spinors, organized by the **dimension and signature of the underlying quadratic space**. For each quadratic space we state which types of spinor occur, and which structural properties separate them.

The general theory is in the companion articles *Clifford Algebras* and the sibling *Spinors*. We assume familiarity with quadratic forms, with the Clifford algebra $Cl(V, Q)$ and its $\mathbb{Z}/2$-grading, with the spin group $\mathrm{Spin}(V, Q)$, and with the spinor module.

The classification has two independent inputs.

- The **dimension** $n = p + q$. It controls whether the spinor module is irreducible or splits into two chiral halves.
- The **signature** $(p,q)$, through the residue of $p - q$ modulo $8$. It controls the reality structure of the spinor module: whether a real, quaternionic, or only a complex structure is available, and whether such a structure respects the chiral splitting.

Over $\mathbb{C}$ there is no signature, and the classification reduces to the parity of $n$. Over $\mathbb{R}$ it is governed by $p - q \bmod 8$. These two statements are the complex and the real Bott periodicity.

A word on conventions. We use the sign convention $v^2 = Q(v) \cdot 1$ of the companion article *Clifford Algebras*, with bilinear form

$$
B(u, v) = \tfrac{1}{2}\bigl(Q(u + v) - Q(u) - Q(v)\bigr).
$$

The real Clifford algebra of signature $(p,q)$ is written $Cl_{p,q}(\mathbb{R})$, and the complex Clifford algebra of dimension $n$ is written $\mathbb{C}l_n$. The spinor module is written $\Delta$; its chiral halves are written $\Delta^+$ and $\Delta^-$. The groups are $\mathrm{Spin}(p,q)$ and $\mathrm{Pin}(p,q)$.

Throughout, "signature $(p,q)$" means that $Q$ has $p$ positive and $q$ negative squares; in an orthogonal basis,

$$
Q(x_1 e_1 + \cdots + x_n e_n) = x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_n^2, \qquad n = p + q.
$$

Only non-degenerate forms are considered; the degenerate case belongs to the companion article *Clifford Algebras*.

---

## 1. The classifying properties

A spinor is an element of a module over a Clifford algebra, so spinors are classified by classifying these modules together with the structures they carry. Four properties do the classifying.

**Dimension $n$.** It fixes the complex dimension of the spinor module, $2^{\lfloor n/2 \rfloor}$, and it determines whether the module is irreducible or splits into chiral halves. The splitting occurs exactly when $n$ is even.

**Signature modulo eight.** The type of the real Clifford algebra — real, complex, or quaternionic — and hence the reality properties of the spinor, depends only on the residue $s = p - q \bmod 8$, not on $p$ and $q$ separately.

**The chiral grading.** When $n$ is even, the spinor module carries a chirality operator, an involution decomposing it as $\Delta_{\mathbb{C}} = \Delta^+_{\mathbb{C}} \oplus \Delta^-_{\mathbb{C}}$. A reality structure may preserve this decomposition or exchange the two halves; the two behaviours are different classes of spinor.

**The reality structure.** A spinor may carry a real structure (a "Majorana condition"), a quaternionic structure, or neither. These possibilities are mutually exclusive and are separated by the commutant of the Clifford action.

Over $\mathbb{C}$ only the parity of $n$ survives, because all non-degenerate complex quadratic forms of a given dimension are isomorphic. Over $\mathbb{R}$ the residues $n \bmod 2$ and $s \bmod 8$ are linked by $n \equiv s \pmod 2$ but carry different information: $n$ controls the size and the splitting, $s$ controls the reality type. The main content of the classification is that the *type* is a function of $s$ alone, while the *size* is a function of $n$ alone.

---

## 2. Dirac, Weyl, Majorana, Majorana–Weyl

Let $(V, Q)$ be a real quadratic space of signature $(p,q)$, $n = p + q$, with Clifford algebra $Cl_{p,q}(\mathbb{R})$. Its complexification is $\mathbb{C}l_n$. The **spinor module** $\Delta$ is an irreducible module of $\mathbb{C}l_n$, of complex dimension

$$
\dim_{\mathbb{C}} \Delta = 2^{\lfloor n/2 \rfloor}.
$$

It restricts to a representation of the spin group $\mathrm{Spin}(p,q)$. A **Dirac spinor** is an element of $\Delta$, with no further structure assumed.

When $n$ is even, choose an orthonormal basis and set $\omega = e_1 e_2 \cdots e_n$. Then

$$
\omega^2 = (-1)^{n(n-1)/2} Q(e_1) \cdots Q(e_n) = (-1)^{n/2 + q}.
$$

Over $\mathbb{C}$ one rescales $\omega$ by a power of $i$ to obtain an involution, giving the decomposition

$$
\Delta_{\mathbb{C}} = \Delta^+_{\mathbb{C}} \oplus \Delta^-_{\mathbb{C}}, \qquad \dim_{\mathbb{C}} \Delta^\pm_{\mathbb{C}} = 2^{n/2 - 1}.
$$

A **Weyl spinor** (chiral spinor) is an element of one of the halves $\Delta^\pm_{\mathbb{C}}$. Weyl spinors exist exactly when $n$ is even. For odd $n$ the volume element is central and acts as a scalar; the module is irreducible and there is no splitting.

A **Majorana spinor** is an element of the fixed space of a **real structure**, a conjugate-linear map $C : \Delta_{\mathbb{C}} \to \Delta_{\mathbb{C}}$ satisfying

$$
C^2 = 1, \qquad C(\lambda \psi) = \bar{\lambda}\, C(\psi) \ (\lambda \in \mathbb{C}), \qquad C \circ \gamma(v) = \gamma(v) \circ C \ (v \in V),
$$

where $\gamma$ is the Clifford action. The fixed space $\Delta_{\mathbb{C}}^C$ is a real form of the complex spinor module and a real representation of $\mathrm{Spin}(p,q)$. A **symplectic Majorana spinor** (pseudo-real, quaternionic Majorana) is defined in the same way with $J^2 = -1$ in place of $C^2 = 1$, giving a quaternionic structure.

A **Majorana–Weyl spinor** is a Weyl spinor that is simultaneously Majorana, that is, a real structure preserving each chiral half instead of exchanging them. The four notions are related by

$$
\text{Majorana--Weyl} \subset \text{Weyl} \subset \text{Dirac}, \qquad \text{Majorana--Weyl} \subset \text{Majorana} \subset \text{Dirac}.
$$

Not every quadratic space admits every type; the point of the classification is to decide which are possible.

---

## 3. Complex spinors and the two chiral halves

Over $\mathbb{C}$ there is a single non-degenerate quadratic form in each dimension, so the classification depends only on $n$. The complex Clifford algebra is

$$
\mathbb{C}l_{2k} \cong M_{2^k}(\mathbb{C}), \qquad \mathbb{C}l_{2k+1} \cong M_{2^k}(\mathbb{C}) \oplus M_{2^k}(\mathbb{C}),
$$

and it is periodic of period two:

$$
\mathbb{C}l_{n+2} \cong \mathbb{C}l_n \otimes M_2(\mathbb{C}).
$$

This is the **complex Bott periodicity**. Its consequences for spinors are the following.

- **Even dimension $n = 2k$.** The algebra $\mathbb{C}l_{2k}$ is a full matrix algebra, so it has a unique irreducible module, of dimension $2^k$. The chirality operator splits it into two halves $\Delta^\pm$, each of dimension $2^{k-1}$. These are the two **Weyl** (half-spin) representations; they are the two non-isomorphic irreducible modules of the even subalgebra $\mathbb{C}l_{2k}^0$, and they are exchanged by the odd part of the Clifford algebra. As representations of the spin group they are the two "handed" spinors.
- **Odd dimension $n = 2k+1$.** The algebra is a sum of two full matrix algebras, and the spinor module has dimension $2^k$ and is irreducible. There is a single spin representation and no Weyl splitting; the volume element acts as a scalar whose square is $(-1)^{k}\prod_i Q(e_i)$, that is $\pm 1$ when that product is $+1$ and $\pm i$ when it is $-1$.

**Examples.** For $n = 2, 4, 6$ the two Weyl representations have complex dimension $1, 2, 4$; for $n = 1$ and $n = 3$ the single spin representation has complex dimension $1$ and $2$.

Over $\mathbb{C}$ the classification records no reality type, because there is a single non-degenerate complex quadratic form in each dimension. The complex classification therefore knows only "Dirac" and "Weyl", and the parity of $n$ is the only invariant.

---

## 4. Reality and quaternionic structures

Let $A = Cl_{p,q}(\mathbb{R})$, acting on the spinor module. The **commutant** of this action, the real-linear endomorphisms commuting with the Clifford action, is a finite-dimensional real division algebra, hence one of $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$. Equivalently, the irreducible module of $A$ has **type** $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$, recorded by the **Frobenius–Schur indicator** ($+1$ real, $0$ complex, $-1$ quaternionic).

The relationship with §2 is the following.

- Type $\mathbb{R}$: the real structure $C$ exists, $C^2 = +1$. The spinor is **Majorana**.
- Type $\mathbb{H}$: the quaternionic structure $J$ exists, $J^2 = -1$. The spinor is **symplectic Majorana**.
- Type $\mathbb{C}$: neither exists, and the module is not isomorphic to its complex conjugate. The spinor is an ordinary **complex Dirac** spinor.

Two warnings. First, the type of the full Clifford module and the type of a Weyl half need not agree: for even $n$ with $s \equiv 2, 6 \pmod 8$ the antilinear structure exchanges the chiral halves, so the halves individually have complex type even though the full module is self-conjugate, real for $s \equiv 2$ and quaternionic for $s \equiv 6$. These are the cases of complex Weyl spinors. Second, the presence of a reality structure depends on the signature, not only on the dimension.

---

## 5. The real classification: signature modulo eight

The real Clifford algebras are periodic of period eight:

$$
Cl_{p+8,q}(\mathbb{R}) \cong Cl_{p,q}(\mathbb{R}) \otimes M_{16}(\mathbb{R}), \qquad Cl_{p,q+8}(\mathbb{R}) \cong Cl_{p,q}(\mathbb{R}) \otimes M_{16}(\mathbb{R}).
$$

Hence the isomorphism class of $Cl_{p,q}(\mathbb{R})$ depends only on $n = p + q$ and the residue $s = p - q \bmod 8$. This is the **real Bott periodicity**, and the eightfold pattern is the Atiyah–Bott–Shapiro / Brauer–Wall periodicity. Since $M_{16}(\mathbb{R})$ has real type, tensoring with it leaves the type unchanged and changes only the matrix size: the *type* is a function of $s$ alone, the *size* a function of $n$.

| $s$ | $Cl_{p,q}(\mathbb{R})$ | type |
|---|---|---|
| $0$ | $M_{2^{n/2}}(\mathbb{R})$ | $\mathbb{R}$ |
| $1$ | $M_{2^{(n-1)/2}}(\mathbb{R}) \oplus M_{2^{(n-1)/2}}(\mathbb{R})$ | $\mathbb{R}$ |
| $2$ | $M_{2^{n/2}}(\mathbb{R})$ | $\mathbb{R}$ |
| $3$ | $M_{2^{(n-1)/2}}(\mathbb{C})$ | $\mathbb{C}$ |
| $4$ | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$ |
| $5$ | $M_{2^{(n-3)/2}}(\mathbb{H}) \oplus M_{2^{(n-3)/2}}(\mathbb{H})$ | $\mathbb{H}$ |
| $6$ | $M_{2^{(n-2)/2}}(\mathbb{H})$ | $\mathbb{H}$ |
| $7$ | $M_{2^{(n-1)/2}}(\mathbb{C})$ | $\mathbb{C}$ |

The exponents are integers because $n$ is even when $s$ is even and odd when $s$ is odd; the parity of $n$ is determined by $s$ modulo $2$.

**Examples.** For $(3,1)$, $s = 2$ and $Cl_{3,1}(\mathbb{R}) \cong M_4(\mathbb{R})$, of real type; for $(1,3)$, $s \equiv 6$ and $Cl_{1,3}(\mathbb{R}) \cong M_2(\mathbb{H})$, of quaternionic type. These have the same dimension and different type, so the residue is a genuine invariant. Also $Cl_{0,3}(\mathbb{R}) \cong \mathbb{H} \oplus \mathbb{H}$ and $Cl_{3,0}(\mathbb{R}) \cong M_2(\mathbb{C})$.

---

## 6. The spinor types by signature modulo eight

The full Dirac spinor has the type of $Cl_{p,q}(\mathbb{R})$. The Weyl halves, when they exist (even $n$), have the type of the even subalgebra:

$$
Cl^0_{p,q}(\mathbb{R}) \cong Cl_{q,p-1}(\mathbb{R}) \quad (p \geq 1), \qquad Cl^0_{0,q}(\mathbb{R}) \cong Cl_{0,q-1}(\mathbb{R}).
$$

Both correspond, through §5, to the residue $1 - s \bmod 8$. The classification is collected below; here $s = p - q \bmod 8$.

| $s$ | $n$ parity | Dirac spinor | Weyl halves | standard name |
|---|---|---|---|---|
| $0$ | even | real | real | Majorana–Weyl |
| $1$ | odd | real | do not exist | Majorana |
| $2$ | even | real | complex | Majorana Dirac; Weyl complex |
| $3$ | odd | complex | do not exist | complex Dirac |
| $4$ | even | quaternionic | quaternionic | symplectic Majorana–Weyl |
| $5$ | odd | quaternionic | do not exist | symplectic Majorana |
| $6$ | even | quaternionic | complex | symplectic Majorana Dirac; Weyl complex |
| $7$ | odd | complex | do not exist | complex Dirac |

Several consequences deserve emphasis.

- A **Majorana spinor exists** exactly when $s \equiv 0, 1, 2 \pmod 8$; a **symplectic Majorana spinor** exactly when $s \equiv 4, 5, 6 \pmod 8$; a spinor with no reality condition (complex Dirac) exactly when $s \equiv 3, 7 \pmod 8$.
- A **Weyl spinor exists** exactly when $n$ is even. A **Majorana–Weyl spinor exists** exactly when $s \equiv 0 \pmod 8$; a **symplectic Majorana–Weyl spinor** exactly when $s \equiv 4 \pmod 8$. For $s \equiv 2, 6 \pmod 8$ a Weyl spinor exists but carries no real structure on either half.

**Dimension of the spinor.** The complex dimension of the Dirac spinor is $2^{\lfloor n/2 \rfloor}$, and a Weyl half has complex dimension $2^{n/2 - 1}$ for even $n$. As a real vector space the Dirac spinor has dimension $2^{\lfloor n/2 \rfloor}$ when the type is $\mathbb{R}$, and twice that when the type is $\mathbb{C}$ or $\mathbb{H}$.

---

## 7. Pin versus Spin

Let $(V, Q)$ have signature $(p,q)$. The **Pin group** is the subgroup of the units of $Cl_{p,q}(\mathbb{R})$ generated by the unit vectors,

$$
\mathrm{Pin}(p,q) = \langle\, v \in V : Q(v) = 1 \,\rangle \subseteq Cl_{p,q}(\mathbb{R})^\times,
$$

and the **spin group** is its even part,

$$
\mathrm{Spin}(p,q) = \mathrm{Pin}(p,q) \cap Cl^0_{p,q}(\mathbb{R}).
$$

Conjugation by an element of $\mathrm{Pin}(p,q)$ preserves $V$ and $Q$, giving surjections

$$
\mathrm{Pin}(p,q) \longrightarrow O(p,q), \qquad \mathrm{Spin}(p,q) \longrightarrow SO(p,q),
$$

both with kernel $\{\pm 1\}$. Thus $\mathrm{Pin}(p,q)$ double covers the full orthogonal group and $\mathrm{Spin}(p,q)$ double covers the special orthogonal group. For $p + q \geq 3$ the spin group is the connected double cover of the identity component $SO^+(p,q)$; the element $-1$ is the nontrivial kernel element. The small exception is $\mathrm{Spin}(1,1) \cong \mathbb{R}^\times$.

There are in fact two Pin groups. Replacing the generating set by the vectors with $Q(v) = -1$ gives a second double cover:

$$
\mathrm{Pin}^\pm(p,q) = \langle\, v \in V : Q(v) = \pm 1 \,\rangle.
$$

When the form is indefinite, both generating sets are non-empty and $\mathrm{Pin}^+$ and $\mathrm{Pin}^-$ are the two distinct double covers of $O(p,q)$; they are exchanged by replacing $Q$ with $-Q$. The spin group is the common even subgroup and does not see the distinction. In definite signature the two conventions are again exchanged by $Q \mapsto -Q$, giving the two double covers $\mathrm{Pin}^\pm(n)$ of $O(n)$.

The Pin/Spin distinction is the difference between the two sign conventions for the Clifford generators, and between a spinor that changes sign under a reflection and one that does not; the element $-1$ acts as $-\mathrm{id}$ on the spinor module. It is orthogonal to the Dirac/Weyl/Majorana classification, which concerns the reality structures the module carries rather than which orthogonal transformations lift to the Clifford algebra. Both are needed on a manifold, whose structure group involves both an orientation (Spin versus Pin) and a reality condition.

---

## 8. Spin structures on manifolds

Let $M$ be a smooth manifold of dimension $n$ with a Riemannian metric.

**Orientation.** The frame bundle reduces from $O(n)$ to $SO(n)$ precisely when the first Stiefel–Whitney class vanishes:

$$
w_1(M) = 0.
$$

**Spin structure.** Given an orientation, the structure group lifts from $SO(n)$ to $\mathrm{Spin}(n)$ precisely when the second Stiefel–Whitney class vanishes:

$$
w_2(M) = 0.
$$

A choice of such a lift is a **spin structure**, and a manifold carrying one is a **spin manifold**; equivalently, a spin structure is a principal $\mathrm{Spin}(n)$-bundle double covering the oriented frame bundle. When spin structures exist they form a torsor over $H^1(M; \mathbb{Z}/2\mathbb{Z})$; in particular, a spin structure on a connected manifold is unique when $H^1(M; \mathbb{Z}/2\mathbb{Z}) = 0$.

**The spinor bundle and the Dirac operator.** A spin structure makes the spinor representations into vector bundles over $M$: the **spinor bundle** carries the spinor module fiberwise, and the Levi-Civita connection lifts to it. The **Dirac operator** composes the covariant derivative with Clifford multiplication; its square is the spin Laplacian, and on a closed spin manifold its index is the $\hat{A}$-genus, an integer by the Atiyah–Singer index theorem.

**Related classes.**

- $w_1$: the obstruction to orientability.
- $w_2$: the obstruction to a spin structure, for an oriented manifold.
- $w_2 + w_1^2$: the obstruction to a $\mathrm{Pin}^-$ structure, in the convention in which $\mathrm{Pin}^+$ is obstructed by $w_2$, on an unoriented manifold. The naming of the two Pin structures is not uniform in the literature; the algebraic distinction is the one in §7, and the two obstruction classes are $w_2$ and $w_2 + w_1^2$.
- $W_3$: the **integral third Stiefel–Whitney class**, the obstruction to a $\mathrm{Spin}^c$ structure, a lift of the structure group to

$$
\mathrm{Spin}^c(n) = \frac{\mathrm{Spin}(n) \times U(1)}{\{\pm 1\}}.
$$

A $\mathrm{Spin}^c$ structure exists exactly when $w_2$ is the mod $2$ reduction of an integral class, and $W_3$ is the obstruction; every oriented manifold of dimension $n \leq 4$ admits one. The $\mathrm{Spin}^c$ case allows a twisted spinor bundle and a twisted Dirac operator.

- The **Pontryagin class** $p_1$ reduces modulo $2$ to $w_2^2$; on a spin manifold this reduction vanishes.

**Examples.** The sphere $S^n$ and the torus $T^n$ are spin. The complex projective space $\mathbb{C}P^k$ is spin exactly when $k$ is odd. A closed orientable surface is spin and carries $2^{2g}$ spin structures, classified by a quadratic refinement measured by the Arf invariant. In dimension four, a closed oriented manifold is spin exactly when its intersection form is even.

---

## 9. The symmetry classes and Bott periodicity

The eightfold pattern of §5 is the real Bott periodicity of the orthogonal group, and it reappears whenever a structure is classified by Clifford modules. The groups carrying the pattern are the homotopy groups of the stable orthogonal and unitary groups:

| $k \bmod 8$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
|---|---|---|---|---|---|---|---|---|
| $KO^{-k}(\mathrm{pt})$ | $\mathbb{Z}$ | $\mathbb{Z}/2$ | $\mathbb{Z}/2$ | $0$ | $\mathbb{Z}$ | $0$ | $0$ | $0$ |
| $KU^{-k}(\mathrm{pt})$ | $\mathbb{Z}$ | $0$ | $\mathbb{Z}$ | $0$ | $\mathbb{Z}$ | $0$ | $\mathbb{Z}$ | $0$ |

Here $KO$ is real and $KU$ complex $K$-theory. The real sequence has period eight and the complex sequence period two, matching §5 and §3. The same periodicity organizes the Cartan classification of symmetric spaces into ten families and the classification of Clifford modules by type into ten classes: the two complex classes A and AIII, and the eight real classes AI, BDI, D, DIII, AII, CII, C, and CI. The labels run through the same residues, and a real or quaternionic structure on the module matches the corresponding structure on a Clifford module.

---

## 10. The hierarchy of the classes

The classes fit into a single hierarchy, from the underlying quadratic space to the concrete spinor types.

**Quadratic space.** A real quadratic space $(V,Q)$ of signature $(p,q)$ determines $n = p+q$ and the residue $s = p-q \bmod 8$.

**Clifford algebra.** These determine $Cl_{p,q}(\mathbb{R})$: matrix size by $n$, type by $s$.

**Covering group.** The algebra contains the Pin group $\mathrm{Pin}^\pm(p,q)$ and its even subgroup $\mathrm{Spin}(p,q)$, double covering $O(p,q)$ and $SO(p,q)$.

**Spinor module and structures.** The algebra has an irreducible module $\Delta$ of complex dimension $2^{\lfloor n/2 \rfloor}$, restricting to a representation of $\mathrm{Spin}(p,q)$; it carries a chirality operator exactly when $n$ is even, splitting it into Weyl halves, and a real or quaternionic structure according to the type.

Over $\mathbb{C}$ there are only two classes: the irreducible spinor (odd $n$) and the pair of Weyl halves (even $n$). Over $\mathbb{R}$ each complex class splits by type into a real, quaternionic, or complex Dirac spinor and, when $n$ is even, a real, quaternionic, or complex pair of Weyl halves. The inclusion lattice is

$$
\text{Majorana--Weyl} \subset \text{Weyl} \subset \text{Dirac}, \qquad \text{Majorana--Weyl} \subset \text{Majorana} \subset \text{Dirac}.
$$

A Majorana–Weyl spinor is thus the most constrained class, requiring both even dimension and a real structure compatible with chirality; a complex Dirac spinor is the least constrained.

---

## 11. Low-dimensional examples

The table collects the standard low-dimensional cases; "Dirac" gives the reality type of the full spinor module, "Weyl" that of the chiral halves.

| $(p,q)$ | $n$ | $s \bmod 8$ | type | Dirac spinor | Weyl halves | spin group |
|---|---|---|---|---|---|---|
| $(1,0)$ | $1$ | $1$ | $\mathbb{R}$ | Majorana | — | $\{\pm 1\}$ |
| $(0,1)$ | $1$ | $7$ | $\mathbb{C}$ | complex | — | $\{\pm 1\}$ |
| $(2,0)$ | $2$ | $2$ | $\mathbb{R}$ | Majorana | complex | $U(1)$ |
| $(1,1)$ | $2$ | $0$ | $\mathbb{R}$ | Majorana | real (MW) | $\mathbb{R}^\times$ |
| $(0,2)$ | $2$ | $6$ | $\mathbb{H}$ | symplectic Majorana | complex | $U(1)$ |
| $(3,0)$ | $3$ | $3$ | $\mathbb{C}$ | complex | — | $SU(2)$ |
| $(2,1)$ | $3$ | $1$ | $\mathbb{R}$ | Majorana | — | $SL(2,\mathbb{R})$ |
| $(1,2)$ | $3$ | $7$ | $\mathbb{C}$ | complex | — | $SL(2,\mathbb{R})$ |
| $(0,3)$ | $3$ | $5$ | $\mathbb{H}$ | symplectic Majorana | — | $SU(2)$ |
| $(4,0)$ | $4$ | $4$ | $\mathbb{H}$ | symplectic Majorana | quaternionic | $SU(2) \times SU(2)$ |
| $(3,1)$ | $4$ | $2$ | $\mathbb{R}$ | Majorana | complex | $SL(2,\mathbb{C})$ |
| $(2,2)$ | $4$ | $0$ | $\mathbb{R}$ | Majorana | real (MW) | $SL(2,\mathbb{R}) \times SL(2,\mathbb{R})$ |
| $(1,3)$ | $4$ | $6$ | $\mathbb{H}$ | symplectic Majorana | complex | $SL(2,\mathbb{C})$ |
| $(0,4)$ | $4$ | $4$ | $\mathbb{H}$ | symplectic Majorana | quaternionic | $SU(2) \times SU(2)$ |
| $(5,1)$ | $6$ | $4$ | $\mathbb{H}$ | symplectic Majorana | quaternionic (MW) | — |
| $(7,1)$ | $8$ | $6$ | $\mathbb{H}$ | symplectic Majorana | complex | — |
| $(9,1)$ | $10$ | $0$ | $\mathbb{R}$ | Majorana | real (MW) | — |

A few of these are worth stating in words.

- **Dimension two.** In the Euclidean signature $(2,0)$ the spin group is $U(1)$ and the two Weyl spinors are complex lines transforming by $e^{\pm i\theta/2}$. In the split signature $(1,1)$ the spin group is $\mathbb{R}^\times$ and the two Weyl spinors are real lines; this is the simplest Majorana–Weyl case.
- **Dimension three.** The Euclidean signature $(3,0)$ gives $SU(2)$ acting on $\mathbb{C}^2$, the fundamental doublet representation. The split signature $(2,1)$ gives $SL(2,\mathbb{R})$ acting on a real two-dimensional Majorana spinor.
- **Dimension four.** The Euclidean signature $(4,0)$ gives $SU(2) \times SU(2)$ with quaternionic Weyl halves. The Lorentzian signature $(3,1)$ gives $SL(2,\mathbb{C})$, with complex two-dimensional Weyl spinors and a Majorana real form of the full Dirac spinor, but no Majorana–Weyl spinor, because the real structure exchanges the two chiralities. In this signature the even Clifford algebra is the biquaternion algebra $Cl^+_{3,1}(\mathbb{R}) \cong \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, so the Lorentzian spinors are the two-dimensional complex modules over the biquaternions and the two chiral components are the left- and right-handed Weyl spinors. The same applies to $(1,3)$, with the chiralities interchanged.

---

## Summary

Let me summarize the classification.

| $s = p-q \bmod 8$ | Dirac spinor | Weyl halves | Majorana–Weyl? |
|---|---|---|---|
| $0$ | real (Majorana) | real | yes |
| $1$ | real (Majorana) | do not exist | no |
| $2$ | real (Majorana) | complex | no |
| $3$ | complex | do not exist | no |
| $4$ | quaternionic (symplectic Majorana) | quaternionic | symplectic only |
| $5$ | quaternionic (symplectic Majorana) | do not exist | no |
| $6$ | quaternionic (symplectic Majorana) | complex | no |
| $7$ | complex | do not exist | no |

The pattern is clear: the dimension determines whether the spinor splits, and the signature modulo eight determines the reality type. The two are independent, and together they classify the spinors over a non-degenerate real quadratic space.

The standard examples that anchor the classification are as follows. In two dimensions the Euclidean case gives the complex Weyl lines of $U(1)$ and the split case the real Majorana–Weyl lines of $\mathbb{R}^\times$. In three dimensions the Euclidean case gives the $SU(2)$ doublet. In four dimensions the Euclidean case gives the quaternionic Weyl halves of $SU(2) \times SU(2)$, and the Lorentzian case the complex Weyl spinors of $SL(2,\mathbb{C})$ together with a Majorana Dirac spinor. In six dimensions the Lorentzian case gives symplectic Majorana–Weyl spinors, and in ten dimensions the real Majorana–Weyl spinors.

---

## Further Reading

- Élie Cartan, *The Theory of Spinors* (Dover, 1966).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001).
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990).
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry* (American Mathematical Society, 2000).
- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974).
- Max Karoubi, *K-Theory: An Introduction* (Springer, 1978).
