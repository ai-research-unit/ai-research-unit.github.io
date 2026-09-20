
# __Quadratic Forms over Algebras__

## Introduction

This article treats quadratic forms whose values lie in an algebra, and quadratic forms defined over an algebra. It continues the articles *Bilinear and Quadratic Forms* and *Algebras*. The treatment is introductory and purely mathematical, and we assume familiarity with modules, algebras, bilinear forms, and quadratic forms.

Two notions must be separated at the outset.

- A quadratic form **with values in an algebra** $A$ is an object over a commutative ring $R$: a function $q : M \to A$ on an $R$-module, where $A$ is an $R$-algebra. The algebra need not be commutative, and the form is required to be only $R$-linear, not $A$-linear. The quaternion and biquaternion norm forms are the standard examples.
- A quadratic form **over an algebra** $A$ is a quadratic form over the ring $A$, in the sense of *Bilinear and Quadratic Forms*, when $A$ is commutative: the algebra is the ring of scalars.

When $A$ is commutative and $M$ is an $A$-module the two notions coincide. Working over a **commutative ring** $R$ with values in an $R$-algebra $A$, the differences from the field case are: the values may be noncommutative; polarization requires 2 invertible in $R$; when 2 is not invertible a quadratic form is not determined by its associated bilinear form; and $A$ may have zero divisors, so a form may vanish on nonzero vectors.

---

# Part I: Quadratic Forms and Their Polar Forms

## 1. Quadratic Forms with Values in an Algebra

Let $R$ be a commutative ring, let $A$ be an $R$-algebra, not assumed commutative, and let $M$ be an $R$-module. A function $q : M \to A$ is a **quadratic form on $M$ with values in $A$** if it is homogeneous of degree 2,

$$
q(rv) = r^2 q(v) \qquad (r \in R,\; v \in M),
$$

and its **polar form**

$$
B(u,v) = \tfrac{1}{2}\bigl(q(u+v) - q(u) - q(v)\bigr)
$$

is $R$-bilinear. Then $B$ is symmetric, and $q(v) = B(v,v)$, because

$$
B(v,v) = \tfrac{1}{2}\bigl(q(2v) - 2q(v)\bigr) = \tfrac{1}{2}\bigl(4q(v) - 2q(v)\bigr) = q(v).
$$

Conversely, if $B : M \times M \to A$ is symmetric and $R$-bilinear, then $q(v) = B(v,v)$ is a quadratic form with polar form $B$, since $\tfrac12\bigl(B(u+v,u+v) - B(u,u) - B(v,v)\bigr) = \tfrac12\bigl(B(u,v) + B(v,u)\bigr) = B(u,v)$. Hence when 2 is invertible in $R$ there is a bijection between quadratic forms $q : M \to A$ and symmetric $R$-bilinear forms $B : M \times M \to A$.

The form $B$ is only $R$-linear: we do not require $B(av,w) = a\,B(v,w)$ for $a \in A$. This is the difference between values **in** $A$ and forms **over** $A$. If $A$ is commutative and $M$ is an $A$-module, one may additionally require $A$-linearity, and the two theories coincide.

**Example.** For $A = R$ this reduces to *Bilinear and Quadratic Forms*.

**Key difference from the field case.** Over a field of characteristic not 2, 2 is automatically invertible; over a ring we must assume it, and over a noncommutative algebra values in and forms over the algebra become genuinely different notions.

## 2. The Associated Bilinear Form and the Quadric

The **associated bilinear form** is

$$
b(u,v) = q(u+v) - q(u) - q(v),
$$

symmetric and $R$-bilinear, with $b = 2B$ and $b(v,v) = 2q(v)$. Over a ring in which 2 is not invertible, $b$ is the natural object and $q$ is genuinely more than $b$ (Section 8).

Suppose now that $A$ is commutative and $M$ is free of finite rank. The **quadric** of $q$ is the set of points

$$
Q(q) = \{[v] \in \mathbb{P}(M) : q(v) = 0\},
$$

