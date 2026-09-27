
# __Real Regular Representation__

## Introduction

The real algebra $\mathbb{R}$ is one-dimensional over $\mathbb{R}$ and one-dimensional over itself. This article presents its **regular representation**, the algebra acting on itself on the left, and the $1 \times 1$ real matrix of that action in the basis $e_0 = 1$. The matrix is the Cayley matrix of real multiplication, and its image is the whole algebra of $1 \times 1$ real matrices, identified with the real scalars. The article is the base rung of the representation ladder of the tensor family: it sits below the $2 \times 2$ real representation of the complex algebra $\mathbb{C}$, the $2 \times 2$ complex representation of the quaternions $\mathbb{H}$ (equivalently the $4 \times 4$ real one), and the $4 \times 4$ complex regular representation of the biquaternions $\mathbb{B}$.

The conventions are those of *Real Algebra*: basis $e_0 = 1$, a general element $x = x e_0$, the sole involution the identity, and norm form $N(x) = x\,x = x^2$. The word *representation* is used in both senses, as in the complex and biquaternion companions: the concrete realization of the algebra by matrices, and the technical action of the algebra on a vector space. The article owns the left matrix, its multiplicativity, the identification with the real scalars, the determinant and the trace, and the relation to the complex, quaternion and biquaternion regular representations; the real-linear module classification and the representation ring are the subject of *Real Representations* and are cited once.

## The Left Regular Representation

**Definition.** The **left regular representation** of $\mathbb{R}$ is the map

$$
\rho_L : \mathbb{R} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{R}), \qquad \rho_L(x)(y) = x y .
$$

For each $x$, the map $y \mapsto xy$ is $\mathbb{R}$-linear because multiplication is bilinear, so $\rho_L(x)$ is an $\mathbb{R}$-linear endomorphism of the one-dimensional real space $\mathbb{R}$. Writing the endomorphism as a matrix in the basis $e_0$, the same symbol $\rho_L(x)$ denotes the matrix acting on the column $(y)$ of $y = y e_0$.

**Proposition (the regular matrix is the Cayley matrix).** In the basis $e_0$,

$$
\rho_L(x) = [\,x\,] .
$$

**Proof.** The single column is the image $\rho_L(x)(e_0) = x e_0 = x$, expressed in the basis $e_0$, giving the entry $x$. $\square$

The matrix has only one independent entry, the single real coordinate of $x$; it is the **Cayley matrix** of real multiplication. The identity matrix is $\rho_L(1) = [1]$, and multiplication by any element is the scalar matrix $[x]$.

**Example.** For $x = -\tfrac{3}{4}$ the Cayley matrix is $\rho_L(x) = [-\tfrac{3}{4}]$, and $\rho_L(x)(1) = -\tfrac{3}{4}$, so the column of $1$ is the element itself.

## The Left Representation Is a Homomorphism

**Theorem (multiplicativity).** For all $x, y \in \mathbb{R}$,

$$
\rho_L(x)\,\rho_L(y) = \rho_L(xy).
$$

Hence $\rho_L$ is an $\mathbb{R}$-algebra homomorphism and the space $\mathbb{R}$ is a left $\mathbb{R}$-module under it. It is **faithful**: if $\rho_L(x) = [0]$ then $x = \rho_L(x)(e_0) = 0$. It is in fact **bijective** onto the algebra of $1\times1$ real matrices, since every $1\times1$ matrix is $[x]$ for its unique entry $x$; the regular representation of the field is therefore an **isomorphism** onto its own matrix algebra, the strongest form the representation can take, and it is the statement that $\mathbb{R}$ already is the algebra of real scalars.

**Proof.** Both sides are $\mathbb{R}$-linear and are computed on the basis. Associativity gives

$$
\rho_L(x)\bigl(\rho_L(y)(e_0)\bigr) = x(y e_0) = (xy)e_0 = \rho_L(xy)(e_0),
$$

so the two matrices agree on a basis; in the $1\times1$ picture this is the identity $[x][y] = [xy]$. $\square$

