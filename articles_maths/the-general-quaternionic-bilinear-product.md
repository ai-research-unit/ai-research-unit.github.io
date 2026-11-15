# __The General Quaternionic Bilinear Product__

## Introduction

The second of the four general products conjugates the first slot by the quaternion involution and leaves the second as it stands. It is written $\tilde Q_1^{\natural}\tilde Q_2$, it is $\mathbb{C}$-bilinear like the plain product, and it is the composition of that product with ${}^{\natural}$ on the left:
$$
\tilde Q_1^{\natural}\tilde Q_2=(\tilde Q_1^{\natural})\,\tilde Q_2 .
$$
The insertion of one involution is enough to destroy associativity, flexibility and alternation, to keep a unit on one side only, to collapse the diagonal onto the centre, and to make the two defects of the halves meet in the two smallest nonzero values of the batch, one for the symmetrisation and three for the antisymmetrisation. This article reads the product on its own: the coordinate rule, the scalar–vector form, the laws, the units, the image and the diagonal, the two halves, the four composites, the trace form against the halves, and the row of the product in the comparison of the four.

The notation is that of [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html): $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with coefficient basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, $\tilde Q=Q_te_t+\vec Q$, the scalar part $\langle\tilde Q\rangle_{*}=Q_t$, the three conjugations $\overline{\phantom{x}}$, ${}^{\natural}$ and ${}^{*}={}^{\natural}\circ\overline{\phantom{x}}$, and the two pairings $(\vec Q_1,\vec Q_2)$ and $\vec Q_1\times\vec Q_2$. The algebra and its four conjugations are [The Biquaternion Algebra](the-biquaternion-algebra.html); the twelve products of the space are [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html); the forms are [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html).

The product is the quaternionic analogue of the plain one, and the two are read side by side throughout the block. The plain product of the previous article is the multiplication; this one is the multiplication with the left factor reflected, and the reflection is the whole of the difference.

## The Product and Its Coordinate Rule

**Definition.** The **general quaternionic bilinear product** is
$$
\tilde Q_1^{\natural}\tilde Q_2=\sum_{\mu}\sum_{\nu}Q_{1\mu}{}^{\natural}Q_{2\nu}\,e_\mu e_\nu ,
$$
where $Q_{1t}{}^{\natural}=Q_{1t}$ and $Q_{1k}{}^{\natural}=-Q_{1k}$ for the three vector coordinates.

**Proposition (the coordinate rule).** For all $\tilde Q_1,\tilde Q_2$,
$$
\tilde Q_1^{\natural}\tilde Q_2=\bigl(Q_{1t}Q_{2t}+Q_{1x}Q_{2x}+Q_{1y}Q_{2y}+Q_{1z}Q_{2z}\bigr)
+\bigl(Q_{1t}Q_{2x}-Q_{1x}Q_{2t}-Q_{1y}Q_{2z}+Q_{1z}Q_{2y}\bigr)\vec e_x
+\bigl(Q_{1t}Q_{2y}+Q_{1x}Q_{2z}-Q_{1y}Q_{2t}-Q_{1z}Q_{2x}\bigr)\vec e_y
+\bigl(Q_{1t}Q_{2z}-Q_{1x}Q_{2y}+Q_{1y}Q_{2x}-Q_{1z}Q_{2t}\bigr)\vec e_z .
$$

*Proof.* The plain coordinate rule with the three vector coordinates of the first factor negated. The scalar coefficient changes sign on its three vector terms and the three vector coefficients change sign on their $Q_{1k}$ terms. Verified exactly on the sixteen pairs of the basis and on general elements with coefficients in $\mathbb{Q}(i)$.

**Corollary (the rule against the plain one).** The two rules differ by the sign in front of every term that carries a vector coordinate of the first factor. There are twelve such terms: three in the scalar coefficient, three in each of the three vector coefficients.

## The Scalar–Vector Form

**Theorem (the scalar–vector form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1^{\natural}\tilde Q_2=\bigl(Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr)+Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2\;}
$$

*Proof.* Group the coordinate rule as in the plain case: the scalar row is the four products with the three vector signs now positive, that is $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$; the mixed rows give $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$; the three remaining terms are $-\vec Q_1\times\vec Q_2$. Computed exactly on general elements.

Three readings follow, and the first is the one that governs the whole article.

