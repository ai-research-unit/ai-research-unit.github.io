# __The Self-Adjoint Part of an Algebra__

## Introduction

An involution of an algebra selects the elements it fixes: the **self-adjoint part** $H(A) = A^+$, whose elements satisfy $h^* = h$. The selection is not a subalgebra in the ordinary sense, because the product of two self-adjoint elements need not be self-adjoint; it is a subalgebra of the **symmetrised** algebra, closed under the Jordan product $x \bullet y = \tfrac12(xy + yx)$. The self-adjoint part is therefore a Jordan algebra.

This article develops the self-adjoint part, the symmetrised product and the Jordan axioms it satisfies, and the standard examples of the symmetric matrices with the transpose and of the Hermitian matrices with the conjugate transpose. The involution on the elements and the decomposition $A = A^+ \oplus A^-$ are *Involutive Algebras*; the Jordan algebras themselves, their classification and their structure theory are *Jordan Algebras* of the same reading unit; the complementary skew part, its Lie algebra and its Jordan module structure are *The Skew Part of an Algebra*, in *Anti-symmetric Algebras*; the unitary elements are *Unitary Elements of an Involutive Algebra*; and the positivity, the order and the norms of the self-adjoint part are Part II and *Hilbert Algebras*.

Throughout, $k$ is a field of characteristic not two, $A$ is a unital associative $k$-algebra with unit $1$, $\sigma$ is an involution of $A$, and the image of an element is written $x^* = \sigma(x)$. The self-adjoint part is $H(A) = \{h \in A : h^* = h\}$, the skew part is $K(A) = A^- = \{k \in A : k^* = -k\}$, the symmetrised product is $x \bullet y = \tfrac12(xy + yx)$, and the unit is self-adjoint because $1^* = 1$.

## The Self-Adjoint Part

### Definition and the Decomposition

**Definition.** The **self-adjoint part** of $(A,\sigma)$ is

$$
H(A) = A^+ = \{h \in A : h^* = h\},
$$

the **skew part** is $K(A) = A^- = \{k \in A : k^* = -k\}$, and the **symmetrised product** is $x \bullet y = \tfrac12(xy+yx)$. The **square** of an element is $x^2 = x \bullet x$ in the Jordan reading.

**Proposition.** $H(A)$ and $K(A)$ are $k$-linear subspaces with

$$
\boxed{\;A = H(A) \oplus K(A), \qquad x = \tfrac12\bigl(x + x^*\bigr) + \tfrac12\bigl(x - x^*\bigr), \qquad 1 \in H(A)\;},
$$

and the involution acts as the identity on $H(A)$ and as minus the identity on $K(A)$; the two spaces are the eigenspaces of $\sigma$ for the eigenvalues $1$ and $-1$.

*Proof.* The involution is linear and has order two, so its eigenvalues lie in $\{1,-1\}$ and the algebra is the direct sum of the two eigenspaces, over a field of characteristic not two in which the averaging decomposition displayed is legitimate; the unit is fixed because $1^* = 1$.

### The Symmetrised Product on the Self-Adjoint Part

**Proposition.** For $x, y \in H(A)$ the product $xy$ satisfies $(xy)^* = yx$, and the symmetrised product is self-adjoint:

$$
\boxed{\;H(A) \bullet H(A) \subseteq H(A)\;}.
$$

*Proof.* For self-adjoint $x, y$, $(xy)^* = y^*x^* = yx$ and $(yx)^* = xy$, so $xy + yx$ is fixed by the involution and the half-sum is self-adjoint.

**Remark (the skew part).** The same computation with one or two signs reversed gives $K(A) \bullet K(A) \subseteq H(A)$ and $H(A) \bullet K(A) \subseteq K(A)$, and the commutator satisfies $[H,H] \subseteq K$, $[H,K] \subseteq H$ and $[K,K] \subseteq K$. The Lie algebra, the graded structure and the Jordan module formed by the two parts are *The Skew Part of an Algebra*; they are recorded here only for the completeness of the pair and are not used in this article.

