
# __Quadratic Forms over Algebras and Norm Forms__

## Introduction

The forms considered so far have taken values in the base field. When the space is the underlying vector space of an algebra, the natural quadratic forms are the **norm forms** $N(x) = x\bar x$, whose values lie in the centre of the algebra, and the vanishing of $N$ controls the multiplicative structure: the non-invertible elements are exactly the zeros of the norm. Closely related are the **composition laws**, identities $N(xy) = N(x)N(y)$ that turn a quadratic form into a multiplicative invariant, and the classical classification of the algebras carrying such a form.

This article develops quadratic forms with values in an algebra, the projective quadrics they define, the norm forms of the algebra of complex numbers, the quaternions and the biquaternions, the Cayley–Dickson doubling that produces the octonions from the quaternions, and the theorem of Hurwitz that a composition law exists only in dimensions one, two, four and eight. The base is a field $F$ of characteristic not $2$. The involution $\bar{\cdot}$ and the reduced norm are from *Hermitian Forms and Involutions*; the biquaternion conventions are, and the split complex and dual numbers are from *Dual Numbers Algebra*. The quadratic-form vocabulary and the notion of isometry are from *Bilinear Forms* and *Quadratic Forms and Polarisation*; the Clifford algebra of a norm form is not used here but is developed.

## Forms with Values in an Algebra

### Setup

Let $F$ be a field of characteristic not $2$, and let $A$ be a commutative $F$-algebra. A **quadratic form with values in $A$** on an $F$-space $V$ is a function $Q : V \to A$ such that

$$
Q(\lambda x) = \lambda^2 Q(x), \qquad Q(x + y) - Q(x) - Q(y) = \text{a symmetric bilinear form in } x, y,
$$

the second condition expressed by saying that the **polar form**

$$
B_Q(x, y) = \tfrac{1}{2}\bigl(Q(x + y) - Q(x) - Q(y)\bigr)
$$

is $A$-valued and bilinear. This is the definition of *Quadratic Forms and Polarisation* with $A$ in place of the field, and every formal identity carries over because the only operations used are addition, multiplication by scalars and halving.

**Definition.** The $A$-valued form $Q$ is **non-degenerate** if the induced map $V \to \operatorname{Hom}_F(V, A)$, $x \mapsto B_Q(x, -)$, is injective, and **strongly non-degenerate** if it is an isomorphism.

Strong non-degeneracy is unavailable for $\dim_F A > 1$: the target $\operatorname{Hom}_F(V, A)$ has $F$-dimension $(\dim_F V)(\dim_F A)$, so no map $V \to \operatorname{Hom}_F(V, A)$ with $\dim_F A > 1$ is an isomorphism, and the two conditions agree only for $\dim_F A = 1$. The notion the applications require is non-degeneracy after extension of scalars: $Q$ is **non-degenerate over $A$** when $x \mapsto B_Q(x, -)$ has trivial kernel and the $A$-bilinear form $B_Q \otimes_F A$ on $V \otimes_F A$ is non-degenerate in the sense of *Bilinear Forms*. For the norm forms of *Hermitian Forms and Involutions* the polar form is $B_N(x, y) = \tfrac{1}{2}\operatorname{Trd}(x\bar y)$, so the condition is the non-degeneracy of the reduced trace pairing. The zeros of a norm form carry the multiplicative structure: $N(x) = 0$ for some $x \neq 0$ exactly when $x$ is a zero divisor, so that for a composition algebra the norm form is isotropic exactly when the algebra is not a division algebra.

### The Quadric

Assume $F$ is a field and $A$ is finite-dimensional over $F$, of dimension $m$ as an $F$-space, with a basis $\alpha_1, \ldots, \alpha_m$. Writing $Q(x) = \sum_k Q_k(x)\alpha_k$ expresses $Q$ by $m$ scalar-valued quadratic forms $Q_k$ on $V$. The **quadric** of $Q$ is the projective variety

$$
\mathcal{Q}(Q) = \{[x] \in \mathbb{P}(V) : Q(x) = 0\},
$$

the common zero set of the $m$ scalar forms $Q_k$, whose dimension over an algebraically closed field is determined by the codimension of the vanishing locus. Over an algebraically closed field $Q(x) = 0$ alone defines a hypersurface when $m = 1$; for larger $m$ the quadric is the intersection of the $m$ hypersurfaces and can be of substantial codimension.