**Proposition (the scalar part is the quaternion norm).** The scalar part of the product is
$$
\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2\bigr)=Q_{1t}Q_{2t}+Q_{1x}Q_{2x}+Q_{1y}Q_{2y}+Q_{1z}Q_{2z}=\sum_{\mu}Q_{1\mu}Q_{2\mu},
$$
the polar form of the quadratic form $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$.

*Proof.* The first display, with the four signs positive. The form is the complexification of the norm form of the quaternion algebra, written without conjugation.

**Remark (the four signs).** The plain product carries $\varepsilon=(1,-1,-1,-1)$ on its scalar row; this product carries $(1,1,1,1)$. The two are the two classical forms of the algebra, the split form and the norm form, and the passage from one to the other is the insertion of ${}^{\natural}$ in the first slot. The form here is the one that is multiplicative, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, verified on general elements; the form of the plain product is not. The comparison is [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html).

**Remark (the three pieces).** The mixed part $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ is antisymmetric in the two factors; the cross term $-\vec Q_1\times\vec Q_2$ is antisymmetric as well. Both pieces change sign under the interchange, and the whole of the symmetric part is the scalar row. This is the opposite arrangement to the plain product, where the mixed part is symmetric and the cross term alone is not.

## The Laws It Keeps and the Laws It Loses

**Theorem (the four laws of the ladder fail).** The product is not associative, not flexible, not left alternative, not right alternative, and not power associative.

*Proof.* Four witnesses, each computed exactly.

*Not associative.* With $\tilde Q_1=\vec e_z$, $\tilde Q_2=e_t$, $\tilde Q_3=e_t$: the left side is $(\vec e_z^{\natural}e_t)e_t=\vec e_z$, and the right side is $\vec e_z^{\natural}(e_te_t)=\vec e_z^{\natural}=-\vec e_z$. The two differ by $2\vec e_z$.

*Not flexible.* With $\tilde Q_1=\vec e_z$, $\tilde Q_2=e_t$: $(\vec e_z^{\natural}e_t)^{\natural}\vec e_z=(-\vec e_z)^{\natural}\vec e_z=-e_t$ against $\vec e_z^{\natural}(e_t^{\natural}\vec e_z)=\vec e_z^{\natural}\vec e_z=e_t$.

*Not alternative.* Left, with $\tilde Q_1=\vec e_x$, $\tilde Q_2=\vec e_y$: $(\vec e_x^{\natural}\vec e_x)^{\natural}\vec e_y=e_t^{\natural}\vec e_y=\vec e_y$ against $\vec e_x^{\natural}(\vec e_x^{\natural}\vec e_y)=\vec e_x^{\natural}(-\vec e_z)=-\vec e_y$. Right, with $\tilde Q_1=\vec e_x$, $\tilde Q_2=e_t$: $(\vec e_x^{\natural}e_t)^{\natural}e_t=\vec e_x$ against $\vec e_x^{\natural}(e_t^{\natural}e_t)=-\vec e_x$.

*Not power associative.* For $\tilde Q=e_t+\vec e_x$: $\tilde Q(\tilde Q\tilde Q)=2e_t-2\vec e_x$ and $(\tilde Q\tilde Q)\tilde Q=2e_t+2\vec e_x$. The third power is not well defined.

**Remark (the reason, in one line).** The product is the plain product composed with an anti-automorphism on the left, and an anti-automorphism does not commute with the insertion of brackets: the reflection moves to the inner factor at the first rebracketing, and every one of the four failures is that movement read on a witness. The plain product keeps the whole ladder precisely because its left factor is not reflected.

**Proposition (the one identity that survives).** The involution ${}^{\natural}$ reverses the product,
$$
\bigl(\tilde Q_1^{\natural}\tilde Q_2\bigr)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1 .
$$

*Proof.* ${}^{\natural}$ is an anti-automorphism of the plain product, so $(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}(\tilde Q_1^{\natural})^{\natural}=\tilde Q_2^{\natural}\tilde Q_1$, and the right-hand side is the product with the arguments interchanged. Verified on general elements.

**Remark (what the identity says).** The involution is an anti-automorphism of the product onto its opposite product. It is the only exact identity of the product beyond bilinearity and the scalar rule, and it is the one used in the theory of the versors: a unit $\tilde R$ with $\tilde R^{\natural}\tilde R=e_t$ acts by the product as the identity on itself.

