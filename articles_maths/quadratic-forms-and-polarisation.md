
# __Quadratic Forms and Polarisation__

## Introduction

A **quadratic form** is a scalar-valued function of one vector that is homogeneous of degree two. The prototype is $\mathfrak{Q}(x) = x_1^2 + \cdots + x_n^2$ on $\mathbb{R}^n$, the standard Euclidean form. This article develops the theory over a commutative ring: the definition, the polar form that recovers a symmetric bilinear form from $m$, the polarisation identities and the matrix of a form, isometry of forms and the orthogonal direct sum, diagonalisation, Sylvester's law of inertia, and the classification of real and complex forms.

The passage between a quadratic form and a symmetric bilinear form is a bijection when $2$ is invertible in the base ring, and it is a genuine obstruction when $2$ is not; the first half treats the correspondence and the last section records its failure.

The base is a commutative ring $R$, and the bilinear vocabulary is that of *Bilinear Forms*: a bilinear form $B$, its Gram matrix $G$, the radical $\operatorname{rad}(B)$, and non-degeneracy as an isomorphism $M \to M^*$. We write $B$ for the symmetric bilinear form associated with a quadratic form $m$, so that $\mathfrak{Q}(v) = B(v, v)$; this fixes the convention in which the fundamental relation of the Clifford algebra reads $uv + vu = 2B(u, v)$. The number systems and the companion articles on tensor and exterior constructions are used only for the examples.

## Quadratic Forms

### Definition

Let $M$ be an $R$-module. A **quadratic form** on $M$ is a function $m : M \to R$ such that

$$
\mathfrak{Q}(rv) = r^2 \mathfrak{Q}(v) \qquad (r \in R,\ v \in M),
$$

and such that the function $B : M \times M \to R$ defined by

$$
B(u, v) = \tfrac{1}{2}\bigl(\mathfrak{Q}(u + v) - \mathfrak{Q}(u) - \mathfrak{Q}(v)\bigr)
$$

is $R$-bilinear. The form $B$ is the **polar form** of $m$, and $m$ is **homogeneous of degree two**. The definition presupposes that $2$ is invertible in $R$, so that the factor $\tfrac{1}{2}$ exists.

**Remark.** The condition that $B$ be bilinear is not a technicality. A function homogeneous of degree two need not polarise: on $\mathbb{F}_2$ the function $\mathfrak{Q}(x) = x^2$ satisfies $\mathfrak{Q}(rx) = r^2 \mathfrak{Q}(x)$, but the associated bilinear form $\mathfrak{Q}(u + v) - \mathfrak{Q}(u) - \mathfrak{Q}(v)$ vanishes identically because $(x + y)^2 = x^2 + y^2$ in characteristic $2$, so no bilinear form carries the information of $m$.

### The Polar Form

**Proposition.** If $B : M \times M \to R$ is a symmetric bilinear form, then $\mathfrak{Q}(v) = B(v, v)$ is a quadratic form with polar form $B$.

**Proof.** Homogeneity is immediate: $\mathfrak{Q}(rv) = B(rv, rv) = r^2 B(v, v) = r^2 \mathfrak{Q}(v)$. For the polar form, bilinearity and symmetry give

$$
\mathfrak{Q}(u + v) - \mathfrak{Q}(u) - \mathfrak{Q}(v) = B(u, v) + B(v, u) = 2B(u, v),
$$

so the function defined in the definition is $B$ itself.

**Corollary (the correspondence).** Let $2$ be invertible in $R$. Then the assignments $B \mapsto m$ with $\mathfrak{Q}(v) = B(v, v)$ and $m \mapsto B$ by the polar formula are mutually inverse bijections between symmetric bilinear forms on $M$ and quadratic forms on $M$.

**Proof.** The polar form of $\mathfrak{Q}(v) = B(v, v)$ is $B$ by the proposition. Conversely, if $B$ is the polar form of $m$, then

$$
B(v, v) = \tfrac{1}{2}\bigl(\mathfrak{Q}(2v) - 2q(v)\bigr) = \tfrac{1}{2}\bigl(4q(v) - 2q(v)\bigr) = \mathfrak{Q}(v),
$$

using $\mathfrak{Q}(2v) = 4q(v)$ and additivity. So the two constructions are inverse.

**Definition.** A quadratic form $m$ is **non-degenerate** if its polar form $B$ is non-degenerate in the sense of *Bilinear Forms*, that is, if $M \to M^*$, $u \mapsto B(u, -)$, is an isomorphism. Its **radical** is $\operatorname{rad}(m) = \operatorname{rad}(B)$.

**Remark.** The associated bilinear form

$$
\mathfrak{b}(u, v) = \mathfrak{Q}(u + v) - \mathfrak{Q}(u) - \mathfrak{Q}(v) = 2B(u, v)
$$

is defined without dividing by $2$ and therefore exists over any ring. Over a ring in which $2$ is a zero divisor it may carry strictly less information than $m$; the extreme case is $\mathbb{F}_2$ above, where $b = 0$ while $m \neq 0$. For this reason the quadratic form, not the bilinear form, is the primitive object in characteristic $2$, and the Clifford construction uses $m$ directly.

