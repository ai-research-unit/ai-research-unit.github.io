# __Zero Divisors of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the
Symmetric Plain Algebra of Biquaternions*. This article determines the elements that annihilate a
non-zero element, gives the criterion, describes the two families, and compares the set with the
sets of the four general products.

The comparison is where the block separates from the algebra. For the four general products of *The
Four General Products of the Biquaternion $\mathbb{C}$ Space* the zero-divisor set is the isotropic
cone of the central square, and the four sets **coincide** (*Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). For
the symmetric plain product the set is **strictly larger**: every element of the vector subspace,
isotropic or not, is a zero divisor, because the symmetrisation drops the cross product that the
plain product uses to keep a non-isotropic pure element regular. The block therefore does not
inherit the zero-divisor theory of the algebra, and the difference is a theorem of this article and
not a defect.

The zero divisors are the elements that fail to be regular, and they are not the same as the
elements that fail to be invertible: the element $e_1$ is invertible, with $C(e_1)=1$, and it
annihilates $e_2$. The careful separation of the two notions is *Norm and Invertibility in the
Symmetric Plain Algebra*; this article owns the annihilating elements.

A zero divisor is defined relative to a product, and the definition is stated once for a general
product in *Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor*;
throughout this article the product is $\bullet$ and, unqualified, **zero divisor** means zero
divisor of $\bullet$. The zero divisors of the algebra, their criterion and their set are *Zero
Divisors of the General Plain Algebra*; the annihilators and the determinant of the left
multiplication are *The Trace Form and the Invariance of the Symmetric Plain Algebra*; the two
families are named by *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*.