**Example.** For $A = \mathbb{C}$ and $Q(z) = z^2$ on $V = \mathbb{C}$ viewed as an $\mathbb{R}$-space, the real and imaginary parts are $\operatorname{Re} z^2 = x^2 - y^2$ and $\operatorname{Im} z^2 = 2xy$; their only common zero is $z = 0$, so the common zero set in $V$ is $\{0\}$ and the quadric $\mathcal{Q}(Q) \subseteq \mathbb{P}^1$ is empty.

### Restriction of Scalars

If $A$ is a finite-dimensional $F$-algebra, an $A$-valued form is, after choosing a basis, a tuple of scalar forms, but the tuple carries more information than any single scalar form: it records the multiplication of $A$. The **restriction of scalars** converts the $A$-module $V$ into an $F$-space $V_F$ of dimension $\dim_F A \cdot \dim_A V$, and a Hermitian or quadratic form over $A$ restricts to a scalar form on $V_F$; this is the construction behind the realification of the unitary group in *The Unitary and Symplectic Groups*.

## Norm Forms of Field Extensions

### The Quadratic Case

Let $K = F(\sqrt d)$ be a separable quadratic extension of $F$, with $d \in F^\times$ not a square. The conjugation $a + b\sqrt d \mapsto a - b\sqrt d$ is the nontrivial involution, and the norm is

$$
N_{K/F}(a + b\sqrt d) = a^2 - d\,b^2.
$$

**Proposition.** The norm of a quadratic extension is a non-degenerate quadratic form, multiplicative, and anisotropic if and only if $K$ is a field.

**Proof.** In the basis $1, \sqrt d$ of $K$ over $F$ the norm has matrix $\operatorname{diag}(1, -d)$, invertible because $d \neq 0$; it is the determinant of left multiplication, so $N(xy) = N(x)N(y)$. If $d = s^2$ is a square in $F$, then $K \cong F \times F$ via $a + b\sqrt d \mapsto (a + b\sqrt d, a - b\sqrt d)$, and $N(a + b\sqrt d) = (a + b\sqrt d)(a - b\sqrt d)$ vanishes for $a = sb \neq 0$; if $d$ is not a square, $a^2 = d b^2$ forces $b = 0$ and then $a = 0$. $\square$

### Higher Degree

**Proposition.** For a separable extension $K/F$ of degree $n > 2$, the norm $N_{K/F}$ is a homogeneous form of degree $n$ and is not a quadratic form.

**Proof.** The norm is the determinant of the $F$-linear map of multiplication by $x$ on the $n$-dimensional space $K$, so it is homogeneous of degree $n$, as in *Hermitian Forms and Involutions*; a homogeneous form of degree $n > 2$ is not quadratic. $\square$

## The Norm Form of the Complex Numbers

### Over the Real Numbers

On $\mathbb{C}$ viewed as an $\mathbb{R}$-space with basis $1, i$, the **norm form** is

$$
N(z) = z\bar z = x^2 + y^2, \qquad z = x + iy.
$$

It is the positive definite form of rank $2$, it is multiplicative, $N(zw) = N(z)N(w)$, and it is anisotropic over $\mathbb{R}$ because a sum of two squares vanishes only at the origin. The associated quadric in $\mathbb{P}^1(\mathbb{R})$ is empty, and in $\mathbb{P}^1(\mathbb{C})$ it is the two points $[\pm i]$, corresponding to the complex lines $\{(x, \pm ix)\}$ on which $x^2 + y^2$ vanishes.

### Over the Complex Numbers

Regarded over $\mathbb{C}$ itself, the form $x^2 + y^2 = (x + iy)(x - iy)$ factors, and it is isotropic: $N$ vanishes on the pair of lines $y = \pm ix$. The change of coordinates $u = x + iy$, $v = x - iy$ brings it to $uv$, and the further change $a = (u + v)/2$, $b = (u - v)/2$ brings that to $a^2 - b^2$; the form is therefore the hyperbolic plane $\langle 1, -1\rangle$, and the quadric is a pair of points. This is the algebraic statement that $\mathbb{C}$ does not carry an anisotropic norm form over $\mathbb{C}$.

## The Norm Form of the Quaternions

### Definition and Properties

Let $\mathbb{H}$ be the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$. The conjugation $\bar{\cdot}$ negates the vector part, and the **norm form** is

$$
N(x) = x\bar x = x_0^2 + x_1^2 + x_2^2 + x_3^2, \qquad x = x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3.
$$

**Proposition.** The norm form of $\mathbb{H}$ is positive definite and multiplicative, $N(xy) = N(x)N(y)$; hence $\mathbb{H}$ is a division algebra over $\mathbb{R}$.