### The Polarisation Identities

Polarising the identity $\mathfrak{Q}(u + v) = \mathfrak{Q}(u) + \mathfrak{Q}(v) + 2B(u, v)$ gives the standard formulas relating $m$ to $B$.

**Proposition.** Let $m$ be a quadratic form with polar form $B$ and let $2$ be invertible in $R$. Then for all $u, v \in M$,

$$
\boxed{\;\mathfrak{Q}(u + v) + \mathfrak{Q}(u - v) = 2q(u) + 2q(v), \qquad \mathfrak{Q}(u + v) - \mathfrak{Q}(u - v) = 4B(u, v)\;},
$$

$$
B(u + v, u - v) = \mathfrak{Q}(u) - \mathfrak{Q}(v).
$$

**Proof.** Expanding in the polar form and using $B(u, -v) = -B(u, v)$,

$$
\mathfrak{Q}(u + v) = \mathfrak{Q}(u) + \mathfrak{Q}(v) + 2B(u, v), \qquad \mathfrak{Q}(u - v) = \mathfrak{Q}(u) + \mathfrak{Q}(v) - 2B(u, v).
$$

Adding the two gives the parallelogram law and subtracting them gives the second identity. For the third, bilinearity and symmetry give $B(u + v, u - v) = B(u, u) - B(v, v) = \mathfrak{Q}(u) - \mathfrak{Q}(v)$.

The parallelogram law and the second identity recover $B$ from $m$ in the two ways that the diagonalisation below uses: the first computes the sum $\mathfrak{Q}(u + v) + \mathfrak{Q}(u - v)$, the second the difference $\mathfrak{Q}(u + v) - \mathfrak{Q}(u - v)$.

**Corollary.** Let $2$ be invertible. If $\mathfrak{Q}(u + v) = \mathfrak{Q}(u) + \mathfrak{Q}(v)$ for all $u, v$, then $m = 0$.

**Proof.** The hypothesis says $2B(u, v) = 0$ for all $u, v$, so $B = 0$ because $2$ is invertible, and then $\mathfrak{Q}(v) = B(v, v) = 0$.

The corollary fails as soon as $2$ is not invertible: over $\mathbb{F}_2$ the form $\mathfrak{Q}(x) = x^2$ is additive and nonzero. The precise shape of the failure is the subject of the last section of this article.

### Examples

**Example (the standard forms).** On $M = R^n$,

$$
\mathfrak{Q}(x) = \sum_{i=1}^{n} x_i^2
$$

is a quadratic form with polar form $B(x, y) = \sum_i x_i y_i$. More generally, for $a_1, \ldots, a_n \in R$,

$$
\mathfrak{Q}(x) = \sum_{i=1}^{n} a_i x_i^2
$$

is a quadratic form, and its polar form has Gram matrix $\operatorname{diag}(a_1, \ldots, a_n)$.

**Example (the norms).** The norm $N(z) = z\bar{z}$ on the complex numbers is the quadratic form $a^2 + b^2$ on $\mathbb{R}^2$; its polar form is the Euclidean inner product. The norm $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ on the quaternions is the form $x_0^2 + x_1^2 + x_2^2 + x_3^2$ on $\mathbb{R}^4$. These are the standard examples of positive-definite forms and are treated systematically.

**Example (the hyperbolic plane).** On $R^2$ the form

$$
\mathfrak{Q}(x, y) = x^2 - y^2
$$

is quadratic, with polar form $B((x_1, y_1), (x_2, y_2)) = x_1 x_2 - y_1 y_2$. It is non-degenerate over a field, and it is isotropic: $\mathfrak{Q}(1, 1) = 0$.

### The Gram Matrix and Congruence

Let $M$ be free of rank $n$ with basis $e_1, \ldots, e_n$, and let $G$ be the Gram matrix of the polar form, $G_{ij} = B(e_i, e_j)$, a symmetric matrix. Writing $x = \sum_i x_i e_i$, bilinearity gives

$$
\mathfrak{Q}(x) = B(x, x) = \sum_{i,j} B(e_i, e_j)\,x_i x_j = x^{T} G\, x,
$$

where $x$ denotes the column of coordinates. The diagonal entries are the values $G_{ii} = \mathfrak{Q}(e_i)$, by the normalisation $\mathfrak{Q}(v) = B(v, v)$, and the off-diagonal entries are recovered from $m$ by

$$
2G_{ij} = \mathfrak{Q}(e_i + e_j) - \mathfrak{Q}(e_i) - \mathfrak{Q}(e_j).
$$

The two formulas together say that $m$ and $G$ determine one another when $2$ is invertible, which is the matrix form of the bijection above.

**Proposition (change of basis).** If $P$ is the matrix of a change of basis of $M$, then the Gram matrix of $m$ in the new basis is $P^{T} G P$.

**Proof.** The coordinates transform by $x = Px'$, so

