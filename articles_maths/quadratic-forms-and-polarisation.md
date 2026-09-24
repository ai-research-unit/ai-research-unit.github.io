
# __Quadratic Forms and Polarisation__

## Introduction

A **quadratic form** is a scalar-valued function of one vector that is homogeneous of degree two. The prototype is $q(x) = x_1^2 + \cdots + x_n^2$ on $\mathbb{R}^n$, the square of the Euclidean length. This article develops the theory over a commutative ring: the definition, the polar form that recovers a symmetric bilinear form from $q$, the polarisation identities and the matrix of a form, isometry of forms and the orthogonal direct sum, diagonalisation, Sylvester's law of inertia, and the classification of real and complex forms.

The passage between a quadratic form and a symmetric bilinear form is a bijection when $2$ is invertible in the base ring, and it is a genuine obstruction when $2$ is not; the first half treats the correspondence and the last section measures its failure.

The base is a commutative ring $R$, and the bilinear vocabulary is that of *Bilinear Forms*: a bilinear form $B$, its Gram matrix $G$, the radical $\operatorname{rad}(B)$, and non-degeneracy as an isomorphism $M \to M^*$. We write $B$ for the symmetric bilinear form associated with a quadratic form $q$, so that $q(v) = B(v, v)$; this fixes the convention in which the fundamental relation of the Clifford algebra reads $uv + vu = 2B(u, v)$. The number systems and the companion articles on tensor and exterior constructions are used only for the examples.

## Quadratic Forms

### Definition

Let $M$ be an $R$-module. A **quadratic form** on $M$ is a function $q : M \to R$ such that

$$
q(rv) = r^2 q(v) \qquad (r \in R,\ v \in M),
$$

and such that the function $B : M \times M \to R$ defined by

$$
B(u, v) = \tfrac{1}{2}\bigl(q(u + v) - q(u) - q(v)\bigr)
$$

is $R$-bilinear. The form $B$ is the **polar form** of $q$, and $q$ is **homogeneous of degree two**. The definition presupposes that $2$ is invertible in $R$, so that the factor $\tfrac{1}{2}$ exists.

**Remark.** The condition that $B$ be bilinear is not a technicality. A function homogeneous of degree two need not polarise: on $\mathbb{F}_2$ the function $q(x) = x^2$ satisfies $q(rx) = r^2 q(x)$, but the associated bilinear form $q(u + v) - q(u) - q(v)$ vanishes identically because $(x + y)^2 = x^2 + y^2$ in characteristic $2$, so no bilinear form carries the information of $q$.

### The Polar Form

**Proposition.** If $B : M \times M \to R$ is a symmetric bilinear form, then $q(v) = B(v, v)$ is a quadratic form with polar form $B$.

**Proof.** Homogeneity is immediate: $q(rv) = B(rv, rv) = r^2 B(v, v) = r^2 q(v)$. For the polar form, bilinearity and symmetry give

$$
q(u + v) - q(u) - q(v) = B(u, v) + B(v, u) = 2B(u, v),
$$

so the function defined in the definition is $B$ itself. $\square$

**Corollary (the correspondence).** Let $2$ be invertible in $R$. Then the assignments $B \mapsto q$ with $q(v) = B(v, v)$ and $q \mapsto B$ by the polar formula are mutually inverse bijections between symmetric bilinear forms on $M$ and quadratic forms on $M$.

**Proof.** The polar form of $q(v) = B(v, v)$ is $B$ by the proposition. Conversely, if $B$ is the polar form of $q$, then

$$
B(v, v) = \tfrac{1}{2}\bigl(q(2v) - 2q(v)\bigr) = \tfrac{1}{2}\bigl(4q(v) - 2q(v)\bigr) = q(v),
$$

using $q(2v) = 4q(v)$ and additivity. So the two constructions are inverse. $\square$

**Definition.** A quadratic form $q$ is **non-degenerate** if its polar form $B$ is non-degenerate in the sense of *Bilinear Forms*, that is, if $M \to M^*$, $u \mapsto B(u, -)$, is an isomorphism. Its **radical** is $\operatorname{rad}(q) = \operatorname{rad}(B)$.

**Remark.** The associated bilinear form

