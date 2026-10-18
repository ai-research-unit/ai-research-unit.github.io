
# __Real Regular Element Representation__

## Introduction

The real algebra $\mathbb{R}$ is one-dimensional over $\mathbb{R}$ and one-dimensional over itself. This article presents its **regular representation**, the algebra acting on itself on the left, and the $1 \times 1$ real matrix of that action in the basis $1$. The matrix is the Cayley matrix of real multiplication, and its image is the whole algebra of $1 \times 1$ real matrices, identified with the real scalars. The article is the base rung of the representation ladder of the tensor family: it sits below the $2 \times 2$ real representation of the complex algebra $\mathbb{C}$.

The conventions are those of *Real Algebra*: basis $1$, a general element $q = q\cdot 1$, the sole involution the identity, and norm $N(q) = q\,q = q^2$. The word *representation* is used in both senses, as in the complex companion: the concrete realization of the algebra by matrices, and the technical action of the algebra on a vector space. The article owns the left matrix, its multiplicativity, the identification with the real scalars, the determinant and the trace, and the relation to the complex regular representation; the real-linear module classification and the representation ring are the subject of *Real Element Representations* and are cited once.

## The Left Regular Representation

**Definition.** The **left regular representation** of $\mathbb{R}$ is the map

$$
L : \mathbb{R} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{R}), \qquad L_{q}(b) = q b .
$$

For each $q$, the map $b \mapsto qb$ is $\mathbb{R}$-linear because multiplication is bilinear, so $L_{q}$ is an $\mathbb{R}$-linear endomorphism of the one-dimensional real space $\mathbb{R}$. Writing the endomorphism as a matrix in the basis $1$, the same symbol $\mathsf{M}_1(q)$ denotes the matrix acting on the column $(b)$ of $b = b e_t$.

**Proposition (the regular matrix is the Cayley matrix).** In the basis $1$,

$$
\mathsf{M}_1(q) = [\,q\,] .
$$

**Proof.** The single column is the image $L_{q}(1) = q\cdot 1 = q$, expressed in the basis $1$, giving the entry $q$.

The matrix has only one independent entry, the single real coordinate of $q$; it is the **Cayley matrix** of real multiplication, written interchangeably $\mathsf{M}_1(q) = [q] = M_q$. The identity matrix is $\mathsf{M}_1(1) = [1]$, and multiplication by any element is the scalar matrix $[q]$.

**Example.** For $q = -\tfrac{3}{4}$ the Cayley matrix is $\mathsf{M}_1(q) = [-\tfrac{3}{4}]$, and $L_{q}(1) = -\tfrac{3}{4}$, so the column of $1$ is the element itself.

## The Left Representation Is a Homomorphism

**Theorem (multiplicativity).** For all $q_1, q_2 \in \mathbb{R}$,

$$
\mathsf{M}_1(q_1)\,\mathsf{M}_1(q_2) = \mathsf{M}_1(q_1 q_2).
$$

Hence $\mathsf{M}_1$ is an $\mathbb{R}$-algebra homomorphism and the space $\mathbb{R}$ is a left $\mathbb{R}$-module under it. It is **faithful**: if $\mathsf{M}_1(q) = [0]$ then $q = L_{q}(1) = 0$. It is in fact **bijective** onto the algebra of $1\times1$ real matrices, since every $1\times1$ matrix is $[q]$ for its unique entry $q$; the regular representation of the field is therefore an **isomorphism** onto its own matrix algebra, the strongest form the representation can take, and it is the statement that $\mathbb{R}$ already is the algebra of real scalars.

**Proof.** Both sides are $\mathbb{R}$-linear and are computed on the basis. Associativity gives

$$
L_{q_1}\bigl(L_{q_2}(1)\bigr) = q_1(q_2 1) = (q_1 q_2)1 = L_{q_1 q_2}(1),
$$

so the two matrices agree on a basis; in the $1\times1$ picture this is the identity $[q_1][q_2] = [q_1 q_2]$.

**Example (a concrete check).** For $q_1 = -\tfrac{3}{4}$ and $q_2 = \tfrac{7}{2}$ the product is $q_1 q_2 = -\tfrac{21}{8}$, and

