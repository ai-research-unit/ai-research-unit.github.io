
# __Hermitian Forms and Involutions__

## Introduction

A Hermitian form is a two-variable form that is linear in one argument and conjugate-linear in the other, the conjugation being an **involution** of the ring of scalars. The prototype is the form $\sum_i \bar{z}_i w_i$ on $\mathbb{C}^n$, whose diagonal is the squared length $\sum_i |z_i|^2$; its isometry group is the unitary group. This article develops the algebraic theory: involutions of rings, sesquilinear and Hermitian forms relative to an involution, the quadratic form carried by the diagonal over the fixed ring, and the trace form and reduced norm attached to a finite-dimensional algebra.

The base is a ring $A$ that is usually non-commutative, with an involution $\sigma$; when a determinant or a trace is needed, $A$ is a finite-dimensional unital algebra over a field $F$. The sesquilinear forms of *Bilinear Forms* are the case $\sigma = \mathrm{id}$ with $A$ commutative, and the unitary group is treated as one of the classical groups in *The Unitary and Symplectic Groups*. The norms of the complex, quaternion and biquaternion algebras are specialisations of the reduced norm defined here, and are computed; the conventions for the biquaternion conjugations are the standard ones.

## Involutions

### Definition

Let $A$ be a ring, not assumed commutative. An **involution** of $A$ is a map $\sigma : A \to A$ such that

$$
\sigma(a + b) = \sigma(a) + \sigma(b), \qquad \sigma(ab) = \sigma(b)\sigma(a), \qquad \sigma(\sigma(a)) = a, \qquad \sigma(1) = 1
$$

for all $a, b \in A$. The first two conditions say that $\sigma$ is an anti-automorphism, and the third that it has order two. The **fixed ring** is

$$
A^\sigma = \{a \in A : \sigma(a) = a\}.
$$

It is a subring containing $1$, and it is the natural ring of scalars for the diagonal of a Hermitian form.

**Proposition.** If $A$ is commutative and $2$ is invertible in $A$, then $\sigma$ is a ring automorphism of order two, and if $\sigma \neq \mathrm{id}$ the fixed ring $A^\sigma$ is a subring with the property that every $a \in A$ satisfies a monic quadratic equation over $A^\sigma$.

**Proof.** Commutativity makes anti-automorphisms into automorphisms. For $a \in A$ write $a = a_+ + a_-$ with $a_+ = (a + \sigma(a))/2$ and $a_- = (a - \sigma(a))/2$, using the invertibility of $2$. Then $a_+ \in A^\sigma$, $a_-$ is anti-fixed, and $a_-^2 \in A^\sigma$ because $\sigma(a_-^2) = \sigma(a_-)^2 = (-a_-)^2 = a_-^2$. Hence $a$ satisfies $x^2 - 2a_+ x + (a_+^2 - a_-^2) = 0$ with coefficients in $A^\sigma$. $\square$

### First and Second Kind

**Definition.** An involution $\sigma$ of a ring $A$ with centre $Z(A)$ is of the **first kind** if $\sigma$ acts as the identity on $Z(A)$, and of the **second kind** if it does not. For a central simple algebra over a field $F$, an involution of the second kind has fixed field $F^\sigma$ with $[F : F^\sigma] = 2$; an involution of the first kind either is **orthogonal** or is **symplectic**, according to the type of the associated bilinear form on the algebra.

### Examples

**Example (complex conjugation).** On $\mathbb{C}$ the map $z \mapsto \bar z$ is an involution of the second kind over $\mathbb{R}$ with fixed ring $\mathbb{R}$. Viewed from $\mathbb{C}$ the conjugation is not $\mathbb{C}$-linear but only $\mathbb{R}$-linear; the sesquilinear theory of $\mathbb{C}$ is therefore a theory over $\mathbb{R}$, and the unitary group of a Hermitian form is a real algebraic group rather than a complex one.