together with the affine cone over it. Its bilinear part is the polar form: along a line $su + tv$,

$$
q(su + tv) = s^2 q(u) + 2st\,B(u,v) + t^2 q(v),
$$

so $B(u,v)$ decides how the line meets the quadric. Over a field with 2 invertible and $q$ nondegenerate, the quadric and the polar form determine each other. For the determinant form on $M_2(\mathbb{C})$, the quadric is the set of singular matrices, the smooth quadric surface $\mathbb{P}^1 \times \mathbb{P}^1$ in $\mathbb{P}^3(\mathbb{C})$; the same quadric is the zero locus of the biquaternion norm form (Section 7).

## 3. Isometries and Similarities

The definitions of the preceding articles do not use commutativity of the values, so they carry over to $A$-valued forms.

An $R$-linear isomorphism $f : M \to M$ is an **isometry** of $q$ if $q(fv) = q(v)$ for all $v$, equivalently (when 2 is invertible) if $B(fu,fv) = B(u,v)$ for all $u,v$. The isometries form the **orthogonal group** $O(M,q)$. A **similarity** is an $R$-linear isomorphism with $q(fv) = \lambda q(v)$ for some multiplier $\lambda \in R^\times$; if $q$ is not identically zero the multiplier is unique, and $f \mapsto \lambda$ is a homomorphism $GO(M,q) \to R^\times$ with kernel $O(M,q)$, where $GO(M,q)$ is the **similarity group**.

Over a field $F$ with $q$ nondegenerate, $O(M,q)$ is the classical orthogonal group; if in addition $\operatorname{char} F \ne 2$, every isometry satisfies $\det(f)^2 = 1$, and the kernel of the determinant is the **special orthogonal group** $SO(M,q)$ (see *Orthogonal Transformations*).

---

# Part II: Composition and Norm Forms

## 4. Composition of Quadratic Forms

Let $A$ be an $R$-algebra, and let $q_1, q_2, q_3$ be $A$-valued quadratic forms on $M_1, M_2, M_3$. A **composition** of $q_1$ and $q_2$ into $q_3$ is a bilinear map $\varphi : M_1 \times M_2 \to M_3$ with

$$
q_3\bigl(\varphi(x,y)\bigr) = q_1(x)\,q_2(y).
$$

For the standard sums of squares on $A^m, A^n, A^p$, this is a **sum-of-squares identity**. The **Hurwitz problem** asks, over $A = \mathbb{R}$, for which triples $(m,n,p)$ such a bilinear identity exists.

**The square case.** If $m = n = p$, a composition exists if and only if $n \in \{1,2,4,8\}$. This is **Hurwitz's theorem**, the four values corresponding to $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$; the identities are the one-square, two-square (Diophantus), four-square (Euler) and eight-square (Degen) identities.

**The general case.** For fixed $n$, the largest $m$ for which a bilinear map $\mathbb{R}^m \times \mathbb{R}^n \to \mathbb{R}^n$ satisfies $|xy| = |x|\,|y|$ for the Euclidean norms is the **Hurwitz–Radon number**

$$
\rho(n) = 8a + 2^b, \qquad n = (2u+1)\,2^{4a+b}, \qquad 0 \le b \le 3,
$$

which also governs the maximal number of linearly independent vector fields on $S^{n-1}$. The square case is the statement that $\rho(n) \ge n$ only for $n \in \{1,2,4,8\}$, with equality.

A composition need not come from an algebra: $\varphi$ is only required to be bilinear.

## 5. Composition Algebras and Hurwitz's Theorem

A **composition algebra** over a field $F$ is an $F$-algebra $A$, not assumed associative or commutative, with a nondegenerate quadratic form $N$ satisfying

$$
N(xy) = N(x)\,N(y).
$$

If $A$ has a unit then $N(1) = 1$: indeed $N(1) = N(1)^2$, and $N(1) = 0$ would force $N \equiv 0$.