**Proof.** Positive definiteness is immediate from the displayed formula. For multiplicativity, $\overline{xy} = \bar y\bar x$, so $N(xy) = xy\,\overline{xy} = xy\bar y\bar x = xN(y)\bar x = N(y)x\bar x = N(x)N(y)$, using that the real number $N(y)$ is central. A nonzero $x$ then has inverse $\bar x/N(x)$. $\square$

### The Quadric in Both Cases

Over $\mathbb{R}$ the norm form $x_0^2 + x_1^2 + x_2^2 + x_3^2$ is anisotropic and its real quadric is empty. Over $\mathbb{C}$ the quaternion algebra splits, $\mathbb{H}_{\mathbb{C}} \cong M_2(\mathbb{C})$, and the norm form becomes $\sum_\mu z_\mu^2$.

**Proposition.** Over $\mathbb{C}$ the quaternion norm form $\sum_{\mu=0}^{3} z_\mu^2$ is isotropic, and its nonzero zeros form the quadric of rank-one $2 \times 2$ matrices, isomorphic to $\mathbb{P}^1 \times \mathbb{P}^1$.

**Proof.** The form is $z_0^2 + z_1^2 + z_2^2 + z_3^2 = (z_0 + iz_1)(z_0 - iz_1) + (z_2 + iz_3)(z_2 - iz_3)$ after collecting the pairs, and it vanishes at $(z_0, z_1, z_2, z_3) = (1, i, 0, 0)$; this shows isotropy. Under the identification $\mathbb{H}_{\mathbb{C}} \cong M_2(\mathbb{C})$ the norm is the determinant, so its zero locus consists of the singular matrices, of which the nonzero ones have rank one. A rank-one matrix is a product $uv^T$ with $0 \neq u, v \in \mathbb{C}^2$, determined up to $(u, v) \mapsto (\lambda u, \lambda^{-1}v)$, so the pair of lines $([u], [v])$ is well defined and the quadric is the image of $\mathbb{P}^1 \times \mathbb{P}^1$ under the Segre embedding. $\square$

## The Norm Form of the Biquaternions

### Definition

Let $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ be the biquaternion algebra, with central unit $i$ of square $-1$ and basis $e_0, e_1, e_2, e_3$ over $\mathbb{C}$, the conventions. The **norm form** is

$$
N(\tilde Q) = \tilde Q \bar{\tilde Q} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2, \qquad \tilde Q = \sum_{\mu=0}^{3} Q_\mu e_\mu,
$$

a $\mathbb{C}$-valued form that is multiplicative, $N(\tilde Q \tilde R) = N(\tilde Q)N(\tilde R)$.

**Proposition.** The norm form of $\mathbb{B}$ is the reduced norm of the central simple algebra $\mathbb{B}$ of degree $2$; equivalently, under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ it is the determinant.

**Proof.** The biquaternion algebra is central simple of degree $2$ over $\mathbb{C}$ and is split, $\mathbb{B} \cong M_2(\mathbb{C})$. Under an explicit isomorphism sending $e_1 \mapsto \operatorname{diag}(i, -i)$ and $e_2 \mapsto \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$, the matrix of $\tilde Q$ is $\begin{pmatrix} Q_0 + iQ_1 & Q_2 + iQ_3 \\ -Q_2 + iQ_3 & Q_0 - iQ_1\end{pmatrix}$, whose determinant is $(Q_0 + iQ_1)(Q_0 - iQ_1) - (Q_2 + iQ_3)(-Q_2 + iQ_3) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$. This is the reduced norm because the reduced norm of a split algebra of degree $2$ is the determinant. $\square$

### The Quadric and the Zero Divisors

**Proposition.** In $\mathbb{B}$ the set of non-invertible elements is exactly the zero set of $N$; the nonzero zeros are the zero divisors, and they correspond to the rank-one matrices of $M_2(\mathbb{C})$.

**Proof.** An element of a finite-dimensional algebra over a field is invertible if and only if its reduced norm is nonzero, as in *Hermitian Forms and Involutions*; the reduced norm here is the determinant, which vanishes exactly on the singular matrices. A nonzero singular $2 \times 2$ matrix has rank one. $\square$

**Remark.** The split nature of $\mathbb{B}$ is visible in the norm form: writing $\tilde Q = P + iQ$ with $P, Q$ in the real quaternion subspace, one has $N(\tilde Q) = N(P) - N(Q) + 2i\,B_N(P, Q)$ with $B_N$ the polar form of the real quaternion norm, and a positive and a negative contribution both occur, so the form is indefinite. The split biquaternions $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$, in which the central unit has square $+1$, behave differently: their norm form $\sum_\mu Q_\mu^2$ with $Q_\mu \in \mathbb{D}$ has positive definite real part and is anisotropic, so it does not detect the zero divisors; those are detected instead by the vanishing of an idempotent component.