**Example (quaternion conjugation).** On $\mathbb{H}$ the map $\bar{x} = \mathrm{Sc}(x) - \mathrm{Vect}(x)$ is an involution of the first kind with fixed ring $\mathbb{R}$. On the biquaternions $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ the three commuting conjugations $\bar{\cdot}$, ${}^{*}$ and ${}^{\dagger}$ are involutions; $\bar{\cdot}$ is the quaternionic one extended by the identity on $\mathbb{C}$, ${}^{*}$ conjugates the complex coefficients, and ${}^{\dagger} = \bar{\cdot} \circ {}^{*}$ is Hermitian conjugation. Their composition rules make the set $\{\mathrm{id}, \bar{\cdot}, {}^{*}, {}^{\dagger}\}$ a Klein four-group.

**Example (matrix transpose).** On $M_n(R)$ over a commutative ring the transpose $M \mapsto M^T$ is an involution of the first kind. On a matrix algebra with a symmetric or alternating form there are further involutions $M \mapsto G^{-1}M^T G$; the transpose corresponds to a symmetric form and the **symplectic involution** $M \mapsto \Omega^{-1}M^T\Omega$ to an alternating one.

**Example (dual and split complex numbers).** On the split complex numbers $\mathbb{D} = \mathbb{R}[j]/(j^2 - 1)$ the map $a + bj \mapsto a - bj$ is an involution with fixed ring $\mathbb{R}$. On the dual numbers $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ the analogous map is an involution, but the norm form it produces is degenerate. The notation $\mathbb{D}$ for the split complex numbers and $\mathbb{D}'$ for the dual numbers is fixed in *Dual Numbers Algebra*.

## The Two Types of Involutions of the First Kind

### Symmetric and Skew Elements

Let $A$ be a ring with an involution $\sigma$ and let $2$ be invertible in $A$. The **symmetric** and **skew** elements of $\sigma$ are

$$
\mathrm{Sym}(A, \sigma) = \{a \in A : \sigma(a) = a\}, \qquad \mathrm{Skew}(A, \sigma) = \{a \in A : \sigma(a) = -a\}.
$$

**Proposition.** $A = \mathrm{Sym}(A, \sigma) \oplus \mathrm{Skew}(A, \sigma)$ as abelian groups, and $\mathrm{Sym}(A,\sigma) = A^\sigma$ is the fixed ring.

**Proof.** For $a \in A$ the elements $a_+ = \tfrac{1}{2}(a + \sigma(a))$ and $a_- = \tfrac{1}{2}(a - \sigma(a))$ are symmetric and skew, and $a = a_+ + a_-$; conversely an element that is both symmetric and skew satisfies $a = -a$, hence $a = 0$ because $2a = 0$ with $2$ invertible. $\square$

So over a field $F$ of characteristic not $2$ one has $\dim_F\mathrm{Sym}(A,\sigma) + \dim_F\mathrm{Skew}(A,\sigma) = \dim_F A$, and the dimension of either part is an invariant of the involution.

### The Two Types

**Definition.** Let $A$ be a central simple $F$-algebra of degree $n$ with an involution $\sigma$ of the first kind. Then $\sigma$ is of **orthogonal type** if $\dim_F \mathrm{Sym}(A, \sigma) = n(n+1)/2$, and of **symplectic type** if $\dim_F \mathrm{Sym}(A, \sigma) = n(n-1)/2$.

**Theorem.** Every involution of the first kind on a central simple algebra is of exactly one of these two types, so the two possibilities are exhaustive and mutually exclusive. This is the standard classification, for which the classical reference is the theory of algebras with involution.

**Proposition.** Let $A = M_n(F)$ with $2$ invertible in $F$.