$$
b(u, v) = q(u + v) - q(u) - q(v) = 2B(u, v)
$$

is defined without dividing by $2$ and therefore exists over any ring. Over a ring in which $2$ is a zero divisor it may carry strictly less information than $q$; the extreme case is $\mathbb{F}_2$ above, where $b = 0$ while $q \neq 0$. For this reason the quadratic form, not the bilinear form, is the primitive object in characteristic $2$, and the Clifford construction uses $q$ directly.

### The Polarisation Identities

Polarising the identity $q(u + v) = q(u) + q(v) + 2B(u, v)$ gives the standard formulas relating $q$ to $B$.

**Proposition.** Let $q$ be a quadratic form with polar form $B$ and let $2$ be invertible in $R$. Then for all $u, v \in M$,

$$
q(u + v) + q(u - v) = 2q(u) + 2q(v), \qquad q(u + v) - q(u - v) = 4B(u, v),
$$

$$
B(u + v, u - v) = q(u) - q(v).
$$

**Proof.** Expanding in the polar form and using $B(u, -v) = -B(u, v)$,

$$
q(u + v) = q(u) + q(v) + 2B(u, v), \qquad q(u - v) = q(u) + q(v) - 2B(u, v).
$$

Adding the two gives the parallelogram law and subtracting them gives the second identity. For the third, bilinearity and symmetry give $B(u + v, u - v) = B(u, u) - B(v, v) = q(u) - q(v)$. $\square$

The parallelogram law and the second identity recover $B$ from $q$ in the two ways that the diagonalisation below uses: the first computes the sum $q(u + v) + q(u - v)$, the second the difference $q(u + v) - q(u - v)$.

**Corollary.** Let $2$ be invertible. If $q(u + v) = q(u) + q(v)$ for all $u, v$, then $q = 0$.

**Proof.** The hypothesis says $2B(u, v) = 0$ for all $u, v$, so $B = 0$ because $2$ is invertible, and then $q(v) = B(v, v) = 0$. $\square$

The corollary fails as soon as $2$ is not invertible: over $\mathbb{F}_2$ the form $q(x) = x^2$ is additive and nonzero. The precise measure of the failure is the subject of the last section of this article.

### Examples

**Example (the standard forms).** On $M = R^n$,

$$
q(x) = \sum_{i=1}^{n} x_i^2
$$

is a quadratic form with polar form $B(x, y) = \sum_i x_i y_i$. More generally, for $a_1, \ldots, a_n \in R$,

$$
q(x) = \sum_{i=1}^{n} a_i x_i^2
$$

is a quadratic form, and its polar form has Gram matrix $\operatorname{diag}(a_1, \ldots, a_n)$.

**Example (the norm forms).** The norm $N(z) = z\bar{z}$ on the complex numbers is the quadratic form $a^2 + b^2$ on $\mathbb{R}^2$; its polar form is the Euclidean inner product. The norm $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ on the quaternions is the form $x_0^2 + x_1^2 + x_2^2 + x_3^2$ on $\mathbb{R}^4$. These are the standard examples of positive-definite forms and are treated systematically.

**Example (the hyperbolic plane).** On $R^2$ the form

$$
q(x, y) = x^2 - y^2
$$

is quadratic, with polar form $B((x_1, y_1), (x_2, y_2)) = x_1 x_2 - y_1 y_2$. It is non-degenerate over a field, and it is isotropic: $q(1, 1) = 0$.

### The Gram Matrix and Congruence

Let $M$ be free of rank $n$ with basis $e_1, \ldots, e_n$, and let $G$ be the Gram matrix of the polar form, $G_{ij} = B(e_i, e_j)$, a symmetric matrix. Writing $x = \sum_i x_i e_i$, bilinearity gives

$$
q(x) = B(x, x) = \sum_{i,j} B(e_i, e_j)\,x_i x_j = x^{T} G\, x,
$$

where $x$ denotes the column of coordinates. The diagonal entries are the values $G_{ii} = q(e_i)$, by the normalisation $q(v) = B(v, v)$, and the off-diagonal entries are recovered from $q$ by

$$
2G_{ij} = q(e_i + e_j) - q(e_i) - q(e_j).
$$

