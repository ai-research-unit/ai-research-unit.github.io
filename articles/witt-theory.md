
# __Witt Theory__

## Introduction

Witt theory is the algebraic theory of quadratic forms over a field, organized around **isometry**. Founded by Ernst Witt in 1937, it provides a small set of invariants — dimension, discriminant, Hasse invariant, Witt index — that classify forms over the fields of arithmetic, and organizes the forms into a ring, the **Witt ring**, whose arithmetic reflects that of the base field.

Three results carry the theory. **Witt's extension theorem** (§2): an isometry between subspaces of a non-degenerate space extends to an isometry of the whole space. **Witt's cancellation theorem** (§4): a non-degenerate summand can be cancelled from an orthogonal sum. The **Witt decomposition** (§6): every form is uniquely a hyperbolic part plus an anisotropic part.

**Standing assumptions.** Throughout, $F$ is a field, spaces are finite-dimensional over $F$, and unless stated otherwise $\operatorname{char} F \neq 2$ and every form is non-degenerate. In characteristic $2$ the polarization identity fails, the correspondence between quadratic and bilinear forms breaks down, and cancellation fails (§5). Definitions are in *Bilinear and Quadratic Forms*; examples in *Bilinear and Quadratic Forms: Categorization*.

---

# Part I: Isometry and the Extension Theorem

## 1. Quadratic Spaces and Isometries

A **quadratic form** on $V$ is a function $q : V \to F$ with $q(\lambda v) = \lambda^2 q(v)$ whose **polar form**

$$
b(x, y) = \tfrac{1}{2}\bigl(q(x + y) - q(x) - q(y)\bigr)
$$

is bilinear. Since $\operatorname{char} F \neq 2$, the factor $\tfrac{1}{2}$ exists and $q$, $b$ determine each other: $b(x, x) = q(x)$.

The pair $(V, q)$ is a **quadratic space**, **non-degenerate** when its radical $\operatorname{rad}(q) = \{v : b(v, w) = 0 \ \forall w\}$ is zero, equivalently when $V \to V^*$, $v \mapsto b(v, -)$, is an isomorphism.

An **isometry** $\sigma : (V, q) \to (V', q')$ is a linear isomorphism with $q'(\sigma x) = q(x)$, equivalently $b'(\sigma x, \sigma y) = b(x, y)$. The isometries of $(V, q)$ form the **orthogonal group** $\operatorname{O}(V, q)$.

A form is **diagonal**, written $q \cong \langle a_1, \ldots, a_n\rangle$, if $q(x) = a_1 x_1^2 + \cdots + a_n x_n^2$ in some basis. Every non-degenerate form over a field of characteristic $\neq 2$ is diagonal: choose $v$ with $q(v) \neq 0$, split $V = Fv \perp v^\perp$, and induct. Its **Gram matrix** is then $\operatorname{diag}(a_1, \ldots, a_n)$, and a change of basis replaces it by the congruent matrix $P^T G P$. Rescaling a basis vector by $c$ multiplies its coefficient by $c^2$, so $\langle a \rangle \cong \langle a c^2 \rangle$ and a coefficient matters only as a class in $F^*/(F^*)^2$.

In characteristic $2$, $b(v, v) = 0$ for every $v$, so $b$ is alternating and does not determine $q$; every diagonal form has $b \equiv 0$.

## 2. The Witt Extension Theorem

For $z$ with $q(z) \neq 0$, the **reflection** in $z$ is

$$
\tau_z(x) = x - \frac{2b(x, z)}{q(z)}\, z,
$$

an isometry with $\tau_z(z) = -z$ and $\tau_z^2 = \operatorname{id}$.

**Witt's lemma.** If $q(x) = q(y) \neq 0$, some isometry carries $x$ to $y$, and it can be chosen to be a product of at most two reflections.

**Proof.** If $q(x - y) \neq 0$ then $\tau_{x-y}(x) = y$. If $q(x - y) = 0$, then $q(x + y) = 4q(x) \neq 0$ and $\tau_{x+y}(x) = -y$; since $\tau_y(y) = -y$, the composition $\tau_y \circ \tau_{x+y}$ carries $x$ to $y$. $\square$