$$
x^{T} G x = (Px')^{T} G (Px') = x'^{T} (P^{T} G P)\, x',
$$

and a quadratic form is determined by its matrix when $2$ is invertible.

Two symmetric matrices $G, G'$ with $G' = P^{T} G P$ for an invertible $P$ are **congruent**, so isometry classes of quadratic forms on a free module are congruence classes of symmetric matrices. Under congruence the rank of $G$ is unchanged, and $\det(P^{T} G P) = \det(P)^2 \det G$ shows that the determinant of the Gram matrix is well defined modulo squares; that residue is the discriminant of the diagonalising section below.

## The Failure of Polarisation

### The Kernel of the Polar Map

When $2$ is not invertible the map $m \mapsto B$ is not available, but the **associated form**

$$
\mathfrak{b}(u, v) = \mathfrak{Q}(u + v) - \mathfrak{Q}(u) - \mathfrak{Q}(v) = 2B(u, v)
$$

is defined over any ring, and the question is how much of $m$ it retains. Two quadratic forms with the same associated form differ by a function $c$ with

$$
c(u + v) = c(u) + c(v), \qquad c(rv) = r^2 c(v),
$$

that is, by an additive function that is homogeneous of degree two. The set of such $c$ is an $R$-module, the kernel of $m \mapsto b$. For $c$ in the kernel, additivity gives $c(2v) = 2c(v)$ while homogeneity gives $c(2v) = 4c(v)$, so $2c(v) = 0$ for every $v$; hence the kernel is zero whenever $2$ is not a zero divisor in $R$, and in particular when $2$ is invertible, by the corollary above. When $2$ is a zero divisor the kernel can be nonzero, and the classification of quadratic forms is then strictly finer than the classification of their associated bilinear forms.

**Example (the field with two elements).** Let $R = \mathbb{F}_2$ and $M = \mathbb{F}_2^n$. Every function $m : M \to \mathbb{F}_2$ with $\mathfrak{Q}(0) = 0$ is given by a polynomial in which no variable occurs with exponent greater than one, and the condition that $\mathfrak{b}$ be bilinear forces every monomial to have degree at most two: a monomial $x_{i_1} \cdots x_{i_d}$ with $d \geq 3$ fails the bilinearity of $\mathfrak{b}$ on the vectors $\{e_{i_1}, e_{i_2}\}$ and $e_{i_3}$. Hence

$$
\mathfrak{Q}(x) = \sum_{i < j} a_{ij}\, x_i x_j + \sum_{i} l_i\, x_i, \qquad a_{ij}, l_i \in \mathbb{F}_2,
$$

and there are $2^{\binom{n}{2} + n} = 2^{n(n+1)/2}$ such forms. Computing $\mathfrak{b}$ from this expression gives

$$
\mathfrak{b}(u, v) = \sum_{i < j} a_{ij}\,(u_i v_j + u_j v_i),
$$

because the linear part contributes $l_i(u_i + v_i - u_i - v_i) = 0$ and $x_i^2 = x_i$ in $\mathbb{F}_2$. So $\mathfrak{b}$ sees the coefficients $a_{ij}$ and loses exactly the linear part: the kernel of $m \mapsto b$ consists of the $2^n$ linear functionals $\sum_i l_i x_i$. In particular $\mathfrak{Q}(x) = x_1$ on $\mathbb{F}_2^n$ is a quadratic form with $b = 0$, which is the extreme case of the failure.

### The Failure beyond Characteristic Two

The kernel is not a characteristic-two phenomenon. Let $R = \mathbb{Z}/4\mathbb{Z}$ and $M = R$, and let $\mathfrak{Q}(x) = x^2$. Then $\mathfrak{Q}(rx) = r^2 \mathfrak{Q}(x)$ and

$$
\mathfrak{b}(x, y) = (x + y)^2 - x^2 - y^2 = 2xy
$$

is bilinear, so $m$ is a quadratic form with associated form $\mathfrak{b}(x, y) = 2xy$, and $\mathfrak{b}(x, x) = 2x^2 = 2q(x) \neq \mathfrak{Q}(x)$. The function $c(x) = 2x$ is additive and homogeneous of degree two, since $2r = 2r^2$ in $\mathbb{Z}/4\mathbb{Z}$, and it is nonzero, so $m$ and $m + c$ are distinct quadratic forms with the same associated form. Any element of the kernel is of the form $c(x) = ax$ with $c(2x) = 2ax = 0$, that is $2a = 0$ in $\mathbb{Z}/4\mathbb{Z}$, so $a \in \{0, 2\}$: the kernel has exactly two elements.

### The Classification in Characteristic Two

When $2$ is not invertible the classification must be carried out on the quadratic form itself. Over $\mathbb{F}_2$ the associated form of every quadratic form is alternating, because

$$
\mathfrak{b}(u, u) = \sum_{i < j} a_{ij}(u_i u_j + u_j u_i) = 0
$$

in characteristic two; hence by the even-rank theorem of *Bilinear Forms* a non-degenerate quadratic form over $\mathbb{F}_2$ has even dimension, and the same rank of $\mathfrak{b}$ is shared by all quadratic forms of that dimension. The finer invariant that separates them is the **Arf invariant**, defined as follows.

