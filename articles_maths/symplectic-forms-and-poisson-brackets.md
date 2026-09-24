
# __Symplectic Forms and Poisson Brackets__

## Introduction

Among the alternating bilinear forms on a module, the nondegenerate ones occupy a distinguished place. A **symplectic form** is a nondegenerate alternating form on a finite-dimensional vector space, and the space on which it lives is necessarily even-dimensional and, after a change of basis, looks like the standard form on $K^{2n}$ that pairs $n$ coordinates with $n$ others. This normal form is the linear Darboux theorem; the automorphisms preserving the form constitute the **symplectic group** $Sp(2n, K)$, which is contained in the special linear group because the Pfaffian forces the determinant to be one. The isotropic subspaces of a symplectic space, and the maximal ones, the Lagrangians, form one of the basic families of classical geometry.

A symplectic form also makes the commutative algebra of functions on the space into a Lie algebra: the **Poisson bracket** $\{f, g\}$ is a derivation in each argument, so it is a bracket on a commutative algebra, and the Jacobi identity for it is the single identity that makes the bracket a Lie bracket. The Hamiltonian vector fields are the derivations produced by the bracket, the map $f \mapsto X_f$ is a homomorphism of Lie algebras onto them, and its kernel is the constants. Finally, the Poisson bracket is the first-order term of the commutator of a formal deformation of the commutative product, the star product; in this precise sense a symplectic space is the classical limit of a noncommutative associative algebra.

This article is algebraic throughout: a symplectic form is a form on a module and a Poisson bracket is a bracket on a commutative algebra. Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$ and $K$ denotes a field of characteristic different from $2$ unless a statement says otherwise; $V$ is a free $K$-module of finite rank, that is, a finite-dimensional vector space, and $n$ always denotes half its dimension when a symplectic structure is present, so that $\dim V = 2n$. At the few points where the base is a general commutative ring they are flagged; the alternating-form remark of *Exterior Powers*, that alternation is the condition available over every ring while skew-symmetry needs $2$ invertible, explains why the definitions below are stated through $\omega(u,u)=0$. No physics is invoked.

The notation of *Exterior Powers*, *The Exterior Algebra* and *The Determinant and Alternating Forms* is kept: $\Lambda^n V$ is the $n$-th exterior power, a $2$-form is an element of $\Lambda^2(V^*)$, and the determinant is the scalar action on $\Lambda^{2n}V$.

## Alternating Bilinear Forms

### Bilinear, Symmetric and Alternating Forms

**Definition.** Let $V$ be a free $K$-module of finite rank. A **bilinear form** on $V$ is a bilinear map $g : V \times V \to K$. It is **symmetric** if $g(u, v) = g(v, u)$ for all $u, v \in V$, and **alternating** if

$$
\omega(u, u) = 0
$$

for all $u \in V$. An alternating bilinear form is also called a **$2$-form**, or a **skew form**.

**Proposition.** Let $\omega$ be an alternating bilinear form. Then $\omega(u, v) = -\omega(v, u)$ for all $u, v \in V$. Conversely, if $2$ is invertible in $K$ and $\omega(u, v) = -\omega(v, u)$ for all $u, v$, then $\omega$ is alternating.

**Proof.** Expanding $0 = \omega(u + v, u + v)$ by bilinearity gives $\omega(u, u) + \omega(u, v) + \omega(v, u) + \omega(v, v) = \omega(u, v) + \omega(v, u)$, so the first claim follows. For the second, put $u = v$ in the skew-symmetry to obtain $\omega(u, u) = -\omega(u, u)$, that is $2\omega(u, u) = 0$, and invertibility of $2$ gives $\omega(u, u) = 0$. $\square$

**Remark.** Over a field of characteristic $2$ skew-symmetry and symmetry coincide, and the alternating condition is strictly stronger; the symplectic theory is stated through alternation so that it is correct in every characteristic. Over characteristic different from $2$ the two notions agree and the reader may substitute skew-symmetry everywhere.

### The Matrix of a Form and the Radical

**Definition.** Let $\mathcal{E} = (e_1, \ldots, e_m)$ be a basis of $V$. The **matrix of $\omega$** in this basis is $\Omega = (\omega_{ij})$ with $\omega_{ij} = \omega(e_i, e_j)$, so that

$$
\omega(u, v) = u^{\mathsf{T}} \Omega\, v
$$

for the coordinate columns $u, v \in K^m$. The form is alternating precisely when $\Omega$ is **alternating**, $\Omega^{\mathsf{T}} = -\Omega$, a condition that forces the diagonal entries to be zero when $2$ is invertible.

**Definition.** The **radical** of a bilinear form $\omega$ on $V$ is

$$
\operatorname{rad}(\omega) = \{u \in V : \omega(u, v) = 0 \text{ for all } v \in V\}.
$$

The form is **nondegenerate** if $\operatorname{rad}(\omega) = 0$.

**Proposition.** Let $\Omega$ be the matrix of $\omega$ in a basis. Then $u \in \operatorname{rad}(\omega)$ if and only if $\Omega u = 0$. Consequently $\omega$ is nondegenerate precisely when $\Omega$ is invertible, and in that case the rank of $\omega$, defined as the rank of $\Omega$, equals $\dim V$.

