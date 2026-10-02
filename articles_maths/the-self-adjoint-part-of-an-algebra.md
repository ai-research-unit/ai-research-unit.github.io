# __The Self-Adjoint Part of an Algebra__

## Introduction

An involution of an algebra selects the elements it fixes: the **self-adjoint part** $H(A) = A^+$, whose elements satisfy $h^* = h$. The selection is not a subalgebra in the ordinary sense, because the product of two self-adjoint elements need not be self-adjoint; it is a subalgebra of the **symmetrised** algebra, closed under the Jordan product $x \circ y = \tfrac12(xy + yx)$. The self-adjoint part is therefore a Jordan algebra, and the complementary part of the skew elements is a Lie algebra and a Jordan module over it; the pair is the algebraic content of the involution.

This article develops the self-adjoint part, the symmetrised product and the Jordan axioms it satisfies, the quadratic representation that replaces the missing associativity of the Jordan product, the decomposition of the algebra into its self-adjoint and skew parts, and the standard examples of the symmetric matrices with the transpose and of the Hermitian matrices with the conjugate transpose. The involution on the elements, the decomposition $A = A^+\oplus A^-$ and the first statement that the symmetric elements form a Jordan algebra are those of *Involutive Linear Algebras*; the Jordan algebras themselves, their classification and their structure theory are *Jordan Algebras* of the same reading unit; the unitary elements and the skew Lie algebra are *Unitary Elements of an Involutive Algebra*; and the positivity, the order and the norms of the self-adjoint part are Part II and *Hilbert Algebras*.

Throughout, $k$ is a field of characteristic not two, $A$ is a unital associative $k$-algebra with unit $1$, $\sigma$ is an involution of $A$, and the image of an element is written $x^* = \sigma(x)$. The self-adjoint part is $H(A) = \{h \in A : h^* = h\}$, the skew part is $K(A) = A^- = \{k \in A : k^* = -k\}$, the symmetrised product is $x \circ y = \tfrac12(xy + yx)$, and the unit is self-adjoint because $1^* = 1$.

## The Self-Adjoint Part

### Definition and the Decomposition

**Definition.** The **self-adjoint part** of $(A,\sigma)$ is

$$
H(A) = A^+ = \{h \in A : h^* = h\},
$$

the **skew part** is $K(A) = A^- = \{k \in A : k^* = -k\}$, and the **symmetrised product** is $x \circ y = \tfrac12(xy+yx)$. The **square** of an element is $x^2 = x \circ x$ in the Jordan reading, written $x^2$ on the left as usual.

**Proposition.** $H(A)$ and $K(A)$ are $k$-linear subspaces with

$$
A = H(A) \oplus K(A), \qquad x = \tfrac12\bigl(x + x^*\bigr) + \tfrac12\bigl(x - x^*\bigr), \qquad 1 \in H(A),
$$

and the involution acts as the identity on $H(A)$ and as minus the identity on $K(A)$; the two spaces are the eigenspaces of $\sigma$ for the eigenvalues $1$ and $-1$.

*Proof.* The involution is linear and has order two, so its eigenvalues lie in $\{1,-1\}$ and the algebra is the direct sum of the two eigenspaces, over a field of characteristic not two in which the averaging decomposition displayed is legitimate; the unit is fixed because $1^* = 1$.

### The Two Products on the Two Parts

**Proposition.** For $x, y \in H(A)$ the product $xy$ satisfies $(xy)^* = yx$, and for $x, y \in K(A)$ the product satisfies $(xy)^* = yx$ as well; the symmetrised products are self-adjoint and the commutators are skew:

$$
H(A) \circ H(A) \subseteq H(A), \qquad K(A) \circ K(A) \subseteq H(A), \qquad H(A) \circ K(A) \subseteq K(A),
$$

$$
[H(A), H(A)] \subseteq K(A), \qquad [K(A), K(A)] \subseteq K(A), \qquad [K(A), H(A)] \subseteq H(A) .
$$