The two formulas together say that $q$ and $G$ determine one another when $2$ is invertible, which is the matrix form of the bijection above.

**Proposition (change of basis).** If $P$ is the matrix of a change of basis of $M$, then the Gram matrix of $q$ in the new basis is $P^{T} G P$.

**Proof.** The coordinates transform by $x = Px'$, so

$$
x^{T} G x = (Px')^{T} G (Px') = x'^{T} (P^{T} G P)\, x',
$$

and a quadratic form is determined by its matrix when $2$ is invertible. $\square$

Two symmetric matrices $G, G'$ with $G' = P^{T} G P$ for an invertible $P$ are **congruent**, so isometry classes of quadratic forms on a free module are congruence classes of symmetric matrices. Under congruence the rank of $G$ is unchanged, and $\det(P^{T} G P) = \det(P)^2 \det G$ shows that the determinant of the Gram matrix is well defined modulo squares; that residue is the discriminant of the diagonalising section below.

## The Failure of Polarisation

### The Kernel of the Polar Map

When $2$ is not invertible the map $q \mapsto B$ is not available, but the **associated form**

$$
b(u, v) = q(u + v) - q(u) - q(v) = 2B(u, v)
$$

is defined over any ring, and the question is how much of $q$ it retains. Two quadratic forms with the same associated form differ by a function $c$ with

$$
c(u + v) = c(u) + c(v), \qquad c(rv) = r^2 c(v),
$$

that is, by an additive function that is homogeneous of degree two. The set of such $c$ is an $R$-module, the kernel of $q \mapsto b$. For $c$ in the kernel, additivity gives $c(2v) = 2c(v)$ while homogeneity gives $c(2v) = 4c(v)$, so $2c(v) = 0$ for every $v$; hence the kernel is zero whenever $2$ is not a zero divisor in $R$, and in particular when $2$ is invertible, by the corollary above. When $2$ is a zero divisor the kernel can be nonzero, and the classification of quadratic forms is then strictly finer than the classification of their associated bilinear forms.

**Example (the field with two elements).** Let $R = \mathbb{F}_2$ and $M = \mathbb{F}_2^n$. Every function $q : M \to \mathbb{F}_2$ with $q(0) = 0$ is given by a polynomial in which no variable occurs with exponent greater than one, and the condition that $b$ be bilinear forces every monomial to have degree at most two: a monomial $x_{i_1} \cdots x_{i_d}$ with $d \geq 3$ fails the bilinearity of $b$ on the vectors $\{e_{i_1}, e_{i_2}\}$ and $e_{i_3}$. Hence

$$
q(x) = \sum_{i < j} a_{ij}\, x_i x_j + \sum_{i} l_i\, x_i, \qquad a_{ij}, l_i \in \mathbb{F}_2,
$$

and there are $2^{\binom{n}{2} + n} = 2^{n(n+1)/2}$ such forms. Computing $b$ from this expression gives

$$
b(u, v) = \sum_{i < j} a_{ij}\,(u_i v_j + u_j v_i),
$$

because the linear part contributes $l_i(u_i + v_i - u_i - v_i) = 0$ and $x_i^2 = x_i$ in $\mathbb{F}_2$. So $b$ sees the coefficients $a_{ij}$ and loses exactly the linear part: the kernel of $q \mapsto b$ consists of the $2^n$ linear functionals $\sum_i l_i x_i$. In particular $q(x) = x_1$ on $\mathbb{F}_2^n$ is a quadratic form with $b = 0$, which is the extreme case of the failure.

### The Failure beyond Characteristic Two

The kernel is not a characteristic-two phenomenon. Let $R = \mathbb{Z}/4\mathbb{Z}$ and $M = R$, and let $q(x) = x^2$. Then $q(rx) = r^2 q(x)$ and

$$
b(x, y) = (x + y)^2 - x^2 - y^2 = 2xy
$$

