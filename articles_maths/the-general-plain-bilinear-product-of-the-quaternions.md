# __The General Plain Bilinear Product of the Quaternions__

## Introduction

Over $\mathbb{R}$ the space of the quaternions carries exactly two general bilinear products, and this article reads the first of them alone, the plain product $\tilde q_1\tilde q_2$. *General* is a term of the batch: a general product is a bilinear map whose two slots are read through the identity or through the conjugation; the two slots read the same involution over $\mathbb{R}$, so exactly two products arise, this one of the pairing $(\mathrm{id},\mathrm{id})$ and the quaternionic one of the pairing $({}^{\natural},\mathrm{id})$.

The biquaternion counterpart is [The General Plain Bilinear Product](the-general-plain-bilinear-product.html), and the two articles are one computation read over $\mathbb{R}$ and over $\mathbb{C}$. What changes is worth naming at once: over $\mathbb{C}$ the plain product has zero divisors and its trace form has signature $(2,2)$; over $\mathbb{R}$ the product is a division product, there are no zero divisors, and the trace form has signature $(1,3)$.

The article reads the product as a product of the batch and not as an introduction to the algebra. The algebra that the product makes of the space — its unit, its inverse, its centre, its automorphisms — is [Introduction to the Quaternion Algebra](introduction-to-the-quaternion-algebra.html) and [The Specificities of the Quaternion Algebra](the-specificities-of-the-quaternion-algebra.html), cited and not restated. The two halves are [The Jordan Structure of the Symmetric Plain Product of the Quaternions](the-jordan-structure-of-the-symmetric-plain-product-of-the-quaternions.html) and [The Lie Structure of the Antisymmetric Plain Product of the Quaternions](the-lie-structure-of-the-antisymmetric-plain-product-of-the-quaternions.html).

## The Product and Its Coordinate Rule

**Definition.** The **general plain bilinear product** of two quaternions $\tilde q_1=q_{1t}e_t+\vec q_1$ and $\tilde q_2=q_{2t}e_t+\vec q_2$ is their product in the algebra, written by juxtaposition,
$$
\tilde q_1\tilde q_2=q_{1t}q_{2t}e_t+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\vec q_2 .
$$

