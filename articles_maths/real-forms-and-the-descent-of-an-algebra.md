# __Real Forms and the Descent of an Algebra__

## Introduction

The complexification $A_{\mathbb{C}} = A\otimes_{\mathbb{R}}\mathbb{C}$ of a real algebra $A$ carries the **conjugation** $\sigma = \mathrm{id}\otimes c$, the tensor product of the identity with the conjugation $c$ of $\mathbb{C}$; this is a semilinear involution of $A_{\mathbb{C}}$ over $\mathbb{R}$, and $A$ is recovered from it as the fixed set $A_{\mathbb{C}}^\sigma = A\otimes1$. A **real form** of a complex algebra $B$ is a real subalgebra $A$ with $A_{\mathbb{C}}\cong B$; the article shows that the real forms of $B$ correspond to the conjugations of $B$, the semilinear involutions $\sigma$ over the conjugation of $\mathbb{C}$, by $A = B^\sigma$, and that the correspondence is a descent: the structure of $B$ — its ideals, quotients, modules and representations — is carried down to $A$ and back up by the scalar extension. This is the Galois descent of *Commutative Algebras with an Involution* read for a general, possibly non-commutative, algebra, and it is the algebraic content of the phrase "the real form of a complex algebra".

The article defines the complexification and its conjugation, proves that the conjugation is a semilinear involution whose fixed set is the original real algebra, and establishes the bijection between real forms and conjugations; it then descends the structure, giving the equivalence between the complex modules with a semilinear involution and the real modules, and illustrates the descent on the matrix algebras, where the split real form $M_n(\mathbb{R})$ and the non-split real form that exists when $n$ is even are exhibited. The article is the algebra case of *Real Forms and the Descent of an Algebra* in the linear reading, and it prepares the formally real algebras of *Formally Real Algebras and the Sum of Squares*, where the conjugation is the one that makes the self-adjoint part carry its order.

The article assumes *Extension of Scalars* for $A\otimes_{\mathbb{R}}\mathbb{C}$ and the properties of the scalar extension, *Tensor Products of Algebras* for the multiplication of the extension, *Involutive Bilinear Algebras* for the semilinear involution and the two kinds, *Commutative Algebras with an Involution* for the descent in the commutative case, *Galois Theory* for the quadratic extension $\mathbb{C}/\mathbb{R}$, and *Central Simple Algebras and the Brauer Group* for the real forms of the matrix algebras. The Jordan case is *Jordan Algebras with an Involution*, and the symmetric algebra is *The Symmetric Algebra with an Involution*. Throughout, $\mathbb{R}$ and $\mathbb{C}$ are the real and complex fields, $A$ is a real unital associative algebra, $B$ is a complex unital associative algebra, $c$ is the conjugation of $\mathbb{C}$, and $\sigma$ is the semilinear involution $\mathrm{id}\otimes c$ or a general conjugation of $B$; no form, norm, length or order occurs, and the order of the self-adjoint part is deferred to Part III.

## Complexification and the Conjugation

### The Complexification

**Definition.** The **complexification** of the real algebra $A$ is the complex algebra $A_{\mathbb{C}} = A\otimes_{\mathbb{R}}\mathbb{C}$ with the product inherited from the tensor product, $(a\otimes\lambda)(b\otimes\mu) = ab\otimes\lambda\mu$; it is the scalar extension of $A$ from $\mathbb{R}$ to $\mathbb{C}$ in the sense of *Extension of Scalars*, and it contains the real subalgebra $A\otimes1\cong A$, its **real part**.

**Proposition.** $\dim_{\mathbb{C}}A_{\mathbb{C}} = \dim_{\mathbb{R}}A$, the map $a\mapsto a\otimes1$ is an $\mathbb{R}$-algebra isomorphism $A\to A\otimes1$, and $A_{\mathbb{C}} = (A\otimes1)\oplus i(A\otimes1)$ as real algebras, where $i = 1\otimes i$.