## The Cayley–Dickson Doubling

### The Doubling Construction

The composition algebras of dimensions $1, 2, 4$ and $8$ are built from one another by a single recursive step, which doubles the dimension and keeps the norm multiplicative.

**Definition.** Let $A$ be an algebra over $F$ with an involution $\bar{\cdot}$, and let $A' = A \oplus A$ as an $F$-space. The **double** of $A$ is $A'$ with the multiplication and involution

$$
(a, b)(c, d) = (ac - \bar d\, b, \; da + b\bar c), \qquad \overline{(a, b)} = (\bar a, -b).
$$

**Proposition.** The double $A'$ is an algebra with unit $(1, 0)$, the displayed map is an involution of $A'$, and the **double norm**

$$
N'(a, b) = (a, b)\overline{(a, b)} = \bigl(N(a) + N(b),\, 0\bigr)
$$

is the $F$-valued quadratic form $N'(a,b) = N(a) + N(b)$, where $N(a) = a\bar a$ is the norm of $A$.

**Proof.** The unit: $(1,0)(c,d) = (c - 0, d + 0) = (c,d)$ and $(a,b)(1,0) = (a - 0, 0 + b) = (a,b)$. For the involution one verifies $\overline{(a,b)(c,d)} = \overline{(c,d)}\,\overline{(a,b)}$ and $\overline{\overline{(a,b)}} = (a,b)$ by expanding the definitions. For the norm,

$$
(a, b)(\bar a, -b) = \bigl(a\bar a - \overline{(-b)}b, \; (-b)a + b\bar{\bar a}\bigr) = \bigl(N(a) + \bar b b, \; -ba + ba\bigr) = \bigl(N(a) + N(b), 0\bigr),
$$

using $\overline{(-b)} = -\bar b$ and $\bar{\bar a} = a$. $\square$

**Theorem (Cayley–Dickson).** If $A$ is an associative composition algebra over $F$, then its double $A'$ is a composition algebra with the norm $N'$, and $\dim_F A' = 2\dim_F A$.

The multiplicativity of $N'$ is the classical statement of the doubling, verified by expanding $N'(xy)$ in the four components and cancelling using $N(uv) = N(u)N(v)$ and the bilinearity of the polar form; it is the algebraic content of the passage from the two-square identity to the four-square identity, and then to the eight-square identity below. Starting from $A = F$ the construction produces, in order, the complex numbers $\mathbb{C}$ (dimension $2$), the quaternions $\mathbb{H}$ (dimension $4$) and the **octonions** $\mathbb{O}$ (dimension $8$); at each step the algebra is a composition algebra, and the properties lost are ordered: $\mathbb{C}$ is no longer ordered, $\mathbb{H}$ is no longer commutative, and $\mathbb{O}$ is no longer associative. The criterion is standard: the double of an associative algebra is associative exactly when the algebra is associative and commutative, which is satisfied at the first two steps and fails at the third.

### The Octonions

**Definition.** The **octonions** are the double $\mathbb{O} = \mathbb{H} \oplus \mathbb{H}$ of the quaternions, of dimension $8$ over $\mathbb{R}$. Writing an element as $(a, b)$ with $a = x_0 + x_1e_1 + x_2e_2 + x_3e_3$ and $b = x_4 + x_5e_1 + x_6e_2 + x_7e_3$ in the quaternion basis, the norm is

$$
N(a, b) = N(a) + N(b) = x_0^2 + x_1^2 + \cdots + x_7^2,
$$

so the norm form of the octonions is the sum of eight squares, positive definite and anisotropic over $\mathbb{R}$.

**Proposition.** The octonions are not associative; for the basis elements of the doubling one has

$$
(e_1e_2)e_4 \neq e_1(e_2e_4).
$$

**Proof.** The basis is that of the recursive construction, with $e_1, e_2, e_3$ the quaternion units and $e_4 = (0, 1)$ the new generator of the doubling ($e_4^2 = -1$); the two products are computed from the multiplication formula and differ by a sign. $\square$

Non-associativity is thus a phenomenon of dimension $8$: the octonions are a division algebra, in which every nonzero element is invertible with inverse $\bar x/N(x)$, and the elements of norm $1$ are closed under multiplication, but they form only a loop, not a group, because the associative law fails. The two-square, four-square and eight-square identities of the next section are the coordinate forms of the multiplicativity of the norms of $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$.