**Theorem (the coordinate rule).** For all $\tilde q_1,\tilde q_2$,
$$
\boxed{\;\tilde q_1\tilde q_2=\bigl(q_{1t}q_{2t}-(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2\;}
$$

*Proof.* On the basis the rules $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z=-\vec e_y\vec e_x$ give $\vec q_1\vec q_2=-(\vec q_1,\vec q_2)+\vec q_1\times\vec q_2$; the four remaining terms are the two scalar products and the two mixed terms. The identity was checked on the sixteen pairs of the basis and on general elements, with a deviation at the level of the arithmetic.

**Corollary (the nine coordinates).** With $\tilde q=(a,x,y,z)$,
$$
(\tilde q_1\tilde q_2)_t=a_1a_2-x_1x_2-y_1y_2-z_1z_2,\qquad
(\tilde q_1\tilde q_2)_x=a_1x_2+x_1a_2+y_1z_2-z_1y_2 ,
$$
and the two remaining coordinates are obtained by the cyclic permutation of $(x,y,z)$.

*Proof.* Read the display of the theorem in coordinates and expand the cross product.

**Remark (the shape of the rule).** The rule is the rule of the plain product of the biquaternions with the four coefficients read as real numbers, and it is the reason the quaternion algebra is the real form of the biquaternion algebra cut by the reality condition on the coefficients. Nothing in the writing of the product uses the complex structure; everything in it uses the three-dimensional cross product of the vector part.

## The Class of the Product

**Proposition (bilinearity).** The product is $\mathbb{R}$-bilinear in each slot, and it is linear in neither slot over $\mathbb{C}$ when the space is read over $\mathbb{C}$ by a complex structure of the left multiplications.

*Proof.* Bilinearity over $\mathbb{R}$ is the distributivity and the homogeneity of the algebra, verified on the basis. For the second statement, $(\lambda\tilde q_1)\tilde q_2=\lambda(\tilde q_1\tilde q_2)$ holds for every real $\lambda$ and fails for a general complex $\lambda$ of the complex structure $L_\nu$, since $L_\nu$ is a derivation of the product and not a scalar multiplication commuting with it.

**Proposition (the product is not symmetric, and the asymmetry is the cross term).** For all $\tilde q_1,\tilde q_2$,
$$
\tilde q_1\tilde q_2-\tilde q_2\tilde q_1=2\,\vec q_1\times\vec q_2 ,
$$
a pure quaternion, which vanishes exactly when the vector parts are parallel.

*Proof.* The scalar row and the mixed terms are symmetric in the two arguments and cancel in the difference; the cross term changes sign and doubles. Verified on the basis and on general elements.

**Remark (the two slots are not interchangeable, and nothing else distinguishes them).** The product has no symmetry and no antisymmetry, and the whole of its asymmetry sits in one term. It is this fact that makes the product readable as the sum of two canonical halves, and it is also the reason the batch has no third product of the pairing $(\mathrm{id},{}^{\natural})$ distinct from the second: the transposed pairing is the conjugate of the product, not a new product.

## The Laws It Keeps and the Laws It Loses

**Theorem (associativity).** For all $\tilde q_1,\tilde q_2,\tilde q_3$,
$$
(\tilde q_1\tilde q_2)\tilde q_3=\tilde q_1(\tilde q_2\tilde q_3).
$$

*Proof.* The left regular representation is multiplicative, $L_{\tilde q_1\tilde q_2}=L_{\tilde q_1}L_{\tilde q_2}$, because the product is the product of the algebra; the identity therefore reduces to the associativity of the composition of linear maps. The finite verification on the $64$ triples of the basis is exact. The algebra is associative by construction, and this is the one law of the four that the quaternionic product of the batch does not keep.

**Proposition (the unit).** The element $e_t$ is a two-sided unit; it is the only one; and the centre of the algebra is the line $\mathbb{R}e_t$.

*Proof.* $e_t\tilde q=\tilde q e_t=\tilde q$ is the definition of the scalar part. A unit $\tilde u$ satisfies $\tilde u\tilde q=\tilde q$ at $\tilde q=e_t$, hence $\tilde u=e_t$. An element is central iff its vector part is parallel to every vector, hence iff it is real. The centre is computed in [The Specificities of the Quaternion Algebra](the-specificities-of-the-quaternion-algebra.html) and the computation is not repeated here.

**Theorem (the division property).** Every nonzero element is invertible, with
$$
\tilde q^{-1}=\frac{\tilde q^{\natural}}{N(\tilde q)},\qquad N(\tilde q)=\tilde q\tilde q^{\natural}=q_t^2+\lvert\vec q\rvert^2 ,
$$
and there are no zero divisors: $\tilde q_1\tilde q_2=0$ implies $\tilde q_1=0$ or $\tilde q_2=0$.

*Proof.* $N$ is multiplicative, $N(\tilde q_1\tilde q_2)=N(\tilde q_1)N(\tilde q_2)$, and it is positive definite, so a product of nonzero elements has nonzero norm. The formula for the inverse is checked by multiplying on both sides. The invertibility theory is [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html).

**Remark (the four laws, sorted).** Of the four laws of an algebra of the batch — associativity, a two-sided unit, commutativity, no zero divisors — the plain product keeps three and loses commutativity. The quaternionic product keeps one, the left unit, and loses the other three. The sorting is the content of the comparison table of the last section, and it is the whole reason the plain product is the one that carries the name of the algebra.

## The Image, the Diagonal and the Scalar Part

**Proposition (the image is everything).** The product is surjective onto $\mathbb{H}$: every element is a product of two elements, and every element is even a square.

*Proof.* For a target $\tilde t=s+\vec w$ put $\tau=2s+2\sqrt{s^2+\lvert\vec w\rvert^2}$, which is positive unless $\tilde t$ is a negative real, and $\tilde q=\tfrac12\sqrt{\tau}+\vec w/\sqrt{\tau}$; then $\tilde q^2=\tilde t$. For a negative real the square root is a pure vector of the right length. Verified on random targets, with the residual at the level of the arithmetic.

**Proposition (the diagonal).** For every $\tilde q$,
$$
\tilde q^2=\bigl(q_t^2-\lvert\vec q\rvert^2\bigr)+2q_t\vec q ,
$$
and the square is scalar exactly when $\tilde q$ is real or pure.

*Proof.* Put $\tilde q_1=\tilde q_2=\tilde q$ in the coordinate rule; the cross product of a vector with itself vanishes. The scalar part of the square is $P(\tilde q)=q_t^2-\lvert\vec q\rvert^2$, the plain algebraic norm of the space, positive on the real axis, negative on the pure vectors, and zero on the cone $q_t^2=\lvert\vec q\rvert^2$.

**Remark (the two invariants of the diagonal).** The diagonal carries two functions of the element and not one: the scalar part of the square, $P$, which is indefinite, and the norm $N=\tilde q\tilde q^{\natural}$, which is definite and multiplicative. The first is the trace form read on the diagonal and the second is the same trace form composed with the conjugation. Both are needed, and the articles of the P norm read the first as the source of a partition of the algebra.

**Proposition (the idempotents and the nilpotents).** The idempotents of the product are $0$ and $e_t$; the nilpotents are $0$; and no nonzero element squares to $-e_t$ times a positive number except the pure vectors of the right length.

*Proof.* $\tilde q^2=\tilde q$ reads $q_t^2-\lvert\vec q\rvert^2=q_t$ and $2q_t\vec q=\vec q$; the second equation gives $q_t=\tfrac12$ or $\vec q=0$, and the first then forces $\tilde q=e_t$ in the first case and $q_t\in\{0,1\}$ in the second. $\tilde q^2=0$ gives $q_t=0$ and $\vec q=0$. The last statement is $\vec q^2=-\lvert\vec q\rvert^2$.

## The Two Halves of This Product

**Theorem (the reconstruction).** For all $\tilde q_1,\tilde q_2$,
$$
\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2 ,
$$
with
$$
\tilde q_1\bullet\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1\bigr)=\bigl(q_{1t}q_{2t}-(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2+q_{2t}\vec q_1
$$
and
$$
\tilde q_1\wedge\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1\bigr)=\vec q_1\times\vec q_2 .
$$

*Proof.* Add and subtract the two orders; the symmetric part keeps the scalar row and the mixed terms, and the antisymmetric part keeps the cross term. Verified exactly on the basis and on general elements.

**Remark (the split is forced).** The two halves are the symmetric and the antisymmetric part of the bilinear map under the interchange of the slots, and a bilinear map over a field of characteristic different from two has exactly one such split. There is therefore no choice in the decomposition, no second way of writing the product as a sum of a commutative and an anticommutative piece, and no free parameter in it. The two halves are studied in [The Jordan Structure of the Symmetric Plain Product of the Quaternions](the-jordan-structure-of-the-symmetric-plain-product-of-the-quaternions.html) and [The Lie Structure of the Antisymmetric Plain Product of the Quaternions](the-lie-structure-of-the-antisymmetric-plain-product-of-the-quaternions.html), and the general theory of the split is [The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System](the-lie-jordan-decomposition-of-a-bilinear-product-and-the-jordan-triple-system.html).

**Remark (what each half keeps).** The symmetric half is commutative, unital with the same unit $e_t$, and satisfies the Jordan identity, so it is a Jordan algebra; it is not associative and it is not formally real. The antisymmetric half is a bracket with values in the pure quaternions, and it is a Lie algebra isomorphic to $\mathfrak{so}(3)$. Neither half is the algebra, and the algebra is recovered from the pair by the theorem above.

## The Four Composites

**Proposition (the four composites).** The product and its two halves compose in exactly four ways, and the four identities are
$$
\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2,\qquad
\tilde q_2\tilde q_1=\tilde q_1\bullet\tilde q_2-\tilde q_1\wedge\tilde q_2 ,
$$
$$
\tilde q_1\bullet\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1\bigr),\qquad
\tilde q_1\wedge\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1\bigr).
$$