**The results.** A non-zero element of the block is a zero divisor exactly when $Q_0=0$ or $C(\tilde Q)=0$, so the zero-divisor set is the union of the vector subspace minus the origin and the isotropic cone $\mathcal C=\{C(\tilde Q)=0\}$ minus the origin. It splits into the pure family, the whole vector subspace minus the origin, each member annihilating a complex plane, and the scalar family, the elements with $Q_0\neq0$ and $C(\tilde Q)=0$, each annihilating the complex line $\mathbb{C}\tilde Q^{\natural}$ and equal up to scalar to a non-trivial idempotent. The set is strictly larger than the zero-divisor set of the algebra and of the four general products, which is the isotropic cone alone, the witness of the difference being $e_1$.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis
$e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and $Q_\mu\in\mathbb{C}$. An
element is $\tilde Q=Q_0e_0+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_ke_k$, and
$(\vec P,\vec Q)=\sum_kP_kQ_k$ is the complex bilinear dot product of the vector parts. The
product with the mark is $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$; the
central square is $C(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2=\tilde Q\tilde Q^{\natural}$, and the left
multiplication is $L^{\bullet}_{\tilde Q}:\tilde R\mapsto\tilde Q\bullet\tilde R$. The vector
subspace $\mathrm{Vect}(\mathbb{B})$ is the set of pure elements, $Q_0=0$.

## The Definition

**Definition (zero divisor of a product).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde{Q}$ be an element. Then $\tilde{Q}$ is a **left zero divisor of $\star$** when there is a
non-zero $\tilde{R}$ with $\tilde{Q}\star\tilde{R}=0$, a **right zero divisor of $\star$** when
there is a non-zero $\tilde{R}$ with $\tilde{R}\star\tilde{Q}=0$, and a **two-sided zero divisor of
$\star$** when it is both. A product is **without zero divisors**, or a **domain**, when no
non-zero element is a zero divisor.

Throughout this article the product is the symmetric plain product $\bullet$. The block is
**commutative**, so $\tilde{Q}\bullet\tilde{R}=\tilde{R}\bullet\tilde{Q}$ and the left, the right
and the two-sided zero divisors are the same set; *unqualified*, **zero divisor** means zero
divisor of $\bullet$, and the criterion is that $\tilde{Q}\neq0$ and the operator
$L^{\bullet}_{\tilde{Q}}$ has non-trivial kernel,

$$
\tilde{Q}\ \text{zero divisor}\iff\ker L^{\bullet}_{\tilde{Q}}\neq\{0\}\iff \tilde{Q}\neq0\ \text{and}\ \det L^{\bullet}_{\tilde{Q}}=0 .
$$

The zero divisors of the four general products and the theorem of the four coinciding sets are
*Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Criterion

**An element of the block is a zero divisor if and only if it is non-zero and $Q_0=0$ or $C(\tilde Q)=0$.**

The determinant of the left multiplication is known from the form:
$\det(L^{\bullet}_{\tilde Q})=Q_0^2C(\tilde Q)$ (*The Trace Form and the Invariance of the
Symmetric Plain Algebra*). The criterion follows at once, and it is simpler to prove it on the
kernel, which also gives the two annihilators.

**Theorem (the criterion).** An element $\tilde Q$ of the block is a zero divisor if and only if it
is non-zero and

$$
Q_0=0\qquad\text{or}\qquad C(\tilde Q)=0 .
$$

*Proof.* Suppose $Q_0=0$, so $\tilde Q=\vec Q$ is pure and non-zero. For a general
$\tilde R=R_0e_0+\vec R$ the product is
$\tilde Q\bullet\tilde R=R_0\vec Q-(\vec Q,\vec R)e_0$, which vanishes exactly when
$R_0=0$ and $(\vec Q,\vec R)=0$; the second condition is one complex equation on
$\vec R$, so there is a non-zero solution and $\tilde Q$ is a zero divisor. Suppose $Q_0\neq0$
and $C(\tilde Q)=0$. Then $\tilde Q\bullet\tilde Q^{\natural}=C(\tilde Q)e_0=0$ by the quadratic
identity, and $\tilde Q^{\natural}\neq0$, so $\tilde Q$ is a zero divisor. Conversely, suppose
$Q_0\neq0$ and $C(\tilde Q)\neq0$ and let $\tilde R$ satisfy $\tilde Q\bullet\tilde R=0$. In
coordinates the equation is the pair

$$
Q_0\vec R+R_0\vec Q=0,\qquad Q_0R_0-(\vec Q,\vec R)=0 .
$$

Taking the dot product of the first with $\vec Q$ gives
$Q_0(\vec Q,\vec R)+R_0(\vec Q,\vec Q)=0$, and substituting
$(\vec Q,\vec R)=Q_0R_0$ from the second gives
$R_0\bigl(Q_0^2+(\vec Q,\vec Q)\bigr)=R_0C(\tilde Q)=0$, so $R_0=0$; then the second gives
$(\vec Q,\vec R)=0$ and the first gives $Q_0\vec R=0$, so $\vec R=0$. Hence
$\tilde R=0$.

**Corollary.** The block is not a domain, and it is not a domain in the strongest possible way: the
whole vector subspace is contained in the zero-divisor set.

The criterion and the criterion of the algebra have the same second clause, $C(\tilde Q)=0$, and
the block adds the first, $Q_0=0$. It is exactly this addition that makes the block's set
different.

## The Two Families

**The criterion splits the zero-divisor set into two families: the pure family, every non-zero pure element, and the scalar family, the elements with $Q_0\neq0$ and $C(\tilde Q)=0$.**

The criterion splits the zero-divisor set into two families, and each family has its own
annihilator.

### The Pure Family

**Proposition.** Every non-zero pure element is a zero divisor.

*Proof.* The product of two pure elements is $\tilde Q\bullet\tilde R=-(\vec Q,\vec R)e_0$,
which vanishes for every non-zero $\tilde R$ in the complex plane orthogonal to $\vec Q$; in
the three-dimensional complex vector subspace the single equation $(\vec Q,\vec R)=0$ has a
two-dimensional solution space.

The family is parametrised by the vector subspace without the origin, a set of complex dimension
three, and each member annihilates a complex plane. **No pure element of the block is regular**,
whatever the value of its central square: $e_1$ is a zero divisor and $C(e_1)=1$, and the whole
pure isotropic cone, whose members have $C=0$, sits inside the same family. The annihilator itself,
of complex dimension two, and the operator with its rank are *Annihilators of the Symmetric Plain
Algebra*, below this article in this category.

### The Scalar Family

**Proposition.** A zero divisor with non-zero scalar part satisfies $C(\tilde Q)=0$.

*Proof.* The natural conjugate gives $\tilde Q\bullet\tilde Q^{\natural}=C(\tilde Q)e_0$, which
vanishes exactly when $C(\tilde Q)=0$, so such an element is a zero divisor; and the criterion's
converse computation shows that no element with $Q_0\neq0$ and $C(\tilde Q)=0$ is regular, the
determinant vanishing through the factor $C(\tilde Q)$.

The family is the set $\{\tilde Q:Q_0\neq0,\ C(\tilde Q)=0\}$, of complex dimension three, and up
to the scalar it is the set of the **idempotents** of the block: the non-zero non-trivial
idempotents are $\tfrac12(e_0+\vec u)$ with $\vec u^2=e_0$ pure, and
$C(\tfrac12(e_0+\vec u))=0$. The exact correspondence is *Idempotents of the Symmetric Plain
Algebra*, and the annihilator of the family, the complex line $\mathbb{C}\tilde Q^{\natural}$, is
*Annihilators of the Symmetric Plain Algebra*.

### The Set

The two families are the entire zero-divisor set, and it is the union of the vector subspace and
the zero-divisor cone $\mathcal{C}$:

$$
\mathcal{Z}(\bullet)=\bigl\{\tilde Q\neq0:\ Q_0=0\ \text{or}\ C(\tilde Q)=0\bigr\}
=\bigl(\mathrm{Vect}(\mathbb{B})\setminus\{0\}\bigr)\cup\bigl(\mathcal{C}\setminus\{0\}\bigr).
$$

**Theorem.** The zero-divisor set of the block contains the zero-divisor set of the algebra and is
strictly larger:

$$
\mathcal{C}\setminus\{0\}=\mathcal Z(\text{algebra})\subsetneq\mathcal Z(\bullet).
$$

*Proof.* The algebra's set is $\mathcal{C}\setminus\{0\}$ (*Zero Divisors of the General Plain
Algebra*), and every one of its elements satisfies $C=0$ and is in $\mathcal Z(\bullet)$. The
inclusion is strict: $e_1$ has $C(e_1)=1\neq0$ and $Q_0=0$, hence is in $\mathcal Z(\bullet)$ and
not in the algebra's set.