is bilinear, so $q$ is a quadratic form with associated form $b(x, y) = 2xy$, and $b(x, x) = 2x^2 = 2q(x) \neq q(x)$. The function $c(x) = 2x$ is additive and homogeneous of degree two, since $2r = 2r^2$ in $\mathbb{Z}/4\mathbb{Z}$, and it is nonzero, so $q$ and $q + c$ are distinct quadratic forms with the same associated form. Any element of the kernel is of the form $c(x) = ax$ with $c(2x) = 2ax = 0$, that is $2a = 0$ in $\mathbb{Z}/4\mathbb{Z}$, so $a \in \{0, 2\}$: the kernel has exactly two elements.

### The Classification in Characteristic Two

When $2$ is not invertible the classification must be carried out on the quadratic form itself. Over $\mathbb{F}_2$ the associated form of every quadratic form is alternating, because

$$
b(u, u) = \sum_{i < j} a_{ij}(u_i u_j + u_j u_i) = 0
$$

in characteristic two; hence by the even-rank theorem of *Bilinear Forms* a non-degenerate quadratic form over $\mathbb{F}_2$ has even dimension, and the same rank of $b$ is shared by all quadratic forms of that dimension. The finer invariant that separates them is the **Arf invariant**, and the classification in characteristic two, together with the failure of Witt cancellation there, is carried out.

## Diagonalisation

### Orthogonal Bases

Let $q$ be a quadratic form on a free module $M$ of finite rank, with polar form $B$. A basis $e_1, \ldots, e_n$ is **orthogonal** for $q$ (or for $B$) if $B(e_i, e_j) = 0$ for $i \neq j$, that is, if the Gram matrix is diagonal.

**Definition.** If $q$ has an orthogonal basis $e_1, \ldots, e_n$ with $q(e_i) = a_i$, then $q$ is **diagonal** in that basis, written

$$
q \cong \langle a_1, a_2, \ldots, a_n\rangle,
$$

and $q(x) = a_1 x_1^2 + \cdots + a_n x_n^2$ in the coordinates of the basis. The symbol $\cong$ denotes isometry of quadratic forms.

### Diagonalisation over a Field

**Theorem (diagonalisation).** Let $F$ be a field of characteristic not $2$, let $V$ be a finite-dimensional $F$-space, and let $q$ be a quadratic form on $V$. Then $q$ has an orthogonal basis, so $q \cong \langle a_1, \ldots, a_n\rangle$ for some $a_i \in F$.

**Proof.** If $q = 0$ every basis is orthogonal. Otherwise choose $e_1$ with $q(e_1) \neq 0$. Then

$$
V = F e_1 \perp e_1^{\perp}, \qquad e_1^\perp = \{v : B(e_1, v) = 0\},
$$

because every $v$ decomposes as $v = \frac{B(v, e_1)}{q(e_1)} e_1 + \bigl(v - \frac{B(v, e_1)}{q(e_1)} e_1\bigr)$, and the second summand lies in $e_1^\perp$; the two subspaces meet in $0$ since $q(e_1) \neq 0$. The restriction of $q$ to $e_1^\perp$ is again a quadratic form on a space of dimension $n - 1$, and induction gives an orthogonal basis of $e_1^\perp$; adjoining $e_1$ finishes the proof. $\square$

**Corollary.** Over a field of characteristic not $2$, every quadratic form is isometric to a diagonal form. The diagonal entries are determined only up to two operations: permuting them, and replacing $a_i$ by $c^2 a_i$ with $c \in F^\times$, since $a_i x_i^2 = a_i (c x_i)^2$ after rescaling the basis vector.

**Definition.** The form $\langle a\rangle$ with $a \in F^\times$ is determined up to isometry by the **square class** of $a$ in $F^\times/(F^\times)^2$. If all the $a_i$ are nonzero the form is non-degenerate, and the product $a_1 \cdots a_n$ modulo squares is the **discriminant** of $q$,

$$
\Delta(q) = a_1 \cdots a_n \in F^\times/(F^\times)^2,
$$

which agrees with the determinant of the Gram matrix modulo squares as defined in *Bilinear Forms*.

### Completions of Squares

Over a field of characteristic not $2$ the diagonalisation can be performed on the polynomial expression itself, which is Lagrange's method of completing the square. For

$$
q(x) = \sum_{i,j} a_{ij} x_i x_j,
$$