### The Split Cases

Replacing the new generator of square $-1$ by one of square $+1$ at any step produces the **split** composition algebras: the split complex numbers $\mathbb{D}$ of *Dual Numbers Algebra*, the split quaternions $M_2(\mathbb{R})$, and the split octonions. Over $\mathbb{R}$ there are, up to isomorphism, exactly two composition algebras in each of the dimensions $2$, $4$ and $8$, one anisotropic and one split, and exactly one in dimension $1$, namely $\mathbb{R}$. The anisotropic ones have positive definite norm forms and are division algebras; the split ones have isotropic norms, and the norm of $M_2(\mathbb{R})$ is the determinant. In the corpus's notation the split complex unit is the $j$ with $j^2 = +1$, and the passage from $\mathbb{C}$ to $\mathbb{D}$ is exactly the sign change described here, so that the two-dimensional composition algebras over $\mathbb{R}$ are $\mathbb{C}$ and $\mathbb{D}$.

### The Cayley–Dickson Process with a Parameter

The doubling above appends a new generator of square $-1$. Allowing a general scaling produces the split algebras as well.

**Definition.** Let $A$ be an algebra with involution over $F$ and let $\mu \in F^\times$. The **$\mu$-double** of $A$ is $A_\mu = A \oplus A$ with

$$
(a, b)(c, d) = (ac + \mu\, \bar d\, b, \; da + b\bar c), \qquad \overline{(a,b)} = (\bar a, -b).
$$

The value $\mu = -1$ recovers the doubling of the previous section. The conjugation is again an involution, and the **norm** of the $\mu$-double is

$$
N_\mu(a, b) = (a,b)\overline{(a,b)} = \bigl(N(a) - \mu N(b), 0\bigr),
$$

so that $N_\mu = N \perp (-\mu)N$ as an orthogonal sum of two copies of $N$, the second scaled by $-\mu$.

**Proof.** As for the doubling: $(a,b)(\bar a, -b) = (a\bar a + \mu\overline{(-b)}b, -ba + b\bar{\bar a}) = (N(a) - \mu N(b), 0)$, using $\overline{(-b)} = -\bar b$. $\square$

**Proposition.** If the norm $N$ of $A$ is the $n$-fold Pfister form $\langle\!\langle a_1, \ldots, a_n\rangle\!\rangle$, then

$$
N_\mu \cong \langle\!\langle a_1, \ldots, a_n, \mu\rangle\!\rangle,
$$

an $(n+1)$-fold Pfister form.

**Proof.** $N \perp (-\mu)N = N \otimes \langle 1, -\mu\rangle$, and $\langle 1, -\mu\rangle = \langle\!\langle \mu\rangle\!\rangle$; the tensor product of Pfister forms is the Pfister form of the concatenated parameters. $\square$

**Theorem.** The parametrised doubling preserves the composition law: if $A$ is an associative composition algebra then $A_\mu$ is a composition algebra with norm $N_\mu$, of twice the dimension. Iterating from $A = F$ with $N(x) = x^2$:

| $\mu$ | dimension $2$ | dimension $4$ | dimension $8$ |
|---|---|---|---|
| $\mu = -1$ | $\mathbb{C}$, norm $\langle 1, 1\rangle$ | $\mathbb{H}$, norm $\langle 1,1,1,1\rangle$ | $\mathbb{O}$, norm the sum of eight squares |
| $\mu = +1$ | $\mathbb{D}$, norm $\langle 1, -1\rangle$ | $\mathbb{H}_{\mathbb{D}} \cong M_2(\mathbb{R})$, norm $\langle 1,-1,-1,1\rangle$ | the split octonions, norm $\langle 1,-1,-1,1,-1,1,1,-1\rangle$ |

In Pfister notation the six norms are $\langle\!\langle -1\rangle\!\rangle = \langle 1,1\rangle$, $\langle\!\langle -1,-1\rangle\!\rangle$, $\langle\!\langle -1,-1,-1\rangle\!\rangle$ for the anisotropic chain $\mathbb{C}, \mathbb{H}, \mathbb{O}$, and $\langle\!\langle 1\rangle\!\rangle = \langle 1,-1\rangle$, $\langle\!\langle 1,1\rangle\!\rangle = \langle 1,-1,-1,1\rangle$, $\langle\!\langle 1,1,1\rangle\!\rangle$ for the split chain $\mathbb{D}, \mathbb{H}_{\mathbb{D}}$, split octonions. The classical chain is the one in which every doubling appends the parameter $-1$; the split chain appends $+1$ and its norms are isotropic from dimension $2$ onwards.