**Theorem (Hurwitz).** A composition algebra over a field has dimension $1, 2, 4$ or $8$. Over a field of characteristic not 2, a unital composition algebra is isomorphic to $F$, to a quadratic étale algebra, to a quaternion algebra, or to an octonion algebra. A quadratic étale algebra is a quadratic field extension or $F \times F$; quaternion and octonion algebras are defined in *Algebras*.

Every unital composition algebra carries a **conjugation** $x \mapsto \bar{x}$ with $\overline{xy} = \bar{y}\,\bar{x}$ and

$$
x\bar{x} = \bar{x}x = N(x)\cdot 1,
$$

so $x$ is invertible if and only if $N(x) \ne 0$, with $x^{-1} = \bar{x}/N(x)$. Over $\mathbb{R}$ the **division** composition algebras are $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ (dimensions $1,2,4,8$, anisotropic norms), and the **split** ones are $\mathbb{R} \times \mathbb{R}$, $M_2(\mathbb{R})$, and the split octonions (isotropic norms, zero divisors); by the Frobenius theorem the associative real division algebras are $\mathbb{R}, \mathbb{C}, \mathbb{H}$.

**Key difference from the field case.** The dimension theorem holds over any field, but the classification is characteristic-sensitive: in characteristic 2 quadratic étale algebras degenerate and separate constructions appear, so the classification above is stated for characteristic not 2. Non-unital composition algebras also exist and can have zero divisors.

## 6. Norm Forms of Algebras

For a finite-dimensional unital associative algebra $A$ over a field $F$, with $m_x(y) = xy$ the left multiplication by $x$, the **regular norm** is

$$
N(x) = \det(m_x).
$$

It is homogeneous of degree $n = \dim_F A$ and multiplicative, because $m_{xy} = m_x m_y$; it is therefore quadratic precisely when $n = 2$. For a **central simple** algebra $A$ the **reduced norm** $\operatorname{Nrd}$ has degree $d = \sqrt{\dim_F A}$ and $d$-th power the regular norm; it is quadratic precisely when $d = 2$, that is, for a quaternion algebra. Likewise the **field norm** $N_{K/F}(x) = \det(m_x)$ of an extension of degree $n$ is quadratic precisely when $n = 2$. For a **composition algebra** the norm is structural, defined by $N(xy) = N(x)N(y)$ rather than by a determinant; this is why octonions have a quadratic norm.

## 7. Norm Forms of Fields, Quaternion Algebras, and Biquaternions

### Quadratic field extensions

Let $K = F(\sqrt{d})$ with $\operatorname{char} F \ne 2$ and $d$ a non-square. For $x = a + b\sqrt{d}$,

$$
N_{K/F}(x) = x\bar{x} = a^2 - d\,b^2,
$$

a nondegenerate binary form; left multiplication by $x$ has determinant $N_{K/F}(x)$. The **norm-one group** $K^1 = \{x \in K^\times : N_{K/F}(x) = 1\}$ acts by multiplication as isometries, and

$$
SO(K, N_{K/F}) \cong K^1, \qquad O(K, N_{K/F}) \cong K^1 \rtimes \langle \sigma \rangle,
$$

where $\sigma(x) = \bar{x}$ is a determinant $-1$ isometry.

### Quaternion algebras

For a quaternion algebra $D$ over $F$, $\operatorname{char} F \ne 2$, with $N(x) = x\bar{x}$, the norm is a nondegenerate quadratic form of dimension 4 and

$$
N(xy) = N(x)\,N(y).
$$

An explicit basis makes $N$ diagonal, so multiplicativity is a four-square identity. The algebra $D$ is a division algebra if and only if $N$ is anisotropic; otherwise $N$ is isotropic and $D \cong M_2(F)$ with $N = \det$. For $\alpha, \beta \in D^\times$ the map $x \mapsto \alpha x\beta$ satisfies $N(\alpha x\beta) = N(\alpha)N(x)N(\beta)$, so it is an isometry exactly when $N(\alpha)N(\beta) = 1$; its determinant is $\bigl(N(\alpha)N(\beta)\bigr)^2 = 1$, so it lies in $SO(N)$. These maps generate $SO(N)$, the **main involution** $x \mapsto \bar{x}$ is a determinant $-1$ isometry, and

