# __The Skew Part of an Algebra__

## Introduction

An involution of an algebra selects the elements it negates: the **skew part** $K(A) = A^-$, whose elements satisfy $k^* = -k$. The selection is not a subalgebra in the ordinary sense, because the product of two skew elements need not be skew; it is closed under the commutator $[x,y] = xy - yx$, so it is a Lie algebra, and it is stable under the symmetrised product with the self-adjoint part, so the pair of the two parts carries the two products of the involution. Together the two parts form a $\mathbb{Z}/2$-graded Lie algebra, and the skew part is the tangent space of the unitary group at the identity.

This article develops the skew part, the commutator and the Lie algebra it defines, the graded Lie algebra formed with the self-adjoint part, the module structure over the Jordan algebra $H(A)$, the tangent space of the unitary group, the Cayley transform, and the standard examples of the alternating matrices with the transpose and of the skew-Hermitian matrices with the conjugate transpose. The involution and the decomposition $A = A^+ \oplus A^-$ are *Involutive Algebras*; the self-adjoint part and its Jordan structure are *The Self-Adjoint Part of an Algebra*, in *Symmetric Algebras*; the Lie algebras, their structure theory and their graded version are *Lie Algebras* and *Graded Lie Algebras and Lie Superalgebras*; the unitary elements are *Unitary Elements of an Involutive Algebra*; and the operator $\operatorname{ad}_x$ is *The Commutator Operator*.

Throughout, $k$ is a field of characteristic not two, $A$ is a unital associative $k$-algebra, $\sigma$ is an involution of $A$, and the image of an element is written $x^* = \sigma(x)$. The self-adjoint part is $H(A) = A^+ = \{h : h^* = h\}$, the skew part is $K(A) = A^- = \{k : k^* = -k\}$, the commutator is $[x,y] = xy - yx$, and the symmetrised product is $x \bullet y = \tfrac12(xy + yx)$.

## The Skew Part

### Definition and the Decomposition

**Definition.** The **skew part** of $(A,\sigma)$ is

$$
K(A) = A^- = \{k \in A : k^* = -k\},
$$

the **self-adjoint part** is $H(A) = A^+ = \{h \in A : h^* = h\}$, the **commutator** is $[x,y] = xy - yx$, and the **symmetrised product** is $x \bullet y = \tfrac12(xy + yx)$.

**Proposition.** $K(A)$ and $H(A)$ are $k$-linear subspaces with

$$
\boxed{\;A = K(A) \oplus H(A), \qquad x = \tfrac12(x - x^*) + \tfrac12(x + x^*)\;},
$$

and the involution acts as minus the identity on $K(A)$ and as the identity on $H(A)$; the two spaces are the eigenspaces of $\sigma$ for the eigenvalues $-1$ and $1$.

*Proof.* The involution is linear of order two, so its eigenvalues lie in $\{1,-1\}$; the averaging decomposition displayed is legitimate because $2$ is invertible, and the two summands are the negated and the fixed elements. The sum is direct because an element that is both fixed and negated satisfies $x = -x$, hence $x = 0$.

### The Product Inclusions

**Proposition.** The commutator and the symmetrised product satisfy

$$
\boxed{\;[H,H] \subseteq K, \qquad [H,K] \subseteq H, \qquad [K,K] \subseteq K\;},
$$

$$
\boxed{\;H \bullet H \subseteq H, \qquad K \bullet K \subseteq H, \qquad H \bullet K \subseteq K\;}.
$$

*Proof.* For self-adjoint $x$ and $y$, $(xy)^* = yx$ and $(yx)^* = xy$, so $[x,y]^* = (xy - yx)^* = yx - xy = -[x,y]$ and $x \bullet y$ is fixed. For self-adjoint $x$ and skew $y$, $(xy)^* = (-y)x = -yx$ and $(yx)^* = x(-y) = -xy$, so $[x,y]^* = -yx + xy = [x,y]$ and $x \bullet y$ is negated. For skew $x$ and $y$, $(xy)^* = (-y)(-x) = yx$ and $(yx)^* = xy$, so $[x,y]^* = yx - xy = -[x,y]$ and $x \bullet y$ is fixed.