1. For the transpose $X \mapsto X^{T}$ one has $\dim \mathrm{Sym} = n(n+1)/2$ and $\dim \mathrm{Skew} = n(n-1)/2$, so the transpose is of orthogonal type.
2. Let $n = 2m$ and let $J = \begin{pmatrix} 0 & I_m \\ -I_m & 0\end{pmatrix}$. For the involution $X \mapsto JX^{T}J^{-1}$ one has $\dim\mathrm{Sym} = m(2m-1) = n(n-1)/2$ and $\dim \mathrm{Skew} = m(2m+1) = n(n+1)/2$, so it is of symplectic type.

**Proof.** The first part is the count of the symmetric and antisymmetric matrices. For the second, write $X = \begin{pmatrix} A & B \\ C & D\end{pmatrix}$ in $m \times m$ blocks and note that $X = JX^{T}J^{-1}$ is equivalent to $XJ = JX^{T}$. Now

$$
XJ = \begin{pmatrix} -B & A \\ -D & C\end{pmatrix}, \qquad JX^{T} = \begin{pmatrix} B^{T} & D^{T} \\ -A^{T} & -C^{T}\end{pmatrix},
$$

so the conditions are $B^{T} = -B$, $C^{T} = -C$ and $A^{T} = D$. The block $A$ is arbitrary, of $m^2$ entries, and the blocks $B$ and $C$ are antisymmetric, of $m(m-1)/2$ entries each; the total is

$$
m^2 + 2\cdot\frac{m(m-1)}{2} = m(2m-1) = \frac{n(n-1)}{2}.
$$

The skew elements satisfy $X = -JX^{T}J^{-1}$, that is $XJ = -JX^{T}$, which replaces the conditions on $B$ and $C$ by symmetry and leaves $A$ free; the count becomes $m^2 + 2\cdot\frac{m(m+1)}{2} = m(2m+1)$. $\square$

### Adjoint Involutions

The two types are exactly the involutions produced by symmetric and by alternating forms, which is the origin of their names.

**Theorem.** Let $b$ be a non-degenerate bilinear form on an $n$-dimensional space $V$ over a field with $2$ invertible, and let the **adjoint involution** $\sigma_b$ on $\mathrm{End}(V)$ be defined by

$$
b(fx, y) = b(x, \sigma_b(f)y).
$$

Then $\sigma_b$ is of orthogonal type when $b$ is symmetric, and of symplectic type when $b$ is alternating.

**Proof.** In a basis with Gram matrix $G$, the defining relation reads $f^{T}G = G\sigma_b(f)$, so $\sigma_b(f) = G^{-1}f^{T}G$ and $f$ is self-adjoint exactly when $Gf = f^{T}G$. If $G^{T} = G$ then $(Gf)^{T} = f^{T}G^{T} = f^{T}G = Gf$, so $Gf$ is symmetric, and conversely a symmetric $Gf$ satisfies $Gf = (Gf)^{T} = f^{T}G$. The assignment $f \mapsto Gf$ is a bijection, so the self-adjoint elements correspond to the symmetric matrices, of dimension $n(n+1)/2$. If $G^{T} = -G$, then $(Gf)^{T} = f^{T}G^{T} = -f^{T}G$, so the condition $Gf = f^{T}G$ becomes $Gf = -(Gf)^{T}$, that is $Gf$ alternating, and the self-adjoint elements correspond to the alternating matrices, of dimension $n(n-1)/2$; such a $G$ is invertible only for even $n$, which is exactly the condition for an alternating form to be non-degenerate. $\square$

**Remark.** The theorem explains the terminology: the transpose on $M_n(R)$ is the adjoint involution of the standard symmetric form, and the map $X \mapsto \Omega^{-1}X^{T}\Omega$ is the adjoint involution of the standard alternating form; both are the involutions of the matrix transpose example above. The involution determined by a form and the type of that involution are therefore the same datum, and the dimension of the symmetric part is the invariant that separates the two cases.

## Sesquilinear and Hermitian Forms

### Sesquilinear Forms

Let $A$ be a ring with involution $\sigma$ and let $M$ be a **right** $A$-module. A function $s : M \times M \to A$ is **$\sigma$-sesquilinear** if it is additive in each argument and

