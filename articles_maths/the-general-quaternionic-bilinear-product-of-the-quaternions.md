# __The General Quaternionic Bilinear Product of the Quaternions__

## Introduction

The second of the two general products of the batch reads the first slot of the plain product through the conjugation,
$$
\tilde q_1\cdot\tilde q_2=\tilde q_1^{\natural}\tilde q_2 ,
$$
and it is the product of the slot pairing $({}^{\natural},\mathrm{id})$. The two slots read the same involution over $\mathbb{R}$, so this is the second and the last general product; the biquaternion counterpart, with two conjugations available, has four and not two.

The product is a deliberate distortion of the plain one: the same multiplication, with the first factor reflected in the conjugation. It destroys associativity, flexibility and power associativity and it keeps only the left unit, while leaving the diagonal and the division property untouched, because the conjugation is an anti-automorphism of the plain algebra and the norm is invariant under it. The result is a product that is normed in the strong sense and is nevertheless not associative.

The article reads the product as a product of the batch. The algebra it defines is the general quaternionic algebra of this space, cited and not restated; its two halves are [The Jordan Structure of the Symmetric Quaternionic Product of the Quaternions](the-jordan-structure-of-the-symmetric-quaternionic-product-of-the-quaternions.html) and [The Lie Structure of the Antisymmetric Quaternionic Product of the Quaternions](the-lie-structure-of-the-antisymmetric-quaternionic-product-of-the-quaternions.html).

## The Product and Its Coordinate Rule

**Definition.** The **general quaternionic bilinear product** is
$$
\tilde q_1\cdot\tilde q_2=\tilde q_1^{\natural}\tilde q_2 ,
$$
with $\tilde q_1^{\natural}=q_{1t}-\vec q_1$.