*Proof.* The tensor product of an $n$-dimensional real space with $\mathbb{C}$ is an $n$-dimensional complex space; the products are read on the decomposable elements; and $\lambda = \mathrm{Re}\,\lambda + i\,\mathrm{Im}\,\lambda$ gives the direct sum. $\square$

### The Conjugation

**Definition.** The **conjugation** of the complexification is

$$
\sigma : A_{\mathbb{C}}\to A_{\mathbb{C}}, \qquad \sigma(a\otimes\lambda) = a\otimes c(\lambda) = a\otimes\bar\lambda .
$$

It is $\mathbb{R}$-linear and satisfies $\sigma(\zeta x) = c(\zeta)\sigma(x)$ for $\zeta \in \mathbb{C}$, so it is **semilinear** over $\mathbb{R}$ with respect to $c$.

**Theorem.** $\sigma$ is a semilinear involution of the algebra $A_{\mathbb{C}}$,

$$
\sigma(xy) = \sigma(x)\sigma(y), \qquad \sigma(x+y) = \sigma(x)+\sigma(y), \qquad \sigma(\zeta x) = \bar\zeta\,\sigma(x), \qquad \sigma^2 = \mathrm{id},
$$

and its fixed set is the real part:

$$
A_{\mathbb{C}}^\sigma = A\otimes1 \cong A .
$$

*Proof.* On decomposable elements $\sigma((a\otimes\lambda)(b\otimes\mu)) = \sigma(ab\otimes\lambda\mu) = ab\otimes\bar\lambda\bar\mu = (a\otimes\bar\lambda)(b\otimes\bar\mu) = \sigma(a\otimes\lambda)\sigma(b\otimes\mu)$; additivity and the scalar rule are immediate, and $\sigma^2 = \mathrm{id}$ because $c^2 = \mathrm{id}$. An element $x = \sum a_j\otimes\lambda_j$ is fixed iff $\sum a_j\otimes(\lambda_j - \bar\lambda_j) = 0$; taking $a_j$ linearly independent forces each $\lambda_j = \bar\lambda_j$, so the fixed set is $A\otimes\mathbb{R} = A\otimes1$. $\square$

**Corollary.** The conjugation is the semilinear involution of the complexification that has $A$ as its self-adjoint part; the map $A\mapsto(A_{\mathbb{C}},\sigma)$ is a functor from the real algebras to the complex algebras with a conjugation, and the decomposition $A_{\mathbb{C}} = A\oplus iA$ is the decomposition into the self-adjoint and the skew parts.

## Real Forms

### Definition and the Correspondence

**Definition.** Let $B$ be a complex algebra. A **real form** of $B$ is a real subalgebra $A\subseteq B$ such that the multiplication map $A\otimes_{\mathbb{R}}\mathbb{C}\to B$, $a\otimes\lambda\mapsto\lambda a$, is an isomorphism of complex algebras. A **conjugation** of $B$ is a semilinear involution of $B$ over $\mathbb{R}$ with respect to $c$.

**Theorem.** The real forms of a complex algebra $B$ are in bijection with the conjugations of $B$, the bijection sending a conjugation $\sigma$ to its fixed algebra $B^\sigma = \{x : \sigma(x) = x\}$ and a real form $A$ to the conjugation of $A_{\mathbb{C}}\cong B$ constructed above. Under the bijection $A\otimes_{\mathbb{R}}\mathbb{C} = B$, the two constructions are inverse.

*Proof.* If $\sigma$ is a conjugation, then $\sigma(\lambda x) = \bar\lambda\sigma(x)$ makes $B$ a complex space on which $\sigma$ is antilinear; the fixed set $B^\sigma$ is a real subspace with $B = B^\sigma\oplus iB^\sigma$, so the multiplication $B^\sigma\otimes_{\mathbb{R}}\mathbb{C}\to B$ is a real-linear isomorphism and a complex-algebra isomorphism. Conversely a real form gives the conjugation of its complexification as above, and the fixed set recovers the real form. The two constructions are inverse by the computation of the fixed set in the theorem above. $\square$