**Witt's extension theorem.** Let $(V, q)$ be a non-degenerate quadratic space over a field of characteristic $\neq 2$, let $U \subseteq V$ be a subspace, and let $\tau : U \to V$ be an isometry into $V$. Then $\tau$ extends to an isometry of $V$.

**Corollary.** Isometric subspaces of $V$ are carried to one another by an isometry of $V$; in particular $\operatorname{O}(V, q)$ acts transitively on the subspaces of each isometry type.

The proof is an induction on $\dim U$: a non-isotropic vector is handled by Witt's lemma together with the splitting $U = Fx \perp (U \cap x^\perp)$, and a totally isotropic $U$ is reduced by splitting off a hyperbolic plane, which non-degeneracy of $V$ supplies. In characteristic $2$ the theorem survives for **non-singular** forms (polar form non-degenerate), with adjustments, since an alternating non-degenerate form has even rank.

## 3. Hyperbolic Planes and Metabolic Spaces

The **hyperbolic plane** is

$$
H = \langle 1, -1\rangle, \qquad q(u, v) = u^2 - v^2,
$$

with orthogonal basis $u, v$ of norms $1, -1$. Equivalently it is spanned by isotropic $e, f$ with $b(e, f) = 1$: then $u = e + \tfrac{1}{2} f$, $v = e - \tfrac{1}{2} f$ recover an orthogonal basis.

A subspace $W$ is **totally isotropic** if $q$ vanishes on it, equivalently (for characteristic $\neq 2$) if $b$ vanishes on it. A non-degenerate $V$ is **metabolic**, also called **split** or **hyperbolic**, if it contains a totally isotropic $W$ with $W = W^\perp$, a **Lagrangian**. This holds if and only if $V \cong mH$ for some $m$, i.e. if and only if $V$ is a sum of hyperbolic planes: from a Lagrangian one picks $e \in W$ and $f$ with $b(e, f) = 1$, adjusts $f$ to be isotropic, splits off $\operatorname{span}\{e, f\} \cong H$, and repeats on the orthogonal complement.

A nonzero $v$ with $q(v) = 0$ is **isotropic**; the form is **isotropic** if such a vector exists and **anisotropic** otherwise. Over a field of characteristic $\neq 2$, a non-degenerate form is isotropic if and only if it contains $H$ as an orthogonal summand: given isotropic $v$, non-degeneracy supplies $w$ with $b(v, w) = 1$, and replacing $w$ by $w - \tfrac{1}{2} q(w) v$ makes it isotropic, so $\operatorname{span}\{v, w\} \cong H$ splits off.

# Part II: Cancellation and Decomposition

## 4. The Witt Cancellation Theorem

**Theorem (Witt cancellation).** Let $\operatorname{char} F \neq 2$ and $q$ be non-degenerate. If $q_1 \perp q \cong q_2 \perp q$, then $q_1 \cong q_2$; moreover the isometry can be chosen to carry the first summand onto the first summand.

**Proof idea.** Let $\sigma : V_1 \perp V \to V_2 \perp V$ be an isometry. The image $\sigma(V)$ is isometric to $V$, so by the extension theorem some isometry $\rho$ of $V_2 \perp V$ has $\rho(\sigma(V)) = V$. Then $\rho \circ \sigma$ preserves $V$, hence restricts to an isometry $V_1 \to V_2$. $\square$

Cancellation makes the hyperbolic part of a form well defined (§6), makes the Witt group well defined (§7), and reduces the isometry problem to anisotropic forms.

## 5. Cancellation in Characteristic 2

Let $\operatorname{char} F = 2$. Then $b(v, v) = 0$ for all $v$ and a quadratic form is not determined by $b$. A form is **non-singular** if $b$ is non-degenerate; such forms have even dimension, and diagonal forms are singular.