**Example (a concrete check).** For $x = -\tfrac{3}{4}$ and $y = \tfrac{7}{2}$ the product is $xy = -\tfrac{21}{8}$, and

$$
\rho_L(x)\rho_L(y) = \bigl[-\tfrac{3}{4}\bigr]\bigl[\tfrac{7}{2}\bigr] = \bigl[-\tfrac{21}{8}\bigr] = \rho_L(xy),
$$

the reversed order giving the same matrix, as the algebra is commutative.

## The Right Regular Representation and Commutativity

**Definition.** The **right regular representation** of $\mathbb{R}$ is the map

$$
\rho_R : \mathbb{R} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{R}), \qquad \rho_R(x)(y) = y x .
$$

**Proposition.** $\rho_R = \rho_L$.

**Proof.** The algebra is commutative, so $yx = xy$ for all $y$, hence the two endomorphisms agree on every element. $\square$

The right regular representation therefore carries no information beyond the left one, and it is not a second realization. This is the first place where the commutative base case differs structurally from the biquaternion algebra: there the left and right regular representations are distinct, the right one is an anti-homomorphism, the naive identity $\rho_R(\tilde{Q}) = \rho_L(\tilde{Q})^{\mathsf{T}}$ is false, and the difference vanishes exactly on the centre. None of that apparatus exists here. The slot is empty because the algebra is commutative, and the emptiness is the statement. The complex algebra is the same case one dimension up, and the split-complex and dual-number algebras are commutative as well; the distinction first appears at the quaternion algebra.

## Transposition and the Involution

**Proposition.** For every real number $x$,

$$
\rho_L(x)^{\mathsf{T}} = \rho_L(x) = \rho_L(\operatorname{id} x),
$$

where the transpose is taken in the basis $e_0$.

**Proof.** A $1\times1$ matrix is its own transpose, and the sole involution is the identity. $\square$

Transposition is therefore trivial in the matrix picture; it does not change the matrix, because a $1\times1$ matrix is symmetric. In the complex case transposition swaps the two off-diagonal entries and realizes complex conjugation, $\rho_L(z)^{\mathsf{T}} = \rho_L(\bar{z})$; here there is no nontrivial involution to realize, so the transpose is the identity, and the involution of the real algebra is the identity as well. The two statements match because there is only one involution, and the only $1\times1$ permutation of a basis is trivial.

## The Determinant and the Trace

**Proposition.** For $x \in \mathbb{R}$,

$$
\det \rho_L(x) = x, \qquad \operatorname{tr}\rho_L(x) = x.
$$

**Proof.** The determinant and the trace of the $1\times1$ matrix $[x]$ are both its entry $x$. $\square$

The determinant is multiplicative, because the matrix product is,

$$
\det\bigl(\rho_L(x)\rho_L(y)\bigr) = \det\rho_L(x)\,\det\rho_L(y), \qquad \det\rho_L(xy) = \det\rho_L(x)\det\rho_L(y),
$$

so the determinant is multiplicative exactly as the norm form is. In the one-dimensional case the determinant **is** the element, and the norm form is its square:

$$
N(x) = x^2 = \bigl(\det\rho_L(x)\bigr)^2 .
$$

The determinant is the **algebra norm** of the one-dimensional algebra, the field norm of $\mathbb{R}$ over itself, and it is the signed quantity $\det\rho_L(x) = x$ whose sign is the sign of the element; the norm form of *Real Norm and Invertibility* squares it and so forgets the sign. This is the base rung of the ladder of determinants: for the complex algebra the regular matrix is $2\times2$ and its determinant is already the norm form itself, $\det\rho_L(z) = a^2+b^2 = N(z)$, with no squaring; for the quaternion algebra the $4\times4$ real regular matrix has determinant the square of the norm form; for the biquaternion algebra the $4\times4$ complex regular matrix likewise has determinant $N^2$. The real case is the one in which the determinant has degree one and the norm form degree two, and the gap is filled by the sign.

