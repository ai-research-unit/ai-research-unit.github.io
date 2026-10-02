# __Unitary Elements of an Involutive Algebra__

## Introduction

An involution of an algebra carries an element $u$ to its **adjoint** $u^* = \sigma(u)$, and the elements whose adjoint is their inverse, $u^*u = uu^* = 1$, are the **unitary elements**. They form a group under multiplication, they sit inside the group of units, and they are the algebraic group that an involution produces: the solutions of the quadratic equation $u^*u = 1$. Two companion objects live beside them — the **self-adjoint** elements, with $h^* = h$, and the **skew** elements, with $k^* = -k$ — and the three are tied together by the identities $u + u^* = 2h$ and $u - u^* = 2k$ for every unitary $u$.

This article develops the unitary elements, the group they form as the fixed subgroup of an order-two automorphism of the units, the skew elements as the algebraic tangent space at the identity and as a Lie algebra under the commutator, and the relation between the unitary and the self-adjoint parts. The involution on the elements, the decomposition $A = A^+\oplus A^-$, the Lie algebra of the skew elements and the Jordan algebra of the symmetric ones are the subject of *Involutive Linear Algebras*; the self-adjoint part is developed in *The Self-Adjoint Part of an Algebra*; and the forms, the adjoint involution that a form defines and the orthogonal and unitary groups of a form are Part II and *Hilbert Algebras*, which own them.

Throughout, $k$ is a field of characteristic not two, $A$ is a unital associative $k$-algebra, and $\sigma$ is an involution of $A$; the image of an element is written $u^* = \sigma(u)$, so that $(uv)^* = v^*u^*$ and $(u^*)^* = u$. The fixed elements $A^+ = \{h : h^* = h\}$ are **self-adjoint** and the negated elements $A^- = \{k : k^* = -k\}$ are **skew**; the group of units is $A^\times$, and the group of unitary elements is written $U(A) = U(A,\sigma)$.

## The Unitary Elements

### Definition

**Definition.** An element $u \in A$ is **unitary** for $\sigma$ if

$$
u^*u = 1 \quad \text{and} \quad uu^* = 1 .
$$

The set of unitary elements is written $U(A) = U(A,\sigma)$, and an element of $U(A)$ is also called a **unitary** of $(A,\sigma)$.

**Proposition.** An element $u$ is unitary if and only if it is a unit and $u^* = u^{-1}$; every unitary is a unit, $1$ is unitary, and the two equations $u^*u = 1$ and $uu^* = 1$ are equivalent when $A$ is finite-dimensional.

*Proof.* If $u^*u = 1$ and $uu^* = 1$ then $u$ has the two-sided inverse $u^*$, so $u \in A^\times$ and $u^* = u^{-1}$. Conversely if $u$ is a unit with $u^* = u^{-1}$ then both products are $1$. The two equations are the two halves of invertibility, and in finite dimension a one-sided inverse of a linear map is two-sided, so either equation suffices.

### The Group

**Theorem.** The unitary elements form a subgroup $U(A) \leq A^\times$. Precisely, the map

$$
\theta : A^\times \longrightarrow A^\times, \qquad \theta(g) = (g^*)^{-1} = \sigma(g)^{-1},
$$

is an automorphism of the group of units with $\theta^2 = \mathrm{id}$, and

$$
U(A) = \{g \in A^\times : \theta(g) = g\}
$$

is its fixed subgroup.

*Proof.* The involution $\sigma$ restricts to an anti-automorphism of $A^\times$ and the inversion is an anti-automorphism of $A^\times$, so their composite $\theta$ is an automorphism; $\theta^2(g) = \sigma(\sigma(g)^{-1})^{-1} = \bigl(\sigma(\sigma(g))^{-1}\bigr)^{-1} = \bigl(g^{-1}\bigr)^{-1} = g$, so $\theta$ has order two. An element is fixed by $\theta$ exactly when $(g^*)^{-1} = g$, that is $g^* = g^{-1}$, which is the unitary condition. A fixed subgroup of an order-two automorphism is a subgroup, so $U(A)$ is a subgroup of $A^\times$, containing $1$, closed under products and inverses; the closure under products can also be checked directly, $(uv)^* = v^*u^* = v^{-1}u^{-1} = (uv)^{-1}$.