one groups the terms involving $x_1$, writes them as $a_{11}(x_1 + \sum_{j>1} \frac{a_{1j}}{a_{11}} x_j)^2$ plus the correction, and proceeds by induction on $n$; if $a_{11} = 0$ but some $a_{1j} \neq 0$, the substitution $x_1 \mapsto x_1 + x_j$ replaces the coefficient of $x_1^2$ by $2a_{1j}$, which is nonzero in characteristic not $2$, and the reduction proceeds. This is the computational form of the diagonalisation theorem.

## Isometry of Forms and Orthogonal Sums

### Isometry of Forms

**Definition.** Let $(M, q)$ and $(M', q')$ be quadratic forms. An **isometry** $T : (M, q) \to (M', q')$ is an $R$-linear isomorphism with

$$
q'(Tx) = q(x) \qquad (x \in M).
$$

When $2$ is invertible this is equivalent to $B'(Tx, Ty) = B(x, y)$ for all $x, y$, by the polarisation identities. The forms are **isometric**, written $q \cong q'$, when such a $T$ exists, and an isometry of $(M, q)$ with itself is an **isometry of the form**, an element of the orthogonal group $\operatorname{O}(M, q)$.

**Proposition.** Isometry of forms is an equivalence relation; the identity is an isometry, the inverse of an isometry is an isometry, and a composite of isometries is an isometry. Isometric forms have conjugate isometry groups.

**Proof.** If $q' \circ T = q$ then $T^{-1}$ carries $q'$ to $q$, and if also $q'' \circ S = q'$ then $q'' \circ (S \circ T) = q$, so the relation is reflexive, symmetric and transitive. For the last statement, $S \mapsto TST^{-1}$ is an isomorphism $\operatorname{O}(M, q) \to \operatorname{O}(M', q')$. $\square$

### Invariants

**Proposition.** Let $q \cong q'$ with $\dim M = \dim M' = n$. Then $q$ and $q'$ have the same rank and the same discriminant, and if both are real forms their indices and nullity agree, hence also their signatures.

**Proof.** An isometry $T$ satisfies $B'(Tx, Ty) = B(x, y)$, so $Tx = 0$ implies $x \in \operatorname{rad}(q)$, and $x \in \operatorname{rad}(q)$ implies $B'(Tx, Ty) = 0$ for all $y$, that is $Tx \in \operatorname{rad}(q')$; since $T$ is bijective it carries $\operatorname{rad}(q)$ isomorphically onto $\operatorname{rad}(q')$, and the ranks agree. The Gram matrices in corresponding bases are congruent, so their determinants differ by a square. For real forms a subspace on which $q$ is positive definite is carried by $T$ to a subspace of the same dimension on which $q'$ is positive definite, so the positive indices satisfy $p(q) \leq p(q')$, and the reverse inequality follows by applying the same argument to $T^{-1}$; the same reasoning gives $r(q) = r(q')$ and hence $z(q) = z(q')$. $\square$

The proposition gives the invariants that the classification theorems of this category compute: dimension, rank, discriminant, and over $\mathbb{R}$ the signature. Each is unchanged by isometry, and each section below shows that on its class of forms the list is complete.

### The Orthogonal Direct Sum

**Definition.** Let $(M, q)$ and $(M', q')$ be quadratic forms. Their **orthogonal direct sum** is the form $q \perp q'$ on $M \oplus M'$ defined by

$$
(q \perp q')(x, x') = q(x) + q'(x').
$$

Its polar form is $B \perp B'$, given by $(B \perp B')((x, x'), (y, y')) = B(x, y) + B'(x', y')$; a short verification shows that this is bilinear and that its diagonal recovers $q \perp q'$, so the notation is consistent.

**Proposition.** The orthogonal direct sum is commutative and associative up to isometry, with $\operatorname{rad}(q \perp q') = \operatorname{rad}(q) \oplus \operatorname{rad}(q')$ and $\operatorname{rank}(q \perp q') = \operatorname{rank}(q) + \operatorname{rank}(q')$. The discriminant is multiplicative,

$$
\Delta(q \perp q') = \Delta(q)\,\Delta(q'),
$$

and for real forms the indices and the nullity add, so $\sigma(q \perp q') = \sigma(q) + \sigma(q')$.