*Proof.* For self-adjoint $x, y$, $(xy)^* = y^*x^* = yx$ and $(yx)^* = xy$, so $xy + yx$ is fixed and $xy - yx$ is negated; the same computation with $x$ or $y$ skew gives the remaining four inclusions, the signs being the two possible combinations.

## The Jordan Structure

### The Axioms

**Definition.** A **Jordan algebra** over $k$ is a commutative $k$-algebra $J$ with a product written $x \circ y$ and a distinguished element $x^{\circ 2} = x \circ x$ such that

$$
(x^{\circ 2} \circ y) \circ x = x^{\circ 2} \circ (y \circ x) \quad \text{for all } x, y \in J .
$$

**Theorem.** The self-adjoint part $H(A)$ with the symmetrised product is a Jordan algebra; the product is commutative and $k$-bilinear, and the Jordan identity holds on $H(A)$ as a consequence of the associativity of the product of $A$. The identity element of $A$ is the identity of the Jordan algebra.

*Proof.* Commutativity and bilinearity are immediate from $x\circ y = \tfrac12(xy+yx)$. For the Jordan identity it is enough to expand the two sides in the associative product for self-adjoint $x$ and $y$:

$$
(x^2\circ y)\circ x = \tfrac14\bigl(x^2yx + yx^2x + xx^2y + xyx^2\bigr) = \tfrac14\bigl(x^2yx + yx^3 + x^3y + xyx^2\bigr),
$$

$$
x^2\circ(y\circ x) = \tfrac14\bigl(x^2yx + x^2xy + yxx^2 + xyx^2\bigr) = \tfrac14\bigl(x^2yx + x^3y + yx^3 + xyx^2\bigr),
$$

and the two expansions agree term by term, using only the associativity of the product of $A$; the identity element satisfies $1\circ h = h$ for every self-adjoint $h$ because $1h = h1 = h$.

**Corollary.** For every self-adjoint $x$ the powers defined by $x^{\circ 0} = 1$, $x^{\circ(n+1)} = x \circ x^{\circ n}$ satisfy $x^{\circ n} = x^n$, and the subalgebra of $H(A)$ generated by a single element is associative; in particular the Jordan algebra generated by one element is the algebra of the polynomials in that element with the symmetrised product.

*Proof.* The equality $x^{\circ n} = x^n$ follows by induction from the associativity of the product in $A$ and the commutativity of $x$ with its own powers; a Jordan algebra generated by one element is associative, by the general theory of *Jordan Algebras*.

### The Quadratic Representation

**Definition.** For a self-adjoint element $x$ the **quadratic representation** is the operator

$$
U_x : H(A) \longrightarrow H(A), \qquad U_x(y) = 2\,(x \circ (x \circ y)) - (x \circ x) \circ y .
$$

**Proposition.** The quadratic representation is $k$-linear in $y$ and satisfies $U_x(y) = xyx$ when read through the associative product of $A$; it is therefore determined by the associative product, and $U_x = 2L(x)^2 - L(x^2)$, where $L(x)$ is the left multiplication of the Jordan algebra by $x$.

*Proof.* Expand in the associative product: $x\circ(x\circ y) = \tfrac14(x^2y + 2xyx + yx^2)$ and $(x\circ x)\circ y = \tfrac12(x^2y + yx^2)$, so $2(x\circ(x\circ y)) - (x\circ x)\circ y = xyx$. The operator $L(x)$ acts by $L(x)y = x\circ y$, and the double product expansion gives the displayed independence from the associator.

**Corollary.** The quadratic representation satisfies $U_x(x) = x^3$ and $U_1 = \mathrm{id}$; the map $x \mapsto U_x$ is quadratic in $x$, and it is the substitute for the missing associativity of the Jordan product, in the sense that the products of three elements in $H(A)$ are governed by it.

### The Skew Part as a Lie Algebra