**Corollary.** $U(A,\sigma)$ is the fixed subgroup of the involutive group $(A^\times,\theta)$ in the sense of *Involutive Groups*, and the assignment $(A,\sigma)\mapsto(U(A,\sigma),\theta)$ is the passage from the involutive algebra to its involutive group of units. For the trivial involution $\sigma = \mathrm{id}$ the automorphism $\theta$ is the inversion, and $U(A,\mathrm{id})$ is the set of the elements $u$ with $u^2 = 1$, which is a subgroup of $A^\times$ exactly when those elements commute pairwise.

## The Skew Elements and the Tangent Space

### The Lie Algebra of the Skew Elements

**Proposition.** The skew elements $A^-$ are closed under the commutator,

$$
[A^-, A^-] \subseteq A^-, \qquad [A^-, A^+] \subseteq A^+, \qquad [A^+, A^+] \subseteq A^-,
$$

so that $A^-$ is a Lie algebra under $[x,y] = xy - yx$, that $A^+$ is a module over it, and that $A^- \oplus A^+$ is a $\mathbb{Z}/2$-graded Lie algebra with the grading-compatible bracket of *Graded Lie Algebras and Lie Superalgebras* — the Koszul sign would give the anticommutator on two skew elements, which is self-adjoint, so the signed convention is not the one here; and since $[A^+,A^+]\subseteq A^-$ and $[A^-,A^+]\subseteq A^+$, the self-adjoint part is also a Lie triple system under $\{h_1,h_2,h_3\} = [h_1,[h_2,h_3]]$. The first statement is that of *Involutive Linear Algebras*.

*Proof.* For $x$ skew and $y$ skew, $(xy)^* = y^*x^* = (-y)(-x) = yx$, so $[x,y]^* = (xy-yx)^* = yx - xy = -[x,y]$ and $[x,y]$ is skew. The two mixed cases are the same computation with one sign, and the even-even case is the first with the signs cancelled.

### The Tangent at the Identity

**Theorem.** The skew elements are the elements that make $1 + t x$ unitary to first order in $t$: expanding

$$
(1+tx)^*(1+tx) = 1 + t(x + x^*) + t^2 x^*x
$$

shows that the coefficient of $t$ vanishes exactly when $x^* = -x$, that is exactly when $x$ is skew. Consequently $A^-$ is the algebraic tangent space of the unitary group at the identity, and the Lie bracket of two skew elements is the second-order shadow of the group commutator: the coefficient of the leading term in the expansion of $(1+tx)(1+ty)(1+tx)^{-1}(1+ty)^{-1}$ lies in the span of $[x,y]$.

*Proof.* The expansion displayed is the definition of the product; the linear term vanishes exactly for $x^* = -x$. For the second statement one expands the four factors to second order; the quadratic part involves $[x,y]$ and the identity $x^* = -x$, $y^* = -y$, and it is the standard identification of the bracket with the commutator of the group, whose totality belongs to the theory of *Involutive Groups* and of the linear groups of Part II.

**Corollary.** For every unitary $u$ the elements $u + u^*$ and $i(u - u^*)$ are self-adjoint when the square root of $-1$ exists in $k$, and $u - u^*$ is always skew. The unitary elements therefore decompose in the affine form

$$
u = \tfrac12(u + u^*) + \tfrac12(u - u^*),
$$

the first summand self-adjoint and the second skew, which is the decomposition $A = A^+\oplus A^-$ applied to $u$.

## The Relation to the Self-Adjoint Part

### The Self-Adjoint Elements of a Unitary

**Proposition.** Let $u$ be unitary. Then $u + u^*$ and $u u^*$ are self-adjoint, $u - u^*$ is skew, and

$$
(u + u^*)^* = u + u^*, \qquad (u - u^*)^* = -(u - u^*), \qquad (u u^*)^* = u u^* = 1 .
$$

