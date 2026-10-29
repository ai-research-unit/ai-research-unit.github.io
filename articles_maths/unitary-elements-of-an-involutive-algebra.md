# __Unitary Elements of an Involutive Algebra__

## Introduction

An involution of an algebra carries an element $u$ to its **adjoint** $u^* = \sigma(u)$, and the elements whose adjoint is their inverse, $u^*u = uu^* = 1$, are the **unitary elements**. They form a group under multiplication, they sit inside the group of units, and they are the algebraic group that an involution produces: the solutions of the quadratic equation $u^*u = 1$. Two companion objects live beside them — the **self-adjoint** elements, with $h^* = h$, and the **skew** elements, with $k^* = -k$ — and every unitary decomposes as $u = \tfrac12(u+u^*) + \tfrac12(u-u^*)$ into a self-adjoint and a skew part.

This article develops the unitary elements, the group they form as the fixed subgroup of an order-two automorphism of the units, and the relation between a unitary and its self-adjoint part. The involution on the elements and the decomposition $A = A^+ \oplus A^-$ are *Involutive Algebras*; the skew part, its Lie algebra, the tangent space at the identity and the Cayley transform are *The Skew Part of an Algebra*, in *Anti-symmetric Algebras*; the self-adjoint part and the symmetrised product are *The Self-Adjoint Part of an Algebra*, in *Symmetric Algebras*; and the forms, the adjoint involution that a form defines and the orthogonal and unitary groups of a form are Part II and *Hilbert Algebras*, which own them.

Throughout, $k$ is a field of characteristic not two, $A$ is a unital associative $k$-algebra, and $\sigma$ is an involution of $A$; the image of an element is written $u^* = \sigma(u)$, so that $(uv)^* = v^*u^*$ and $(u^*)^* = u$. The fixed elements $A^+ = \{h : h^* = h\}$ are **self-adjoint** and the negated elements $A^- = \{k : k^* = -k\}$ are **skew**; the group of units is $A^\times$, and the group of unitary elements is written $\mathrm{U}(A) = \mathrm{U}(A,\sigma)$.

## The Unitary Elements

### Definition

**Definition.** An element $u \in A$ is **unitary** for $\sigma$ if

$$
u^*u = 1 \quad \text{and} \quad uu^* = 1 .
$$

The set of unitary elements is written $\mathrm{U}(A) = \mathrm{U}(A,\sigma)$, and an element of $\mathrm{U}(A)$ is also called a **unitary** of $(A,\sigma)$.

**Proposition.** An element $u$ is unitary if and only if it is a unit and $u^* = u^{-1}$; every unitary is a unit, $1$ is unitary, and the two equations $u^*u = 1$ and $uu^* = 1$ are equivalent when $A$ is finite-dimensional.

*Proof.* If $u^*u = 1$ and $uu^* = 1$ then $u$ has the two-sided inverse $u^*$, so $u \in A^\times$ and $u^* = u^{-1}$. Conversely if $u$ is a unit with $u^* = u^{-1}$ then both products are $1$. The two equations are the two halves of invertibility, and in finite dimension a one-sided inverse of a linear map is two-sided, so either equation suffices.

### The Group

**Theorem.** The unitary elements form a subgroup $\mathrm{U}(A) \leq A^\times$. Precisely, the map

$$
\theta : A^\times \longrightarrow A^\times, \qquad \theta(g) = (g^*)^{-1} = \sigma(g)^{-1},
$$

is an automorphism of the group of units with $\theta^2 = \mathrm{id}$, and

$$
\boxed{\;\mathrm{U}(A) = \{g \in A^\times : \theta(g) = g\}\;}
$$

is its fixed subgroup.

*Proof.* The involution $\sigma$ restricts to an anti-automorphism of $A^\times$ and the inversion is an anti-automorphism of $A^\times$, so their composite $\theta$ is an automorphism; $\theta^2(g) = \sigma(\sigma(g)^{-1})^{-1} = \bigl(\sigma(\sigma(g))^{-1}\bigr)^{-1} = \bigl(g^{-1}\bigr)^{-1} = g$, so $\theta$ has order two. An element is fixed by $\theta$ exactly when $(g^*)^{-1} = g$, that is $g^* = g^{-1}$, which is the unitary condition. A fixed subgroup of an order-two automorphism is a subgroup, so $\mathrm{U}(A)$ is a subgroup of $A^\times$, containing $1$, closed under products and inverses; the closure under products can also be checked directly, $(uv)^* = v^*u^* = v^{-1}u^{-1} = (uv)^{-1}$.

**Corollary.** $\mathrm{U}(A,\sigma)$ is the fixed subgroup of the involutive group $(A^\times,\theta)$ in the sense of *Involutive Groups*, and the assignment $(A,\sigma)\mapsto(\mathrm{U}(A,\sigma),\theta)$ is the passage from the involutive algebra to its involutive group of units. For the trivial involution $\sigma = \mathrm{id}$ the automorphism $\theta$ is the inversion, and $\mathrm{U}(A,\mathrm{id})$ is the set of the elements $u$ with $u^2 = 1$, which is a subgroup of $A^\times$ exactly when those elements commute pairwise.

## The Self-Adjoint Elements of a Unitary

**Proposition.** Let $u$ be unitary. Then $u + u^*$ and $u u^*$ are self-adjoint, $u - u^*$ is skew, and

$$
(u + u^*)^* = u + u^*, \qquad (u - u^*)^* = -(u - u^*), \qquad (u u^*)^* = u u^* = 1 .
$$