**Theorem.** The skew part $K(A)$ is a Lie algebra under $[x,y] = xy - yx$, and the bracket makes $K(A)\oplus H(A)$ a $\mathbb{Z}/2$-graded Lie algebra with the grading-compatible bracket of *Graded Lie Algebras and Lie Superalgebras*, the even part being $K(A)$ and the odd part $H(A)$; the bracket is also a module structure on the self-adjoint part, $[K(A),H(A)]\subseteq H(A)$, and the inclusion $[H(A),H(A)]\subseteq K(A)$ makes $H(A)$ a **Lie triple system** under $\{h_1,h_2,h_3\} = [h_1,[h_2,h_3]]$. The symmetrised product makes $H(A)$ a Jordan algebra and preserves $K(A)$ under multiplication by $H(A)$, $H(A)\circ K(A)\subseteq K(A)$, so that the pair $\bigl(H(A), K(A)\bigr)$ carries the two products.

*Proof.* The bracket inclusions $[K,K]\subseteq K$, $[K,H]\subseteq H$, $[H,H]\subseteq K$ of the preceding proposition give the three pieces of the graded structure, with the Jacobi identity inherited from the associativity of the product of $A$; the triple product of three self-adjoint elements is again self-adjoint, because $[h_2,h_3]\in K(A)$ and $[h_1,K(A)]\subseteq H(A)$; and the closure $H\circ K\subseteq K$ gives the action of the Jordan algebra on the skew part. The grading here is the compatible one and not the signed one: with the Koszul sign the bracket of two self-adjoint elements would be their anticommutator, which is self-adjoint rather than skew, so the sign rule would move the two parts and would not give this grading at all. The pair of the two products is the **Jordan pair** of the involution, and the verification of the remaining module axioms is the computation linking the two products; the structure theory of Jordan pairs belongs to *Jordan Algebras*, where the axioms are set out.

## The Elementary Elements

**Proposition.** The self-adjoint and skew parts contain the following elements for every $a \in A$:

$$
a + a^* \in H(A), \qquad a - a^* \in K(A), \qquad aa^* \in H(A), \qquad a^*a \in H(A), \qquad [a, a^*] \in K(A) .
$$

*Proof.* Apply the involution: $(a+a^*)^* = a^*+a$, $(a-a^*)^* = a^*-a$, $(aa^*)^* = aa^*$, $(a^*a)^* = a^*a$, and $[a,a^*]^* = [a^*, a] = -[a,a^*]$.

**Corollary.** Every element of $A$ is the sum of a self-adjoint and a skew element, and the element $aa^*$ is self-adjoint; when $aa^* = 0$ implies $a = 0$ for every $a$ — the case of an algebra with a positive definite norm form, whose theory is Part II — the self-adjoint part carries the order structure of the squares, and that order belongs to *Hilbert Algebras*, not here.

## The Examples

### The Transpose on a Matrix Algebra

Let $A = M_n(k)$ with $X^* = X^{\mathsf{T}}$ and $2 \neq 0$. The self-adjoint part is the space of the symmetric matrices, of dimension $n(n+1)/2$; the skew part is the space of the alternating matrices, of dimension $n(n-1)/2$; and $H(A)$ is the Jordan algebra in which the symmetrised product of two symmetric matrices is symmetric. The skew part is the Lie algebra $\mathfrak{so}_n$ under the commutator, and the pair $(\mathfrak{so}_n, \mathrm{Sym})$ is the graded Lie algebra of the involution, the symmetric matrices also being a Lie triple system under $\{h_1,h_2,h_3\} = [h_1,[h_2,h_3]]$. The two dimensions add to $n^2$, as the decomposition requires.

### The Conjugate Transpose on a Complex Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the conjugate transpose $X^* = \overline{X}^{\mathsf{T}}$. The self-adjoint part is the space of the Hermitian matrices, a real Jordan algebra under the symmetrised product, and the skew part is the space of the skew-Hermitian matrices, the Lie algebra $\mathfrak{u}_n$; the decomposition is the one of every matrix into its Hermitian and skew-Hermitian parts. The scalars here are the complex numbers with the conjugation, so the involution on $A$ is $\varsigma$-semilinear; the Hermitian form and the positive definiteness of the self-adjoint part belong to *Hilbert Algebras*.