$$
s(xa, yb) = \sigma(a)\, s(x, y)\, b \qquad (a, b \in A,\ x, y \in M).
$$

The right-module convention is the natural one for sesquilinear forms: the second argument is $A$-linear and the first is $\sigma$-$A$-linear. Over a commutative ring with $\sigma = \mathrm{id}$ this reduces to a bilinear form in the sense of *Bilinear Forms*.

**Proposition.** Let $s$ be $\sigma$-sesquilinear. Then the map $s' : M \times M \to A$ defined by $s'(x, y) = \sigma(s(y, x))$ is again $\sigma$-sesquilinear.

**Proof.** Additivity is clear. For the scaling,

$$
s'(xa, yb) = \sigma\bigl(s(yb, xa)\bigr) = \sigma\bigl(\sigma(b)s(y,x)a\bigr) = \sigma(a)\sigma(s(y,x))\sigma(\sigma(b)) = \sigma(a)\,s'(x,y)\,b,
$$

using $\sigma^2 = \mathrm{id}$. $\square$

### Hermitian and Skew-Hermitian Forms

**Definition.** A $\sigma$-sesquilinear form $s$ is **Hermitian** if $s(x, y) = \sigma(s(y, x))$, and **skew-Hermitian** if $s(x, y) = -\sigma(s(y, x))$. In the notation of the proposition, Hermitian means $s = s'$ and skew-Hermitian means $s = -s'$.

**Proposition.** Let $s$ be $\sigma$-Hermitian. Then its **diagonal** $q(x) = s(x, x)$ takes values in the fixed ring $A^\sigma$, and satisfies

$$
q(xa) = \sigma(a)\,q(x)\,a, \qquad q(x + y) - q(x) - q(y) = s(x, y) + \sigma(s(x, y)).
$$

In particular, for a central element $a \in A^\sigma$ the diagonal is homogeneous of degree two, $q(xa) = a^2 q(x)$.

**Proof.** For the fixed-ring property, $\sigma(q(x)) = \sigma(s(x,x)) = s(x,x) = q(x)$ by Hermitian symmetry. The scaling is $q(xa) = s(xa, xa) = \sigma(a)s(x,x)a = \sigma(a)q(x)a$. The polar identity is the expansion of $s(x + y, x + y)$ using additivity and the Hermitian symmetry. $\square$

**Definition.** The **diagonal form** of a $\sigma$-Hermitian form is the function $x \mapsto s(x, x)$ on $M$, with polar expression $s(x, y) + \sigma(s(x, y))$; over a field with $\sigma = \mathrm{id}$ the polar expression is $2B$, the associated bilinear form of *Quadratic Forms and Polarisation*. The diagonal form is a quadratic form on the fixed ring in the sense, and the name distinguishes it from the trace form of an algebra, defined below. When $A$ is a division ring with involution and $s$ is non-degenerate, the isometry group of $s$ is the **unitary group** of the form, and it is related to the classical groups of *The Unitary and Symplectic Groups*.

### The Matrix of a Hermitian Form

Assume $A$ is a division ring, $M$ is a free right $A$-module of finite rank, and $(e_1, \ldots, e_n)$ is a basis. The **Gram matrix** of $s$ is $H_{ij} = s(e_i, e_j)$, and $H$ is Hermitian in the sense $H^{\dagger} = H$, where $H^{\dagger} = \sigma(H)^T$. For $x = \sum_i e_i x_i$ and $y = \sum_j e_j y_j$,

$$
s(x, y) = \sum_{i,j} \sigma(x_i)\, H_{ij}\, y_j = x^{\dagger} H\, y,
$$

so a Hermitian form is represented by a Hermitian matrix, and the form is non-degenerate exactly when $H$ is invertible. Over $\mathbb{C}$ with the identity matrix this is the standard form of $U(n)$ in *The Unitary and Symplectic Groups*.

### The Radical and Non-Degeneracy