**Proof.** By definition $u \in \operatorname{rad}(\omega)$ means $u^{\mathsf{T}}\Omega v = 0$ for all coordinate vectors $v$, equivalently $u^{\mathsf{T}}\Omega = 0$, equivalently $\Omega u = 0$ because $\Omega^{\mathsf{T}} = -\Omega$. $\square$

## The Standard Symplectic Form

### Definition on $K^{2n}$

**Definition.** The **standard symplectic form** on $K^{2n}$, with coordinates written $(x_1, \ldots, x_n, y_1, \ldots, y_n)$, is

$$
\omega_0(u, v) = \sum_{i=1}^{n} (x_i v_{y_i} - y_i v_{x_i}),
$$

where $u = (x_1, \ldots, x_n, y_1, \ldots, y_n)$ and $v = (v_{x_1}, \ldots, v_{x_n}, v_{y_1}, \ldots, v_{y_n})$. Its matrix in the standard basis is the $2n \times 2n$ block matrix

$$
J = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}.
$$

**Proposition.** $\omega_0$ is alternating and nondegenerate, and $\det(J) = 1$; hence $J$ is invertible with $J^{-1} = -J$.

**Proof.** Alternation is immediate from the definition: $\omega_0(u, u) = \sum_i (x_i y_i - y_i x_i) = 0$. For nondegeneracy, suppose $\omega_0(u, v) = 0$ for all $v$. Evaluating on the basis vector $e_i$ of the $x$-block gives $\omega_0(u, e_i) = -y_i = 0$, and evaluating on the basis vector $f_i$ of the $y$-block gives $\omega_0(u, f_i) = x_i = 0$; hence $u = 0$. Finally $\det J = 1$: exchanging the two block columns multiplies the determinant by $(-1)^{n^2} = (-1)^n$ and leaves the block triangular matrix $\begin{pmatrix} I_n & 0 \\ 0 & -I_n\end{pmatrix}$ of determinant $\det(I_n)\det(-I_n) = (-1)^n$, so the two signs cancel. $\square$

**Remark.** The determinant can also be reached through the Pfaffian: for the coordinate order used here, $\operatorname{Pf}(J) = (-1)^{n(n-1)/2}$, whence $\det(J) = \operatorname{Pf}(J)^2 = 1$.

### Non-Degeneracy and the Symplectic Basis

**Definition.** A **symplectic form** on a finite-dimensional vector space $V$ is a nondegenerate alternating bilinear form $\omega$ on $V$. The pair $(V, \omega)$ is a **symplectic space**.

**Theorem (symplectic basis; linear Darboux).** Let $(V, \omega)$ be a symplectic space of dimension $m$ over $K$. Then $m = 2n$ is even, and there is a basis

$$
e_1, \ldots, e_n, f_1, \ldots, f_n
$$

of $V$, called a **symplectic basis**, such that

$$
\omega(e_i, e_j) = 0, \qquad \omega(f_i, f_j) = 0, \qquad \omega(e_i, f_j) = \delta_{ij}.
$$

In this basis the matrix of $\omega$ is $J$, so every symplectic space of dimension $2n$ is isomorphic to $(K^{2n}, \omega_0)$.

**Proof.** If $V = 0$ there is nothing to prove. Otherwise choose $e_1 \neq 0$. Since $\omega$ is nondegenerate there is $f_1$ with $\omega(e_1, f_1) \neq 0$; replacing $f_1$ by $\omega(e_1, f_1)^{-1} f_1$ gives $\omega(e_1, f_1) = 1$. The restriction of $\omega$ to the orthogonal complement $W = \langle e_1, f_1\rangle^{\perp}$ is alternating, and it is nondegenerate: if $w \in W$ is orthogonal to all of $W$, then $w$ is orthogonal to $e_1, f_1$ as well, because $w \in W$, and every element of $V$ is a combination of $e_1, f_1$ and an element of $W$, so $w \in \operatorname{rad}(\omega) = 0$. Moreover $V = \langle e_1, f_1\rangle \oplus W$: any $v$ can be corrected by a multiple of $f_1$ and a multiple of $e_1$ to land in $W$, since $\omega(e_1, v)$ and $\omega(f_1, v)$ can be adjusted to zero, and the sum is direct because $\langle e_1, f_1\rangle \cap W = 0$. Induction on $\dim V$ now applies to $W$, producing $e_2, \ldots, e_n, f_2, \ldots, f_n$. $\square$

**Corollary.** A symplectic space has even dimension, and a nondegenerate alternating form exists on $V$ if and only if $\dim V$ is even.

### The Darboux Normal Form

The theorem says that a symplectic form has no invariants beyond its dimension: there is no analogue of the signature of a symmetric form. Every symplectic form of dimension $2n$ is equivalent to $\omega_0$. This rigidity is the **linear Darboux normal form**, and it is the reason the symplectic group is a single family rather than a family depending on a form: all symplectic groups of the same rank are conjugate inside $GL_{2n}(K)$.