## The One-Sided Units

**Theorem (a left unit and no right unit).** The element $e_t$ is a left identity, $e_t^{\natural}\tilde Q=\tilde Q$ for every $\tilde Q$, and there is no right identity.

*Proof.* $e_t^{\natural}=e_t$ and $e_t\tilde Q=\tilde Q$ in the algebra. For the right side, $\tilde Q^{\natural}e_t=\tilde Q^{\natural}$, which equals $\tilde Q$ only for $\tilde Q\in\mathbb{B}_{C}$; the right multiplication by $e_t$ is the involution ${}^{\natural}$, whose eigenvalues $1$ and $-1$ are both present. The linear system for a right unit, sixteen equations in four unknowns, has no solution; its least-squares residual is $\tfrac32$ and the solution is not a solution.

**Corollary (the left unit is unique).** If $\tilde U^{\natural}\tilde Q=\tilde Q$ for all $\tilde Q$ then $\tilde U=e_t$.

*Proof.* Put $\tilde Q=e_t$: $\tilde U^{\natural}=e_t$, so $\tilde U=e_t$. Computed as a linear system, the solution is $(1,0,0,0)$ with zero residual.

**Remark (the three failures, named).** The right multiplication by $e_t$ is the involution and not the identity, and that single fact is the source of three of the failures above: the associator with $\tilde Q_2=\tilde Q_3=e_t$ is $\tilde Q_1-\tilde Q_1^{\natural}$, the flexing identity at $\tilde Q_2=e_t$ reads the same difference, and the right alternativity fails because the involution does not commute with itself in the wrong order. A right ideal of the product, in the sense of a subspace closed under multiplication on the right by every element, is therefore not what the algebra's right ideals are.

## The Image, the Diagonal and the Scalar Part

**Proposition (the image is the whole space).** The image of the product is $\mathbb{B}$, of complex dimension $4$.

*Proof.* $\tilde Q_1^{\natural}\tilde Q_2$ with $\tilde Q_1=e_t$ is $\tilde Q_2$, so the image contains every element. The span of the sixteen basis products is four-dimensional, computed exactly.

**Theorem (the diagonal is central).** For every $\tilde Q$,
$$
\tilde Q^{\natural}\tilde Q=N(\tilde Q)\,e_t=\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)e_t ,
$$
and the image of the diagonal is the centre $\mathbb{B}_{C}$, of complex dimension $1$.

*Proof.* The scalar–vector form at the two equal arguments: the mixed terms cancel and the cross term vanishes, leaving the scalar row. The image is one-dimensional because every value is a multiple of $e_t$, and it is exactly the centre because $N$ takes every complex value, $N(\lambda e_t)=\lambda^2$. Verified on general elements.

**Remark (what the collapse costs).** The diagonal of this product carries no vector information at all: it is a single quadratic form, and the map $\tilde Q\mapsto\tilde Q^{\natural}\tilde Q$ factors through the norm. Two consequences follow and both are used below. First, the square determines the norm and nothing else, so no power of an element can recover its vector part. Second, the zero set of the diagonal is the isotropic cone of $N$, the cone $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$, which is not trivial over $\mathbb{C}$: the element $e_t+i\vec e_x$ is isotropic and its square is zero.

**Proposition (the singular left multiplications).** The left multiplication $\tilde Q_2\mapsto\tilde Q_1^{\natural}\tilde Q_2$ is invertible for a generic $\tilde Q_1$ and singular for an isotropic one. For $\tilde Q_1=e_t+i\vec e_x$ the singular values are $2,2,0,0$.

*Proof.* The operator is the left multiplication of the algebra by $\tilde Q_1^{\natural}$, and the algebra has zero divisors: $(e_t-i\vec e_x)(e_t+i\vec e_x)=e_t+\vec e_x^2=0$. The singular values are computed from the matrix of the operator in the coefficient basis.

**The scalar part.** The scalar part of the product is the form $N$, of Gram matrix the identity and rank $4$. It is symmetric, nondegenerate, and its radical is zero. It is the only one of the four forms of the batch that is definite on the real quaternion subspace, where it is the sum of four squares.

## The Two Halves of This Product