**Definition.** The **radical** of a $\sigma$-Hermitian form $s$ on $M$ is

$$
\operatorname{rad}(s) = \{x \in M : s(x, y) = 0 \text{ for all } y \in M\},
$$

and $s$ is **non-degenerate** when the radical is zero.

**Proposition.** Let $M$ be free of finite rank with Gram matrix $H$. Then $x \in \operatorname{rad}(s)$ if and only if $Hx = 0$, and $s$ is non-degenerate exactly when $H$ is invertible.

**Proof.** With $x = \sum_i e_ix_i$ the condition $s(x, y) = 0$ for all $y$ reads $x^{\dagger}Hy' = 0$ for every column $y'$, that is $x^{\dagger}H = 0$. Transposing and conjugating gives $(x^{\dagger}H)^{\dagger} = H^{\dagger}x = Hx$, using $H^{\dagger} = H$; so the radical is the kernel of $H$, and it vanishes exactly when $H$ is invertible. $\square$

### Isometries and the Extension Theorem

**Remark (reflections and extension).** When $A$ is commutative and $\sigma = \mathrm{id}$, so that $s$ is a symmetric bilinear form, the reflections of *Isometries and Orthogonal Transformations* apply verbatim and the extension and cancellation theorems are standard. For a general division ring with involution the same two theorems hold in the Hermitian case by Dieudonné's theorem for Hermitian forms, with the exception of a field of characteristic two, where the phenomena described reappear. These results are cited here as standard; their proofs belong to the theory of forms over division rings.

The Hermitian case is genuinely richer than the symmetric one over a field. When $\sigma \neq \mathrm{id}$ the diagonal values $s(x,x)$ lie in the fixed field $A^\sigma$, which is properly smaller than the ring of scalars, so a Hermitian form carries a quadratic form over the fixed field rather than a bilinear form over the whole ring; this is the mechanism by which the norm forms of the complex and quaternion algebras become quadratic forms over $\mathbb{R}$, as developed.

## Norms and Traces of an Algebra

### The Regular Norm and the Trace Form

Let $A$ be a finite-dimensional unital associative algebra over a field $F$, and for $x \in A$ let $m_x : A \to A$ be left multiplication by $x$, an $F$-linear endomorphism.

**Definition.** The **regular norm** and the **regular trace** of $x$ are

$$
N(x) = \det(m_x), \qquad \operatorname{Tr}(x) = \operatorname{Tr}(m_x).
$$

The **trace form** of $A$ is the symmetric bilinear form

$$
T(x, y) = \operatorname{Tr}(m_{xy}) = \operatorname{Tr}(m_x m_y),
$$

with associated quadratic form $q_T(x) = T(x, x) = \operatorname{Tr}(m_{x^2})$ when $\operatorname{char} F \neq 2$.

**Proposition.** The regular norm is multiplicative, $N(xy) = N(x)N(y)$, and homogeneous of degree $n = \dim_F A$; the trace form is symmetric bilinear and satisfies $T(x, y) = T(y, x)$.

**Proof.** $m_{xy} = m_x \circ m_y$, so $\det(m_{xy}) = \det(m_x)\det(m_y)$; homogeneity of degree $n$ follows from $\det(\lambda I) = \lambda^n$ applied to $m_{\lambda x} = \lambda m_x$. The trace form is symmetric because $\operatorname{Tr}(m_{xy}) = \operatorname{Tr}(m_x m_y) = \operatorname{Tr}(m_y m_x) = \operatorname{Tr}(m_{yx})$. $\square$

**Proposition.** The regular norm $N$ is a quadratic form precisely when $\dim_F A = 2$.

**Proof.** A homogeneous polynomial of degree $n$ is a quadratic form only for $n = 2$. $\square$

**Example (a field extension).** For a separable field extension $K/F$ of degree $n$, the left multiplication $m_x$ is the $F$-linear map "multiply by $x$", and the trace form is