**Proof.** Multiplicativity of $N_\mu$ is the classical computation of the doubling, unchanged by the parameter except for the sign in the second factor; it is verified at each step by expanding $N_\mu(xy)$ in the four components. The dimension doubles by construction. The table records the diagonalised norms obtained by iterating: at $\mu = -1$ every new generator contributes a positive square, at $\mu = +1$ the new generator contributes a negative one. $\square$

### Classification of the Composition Algebras

**Theorem (standard).** Let $A$ be a composition algebra of dimension at least $2$ over a field $F$ of characteristic not $2$. Then $\dim_F A \in \{2, 4, 8\}$; a $2$-dimensional composition algebra is a separable quadratic $F$-algebra, that is a field $F(\sqrt d)$ or the split algebra $F \times F$, a $4$-dimensional one is a quaternion algebra, and an $8$-dimensional one is an octonion algebra. A composition algebra is determined up to isomorphism by its norm form, and the norm forms occurring are exactly the Pfister forms $\langle\!\langle a_1, \ldots, a_n\rangle\!\rangle$ of dimension $2^n = \dim_F A$.

**Remark.** The theorem is standard and is cited as such; the correspondence between algebras and forms is the content of the classification of the composition algebras, and it is why the norm form alone decides the isomorphism type. The real case is the table above: in dimension $2$ the norms $\langle 1, 1\rangle$ and $\langle 1, -1\rangle$ give $\mathbb{C}$ and $\mathbb{D}$; in dimension $4$ the anisotropic norm $\langle 1,1,1,1\rangle$ gives $\mathbb{H}$ and the isotropic norm $\langle 1,-1,-1,1\rangle$ gives $\mathbb{H}_{\mathbb{D}} \cong M_2(\mathbb{R})$; in dimension $8$ the two norms give the division octonions and the split octonions. Over $\mathbb{R}$ there are therefore exactly two composition algebras in each of the dimensions $2$, $4$ and $8$, matching the two possible signs of the Pfister parameter.

## Composition of Quadratic Forms

### Composition Algebras

**Definition.** A **composition algebra** over $F$ is an $F$-algebra $A$, not assumed associative, with a non-degenerate quadratic form $N : A \to F$ such that

$$
N(xy) = N(x)N(y) \qquad (x, y \in A).
$$

The form $N$ is the **norm** of the composition algebra, and the identity is a **composition law**.

**Example.** The field $F$ with $N(x) = x^2$ is a composition algebra of dimension $1$; the complex numbers with $N(z) = z\bar z$ are a composition algebra of dimension $2$; the quaternions with $N(x) = x\bar x$ are one of dimension $4$. The biquaternions over $\mathbb{R}$ are not a composition algebra, because their norm takes values in $\mathbb{C}$ rather than in $\mathbb{R}$; over $\mathbb{C}$, however, $\mathbb{B} \cong M_2(\mathbb{C})$ is a split composition algebra of dimension $4$ with the determinant as its norm.

**Proposition.** In a composition algebra the polar form of the norm satisfies

$$
B_N(xy, xz) = N(x)B_N(y, z), \qquad B_N(xz, yz) = N(z)B_N(x, y),
$$

so left and right multiplication by $x$ are similarities of the norm form with multiplier $N(x)$.

**Proof.** Polarise the identity $N(xy) = N(x)N(y)$ in $y$ to obtain the first relation, and in $x$ to obtain the second, exactly as the polar form is obtained in *Quadratic Forms and Polarisation*. $\square$

### The Classical Composition Identities

The dimensions $1, 2, 4, 8$ are the dimensions in which a composition law exists, and each produces an identity of sums of squares.

**Theorem (two squares).** For all $x_1, x_2, y_1, y_2$ in $F$,

$$
(x_1^2 + x_2^2)(y_1^2 + y_2^2) = (x_1y_1 - x_2y_2)^2 + (x_1y_2 + x_2y_1)^2.
$$

**Proof.** This is multiplicativity of the complex norm, $N(z)N(w) = N(zw)$, written in coordinates for $z = x_1 + ix_2$ and $w = y_1 + iy_2$. $\square$

**Theorem (four squares, Euler).** For all $x_i, y_i$ in $F$,

$$
\Bigl(\sum_{k=1}^{4} x_k^2\Bigr)\Bigl(\sum_{k=1}^{4} y_k^2\Bigr) = \sum_{k=1}^{4} z_k^2,
$$