Cancellation can fail. Take $q = \langle 1\rangle$, $q_1 = \langle 1, 1\rangle$, $q_2 = \langle 0, 0\rangle$, where $\langle 0, 0\rangle$ is the zero form on a plane. Then $q_1 \perp q \cong \langle 1, 1, 1\rangle$ and $q_2 \perp q \cong \langle 0, 0, 1\rangle$, that is, the forms $p(x, y, z) = x^2 + y^2 + z^2$ and $p'(x, y, z) = z^2$. The invertible linear map

$$
T(x, y, z) = (x, \, y, \, x + y + z)
$$

satisfies, since $(a + b)^2 = a^2 + b^2$ in characteristic $2$,

$$
p\bigl(T(x, y, z)\bigr) = x^2 + y^2 + (x + y + z)^2 = x^2 + y^2 + x^2 + y^2 + z^2 = z^2 = p'(x, y, z).
$$

Hence $q_1 \perp q \cong q_2 \perp q$. But $q_1(1, 0) = 1$ while $q_2$ is identically zero, so $q_1 \not\cong q_2$.

The cancelled form $q = \langle 1\rangle$ is singular: its polar form vanishes identically, although $q$ vanishes only at $0$. Cancellation is restored when the cancelled form is non-singular: non-singular forms in characteristic $2$ are classified by dimension and the **Arf invariant** in $F/\wp(F)$, where $\wp(x) = x^2 + x$, which plays the role of the discriminant, and the Witt group of non-singular forms is well defined.

## 6. The Witt Decomposition and the Witt Index

**Theorem (Witt decomposition).** Let $\operatorname{char} F \neq 2$ and $(V, q)$ be non-degenerate. Then there are an integer $m \geq 0$ and an anisotropic form $q_{\mathrm{an}}$, unique up to isometry, with

$$
q \cong \underbrace{H \perp \cdots \perp H}_{m} \perp \, q_{\mathrm{an}} = mH \perp q_{\mathrm{an}}.
$$

The integer $m$ is the **Witt index** $i_W(q)$; it is also the common dimension of all maximal totally isotropic subspaces of $V$.

**Proof.** Existence: split off a hyperbolic plane while the form is isotropic; the dimension decreases by $2$ and the form stays non-degenerate, so the process terminates at an anisotropic form. Uniqueness: cancel $H$ using §4. Since $mH$ contains an $m$-dimensional totally isotropic subspace and the anisotropic part contains none, $m$ is the maximal such dimension. $\square$

Properties:

- $q$ is anisotropic if and only if $m = 0$; $q$ is metabolic if and only if $m = \tfrac{1}{2} \dim V$, which forces $\dim V$ to be even.
- $m \le \lfloor \tfrac{1}{2} \dim V \rfloor$.
- $m$ is an isometry invariant, and base change to a field extension $E/F$ can only increase it: $i_W(q_E) \ge i_W(q)$. The increase can be strict: $x^2 + y^2$ has index $0$ over $\mathbb{R}$ but index $1$ over $\mathbb{C}$.

---

# Part III: The Witt Group and the Grothendieck–Witt Ring

## 7. The Witt Group

Fix a field $F$ of characteristic $\neq 2$ and write $[q]$ for the isometry class of a non-degenerate form. Orthogonal sum makes these classes a commutative monoid with identity the zero form. Declare

$$
q \sim q' \iff q \perp rH \cong q' \perp sH \ \text{ for some } r, s \ge 0;
$$

by Witt cancellation this is an equivalence relation compatible with $\perp$. The set $W(F)$ of classes, with addition $[q] + [q'] = [q \perp q']$, is the **Witt group** of $F$. The class of the zero form, and more generally of any metabolic form, is the identity, and the inverse of $[q]$ is $[-q]$, where $-q$ is $q$ scaled by $-1$: if $q \cong \langle a_1, \ldots, a_n\rangle$, then

$$
q \perp (-q) \cong \langle a_1, -a_1, \ldots, a_n, -a_n\rangle \cong nH.
$$