*Proof.* The first two are the theorem of the preceding section applied to the two orders, and the last two are the definitions of the halves. All four were verified on general elements.

**Remark (the square in the four readings).** On the diagonal the four composites collapse to two: the halves agree, $\tilde q\wedge\tilde q=0$, and the product, the symmetric half and the reversed product coincide in $\tilde q^2$. The antisymmetric half vanishes identically on the diagonal, and this is the reason every statement about squares of the algebra is a statement about the symmetric half alone.

**Remark (the four composites of the batch).** The same four identities exist for the quaternionic product, with the conjugation inserted in the first slot, and they are the four composites of [The General Quaternionic Bilinear Product of the Quaternions](the-general-quaternionic-bilinear-product-of-the-quaternions.html). The two families together are the eight composites of the batch, and the twelve of the biquaternion are the same eight counted over $\mathbb{C}$ with the two complex conjugations added.

## The Trace Form

**Definition.** The **trace form** of the plain product is
$$
\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr)=q_{1t}q_{2t}-(\vec q_1,\vec q_2).
$$

**Theorem (the form and its signature).** The form is symmetric, nondegenerate, of signature $(1,3)$, with Gram matrix $\mathrm{diag}(1,-1,-1,-1)$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$; its quadratic form is $P$; its radical is zero; its isotropic cone is $\{q_t^2=\lvert\vec q\rvert^2\}$.