**Definition.** The **symmetric quaternionic bilinear product** and the **antisymmetric quaternionic bilinear product** are
$$
\tilde Q_1\bullet_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1\bigr),\qquad
\tilde Q_1\wedge_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr).
$$

**Theorem (the reconstruction and the two forms).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1^{\natural}\tilde Q_2=\tilde Q_1\bullet_{\natural}\tilde Q_2+\tilde Q_1\wedge_{\natural}\tilde Q_2\;},
$$
$$
\tilde Q_1\bullet_{\natural}\tilde Q_2=\bigl(Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr)e_t,\qquad
\tilde Q_1\wedge_{\natural}\tilde Q_2=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

*Proof.* The scalar row is symmetric under the interchange of the arguments and stays in the symmetrisation; the two vector pieces are antisymmetric and stay in the antisymmetrisation. Verified on general elements.

**Corollary (the symmetrisation is central).** $\tilde Q_1\bullet_{\natural}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, with $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ the polar form of $N$. The symmetrisation is commutative, its image is the centre, and it is the rank-one product $\tilde Q_1\tilde Q_2\mapsto\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$.

**Remark (a degenerate Jordan product).** A commutative product whose image is one-dimensional is a Jordan algebra with the Jordan identity for the trivial reason that every product of three elements is a scalar times $e_t$. The identity is still not automatic: the defect of this symmetrisation is one-dimensional and the witness is $\tilde Q_1=\tilde Q_2=\vec e_x$, as [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html) records. The reason is that the product has no unit on the right, and the Jordan identity is stated with a unit.