where $z = (x_1 + x_2e_1 + x_3e_2 + x_4e_3)(y_1 + y_2e_1 + y_3e_2 + y_4e_3)$ is the quaternion product; the coordinates $z_k$ of the product are the right-hand side.

**Proof.** This is multiplicativity of the quaternion norm in coordinates, with $N(x) = \sum_k x_k^2$ by the formula above. $\square$

**Theorem (eight squares, Degen).** The same statement holds with eight squares, the product being taken in the octonion algebra of the Cayley–Dickson construction above; by Hurwitz's theorem below, the dimensions $1, 2, 4$ and $8$ are the only ones in which such an identity holds.

### Hurwitz's Theorem

**Theorem (Hurwitz).** Let $A$ be a composition algebra over a field $F$ of characteristic not $2$. Then $\dim_F A \in \{1, 2, 4, 8\}$. Over $\mathbb{R}$ the four composition algebras with anisotropic norm form are, up to isomorphism, the real numbers, the complex numbers, the quaternions and the octonions, of dimensions $1, 2, 4, 8$; the split forms of dimensions $2, 4, 8$ are the remaining composition algebras over $\mathbb{R}$.

**Remark.** The theorem is standard and is cited as such; its proof uses the polarised identity above to build a subalgebra generated by two elements and then analyses the possible dimensions of the subalgebras. We give the statement and the two explicit identities, which exhibit the cases $2$ and $4$; the case $8$ is the octonion algebra, whose norm form is anisotropic of dimension $8$ and whose multiplication fails to be associative. In dimensions other than $1, 2, 4, 8$ there is no composition law, so the sums-of-squares identities above cannot be extended: the failure is measured by the theorem.

**Corollary.** The norm forms of the real division algebras have dimensions $1, 2, 4$ and $8$ and are anisotropic and positive definite. Replacing a central unit of square $-1$ by one of square $+1$ keeps the dimension but not the definiteness: the split complex norm $a^2 - b^2$ is indefinite of signature $(1, 1)$, and for the split quaternions the determinant form $\langle 1, -1, -1, 1\rangle$ of $M_2(\mathbb{R})$ is indefinite of signature $(2, 2)$; the $\mathbb{D}$-valued norm of the $\mathbb{D}$-algebra $\mathbb{H}_{\mathbb{D}}$ instead has positive definite real part and vanishes only at $0$, so it does not detect the zero divisors, which are read off from the vanishing of an idempotent component.

## Summary

A **quadratic form with values in a commutative algebra** $A$ is a function $Q : V \to A$ that is homogeneous of degree two and whose polar form $B_Q(x, y) = \tfrac{1}{2}(Q(x+y) - Q(x) - Q(y))$ is $A$-bilinear. Expanding in a basis of $A$ produces scalar forms whose common zero locus is the **quadric** $\mathcal{Q}(Q) \subseteq \mathbb{P}(V)$.

The **norm form** $N(x) = x\bar x$ of an algebra with involution is the central example. For a quadratic field extension $K = F(\sqrt d)$ it is $a^2 - db^2$, anisotropic exactly when $K$ is a field; for a separable extension of degree $n > 2$ it is a form of degree $n$, hence not quadratic. For the complex numbers it is $x^2 + y^2$, positive definite and anisotropic over $\mathbb{R}$ and isotropic over $\mathbb{C}$. For the quaternions it is $x_0^2 + x_1^2 + x_2^2 + x_3^2$, positive definite and multiplicative, making $\mathbb{H}$ a division algebra; over $\mathbb{C}$ the quaternion algebra splits and this form becomes the determinant on $M_2(\mathbb{C})$, whose nonzero zeros are the rank-one matrices and whose quadric is the Segre quadric $\mathbb{P}^1 \times \mathbb{P}^1$. For the biquaternions the norm is $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$, the reduced norm, equal to the determinant under $\mathbb{B} \cong M_2(\mathbb{C})$; it is isotropic and its nonzero zeros are the zero divisors. The norm forms of the quadratic extension and of the quaternions give the complex and quaternion composition laws $N(xy) = N(x)N(y)$, hence the two-square and four-square identities, and **Hurwitz's theorem** states that a composition algebra has dimension $1, 2, 4$ or $8$, the four anisotropic real cases being $\mathbb{R}, \mathbb{C}, \mathbb{H}$ and the octonions.