## The Symplectic Group

### Definition and Matrix Conditions

**Definition.** Let $(V, \omega)$ be a symplectic space. The **symplectic group** is

$$
Sp(V, \omega) = \{A \in GL(V) : \omega(Au, Av) = \omega(u, v) \ \text{for all } u, v \in V\}.
$$

For $V = K^{2n}$ with the standard form one writes $Sp(2n, K) = \{A \in GL_{2n}(K) : A^{\mathsf{T}} J A = J\}$.

**Proposition.** $Sp(V, \omega)$ is a subgroup of $GL(V)$, and $Sp(2n, K)$ is the subgroup of $GL_{2n}(K)$ defined by the polynomial equations $A^{\mathsf{T}} J A = J$.

**Proof.** The identity preserves $\omega$; if $A$ and $B$ preserve $\omega$ then so does $AB$, since $\omega(ABu, ABv) = \omega(Bu, Bv) = \omega(u, v)$; and if $A$ preserves $\omega$ then so does $A^{-1}$, applying the preservation to $A^{-1}u, A^{-1}v$. The matrix description is the same condition written in the standard basis. $\square$

### Determinant One

**Theorem.** Every $A \in Sp(2n, K)$ has $\det(A) = 1$. Hence $Sp(2n, K) \subseteq SL_{2n}(K)$.

**Proof.** Taking determinants in $A^{\mathsf{T}} J A = J$ gives $(\det A)^2 \det J = \det J$, and $\det J = 1 \neq 0$, so $(\det A)^2 = 1$ and $\det A = \pm 1$. To rule out $-1$ one uses the Pfaffian identity established in the section *The Pfaffian and the Volume Form* below: the Pfaffian is multiplicative in the sense $\operatorname{Pf}(A^{\mathsf{T}} \Omega A) = \det(A)\operatorname{Pf}(\Omega)$ for every alternating $\Omega$ and every $A$, and with $\Omega = J$ and $A^{\mathsf{T}} J A = J$ this gives $\operatorname{Pf}(J) = \det(A)\operatorname{Pf}(J)$. Since $\operatorname{Pf}(J) = (-1)^{n(n-1)/2} \neq 0$, it follows that $\det(A) = 1$. $\square$

### The Lie Algebra $\mathfrak{sp}(2n, K)$

**Definition.** The **symplectic Lie algebra** is

$$
\mathfrak{sp}(2n, K) = \{X \in \mathfrak{gl}(2n, K) : X^{\mathsf{T}} J + J X = 0\}.
$$

**Proposition.** $\mathfrak{sp}(2n, K)$ is a Lie subalgebra of $\mathfrak{gl}(2n, K)$ under the commutator bracket, of dimension $n(2n+1)$, and it consists of those $X$ for which $JX$ is symmetric. It is the tangent space at the identity of $Sp(2n, K)$, equivalently the Lie algebra of the symplectic group in the sense of *Lie Groups*.

**Proof.** Differentiating the defining equations $A^{\mathsf{T}} J A = J$ along a path $A(t) = I + tX + O(t^2)$ gives $X^{\mathsf{T}} J + J X = 0$, so the tangent space is contained in the displayed set; the two sides have the same dimension because the map $X \mapsto JX$ identifies the solution set with the symmetric matrices, which form a subspace of dimension $\binom{2n+1}{2} = n(2n+1)$. Closure under the commutator is the usual one: if $X^{\mathsf{T}}J + JX = 0$ and $Y^{\mathsf{T}}J + JY = 0$, then $[X,Y]^{\mathsf{T}}J + J[X,Y] = 0$, as one checks by expanding. $\square$

### Order over a Finite Field

**Proposition.** For a prime power $q$ one has

$$
|Sp(2n, \mathbb{F}_q)| = q^{n^2} \prod_{i=1}^{n} (q^{2i} - 1).
$$

**Proof.** Count the symplectic bases of $\mathbb{F}_q^{2n}$. The first vector $e_1$ may be any nonzero vector, of which there are $q^{2n} - 1$; having chosen $e_1$, the vector $f_1$ must satisfy $\omega(e_1, f_1) = 1$, a single nonhomogeneous linear condition, which has $q^{2n-1}$ solutions. Continuing, once $e_1, f_1, \ldots, e_{i-1}, f_{i-1}$ have been chosen, let $W_{i-1}$ be their orthogonal complement, of dimension $2n - 2i + 2$; the vector $e_i$ must lie in $W_{i-1}$ and be nonzero, giving $q^{2n-2i+2} - 1$ choices, and then $f_i$ must satisfy the single nonhomogeneous condition $\omega(e_i, f_i) = 1$ inside $W_{i-1}$, an affine hyperplane of $q^{2n-2i+1}$ elements. Multiplying,

$$
|Sp(2n, \mathbb{F}_q)| = \prod_{i=1}^{n} (q^{2n-2i+2} - 1)\, q^{2n-2i+1} = q^{\sum_{i=1}^n (2n-2i+1)} \prod_{i=1}^{n}(q^{2i} - 1),
$$