**Proof.** The map $(x, x') \mapsto (x', x)$ is an isometry $q \perp q' \to q' \perp q$, and $(M \oplus M') \oplus M'' \to M \oplus (M' \oplus M'')$ is an isometry for the two bracketings; the radical statement is the vanishing of $B(x,y) + B'(x',y')$ for all $y, y'$, which forces $x \in \operatorname{rad}(q)$ and $x' \in \operatorname{rad}(q')$. The Gram matrix of $q \perp q'$ in the union of orthogonal bases is block diagonal, so it is diagonalisable and the rank and discriminant are as claimed; for the indices, diagonalising both real forms gives a diagonal basis of the sum whose positive, negative and zero entries are the combined entries of the two forms, and by Sylvester's law below the index of a real form is the number of positive entries of any diagonal basis, so the indices and the nullity add. $\square$

**Example.** With the diagonal notation, $\langle a \rangle \perp \langle b \rangle \cong \langle a, b\rangle$, and the hyperbolic plane of the example above is $\langle 1 \rangle \perp \langle -1\rangle$, written $\langle 1, -1\rangle$; it is the smallest non-degenerate isotropic real form, and it is the elementary block of the Witt theory.

## Sylvester's Law of Inertia

### The Real Case

Over $\mathbb{R}$ a diagonal form can be normalised further, because every positive number is a square and every negative number is minus a square.