**Theorem (the coordinate rule).** For all $\tilde q_1,\tilde q_2$,
$$
\boxed{\;\tilde q_1\cdot\tilde q_2=\bigl(q_{1t}q_{2t}+(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2\;}
$$

*Proof.* Apply the coordinate rule of the plain product to the pair $(\tilde q_1^{\natural},\tilde q_2)$: the scalar row becomes $q_{1t}q_{2t}+(\vec q_1,\vec q_2)$, the mixed terms become $q_{1t}\vec q_2-q_{2t}\vec q_1$, and the cross term becomes $-\vec q_1\times\vec q_2$ because the vector part of the first factor has changed sign. Verified exactly on the sixteen pairs of the basis and on general elements.

**Corollary (the exchange relation).** For all $\tilde q_1,\tilde q_2$,
$$
\tilde q_2^{\natural}\tilde q_1=\bigl(\tilde q_1^{\natural}\tilde q_2\bigr)^{\natural} ,
$$
so the transposed product is the conjugate of the product and the product is not symmetric in any sense.

*Proof.* The conjugate of $\tilde q_1^{\natural}\tilde q_2$ is $\tilde q_2^{\natural}\tilde q_1$, the conjugation reversing the order. Verified on the basis.

## The Scalar–Vector Form

**Proposition (the four pieces).** In the notation $a=q_{1t}$, $b=q_{2t}$, $\vec u=\vec q_1$, $\vec v=\vec q_2$,
$$
\tilde q_1\cdot\tilde q_2=ab+(\vec u,\vec v)+a\vec v-b\vec u-\vec u\times\vec v ,
$$
and the four pieces are respectively symmetric, symmetric, mixed and antisymmetric under the interchange of the two arguments.

*Proof.* Read the coordinate rule in the four symbols. The inner product is symmetric, $a\vec v$ and $b\vec u$ exchange under the interchange, and the cross product changes sign. Verified on general elements.

**Remark (the scalar part is the quaternion form).** The scalar part $ab+(\vec u,\vec v)$ is the polar form of the norm $N$, and it is positive definite, so the product is scalar-positive in the sense that the scalar part of a square is never negative. This is the sharpest difference from the plain product, whose scalar part $ab-(\vec u,\vec v)$ is indefinite and vanishes on a cone of dimension three.

**Remark (the antisymmetric piece is the whole of the distortion).** The product differs from the plain product in the sign of the first slot alone, and the difference of the two products is
$$
\tilde q_1\tilde q_2-\tilde q_1^{\natural}\tilde q_2=2q_{1t}\vec q_2 ,
$$
a mixed term and nothing else. So the distortion is invisible on the vector subspace, where the two products agree, and it grows with the scalar part of the left factor. The two products agree exactly on the pure quaternions, and they coincide everywhere only on the real line, where both are the multiplication of the reals.

## The Laws It Keeps and the Laws It Loses

**Theorem (associativity fails).** There are $\tilde q_1,\tilde q_2,\tilde q_3$ with
$$
(\tilde q_1\cdot\tilde q_2)\cdot\tilde q_3\neq\tilde q_1\cdot(\tilde q_2\cdot\tilde q_3).
$$

*Proof.* Take $\tilde q_1=\tilde q_2=\vec e_x$ and $\tilde q_3=\vec e_y$. Then $\vec e_x\cdot\vec e_x=\vec e_x^{\natural}\vec e_x=e_t$, so the left side is $e_t\cdot\vec e_y=\vec e_y$; and $\vec e_x\cdot\vec e_y=\vec e_x^{\natural}\vec e_y=-\vec e_z$, so the right side is $\vec e_x\cdot(-\vec e_z)=\vec e_x^{\natural}(-\vec e_z)=\vec e_x\vec e_z=-\vec e_y$. The two differ by $2\vec e_y$. Computed exactly.

**Proposition (the general form of the failure).** In the plain algebra,
$$
(\tilde q_1\cdot\tilde q_2)\cdot\tilde q_3-\tilde q_1\cdot(\tilde q_2\cdot\tilde q_3)=\tilde q_2^{\natural}\tilde q_1\tilde q_3-\tilde q_1^{\natural}\tilde q_2^{\natural}\tilde q_3=\tilde q_2^{\natural}\,2\vec q_1\,\tilde q_3+\bigl[\tilde q_2^{\natural},\tilde q_1^{\natural}\bigr]\tilde q_3 ,
$$
so the failure vanishes on the real line $\vec q_1=0$ and nowhere else.

*Proof.* The first order gives $(\tilde q_1^{\natural}\tilde q_2)^{\natural}\tilde q_3=\tilde q_2^{\natural}\tilde q_1\tilde q_3$, the second gives $\tilde q_1^{\natural}\tilde q_2^{\natural}\tilde q_3$, and the two are brought together by writing $\tilde q_1=\tilde q_1^{\natural}+2\vec q_1$. The bracket $[\tilde q_2^{\natural},\tilde q_1^{\natural}]=\tilde q_2^{\natural}\tilde q_1^{\natural}-\tilde q_1^{\natural}\tilde q_2^{\natural}$ is a commutator of the plain product, hence pure, and it cancels in the first case. Verified on general triples, with a deviation at the level of the arithmetic.

**Theorem (flexibility and power associativity fail).** The identity $\tilde q_1\cdot(\tilde q_2\cdot\tilde q_1)=(\tilde q_1\cdot\tilde q_2)\cdot\tilde q_1$ fails, and so does the identity that makes the third power unambiguous.

*Proof.* Take $\tilde q_1=\tilde q_2=\vec e_x$. The left side is $\vec e_x\cdot(\vec e_x\cdot\vec e_x)=\vec e_x\cdot e_t=\vec e_x^{\natural}=-\vec e_x$; the right side is $(\vec e_x\cdot\vec e_x)\cdot\vec e_x=e_t\cdot\vec e_x=\vec e_x$. The two differ by $2\vec e_x$, and the same computation is the two bracketings of the cube, so the first ambiguous power is the third. The general defect is $\tilde q_1^{\natural}\tilde q_2^{\natural}\tilde q_1-\tilde q_2^{\natural}N(\tilde q_1)$, which vanishes exactly on the real line $\vec q_1=0$ and was found to be nonzero at every other random pair. Computed exactly.

**Remark (a normed product that is not associative).** The norm is multiplicative for this product, $N(\tilde q_1\cdot\tilde q_2)=N(\tilde q_1)N(\tilde q_2)$, because $N$ is multiplicative for the plain product and invariant under the conjugation; the product has therefore no zero divisors either. A product may be normed and not associative, and this is the smallest example of it in the batch. The two properties that fail, associativity and flexibility, are exactly the two that involve reading the same element in two slots in two different ways.

## The One-Sided Units

**Theorem (the left unit is $e_t$, alone).** For every $\tilde q$,
$$
e_t\cdot\tilde q=e_t^{\natural}\tilde q=\tilde q ,\qquad
\tilde q\cdot e_t=\tilde q^{\natural} ,
$$
so $e_t$ is a left unit and not a right one, and it is the only left unit.

*Proof.* The first display is $e_t^{\natural}=e_t$. The second is the definition. For uniqueness, a left unit $\tilde u$ satisfies $\tilde u^{\natural}\tilde q=\tilde q$ at every $\tilde q$, hence $\tilde u^{\natural}=e_t$ and $\tilde u=e_t$. Verified by solving the four linear systems in the coefficient basis: the solution space of the left-unit equations is one-dimensional and spanned by $e_t$.

**Proposition (there is no right unit).** No element $\tilde u$ satisfies $\tilde q\cdot\tilde u=\tilde q$ for all $\tilde q$.

*Proof.* At $\tilde q=e_t$ the condition reads $\tilde u=e_t$, and at $\tilde q=\vec e_x$ it then reads $-\vec e_x=\vec e_x$. The right-unit system is inconsistent; its least-squares residual is $1$, computed on the coefficient basis.

**Remark (the two one-sided actions).** The left multiplication $L_{\tilde q_1}\tilde q_2=\tilde q_1^{\natural}\tilde q_2$ composes as
$$
L_{\tilde q_1}L_{\tilde q_2}=L_{\tilde q_2\tilde q_1},
$$
the opposite of the plain product: the left multiplications close under the opposite law, which is the algebraic form of the left-handedness of the block. The right multiplications do not compose at all, and this asymmetry between the two sides is the algebraic form of the absence of a right unit.

## The Image, the Diagonal and the Scalar Part

**Proposition (the image is everything, and the diagonal is the ray).** Every element is a value of the product, and for every $\tilde q$,
$$
\tilde q\cdot\tilde q=\tilde q^{\natural}\tilde q=N(\tilde q)e_t .
$$

*Proof.* For the image, a target $\tilde t$ is $\tilde t^{\natural}\cdot e_t$. For the diagonal, the product of $\tilde q^{\natural}$ with $\tilde q$ is the norm, since the vector parts cancel and the two mixed terms cancel. Verified on the basis and on general elements.

**Corollary (the square loses the vector part).** The image of the diagonal is the closed ray $\mathbb{R}_{\geq0}e_t$, and the square of an element carries no information but its modulus.

*Proof.* The square is $N(\tilde q)e_t$ and $N\geq0$. The vector part of the square is zero for every element, and two elements with the same norm have the same square.

**Remark (the diagonal against the plain diagonal).** The plain diagonal is $\tilde q^2=(q_t^2-\lvert\vec q\rvert^2)+2q_t\vec q$ and it is injective off the cone where it is not; the quaternionic diagonal is $N(\tilde q)e_t$ and it is never injective. The loss is the price of the reflection in the first slot, and it is the reason the symmetrisation of this product is scalar valued: the symmetric half is the polar form of the very norm that the diagonal computes.

**Proposition (the two-point set of idempotents).** The idempotents of the quaternionic product are $0$ and $e_t$.

*Proof.* $N(\tilde\Pi_{\mathrm{id}})e_t=\tilde\Pi_{\mathrm{id}}$ forces $\tilde\Pi_{\mathrm{id}}=\lambda e_t$ with $\lambda^2=\lambda$. Verified by solving the equations in the coefficient basis. The idempotents of the product, and their coincidence with the idempotents of the plain product, are treated in [Square Roots of One and the Idempotents of the Quaternionic Product](square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.html).

## The Two Halves of This Product

**Theorem (the reconstruction).** For all $\tilde q_1,\tilde q_2$,
$$
\tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge_{\natural}\tilde q_2 ,
$$
with
$$
\langle\tilde q_1,\tilde q_2\rangle_{\natural}=q_{1t}q_{2t}+(\vec q_1,\vec q_2)
$$
and
$$
\tilde q_1\wedge_{\natural}\tilde q_2=\tfrac12\bigl(\tilde q_1^{\natural}\tilde q_2-\tilde q_2^{\natural}\tilde q_1\bigr)=q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2 .
$$

*Proof.* The symmetric part of the coordinate rule keeps the scalar row, which is symmetric, and doubles the mixed terms; the antisymmetric part keeps the mixed terms with their signs and the cross term. The first is the polar form of $N$ times $e_t$; the second is the display. Verified exactly on the basis and on general elements.

**Remark (one half is a form and the other is a bracket).** The two halves are of different kinds: the symmetric half is scalar valued and is a symmetric bilinear form in disguise, and the antisymmetric half is purely vector valued and is a bracket. Neither half is an algebra over the space in the ordinary sense, and the reconstruction is the only statement that binds them. The first half is read in [The Jordan Structure of the Symmetric Quaternionic Product of the Quaternions](the-jordan-structure-of-the-symmetric-quaternionic-product-of-the-quaternions.html), where it fails the Jordan identity by a one-dimensional defect, and the second in [The Lie Structure of the Antisymmetric Quaternionic Product of the Quaternions](the-lie-structure-of-the-antisymmetric-quaternionic-product-of-the-quaternions.html), where it fails the Jacobi identity by a three-dimensional defect.

**Remark (the two halves of the two products coincide).** The antisymmetric half of this product is the antisymmetric half of the plain product plus a mixed term, and the symmetric half of this product is the polar form of $N$ times $e_t$. The plain product has the indefinite part in its symmetric half and the cross product in its antisymmetric half; the quaternionic product has the definite form in its symmetric half and carries the mixed terms in its antisymmetric half. The two splits are not the same split and they do not commute with the exchange of the products.

## The Four Composites

**Proposition (the four composites).** The product and its two halves compose in exactly four ways:
$$
\tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge_{\natural}\tilde q_2,\qquad
\tilde q_2^{\natural}\tilde q_1=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t-\tilde q_1\wedge_{\natural}\tilde q_2 ,
$$
and the two halves are the half-sum and the half-difference of the two orders.

*Proof.* The first two are the theorem of the preceding section applied to the two orders, using the exchange relation; the last two are the definitions. Verified on general elements.

## The Trace Form and the Halves

**Definition.** The **trace form** of the quaternionic product is
$$
\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}\bigl(\tilde q_1^{\natural}\tilde q_2\bigr)=q_{1t}q_{2t}+(\vec q_1,\vec q_2)=\langle\tilde q_1,\tilde q_2\rangle_{\natural}.
$$

**Theorem (the form is the quaternion form).** The form is symmetric, positive definite, of Gram matrix $I_4$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with radical $0$ and no isotropic element but $0$; its quadratic form is $N$; and it is recovered from the product by $\tilde q_1\bullet_{\natural}\tilde q_2=\tau(\tilde q_1,\tilde q_2)e_t$.

*Proof.* The scalar part of $\tilde q_1^{\natural}\tilde q_2$ is the display, symmetric because the mixed terms and the cross term have no scalar part. The Gram matrix is read on the basis, where $\tau(e_t,e_t)=1$ and $\tau(\vec e_k,\vec e_k)=1$ and the mixed entries vanish. The polar form of $N$ is $\tfrac12(N(\tilde q_1+\tilde q_2)-N(\tilde q_1)-N(\tilde q_2))$, which is the display.

**Proposition (the invariance across the product, and its failure).** For all $\tilde q_1,\tilde q_2,\tilde q_3$,
$$
\tau\bigl(\tilde q_1^{\natural}\tilde q_2,\tilde q_3\bigr)=\tau\bigl(\tilde q_2,\tilde q_3\tilde q_1^{\natural}\bigr),
$$
while
$$
\tau\bigl(\tilde q_1^{\natural}\tilde q_2,\tilde q_3\bigr)\neq\tau\bigl(\tilde q_1^{\natural},\tilde q_2^{\natural}\tilde q_3\bigr)
$$
in general.

*Proof.* The first identity is the cyclic invariance of the scalar part in the plain algebra: $\mathrm{Sc}\bigl((\tilde q_1^{\natural}\tilde q_2)^{\natural}\tilde q_3\bigr)=\mathrm{Sc}\bigl(\tilde q_2^{\natural}\tilde q_1\tilde q_3\bigr)$, and the last scalar is cyclically invariant. For the second, take $\tilde q_1=\tilde q_2=\tilde q_3=\vec e_x$: the left side is $-1$ and the right side is $0$. Both statements were verified on general triples.

**Remark (the failure is the failure of associativity).** The second identity is the associativity of the form, and it holds exactly when the product is associative with respect to the form; it fails here because the product is not associative. The first identity is the weaker invariance that survives every product built from the plain one and an involution, and it is the one that makes the form self-adjoint for the left multiplications. The two statements together are the exact account of what the definite form gives and what it does not.

## The Place among the Two

| | $\tilde q_1\tilde q_2$ | $\tilde q_1^{\natural}\tilde q_2$ |
|---|---|---|
| scalar row | $q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ | $q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ |
| mixed terms | $q_{1t}\vec q_2+q_{2t}\vec q_1$ | $q_{1t}\vec q_2-q_{2t}\vec q_1$ |
| cross term | $+\vec q_1\times\vec q_2$ | $-\vec q_1\times\vec q_2$ |
| associative | yes | no |
| flexible | yes | no |
| power associative | yes | no |
| unit | two-sided, $e_t$ | left only, $e_t$ |
| diagonal | $P+2q_t\vec q$ | $N e_t$ |
| norm multiplicative | yes | yes |
| zero divisors | none | none |
| trace form | $(1,3)$ | $(4,0)$ |
| symmetric half | indefinite Jordan product | the form times $e_t$ |
| antisymmetric half | $\vec q_1\times\vec q_2$ | $q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$ |

**Remark (the column that carries the definite form).** This is the column that is neither associative nor unital and the only one that carries a positive definite form on the trace, and it is the only one of the two whose diagonal is scalar for every element. The three facts have one cause: the conjugation in the first slot is an anti-automorphism of the plain product, and an anti-automorphism preserves the norm, reverses the order, and destroys the reassociation.

## Summary

The general quaternionic bilinear product is
$$
\tilde q_1^{\natural}\tilde q_2=\bigl(q_{1t}q_{2t}+(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2 ,
$$
$\mathbb{R}$-bilinear, non-associative, non-flexible, non-power-associative, with $e_t$ as its only left unit and with no right unit.

Its image is the whole algebra, its diagonal is $N(\tilde q)e_t$ and loses the vector part, and its idempotents are $0$ and $e_t$. It is normed: $N(\tilde q_1\cdot\tilde q_2)=N(\tilde q_1)N(\tilde q_2)$, and it has no zero divisors.

Its two halves are the scalar form $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$ and the bracket $q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$, and its trace form is the quaternion form, positive definite, of Gram matrix $I_4$, which is the form that the symmetric half is. Between the two general products, this is the one that carries the definite form and loses the laws of association, and the other is the one that keeps them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra |
| $\tilde q=q_te_t+\vec q$ | the element, its scalar part and its vector part |
| $\tilde q_1^{\natural}\tilde q_2$ | the general quaternionic bilinear product |
| ${}^{\natural}$ | the quaternion conjugation |
| $\bullet_{\natural}$ | the symmetric quaternionic product |
| $\wedge_{\natural}$ | the antisymmetric quaternionic product |
| $\langle\cdot,\cdot\rangle_{\natural}$ | the polar form of the norm, $q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ |
| $N(\tilde q)=\tilde q^{\natural}\tilde q$ | the quaternion norm |
| $P(\tilde q)=\mathrm{Sc}(\tilde q^2)$ | the plain algebraic norm |
| $L_{\tilde q}$ | the left multiplication of the quaternionic product |

## Further Reading

- [The General Plain Bilinear Product of the Quaternions](the-general-plain-bilinear-product-of-the-quaternions.html), for the first of the two general products.
- [The Jordan Structure of the Symmetric Quaternionic Product of the Quaternions](the-jordan-structure-of-the-symmetric-quaternionic-product-of-the-quaternions.html), for the first half.
- [The Lie Structure of the Antisymmetric Quaternionic Product of the Quaternions](the-lie-structure-of-the-antisymmetric-quaternionic-product-of-the-quaternions.html), for the second half.
- [The General Quaternionic Bilinear Product](the-general-quaternionic-bilinear-product.html), for the biquaternion counterpart.