**Corollary.** $\rho_L(x)$ is invertible exactly when $x \neq 0$, since $\det\rho_L(x) = x$; this is the invertibility criterion of *Real Norm and Invertibility*, and for $x > 0$ the matrix is orientation-preserving while for $x < 0$ it reverses orientation.

## The Identification with the Real Scalars

The image of the regular representation is the algebra

$$
\rho_L(\mathbb{R}) = \{\,[x] : x \in \mathbb{R}\,\}
$$

of all $1\times1$ real matrices.

**Proposition.** The map $\rho_L$ is an isomorphism of $\mathbb{R}$ onto the real $1\times1$ matrices, and the identification of a real number with the scalar matrix $[x]$ is the identification of $\mathbb{R}$ with the real scalars of every real matrix algebra.

**Proof.** The map is an injective algebra homomorphism by multiplicativity and faithfulness, and every $1\times1$ matrix is $[x]$ for a unique $x$, so it is surjective; a bijective algebra homomorphism is an isomorphism. The scalar matrices of any real matrix algebra are the matrices $\lambda I$, and for the $1\times1$ algebra $I = [1]$ so the scalars are exactly the images $[x]$. $\square$

The image $\rho_L(\mathbb{R})$ is the field of real scalars, and its group of nonzero elements is $\mathbb{R}^\times$, the group of invertible scalars. The determinant is the element and the trace is the element, so the polar decomposition $x = |x|\operatorname{sgn}x$ is the decomposition of the scalar matrix into the positive scalar $[|x|]$ and the sign $[\operatorname{sgn}x]$, as developed in *Real Polar Representation*.

## The Module Structure: Irreducibility

The regular representation is the algebra acting on itself, and over $\mathbb{R}$ the module $\mathbb{R}$ is one-dimensional. Since $\mathbb{R}$ is a field, its only submodules are $\{0\}$ and $\mathbb{R}$ itself:

**Proposition.** The regular module is **simple** (irreducible), and the regular representation has no proper nonzero invariant subspace.

**Proof.** A submodule is an ideal of the field $\mathbb{R}$, and a field has no proper nonzero ideals. Equivalently, $\rho_L(y)$ spans the whole module for every nonzero $y$. $\square$

This is the largest structural difference from the biquaternion algebra. There the regular module is $\mathbb{B} = I_1 \oplus I_2$, the direct sum of two minimal left ideals, and the regular representation is reducible, $\rho_L \cong V \oplus V$ with $V = \mathbb{C}^2$ the simple module. Here the algebra is a field, its regular module is simple, and there is no Peirce decomposition, no idempotent splitting and no centralizer larger than the image itself. The endomorphism algebra of the regular module is $\operatorname{End}_{\mathbb{R}}(\mathbb{R}) = \mathbb{R}$, the image of $\rho_L$, which is the commutative shadow of the double-centralizer statement $\operatorname{End}_{\mathbb{B}}(\mathbb{B}) = \rho_R(\mathbb{B})$ of the biquaternion article. The complex case is the same statement, its regular module also being simple over $\mathbb{C}$.

## The Relation to the Complex, Quaternion and Biquaternion Representations

The regular representation of $\mathbb{R}$ is the base factor of a tensor product. For real algebras $A$ and $B$, left multiplication by $x \otimes y$ on $A \otimes_{\mathbb{R}} B$ is the tensor product of the left multiplications,

$$
\rho_{A \otimes B}(x \otimes y) = \rho_A(x) \otimes \rho_B(y),
$$

because $(x \otimes y)(a \otimes b) = xa \otimes yb$. Taking $A = \mathbb{C}$ and $B = \mathbb{H}$, so that $A \otimes B = \mathbb{B}$, the regular representation of the biquaternions is the tensor product of the two-dimensional real regular representation of $\mathbb{C}$ and the four-dimensional real regular representation of $\mathbb{H}$,