$$
O(D,N) = \bigl\langle SO(D,N),\; \bar{\cdot}\,\bigr\rangle.
$$

For the split algebra $D = M_2(F)$ this says that $SO(\det)$ is generated by $x \mapsto axb$ with $\det(a)\det(b) = 1$, and $O(\det)$ is generated by these together with transposition.

### Biquaternions

For $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} \cong M_2(\mathbb{C})$, the norm form

$$
N(\tilde{Q}) = \tilde{Q}\,\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2
$$

is the reduced norm, that is, the determinant: a nondegenerate quadratic form with values in $\mathbb{C}$, multiplicative, and the standard form in suitable coordinates over $\mathbb{C}$. It is isotropic, with zero locus the singular quadric of Section 2, and its nonzero zeros are exactly the zero divisors of $\mathbb{B}$. The form is not real-valued on $\mathbb{B}$. On the quaternion subspace $\mathbb{H}_{\mathbb{B}} \cong \mathbb{R}^4$ it restricts to the positive definite form $q_0^2 + q_1^2 + q_2^2 + q_3^2$; on the four-dimensional subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ it restricts to the Lorentzian forms of signature $(1,3)$ and $(3,1)$, whose isometry group is the full Lorentz group $O(1,3)$. The elements of norm one form a group isomorphic to $SL(2,\mathbb{C})$, which acts by left and right multiplication and covers $SO^+(1,3)$ twice. Details are in *Biquaternion Norm and Invertibility* and *Biquaternion Zero Divisors*.

**Key difference from the field case.** Over a field, an anisotropic norm form makes the algebra a division algebra; over a commutative ring with zero divisors it does not, as the $\mathbb{C}$-valued biquaternion norm shows. The biquaternion norm form is a form over the commutative ring $\mathbb{C}$, while the real subspaces are studied by restricting scalars.

---

# Part III: Rings, Involution, and Hermitian Forms

## 8. Quadratic Forms over Rings Where 2 Is Not Invertible

Over a ring in which 2 is not invertible, the polar form must be replaced by the associated bilinear form, and the two notions separate.

Let $R$ be a commutative ring. A **quadratic form** on an $R$-module $M$ is a function $q : M \to R$ with $q(rv) = r^2 q(v)$ for all $r, v$, such that

$$
b(u,v) = q(u+v) - q(u) - q(v)
$$

is $R$-bilinear. Then $b$ is symmetric and $b(v,v) = q(2v) - 2q(v) = 2q(v)$. If 2 is invertible, $q(v) = \tfrac12 b(v,v)$ recovers $q$ from $b$; otherwise $b$ need not determine $q$.

The obstruction is 2-torsion. If $q_1, q_2$ have the same associated bilinear form, then $d = q_1 - q_2$ is additive with $d(rv) = r^2 d(v)$. Comparing the two evaluations of $d\bigl((r+1)v\bigr)$ gives

$$
2r\,d(v) = 0,
$$

in particular $2d(v) = 0$. So if 2 is not a zero divisor in $R$, then $d = 0$ and $q \mapsto b$ is injective; if 2 is a zero divisor, distinct quadratic forms may share the same bilinear form.

**Example.** Over $\mathbb{F}_2$, the forms $q_0(x) = 0$ and $q_1(x) = x^2$ on $\mathbb{F}_2$ both have $b(x,y) = (x+y)^2 - x^2 - y^2 = 0$, because $(x+y)^2 = x^2 + y^2$ in characteristic 2; the same happens over $\mathbb{Z}/2\mathbb{Z}$ and over any algebra in which 2 is a zero divisor. For the dual-number algebra $\mathbb{F}_2[\varepsilon]/(\varepsilon^2) \cong \mathbb{F}_2[C_2]$, the norm form