*Proof.* Apply $^*$ and use $(uv)^* = v^*u^*$ and $u^* = u^{-1}$: $(u+u^*)^* = u^* + u = u+u^*$, $(u-u^*)^* = u^* - u = -(u-u^*)$, and $(uu^*)^* = u u^* = 1$.

### The Symmetrised Product

**Definition.** The **symmetrised product** of two elements is $x \circ y = \tfrac12(xy + yx)$, and the self-adjoint part $H(A) = A^+$ is a **Jordan algebra** under it, in the sense of *Involutive Linear Algebras*.

**Proposition.** The symmetrised product of two skew elements and of two self-adjoint elements is self-adjoint, while the symmetrised product of a self-adjoint and a skew element is skew:

$$
A^- \circ A^- \subseteq A^+, \qquad A^+ \circ A^+ \subseteq A^+, \qquad A^+ \circ A^- \subseteq A^- .
$$

Consequently $H(A)$ is closed under $\circ$, and the skew part $A^-$ is a **Jordan module** over the Jordan algebra $H(A)$ under the same product.

*Proof.* For $x, y$ skew, $(xy)^* = y^*x^* = yx$ and $(yx)^* = xy$, so $\tfrac12(xy+yx)$ is fixed by $^*$; similarly for two self-adjoint elements. For $h$ self-adjoint and $k$ skew, $(hk)^* = k^*h^* = -kh$ and $(kh)^* = -hk$, so the half-sum is negated by $^*$.

### The Cayley Transform

**Proposition.** Let $k$ be a skew element with $1 - k$ invertible, and set

$$
u = (1+k)(1-k)^{-1} .
$$

Then $u$ is unitary, and its inverse is $(1-k)(1+k)^{-1}$. In particular the unitary group contains the image of the Cayley transform of the skew elements, and the transform is the algebraic substitute for the exponential of the Lie algebra: its first-order term at $k = 0$ is $2k$.

*Proof.* Compute $u^* = \bigl((1-k)^{-1}\bigr)^*(1+k)^*$. Since $(1-k)^* = 1 + k$ and $(1+k)^* = 1-k$, and since the involution reverses inverses, $u^* = (1+k)^{-1}(1-k)$. The factors $1+k$ and $1-k$ commute, so

$$
u^*u = (1+k)^{-1}(1-k)(1+k)(1-k)^{-1} = (1+k)^{-1}(1-k^2)(1-k)^{-1} = (1+k)^{-1}(1+k)(1-k)(1-k)^{-1} = 1,
$$

and the same computation with the factors in the other order gives $uu^* = 1$. The derivative statement is the expansion $u = (1+k)(1 + k + k^2 + \cdots) = 1 + 2k + O(k^2)$ for nilpotent or small $k$.

The exponential $e^{k}$ is not available in a bare $k$-algebra; the formal series identifies the Lie algebra of the skew elements with the unitary group, as in the theory of the linear groups, and the convergent reading belongs to *Hilbert Algebras* and to Part II.

## The Examples

### The Trivial Involution

Let $\sigma = \mathrm{id}_A$. Then $u^* = u$, the group $U(A,\mathrm{id})$ is the set of the units $u$ with $u^2 = 1$, that is the involutions of the group of units, and the skew part $A^- = \{k : k = -k\}$ is zero in characteristic not two. The example is the degenerate one, and it shows that the unitary group measures the involution and not the algebra.

### The Transpose on a Matrix Algebra

Let $A = M_n(k)$ with the transpose, $X^* = X^{\mathsf{T}}$, and $2 \neq 0$. Then $U(A) = \{X \in GL_n(k) : X^{\mathsf{T}}X = 1\} = O_n(k)$ is the orthogonal group of the standard symmetric form; the skew part is the space of the alternating matrices, the self-adjoint part the space of the symmetric matrices, and the decomposition $M_n = \mathrm{Sym}\oplus \mathrm{Alt}$ is the one of *Involutive Linear Algebras*. The form that makes $O_n(k)$ the orthogonal group, and its classification among the symmetric and the alternating forms, belong to *Hilbert Algebras*.