**Definition.** Let $F$ be a field of characteristic $2$ and write a binary form as $[a, b] : (x, y) \mapsto ax^2 + xy + by^2$, with $b \neq 0$ and $a \in F$. The **Arf invariant** of an orthogonal sum $m = [a_1, b_1] \perp \cdots \perp [a_n, b_n]$ is the class of the sum $a_1b_1 + \cdots + a_nb_n$ in the additive quotient $F/\wp(F)$, where

$$
\wp(F) = \{\alpha^2 + \alpha : \alpha \in F\}.
$$

It is an isometry invariant, and it is exactly what the associated form cannot see: over $\mathbb{F}_2$ the forms $xy = [0, 1]$ and $x^2 + xy + y^2 = [1, 1]$ have the same associated form and Arf invariants $0$ and the class of $1$, and over a finite field the dimension together with the Arf invariant is a complete invariant of the isometry class. The value group has changed character: the discriminant, a class in the multiplicative group $F^\times/(F^\times)^2$, is replaced by a class in the additive quotient $F/\wp(F)$, and the sum $a_1b_1 + \cdots + a_nb_n$ has no meaning as a determinant. The classification in characteristic two, and the chain equivalence that replaces Witt cancellation there, are carried out in *Witt's Theorems*.

## Diagonalisation

### Orthogonal Bases

Let $m$ be a quadratic form on a free module $M$ of finite rank, with polar form $B$. A basis $e_1, \ldots, e_n$ is **orthogonal** for $m$ (or for $B$) if $B(e_i, e_j) = 0$ for $i \neq j$, that is, if the Gram matrix is diagonal.

**Definition.** If $m$ has an orthogonal basis $e_1, \ldots, e_n$ with $\mathfrak{Q}(e_i) = a_i$, then $m$ is **diagonal** in that basis, written

$$
m \cong \langle a_1, a_2, \ldots, a_n\rangle,
$$

and $\mathfrak{Q}(x) = a_1 x_1^2 + \cdots + a_n x_n^2$ in the coordinates of the basis. The symbol $\cong$ denotes isometry of quadratic forms.

### Diagonalisation over a Field

**Theorem (diagonalisation).** Let $F$ be a field of characteristic not $2$, let $V$ be a finite-dimensional $F$-space, and let $m$ be a quadratic form on $V$. Then $m$ has an orthogonal basis, so $m \cong \langle a_1, \ldots, a_n\rangle$ for some $a_i \in F$.

**Proof.** If $m = 0$ every basis is orthogonal. Otherwise choose $\vec e_x$ with $\mathfrak{Q}(\vec e_x) \neq 0$. Then

$$
V = F \vec e_x \perp \vec e_x^{\perp}, \qquad \vec e_x^\perp = \{v : B(\vec e_x, v) = 0\},
$$

because every $v$ decomposes as $v = \frac{B(v, \vec e_x)}{\mathfrak{Q}(\vec e_x)} \vec e_x + \bigl(v - \frac{B(v, \vec e_x)}{\mathfrak{Q}(\vec e_x)} \vec e_x\bigr)$, and the second summand lies in $\vec e_x^\perp$; the two subspaces meet in $0$ since $\mathfrak{Q}(\vec e_x) \neq 0$. The restriction of $m$ to $\vec e_x^\perp$ is again a quadratic form on a space of dimension $n - 1$, and induction gives an orthogonal basis of $\vec e_x^\perp$; adjoining $\vec e_x$ finishes the proof.

**Corollary.** Over a field of characteristic not $2$, every quadratic form is isometric to a diagonal form. The diagonal entries are determined only up to two operations: permuting them, and replacing $a_i$ by $c^2 a_i$ with $c \in F^\times$, since $a_i x_i^2 = a_i (c x_i)^2$ after rescaling the basis vector.

**Definition.** The form $\langle a\rangle$ with $a \in F^\times$ is determined up to isometry by the **square class** of $\mathfrak{a}$ in $F^\times/(F^\times)^2$. If all the $a_i$ are nonzero the form is non-degenerate, and the product $a_1 \cdots a_n$ modulo squares is the **discriminant** of $m$,

$$
\Delta(m) = a_1 \cdots a_n \in F^\times/(F^\times)^2,
$$

which agrees with the determinant of the Gram matrix modulo squares as defined in *Bilinear Forms*.

### Completions of Squares

Over a field of characteristic not $2$ the diagonalisation can be performed on the polynomial expression itself, which is Lagrange's method of completing the square. For

$$
\mathfrak{Q}(x) = \sum_{i,j} a_{ij} x_i x_j,
$$

one groups the terms involving $x_1$, writes them as $a_{11}(x_1 + \sum_{j>1} \frac{a_{1j}}{a_{11}} x_j)^2$ plus the correction, and proceeds by induction on $n$; if $a_{11} = 0$ but some $a_{1j} \neq 0$, the substitution $x_1 \mapsto x_1 + x_j$ replaces the coefficient of $x_1^2$ by $2a_{1j}$, which is nonzero in characteristic not $2$, and the reduction proceeds. This is the computational form of the diagonalisation theorem.