## The Comparison with the Four General Products

**The zero-divisor sets of the four general products coincide with each other and with the isotropic cone of the central square, and the zero-divisor set of the block is strictly larger than all four.**

**Theorem.** The zero-divisor sets of the four general products coincide with each other and with
the isotropic cone of the central square, and the zero-divisor set of the block is strictly larger
than all four.

*Proof.* The coincidence for the four general products is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The
strict inclusion is the theorem above: the block's set contains the isotropic cone and the whole
vector subspace.

So no transfer of the zero-divisor classification from the four general products to the block is
valid, and this is the point of the article. The reason is visible in the product: the plain
product of two pure elements is
$\vec P\vec Q=-(\vec P,\vec Q)+\vec P\times\vec Q$, whose antisymmetric
cross term keeps a non-isotropic pure element regular, while the symmetrisation removes the cross
term and leaves only the scalar $-(\vec P,\vec Q)e_0$, which vanishes on the orthogonal
complement whatever the central square. **The block's zero-divisor set is the union of the vector
subspace and the isotropic cone, not the isotropic cone alone.**

**Remark (the regularity and the invertibility).** The zero divisors are exactly the elements with
a singular left multiplication, and an element of the block can be invertible and a zero divisor:
$e_1$ satisfies both conditions. The invertible elements are the complement of the isotropic cone,
so the zero divisors that are invertible are the pure non-isotropic elements, that is the vector
subspace with its isotropic cone removed.

## The Relation to the Other Notions

**The pure roots of $\pm1$ are zero divisors whatever their central square, the non-zero roots of $0$ are the nilpotents, and the scalar family is exactly the non-zero scalar multiples of the non-trivial idempotents, every idempotent other than $0$ and $e_0$ being a zero divisor.**

**Zero divisors and the roots.** A root of $-1$ or of $+1$ that is pure is a zero divisor whatever
its central square, so the block has invertible roots of the central values that are not regular;
this does not occur in the algebra, whose pure roots of $-1$ are units. The root theory is *Square
Roots of One and the Idempotents of the Symmetric Plain Algebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*; the roots of $0$ are the
pure isotropic elements, the nilpotents of *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*.

**Zero divisors and the idempotents.** The scalar family is the set of the non-zero scalar
multiples of the non-trivial idempotents, and every idempotent other than $0$ and $e_0$ is a zero
divisor; the identity and the origin are not.

## Summary

A zero divisor of the block is a non-zero element annihilated by a non-zero element, the notion
coincides on the left, the right and the two-sided because the product is commutative, and the
criterion is $Q_0=0$ or $C(\tilde Q)=0$. The set splits into the pure family, all of the vector
subspace without the origin, whose members have a two-dimensional annihilator equal to the
orthogonal complement of the vector part in the pure subspace, and the scalar family, the non-pure
isotropic elements, whose members have the one-dimensional annihilator
$\mathbb{C}\tilde Q^{\natural}$ and which are the non-zero scalar multiples of the non-trivial
idempotents. The zero-divisor set is the union of the vector subspace and the isotropic cone, and
it strictly contains the zero-divisor set of the algebra and the common set of the four general
products, which is the isotropic cone alone; the witness of the difference is $e_1$, a zero divisor
of the block with $C(e_1)=1$. An element of the block can be invertible and a zero divisor, and the
invertible elements are exactly the complement of the isotropic cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\mathrm{ann}(\tilde Q)=\ker L^{\bullet}_{\tilde Q}$ | the annihilator of $\tilde Q$, its left and right annihilator being equal |
| $\mathcal Z(\bullet)=(\mathrm{Vect}\setminus\{0\})\cup(\mathcal{C}\setminus\{0\})$ | the zero-divisor set of the block |
| $Q_0=0$ or $C(\tilde Q)=0$ | the criterion for a non-zero element |
| $\tilde Q^{\natural}$ | the natural conjugate, spanning the annihilator in the scalar family |
| $\det L^{\bullet}_{\tilde Q}=Q_0^2C(\tilde Q)$ | the determinant that detects the zero divisors |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor*, for the product-relative definition and the dictionary of the classes.
- *Zero Divisors of the General Plain Algebra*, for the zero divisors of the algebra, their criterion and their set.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the four coinciding sets, against which the block's set is compared.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the invertible elements and the distinction with the regular ones.
- *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*, for the two families named by the block.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra*, for the determinant $\det L^{\bullet}_{\tilde Q}=Q_0^2C(\tilde Q)$.
- *Annihilators of the Symmetric Plain Algebra* (`articles_maths/annihilators-of-the-symmetric-plain-algebra.md`), below this article in this category, the companion article, for the annihilator of an element, the operator and its features, the rank table and the dichotomy by the families