## The Lie Algebra Structure

### The Commutator on the Skew Part

**Definition.** On $A$ the **commutator** is $[x,y] = xy - yx$; it is $k$-bilinear, alternating, $[x,x] = 0$, and it satisfies the Jacobi identity

$$
[x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0 ,
$$

so $A$ with the commutator is a Lie algebra over $k$ in the sense of *Lie Algebras*.

**Theorem.** $K(A)$ is a Lie subalgebra of $A$ under the commutator, and the bracket makes $K(A) \oplus H(A)$ a $\mathbb{Z}/2$-graded Lie algebra with the compatible grading of *Graded Lie Algebras and Lie Superalgebras*, the even part being $K(A)$ and the odd part $H(A)$.

*Proof.* The closure $[K,K] \subseteq K$ is the third inclusion of the proposition, and the Jacobi identity is inherited from the associativity of the product of $A$, as in *Lie Algebras*, §*The Commutator Bracket*. The remaining two inclusions $[K,H] \subseteq H$ and $[H,H] \subseteq K$ are the other two lines, so the bracket respects the parity with $\deg K = 0$ and $\deg H = 1$.

**Corollary.** $H(A)$ is a **Lie triple system** under

$$
\{h_1,h_2,h_3\} = [h_1,[h_2,h_3]] ,
$$

and the triple product is again self-adjoint.

*Proof.* $[h_2,h_3] \in K$ and $[h_1,K] \subseteq H$, so the triple lies in $H$; the Lie triple system axioms are the Jacobi identity applied three times.

**Remark (the sign).** The grading here is the compatible one and not the Koszul signed one: the bracket is the commutator, which is alternating on the whole algebra, so for two odd elements it is antisymmetric, whereas a super Lie bracket would be symmetric there. The signed reading, with the anticommutator on the odd part, is *Graded Lie Algebras and Lie Superalgebras*.

### The Adjoint Action

**Definition.** For $x \in A$ the **adjoint action** is

$$
\operatorname{ad}_x : A \longrightarrow A, \qquad \operatorname{ad}_x(y) = [x,y] .
$$

**Proposition.** For $x \in K(A)$ the operator $\operatorname{ad}_x$ preserves $K(A)$ and $H(A)$, is a derivation of $A$, and the map $x \mapsto \operatorname{ad}_x$ is a homomorphism of Lie algebras $K(A) \to \operatorname{Der}(A)$ whose kernel is $K(A) \cap Z(A)$.

*Proof.* The preservation is the proposition above. The derivation identity is $\operatorname{ad}_x(yz) = xyz - yzx = (xy - yx)z + y(xz - zx) = \operatorname{ad}_x(y)z + y\operatorname{ad}_x(z)$, using associativity. The bracket of the operators is $\operatorname{ad}_{[x,y]} = [\operatorname{ad}_x,\operatorname{ad}_y]$, which is the Jacobi identity; the kernel is the set of $x$ with $[x,y] = 0$ for all $y$, that is $K(A) \cap Z(A)$. The operator theory of $\operatorname{ad}_x$ is *The Commutator Operator*.

### The Module Structure over the Jordan Algebra

**Proposition.** Under the symmetrised product, $K(A)$ is stable under multiplication by $H(A)$,

$$
H(A) \bullet K(A) \subseteq K(A), \qquad H(A) \bullet H(A) \subseteq H(A), \qquad K(A) \bullet K(A) \subseteq H(A),
$$

so the pair $\bigl(H(A),K(A)\bigr)$ carries the two products.

*Proof.* The three inclusions are the second display of the proposition above. The pair is the **Jordan pair** of the involution; the verification of the remaining module axioms is the computation linking the two products, and the structure theory of Jordan pairs belongs to *Jordan Algebras*.

## The Tangent Space of the Unitary Group

**Theorem.** The skew elements are the elements that make $1 + tx$ unitary to first order in $t$: expanding

$$
(1+tx)^*(1+tx) = 1 + t(x + x^*) + t^2 x^*x
$$

shows that the coefficient of $t$ vanishes exactly when $x^* = -x$, that is exactly when $x$ is skew. Consequently $K(A)$ is the algebraic tangent space of the unitary group $\mathrm{U}(A)$ at the identity, and the Lie bracket of two skew elements is the second-order shadow of the group commutator: the coefficient of the leading term in the expansion of $(1+tx)(1+ty)(1+tx)^{-1}(1+ty)^{-1}$ lies in the span of $[x,y]$.

*Proof.* The expansion displayed is the definition of the product; the linear term vanishes exactly for $x^* = -x$. For the second statement one expands the four factors to second order; the quadratic part involves $[x,y]$ and the identities $x^* = -x$, $y^* = -y$, and it is the standard identification of the bracket with the commutator of the group, whose totality belongs to the theory of *Involutive Groups* and of the linear groups of Part II.

**Corollary.** For every unitary $u$ the elements $u + u^*$ and $u u^*$ are self-adjoint, and $u - u^*$ is skew. The unitary elements therefore decompose in the affine form

$$
\boxed{\;u = \tfrac12(u + u^*) + \tfrac12(u - u^*)\;},
$$

the first summand self-adjoint and the second skew, which is the decomposition $A = A^+\oplus A^-$ applied to $u$.

## The Cayley Transform

**Proposition.** Let $\kappa$ be a skew element with $1 - \kappa$ invertible, and set

$$
\boxed{\;u = (1+\kappa)(1-\kappa)^{-1}\;} .
$$

Then $u$ is unitary, and its inverse is $(1-\kappa)(1+\kappa)^{-1}$. In particular the unitary group contains the image of the Cayley transform of the skew elements, and the transform is the algebraic substitute for the exponential of the Lie algebra: its first-order term at $\kappa = 0$ is $2\kappa$.

*Proof.* Compute $u^* = \bigl((1-\kappa)^{-1}\bigr)^*(1+\kappa)^*$. Since $(1-\kappa)^* = 1 + \kappa$ and $(1+\kappa)^* = 1-\kappa$, and since the involution reverses inverses, $u^* = (1+\kappa)^{-1}(1-\kappa)$. The factors $1+\kappa$ and $1-\kappa$ commute, so

$$
u^*u = (1+\kappa)^{-1}(1-\kappa)(1+\kappa)(1-\kappa)^{-1} = (1+\kappa)^{-1}(1-\kappa^2)(1-\kappa)^{-1} = (1+\kappa)^{-1}(1+\kappa)(1-\kappa)(1-\kappa)^{-1} = 1,
$$

and the same computation with the factors in the other order gives $uu^* = 1$. The derivative statement is the expansion $u = (1+\kappa)(1 + \kappa + \kappa^2 + \cdots) = 1 + 2\kappa + O(\kappa^2)$ for nilpotent or small $\kappa$.

The exponential $\exp(\kappa)$ is not available in a bare $k$-algebra; the formal series identifies the Lie algebra of the skew elements with the unitary group, as in the theory of the linear groups, and the convergent reading belongs to *Hilbert Algebras* and to Part II.

## The Examples

### The Transpose on a Matrix Algebra

Let $A = M_n(k)$ with $X^* = X^{\mathsf{T}}$ and $2 \neq 0$. The skew part is the space of the alternating matrices, of dimension $n(n-1)/2$, and the theorem says that the commutator of two alternating matrices is alternating; for $n = 3$ they form a three-dimensional Lie algebra, the Lie algebra $\mathfrak{so}_3$ of the orthogonal group. The self-adjoint part is the space of the symmetric matrices, of dimension $n(n+1)/2$, and the two dimensions add to $n^2$, as the decomposition requires.

### The Conjugate Transpose on a Complex Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the conjugate transpose $X^* = \overline{X}^{\mathsf{T}}$. The skew part is the space of the skew-Hermitian matrices, the Lie algebra $\mathfrak{u}_n$ of the unitary group in the real reading; the self-adjoint part is the space of the Hermitian matrices. The scalars here are the complex numbers with the conjugation, so the involution on $A$ is $\varsigma$-semilinear; the Hermitian form and the positive definiteness of the self-adjoint part belong to *Hilbert Algebras*.

### The Trivial Involution

Let $\sigma = \mathrm{id}_A$. Then $K(A) = 0$ and $H(A) = A$; the skew part vanishes and the Lie algebra is the zero algebra.

### The Inversion on a Group Algebra

Let $A = k[G]$ with the involution $g^* = g^{-1}$. Then the skew part is spanned by the differences $g - g^{-1}$ for $g$ not of order two, and the self-adjoint part by the elements $g + g^{-1}$ and by the $g$ of order two. The bracket of two skew elements is again skew, by the theorem.

### The Exchange Involution

Let $A = B \times B^{\mathrm{opp}}$ with the exchange involution $(b,c)^* = (c,b)$. The skew part is the antidiagonal $\{(b,-b)\} \cong B$, and the bracket is

$$
[(b,-b),(b',-b')] = ([b,b'],\,-[b,b']) ,
$$

so $K(A)$ is isomorphic to $B$ with the commutator bracket, that is to the commutator algebra $B^-$ of *The Commutator Operator*.

## Summary

The **skew part** $K(A) = \{k : k^* = -k\}$ of an algebra with an involution is a linear subspace with $A = K(A)\oplus H(A)$, where $H(A) = \{h : h^* = h\}$ is the self-adjoint part; the involution acts as minus the identity on $K(A)$ and as the identity on $H(A)$. The skew part is closed under the commutator, so it is a **Lie algebra**, and $K(A)\oplus H(A)$ is a $\mathbb{Z}/2$-graded Lie algebra with the compatible grading, the even part $K(A)$ and the odd part $H(A)$; $H(A)$ is a **Lie triple system** under $\{h_1,h_2,h_3\} = [h_1,[h_2,h_3]]$. The adjoint action $\operatorname{ad}_x$ of a skew element is a derivation that preserves the two parts, and the map $x \mapsto \operatorname{ad}_x$ is a homomorphism $K(A) \to \operatorname{Der}(A)$ with kernel $K(A)\cap Z(A)$. The symmetrised product makes $K(A)$ stable under multiplication by the Jordan algebra $H(A)$, so the pair carries the two products and is the Jordan pair of the involution. The skew part is the tangent space of the unitary group at the identity, and the Cayley transform produces unitary elements from skew ones. The standard examples are the alternating matrices with the transpose, whose Lie algebra is $\mathfrak{so}_n$, and the skew-Hermitian matrices with the conjugate transpose, whose Lie algebra is $\mathfrak{u}_n$. The involution and the decomposition are *Involutive Algebras*; the self-adjoint part and its Jordan structure are *The Self-Adjoint Part of an Algebra*; the Lie theory is *Lie Algebras* and *Graded Lie Algebras and Lie Superalgebras*; the unitary elements are *Unitary Elements of an Involutive Algebra*; and the operator is *The Commutator Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars, of characteristic not two |
| $A$ | a unital associative $k$-algebra |
| $\sigma$, $x^* = \sigma(x)$ | the involution and the adjoint of an element |
| $K(A) = A^-$ | the skew elements, $k^* = -k$ |
| $H(A) = A^+$ | the self-adjoint elements, $h^* = h$ |
| $[x,y] = xy - yx$ | the commutator |
| $x \bullet y = \tfrac12(xy+yx)$ | the symmetrised product |
| $\operatorname{ad}_x(y) = [x,y]$ | the adjoint action |
| $\{h_1,h_2,h_3\} = [h_1,[h_2,h_3]]$ | the Lie triple product on $H(A)$ |
| $\mathrm{U}(A)$ | the unitary group, $u^*u = uu^* = 1$ |
| $\mathfrak{so}_n$, $\mathfrak{u}_n$ | the skew parts of the matrix examples |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan pair of an involution and the module structure on the skew part.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the symmetric and skew parts of an involution of a central simple algebra.
- Israel Nathan Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and the skew elements of a ring with involution and their Lie structure.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the Lie algebra structure and the graded reading.