and the exponent is $\sum_{i=1}^n (2n - 2i + 1) = n^2$. $\square$

**Example.** For $n = 1$, $Sp(2, \mathbb{F}_q) = SL_2(\mathbb{F}_q)$, and the formula gives $q(q^2 - 1)$, which is the order of $SL_2(\mathbb{F}_q)$. Indeed every $2 \times 2$ matrix of determinant $1$ preserves the alternating form up to scalar, and the scalar is fixed to $1$ by the determinant.

## Isotropic and Lagrangian Subspaces

### Isotropic Subspaces

**Definition.** Let $(V, \omega)$ be a symplectic space. A subspace $W \subseteq V$ is **isotropic** if $\omega(u, v) = 0$ for all $u, v \in W$; it is **coisotropic** if $W^{\perp} \subseteq W$, where $W^{\perp} = \{u : \omega(u, w) = 0 \text{ for all } w \in W\}$; and it is **Lagrangian** if it is isotropic and $\dim W = \tfrac{1}{2}\dim V$.

**Proposition.** For every subspace $W$ of a symplectic space $V$ one has $\dim W + \dim W^{\perp} = \dim V$. If $W$ is isotropic then $\dim W \leq \tfrac{1}{2}\dim V$.

**Proof.** The linear map $V \to W^*$, $v \mapsto \omega(v, \cdot)|_W$, has kernel $W^{\perp}$; it is onto, because a linear functional on $W$ extends to $V$ and is represented by an element of $V$ by nondegeneracy of $\omega$. Hence $\dim W^{\perp} = \dim V - \dim W$. If $W$ is isotropic then $W \subseteq W^{\perp}$, so $\dim W \leq \dim W^{\perp} = \dim V - \dim W$. $\square$

### Lagrangian Subspaces

**Theorem.** Let $(V, \omega)$ be symplectic of dimension $2n$. A subspace $W$ is Lagrangian if and only if it is isotropic of dimension $n$, and Lagrangian subspaces exist.

**Proof.** An isotropic subspace of dimension $n$ is Lagrangian by definition. Conversely a Lagrangian is isotropic of dimension $n$. For existence, the span $\langle e_1, \ldots, e_n\rangle$ of the first half of a symplectic basis is isotropic, since $\omega(e_i, e_j) = 0$. $\square$

**Example.** In $(K^{2n}, \omega_0)$ the subspaces $\langle e_1, \ldots, e_n\rangle$ and $\langle f_1, \ldots, f_n\rangle$ are Lagrangian, and so is the diagonal $\langle e_i + f_i : i = 1, \ldots, n\rangle$.

### The Lagrangian Grassmannian

**Definition.** The set of all Lagrangian subspaces of $(V, \omega)$ is the **Lagrangian Grassmannian**, written $\operatorname{Lag}(V)$. The symplectic group acts transitively on it, and the stabiliser of a Lagrangian is a maximal parabolic subgroup, so $\operatorname{Lag}(V) \cong Sp(V, \omega)/P$.

**Proposition.** $\operatorname{Lag}(V)$ is a smooth projective variety of dimension $\tfrac{1}{2} n(n+1)$. Over $\mathbb{F}_q$ its cardinality is $\prod_{i=1}^{n}(q^i + 1)$.

**Proof.** The count over $\mathbb{F}_q$ is obtained by counting the ordered isotropic tuples: the number of ordered symplectic bases whose first $n$ vectors span a given Lagrangian is $|P|$, and dividing $|Sp(2n, \mathbb{F}_q)|$ by $|P|$ gives $\prod_{i=1}^{n}(q^i + 1)$ by a direct computation. The leading power of $q$ in that product is $q^{n(n+1)/2}$, which is the dimension of the variety. $\square$

## The Pfaffian and the Volume Form

### The Pfaffian of an Alternating Form

**Definition.** Let $\Omega$ be the matrix of an alternating bilinear form on a $2n$-dimensional space in a basis. The **Pfaffian** of $\Omega$ is the polynomial

$$
\operatorname{Pf}(\Omega) = \frac{1}{2^n n!} \sum_{\sigma \in S_{2n}} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} \Omega_{\sigma(2i-1), \sigma(2i)},
$$

an integral polynomial in the entries, defined over every commutative ring.

**Theorem (Pfaffian identities).** For every alternating $\Omega$ and every $A \in GL_{2n}(K)$,

$$
\operatorname{Pf}(A^{\mathsf{T}} \Omega A) = \det(A)\, \operatorname{Pf}(\Omega), \qquad \det(\Omega) = \operatorname{Pf}(\Omega)^2.
$$