**Proposition (uniqueness).** Two real forms $A_1, A_2$ of $B$ coincide exactly when their conjugations coincide; the set of the real forms of $B$ is thus in bijection with the set of the conjugations of $B$, and a form is **split** when its conjugation is inner.

### The Descent of the Module Category

**Theorem (descent).** Let $B$ be a complex algebra with a conjugation $\sigma$ and real form $A = B^\sigma$. The functors

$$
M \longmapsto H(M) = \{m \in M : \tau(m) = m\}, \qquad N \longmapsto N\otimes_{\mathbb{R}}\mathbb{C}
$$

are inverse equivalences between the category of complex $B$-modules with a semilinear involution $\tau$ compatible with $\sigma$ and the category of real $A$-modules.

*Proof.* This is *Commutative Algebras with an Involution* read with the centre and the scalars specialised to $\mathbb{C}/\mathbb{R}$; the quadratic model is the one with $t = i$, $t^2 = -1 \in \mathbb{R}$, under which the descent applies because $\mathbb{C}$ is faithfully flat and free of rank two over $\mathbb{R}$. The same computation $M = H(M)\oplus iH(M)$ gives the inverse. $\square$

## Descent of the Structure

### Ideals, Quotients and Products

**Proposition.** Let $I$ be an ideal of $B$ stable under the conjugation $\sigma$, so $\sigma(I) = I$. Then $I\cap A$ is an ideal of $A$, $\sigma$ descends to the quotient $B/I$, and the real form of $B/I$ is $A/(I\cap A)$ up to the canonical identification.

*Proof.* Stability gives the induced involution on the quotient by *Involutive Bilinear Algebras*; the fixed subalgebra of the quotient is the quotient of the fixed subalgebra by the fixed part of the ideal. $\square$

**Proposition.** If $A_1, A_2$ are real algebras, the complexification of $A_1\times A_2$ is the product of the complexifications, with the componentwise conjugation; for a tensor product of real algebras, $(A_1\otimes_{\mathbb{R}}A_2)_{\mathbb{C}}\cong (A_1)_{\mathbb{C}}\otimes_{\mathbb{C}}(A_2)_{\mathbb{C}}$ with the conjugation $\sigma_1\otimes\sigma_2$.

*Proof.* The tensor product is a quotient of the free product and the constructions commute with the scalar extension. $\square$

### The Descent of an Automorphism and a Derivation

**Proposition.** Let $\varphi$ be an automorphism of $B$ commuting with the conjugation $\sigma$, so $\varphi\sigma = \sigma\varphi$. Then $\varphi$ preserves the real form $A = B^\sigma$, its restriction $\varphi|_A$ is an automorphism of $A$, and $\varphi$ is the complexification of $\varphi|_A$. Let $D$ be a $\mathbb{C}$-linear derivation of $B$ with $D\sigma = \sigma D$; then $D$ preserves $A$, its restriction is an $\mathbb{R}$-linear derivation of $A$, and $D$ is the complexification of its restriction.

*Proof.* A $\sigma$-equivariant map preserves the fixed set, hence restricts to $A$; the maps $\varphi$ and $D$ are $\mathbb{C}$-linear, so they are determined by their restrictions to the real part $A$ of $B = A\oplus iA$, and the scalar extension of a $\mathbb{C}$-linear map is the map itself. The derivation property and the multiplicativity are inherited by the restriction. $\square$

## Examples

**Example (the field).** For $A = \mathbb{R}$ the complexification is $\mathbb{C}$ with the conjugation $z\mapsto\bar z$, and the real form of $\mathbb{C}$ is $\mathbb{R}$. This is the base case of the whole construction.