## The Jordan Structure

### The Axioms

**Definition.** A **Jordan algebra** over $k$ is a commutative $k$-algebra $J$ with a product written $x \bullet y$ and a distinguished element $x^{\circ 2} = x \bullet x$ such that

$$
(x^{\circ 2} \bullet y) \bullet x = x^{\circ 2} \bullet (y \bullet x) \quad \text{for all } x, y \in J .
$$

**Theorem.** The self-adjoint part $H(A)$ with the symmetrised product is a Jordan algebra; the product is commutative and $k$-bilinear, and the Jordan identity holds on $H(A)$ as a consequence of the associativity of the product of $A$. The identity element of $A$ is the identity of the Jordan algebra.

*Proof.* Commutativity and bilinearity are immediate from $x\bullet y = \tfrac12(xy+yx)$. For the Jordan identity it is enough to expand the two sides in the associative product for self-adjoint $x$ and $y$:

$$
(x^2\bullet y)\bullet x = \tfrac14\bigl(x^2yx + yx^2x + xx^2y + xyx^2\bigr) = \tfrac14\bigl(x^2yx + yx^3 + x^3y + xyx^2\bigr),
$$

$$
x^2\bullet(y\bullet x) = \tfrac14\bigl(x^2yx + x^2xy + yxx^2 + xyx^2\bigr) = \tfrac14\bigl(x^2yx + x^3y + yx^3 + xyx^2\bigr),
$$

and the two expansions agree term by term, using only the associativity of the product of $A$; the identity element satisfies $1\bullet h = h$ for every self-adjoint $h$ because $1h = h1 = h$.

**Corollary.** For every self-adjoint $x$ the powers defined by $x^{\circ 0} = 1$, $x^{\circ(n+1)} = x \bullet x^{\circ n}$ satisfy $x^{\circ n} = x^n$, and the subalgebra of $H(A)$ generated by a single element is associative; in particular the Jordan algebra generated by one element is the algebra of the polynomials in that element with the symmetrised product.

*Proof.* The equality $x^{\circ n} = x^n$ follows by induction from the associativity of the product in $A$ and the commutativity of $x$ with its own powers; a Jordan algebra generated by one element is associative, by the general theory of *Jordan Algebras*.

### The Quadratic Representation

The quadratic representation $\mathrm{Jor}_x(y)=2\,(x\bullet(x\bullet y))-(x\bullet x)\bullet y$, the identity $\mathrm{Jor}_x(y)=xyx$ in the associative product, and the fundamental formula it satisfies are operator theory: they are *The Left and Right Multiplication Operators on a Jordan Algebra*, §*The Quadratic Representation*, and *The Jordan Multiplication Operators*, §*The Quadratic Representation*. They are cited where needed and are not developed here.

## The Elementary Elements

**Proposition.** The self-adjoint part contains the following elements for every $a \in A$:

$$
\boxed{\;a + a^* \in H(A), \qquad aa^* \in H(A), \qquad a^*a \in H(A)\;}.
$$

*Proof.* Apply the involution: $(a+a^*)^* = a^*+a$, $(aa^*)^* = aa^*$, and $(a^*a)^* = a^*a$.

**Corollary.** Every element of $A$ is the sum of a self-adjoint and a skew element, and the element $aa^*$ is self-adjoint; when $aa^* = 0$ implies $a = 0$ for every $a$ — the case of an algebra with a positive definite norm form, whose theory is Part II — the self-adjoint part carries the order structure of the squares, and that order belongs to *Hilbert Algebras*, not here.

## The Examples

### The Transpose on a Matrix Algebra

Let $A = M_n(k)$ with $X^* = X^{\mathsf{T}}$ and $2 \neq 0$. The self-adjoint part is the space of the symmetric matrices, of dimension $n(n+1)/2$, and $H(A)$ is the Jordan algebra in which the symmetrised product of two symmetric matrices is symmetric. The complementary skew part is the space of the alternating matrices, of dimension $n(n-1)/2$, and its Lie theory is *The Skew Part of an Algebra*. The two dimensions add to $n^2$, as the decomposition requires.