$$
\mathsf{M}_1(q_1)\mathsf{M}_1(q_2) = \bigl[-\tfrac{3}{4}\bigr]\bigl[\tfrac{7}{2}\bigr] = \bigl[-\tfrac{21}{8}\bigr] = \mathsf{M}_1(q_1 q_2),
$$

the reversed order giving the same matrix, as the algebra is commutative.

## The Right Regular Representation and Commutativity

**Definition.** The **right regular representation** of $\mathbb{R}$ is the map

$$
R : \mathbb{R} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{R}), \qquad R_{q}(b) = b q .
$$

**Proposition.** $\mathsf{M}_1^{R} = \mathsf{M}_1$.

**Proof.** The algebra is commutative, so $b q = q b$ for all $b$, hence the two endomorphisms agree on every element.

The right regular representation therefore carries no information beyond the left one, and it is not a second realization. The slot is empty because the algebra is commutative, and the emptiness is the statement. The complex algebra is the same case one dimension up, and the split-complex and dual-number algebras are commutative as well.

## Transposition and the Involution

**Proposition.** For every real number $q$,

$$
\mathsf{M}_1(q)^{\mathsf{T}} = \mathsf{M}_1(q) = \mathsf{M}_1(\operatorname{id} q),
$$

where the transpose is taken in the basis $1$.

**Proof.** A $1\times1$ matrix is its own transpose, and the sole involution is the identity.

Transposition is therefore trivial in the matrix picture; it does not change the matrix, because a $1\times1$ matrix is symmetric. In the complex case transposition swaps the two off-diagonal entries and realizes complex conjugation, $\mathsf{M}_1(A)^{\mathsf{T}} = \mathsf{M}_1(\bar A)$; here there is no nontrivial involution to realize, so the transpose is the identity, and the involution of the real algebra is the identity as well. The two statements match because there is only one involution, and the only $1\times1$ permutation of a basis is trivial.

## The Determinant and the Trace

**Proposition.** For $q \in \mathbb{R}$,

$$
\det \mathsf{M}_1(q) = q, \qquad \operatorname{tr}\mathsf{M}_1(q) = q.
$$

**Proof.** The determinant and the trace of the $1\times1$ matrix $[q]$ are both its entry $q$.

The determinant is multiplicative, because the matrix product is,

$$
\det\bigl(\mathsf{M}_1(q_1)\mathsf{M}_1(q_2)\bigr) = \det\mathsf{M}_1(q_1)\,\det\mathsf{M}_1(q_2), \qquad \det\mathsf{M}_1(q_1 q_2) = \det\mathsf{M}_1(q_1)\det\mathsf{M}_1(q_2),
$$

so the determinant is multiplicative exactly as the norm is. In the one-dimensional case the determinant **is** the element, and the norm is its square:

$$
N(q) = q^2 = \bigl(\det\mathsf{M}_1(q)\bigr)^2 .
$$

The determinant is the **algebra norm** of the one-dimensional algebra, the field norm of $\mathbb{R}$ over itself, and it is the signed quantity $\det\mathsf{M}_1(q) = q$ whose sign is the sign of the element; the norm of *Real Norm and Invertibility* squares it and so forgets the sign. This is the base rung of the ladder of determinants: for the complex algebra the regular matrix is $2\times2$ and its determinant is already the norm itself, $\det\mathsf{M}_1(A) = u^2+v^2 = N(A)$, with no squaring. The real case is the one in which the determinant has degree one and the norm degree two, and the gap is filled by the sign.

**Corollary.** $\mathsf{M}_1(q)$ is invertible exactly when $q \neq 0$, since $\det\mathsf{M}_1(q) = q$; this is the invertibility criterion of *Real Norm and Invertibility*, and for $q > 0$ the matrix is orientation-preserving while for $q < 0$ it reverses orientation.

## The Identification with the Real Scalars

The image of the regular representation is the algebra

$$
\mathsf{M}_1(\mathbb{R}) = \{\,[q] : q \in \mathbb{R}\,\}
$$

of all $1\times1$ real matrices.

**Proposition.** The map $\mathsf{M}_1$ is an isomorphism of $\mathbb{R}$ onto the real $1\times1$ matrices, and the identification of a real number with the scalar matrix $[q]$ is the identification of $\mathbb{R}$ with the real scalars of every real matrix algebra.