**Proof.** Both identities are polynomial identities with integer coefficients in the entries of $\Omega$ and $A$, so it suffices to establish them over a field of characteristic $0$. In the coordinates $x_1, \ldots, x_n, y_1, \ldots, y_n$ of the preceding sections the matrix of the standard form is the block matrix $J = \begin{pmatrix} 0 & I_n \\ -I_n & 0\end{pmatrix}$, whose Pfaffian is $\operatorname{Pf}(J) = (-1)^{n(n-1)/2}$: the only nonvanishing summands pair $x_i$ with $y_i$, and the sign is the parity of the permutation that sorts these pairs, since $\operatorname{Pf}$ is unchanged by an even reordering of the variables and changes sign under an odd one. Conjugating by the permutation matrix that reorders the coordinates as $x_1, y_1, x_2, y_2, \ldots$ gives the block diagonal matrix $J'$ with diagonal blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$, for which $\det(J') = 1$ and $\operatorname{Pf}(J') = 1$, each nonvanishing summand contributing $+1$. For the change-of-basis rule, use the equivalent definition of the Pfaffian as the scalar appearing in

$$
\frac{1}{2^n n!}\Bigl(\sum_{i,j}\Omega_{ij}\,x_i \wedge x_j\Bigr)^{n} = \operatorname{Pf}(\Omega)\, x_1 \wedge \cdots \wedge x_{2n},
$$

which agrees with the explicit sum above because the $n$-fold wedge counts each partition of $\{1, \ldots, 2n\}$ into unordered pairs $n!$ times and the ordered sum counts it $2^n n!$ times. Writing $\Omega' = A^{\mathsf{T}}\Omega A$ for the matrix of the form in the coordinates $y = Ax$ gives $\sum \Omega'_{ij}x_i\wedge x_j = \sum\Omega_{ij}y_i\wedge y_j$, and $y_1\wedge\cdots\wedge y_{2n} = \det(A)x_1\wedge\cdots\wedge x_{2n}$; taking $n$-th powers of both sides of this identity and comparing the coefficients of $x_1\wedge\cdots\wedge x_{2n}$ gives $\operatorname{Pf}(A^{\mathsf{T}}\Omega A) = \det(A)\operatorname{Pf}(\Omega)$. For the second identity, the normal form theorem supplies $B$ with $\Omega = B^{\mathsf{T}}JB$, so with $J' = P^{\mathsf{T}}JP$ as above one has $J = PJ'P^{\mathsf{T}}$ and hence $\Omega = C^{\mathsf{T}}J'C$ for $C = P^{\mathsf{T}}B$, whence $\operatorname{Pf}(\Omega) = \det(C)\operatorname{Pf}(J') = \det(C)$ and $\det(\Omega) = \det(C)^2\det(J') = \det(C)^2$; hence $\det(\Omega) = \operatorname{Pf}(\Omega)^2$. $\square$

**Corollary.** A symplectic form is nondegenerate precisely when its Pfaffian is nonzero; over a field, an alternating matrix of even size is invertible exactly when its Pfaffian is nonzero.

### The Volume Form and the Symplectic Group

**Definition.** Let $(V, \omega)$ be symplectic of dimension $2n$. The **Liouville form** is the top-degree form

$$
\frac{1}{n!}\, \omega^{\wedge n} \in \Lambda^{2n}(V^*),
$$

which is nonzero because $\omega$ is nondegenerate; in a symplectic basis, where the matrix of $\omega$ is the block diagonal matrix with blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$, it equals $e^1 \wedge f^1 \wedge \cdots \wedge e^n \wedge f^n$, a volume form on $V$.

**Proposition.** Every $A \in Sp(V, \omega)$ preserves the Liouville form, and consequently $\det(A) = 1$; the volume of a symplectic space is preserved by its symplectic automorphisms.

**Proof.** If $A$ preserves $\omega$ then $A$ preserves $\omega^{\wedge n}$ and hence its scalar multiple $\omega^{\wedge n}/n!$, so $\det(A) = 1$ by the determinant-one theorem. $\square$

**Remark.** The Liouville form is the symplectic analogue of a volume form, and the inclusion $Sp \subseteq SL$ says that symplectic transformations preserve it. The Pfaffian is the square root of the determinant, defined only for alternating matrices, and it is the algebraic reason for the restriction to determinant one.

## The Poisson Bracket

### Derivations and the Jacobi Identity

**Definition.** Let $A$ be a commutative $R$-algebra with product written $fg$. A **Poisson bracket** on $A$ is an $R$-bilinear map $\{\cdot, \cdot\} : A \times A \to A$ such that for all $f, g, h \in A$:

**(a)** $\{f, g\} = -\{g, f\}$ (skew-symmetry);

**(b)** $\{f, gh\} = \{f, g\}h + g\{f, h\}$ (the Leibniz rule, or derivation property);

**(c)** $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$ (the Jacobi identity).

The triple $(A, \cdot, \{\cdot, \cdot\})$ is a **Poisson algebra**. Over a field of characteristic different from $2$ condition (a) is equivalent to $\{f, f\} = 0$.

**Proposition.** In a Poisson algebra, for each $f$ the map $\operatorname{ad}_f = \{f, \cdot\} : A \to A$ is a derivation of the commutative product, and the map $f \mapsto \operatorname{ad}_f$ is a homomorphism of Lie algebras

$$
\operatorname{ad} : (A, \{\cdot, \cdot\}) \to \operatorname{Der}(A),
$$

where $\operatorname{Der}(A)$ is the Lie algebra of derivations of $A$ under the commutator. Hence $A$ is a Lie algebra under $\{\cdot, \cdot\}$, and its image in $\operatorname{Der}(A)$ consists of the **Hamiltonian derivations**.

**Proof.** The derivation property is (b) rewritten. The map $\operatorname{ad}$ is $R$-linear, and the Jacobi identity (c) reads $\operatorname{ad}_{\{f,g\}} = [\operatorname{ad}_f, \operatorname{ad}_g]$, which is exactly the statement that $\operatorname{ad}$ preserves the bracket. $\square$

### The Bracket from a Symplectic Form

Let $V$ be a symplectic space of dimension $2n$ over $K$ with form $\omega$, and let $A$ be a commutative $K$-algebra of functions on $V$ on which the partial derivatives with respect to a basis act; the standard algebraic example is the polynomial algebra $A = K[x_1, \ldots, x_n, y_1, \ldots, y_n]$, with $\omega = \omega_0$ in the coordinates of the previous sections.

**Definition.** For $f \in A$ the **Hamiltonian vector field** of $f$ is the derivation $X_f$ determined by

$$
\omega(X_f, Y) = Y(f) \qquad \text{for all derivations } Y,
$$

equivalently $X_f = \sum_{i,j} \omega^{ij}\, \partial_i f\, \partial_j$, where $(\omega^{ij})$ is the inverse matrix of $(\omega_{ij})$ and $\partial_i$ runs over the coordinate derivations. The **Poisson bracket** of $f, g \in A$ is

$$
\{f, g\} = \omega(X_f, X_g) = X_g(f) = -X_f(g).
$$

Since $X_g = \sum_{i,j} \omega^{ij}\,\partial_j g\,\partial_i$, the bracket in coordinates is

$$
\{f, g\} = \sum_{i,j} \omega^{ij}\, \partial_j f\, \partial_i g,
$$

the index of the inverse matrix attached to the coordinate index of $g$ in the first slot and to that of $f$ in the second, as the equality $\{f,g\} = X_g(f)$ requires. In the standard coordinates, with $\omega^{ij}$ the entries of $-J$ for the form $\omega_0$, this is

$$
\{f, g\} = \sum_{i=1}^{n} \left( \frac{\partial f}{\partial x_i}\frac{\partial g}{\partial y_i} - \frac{\partial f}{\partial y_i}\frac{\partial g}{\partial x_i} \right).
$$

**Theorem.** The bracket so defined is a Poisson bracket on $A$: it is bilinear, alternating, a derivation in each argument, and satisfies the Jacobi identity. The map $f \mapsto X_f$ is a homomorphism of Lie algebras onto the Hamiltonian derivations, with kernel the constants $K \cdot 1$ when the derivatives separate constants.

**Proof.** Bilinearity and alternation are immediate from the definition and from $\omega$ being alternating. For the derivation property, $X_{gh} = g X_h + h X_g$ because $d(gh) = g\, dh + h\, dg$ and $\omega$ is bilinear; substituting into $\{f, gh\} = \omega(X_f, X_{gh})$ gives (b). For the Jacobi identity, expand in coordinates: the bracket is $\sum_{ij}\omega^{ij}\partial_j f\, \partial_i g$ with $\omega^{ij}$ constant and alternating, so the bracket of two coordinate functions is the constant $\{x_i, x_j\} = -\omega^{ij}$, and the triple bracket of coordinate functions vanishes. The expression $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\}$ is a derivation in each of its three arguments, as the Leibniz rule (b) shows by expanding a product in that argument, and it vanishes on the coordinate functions; since the coordinate functions generate $A$, it vanishes identically. The remaining statements follow from the proposition above, the kernel of $f \mapsto X_f$ consisting exactly of the functions with all first partial derivatives zero. $\square$