## Isometry of Forms and Orthogonal Sums

### Isometry of Forms

**Definition.** Let $(M, \mathfrak{Q})$ and $(M', m')$ be quadratic forms. An **isometry** $T : (M, \mathfrak{Q}) \to (M', m')$ is an $R$-linear isomorphism with

$$
m'(Tx) = \mathfrak{Q}(x) \qquad (x \in M).
$$

When $2$ is invertible this is equivalent to $B'(Tx, Ty) = B(x, y)$ for all $x, y$, by the polarisation identities. The forms are **isometric**, written $m \cong m'$, when such a $T$ exists, and an isometry of $(M, \mathfrak{Q})$ with itself is an **isometry of the form**, an element of the orthogonal group $\operatorname{O}(M, \mathfrak{Q})$.

**Proposition.** Isometry of forms is an equivalence relation; the identity is an isometry, the inverse of an isometry is an isometry, and a composite of isometries is an isometry. Isometric forms have conjugate isometry groups.

**Proof.** If $m' \circ T = m$ then $T^{-1}$ carries $m'$ to $m$, and if also $m'' \circ S = m'$ then $m'' \circ (S \circ T) = m$, so the relation is reflexive, symmetric and transitive. For the last statement, $S \mapsto TST^{-1}$ is an isomorphism $\operatorname{O}(M, \mathfrak{Q}) \to \operatorname{O}(M', m')$.

### Invariants

**Proposition.** Let $m \cong m'$ with $\dim M = \dim M' = n$. Then $m$ and $m'$ have the same rank and the same discriminant, and if both are real forms their indices and nullity agree, hence also their signatures.

**Proof.** An isometry $T$ satisfies $B'(Tx, Ty) = B(x, y)$, so $Tx = 0$ implies $x \in \operatorname{rad}(m)$, and $x \in \operatorname{rad}(m)$ implies $B'(Tx, Ty) = 0$ for all $y$, that is $Tx \in \operatorname{rad}(m')$; since $T$ is bijective it carries $\operatorname{rad}(m)$ isomorphically onto $\operatorname{rad}(m')$, and the ranks agree. The Gram matrices in corresponding bases are congruent, so their determinants differ by a square. For real forms a subspace on which $m$ is positive definite is carried by $T$ to a subspace of the same dimension on which $m'$ is positive definite, so the positive indices satisfy $n(m) \leq n(m')$, and the reverse inequality follows by applying the same argument to $T^{-1}$; the same reasoning gives $r(m) = r(m')$ and hence $z(m) = z(m')$.

The proposition gives the invariants that the classification theorems of this category compute: dimension, rank, discriminant, and over $\mathbb{R}$ the signature. Each is unchanged by isometry, and each section below shows that on its class of forms the list is complete.

### The Orthogonal Direct Sum

**Definition.** Let $(M, \mathfrak{Q})$ and $(M', m')$ be quadratic forms. Their **orthogonal direct sum** is the form $m \perp m'$ on $M \oplus M'$ defined by

$$
(m \perp m')(x, x') = \mathfrak{Q}(x) + m'(x').
$$

Its polar form is $B \perp B'$, given by $(B \perp B')((x, x'), (y, y')) = B(x, y) + B'(x', y')$; a short verification shows that this is bilinear and that its diagonal recovers $m \perp m'$, so the notation is consistent.

**Proposition.** The orthogonal direct sum is commutative and associative up to isometry, with $\operatorname{rad}(m \perp m') = \operatorname{rad}(m) \oplus \operatorname{rad}(m')$ and $\operatorname{rank}(m \perp m') = \operatorname{rank}(m) + \operatorname{rank}(m')$. The discriminant is multiplicative,

$$
\boxed{\;\Delta(m \perp m') = \Delta(m)\,\Delta(m')\;},
$$

and for real forms the indices and the nullity add, so $\sigma(m \perp m') = \sigma(m) + \sigma(m')$.

**Proof.** The map $(x, x') \mapsto (x', x)$ is an isometry $m \perp m' \to m' \perp m$, and $(M \oplus M') \oplus M'' \to M \oplus (M' \oplus M'')$ is an isometry for the two bracketings; the radical statement is the vanishing of $B(x,y) + B'(x',y')$ for all $y, y'$, which forces $x \in \operatorname{rad}(m)$ and $x' \in \operatorname{rad}(m')$. The Gram matrix of $m \perp m'$ in the union of orthogonal bases is block diagonal, so it is diagonalisable and the rank and discriminant are as claimed; for the indices, diagonalising both real forms gives a diagonal basis of the sum whose positive, negative and zero entries are the combined entries of the two forms, and by Sylvester's law below the index of a real form is the number of positive entries of any diagonal basis, so the indices and the nullity add.