**Theorem (Sylvester's law of inertia).** Let $q$ be a quadratic form on a finite-dimensional real vector space $V$. Then there are unique integers $p, r, z \geq 0$ with $p + r + z = \dim V$ such that

$$
q \cong \underbrace{\langle 1, \ldots, 1\rangle}_{p} \perp \underbrace{\langle -1, \ldots, -1\rangle}_{r} \perp \underbrace{\langle 0, \ldots, 0\rangle}_{z}.
$$

The numbers $p$ and $r$ are the **positive** and **negative indices**, $z$ is the **nullity**, and $\operatorname{rank}(q) = p + r$.

**Proof.** Diagonalise, $q \cong \langle a_1, \ldots, a_n\rangle$ with $a_i \in \mathbb{R}$. Replacing $a_i$ by $a_i/|a_i|$ when $a_i \neq 0$ gives the displayed normal form, so existence holds. For uniqueness, one of $p, r$ is the largest dimension of a subspace on which $q$ is positive definite, and the other the largest dimension on which it is negative definite. Indeed, on the span of the first $p$ basis vectors $q$ is positive definite, so the largest such dimension is at least $p$; if $W$ were a subspace of dimension exceeding $p$ on which $q$ is positive definite, then $W$ would meet the span of the last $r + z$ basis vectors (dimension $n - p$) in a nonzero vector $w$, and $q(w) \leq 0$, a contradiction. Hence the largest dimension is exactly $p$; the argument for $r$ is the same with $-q$. Both numbers being determined by $q$, the decomposition is unique. $\square$

**Definition.** The **signature** of a real quadratic form is

$$
\sigma(q) = p - r.
$$

Orthogonal direct sums add signatures, positive indices, negative indices and nullities; these facts are used.

**Example.** On $\mathbb{R}^3$ the form $q(x, y, z) = x^2 + y^2 - z^2$ has signature $1$, indices $p = 2$, $r = 1$, and nullity $0$. It is non-degenerate and indefinite. The form $x^2 + y^2$ on $\mathbb{R}^3$ has $p = 2$, $r = 0$, $z = 1$, signature $2$, and is degenerate.

### The Classification over $\mathbb{R}$ and $\mathbb{C}$

**Theorem (classification over $\mathbb{R}$).** Two real quadratic forms of the same dimension are isometric if and only if they have the same signature and the same rank, equivalently the same triple $(p, r, z)$.

**Proof.** If they are isometric their indices agree by the characterisation of $p$ and $r$ in the proof of Sylvester's law as extremal dimensions, which is an isometry invariant. Conversely, two forms with the same $(p, r, z)$ are each isometric to the normal form determined by that triple. $\square$

**Theorem (classification over $\mathbb{C}$).** Every non-degenerate complex quadratic form of dimension $n$ is isometric to $n\langle 1\rangle$. Hence two non-degenerate complex forms are isometric if and only if they have the same dimension, and in general two complex forms are isometric if and only if they have the same rank.

**Proof.** In $\mathbb{C}$ every nonzero number is a square, so each diagonal entry $a_i \neq 0$ can be replaced by $1$; the diagonal form is then a block of ones and a block of zeros, determined by the number of nonzero entries, which is the rank. $\square$

**Remark.** The contrast is the reason the real theory is richer: over $\mathbb{C}$ there is one non-degenerate form in each dimension, while over $\mathbb{R}$ there are $n + 1$, indexed by the signature.

### Definite, Semidefinite and Indefinite Forms

A real form is **positive definite** if $q(v) > 0$ for all $v \neq 0$, **negative definite** if $-q$ is, **positive semidefinite** if $q(v) \geq 0$ for all $v$, and **indefinite** if it takes both signs. For a non-degenerate form of dimension $n$ with indices $(p, r)$:

- $q$ is positive definite if and only if $p = n$, equivalently $\sigma(q) = n$;
- $q$ is negative definite if and only if $r = n$, equivalently $\sigma(q) = -n$;
- $q$ is indefinite if and only if $p, r > 0$.

The positive definite forms are exactly the inner products of Euclidean geometry; the existence of a positive definite form on a real space is the algebraic content of the choice of a Euclidean structure, and the orthogonal group of such a form is the compact orthogonal group treated.

### Isotropic Vectors and Anisotropy

**Definition.** A nonzero vector $v$ with $q(v) = 0$ is **isotropic**, and $q$ is **isotropic** if such a vector exists. A form with no isotropic vector is **anisotropic**. The set of isotropic vectors, projectivised, is the **quadric** of $q$, treated.

**Proposition.** A non-degenerate real form with $p, r > 0$ is isotropic, and a non-degenerate real form with $r = 0$ or $p = 0$ is anisotropic. A non-degenerate complex form of dimension at least $2$ is isotropic.

**Proof.** If $p, r > 0$ choose $u$ with $q(u) = 1$ in the positive part and $w$ with $q(w) = -1$ in the negative part; then $q(u + w) = 1 - 1 = 0$ and $u + w \neq 0$. If $r = 0$ then $q$ is positive definite and vanishes only at $0$. For a complex form of dimension at least $2$, in a diagonal basis $a_1 x_1^2 + a_2 x_2^2$ with all $a_i \neq 0$, the vector with $x_1^2 = -a_2/a_1$, $x_2 = 1$ is isotropic. $\square$

The hyperbolic plane $q(x, y) = x^2 - y^2$ is the smallest isotropic non-degenerate real form. Its role as the elementary building block of Witt theory is not covered here.

## Summary

A **quadratic form** on an $R$-module $M$ is a function $q$ with $q(rv) = r^2 q(v)$ whose **polar form** $B(u, v) = \tfrac{1}{2}(q(u + v) - q(u) - q(v))$ is bilinear. When $2$ is invertible in $R$ the assignments $q \leftrightarrow B$ with $q(v) = B(v, v)$ are mutually inverse bijections between quadratic forms and symmetric bilinear forms, and the **polarisation identities** recover $B$ from $q$:

$$
q(u + v) + q(u - v) = 2q(u) + 2q(v), \qquad q(u + v) - q(u - v) = 4B(u, v).
$$

In a basis the form is $q(x) = x^{T} G x$ with $G$ the Gram matrix of $B$, its diagonal entries are $q(e_i)$, and a change of basis with matrix $P$ replaces $G$ by the congruent matrix $P^{T} G P$. An **isometry** $T : (M, q) \to (M', q')$ is a linear isomorphism with $q' \circ T = q$; isometric forms have the same rank and discriminant, and over $\mathbb{R}$ the same signature. The **orthogonal direct sum** $q \perp q'$ on $M \oplus M'$ adds ranks and signatures and multiplies discriminants.

When $2$ is not invertible the correspondence fails. The associated bilinear form $b = 2B$ is always defined, and two quadratic forms with the same $b$ differ by an additive function homogeneous of degree two; the kernel of $q \mapsto b$ is zero whenever $2$ is not a zero divisor, in particular when $2$ is invertible. Over $\mathbb{F}_2$ the kernel consists of the $2^n$ linear functionals on $\mathbb{F}_2^n$, so a quadratic form there has the shape $\sum_{i<j} a_{ij}x_ix_j + \sum_i l_i x_i$, of which $b$ records only the quadratic part, and the classification needs the finer Arf invariant. Over $\mathbb{Z}/4\mathbb{Z}$ the same failure occurs for $q(x) = x^2$, whose kernel has two elements. A quadratic form is **non-degenerate** when its polar form is, and its radical is $\operatorname{rad}(q) = \{v : B(v, w) = 0$ for all $w\}$.

Over a field of characteristic not $2$, every finite-dimensional quadratic form **diagonalises**: $q \cong \langle a_1, \ldots, a_n\rangle$, with $q(x) = \sum_i a_i x_i^2$. The entries are determined up to permutation and up to multiplication by squares, and the product $a_1 \cdots a_n$ modulo squares is the **discriminant**.

Over $\mathbb{R}$ every form has a unique normal form $p\langle 1\rangle \perp r\langle -1\rangle \perp z\langle 0\rangle$. The integers $p, r$ are the positive and negative indices, $z$ is the nullity, and $\sigma(q) = p - r$ is the **signature**; by **Sylvester's law of inertia** they are isometry invariants, and they classify real quadratic forms completely. A non-degenerate real form is positive definite when $r = 0$, negative definite when $p = 0$, indefinite when $p, r > 0$, and it is isotropic exactly in the indefinite case. Over $\mathbb{C}$ every nonzero coefficient is a square, so a form is determined by its rank, and every non-degenerate complex form of dimension $n$ is isometric to $n\langle 1\rangle$. A nonzero vector with $q(v) = 0$ is **isotropic**, and the isotropic vectors form the **quadric** of $q$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$, with $2$ invertible unless stated |
| $F$, $K$ | Fields |
| $M$, $V$ | $R$-module, respectively finite-dimensional $F$-space |
| $q$ | Quadratic form $q : M \to R$ |
| $B$ | Polar form of $q$, symmetric bilinear, $q(v) = B(v, v)$ |
| $b = 2B$ | Associated bilinear form, defined without dividing by $2$ |
| $T : (M, q) \to (M', q')$ | Isometry of quadratic forms, $q' \circ T = q$ |
| $\operatorname{O}(M, q)$ | Isometry group of the form $q$ |
| $\perp$ | Orthogonal direct sum |
| $G$ | Gram matrix of $B$ in a basis, $q(x) = x^{T}Gx$ |
| $P$ | Matrix of a change of basis, $G \mapsto P^{T}GP$ |
| $\operatorname{rad}(q) = \operatorname{rad}(B)$ | Radical of the form |
| $\langle a_1, \ldots, a_n\rangle$ | Diagonal form $\sum_i a_i x_i^2$ |
| $\cong$ | Isometry of quadratic forms |
| $e^\perp$ | Orthogonal complement of the vector $e$ |
| $\mathbb{F}_2$ | Field $\mathbb{Z}/2\mathbb{Z}$ of two elements |
| $\mathbb{Z}/n\mathbb{Z}$ | Integers modulo $n$ |
| $\Delta(q)$ | Discriminant $a_1 \cdots a_n \in F^\times/(F^\times)^2$ |
| $p, r, z$ | Positive index, negative index, nullity of a real form |
| $\sigma(q) = p - r$ | Signature of a real quadratic form |
| $\operatorname{rank}(q) = p + r$ | Rank of a real form |
| $\mathbb{R}, \mathbb{C}$ | Real and complex numbers |
| $\mathbb{H}$ | Quaternions |





## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for polarisation and the correspondence between quadratic and bilinear forms.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for diagonalisation and the algebraic theory of quadratic forms over fields.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the arithmetic theory and the role of the discriminant.
- O. Timothy O'Meara, *Introduction to Quadratic Forms*, Grundlehren der mathematischen Wissenschaften 117 (Springer, 1973), for Sylvester's law and the classical classification.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the structure theory over fields.