### The Inversion on a Group Algebra

Let $A = k[G]$ with the involution $\sigma(g) = g^{-1}$; then $(uv)^* = v^*u^*$ because the inversion reverses products, so $\sigma$ is an involution, and each group element $g$ is unitary, $g^* = g^{-1}$. The map $G \to U(k[G],\sigma)$ is injective, and the unitary group contains the image of $G$; the rest of the unitary group consists of the invertible elements $u$ with $u^*=u^{-1}$ and depends on $G$ and on $k$.

### The Exchange Involution

Let $A = B \times B^{\mathrm{op}}$ with the exchange involution $(b, c)^* = (c, b)$, as in *Involutive Linear Algebras*. An element $(b,c)$ is unitary exactly when $(c,b)(b,c) = 1$, that is when $cb = 1$ and $bc = 1$, so $c = b^{-1}$; hence

$$
U(B \times B^{\mathrm{op}}) = \{(b, b^{-1}) : b \in B^\times\} \cong B^\times ,
$$

and the unitary group of the exchange involution is the group of units of $B$.

### The Conjugate Transpose

Let $A = M_n(\mathbb{C})$ with the $\varsigma$-semilinear conjugate transpose $X^* = \overline{X}^{\mathsf{T}}$. The unitary elements are the matrices with $X^*X = 1$, that is the unitary group $U_n$; the self-adjoint elements are the Hermitian matrices and the skew elements the skew-Hermitian ones. The conjugation $\varsigma$ of $\mathbb{C}$ is a semilinear involution of the scalars, the case of the second kind, and the form of the associated sesquilinear pairing belongs to *Hilbert Algebras*.

## Summary

For an involution $\sigma$ of $A$, written $u^* = \sigma(u)$, the **unitary elements** are those with $u^*u = uu^* = 1$, equivalently the units with $u^* = u^{-1}$. They form the subgroup $U(A) \leq A^\times$, which is the fixed subgroup of the order-two automorphism $\theta(g) = (g^*)^{-1}$ of $A^\times$; this is the passage from the involutive algebra to the involutive group of units of *Involutive Groups*. The **skew** elements $A^- = \{k : k^* = -k\}$ are closed under the commutator, so they form a Lie algebra, and they are the algebraic tangent space of $U(A)$ at the identity: the elements $x$ with $1 + tx$ unitary to first order are exactly the skew elements. The **self-adjoint** elements $A^+ = H(A)$ form the Jordan algebra under the symmetrised product, and $A^-$ is a Jordan module over it; every unitary decomposes as $u = \tfrac12(u+u^*) + \tfrac12(u-u^*)$ into a self-adjoint and a skew part. The examples are the orthogonal group for the transpose, the image of $G$ for the inversion of a group algebra, the group of units for the exchange involution, and the unitary group for the conjugate transpose. The involution on the elements is *Involutive Linear Algebras*, the self-adjoint part is *The Self-Adjoint Part of an Algebra*, the forms and the linear groups belong to *Hilbert Algebras* and to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars, of characteristic not two |
| $A$ | a unital associative $k$-algebra |
| $\sigma$ | an involution of $A$ |
| $u^* = \sigma(u)$ | the adjoint of an element |
| $A^+ = H(A)$ | the self-adjoint elements, $h^* = h$ |
| $A^-$ | the skew elements, $k^* = -k$ |
| $U(A) = U(A,\sigma)$ | the unitary elements, $u^*u = uu^* = 1$ |
| $\theta(g) = (g^*)^{-1}$ | the order-two automorphism of $A^\times$ |
| $x \circ y = \tfrac12(xy+yx)$ | the symmetrised product |
| $O_n(k)$ | the orthogonal group, for the transpose |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the unitary elements and the involutions of a central simple algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan algebra of the self-adjoint elements and the symmetrised product.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the unitary and the self-adjoint elements of an algebra with involution.
- Israel Nathan Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and the skew elements and their Lie and Jordan structures.