### The Conjugate Transpose on a Complex Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the conjugate transpose $X^* = \overline{X}^{\mathsf{T}}$. The self-adjoint part is the space of the Hermitian matrices, a real Jordan algebra under the symmetrised product. The scalars here are the complex numbers with the conjugation, so the involution on $A$ is $\varsigma$-semilinear; the Hermitian form and the positive definiteness of the self-adjoint part belong to *Hilbert Algebras*.

### The Trivial Involution

Let $\sigma = \mathrm{id}_A$. Then $H(A) = A$ and $K(A) = 0$, and the symmetrised product is the anticommutator $x\bullet y = \tfrac12(xy+yx)$; the Jordan algebra is the **special Jordan algebra** of the associative algebra $A$, that is $A$ with the symmetrised product, which is the ordinary algebra only when $A$ is commutative. The example shows that the Jordan structure exists whether or not the skew part does.

### The Inversion on a Group Algebra

Let $A = k[G]$ with the involution $g^* = g^{-1}$. Then the self-adjoint part is spanned by the elements $g + g^{-1}$ for $g$ not of order two and by the $g$ of order two, and the skew part by the differences $g - g^{-1}$; the self-adjoint part is the Jordan algebra of the symmetric elements of the group algebra. The decomposition of $k[G]$ into its self-adjoint and skew parts is the one used in the harmonic analysis of the group, whose analytic reading belongs to Part II.

### The Exchange Involution

Let $A = B \times B^{\mathrm{opp}}$ with the exchange involution $(b,c)^* = (c,b)$. The self-adjoint part is the diagonal $\{(b,b)\} \cong B$, and the skew part is the antidiagonal $\{(b,-b)\} \cong B$. The ordinary product of the diagonal is $(b,b)(c,c) = (bc,cb)$, which stays in the diagonal exactly when $b$ and $c$ commute; the symmetrised product is $(b \bullet c, b \bullet c)$, so $H(A)$ is the Jordan algebra $B^+$ of *Jordan Algebras*, and it is a subalgebra exactly when $B$ is commutative.

## Summary

The **self-adjoint part** $H(A) = \{h : h^* = h\}$ of an algebra with an involution is a linear subspace with $A = H(A)\oplus K(A)$, where $K(A) = \{k : k^* = -k\}$ is the skew part; the unit lies in $H(A)$, and the decomposition $x = \tfrac12(x+x^*) + \tfrac12(x-x^*)$ is the eigenvalue decomposition of the involution. The symmetrised product $x\bullet y = \tfrac12(xy+yx)$ makes $H(A)$ a **Jordan algebra**, commutative, with the Jordan identity inherited from the associativity of $A$; the powers in the Jordan product coincide with the ordinary powers, and the subalgebra generated by one element is associative. The quadratic representation and the fundamental formula it satisfies are operator theory and are cited in §*The Quadratic Representation*. The complementary skew part carries the Lie algebra, the graded structure and the Jordan module of *The Skew Part of an Algebra*, and it is not developed here. The standard examples are the symmetric matrices with the transpose and the Hermitian matrices with the conjugate transpose, whose positive and normed theory belongs to *Hilbert Algebras*. The general involution and the decomposition are *Involutive Algebras*; the Jordan algebras are *Jordan Algebras* of the same reading unit; the unitary elements are *Unitary Elements of an Involutive Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars, of characteristic not two |
| $A$ | a unital associative $k$-algebra |
| $\sigma$, $x^* = \sigma(x)$ | the involution and the adjoint of an element |
| $H(A) = A^+$ | the self-adjoint elements, $h^* = h$ |
| $K(A) = A^-$ | the skew elements, $k^* = -k$, the complement |
| $x \bullet y = \tfrac12(xy+yx)$ | the symmetrised product |
| $x^{\circ n}$ | the Jordan powers |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan algebra of the self-adjoint elements and the quadratic representation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the symmetric parts of the involutions of a central simple algebra.