Since every form is diagonal, $W(F)$ is generated by the one-dimensional classes $[\langle a\rangle]$, and $[\langle a\rangle] = [\langle a c^2\rangle]$ for $c \in F^*$, so representatives of $F^*/(F^*)^2$ suffice. Dimension gives a surjective homomorphism $\dim : W(F) \to \mathbb{Z}/2$, since metabolic forms have even dimension; its kernel is the **fundamental ideal** $I(F)$ of even-dimensional classes. A form represents $0$ in $W(F)$ exactly when it is metabolic.

## 8. The Grothendieck–Witt Ring

The **Grothendieck–Witt ring** $GW(F)$ is the group completion of the monoid of isometry classes under $\perp$, made into a ring by the **tensor product of forms**

$$
(q \otimes q')(v \otimes w) = q(v)\, q'(w), \qquad \langle a_1, \ldots, a_m\rangle \otimes \langle b_1, \ldots, b_n\rangle = \langle a_i b_j\rangle .
$$

Since $\otimes$ preserves isometry and distributes over $\perp$, $GW(F)$ is a commutative ring with unit $[\langle 1\rangle]$, and dimension is a ring homomorphism to $\mathbb{Z}$, split by $n \mapsto n[\langle 1\rangle]$, so

$$
GW(F) \cong \mathbb{Z} \oplus I(F), \qquad I(F) = \ker(\dim).
$$

Passing to the Witt class is a surjective ring homomorphism $GW(F) \to W(F)$ whose kernel is generated by the hyperbolic class $[H] = [\langle 1, -1\rangle]$, since a metabolic form is a sum of hyperbolic planes. Hence

$$
W(F) \cong GW(F) / \mathbb{Z}[H].
$$

The product on $W(F)$ is well defined because tensoring a metabolic form with any form gives a metabolic form, so $W(F)$ is a commutative ring, the **Witt ring**, graded by dimension modulo $2$:

$$
W(F) = W_0 \oplus W_1, \qquad W_0 = I(F), \qquad W_1 = [\langle 1\rangle] + W_0, \qquad W(F)/I(F) \cong \mathbb{Z}/2.
$$

**The Witt relation.** For $a, b \in F^*$ with $a + b \neq 0$, the substitution $u = (ax + by)/(a+b)$, $v = (x - y)/(a+b)$ gives

$$
\langle a\rangle \perp \langle b\rangle \cong \langle a + b\rangle \perp \langle ab(a + b)\rangle ,
$$

so, writing $[a] = [\langle a\rangle]$,

$$
[a] + [b] = [a+b] + [ab(a+b)], \qquad [a][b] = [ab], \qquad [1] = 1.
$$

The classes $[a]$, $a \in F^*$, generate $GW(F)$ subject to these relations.

## 9. The Discriminant

Let $q$ be a non-degenerate form of dimension $n$ with Gram matrix $G$. The **discriminant** is

$$
\Delta(q) = \det(G) \in F^*/(F^*)^2,
$$

independent of the basis, since $G \mapsto P^T G P$ multiplies the determinant by $(\det P)^2$. For a diagonal form $\Delta(\langle a_1, \ldots, a_n\rangle) = a_1 \cdots a_n$, and

$$
\Delta(q \perp q') = \Delta(q)\, \Delta(q'), \qquad \Delta(q \otimes q') = \Delta(q)^{\dim q'}\, \Delta(q')^{\dim q}.
$$

It is not a Witt invariant, because $\Delta(H) = -1$. The **signed discriminant**

$$
d(q) = (-1)^{n(n-1)/2}\, \Delta(q)
$$

satisfies $d(H) = 1$, is unchanged by adding $H$, and is multiplicative on even-dimensional forms, so it descends to a homomorphism

$$
d : I(F) \longrightarrow F^*/(F^*)^2,
$$

surjective because $d(\langle 1, -a\rangle) = a$. Its kernel is $I(F)^2$, so

$$
I(F)/I(F)^2 \cong F^*/(F^*)^2.
$$

The discriminant is not complete: over $\mathbb{Q}$, $\langle 1, 1\rangle$ and $\langle -1, -1\rangle$ both have discriminant $1$ but signatures $2$ and $-2$, so they are not isometric.

## 10. The Hasse Invariant

For $q \cong \langle a_1, \ldots, a_n\rangle$ over a field of characteristic $\neq 2$, the **Hasse invariant**, also called the **Hasse–Witt** or **Clifford invariant**, is

$$
c(q) = \prod_{1 \le i < j \le n} (a_i, a_j) \in \operatorname{Br}_2(F),
$$

where $(a, b)$ is the class of the quaternion algebra $(a, b)_F$ in the Brauer group, and $\operatorname{Br}_2(F) = \{x \in \operatorname{Br}(F) : 2x = 0\}$. It is independent of the diagonalization, $c(\langle a\rangle) = 1$, and $c(H) = 1$, so it is a Witt invariant. Under orthogonal sums,

$$
c(q \perp q') = c(q)\, c(q')\, \bigl(\Delta(q), \Delta(q')\bigr),
$$

so $c$ is additive on even-dimensional classes of trivial discriminant. Over $\mathbb{R}$, with signature $(p, r)$, one has $(a_i, a_j) = -1$ exactly when both entries are negative, hence

$$
c(q) = (-1)^{r(r-1)/2},
$$

so $c$ is determined by the signature and adds nothing there. The discriminant and Hasse invariant are the first two cohomological invariants of a quadratic form, taking values in $H^1(F, \mu_2) = F^*/(F^*)^2$ and $H^2(F, \mu_2) = \operatorname{Br}_2(F)$.

---

# Part IV: Witt Groups of Fields and Classification

## 11. The Real and Complex Witt Groups

Over $\mathbb{R}$, Sylvester's law of inertia states that $q \cong \langle 1^p, (-1)^r\rangle$ with $p, r \ge 0$ determined by $q$; the **signature** is $\sigma(q) = p - r$. Orthogonal sum adds signatures and tensor product multiplies them, so

$$
W(\mathbb{R}) \cong \mathbb{Z}, \qquad [q] \mapsto \sigma(q),
$$

is an isomorphism of rings, with fundamental ideal $I(\mathbb{R}) = 2\mathbb{Z}$. The Hasse invariant is redundant here.

Over $\mathbb{C}$ every nonzero coefficient is a square, $\lambda = \mu^2$, and can be removed by rescaling, so every non-degenerate form is isometric to $n\langle 1\rangle$ with $n = \dim q$; it is metabolic exactly when $n$ is even. Hence

$$
W(\mathbb{C}) \cong \mathbb{Z}/2, \qquad [q] \mapsto \dim q \bmod 2,
$$

which is likewise a ring isomorphism.

For a field extension $E/F$, base change is a ring homomorphism $W(F) \to W(E)$, $[q] \mapsto [q_E]$; for $\mathbb{R} \subset \mathbb{C}$ it is $\sigma \mapsto \sigma \bmod 2$, with kernel $I(\mathbb{R})$.

## 12. The Witt Group of the Rationals

Let $\mathbb{Q}_p$ be the field of $p$-adic numbers and set $\mathbb{Q}_\infty = \mathbb{R}$.

**Hasse–Minkowski theorem.** Non-degenerate quadratic forms $q, q'$ over $\mathbb{Q}$ are isometric if and only if they are isometric over $\mathbb{Q}_v$ for every place $v$.

The local data are the signature at the real place and the dimension, discriminant, and Hasse invariant at each finite prime, so

$$
W(\mathbb{Q}) \longrightarrow W(\mathbb{R}) \times \prod_p W(\mathbb{Q}_p)
$$

is injective: a form is metabolic over $\mathbb{Q}$ exactly when it is metabolic over every completion. Here $W(\mathbb{R}) \cong \mathbb{Z}$ and $W(\mathbb{Q}_p)$ is finite for each prime. Over a finite field $\mathbb{F}_q$ with $q$ odd the Hasse invariant is trivial, so forms are classified by dimension modulo $2$ and discriminant, and

$$
W(\mathbb{F}_q) \cong
\begin{cases}
\mathbb{Z}/4, & q \equiv 3 \pmod 4,\\
\mathbb{Z}/2 \times \mathbb{Z}/2, & q \equiv 1 \pmod 4.
\end{cases}
$$

The image is cut out by Hilbert reciprocity: for all $a, b \in \mathbb{Q}^*$, only finitely many $(a, b)_v$ differ from $1$, and $\prod_v (a, b)_v = 1$. Since $\mathbb{Q}^*/\mathbb{Q}^{*2}$ is generated by $-1$ and the primes, $W(\mathbb{Q})$ is generated as a ring by the classes $[\langle -1\rangle]$ and $[\langle p\rangle]$, $p$ prime; the signature gives a surjection $W(\mathbb{Q}) \to \mathbb{Z}$.

## 13. Classification of Non-Degenerate Forms

Witt's theorems reduce the classification to the Witt index and the anisotropic part, which is unique up to isometry. Over the fields of arithmetic the anisotropic part is governed by the following complete invariants.

| Field $F$ | Complete invariants of a non-degenerate form | $W(F)$ |
|---|---|---|
| algebraically closed (e.g. $\mathbb{C}$) | dimension $n$ | $\mathbb{Z}/2$ |
| $\mathbb{R}$ | signature $(p, r)$ | $\mathbb{Z}$ |
| finite field $\mathbb{F}_q$, $q$ odd | $n \bmod 2$ and $\Delta \in \mathbb{F}_q^*/(\mathbb{F}_q^*)^2$ | $\mathbb{Z}/4$ if $q \equiv 3 \pmod 4$, $\mathbb{Z}/2 \times \mathbb{Z}/2$ if $q \equiv 1 \pmod 4$ |
| local field $\mathbb{Q}_p$, $p$ odd | dimension, discriminant, Hasse invariant | finite |
| $\mathbb{Q}$ | local–global (Hasse–Minkowski): signature at $\infty$, $(n, \Delta, c)$ at each finite prime | — |

- In dimension $1$ the discriminant is complete; in dimension $2$ it is not, and the Hasse invariant is needed as well.
- Over a non-archimedean local field the triple (dimension, discriminant, Hasse invariant) is complete; over a global field the same triple at each completion, together with the signature, is complete (Hasse–Minkowski).
- Over a general field, $n$, $\Delta$, and $c$ are only the first invariants: $\Delta$ accounts for $I/I^2$ and $c$ for $I^2/I^3$, with higher invariants in the higher quotients $I^n/I^{n+1}$; there is no finite complete list, but Witt's theorems still reduce the problem to anisotropic forms.

## 14. Witt Theory and Clifford Algebras

Let $q$ be a non-degenerate form of dimension $n$. The **Clifford algebra** $C(q)$ is the quotient of the tensor algebra $T(V)$ by the ideal generated by the elements $v \otimes v - q(v) \cdot 1$. For $q \cong \langle a_1, \ldots, a_n\rangle$ it is generated by $e_1, \ldots, e_n$ subject to

$$
e_i^2 = a_i, \qquad e_i e_j = -e_j e_i \quad (i \neq j).
$$

It is $\mathbb{Z}/2$-graded, $C(q) = C_0(q) \oplus C_1(q)$, with $\dim C(q) = 2^n$ and $\dim C_0(q) = 2^{n-1}$, and orthogonal sums correspond to graded tensor products:

$$
C(q \perp q') \cong C(q) \, \hat{\otimes} \, C(q'), \qquad C_0(q \perp q') \cong C_0(q) \otimes C_0(q') \oplus C_1(q) \otimes C_1(q').
$$

The Hasse invariant is its Brauer class. For even $n$, $C(q)$ is central simple over $F$ and $c(q) = [C(q)]$; for odd $n$, $C_0(q)$ is central simple over $F$ and $c(q) = [C_0(q)]$. The discriminant appears as the center: for odd $n$,

$$
Z(C(q)) = F\bigl[\sqrt{d(q)}\bigr],
$$

so $C(q)$ is central over $F$ exactly when the discriminant is trivial.

The two invariants are the first two steps of the filtration of $W(F)$ by powers of the fundamental ideal: the discriminant gives $I/I^2 \cong F^*/(F^*)^2$, and the Hasse invariant induces $I^2/I^3 \cong \operatorname{Br}_2(F)$, a theorem of Merkurjev. Over $\mathbb{R}$ this filtration detects the signature only modulo powers of $2$, which is why the signature, not these invariants, is complete there.

---

# Part V: Summary

## 15. Summary

Throughout, $F$ has characteristic $\neq 2$ and forms are finite-dimensional and non-degenerate.

- A form has polar form $b(x, y) = \tfrac{1}{2}(q(x + y) - q(x) - q(y))$; the pair $(q, b)$ is determined by either member, and every non-degenerate form is diagonal.
- **Witt's lemma and extension theorem:** equal nonzero norms are related by at most two reflections; an isometry between subspaces of a non-degenerate space extends to the whole space.
- **Hyperbolic plane** $H = \langle 1, -1\rangle$; **metabolic** spaces are sums of hyperbolic planes, equivalently have a Lagrangian.
- **Witt cancellation:** $q_1 \perp q \cong q_2 \perp q$ with $q$ non-degenerate implies $q_1 \cong q_2$. It fails in characteristic $2$: $\langle 1, 1\rangle \perp \langle 1\rangle \cong \langle 0, 0\rangle \perp \langle 1\rangle$, yet $\langle 1, 1\rangle \not\cong \langle 0, 0\rangle$.
- **Witt decomposition:** $q \cong mH \perp q_{\mathrm{an}}$, uniquely, with $m$ the **Witt index**, the common dimension of maximal totally isotropic subspaces.
- **Witt group and Grothendieck–Witt ring:** $W(F)$ is isometry classes modulo metabolic forms under $\perp$, generated by one-dimensional classes, with $W(F) \to \mathbb{Z}/2$ having kernel the fundamental ideal $I(F)$; $GW(F)$ adds $\otimes$, with $GW(F) \cong \mathbb{Z} \oplus I(F)$ and $W(F) \cong GW(F)/\mathbb{Z}[H]$.
- **Discriminant and Hasse invariant:** $\Delta(q) = \det(\mathrm{Gram}) \in F^*/(F^*)^2$, whose signed form gives $I/I^2 \cong F^*/(F^*)^2$, and $c(q) = \prod_{i<j}(a_i, a_j) \in \operatorname{Br}_2(F)$, the Clifford invariant, giving $I^2/I^3 \cong \operatorname{Br}_2(F)$.
- **Real, complex, rational:** $W(\mathbb{R}) \cong \mathbb{Z}$ by signature, $W(\mathbb{C}) \cong \mathbb{Z}/2$ by dimension modulo $2$, and $W(\mathbb{Q})$ embeds into $W(\mathbb{R}) \times \prod_p W(\mathbb{Q}_p)$ by Hasse–Minkowski, generated by $[\langle -1\rangle]$ and $[\langle p\rangle]$.
- **Classification:** over $\mathbb{R}$ by signature; over local and global fields by dimension, discriminant, and Hasse invariant; over a general field by the Witt index and the anisotropic part.

---

## Further Reading

- Ernst Witt, "Theorie der quadratischen Formen in beliebigen Körpern", *Journal für die reine und angewandte Mathematik* 176 (1937), 31–44. The founding paper.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67, American Mathematical Society, 2005.
- John Milnor and Dale Husemoller, *Symmetric Bilinear Forms*, Ergebnisse der Mathematik 73, Springer, 1973.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270, Springer, 1985.
- Richard Elman, Nikita Karpenko and Alexander Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms*, Colloquium Publications 56, American Mathematical Society, 2008.
- O. Timothy O'Meara, *Introduction to Quadratic Forms*, Grundlehren der mathematischen Wissenschaften 117, Springer, 1973.
- Jean-Pierre Serre, *A Course in Arithmetic*, Graduate Texts in Mathematics 7, Springer, 1973. For the Hasse–Minkowski theorem over $\mathbb{Q}$.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294, Springer, 1991.
- Martin Kneser, *Quadratische Formen*, Springer, 2002.