**Remark.** In the general setting of a symplectic manifold the constant-coefficient computation is replaced by the closedness condition $d\omega = 0$, and the Jacobi identity for the bracket is equivalent to $d\omega = 0$. The algebraic content is the same: the bracket is a derivation in each slot, and the Jacobi identity is the statement that the derivations it produces commute up to the bracket.

### The Bracket as a Lie Algebra Structure

**Corollary.** With the Poisson bracket, $A$ is a Lie algebra over $K$, and the Hamiltonian vector fields form a Lie subalgebra $\operatorname{Ham}(V)$ of $\operatorname{Der}(A)$. There is a short exact sequence of Lie algebras

$$
0 \longrightarrow K \cdot 1 \longrightarrow (A, \{\cdot, \cdot\}) \xrightarrow{\ f \mapsto X_f\ } \operatorname{Ham}(V) \longrightarrow 0,
$$

in which the constants constitute the centre of the bracket, since $\{f, g\} = 0$ for all $g$ exactly when $X_f = 0$ exactly when $f$ is constant.

**Example.** For $n = 1$ and $A = K[x, y]$, the bracket is $\{f, g\} = f_x g_y - f_y g_x$, the Jacobian determinant of the pair $(f, g)$ with respect to $(x, y)$. The coordinate functions satisfy $\{x, y\} = 1$, and the monomials $x^a y^b$ span $A$; the bracket of two monomials is again a monomial times a scalar, $\{x^a y^b, x^c y^d\} = (ad - bc)\, x^{a+c-1} y^{b+d-1}$, so the bracket carries the monomial grading into a grading shifted by two: the degree of $\{f, g\}$ is two less than the sum of the degrees of $f$ and $g$ when both are homogeneous, and the bracket of two linear functions is constant. The Hamiltonian vector field of $f$ is $X_f = f_y \partial_x - f_x \partial_y$, the infinitesimal rotation generated by $f$.