$$
T(x, y) = \operatorname{Tr}_{K/F}(xy), \qquad q_T(x) = \operatorname{Tr}_{K/F}(x^2).
$$

For $K = F(\sqrt d)$ with $\operatorname{char} F \neq 2$ and $x = a + b\sqrt d$,

$$
q_T(x) = \operatorname{Tr}_{K/F}(x^2) = 2(a^2 + d\,b^2), \qquad N(x) = \operatorname{N}_{K/F}(x) = a^2 - d\,b^2.
$$

The two forms already differ in dimension two: the regular norm is the field norm and is quadratic here, while the trace form has dimension two as well but is a different form.

### The Reduced Trace and Reduced Norm

Let $A$ be a central simple algebra over a field $F$ of degree $d$, so that $A \otimes_F \bar F \cong M_d(\bar F)$ for an algebraic closure $\bar F$, and $\dim_F A = d^2$.

**Definition.** Fix an isomorphism $A \otimes_F \bar F \cong M_d(\bar F)$ as above. The **reduced trace** and **reduced norm** of $x \in A$ are the trace and the determinant of the image of $x \otimes 1$; both lie in $F$ and are independent of the chosen isomorphism. Equivalently, when $d$ is invertible in $F$, they are obtained from the regular trace and norm by

$$
\operatorname{Trd}(x) = \operatorname{Tr}(m_x)/d, \qquad \operatorname{Nrd}(x)^{\,d} = N(x).
$$

The two descriptions agree because $m_x$ becomes left multiplication by a $d \times d$ matrix over $\bar F$, whose trace is $d$ times the matrix trace and whose determinant is the $d$-th power of the matrix determinant.

**Proposition.** The reduced trace is an $F$-linear functional with $\operatorname{Trd}(1) = d$, and the reduced norm is multiplicative, $\operatorname{Nrd}(xy) = \operatorname{Nrd}(x)\operatorname{Nrd}(y)$, with $\operatorname{Nrd}(1) = 1$ and $\operatorname{Nrd}(x) = 0$ exactly when $x$ is not invertible. The $d$-th power of the reduced norm is the regular norm.

**Proof.** These are standard properties of the reduced trace and norm of a central simple algebra; they follow by extension of scalars to $\bar F$, where $A$ becomes $M_d(\bar F)$ and $\operatorname{Trd}$, $\operatorname{Nrd}$ become the ordinary trace and determinant. $\square$

**Definition.** The **reduced trace form** is the symmetric bilinear form

$$
T_{\operatorname{red}}(x, y) = \operatorname{Trd}(xy),
$$

and the **reduced norm form** is the multiplicative form $x \mapsto \operatorname{Nrd}(x)$.

**Proposition.** For a central simple algebra of degree $d$, the reduced norm is a form of degree $d$, hence a quadratic form precisely when $d = 2$, that is, for a quaternion algebra.

**Proof.** Immediate from the definition: $\operatorname{Nrd}(\lambda x) = \lambda^d \operatorname{Nrd}(x)$. $\square$

### The Polar Form of the Reduced Norm

For a quaternion algebra $D$ over a field $F$ of characteristic not $2$, with the canonical involution $x \mapsto \bar x$ and reduced norm $N(x) = x\bar x = \operatorname{Nrd}(x)$, the polar form of $N$ is

$$
B_N(x, y) = \tfrac{1}{2}\bigl(N(x + y) - N(x) - N(y)\bigr) = \tfrac{1}{2}\bigl(x\bar y + y\bar x\bigr) = \tfrac{1}{2}\operatorname{Trd}(x\bar y).
$$

**Proposition.** The polar form $B_N$ of the reduced norm is not a scalar multiple of the reduced trace form $T_{\operatorname{red}}(x, y) = \operatorname{Trd}(xy)$.