$$
\rho_L^{\mathbb{B}} = \rho_L^{\mathbb{C}} \otimes_{\mathbb{R}} \rho_L^{\mathbb{H}}, \qquad \dim_{\mathbb{R}} = 2 \times 4 = 8,
$$

which is the $4 \times 4$ complex regular representation of $\mathbb{B}$ read over $\mathbb{R}$. The real representation is the scalar base factor of this product: at each of the two tensor levels the coefficient factor is a copy of the real scalars, and the complex Cayley factor $\rho_L^{\mathbb{C}}$ acts on each $\mathbb{C}$-coefficient while the quaternion Cayley factor $\rho_L^{\mathbb{H}}$ acts on the index $\mu$. The two combine into the Cayley matrix of *Biquaternion 4×4 Regular Matrix Representation*.

The lower end of the same hierarchy is the $2 \times 2$ complex representation of the quaternions. Since $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong M_2(\mathbb{C})$, the quaternion regular representation, of real dimension $4$, complexifies to the $2 \times 2$ complex representation

$$
\rho^{\mathbb{H}} : \mathbb{H} \longrightarrow M_2(\mathbb{C}), \qquad q = q_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 \longmapsto \begin{pmatrix} q_0 + i q_1 & q_2 + i q_3 \\ -q_2 + i q_3 & q_0 - i q_1 \end{pmatrix},
$$

with determinant $N_{\mathbb{H}}(q) = q_0^2+q_1^2+q_2^2+q_3^2$. The four cases form the chain

| algebra | dimension over $\mathbb{R}$ | regular matrix | determinant |
|---|---|---|---|
| $\mathbb{R}$ | $1$ | $1 \times 1$ real, Cayley | $x$, the element itself |
| $\mathbb{C}$ | $2$ | $2 \times 2$ real, Cayley | $N_{\mathbb{C}}(z) = a^2+b^2$ |
| $\mathbb{H}$ | $4$ | $4 \times 4$ real, or $2 \times 2$ complex | $N_{\mathbb{H}}(q)^2$ over $\mathbb{R}$, $N_{\mathbb{H}}(q)$ over $\mathbb{C}$ |
| $\mathbb{B}$ | $8$ | $4 \times 4$ complex, Cayley, reducible | $N_{\mathbb{B}}(\tilde{Q})^2$ |

The real case is the bottom of the chain in two senses: its regular representation is the smallest Cayley matrix, and its module is simple, whereas the quaternion and biquaternion regular modules are sums of copies of a smaller simple module once the algebra is complexified. The determinant column is the ladder of the squarings: the real determinant is the element, the complex determinant is the norm form, and from the quaternion and biquaternion cases onward the determinant acquires a further square because the regular module splits into two copies of the simple module.

## Worked Examples

**The Cayley matrix on the worked pair.** With $x = -\tfrac{3}{4}$ and $y = \tfrac{7}{2}$ the regular matrix is the $1\times1$ matrix of the element,

$$
\rho_L(x) = \bigl[-\tfrac{3}{4}\bigr], \qquad \rho_L(y) = \bigl[\tfrac{7}{2}\bigr],
$$

with determinant and trace

$$
\det\rho_L(x) = -\tfrac{3}{4}, \qquad \operatorname{tr}\rho_L(x) = -\tfrac{3}{4}, \qquad \det\rho_L(y) = \tfrac{7}{2}, \qquad \operatorname{tr}\rho_L(y) = \tfrac{7}{2}.
$$

**Multiplicativity.** The $1\times1$ matrices multiply as the numbers do:

$$
\rho_L(x)\,\rho_L(y) = \bigl[-\tfrac{3}{4}\bigr]\bigl[\tfrac{7}{2}\bigr] = \bigl[-\tfrac{21}{8}\bigr] = \rho_L(xy),
$$

so $\rho_L$ is a faithful algebra homomorphism, indeed an isomorphism onto the whole of the real $1\times1$ matrices.

**The determinant and the norm form.** The determinant of the Cayley matrix is the element itself, $\det\rho_L(a) = a$, and the norm form is its square,