## Formal Deformation to a Commutator Algebra

The Poisson bracket is the first-order term of a noncommutative associative product, in a sense made precise by deformation.

### The Star Product

Let $A = K[x_1, \ldots, x_n, y_1, \ldots, y_n]$ and let $\omega^{ij}$ be the constant matrix inverse to the symplectic form. On the algebra $A[[\hbar]]$ of formal power series in a central parameter $\hbar$, define the **star product**

$$
f * g = \sum_{r \geq 0} \frac{(-\hbar)^r}{r!} \sum_{i_1, j_1, \ldots, i_r, j_r} \omega^{i_1 j_1} \cdots \omega^{i_r j_r}\, \partial_{i_1} \cdots \partial_{i_r} f\; \partial_{j_1} \cdots \partial_{j_r} g.
$$

The sum is finite on polynomials, because derivatives of sufficiently high order vanish, so the series is well defined on $A$ and extends to $A[[\hbar]]$.

**Theorem (Weyl–Moyal).** The star product is an associative $K[[\hbar]]$-bilinear product on $A[[\hbar]]$, with unit the constant function $1$, and it is a deformation of the commutative product:

$$
f * g = fg + \hbar\, \{f, g\} + O(\hbar^2).
$$

Only the odd powers of $\hbar$ survive in the commutator, and

$$
f * g - g * f = 2\hbar\, \{f, g\} + O(\hbar^3),
$$

so the Poisson bracket is the leading term of the commutator of the deformed product, up to the normalisation factor $2\hbar$.

**Proof.** The $r = 0$ term of the definition is $fg$ and the $r = 1$ term is $-\sum_{ij}\omega^{ij}\partial_i f \partial_j g = \sum_{ij}\omega^{ij}\partial_j f \partial_i g = \{f,g\}$, which gives the first display. The $r$-th term of $g*f$ is obtained from that of $f*g$ by exchanging $f$ and $g$ and relabelling the summation indices; for even $r$ this term is symmetric in $f, g$ and for odd $r$ it is antisymmetric, so the commutator retains only the odd powers, and its $r = 1$ term is $2\hbar\{f,g\}$. Associativity is the classical theorem of Weyl and Moyal, and is most cleanly seen by transporting the product along the Weyl map: there is a linear isomorphism from $A[[\hbar]]$ onto a space of operators under which the star product becomes operator composition, and composition is associative. $\square$

**Remark.** The theorem identifies the Poisson algebra $(A, \cdot, \{\cdot, \cdot\})$ as the classical limit of a family of noncommutative associative algebras $A_\hbar = (A[[\hbar]], *)$. The bracket is exactly the commutator of the deformation, divided by $\hbar$ and taken to leading order, so the Lie algebra structure on the functions is not an isolated algebraic accident but the shadow at order $\hbar$ of an associative product. For a general Poisson manifold the existence of a star product with the analogous property is Kontsevich's deformation-quantisation theorem; the constant-coefficient case above is the classical Weyl–Moyal product, and it is entirely algebraic.

## Summary

A symplectic form on a finite-dimensional vector space $V$ over a field $K$ of characteristic different from $2$ is a nondegenerate alternating bilinear form $\omega$. Its matrix in a basis is an invertible alternating matrix, and nondegeneracy is equivalent to the radical being zero. Every symplectic space of dimension $2n$ admits a symplectic basis $e_1, \ldots, e_n, f_1, \ldots, f_n$ with $\omega(e_i, f_j) = \delta_{ij}$ and all other pairings zero; hence the dimension is even and every symplectic form is equivalent to the standard form $\omega_0$ on $K^{2n}$, the linear Darboux normal form.

The symplectic group $Sp(V, \omega) = \{A \in GL(V) : \omega(Au, Av) = \omega(u, v)\}$ preserve the form; every element has determinant one, by the Pfaffian identity $\operatorname{Pf}(A^{\mathsf{T}}\Omega A) = \det(A)\operatorname{Pf}(\Omega)$, and the Lie algebra is $\mathfrak{sp}(2n, K) = \{X : X^{\mathsf{T}}J + JX = 0\}$ of dimension $n(2n+1)$. Isotropic subspaces have dimension at most $n$; the Lagrangians are the isotropic subspaces of dimension $n$, they form the Lagrangian Grassmannian of dimension $\tfrac{1}{2}n(n+1)$, and the Pfaffian is the square root of the determinant of an alternating matrix, so the Liouville form $\omega^{\wedge n}/n!$ is preserved by symplectic maps.