### The Trivial Involution

Let $\sigma = \mathrm{id}_A$. Then $H(A) = A$ and $K(A) = 0$, and the symmetrised product is the anticommutator $x\circ y = \tfrac12(xy+yx)$; the Jordan algebra is the special Jordan algebra $A^+$ associated with the associative algebra $A$, which is the ordinary algebra only when $A$ is commutative. The example shows that the Jordan structure exists whether or not the skew part does.

### The Inversion on a Group Algebra

Let $A = k[G]$ with the involution $g^* = g^{-1}$. Then the self-adjoint part is spanned by the elements $g + g^{-1}$ for $g$ not of order two and by the $g$ of order two, and the skew part by the differences $g - g^{-1}$; the self-adjoint part is the Jordan algebra of the symmetric elements of the group algebra, and the decomposition of $k[G]$ into its self-adjoint and skew parts is the one used in the harmonic analysis of the group, whose analytic reading belongs to Part II.

### The Exchange Involution

Let $A = B \times B^{\mathrm{op}}$ with the exchange involution $(b,c)^* = (c,b)$. The self-adjoint part is the diagonal $\{(b,b)\} \cong B$, and the skew part is the antidiagonal $\{(b,-b)\} \cong B$; the symmetrised product on the diagonal is the product of $B$, so $H(A) \cong B$ as an algebra, and the skew part is the Lie algebra $B$ under the commutator.

## Summary

The **self-adjoint part** $H(A) = \{h : h^* = h\}$ of an algebra with an involution is a linear subspace with $A = H(A)\oplus K(A)$, where $K(A) = \{k : k^* = -k\}$ is the skew part; the unit lies in $H(A)$, and the decomposition $x = \tfrac12(x+x^*) + \tfrac12(x-x^*)$ is the eigenvalue decomposition of the involution. The symmetrised product $x\circ y = \tfrac12(xy+yx)$ makes $H(A)$ a **Jordan algebra**, commutative, with the Jordan identity inherited from the associativity of $A$; the powers in the Jordan product coincide with the ordinary powers, and the subalgebra generated by one element is associative. The **quadratic representation** $U_x(y) = 2(x\circ(x\circ y)) - (x\circ x)\circ y$ equals $xyx$ in the associative product and supplies the missing associativity. The skew part $K(A)$ is a Lie algebra under the commutator and a Jordan module over $H(A)$ under the symmetrised product, so that $K(A)\oplus H(A)$ is a $\mathbb{Z}/2$-graded Lie algebra with the grading-compatible bracket, the even part being $K(A)$ and the odd part $H(A)$, and the self-adjoint part is a Lie triple system under $\{h_1,h_2,h_3\} = [h_1,[h_2,h_3]]$. The standard examples are the symmetric matrices with the transpose and the Hermitian matrices with the conjugate transpose, whose positive and normed theory belongs to *Hilbert Algebras*. The general involution and the decomposition are *Involutive Linear Algebras*; the Jordan algebras are *Jordan Algebras* of the same reading unit; the unitary elements and the skew Lie algebra are *Unitary Elements of an Involutive Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars, of characteristic not two |
| $A$ | a unital associative $k$-algebra |
| $\sigma$, $x^* = \sigma(x)$ | the involution and the adjoint of an element |
| $H(A) = A^+$ | the self-adjoint elements, $h^* = h$ |
| $K(A) = A^-$ | the skew elements, $k^* = -k$ |
| $x \circ y = \tfrac12(xy+yx)$ | the symmetrised product |
| $x^{\circ n}$ | the Jordan powers |
| $U_x(y) = xyx$ | the quadratic representation |
| $L(x)$ | the left multiplication of the Jordan algebra |
| $\mathfrak{so}_n, \mathfrak{u}_n$ | the skew parts of the matrix examples |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan algebra of the self-adjoint elements and the quadratic representation.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan axioms, the special Jordan algebras and the quadratic representation.
- Israel Nathan Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and the skew elements and the graded Lie structure.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the self-adjoint part of an algebra with involution.