**Proof.** For $y = 1$ the two forms give $B_N(x, 1) = \tfrac{1}{2}(x + \bar x) = \tfrac{1}{2}\operatorname{Trd}(x)$ and $T_{\operatorname{red}}(x, 1) = \operatorname{Trd}(x)$, so any constant of proportionality would have to be $\tfrac{1}{2}$. Equality would then require $\operatorname{Trd}(x\bar y) = \operatorname{Trd}(xy)$ for all $x, y$, that is $\operatorname{Trd}\bigl(x(\bar y - y)\bigr) = 0$. With $x = y = e_1$ this reads $\operatorname{Trd}\bigl(-2e_1^2\bigr) = \operatorname{Trd}(2) = 4 \neq 0$, a contradiction. $\square$

**Example (the biquaternions).** For $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} \cong M_2(\mathbb{C})$ the reduced norm is the determinant and the regular norm is its square; the norm form $N(\tilde Q) = \tilde Q\bar{\tilde Q} = \sum_\mu Q_\mu^2$ is exactly the reduced norm. It is $\mathbb{C}$-valued, isotropic, and vanishes on the zero divisors, and its nonzero zeros are precisely the matrices of rank one. The Hermitian conjugation ${}^{\dagger}$ of that algebra makes $T_{\operatorname{red}}(\tilde P, \tilde Q) = \operatorname{Trd}(\tilde P \tilde Q)$ a symmetric $\mathbb{C}$-bilinear form, while the form $\operatorname{Trd}(\tilde P \tilde Q^{\dagger})$ is complex-Hermitian and positive definite on the underlying real space; the two are related by the conjugation ${}^{\dagger}$.

## Summary

An **involution** of a ring $A$ is an anti-automorphism $\sigma$ with $\sigma^2 = \mathrm{id}$; its fixed ring $A^\sigma$ contains $1$. It is of the **first kind** if it fixes the centre and of the **second kind** otherwise; over a field, an involution of the second kind has the field fixed pointwise of index two. Examples include complex conjugation on $\mathbb{C}$, quaternion conjugation on $\mathbb{H}$ (and its three extensions to the biquaternions $\mathbb{B}$), the transpose on a matrix ring, and the canonical involutions of the split complex numbers $\mathbb{D}$ and the dual numbers $\mathbb{D}'$.

Over a field of characteristic not two, an involution of a finite-dimensional algebra decomposes it into symmetric and skew parts, $A = \mathrm{Sym}(A, \sigma)\oplus \mathrm{Skew}(A, \sigma)$, with $\mathrm{Sym}(A,\sigma) = A^\sigma$. For an involution of the first kind on a central simple algebra of degree $n$ the dimension of the symmetric part is one of the two numbers $n(n+1)/2$ and $n(n-1)/2$, and the involution is accordingly of **orthogonal** type or of **symplectic** type; these are the only two possibilities. Transposition on $M_n$ is orthogonal, while for even $n$ the involution $X \mapsto JX^{T}J^{-1}$ with $J$ the standard alternating matrix is symplectic. The **adjoint involution** of a non-degenerate symmetric bilinear form is orthogonal and that of a non-degenerate alternating form is symplectic, which is the origin of the two names; the assignment $f \mapsto Gf$ identifies the self-adjoint elements with the symmetric, respectively the alternating, matrices.

A **$\sigma$-sesquilinear** form on a right $A$-module satisfies $s(xa, yb) = \sigma(a)s(x, y)b$. It is **Hermitian** if $s(x, y) = \sigma(s(y, x))$ and **skew-Hermitian** if the sign is reversed. The **diagonal** $q(x) = s(x, x)$ of a Hermitian form takes values in the fixed ring $A^\sigma$ and satisfies $q(xa) = \sigma(a)q(x)a$, so on central fixed scalars it is homogeneous of degree two; its polar expression is $s(x, y) + \sigma(s(x, y))$, and it is written accordingly as the **diagonal form**, to distinguish it from the trace form of an algebra. The **radical** $\operatorname{rad}(s) = \{x: s(x, y) = 0$ for all $y\}$ is the kernel of the Gram matrix $H$ in the free case, so $s$ is non-degenerate exactly when $H$ is invertible; the isometry group is then the unitary group of *The Unitary and Symplectic Groups*. The Witt-type extension and cancellation theorems hold in this setting by Dieudonné's theorem for Hermitian forms over division rings, with the exception of characteristic two, where the phenomena reappear.