*Proof.* The scalar part of the product is the displayed bilinear form, symmetric because the scalar part of a commutator vanishes. The Gram matrix is read on the basis. A vector orthogonal to everything is orthogonal to $e_t$ and to the three vector units, hence zero. The quadratic form is $\tau(\tilde q,\tilde q)=q_t^2-\lvert\vec q\rvert^2$. The form is the Minkowski form of [Quaternion Metrics](quaternion-metrics.html), and its signature is computed there.

**Proposition (the two invariances).** For all $\tilde q_1,\tilde q_2,\tilde q_3$,
$$
\tau(\tilde q_1\tilde q_2,\tilde q_3)=\tau(\tilde q_1,\tilde q_2\tilde q_3),\qquad
\tau(\tilde q_1\tilde q_2,\tilde q_3)=\tau(\tilde q_2,\tilde q_1\tilde q_3).
$$

*Proof.* The first is the invariance of the scalar part under the cyclic permutation of a product of three factors, which holds because $\mathrm{Sc}(\tilde q_1\tilde q_2\tilde q_3)$ is unchanged by a cyclic permutation and $\mathrm{Sc}$ is invariant under the conjugation; the second follows from the first and from the symmetry of $\tau$ together with $\tau(\tilde q_1\tilde q_2,\tilde q_3)=\tau(\tilde q_3,\tilde q_1\tilde q_2)$. Both were verified on general triples, with a deviation at the level of the arithmetic.

**Remark (the form against the norm).** The form $\tau$ is indefinite and the norm $N$ is definite, and the two are related by $N(\tilde q)=\tau(\tilde q,\tilde q^{\natural})$. The form is the one that the product makes canonical, and the norm is the one that the conjugation makes canonical; the algebra needs both, and the articles of the P norm are the reading of the first as a partition.

## The Place among the Two