The recursion behind that list is the **Cayley–Dickson doubling**: on $A' = A \oplus A$ with $(a,b)(c,d) = (ac - \bar db, da + b\bar c)$ and $\overline{(a,b)} = (\bar a, -b)$, the norm $N'(a,b) = N(a) + N(b)$ is multiplicative whenever $A$ is an associative composition algebra, and the dimension doubles. Starting from $\mathbb{R}$ this yields $\mathbb{C}$, $\mathbb{H}$ and the octonions $\mathbb{O}$, whose norm form is the sum of eight squares; the double is associative exactly when the algebra doubled is associative and commutative, so associativity survives the first two steps and fails at $\mathbb{H} \to \mathbb{O}$, where $(e_1e_2)e_4 \neq e_1(e_2e_4)$. Replacing the new generator of square $-1$ by one of square $+1$ produces the split composition algebras, and over $\mathbb{R}$ there are exactly two composition algebras in each of the dimensions $2$, $4$ and $8$, one anisotropic and one split.

The doubling with a general parameter $\mu$ has $(a,b)(c,d) = (ac + \mu\bar db, da + b\bar c)$ and norm $N_\mu = N \perp (-\mu)N$, so that the parameter is appended to the Pfister form: if $N \cong \langle\!\langle a_1, \ldots, a_n\rangle\!\rangle$ then $N_\mu \cong \langle\!\langle a_1, \ldots, a_n, \mu\rangle\!\rangle$. Iterating with $\mu = -1$ gives $\mathbb{C}, \mathbb{H}, \mathbb{O}$ with positive definite norms $\langle\!\langle -1\rangle\!\rangle = \langle 1,1\rangle$, $\langle\!\langle -1,-1\rangle\!\rangle$ and $\langle\!\langle -1,-1,-1\rangle\!\rangle$, while iterating with $\mu = +1$ gives the split complex numbers $\mathbb{D}$, the split quaternions $M_2(\mathbb{R})$ and the split octonions, with isotropic norms from dimension $2$ onwards. **The classification of the composition algebras** states that the composition algebras of dimension at least $2$ are the separable quadratic algebras, the quaternion algebras and the octonion algebras, and that such an algebra is determined up to isomorphism by its norm form, the possible norms being exactly the Pfister forms of dimension $2, 4, 8$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Field of characteristic not $2$ |
| $A$ | Commutative $F$-algebra (for $A$-valued forms); composition algebra |
| $V$ | Finite-dimensional $F$-space |
| $Q$, $B_Q$ | $A$-valued quadratic form and its polar form |
| non-degenerate over $A$ | $x \mapsto B_Q(x, -)$ injective and $B_Q \otimes_F A$ non-degenerate |
| $\mathcal{Q}(Q)$ | Quadric $\{[x] : Q(x) = 0\}$ |
| $\mathbb{P}(V)$ | Projective space of lines in $V$ |
| $N$, $N_{K/F}$ | Norm form; field norm |
| $K = F(\sqrt d)$ | Separable quadratic extension |
| $B_N$ | Polar form of the norm, $B_N(x,y) = \tfrac12(N(x+y)-N(x)-N(y))$ |
| $\bar{\cdot}$ | Conjugation on $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B}$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central complex unit, $i^2 = -1$, in $\mathbb{B}$ |
| $j$ | Split unit, $j^2 = +1$, in $\mathbb{D}$ and $\mathbb{H}_{\mathbb{D}}$ |
| $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}, \mathbb{D}, \mathbb{D}'$ | Real, complex, quaternion, biquaternion, split complex, dual numbers |
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternions, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{O}$ | Octonions, the double of $\mathbb{H}$ |
| $A'$ | Double of $A$: $A \oplus A$ with the Cayley–Dickson product |
| $(a,b)(c,d) = (ac - \bar d b, da + b\bar c)$ | Cayley–Dickson multiplication |
| $N'(a,b) = N(a) + N(b)$ | Norm of the double |
| $\mu$ | Parameter of the generalised doubling, $\mu \in F^\times$ |
| $A_\mu$ | $\mu$-double of $A$ |
| $N_\mu = N \perp (-\mu)N$ | Norm of the $\mu$-double |
| $\langle\!\langle a_1,\ldots,a_n\rangle\!\rangle$ | Pfister form, the norm of a composition algebra of dimension $2^n$ |
| Split octonions | $\mu = +1$ double of $\mathbb{H}_{\mathbb{D}}$, isotropic norm |
| $M_2(\mathbb{C})$ | $2 \times 2$ complex matrices |
| Segre embedding | The map $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$ |



## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for norm forms, composition laws and the theorem of Hurwitz.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the reduced norm and the norm form of a central simple algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for composition algebras and their classification.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the norm forms and multiplication tables of $\mathbb{H}$ and the octonions.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2009), for the norm form of a field extension and the quadratic case.