**Example.** With the diagonal notation, $\langle a \rangle \perp \langle b \rangle \cong \langle a, b\rangle$, and the hyperbolic plane of the example above is $\langle 1 \rangle \perp \langle -1\rangle$, written $\langle 1, -1\rangle$; it is the smallest non-degenerate isotropic real form, and it is the elementary block of the Witt theory.

## Sylvester's Law of Inertia

### The Real Case

Over $\mathbb{R}$ a diagonal form can be normalised further, because every positive number is a square and every negative number is minus a square.

**Theorem (Sylvester's law of inertia).** Let $m$ be a quadratic form on a finite-dimensional real vector space $V$. Then there are unique integers $n, r, z \geq 0$ with $n + r + z = \dim V$ such that

$$
\boxed{\;m \cong \underbrace{\langle 1, \ldots, 1\rangle}_{n} \perp \underbrace{\langle -1, \ldots, -1\rangle}_{r} \perp \underbrace{\langle 0, \ldots, 0\rangle}_{z}\;}.
$$

The numbers $n$ and $r$ are the **positive** and **negative indices**, $z$ is the **nullity**, and $\operatorname{rank}(m) = n + r$.

**Proof.** Diagonalise, $m \cong \langle a_1, \ldots, a_n\rangle$ with $a_i \in \mathbb{R}$. Replacing $a_i$ by $a_i/|a_i|$ when $a_i \neq 0$ gives the displayed normal form, so existence holds. For uniqueness, one of $n, r$ is the largest dimension of a subspace on which $m$ is positive definite, and the other the largest dimension on which it is negative definite. Indeed, on the span of the first $n$ basis vectors $m$ is positive definite, so the largest such dimension is at least $n$; if $W$ were a subspace of dimension exceeding $n$ on which $m$ is positive definite, then $W$ would meet the span of the last $r + z$ basis vectors (dimension $n - n$) in a nonzero vector $w$, and $\mathfrak{Q}(w) \leq 0$, a contradiction. Hence the largest dimension is exactly $n$; the argument for $r$ is the same with $-m$. Both numbers being determined by $m$, the decomposition is unique.

**Definition.** The **signature** of a real quadratic form is

$$
\sigma(m) = n - r.
$$

Orthogonal direct sums add signatures, positive indices, negative indices and nullities; these facts are used.

**Example.** On $\mathbb{R}^3$ the form $\mathfrak{Q}(x, y, z) = x^2 + y^2 - z^2$ has signature $1$, indices $n = 2$, $r = 1$, and nullity $0$. It is non-degenerate and indefinite. The form $x^2 + y^2$ on $\mathbb{R}^3$ has $n = 2$, $r = 0$, $z = 1$, signature $2$, and is degenerate.

### The Classification over $\mathbb{R}$ and $\mathbb{C}$

**Theorem (classification over $\mathbb{R}$).** Two real quadratic forms of the same dimension are isometric if and only if they have the same signature and the same rank, equivalently the same triple $(n, r, z)$.

**Proof.** If they are isometric their indices agree by the characterisation of $n$ and $r$ in the proof of Sylvester's law as extremal dimensions, which is an isometry invariant. Conversely, two forms with the same $(n, r, z)$ are each isometric to the normal form determined by that triple.

**Theorem (classification over $\mathbb{C}$).** Every non-degenerate complex quadratic form of dimension $n$ is isometric to $n\langle 1\rangle$. Hence two non-degenerate complex forms are isometric if and only if they have the same dimension, and in general two complex forms are isometric if and only if they have the same rank.

**Proof.** In $\mathbb{C}$ every nonzero number is a square, so each diagonal entry $a_i \neq 0$ can be replaced by $1$; the diagonal form is then a block of ones and a block of zeros, determined by the number of nonzero entries, which is the rank.

**Remark.** The contrast is the reason the real theory is richer: over $\mathbb{C}$ there is one non-degenerate form in each dimension, while over $\mathbb{R}$ there are $n + 1$, indexed by the signature.

### Definite, Semidefinite and Indefinite Forms

A real form is **positive definite** if $\mathfrak{Q}(v) > 0$ for all $v \neq 0$, **negative definite** if $-m$ is, **positive semidefinite** if $\mathfrak{Q}(v) \geq 0$ for all $v$, and **indefinite** if it takes both signs. For a non-degenerate form of dimension $n$ with indices $(n, r)$:

- $m$ is positive definite if and only if $n = n$, equivalently $\sigma(m) = n$;
- $m$ is negative definite if and only if $r = n$, equivalently $\sigma(m) = -n$;
- $m$ is indefinite if and only if $n, r > 0$.

The positive definite forms are exactly the inner products of Euclidean geometry; the existence of a positive definite form on a real space is the algebraic content of the choice of a Euclidean structure, and the orthogonal group of such a form is the classical group of *Isometries and Orthogonal Transformations* in Part IV.

### Isotropic Vectors and Anisotropy

**Definition.** A nonzero vector $v$ with $\mathfrak{Q}(v) = 0$ is **isotropic**, and $m$ is **isotropic** if such a vector exists. A form with no isotropic vector is **anisotropic**. The set of isotropic vectors, projectivised, is the **quadric** of $m$, treated.

**Proposition.** A non-degenerate real form with $n, r > 0$ is isotropic, and a non-degenerate real form with $r = 0$ or $n = 0$ is anisotropic. A non-degenerate complex form of dimension at least $2$ is isotropic.

**Proof.** If $n, r > 0$ choose $u$ with $\mathfrak{Q}(u) = 1$ in the positive part and $w$ with $\mathfrak{Q}(w) = -1$ in the negative part; then $\mathfrak{Q}(u + w) = 1 - 1 = 0$ and $u + w \neq 0$. If $r = 0$ then $m$ is positive definite and vanishes only at $0$. For a complex form of dimension at least $2$, in a diagonal basis $a_1 x_1^2 + a_2 x_2^2$ with all $a_i \neq 0$, the vector with $x_1^2 = -a_2/a_1$, $x_2 = 1$ is isotropic.

The hyperbolic plane $\mathfrak{Q}(x, y) = x^2 - y^2$ is the smallest isotropic non-degenerate real form. Its role as the elementary building block of Witt theory — the hyperbolic planes that split off, the index and cancellation — is in *Witt's Theorems*.

## The Bezoutian Form

A pair of polynomials determines a quadratic form over the base field, and this is the construction through which the theory of forms enters the arithmetic of a rational function field. Let $g \in F[t]$ be monic and square-free and let $f \in F[t]$ be coprime to $g$. The **Bezoutian form** of $f$ modulo $g$ is the quadratic form

$$
m_{f,g} : F[t]/(g) \longrightarrow F, \qquad m_{f,g}(x) = s_g\big(f(\theta)x^2\big),
$$

where $\theta$ is the class of $t$ and $s_g$ is the coefficient functional of $\theta^{\deg g-1}$; it is non-degenerate exactly when $f$ is coprime to $g$, and its class $B(f/g)$ is an element of the Witt group of *The Witt Group and the Grothendieck–Witt Ring* computed from the pair by two rules, one decomposing the modulus into coprime factors and one exchanging the numerator with the modulus. The construction, the rules and the criterion by which a non-trivial Bezoutian obstructs the representability of a ramification sequence by a single symbol are the subject of *Ramification Sequences and Bezoutian Forms*. It is there that the worked example over $\mathbb{Q}$ computes the sequence of degree four of the class $\{g_1,2\}+\{g_2,6\}$ and its Bezoutian, a scalar multiple of the anisotropic Pfister form $\langle\!\langle 2,3\rangle\!\rangle$ — the form-theoretic face of the biquaternion division algebras of *Division Algebras*.
## Summary

A **quadratic form** on an $R$-module $M$ is a function $m$ with $\mathfrak{Q}(rv) = r^2 \mathfrak{Q}(v)$ whose **polar form** $B(u, v) = \tfrac{1}{2}(\mathfrak{Q}(u + v) - \mathfrak{Q}(u) - \mathfrak{Q}(v))$ is bilinear. When $2$ is invertible in $R$ the assignments $m \leftrightarrow B$ with $\mathfrak{Q}(v) = B(v, v)$ are mutually inverse bijections between quadratic forms and symmetric bilinear forms, and the **polarisation identities** recover $B$ from $m$:

$$
\mathfrak{Q}(u + v) + \mathfrak{Q}(u - v) = 2q(u) + 2q(v), \qquad \mathfrak{Q}(u + v) - \mathfrak{Q}(u - v) = 4B(u, v).
$$

In a basis the form is $\mathfrak{Q}(x) = x^{T} G x$ with $G$ the Gram matrix of $B$, its diagonal entries are $\mathfrak{Q}(e_i)$, and a change of basis with matrix $P$ replaces $G$ by the congruent matrix $P^{T} G P$. An **isometry** $T : (M, \mathfrak{Q}) \to (M', m')$ is a linear isomorphism with $m' \circ T = m$; isometric forms have the same rank and discriminant, and over $\mathbb{R}$ the same signature. The **orthogonal direct sum** $m \perp m'$ on $M \oplus M'$ adds ranks and signatures and multiplies discriminants.

When $2$ is not invertible the correspondence fails. The associated bilinear form $b = 2B$ is always defined, and two quadratic forms with the same $\mathfrak{b}$ differ by an additive function homogeneous of degree two; the kernel of $m \mapsto b$ is zero whenever $2$ is not a zero divisor, in particular when $2$ is invertible. Over $\mathbb{F}_2$ the kernel consists of the $2^n$ linear functionals on $\mathbb{F}_2^n$, so a quadratic form there has the shape $\sum_{i<j} a_{ij}x_ix_j + \sum_i l_i x_i$, of which $\mathfrak{b}$ records only the quadratic part, and the classification needs the finer **Arf invariant**, the class of $a_1b_1 + \cdots + a_nb_n$ in the additive quotient $F/\wp(F)$ with $\wp(F) = \{\alpha^2 + \alpha\}$ for the standard presentation $[a_1, b_1] \perp \cdots \perp [a_n, b_n]$. Over $\mathbb{Z}/4\mathbb{Z}$ the same failure occurs for $\mathfrak{Q}(x) = x^2$, whose kernel has two elements. A quadratic form is **non-degenerate** when its polar form is, and its radical is $\operatorname{rad}(m) = \{v : B(v, w) = 0$ for all $w\}$.

Over a field of characteristic not $2$, every finite-dimensional quadratic form **diagonalises**: $m \cong \langle a_1, \ldots, a_n\rangle$, with $\mathfrak{Q}(x) = \sum_i a_i x_i^2$. The entries are determined up to permutation and up to multiplication by squares, and the product $a_1 \cdots a_n$ modulo squares is the **discriminant**.

Over $\mathbb{R}$ every form has a unique normal form $n\langle 1\rangle \perp r\langle -1\rangle \perp z\langle 0\rangle$. The integers $n, r$ are the positive and negative indices, $z$ is the nullity, and $\sigma(m) = n - r$ is the **signature**; by **Sylvester's law of inertia** they are isometry invariants, and they classify real quadratic forms completely. A non-degenerate real form is positive definite when $r = 0$, negative definite when $n = 0$, indefinite when $n, r > 0$, and it is isotropic exactly in the indefinite case. Over $\mathbb{C}$ every nonzero coefficient is a square, so a form is determined by its rank, and every non-degenerate complex form of dimension $n$ is isometric to $n\langle 1\rangle$. A nonzero vector with $\mathfrak{Q}(v) = 0$ is **isotropic**, and the isotropic vectors form the **quadric** of $m$.

The **Bezoutian form** of a pair of polynomials, with $g$ monic and square-free and $f$ coprime to $g$, is a quadratic form on the space $F[t]/(g)$, non-degenerate exactly when $f$ is a unit of $F[t]/(g)$ and computed from the pair by two rules; it is the object through which the representability of a ramification sequence by a symbol is expressed as a statement about the Witt group, and it is the subject of *Ramification Sequences and Bezoutian Forms*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$, with $2$ invertible unless stated |
| $F$, $K$ | Fields |
| $M$, $V$ | $R$-module, respectively finite-dimensional $F$-space |
| $m$ | Quadratic form $m : M \to R$ |
| $B$ | Polar form of $m$, symmetric bilinear, $\mathfrak{Q}(v) = B(v, v)$ |
| $b = 2B$ | Associated bilinear form, defined without dividing by $2$ |
| $T : (M, \mathfrak{Q}) \to (M', m')$ | Isometry of quadratic forms, $m' \circ T = m$ |
| $\operatorname{O}(M, \mathfrak{Q})$ | Isometry group of the form $m$ |
| $\perp$ | Orthogonal direct sum |
| $G$ | Gram matrix of $B$ in a basis, $\mathfrak{Q}(x) = x^{T}Gx$ |
| $P$ | Matrix of a change of basis, $G \mapsto P^{T}GP$ |
| $\operatorname{rad}(m) = \operatorname{rad}(B)$ | Radical of the form |
| $\langle a_1, \ldots, a_n\rangle$ | Diagonal form $\sum_i a_i x_i^2$ |
| $\cong$ | Isometry of quadratic forms |
| $e^\perp$ | Orthogonal complement of the vector $e$ |
| $\mathbb{F}_2$ | Field $\mathbb{Z}/2\mathbb{Z}$ of two elements |
| $\mathbb{Z}/n\mathbb{Z}$ | Integers modulo $n$ |
| $\Delta(m)$ | Discriminant $a_1 \cdots a_n \in F^\times/(F^\times)^2$ |
| $\wp(F) = \{\alpha^2 + \alpha\}$ | Additive subgroup giving the value group of the Arf invariant |
| $[a, b]$ | Binary form $ax^2 + xy + by^2$ over a field of characteristic $2$ |
| Arf invariant | Class of $\sum_i a_ib_i$ in $F/\wp(F)$, the discriminant in characteristic $2$ |
| $B(f/g)$ | Bezoutian form of the pair, in *Ramification Sequences and Bezoutian Forms* |
| $n, r, z$ | Positive index, negative index, nullity of a real form |
| $\sigma(m) = n - r$ | Signature of a real quadratic form |
| $\operatorname{rank}(m) = n + r$ | Rank of a real form |
| $\mathbb{R}, \mathbb{C}$ | Real and complex numbers |
| $\mathbb{H}$ | Quaternions |





## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for polarisation and the correspondence between quadratic and bilinear forms.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for diagonalisation and the algebraic theory of quadratic forms over fields.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the arithmetic theory and the role of the discriminant.
- O. Timothy O'Meara, *Introduction to Quadratic Forms*, Grundlehren der mathematischen Wissenschaften 117 (Springer, 1973), for Sylvester's law and the classical classification.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the structure theory over fields.
- Richard Elman, Nikita Karpenko and Alexander Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms*, American Mathematical Society Colloquium Publications 56 (2008), for the Arf invariant, the associated bilinear form in characteristic $2$ and the classification there.