On the commutative algebra of functions on a symplectic space, the Poisson bracket is a bilinear, alternating, derivation-like bracket satisfying the Jacobi identity; it makes the functions a Lie algebra, the Hamiltonian vector fields a Lie subalgebra of the derivations, and the map $f \mapsto X_f$ a Lie algebra homomorphism with kernel the constants. Finally, the star product is an associative deformation of the commutative product whose commutator has the Poisson bracket as its leading term, so the bracket is the classical limit of a commutator algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$; the default base |
| $K$ | Field of characteristic different from $2$ where stated |
| $V$ | Finite-dimensional $K$-vector space, a free $K$-module of finite rank |
| $g$ | A bilinear form, symmetric unless stated otherwise |
| $\omega$, $\omega_0$ | Alternating $2$-form; standard symplectic form on $K^{2n}$ |
| $\Omega = (\omega_{ij})$, $\Omega^{\mathsf{T}} = -\Omega$ | Matrix of an alternating form |
| $\operatorname{rad}(\omega)$ | Radical, $\{u : \omega(u, v) = 0 \ \forall v\}$; form nondegenerate iff radical zero |
| $n$ | Half the dimension of a symplectic space, $\dim V = 2n$ |
| $J = \begin{pmatrix} 0 & I_n \\ -I_n & 0\end{pmatrix}$ | Matrix of $\omega_0$; $J^{-1} = -J$, $\det J = 1$, $\operatorname{Pf}(J) = (-1)^{n(n-1)/2}$ |
| $e_1, \ldots, e_n, f_1, \ldots, f_n$ | Symplectic basis; $\omega(e_i, f_j) = \delta_{ij}$ |
| $Sp(V, \omega)$, $Sp(2n, K)$ | Symplectic group; $A^{\mathsf{T}} J A = J$; contained in $SL$ |
| $\mathfrak{sp}(2n, K)$ | Symplectic Lie algebra, $X^{\mathsf{T}} J + J X = 0$, dimension $n(2n+1)$ |
| $W^{\perp}$ | Orthogonal complement, $\{u : \omega(u, w) = 0 \ \forall w \in W\}$ |
| Isotropic, Lagrangian | $\omega\vert_W = 0$; maximal isotropic, of dimension $n$ |
| $\operatorname{Lag}(V)$ | Lagrangian Grassmannian, dimension $\tfrac{1}{2}n(n+1)$ |
| $\operatorname{Pf}(\Omega)$ | Pfaffian; $\operatorname{Pf}(A^{\mathsf{T}}\Omega A) = \det(A)\operatorname{Pf}(\Omega)$, $\det\Omega = \operatorname{Pf}(\Omega)^2$ |
| $\omega^{\wedge n}/n!$ | Liouville form, the symplectic volume form |
| $\omega^{ij} = (\Omega^{-1})^{ij}$ | Inverse matrix of the form; $\{f,g\} = \sum_{i,j}\omega^{ij}\,\partial_j f\,\partial_i g$, equal to the entries of $-J$ in standard coordinates |
| $\{f, g\}$ | Poisson bracket; bilinear, alternating, derivational, Jacobi |
| $X_f$ | Hamiltonian vector field, $\omega(X_f, Y) = Y(f)$ |
| $\operatorname{Ham}(V)$ | Lie algebra of Hamiltonian vector fields |
| $\operatorname{Der}(A)$ | Lie algebra of derivations of $A$; $\operatorname{Ham}(V) \subseteq \operatorname{Der}(A)$ |
| $\mathcal{E} = (e_1, \ldots, e_m)$ | Ordered basis of $V$; matrices of forms are taken in it |
| $f * g$ | Star product; associative deformation with $f*g = fg + \hbar\{f,g\} + O(\hbar^2)$ and $f*g - g*f = 2\hbar\{f,g\} + O(\hbar^3)$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for alternating forms, the symplectic basis, and the Pfaffian.
- Werner Greub, *Linear Algebra* (Springer, 4th ed. 1975), for bilinear and alternating forms, nondegeneracy, and normal forms.
- Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology* (Oxford University Press, 3rd ed. 2017), for symplectic vector spaces, Lagrangian subspaces, and the linear Darboux theorem.
- Larry C. Grove, *Classical Groups and Geometric Algebra* (American Mathematical Society, 2002), for the symplectic group, its order over a finite field, and its Lie algebra.
- V. I. Arnold and Alexander B. Givental, *Symplectic Geometry*, in *Dynamical Systems IV* (Springer, 2001), for symplectic forms, the Poisson bracket, and Hamiltonian vector fields.
- Paulette Libermann and Charles-Michel Marle, *Symplectic Geometry and Analytical Mechanics* (Reidel, 1987), for the Darboux theorem and isotropic subspaces.
- Maxim Kontsevich, "Deformation Quantization of Poisson Manifolds", *Letters in Mathematical Physics* 66 (2003), for the star product and the deformation of a Poisson algebra.
- Simone Gutt, "An Explicit Construction of the Weyl Quantization" (in *Deformation Theory of Algebras and Structures*, Kluwer, 1995), for the Weyl–Moyal product and its associativity.