$$
N(a) = a^2 = \bigl(\det\rho_L(a)\bigr)^2 .
$$

On the worked elements, $\det\rho_L(x)^2 = \bigl(-\tfrac{3}{4}\bigr)^2 = \tfrac{9}{16} = N(x)$ and $\det\rho_L(y)^2 = \tfrac{49}{4} = N(y)$. The determinant is invertible exactly when the element is, which is the concrete form of the invertibility criterion.

**The determinant of an exponential.** The classical identity $\det(e^{M}) = e^{\operatorname{tr}(M)}$ read for the $1\times1$ matrix $M = [a]$ gives

$$
\det\rho_L(e^{a}) = \det\bigl[e^{a}\bigr] = e^{\operatorname{tr}[a]} = e^{a},
$$

whose square is the norm form of the exponential, $N(e^{a}) = e^{2a}$.

## Summary

The left regular representation of $\mathbb{R}$, defined by $\rho_L(x)(y) = xy$, is the algebra acting on itself on the left, and in the basis $e_0$ its matrix is the Cayley matrix

$$
\rho_L(x) = [\,x\,] .
$$

It is a faithful, indeed bijective, $\mathbb{R}$-algebra homomorphism, $\rho_L(x)\rho_L(y) = \rho_L(xy)$; its transpose is itself and realizes the identity involution; its determinant is $x$ and its trace is $x$. The image is the field of real scalars, the $1\times1$ real matrices, and the polar decomposition of $x$ is the decomposition of its scalar matrix into a positive scalar and a sign.

Because the algebra is commutative, the right regular representation coincides with the left and the left-right apparatus of the biquaternion case is empty. Because the algebra is a field, the regular module is simple: the biquaternion reduction $\rho_L \cong V \oplus V$ into two minimal left ideals, the determinant $N^2$, and the nontrivial centralizer all have no analogue here, and their absence is the commutativity and the divisibility of $\mathbb{R}$. The determinant of the Cayley matrix is the element, whose square is the norm form; this is the first rung of the determinant ladder whose other members are the norm form of $\mathbb{C}$ and the squared norm forms of $\mathbb{H}$ and $\mathbb{B}$. The real regular representation is the scalar base factor of the tensor product $\rho_L^{\mathbb{B}} = \rho_L^{\mathbb{C}} \otimes_{\mathbb{R}} \rho_L^{\mathbb{H}}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, basis $e_0 = 1$; the one-dimensional space |
| $\rho_L(x)(y) = xy$ | the left regular representation |
| $\rho_R(x)(y) = yx$ | the right regular representation, equal to $\rho_L$ |
| $\rho_L(x) = [x]$ | the $1\times1$ Cayley matrix of multiplication by $x$ |
| $\operatorname{id}$ | the identity involution; $\rho_L(x)^{\mathsf{T}} = \rho_L(\operatorname{id}x)$ |
| $\det\rho_L(x) = x$ | the determinant, the algebra norm whose square is the norm form |
| $\operatorname{tr}\rho_L(x) = x$ | the trace |
| $N(x) = x^2 = (\det\rho_L(x))^2$ | the norm form |
| $\rho_L(\mathbb{R}) = \{[x]\}$ | the image, the real scalars |
| $\rho_L^{\mathbb{C}}, \rho_L^{\mathbb{H}}, \rho_L^{\mathbb{B}}$ | the regular representations of the higher members of the ladder |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation, the Cayley matrix and the determinant as an algebra norm.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for the regular representation of a field and the simplicity of its module.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the identification of an algebra with its scalar matrices and the tensor product of representations.
- John B. Fraleigh, *A First Course in Abstract Algebra*, 7th edition (Addison–Wesley, 2003), for the field of $1\times1$ real matrices and the group of scalars.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the regular representations of the division algebras and their determinants.
- T. Y. Lam, *A First Course in Noncommutative Rings*, 2nd edition (Springer, 2001), for the structure of the regular module and its endomorphism algebra.