**Proof.** The map is an injective algebra homomorphism by multiplicativity and faithfulness, and every $1\times1$ matrix is $[q]$ for a unique $q$, so it is surjective; a bijective algebra homomorphism is an isomorphism. The scalar matrices of any real matrix algebra are the matrices $\lambda I$, and for the $1\times1$ algebra $I = [1]$ so the scalars are exactly the images $[q]$.

The image $\mathsf{M}_1(\mathbb{R})$ is the field of real scalars, and its group of nonzero elements is $\mathbb{R}^\times$, the group of invertible scalars. The determinant is the element and the trace is the element, so the polar decomposition $q = |q|\operatorname{sgn}q$ is the decomposition of the scalar matrix into the positive scalar $[|q|]$ and the sign $[\operatorname{sgn}q]$, as developed in *Real Polar Element Representation*.

## The Module Structure: Irreducibility

The regular representation is the algebra acting on itself, and over $\mathbb{R}$ the module $\mathbb{R}$ is one-dimensional. Since $\mathbb{R}$ is a field, its only submodules are $\{0\}$ and $\mathbb{R}$ itself:

**Proposition.** The regular module is **simple** (irreducible), and the regular representation has no proper nonzero invariant subspace.

**Proof.** A submodule is an ideal of the field $\mathbb{R}$, and a field has no proper nonzero ideals. Equivalently, $\mathsf{M}_1(q)$ spans the whole module for every nonzero $q$.

The algebra is a field, so its regular module is simple, and there is no Peirce decomposition, no idempotent splitting and no centralizer larger than the image itself. The endomorphism algebra of the regular module is $\operatorname{End}_{\mathbb{R}}(\mathbb{R}) = \mathbb{R}$, the image of $\mathsf{M}_1$. The complex case is the same statement, its regular module also being simple over $\mathbb{C}$.

## The Relation to the Complex Representation

The regular representation of $\mathbb{R}$ is the base factor of a tensor product. For real algebras $A$ and $B$, left multiplication by $a \otimes b$ on $A \otimes_{\mathbb{R}} B$ is the tensor product of the left multiplications,

$$
\rho_{A \otimes B}(a \otimes b) = \rho_A(a) \otimes \rho_B(b),
$$

because $(a \otimes b)(u \otimes v) = au \otimes bv$. The real representation is the scalar base factor of such a product: at each tensor level the coefficient factor is a copy of the real scalars, and the same construction with any higher member of the family produces the tensor product of the regular representation of that member with the complex one. The one higher case computed here is the complex algebra, whose $2 \times 2$ real Cayley matrix $\mathsf{M}_2^{\mathbb{C}}$ is the first regular matrix that is not a scalar.

The two cases form the chain

| algebra | dimension over $\mathbb{R}$ | regular matrix | determinant |
|---|---|---|---|
| $\mathbb{R}$ | $1$ | $1 \times 1$ real, Cayley | $q$, the element itself |
| $\mathbb{C}$ | $2$ | $2 \times 2$ real, Cayley | $N_{\mathbb{C}}(A) = u^2+v^2$ |

The real case is the bottom of the chain: its regular representation is the smallest Cayley matrix, and its module is simple. The determinant column is the ladder of the squarings: the real determinant is the element, and the complex determinant is the norm.

## Worked Examples

**The Cayley matrix on the worked pair.** With $q_1 = -\tfrac{3}{4}$ and $q_2 = \tfrac{7}{2}$ the regular matrix is the $1\times1$ matrix of the element,

$$
\mathsf{M}_1(q_1) = \bigl[-\tfrac{3}{4}\bigr], \qquad \mathsf{M}_1(q_2) = \bigl[\tfrac{7}{2}\bigr],
$$

with determinant and trace

$$
\det\mathsf{M}_1(q_1) = -\tfrac{3}{4}, \qquad \operatorname{tr}\mathsf{M}_1(q_1) = -\tfrac{3}{4}, \qquad \det\mathsf{M}_1(q_2) = \tfrac{7}{2}, \qquad \operatorname{tr}\mathsf{M}_1(q_2) = \tfrac{7}{2}.
$$

**Multiplicativity.** The $1\times1$ matrices multiply as the numbers do:

$$
\mathsf{M}_1(q_1)\,\mathsf{M}_1(q_2) = \bigl[-\tfrac{3}{4}\bigr]\bigl[\tfrac{7}{2}\bigr] = \bigl[-\tfrac{21}{8}\bigr] = \mathsf{M}_1(q_1 q_2),
$$

so $\mathsf{M}_1$ is a faithful algebra homomorphism, indeed an isomorphism onto the whole of the real $1\times1$ matrices.

**The determinant and the norm.** The determinant of the Cayley matrix is the element itself, $\det\mathsf{M}_1(q) = q$, and the norm is its square,

$$
N(q) = q^2 = \bigl(\det\mathsf{M}_1(q)\bigr)^2 .
$$

On the worked elements, $\det\mathsf{M}_1(q_1)^2 = \bigl(-\tfrac{3}{4}\bigr)^2 = \tfrac{9}{16} = N(q_1)$ and $\det\mathsf{M}_1(q_2)^2 = \tfrac{49}{4} = N(q_2)$. The determinant is invertible exactly when the element is, which is the concrete form of the invertibility criterion.

**The determinant of an exponential.** The classical identity $\det(\exp(M)) = \exp(\operatorname{tr}(M))$ read for the $1\times1$ matrix $M = [a]$ gives

$$
\det\mathsf{M}_1(\exp(a)) = \det\bigl[\exp(a)\bigr] = \exp(\operatorname{tr}[a]) = \exp(a),
$$

whose square is the norm of the exponential, $N(\exp(a)) = \exp(2a)$.

## Summary

The left regular representation of $\mathbb{R}$, defined by $L_{q}(b) = q b$, is the algebra acting on itself on the left, and in the basis $1$ its matrix is the Cayley matrix

$$
\mathsf{M}_1(q) = [\,q\,] .
$$

It is a faithful, indeed bijective, $\mathbb{R}$-algebra homomorphism, $\mathsf{M}_1(q_1)\mathsf{M}_1(q_2) = \mathsf{M}_1(q_1 q_2)$; its transpose is itself and realizes the identity involution; its determinant is $q$ and its trace is $q$. The image is the field of real scalars, the $1\times1$ real matrices, and the polar decomposition of $q$ is the decomposition of its scalar matrix into a positive scalar and a sign.

Because the algebra is commutative, the right regular representation coincides with the left and the left-right apparatus is empty. Because the algebra is a field, the regular module is simple: there is no splitting into minimal left ideals, no determinant $N^2$, and no nontrivial centralizer, and their absence is the commutativity and the divisibility of $\mathbb{R}$. The determinant of the Cayley matrix is the element, whose square is the norm; this is the first rung of the determinant ladder whose next member is the norm of $\mathbb{C}$. The real regular representation is the scalar base factor of the tensor product of the regular representations of the family.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, basis $1$; the one-dimensional space |
| $L_{q}(b) = qb$ | the left regular representation |
| $R_{q}(b) = bq$ | the right regular representation, equal to $\mathsf{M}_1$ |
| $\mathsf{M}_1(q) = [q] = M_q$ | the $1\times1$ Cayley matrix of multiplication by $q$ |
| $\operatorname{id}$ | the identity involution; $\mathsf{M}_1(q)^{\mathsf{T}} = \mathsf{M}_1(\operatorname{id}q)$ |
| $\det\mathsf{M}_1(q) = q$ | the determinant, the algebra norm whose square is the norm |
| $\operatorname{tr}\mathsf{M}_1(q) = q$ | the trace |
| $N(q) = q^2 = (\det\mathsf{M}_1(q))^2$ | the norm |
| $\mathsf{M}_1(\mathbb{R}) = \{[q]\}$ | the image, the real scalars |
| $\mathsf{M}_2^{\mathbb{C}}$ | the regular representation of the complex algebra |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation, the Cayley matrix and the determinant as an algebra norm.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for the regular representation of a field and the simplicity of its module.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the identification of an algebra with its scalar matrices and the tensor product of representations.
- John B. Fraleigh, *A First Course in Abstract Algebra*, 7th edition (Addison–Wesley, 2003), for the field of $1\times1$ real matrices and the group of scalars.
- T. Y. Lam, *A First Course in Noncommutative Rings*, 2nd edition (Springer, 2001), for the structure of the regular module and its endomorphism algebra.