$$
N(a + b\varepsilon) = (a + b\varepsilon)(a - b\varepsilon) = a^2
$$

is nonzero while its associated bilinear form vanishes identically, because $2 = 0$: the extreme case in which $b$ carries no information.

## 9. Sesquilinear and Hermitian Forms Relative to an Involution

Let $A$ be a ring, possibly noncommutative, with an **involution** $\sigma$, meaning $\sigma(a+b) = \sigma(a)+\sigma(b)$, $\sigma(ab) = \sigma(b)\sigma(a)$, $\sigma \circ \sigma = \mathrm{id}$ and $\sigma(1) = 1$. Let $M$ be a **right** $A$-module. A function $s : M \times M \to A$ is **$\sigma$-sesquilinear** if it is additive in each argument and

$$
s(xa,\, yb) = \sigma(a)\, s(x,y)\, b,
$$

and **$\sigma$-Hermitian** if $s(y,x) = \sigma(s(x,y))$; it is $\sigma$-skew-Hermitian if $s(y,x) = -\sigma(s(x,y))$. With $\sigma = \mathrm{id}$ and $A$ commutative these are the symmetric and alternating bilinear forms.

The **diagonal** $q(x) = s(x,x)$ of a Hermitian form takes values in the fixed ring $A^\sigma = \{a : \sigma(a) = a\}$ and satisfies $q(xa) = \sigma(a)q(x)a$; in particular, for $a$ central in $A$ and fixed by $\sigma$, $q(xa) = a^2 q(x)$, so on central scalars $q$ is a quadratic form over the fixed ring $A^\sigma$. Its polar form is the **trace** of $s$:

$$
q(x+y) - q(x) - q(y) = s(x,y) + s(y,x) = s(x,y) + \sigma(s(x,y)).
$$

**Examples.** For $A = \mathbb{C}$ with complex conjugation, $s(z,w) = \sum_i \bar{z}_i w_i$ on $\mathbb{C}^n$ has diagonal $q(z) = \sum_i |z_i|^2$, and the isometry group of a nondegenerate Hermitian form is the **unitary group** $U(M,s)$, equal to $U(n)$ for the standard form. For $A = \mathbb{H}$ with quaternion conjugation, $s(x,y) = \bar{x}y$ is Hermitian with diagonal the quaternion norm; more generally the norm of any composition algebra is the diagonal of $s(x,y) = \bar{x}y$. The trivial involution recovers symmetric bilinear forms, and over a division ring with an involution the isometry groups are again unitary groups, with a Witt extension theorem under the usual trace hypotheses (Section 13).

## 10. Trace Forms and Reduced Norms

For a finite-dimensional unital associative algebra $A$ over a field $F$, with $m_x$ the left multiplication by $x$, the **trace form** is

$$
T(x,y) = \operatorname{Tr}(m_{xy}) = \operatorname{Tr}(m_x m_y),
$$

symmetric bilinear, with associated quadratic form $q_T(x) = \operatorname{Tr}(x^2)$ when $\operatorname{char} F \ne 2$. For a field extension it is $T(x,y) = \operatorname{Tr}_{K/F}(xy)$.

The trace form is generally not the polar form of the norm form. For $K = F(\sqrt{d})$,

$$
T(x,x) = \operatorname{Tr}(x^2) = 2(a^2 + d\,b^2), \qquad N_{K/F}(x) = a^2 - d\,b^2,
$$

already different in dimension 2. For a quaternion algebra with $N(x) = x\bar{x}$, the polar form of $N$ is

$$
B_N(x,y) = \tfrac{1}{2}\bigl(N(x+y) - N(x) - N(y)\bigr) = \tfrac{1}{2}\bigl(x\bar{y} + y\bar{x}\bigr) = \tfrac{1}{2}\operatorname{Trd}(x\bar{y}),
$$