**Example (the matrix algebra).** For $A = M_n(\mathbb{R})$ the complexification is $M_n(\mathbb{C})$, and $M_n(\mathbb{R})$ is the real form of $M_n(\mathbb{C})$ given by the entrywise conjugation $\sigma(X) = \bar X$, whose fixed set is $M_n(\mathbb{R})$. The conjugate transpose gives a different conjugation of the algebra $M_n(\mathbb{C})$ read together with its transpose involution, and its fixed set is the real algebra of Hermitian matrices; the two maps are distinguished, and the real forms of $M_n(\mathbb{C})$ as a complex algebra are the classes of the entrywise conjugations. When $n$ is even there is also a non-split real form, the algebra of the quaternionic matrices, whose existence belongs to *Division Algebras* and to *Central Simple Algebras and the Brauer Group*.

**Example (a conjugate real form).** Let $\sigma$ be a conjugation of $B$ and let $v \in B^\times$ satisfy that $v^{-1}\sigma(v)$ is central. Then $\sigma_v(x) = v\sigma(x)v^{-1}$ is again a conjugation, and its real form is the conjugate $v\,B^\sigma\,v^{-1}$ of $B^\sigma$. The conjugations of $B$ are thus acted on by the units, and the classification of the real forms up to conjugation is the algebra reading of the first Galois cohomology of the involution, *Galois Cohomology*.

*Proof.* $\sigma_v^2(x) = v\sigma(v)\,x\,\sigma(v)^{-1}v^{-1}$, which is the identity for all $x$ exactly when $v\sigma(v)$ is central; and $\sigma_v(v\,y\,v^{-1}) = v\,\sigma(v y v^{-1})\,v^{-1} = v\sigma(v)\,\sigma(y)\,\sigma(v)^{-1}v^{-1} = v\,y\,v^{-1}$ for $y \in B^\sigma$, using the centrality of $v^{-1}\sigma(v)$ to move $v$ past $\sigma(y)$. $\square$

## Summary

The **complexification** $A_{\mathbb{C}} = A\otimes_{\mathbb{R}}\mathbb{C}$ of a real algebra $A$ carries the **conjugation** $\sigma = \mathrm{id}\otimes c$, a semilinear involution whose fixed set is the real part $A\otimes1$. A **real form** of a complex algebra $B$ is a real subalgebra with $A_{\mathbb{C}}\cong B$, and the real forms are in bijection with the **conjugations** of $B$ by $A = B^\sigma$; the bijection is realised by the fixed-set and complexification functors, which are inverse. The structure descends: stable ideals and quotients, products and tensor products, equivariant automorphisms and derivations, and the module category, where the complex modules with a compatible semilinear involution are equivalent to the real modules of the real form. The field $\mathbb{C}/\mathbb{R}$ and the matrix algebras with the entrywise conjugation and with the conjugate transpose are the worked examples, and the non-split real form of $M_n(\mathbb{C})$ belongs to *Division Algebras*. No form, norm, length or order occurs; the order of the self-adjoint part is Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Real unital algebra |
| $A_{\mathbb{C}} = A\otimes_{\mathbb{R}}\mathbb{C}$ | Complexification |
| $c$ | Conjugation of $\mathbb{C}$ |
| $\sigma = \mathrm{id}\otimes c$ | Conjugation of the complexification |
| $A_{\mathbb{C}}^\sigma = A\otimes1\cong A$ | Real part, the fixed algebra |
| $A_{\mathbb{C}} = A\oplus iA$ | Self-adjoint and skew decomposition |
| $A\subseteq B$ real form | $A\otimes_{\mathbb{R}}\mathbb{C}\cong B$ |
| $B^\sigma$ | Real form attached to a conjugation $\sigma$ |
| $M\mapsto H(M)$, $N\mapsto N\otimes_{\mathbb{R}}\mathbb{C}$ | Descent equivalence |
| $\sigma$-stable ideal $I$, $I\cap A$ | Descent of the ideals |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of the first and second kind and the descent by a quadratic extension.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the real forms, the conjugations and the self-adjoint part.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the scalar extension, the semilinear maps and the Galois descent.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the classification of the real forms by the Galois cohomology of the conjugation.
- Serge Lang, *Algebra* (Springer, revised third edition, 2002), for the matrix algebras over a field, the central simple algebras and the real forms.