For a finite-dimensional unital algebra $A$ over a field, the **regular norm** $N(x) = \det(m_x)$ is multiplicative of degree $\dim_F A$, and the **trace form** $T(x, y) = \operatorname{Tr}(m_{xy})$ is symmetric bilinear with associated quadratic form $\operatorname{Tr}(x^2)$. For a field extension it is $T(x, y) = \operatorname{Tr}_{K/F}(xy)$. For a central simple algebra of degree $d$ the **reduced trace** and **reduced norm** are the trace and determinant of the image of $x$ in $M_d(\bar F)$, equivalently $\operatorname{Trd}(x) = \operatorname{Tr}(m_x)/d$ and $\operatorname{Nrd}(x)^d = N(x)$ when $d$ is invertible; the reduced norm is quadratic exactly when $d = 2$, that is for a quaternion algebra, where its polar form is $\tfrac{1}{2}\operatorname{Trd}(x\bar y)$, which is not the reduced trace form $\operatorname{Trd}(xy)$. The norms of the complex, quaternion and biquaternion algebras are instances, computed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Ring, possibly non-commutative; usually a finite-dimensional $F$-algebra |
| $F$, $K$ | Fields |
| $\sigma$ | Involution of $A$ |
| $A^\sigma$ | Fixed ring of $\sigma$ |
| $Z(A)$ | Centre of $A$ |
| $M$ | Right $A$-module |
| $s(x, y)$ | $\sigma$-sesquilinear form |
| $q(x) = s(x, x)$ | Diagonal (quadratic) form of a Hermitian form |
| $H$ | Hermitian Gram matrix, $H_{ij} = s(e_i, e_j)$ |
| $H^{\dagger} = \sigma(H)^T$ | Hermitian transpose |
| $\bar{\cdot}$ | Quaternion conjugation; a conjugation on $\mathbb{B}$, $\mathbb{D}$, $\mathbb{D}'$ |
| ${}^{*}$ | Complex conjugation of coefficients |
| ${}^{\dagger}$ | Hermitian conjugation, ${}^{\dagger} = \bar{\cdot}\circ{}^{*}$ |
| $\mathrm{Sym}(A, \sigma)$, $\mathrm{Skew}(A, \sigma)$ | Symmetric and skew elements, $A = \mathrm{Sym}\oplus\mathrm{Skew}$ |
| $\sigma_b$, $G$ | Adjoint involution of a form $b$; its Gram matrix |
| $J$ | Standard alternating matrix $\begin{pmatrix} 0 & I \\ -I & 0\end{pmatrix}$ |
| $\operatorname{rad}(s)$ | Radical of the form $s$ |
| $m_x$ | Left multiplication by $x$ |
| $N(x) = \det(m_x)$ | Regular norm |
| $\operatorname{Tr}(x) = \operatorname{Tr}(m_x)$ | Regular trace |
| $T(x, y) = \operatorname{Tr}(m_{xy})$ | Trace form |
| $\operatorname{Trd}$, $\operatorname{Nrd}$ | Reduced trace and reduced norm |
| $T_{\operatorname{red}}(x, y) = \operatorname{Trd}(xy)$ | Reduced trace form |
| $d$ | Degree of a central simple algebra, $\dim_F A = d^2$ |
| $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}, \mathbb{D}, \mathbb{D}'$ | Real, complex, quaternion, biquaternion, split complex, dual numbers |



## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for involutions, sesquilinear forms and hermitian forms over rings.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the Hermitian theory over division rings and the unitary groups.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the trace form and the reduced norm.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular norm, the reduced norm and central simple algebras.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for involutions of the first and second kind and their classification.