| | $\tilde q_1\tilde q_2$ | $\tilde q_1^{\natural}\tilde q_2$ |
|---|---|---|
| scalar row | $q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ | $q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ |
| mixed terms | $q_{1t}\vec q_2+q_{2t}\vec q_1$ | $q_{1t}\vec q_2-q_{2t}\vec q_1$ |
| cross term | $+\vec q_1\times\vec q_2$ | $-\vec q_1\times\vec q_2$ |
| associative | yes | no |
| unit | two-sided, $e_t$ | left only, $e_t$ |
| diagonal | indefinite, $P$ | definite, $N$ |
| trace form | $(1,3)$ | $(4,0)$ |
| commutator | $\wedge$ | $-\wedge$ |
| symmetrisation | $\bullet$ | scalar-valued |

**Remark (the column that is the algebra).** This is the column that is associative and two-sidedly unital, and it is the only one: the quaternionic product keeps a left unit and loses associativity, and no third product exists over $\mathbb{R}$. The table is the row of the plain product in the comparison of the six, and the whole of the difference between the two general products is the sign of the conjugation in the first slot: it flips the scalar row, flips the mixed terms and flips the cross term, and the flips destroy associativity, the right unit and the division property of the product as a product of the batch.

## Summary

The general plain bilinear product is
$$
\tilde q_1\tilde q_2=\bigl(q_{1t}q_{2t}-(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2 ,
$$
$\mathbb{R}$-bilinear, associative, two-sidedly unital with the unit $e_t$, and a division product: $\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$ and there are no zero divisors.

Its image is the whole algebra and every element is a square; its diagonal is $\tilde q^2=(q_t^2-\lvert\vec q\rvert^2)+2q_t\vec q$; its idempotents are $0$ and $e_t$; its only central elements are the reals.

It splits uniquely into the symmetric half $\tilde q_1\bullet\tilde q_2$ and the antisymmetric half $\tilde q_1\wedge\tilde q_2=\vec q_1\times\vec q_2$, and the four composites of the product with its two halves reconstruct each from the others.

Its trace form is $\tau=\mathrm{Sc}(\tilde q_1\tilde q_2)$, of signature $(1,3)$, nondegenerate, associative and self-adjoint; its quadratic form is the indefinite norm $P$; the norm $N$ is the same form composed with the conjugation. Between the two general products, this is the one that is associative and carries the unit, and the other is the one that carries a definite form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra |
| $\tilde q=q_te_t+\vec q$ | the element, its scalar part and its vector part |
| $\tilde q_1\tilde q_2$ | the general plain bilinear product |
| ${}^{\natural}$ | the quaternion conjugation |
| $\bullet$ | the symmetric plain product |
| $\wedge$ | the antisymmetric plain product |
| $(\cdot,\cdot)$ | the Euclidean inner product of the vector parts |
| $\times$ | the cross product of the vector parts |
| $P(\tilde q)=\mathrm{Sc}(\tilde q^2)$ | the plain algebraic norm |
| $N(\tilde q)=\tilde q\tilde q^{\natural}$ | the quaternion norm |
| $\tau$ | the trace form $\mathrm{Sc}(\tilde q_1\tilde q_2)$ |

## Further Reading

- [The General Quaternionic Bilinear Product of the Quaternions](the-general-quaternionic-bilinear-product-of-the-quaternions.html), for the second of the two general products.
- [The Jordan Structure of the Symmetric Plain Product of the Quaternions](the-jordan-structure-of-the-symmetric-plain-product-of-the-quaternions.html), for the first half.
- [The Lie Structure of the Antisymmetric Plain Product of the Quaternions](the-lie-structure-of-the-antisymmetric-plain-product-of-the-quaternions.html), for the second half.
- [Introduction to the Quaternion Algebra](introduction-to-the-quaternion-algebra.html), for the algebra the product makes of the space.
- [The General Plain Bilinear Product](the-general-plain-bilinear-product.html), for the biquaternion counterpart.