distinct from $T(x,y) = \operatorname{Trd}(xy)$. For a central simple algebra of degree $d$, the **reduced trace form** $(x,y) \mapsto \operatorname{Trd}(xy)$ is symmetric bilinear, and the **reduced norm** is a form of degree $d$, quadratic precisely when $d = 2$; then it is the norm form of Section 7.

**Key difference from the field case.** Over a commutative ring, traces require a free module of finite rank, and reduced traces and norms require the usual hypotheses on the base (an Azumaya algebra); the canonical forms attached to an algebra are sensitive to the base ring.

---

# Part IV: Clifford Algebras, Orthogonal Groups, and Witt's Theorems

## 11. The Clifford Algebra of a Form on a Module

Let $R$ be a commutative ring, $M$ an $R$-module, and $Q : M \to R$ a quadratic form with polar form $B$. The **Clifford algebra** $Cl(M,Q)$ is the quotient of the tensor algebra $T(M)$ by the two-sided ideal generated by the elements $v \otimes v - Q(v)\cdot 1$; equivalently, it is the associative unital $R$-algebra generated by $M$ subject to

$$
v^2 = Q(v)\cdot 1.
$$

It has the universal property that every $R$-linear map $f : M \to A$ into a unital associative $R$-algebra with $f(v)^2 = Q(v)\cdot 1_A$ extends uniquely to an algebra homomorphism $Cl(M,Q) \to A$. It is $\mathbb{Z}/2$-graded, with even part $Cl^0$ and odd part $Cl^1$. When 2 is invertible, the polarization identity turns the defining relation into the **Clifford relations**

$$
uv + vu = 2B(u,v)\cdot 1.
$$

The construction, radical, and classification are in *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*. A form with values in a general noncommutative algebra has no such construction, because the relation requires $Q(v)$ to be central.

## 12. The Orthogonal Group and the Clifford Group

An isometry $f \in O(M,q)$ preserves $q$ and therefore extends, by the universal property, to a grading-preserving algebra automorphism of $Cl(M,q)$:

$$
O(M,q) \longrightarrow \operatorname{Aut}\bigl(Cl(M,q)\bigr).
$$

Conversely, units of the Clifford algebra act on $M$ by conjugation. Let $\alpha$ be the **grade involution**, which multiplies $Cl^1$ by $-1$ and fixes $Cl^0$. The **Clifford group** is

$$
\Gamma(M,q) = \bigl\{ s \in Cl(M,q)^\times : sMs^{-1} \subseteq M \bigr\},
$$

and the **grade-twisted adjoint** $\rho(s)(v) = \alpha(s)\,v\,s^{-1}$ maps $\Gamma(M,q)$ into $O(M,q)$. When $q$ is nondegenerate, $\rho$ is surjective with kernel $R^\times$; the **Pin group**, generated by the unit vectors, is a double cover of $O(M,q)$, and its even part is the **Spin group**, a double cover of $SO(M,q)$. Indeed, a non-isotropic vector $v$ gives the reflection

$$
s_v(u) = u - \frac{2B(u,v)}{Q(v)}\,v,
$$

realized by $\rho(v)$, and over a field of characteristic not 2 every isometry is a product of reflections (the Cartan–Dieudonné theorem). See *Spinors*.

## 13. Witt's Theorems Where They Apply

Let $F$ be a field of characteristic not 2 and $(V,Q)$ a finite-dimensional nondegenerate quadratic space, with polar form $B$ and reflections $s_v(u) = u - \frac{2B(u,v)}{Q(v)}v$.

**Extension.** Every isometry between two subspaces of $V$ extends to an isometry of $V$.

**Cancellation.** If $V_1 \perp V_2 \cong V_1 \perp V_3$ and $V_1$ is nondegenerate, then $V_2 \cong V_3$. Hence the isometry classes of nondegenerate quadratic forms form a cancellation monoid under orthogonal direct sum, whose group completion is the **Grothendieck–Witt group** $GW(F)$, and whose quotient by the hyperbolic forms is the **Witt group** $W(F)$; the Witt group and ring are treated in *Witt Theory*.