*Proof.* Apply $^*$ and use $(uv)^* = v^*u^*$ and $u^* = u^{-1}$: $(u+u^*)^* = u^* + u = u+u^*$, $(u-u^*)^* = u^* - u = -(u-u^*)$, and $(uu^*)^* = u u^* = 1$.

**Corollary.** Every unitary decomposes in the affine form

$$
\boxed{\;u = \tfrac12(u + u^*) + \tfrac12(u - u^*)\;}
$$

into a self-adjoint and a skew part, which is the decomposition $A = A^+\oplus A^-$ applied to $u$. The skew part $u - u^*$ and the Cayley transform that produces unitary elements from skew ones are *The Skew Part of an Algebra*; the self-adjoint part and its Jordan product are *The Self-Adjoint Part of an Algebra*.

## The Examples

### The Trivial Involution

Let $\sigma = \mathrm{id}_A$. Then $u^* = u$, the group $\mathrm{U}(A,\mathrm{id})$ is the set of the units $u$ with $u^2 = 1$, that is the involutions of the group of units, and the skew part $A^- = \{k : k = -k\}$ is zero in characteristic not two. The example is the degenerate one, and it shows that the unitary group measures the involution and not the algebra.

### The Transpose on a Matrix Algebra

Let $A = M_n(k)$ with the transpose, $X^* = X^{\mathsf{T}}$, and $2 \neq 0$. Then $\mathrm{U}(A) = \{X \in GL_n(k) : X^{\mathsf{T}}X = 1\} = O_n(k)$ is the orthogonal group of the standard symmetric form; the skew part is the space of the alternating matrices, the self-adjoint part the space of the symmetric matrices, and the decomposition $M_n = \mathrm{Sym}\oplus \mathrm{Alt}$ is the one of *Involutive Algebras*. The form that makes $O_n(k)$ the orthogonal group, and its classification among the symmetric and the alternating forms, belong to *Hilbert Algebras*.

### The Inversion on a Group Algebra

Let $A = k[G]$ with the involution $\sigma(g) = g^{-1}$; then $(uv)^* = v^*u^*$ because the inversion reverses products, so $\sigma$ is an involution, and each group element $g$ is unitary, $g^* = g^{-1}$. The map $G \to U(k[G],\sigma)$ is injective, and the unitary group contains the image of $G$; the rest of the unitary group consists of the invertible elements $u$ with $u^*=u^{-1}$ and depends on $G$ and on $k$.

### The Exchange Involution

Let $A = B \times B^{\mathrm{opp}}$ with the exchange involution $(b, c)^* = (c, b)$, as in *Involutive Algebras*. An element $(b,c)$ is unitary exactly when $(c,b)(b,c) = 1$, that is when $cb = 1$ and $bc = 1$, so $c = b^{-1}$; hence

$$
U(B \times B^{\mathrm{opp}}) = \{(b, b^{-1}) : b \in B^\times\} \cong B^\times ,
$$

and the unitary group of the exchange involution is the group of units of $B$.

### The Conjugate Transpose

Let $A = M_n(\mathbb{C})$ with the $\varsigma$-semilinear conjugate transpose $X^* = \overline{X}^{\mathsf{T}}$. The unitary elements are the matrices with $X^*X = 1$, that is the unitary group $U_n$; the self-adjoint elements are the Hermitian matrices and the skew elements the skew-Hermitian ones. The conjugation $\varsigma$ of $\mathbb{C}$ is a semilinear involution of the scalars, the case of the second kind, and the form of the associated sesquilinear pairing belongs to *Hilbert Algebras*.

## Summary

For an involution $\sigma$ of $A$, written $u^* = \sigma(u)$, the **unitary elements** are those with $u^*u = uu^* = 1$, equivalently the units with $u^* = u^{-1}$. They form the subgroup $\mathrm{U}(A) \leq A^\times$, which is the fixed subgroup of the order-two automorphism $\theta(g) = (g^*)^{-1}$ of $A^\times$; this is the passage from the involutive algebra to the involutive group of units of *Involutive Groups*. The **self-adjoint** elements are the fixed elements $A^+ = H(A)$ and the **skew** elements the negated ones $A^- = K(A)$; every unitary decomposes as $u = \tfrac12(u+u^*) + \tfrac12(u-u^*)$ into a self-adjoint and a skew part. The examples are the orthogonal group for the transpose, the image of $G$ for the inversion of a group algebra, the group of units for the exchange involution, and the unitary group for the conjugate transpose. The involution on the elements is *Involutive Algebras*, the self-adjoint part is *The Self-Adjoint Part of an Algebra*, the skew part, its Lie algebra, the tangent space and the Cayley transform are *The Skew Part of an Algebra*, and the forms and the linear groups belong to *Hilbert Algebras* and to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars, of characteristic not two |
| $A$ | a unital associative $k$-algebra |
| $\sigma$ | an involution of $A$ |
| $u^* = \sigma(u)$ | the adjoint of an element |
| $A^+ = H(A)$ | the self-adjoint elements, $h^* = h$ |
| $A^-$ | the skew elements, $k^* = -k$ |
| $\mathrm{U}(A) = \mathrm{U}(A,\sigma)$ | the unitary elements, $u^*u = uu^* = 1$ |
| $\theta(g) = (g^*)^{-1}$ | the order-two automorphism of $A^\times$ |
| $O_n(k)$ | the orthogonal group, for the transpose |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the unitary elements and the involutions of a central simple algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the unitary and the self-adjoint elements of an algebra with involution.