**Remark (the antisymmetrisation).** The antisymmetrisation carries three pieces, the two mixed terms and the cross term, and it has zero diagonal. Its image is three-dimensional and it is the vector subspace, so the antisymmetrisation lands in $\mathbb{B}_{V}$ and takes the scalar coordinate of neither argument into the value except through the mixed terms. The Jacobi identity fails, with a three-dimensional defect and the witness $(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(e_t,\vec e_x,\vec e_y)$ giving $-\vec e_z$.

## The Four Composites

**Theorem (the table of the composites).** For the quaternionic bilinear family the images and the scalar parts of the four composites are

| composite | image, complex dimension | scalar part |
|---|---|---|
| $ss$ | $1$ | present |
| $sa$ | $1$ | present |
| $as$ | $3$ | zero |
| $aa$ | $3$ | zero |

*Proof.* The symmetrisation is central, so an inner $s$ forces the whole value into the centre and an outer $s$ reads a scalar part; an outer $a$ is alternating and kills the scalar part. The dimensions are the spans over all triples of the complex basis, computed exactly.

**Remark (the two rows).** The family is the extreme case of the discriminator: the inner symmetrisation collapses both rows to dimension $1$, and the scalar part separates them. Compared with the plain family, whose rows are $4,4,3,3$, the collapse is the work of the central image of the symmetrisation, and it is the only family besides the plain sesquilinear one where the collapse happens.

**Corollary (the composites land in the vector subspace).** $as$ and $aa$ take their values in $\mathbb{B}_{V}$, and the loss of the scalar part is exact.

## The Trace Form and the Halves

**Definition.** The trace form of the family is $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, the form $N$.

**Theorem (the exact split).** For all $\tilde Q_1,\tilde Q_2,\tilde Q_3,\tilde Q_4$,
$$
\mathrm{Sc}\bigl(\tilde Q_1\bullet_{\natural}\tilde Q_2\;\cdot\;\tilde Q_3\wedge_{\natural}\tilde Q_4\bigr)=0 ,
$$
and consequently
$$
\tau(\tilde Q_1,\tilde Q_2)=\tau\bigl(s(\tilde Q_1,\tilde Q_2),s(\tilde Q_1,\tilde Q_2)\bigr)+\tau\bigl(a(\tilde Q_1,\tilde Q_2),a(\tilde Q_1,\tilde Q_2)\bigr)
$$
for the two halves $s=\bullet_{\natural}$ and $a=\wedge_{\natural}$ of a single pair.

*Proof.* The symmetrisation is a multiple of $e_t$, so the product of a symmetric value with an antisymmetric one is that multiple times the antisymmetric value, whose scalar part is zero because $a$ is alternating. The consequence is the expansion of $\tau$ at the equal pairs with the cross term removed. Both statements were verified on all sixteen basis pairs and on random quadruples, with deviations at the level of the arithmetic.

**Remark (two facts, only one of them exclusive).** The four-argument vanishing is one of the two signs of the two orthogonal families of the batch; the general plain sesquilinear product has it and the other two do not. The split identity at the single pair is weaker and holds for the plain product as well, as the previous article records, so it is not by itself a discriminator. The discriminating statement is the four-argument one, and it is the one used in [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

**Remark (the form against the halves).** The form $N$ is the norm form, and the identity above says that the norm of any element of the algebra splits into the norm of the symmetric half and the norm of the antisymmetric half of its product with any second element. Since the symmetric half of a pair is the scalar product of the two and the antisymmetric half is the vector part, the statement is the four-dimensional Pythagoras of the quaternion algebra, read with the norm and not with the conjugation.

## The Place among the Four

| | this product | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
|---|---|---|---|---|
| class | $\mathbb{C}$-bilinear | $\mathbb{C}$-bilinear | sesquilinear | sesquilinear |
| associative | no | yes | no | no |
| unit | left | both | right | none |
| diagonal image | $\mathbb{B}_{C}$ | $\mathbb{B}$ | $\mathbb{B}_{\Psi}$ | $\mathbb{B}$ |
| trace form | $N$, rank $4$ | $P$, rank $4$ | $H$, rank $4$ | $K$, rank $4$ |
| $\tau(s,a)=0$ for all arguments | yes | no | yes | no |
| Jacobi defect | $3$ | $0$ | $3$ | $3$ |
| Jordan defect | $1$ | $0$ | $1$ | $4$ |

**Remark (the smallest pair of defects).** This column carries the smallest nonzero defects of the batch, three for the bracket and one for the symmetric product, and both are the defects of the same object: the failure of the right multiplication by $e_t$ to be the identity. The plain sesquilinear product has the same two numbers with the roles of the sides exchanged, and the general quaternionic sesquilinear product has the largest, three and four. The pattern is read across the two companion articles, [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html) and [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html).

## Summary

The general quaternionic bilinear product is $\tilde Q_1^{\natural}\tilde Q_2=[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)]+Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, the plain product with the left factor reflected by the quaternion involution. It is $\mathbb{C}$-bilinear and it fails associativity, flexibility, alternation and power associativity, each with a witness of two or three basis elements. The involution reverses it, $(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1$.

The element $e_t$ is a left unit and not a right one, and the left unit is unique; the right multiplication by $e_t$ is the involution itself, which is the source of the three failed laws. The image is the whole space; the diagonal is central, $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_t$, with the norm form $N$ of Gram matrix the identity; the diagonal image is the centre, and the isotropic cone of $N$ is the zero set of the diagonal. Left multiplications by isotropic elements are singular.

The symmetrisation is the rank-one central product $\tilde Q_1\bullet_{\natural}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$; the antisymmetrisation carries the three vector pieces and has zero diagonal. The four composites have images of dimensions $1,1,3,3$. The trace form $N$ is orthogonal to the halves in the four-argument sense, so the norm of a product splits exactly over its symmetric and antisymmetric parts, and the product is one of the two columns of the batch for which that exactness holds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the coefficient basis |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product |
| ${}^{\natural}$ | the quaternion involution, $e_t\mapsto e_t$, $\vec e_k\mapsto-\vec e_k$ |
| $(\vec Q_1,\vec Q_2)$, $\vec Q_1\times\vec Q_2$ | the complex bilinear dot product and cross product |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the quaternion norm, the scalar part of the product |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the polar form of $N$ |
| $\tilde Q_1\bullet_{\natural}\tilde Q_2$ | the symmetric quaternionic bilinear product, the symmetrisation |
| $\tilde Q_1\wedge_{\natural}\tilde Q_2$ | the antisymmetric quaternionic bilinear product, the antisymmetrisation |
| $s$, $a$ | the two halves of the product |
| $ss,sa,as,aa$ | the four composites of the family |
| $\mathbb{B}_{C}$, $\mathbb{B}_{V}$ | the centre and the vector subspace |

## Further Reading

- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products and the identities linking them.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the halves and the composites.
- [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html), for the vector halves and the subspaces.
- [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html) and [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html), for the two halves of this product.
- [The General Plain Bilinear Product](the-general-plain-bilinear-product.html), for the product this one reflects.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for $N$ and its three companions.