**Decomposition.** Every nondegenerate quadratic space over $F$ decomposes as $V \cong V_0 \perp k\,\mathbb{H}$, with $V_0$ anisotropic, $\mathbb{H} = \langle 1, -1\rangle$ the hyperbolic plane, and $k$ the **Witt index**; the decomposition is unique up to isometry of $V_0$ and the value of $k$.

**Similarities and Hermitian case.** The extension theorem holds for similarities with the same multiplier, so $GO(V,Q)$ has the same rigidity. Over a division ring with an involution, extension and cancellation hold for nondegenerate Hermitian forms under the usual trace hypotheses in characteristic 2, with unitary isometry groups.

**Key difference from the field case.** Over a general commutative ring these theorems can fail, because a nondegenerate submodule need not be a direct summand and because nondegeneracy is stronger than the vanishing of the radical. The replacement is the theory of quadratic modules built from the definitions of Section 8; see *Witt Theory*.

---

## Summary

**A form with values in an algebra** $A$ is a function $q : M \to A$, homogeneous of degree 2, whose polar form $B(u,v) = \tfrac12(q(u+v)-q(u)-q(v))$ is $R$-bilinear; then $q(v) = B(v,v)$, and when 2 is invertible this gives a bijection with symmetric $R$-bilinear forms with values in $A$. The associated bilinear form is $b = 2B$, and the quadric of $q$ is its zero locus, with $B$ the bilinear part of its equation. Isometries form $O(M,q)$, and similarities form $GO(M,q)$ with multiplier in $R^\times$.

**Composition** is a bilinear $\varphi$ with $q_3(\varphi(x,y)) = q_1(x)q_2(y)$; in the square case the Hurwitz problem has solutions only for $1,2,4,8$, and the Hurwitz–Radon numbers govern the general case. **Composition algebras** are algebras with a nondegenerate multiplicative quadratic norm; a unital one over a field of characteristic not 2 has dimension $1,2,4,8$ and is a field, a quadratic étale algebra, a quaternion algebra, or an octonion algebra.

**Norm forms** are quadratic only in special dimensions: the regular norm and the field norm in dimension 2, the reduced norm for quaternion algebras, and the norm of a composition algebra by definition. The isometry groups are described in Section 7: for a quadratic extension $SO \cong K^1$ and $O$ adds conjugation; for a quaternion algebra $SO$ is generated by $x \mapsto \alpha x\beta$ with $N(\alpha)N(\beta)=1$ and $O$ adds the main involution; for the biquaternions the norm is $\mathbb{C}$-valued and isotropic, its Lorentzian restrictions have isometry group $O(1,3)$, and the norm-one group is $SL(2,\mathbb{C})$.

**Hermitian forms** relative to an involution have quadratic diagonals over the fixed ring and give the unitary groups. The **Clifford algebra** $Cl(M,Q)$, universal for $v^2 = Q(v)$, has units acting by the grade-twisted adjoint, yielding the Clifford, Pin and Spin groups. **Witt's** extension, cancellation and decomposition theorems hold for nondegenerate forms over fields of characteristic not 2, and for Hermitian forms over division rings under trace hypotheses; over general rings they require the theory of quadratic modules.

**Key differences from the field case.** Values may be noncommutative, and forms are $R$-linear rather than $A$-linear; polarization requires 2 invertible, and when 2 is a zero divisor a quadratic form is not determined by its associated bilinear form; a norm form may vanish on nonzero elements because of zero divisors; over a ring a nondegenerate submodule need not be a direct summand, so Witt's theorems may fail.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009).
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991).
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005).
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985).
- John Milnor and Dale Husemoller, *Symmetric Bilinear Forms* (Springer, 1973).
- Richard Elman, Nikita Karpenko and Alexander Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms* (AMS, 2008).
- Nicolas Bourbaki, *Algebra* (Springer, 2003).
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966).
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000).
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001).
