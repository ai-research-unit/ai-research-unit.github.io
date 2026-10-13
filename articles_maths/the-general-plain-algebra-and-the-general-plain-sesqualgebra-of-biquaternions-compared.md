# __The General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared__

## Introduction

The underlying space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, defined side by side in *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and compared in *Comparison Between the Four General Products*. Two of them are built from the plain product alone and the involution of the algebra, and they are the subjects of this article: the **general plain product** $\tilde P\tilde Q$, which makes $\mathbb{B}$ an associative unital $\mathbb{C}$-algebra, and the **general plain sesquilinear product** $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, which makes $\mathbb{B}$ a sesqualgebra over $\mathbb{C}$ and is the **derived operation** of the first with respect to the Hermitian conjugation. The two structures live on the same four-dimensional complex space, share the same norm and the same zero divisors, and differ everywhere the involution enters.

This article compares the two structures point by point, on ten headings: the multiplication and the unit, associativity, the involution, the norm and invertibility, the zero divisors and the nilpotents, the idempotents, the square roots, the form, the operators, and the matrix models. It is a comparison and not a construction: every structure is assumed as built in *Introduction to the General Plain Algebra of Biquaternions* and *Introduction to the General Plain Sesqualgebra of Biquaternions*, and every contrast is read off a statement proved in one of the two chapters, cited where it is used. The two quaternionic structures are the twins of the two here and are compared, with the four general products read on four columns, in *Comparison Between the Four General Products*; they are named only where the contrast needs them, and never developed.

The article is arranged so that each section is self-contained: the entry of the two structures under the heading, the contrast, its cause, and the article that owns the proof. The closing *Summary* collects the ten rows in one table.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with the basis $e_0,e_1,e_2,e_3$ and the central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$; $\mathrm{Sc}(\tilde Q)=Q_0$ is the scalar part and $\mathrm{Vect}(\tilde Q)=\mathbf Q$ the vector part. The coefficient conjugation is $\overline{Q_\mu}$, the quaternion conjugation is $\tilde Q^{\natural}=Q_0e_0-\mathbf Q$, and the Hermitian conjugation is the composite ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, of coordinates $Q^{*}_0=\overline{Q_0}$ and $Q^{*}_k=-\overline{Q_k}$, that is $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The **norm** is the central square $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=Q_0^2+Q_1^2+Q_2^2+Q_3^2$. The two structures are written $(\mathbb{B},\cdot)$, the general plain algebra, and $(\mathbb{B},\star)$ with $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, the general plain sesqualgebra. Throughout, an **idempotent** is an element $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$ in the product under discussion, and a **projector** is an idempotent operator of the space.

## The Two Products and the Two Units

The two products differ first in their class.

**Proposition (the class of each product).** The general plain product $\tilde P\tilde Q$ is $\mathbb{C}$-bilinear; the general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ is additive in each variable, $\mathbb{C}$-linear in the first and $\mathbb{C}$-**conjugate**-linear in the second,
$$
(\lambda\tilde P)\star\tilde Q=\lambda\,(\tilde P\star\tilde Q),\qquad \tilde P\star(\lambda\tilde Q)=\bar\lambda\,(\tilde P\star\tilde Q),\qquad \lambda\in\mathbb{C}.
$$

The two scalar rules are the axioms of a sesqualgebra over the field $\mathbb{C}$ with its conjugation $\varsigma(z)=\bar z$; associativity, commutativity and the unit are not axioms but consequences of the products (*Sesqualgebras*, *The Sesquilinear Product*).

The unit separates them at once.

**Theorem (the two units).** Of the two structures, only the algebra has a two-sided unit. In $(\mathbb{B},\cdot)$ the element $e_0$ is a two-sided identity and the only one. In $(\mathbb{B},\star)$ the element $e_0$ is a **right** identity, $\tilde Q\star e_0=\tilde Q$ for every $\tilde Q$, and not a left one, the left action being the involution itself:
$$
e_0\star\tilde Q=\tilde Q^{*}.
$$

*Proof.* The identity of the algebra is the definition of the plain product, and uniqueness is the standard argument for a two-sided unit. For the sesquilinear product, $e_\mu\star e_0=e_\mu$ for every basis element, whence $\tilde Q\star e_0=\tilde Q$ by additivity; and $e_0\star\tilde Q=\tilde Q^{*}$, witnessed at $\tilde Q=e_1$ by $-e_1\neq e_1$. A left unit $\tilde E$ would satisfy $\tilde E=\tilde E\star e_0=e_0$, whence $\tilde E=e_0$, and $e_0$ is not a left unit because $e_0\star\tilde X=\tilde X^{*}\neq\tilde X$ for any non-Hermitian $\tilde X$. The one-sided unit is the mark of the derived operation and appears in the general theory in the same form. The same computation is *The Two One-Sided Actions and the Absence of a Unit*.

The two products are recorded in one table.

| property | $(\mathbb{B},\cdot)$ | $(\mathbb{B},\star)$ |
|---|---|---|
| rule | $\tilde P\tilde Q$ | $\tilde P\tilde Q^{*}$ |
| additive in each variable | yes | yes |
| $\mathbb{C}$-linear in the first slot | yes | yes |
| $\mathbb{C}$-linear in the second slot | yes | no, conjugate-linear |
| class | associative unital algebra | sesqualgebra, derived operation |
| $e_0$ a left identity | yes | no |
| $e_0$ a right identity | yes | yes |
| $e_0$ a two-sided identity | yes | no |

The asymmetry of the unit is not a defect of the chosen element: it is the visible form of the second scalar rule, and it survives every change of basis. The product is the **derived operation** $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of the pair $(\mathbb{B},{}^{*})$ in the sense of *Sesqualgebras*, and that is its place in the theory rather than a second multiplication of the algebra.

## Associativity

**Theorem (the failure of associativity).** The product of the algebra is associative. The product of the sesqualgebra is neither associative nor commutative.

*Proof.* The plain product is the multiplication of the matrix algebra $\mathbb{B}\cong M_2(\mathbb{C})$, hence associative. For the sesquilinear product, the algebra is of full type over $\mathbb{C}$ and the base involution $\varsigma$ is not the identity; the collapse theorem of *Sesqualgebras* then forbids associativity and commutativity, since either would force $\varsigma=\mathrm{id}$. The two witnesses are explicit. Associativity fails on $(e_0,e_1,e_1)$,
$$
(e_0\star e_1)\star e_1=(-e_1)\star e_1=-e_0,\qquad e_0\star(e_1\star e_1)=e_0\star e_0=e_0,
$$
and commutativity fails on $(e_1,e_2)$, where $e_1\star e_2=-e_3$ while $e_2\star e_1=e_3$.

The failure has one cause, and it is the same cause as the one-sided unit: the involution sits in the second slot. Conjugating a product transposes the two factors, ${(xy)}^{*}=y^{*}x^{*}$, and the transposition is what no parenthesis can absorb. In the algebra the involution is nowhere in the product and the associativity is untouched; in the sesqualgebra it is the second slot, and associativity is destroyed. The associator of the sesquilinear product and the ternary product $\tilde P\tilde Q^{*}\tilde R$ it defines are *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

## The Involution

The two structures carry the same three coefficient maps and use them differently. Each map is $\mathbb{C}$-conjugate-linear or $\mathbb{C}$-linear according to whether it conjugates the coefficients, and is measured on the product.

| map | coordinates | on $\mathbb{C}$ | on the plain product | character |
|---|---|---|---|---|
| $\bar{\cdot}$ | $Q_\mu\mapsto\overline{Q_\mu}$ | conjugation | $\overline{\tilde P\tilde Q}=\bar{\tilde P}\,\bar{\tilde Q}$ | automorphism |
| ${}^{\natural}$ | $Q_0\mapsto Q_0$, $Q_k\mapsto-Q_k$ | identity | $(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$ | anti-automorphism |
| ${}^{*}$ | $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ | conjugation | $(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}$ | anti-automorphism |

**Theorem (the involution in each structure).** In the algebra the Hermitian conjugation is an anti-automorphism, $(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}$. In the sesqualgebra it is the reversal law
$$
(\tilde P\star\tilde Q)^{*}=\tilde Q\star\tilde P,
$$
so that the involution exchanges the two slots of the multiplication.

*Proof.* The algebra identity is the composition of the two rows above: the coefficient conjugation is an automorphism and the quaternion conjugation an anti-automorphism, and the composite of an automorphism with an anti-automorphism is an anti-automorphism. The reversal law is the same identity read in the derived operation: $(\tilde P\tilde Q^{*})^{*}=\tilde Q\tilde P^{*}$, which is $\tilde Q\star\tilde P$.

So the same involution plays two roles. In the algebra it is superfluous to the multiplication and serves the form and the adjoint; the algebra forgets it, and its product is defined for every pair of elements without reference to it. In the sesqualgebra it is half of the multiplication, and the product of two elements is available only through it. The four conjugations that index the four general products are *The Group of Involutions*; the Hermitian and anti-Hermitian halves it cuts out are *Hermitian and Skew-Hermitian Elements*.

## Norm and Invertibility

The two structures share the norm and the criterion that reads it, and they differ in what they build on it.

**Theorem (the norm under the two products).** The norm $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ is central, of coordinates $\sum_\mu Q_\mu^2$, and it is multiplicative for the algebra and twisted for the sesqualgebra:
$$
N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q),\qquad N(\tilde P\star\tilde Q)=N(\tilde P)\,\overline{N(\tilde Q)}.
$$

*Proof.* Both identities are the multiplicativity of the scalar part of the plain product with the two conjugations read in the two slots; the second is the first with $\tilde Q$ replaced by $\tilde Q^{*}$ and the coefficient conjugation extracted, $N(\tilde Q^{*})=\overline{N(\tilde Q)}$, which the coordinates give directly.

The first identity is what a norm should satisfy, and it makes the norm a multiplicative quadratic form on the algebra; the second is a twisting law and is not multiplicativity, the second factor being conjugated. The consequence is the whole contrast of the section.

**Theorem (the units).** The algebra has a group of units and a division criterion; the sesqualgebra has neither, and keeps only the criterion.

- In the algebra, the invertible elements are exactly those of nonzero norm, $\mathbb{B}^{\times}=\{\tilde Q:N(\tilde Q)\neq0\}$, the inverse is unique and two-sided,
$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)},
$$
and the group of units is $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$. An element is therefore invertible exactly when it is not a zero divisor, and the two-sided inverse solves both equations $\tilde X\tilde Y=e_0$ and $\tilde Y\tilde X=e_0$ at once.
- In the sesqualgebra, no element is a two-sided unit: a two-sided unit $\tilde E$ would give $e_0\star\tilde E=e_0$, that is $\tilde E^{*}=e_0$ by the left action, whence $\tilde E=e_0$, and $e_0$ is not a left unit. The set of invertible elements is empty, and what survives is the **one-sided inverse**: the two equations $\tilde X\star\tilde R=e_0$ and $\tilde R\star\tilde X=e_0$ have a common solution exactly when $N(\tilde X)\neq0$, and then it is unique,
$$
\tilde X^{-1\star}=(\tilde X^{-1})^{*}=\frac{\overline{\tilde X}}{\overline{N(\tilde X)}}.
$$

*Proof.* For the algebra, $\tilde Q^{\natural}/N(\tilde Q)$ is the classical inverse of the quaternion algebra extended over $\mathbb{C}$, and the criterion $N\neq0$ is the invertibility criterion, computed in *Norm and Invertibility in the General Plain Algebra*. For the sesqualgebra, $\tilde X\star\tilde R=e_0$ reads $\tilde X\tilde R^{*}=e_0$, that is $\tilde R^{*}=\tilde X^{-1}$, whence $\tilde R=(\tilde X^{-1})^{*}$; the other equation gives the same element because the involution is an anti-automorphism, $(\tilde X^{*})^{-1}=(\tilde X^{-1})^{*}$. The absence of a two-sided unit forbids the name "invertible element" and leaves the one-sided inverse, which is *Norm and Invertibility in the General Plain Sesqualgebra*.

The two structures therefore agree on the partition of $\mathbb{B}$ into the singular elements $\{N=0\}$ and the rest, and disagree on the group: the algebra's units are the complement of the zero-divisor cone and form $\mathrm{GL}_2(\mathbb{C})$, while the sesqualgebra's "unit group" is empty and only the one-sided inverse survives. The norm is the central square and not the form of either structure; the forms are in §*The Form*.

## Zero Divisors and Nilpotents

The zero divisors coincide, and the nilpotents do not.

**Theorem (the zero divisors coincide).** The left, right and two-sided zero divisors of the algebra and of the sesqualgebra are the same set, and it is the nonzero part of the zero-divisor cone
$$
Z=\{\tilde P\neq0:N(\tilde P)=0\},
$$
a complex cone of dimension three, of real dimension six, with annihilator a complex plane for each of its nonzero elements.

*Proof.* The criterion is the vanishing of the central square $N(\tilde P)=\sum_\mu P_\mu^2$ for each of the four general products, proved in *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*: the four products differ only by the involutions of the two slots, the involutions are bijections, and the central square is invariant, so the four product-wise zero-divisor sets coincide. In the $2\times2$ model the left multiplication is the matrix product by $\mathsf{M}_2(\tilde P)$, so its kernel is a complex plane exactly when $N(\tilde P)=0$ and vanishes otherwise; the right multiplication gives the same condition.

**Theorem (the nilpotents differ).** The two structures have the same nilpotents as a set and different nilpotents as a class.

- In the algebra the square-zero elements are exactly the **pure isotropic cone**
$$
\{\tilde P:P_0=0,\ (\mathbf P,\mathbf P)=0\},
$$
a complex cone of dimension two, of real dimension four, and every nonzero element of it is a nilpotent of index two, $\tilde P^2=0$; equivalently the square reads $\tilde P^2=\bigl(P_0^2-(\mathbf P,\mathbf P)\bigr)e_0+2P_0\mathbf P$ and vanishes exactly on the cone.
- In the sesqualgebra there is **no nonzero square-zero element**: the square $\tilde P\star\tilde P=\tilde P\tilde P^{*}$ has scalar part $\sum_\mu\lvert P_\mu\rvert^2$, which is real, nonnegative and vanishes only at $\tilde P=0$. The sesqualgebra nevertheless has nilpotents, and they are exactly the pure isotropic cone above, of **index three**: an element of the cone satisfies $\tilde P^{\star2}\neq0$ and $\tilde P^{\star3}=0$.

*Proof.* The square of the algebra is developed by the coordinates of the plain product; the vanishing of its scalar and vector parts is the two scalar equations $P_0^2=(\mathbf P,\mathbf P)$ and $P_0\mathbf P=0$, whose solutions are the pure isotropic cone together with the origin. For the sesqualgebra, the scalar part is $\mathrm{Sc}(\tilde P\tilde P^{*})=\sum_\mu P_\mu\overline{P_\mu}=\sum_\mu\lvert P_\mu\rvert^2$, a sum of nonnegative reals, vanishing only if every coordinate vanishes. The pure isotropic elements satisfy $\tilde P\tilde P=0$, and one verifies $\tilde P\tilde P^{*}\neq0$ while $\tilde P(\tilde P^{*})\tilde P^{*}=0$ on the cone; the index is read in the $2\times2$ model, where the cone is the rank-one traceless matrices and the criterion $P_0=0$ is the vanishing of the trace. The two classes are *Nilpotents of the General Plain Algebra*, *Nilpotents of the General Plain Sesqualgebra* and *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the central square that both criteria read is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

| class | $(\mathbb{B},\cdot)$ | $(\mathbb{B},\star)$ |
|---|---|---|
| zero divisors | $\{N=0\}\setminus\{0\}$ | same set |
| square-zero elements | pure isotropic cone, index $2$ | $\{0\}$ |
| nilpotents | pure isotropic cone, index $2$ | pure isotropic cone, index $3$ |
| nilpotents inside the zero divisors | proper subfamily | proper subfamily |

The sesqualgebra thus has a **thinner** square-zero set than the algebra and the **same** nilpotent set, and the partition of the zero divisors by the scalar part is inherited unchanged: the pure family $P_0=0$ with $(\mathbf P,\mathbf P)=0$ is the nilpotent family, and the non-pure family $P_0\neq0$ consists of zero divisors that are not nilpotents in either structure. The index is the only thing the second slot changes, and it changes it from two to three.

## Idempotents

**Theorem (the two idempotent sets).** The idempotents of the algebra are the elements $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$, and they form the family
$$
\{0,e_0\}\cup\Bigl\{\tfrac12(e_0+\eta):\eta\in\mathrm{Vect}(\mathbb{B}),\ \eta^2=e_0\Bigr\},
$$
of real dimension four; those other than $0$ and $e_0$ have central square $0$ and are zero divisors, and the complementation $\tilde\Pi\mapsto e_0-\tilde\Pi$ pairs them with orthogonality $\tilde\Pi(e_0-\tilde\Pi)=0$. The idempotents of the sesqualgebra are exactly the **Hermitian idempotents**
$$
\{0,e_0\}\cup\Bigl\{\tfrac12(e_0+i\hat\mu):\hat\mu\in\mathbb{R}^3,\ \lvert\hat\mu\rvert=1\Bigr\},
$$
the two-sphere of real dimension two, and the sesqualgebra's idempotent family is the Hermitian part of the algebra's.

*Proof.* The algebra equation $\tilde\Pi^2=\tilde\Pi$ is $\tilde\Pi=1/2(e_0+\eta)$ with $\eta$ a pure vector of square one, computed in *Idempotents of the General Plain Algebra*; the central square of such an element is $N(\tilde\Pi)=\tfrac14\bigl(1+\sum_k\eta_k^2\bigr)$ in the coordinates, which vanishes because $\eta^2=e_0$ forces $\sum_k\eta_k^2=-1$, and complementation is immediate from $\eta^2=e_0$. For the sesqualgebra, the equation is $\tilde\Pi\tilde\Pi^{*}=\tilde\Pi$, which in the $2\times2$ model reads $\mathsf{M}_2(\tilde\Pi)\mathsf{M}_2(\tilde\Pi)^{\dagger}=\mathsf{M}_2(\tilde\Pi)$, that is, the matrix is an orthogonal projection; an orthogonal projection is Hermitian and idempotent, and reading Hermiticity back through $\mathsf{M}_2$ gives $\tilde\Pi^{*}=\tilde\Pi$ and the parametrisation above. The two families are *Idempotents of the General Plain Algebra*, *Idempotents of the General Plain Sesqualgebra* and *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

Three readings of the same classification are worth separating.

- **The nesting.** The sesqualgebra's idempotents are a proper subfamily of the algebra's: the Hermitian ones, a two-sphere inside the four-dimensional family. The algebra's idempotents include, besides the Hermitian two-sphere, the non-Hermitian idempotents, which lie in none of the remarkable subspaces and which no sesquilinear product sees.
- **The idempotents are zero divisors.** Every nontrivial idempotent of the algebra has $N=0$, and the same holds for the sesqualgebra's. Idempotence and invertibility are therefore incompatible in either structure, as they must be.
- **The projector calculus.** In the algebra an idempotent element corresponds to a projector: its left multiplication $L_{\tilde\Pi}$ is idempotent, its image is the principal left ideal $\mathbb{B}\tilde\Pi$ and its kernel the annihilator, because the product is associative. This correspondence is the criterion of *The Specificities of the General Plain Algebra* and holds in the algebra alone among the twelve structures; in the sesqualgebra the left multiplications are conjugate-linear, no nonzero one is a projector, and the correspondence is unavailable. The right multiplications of the sesqualgebra do have a projector criterion, and it classifies the *algebra's* idempotents rather than the sesqualgebra's, as *The Specificities of the General Plain Sesqualgebra* proves.

## Square Roots

The two equations are $\tilde X^2=\tilde A$ and $\tilde X\star\tilde X=\tilde A$, and the images of the two square maps are different sets.

**Theorem (the sesquilinear square).** For every $\tilde X$, the sesquilinear square $\tilde X\star\tilde X=\tilde X\tilde X^{*}$ is Hermitian and its scalar part is the Euclidean quadratic form,
$$
\mathrm{Sc}(\tilde X\star\tilde X)=\sum_\mu\lvert X_\mu\rvert^2.
$$
Its image is the **Hermitian cone** $\{\alpha e_0+i\mathbf w:\alpha\geq\lvert\mathbf w\rvert\}\subset\mathbb{M}_+$, of real dimension four, and the boundary $\alpha=\lvert\mathbf w\rvert$ is exactly the zero-divisor set: writing $\tilde X\star\tilde X=\alpha e_0+i\mathbf w$ with $\alpha\in\mathbb{R}$ and $\mathbf w\in\mathbb{R}^3$, one has
$$
\alpha^2-\lvert\mathbf w\rvert^2=\lvert N(\tilde X)\rvert^2 .
$$

*Proof.* Hermiticity is the reversal law at $\tilde P=\tilde Q$, $(\tilde X\star\tilde X)^{*}=\tilde X\star\tilde X$; the scalar part is $\mathrm{Sc}(\tilde X\tilde X^{*})=\sum_\mu X_\mu\overline{X_\mu}$; the identity for the vector part follows by expanding the square in the four coordinates and using $\lvert N\rvert^2=(a^2-b^2)^2+(2a\cdot b)^2$ for $\tilde X=a+ib$ with real $a,b$, and its vanishing is $N(\tilde X)=0$. The cone and its boundary are *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*.

The contrast on the central values is complete.

| central value | algebra $(\mathbb{B},\cdot)$ | sesqualgebra $(\mathbb{B},\star)$ |
|---|---|---|
| $-e_0$ | nonempty: the roots of $-1$, the elements $\pm ie_0$ and the pure $\mathbf X$ with $\mathbf X\cdot\mathbf X=1$ | **empty** |
| $0$ | the pure isotropic cone | $\{0\}$ |
| $+e_0$ | nonempty: the involutions, the roots of $+1$ | the unitary group $U(2)$, written $e^{i\theta}w$ over the real unit quaternions $w$ |

*Proof of the sesquilinear column.* A root of $-e_0$ would have scalar part $\sum_\mu\lvert X_\mu\rvert^2=-1$, impossible; the root of $0$ forces every coordinate to vanish, since the scalar part is a sum of nonnegative reals; and the root of $+e_0$ is the equation $\tilde X\tilde X^{*}=e_0$, solved by $\tilde X=e^{i\theta}w$ with $\theta$ real and $w$ a real unit quaternion, because such an element has $\tilde X^{*}=e^{-i\theta}w^{\natural}=e^{-i\theta}w^{-1}$ and its sesquilinear square is $\tilde X\star\tilde X=e^{i\theta}w\,e^{-i\theta}w^{-1}=w\,w^{-1}=e_0$. The algebra's column is the classification of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*; the sesquilinear column is *Square Roots of Minus One, Zero and Plus One in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, where the roots of $+1$ are identified with the unitary group; and the general equations are *Square Roots of a General Element in the General Plain Algebra* and *Square Roots of a General Element in the General Plain Sesqualgebra*.

The sharp difference is the sign. The algebra's square map reaches every central value, the roots of $-1$ in particular, because the algebra is split over $\mathbb{C}$ and its square is unconstrained. The sesqualgebra's square map is confined to the Hermitian cone and never becomes negative, since its scalar part is a sum of squares; a root of the sesquilinear equation exists exactly when the target lies in the cone, and no non-real or negative central value has one. On the boundary of the cone the two phenomena meet: the identity $\alpha^2-\lvert\mathbf w\rvert^2=\lvert N(\tilde X)\rvert^2$ shows that a sesquilinear square lies on the boundary $\alpha=\lvert\mathbf w\rvert$ exactly when $\tilde X$ is a zero divisor of the algebra, so the boundary of the sesquilinear cone is the image of the algebra's zero-divisor cone.

## The Form

Each structure carries the form that its own product selects, and the two forms are the two readings of the same scalar part through the two slots.

**Theorem (the two forms).** The algebra carries the general plain bilinear form and the sesqualgebra the general plain sesquilinear form,
$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu Q_\mu,\qquad \langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu}.
$$
The first is symmetric, $\mathbb{C}$-bilinear and non-degenerate, of coefficient Gram matrix $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ and real signature $(4,4)$; it is the invariant bilinear form of the algebra. The second is Hermitian, positive definite and non-degenerate, of coefficient Gram matrix $\mathrm{I}_4$ and real signature $(8,0)$; on the $2\times2$ model it is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr)$, and it makes $\mathbb{B}$ a complex Hilbert space for which the involution is an anti-linear isometry.

*Proof.* Each form is the scalar part of the corresponding product, and the coordinate expressions are the definition of the scalar part; the Gram matrix of the first is $\mathrm{E}$ and of the second $\mathrm{I}_4$, since $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\mathrm{Sc}(e_\mu e_\nu^{*})=\delta_{\mu\nu}$. The second is positive definite because $\langle\tilde P,\tilde P\rangle_{*}=\sum_\mu\lvert P_\mu\rvert^2$, a sum of nonnegative reals vanishing only at the origin. The four pairings of the algebra, their Gram matrices and their adjoints are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the form of the algebra and its transposes are *Association and the Transpose on the General Plain Algebra*.

Three consequences separate the structures.

- **Definiteness.** The algebra's form is indefinite, of signature $(4,4)$: the coefficient basis splits into four directions on which the form restricted to the real span is positive and four on which it is negative. The sesqualgebra's form is definite; its quadratic form $\sum_\mu\lvert Q_\mu\rvert^2$ is positive and vanishes only at the origin. The algebra is split over $\mathbb{C}$, and its form records the split; the sesqualgebra's form is the Euclidean structure and records none.
- **The square.** The square of the algebra need not be self-adjoint for the algebra's form, while the square of the sesqualgebra is always self-adjoint for its own form and lies in the positive cone. The two facts are one: the sesquilinear square is $\tilde X\tilde X^{*}$, the canonical self-adjoint square of the involution, and $\mathrm{Sc}$ of it is the positive definite form itself.
- **The groups.** The isometries of the two forms are the two classical groups attached to the two approaches: $\mathrm{O}_4(\mathbb{C})$ for the algebra's bilinear form and the unitary group of the Hermitian form for the sesqualgebra's, the latter the maximal compact structure of the space. The distinguishing of the two forms is the work of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* and *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*; the trace forms and the transposes are *Association and the Transpose on the General Plain Algebra*.

The norm is not either form. $N(\tilde Q)=\sum_\mu Q_\mu^2$ is the quadratic form of the natural bilinear pairing $\sum_\mu P_\mu Q_\mu$ of the coefficients, and the vanishing set of that quadratic form is exactly the zero-divisor cone $\{N=0\}$; the algebra's own form is the $\varepsilon$-signed pairing, a different quadratic form, and the sesqualgebra's is the definite one. The four forms and the four algebraic norms of the biquaternion space are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, *Remarkable Subspaces and the Four Forms* and *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

## The Operators

The operators of the two structures are built from the same four multiplications and obey different laws.

**Theorem (the multiplication operators).** The left and the right multiplications of the algebra,
$$
L_{\tilde A}(\tilde Y)=\tilde A\tilde Y,\qquad R_{\tilde B}(\tilde Y)=\tilde Y\tilde B,
$$
are $\mathbb{C}$-linear and satisfy $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$ and $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$. Those of the sesqualgebra,
$$
L^{\star}_{\tilde A}(\tilde Y)=\tilde A\star\tilde Y=\tilde A\tilde Y^{*},\qquad R^{\star}_{\tilde B}(\tilde Y)=\tilde Y\star\tilde B=\tilde Y\tilde B^{*},
$$
are respectively conjugate-linear and $\mathbb{C}$-linear, and they satisfy
$$
R^{\star}_{\tilde A}R^{\star}_{\tilde B}=R^{\star}_{\tilde A\tilde B},\qquad R^{\star}_{\tilde A}={}^{*}\circ L^{\star}_{\tilde A},
$$
so that the **left** multiplications of the sesqualgebra form no monoid, while its **right** multiplications do, in the forward order.

*Proof.* The three laws of the algebra are the associativity of the product read on the three composite operators; the left multiplications are a faithful copy of the algebra and the right multiplications a faithful copy of its opposite. For the sesqualgebra, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}(\tilde Y)=(\tilde Y\tilde B^{*})\tilde A^{*}=\tilde Y(\tilde A\tilde B)^{*}=R^{\star}_{\tilde A\tilde B}(\tilde Y)$ by the anti-automorphism property of the involution, and $(\tilde A\tilde Y^{*})^{*}=\tilde Y\tilde A^{*}$ gives the identity $R^{\star}_{\tilde A}={}^{*}\circ L^{\star}_{\tilde A}$. The composite $L^{\star}_{\tilde A}L^{\star}_{\tilde B}$ is the composite of two conjugate-linear maps, hence $\mathbb{C}$-linear, and a left multiplication is conjugate-linear; so it is not a left multiplication, and no monoid law is available on that side. The forward law is the specificity of the sesqualgebra among the twelve structures, proved in *The Specificities of the General Plain Sesqualgebra*; the operators are *One-Sided Operators on the General Plain Algebra of Biquaternions* and *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*.

| operator fact | $(\mathbb{B},\cdot)$ | $(\mathbb{B},\star)$ |
|---|---|---|
| left multiplications | $\mathbb{C}$-linear, $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ | conjugate-linear, no monoid |
| right multiplications | $\mathbb{C}$-linear, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$ | $\mathbb{C}$-linear, $R^{\star}_{\tilde A}R^{\star}_{\tilde B}=R^{\star}_{\tilde A\tilde B}$ |
| the two families commute | yes | no |
| adjoint of the right multiplication | $R_{\tilde A}^{\approx}=L_{\tilde A}$ | $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$ |
| two-sided operators | $L_{\tilde A}R_{\tilde B}$, no norm entering | the dagger sandwich $\Theta_{\tilde Q}(\tilde Y)=\tilde Q\tilde Y\tilde Q^{*}$ |
| enveloping structure | $\mathbb{B}^{\mathrm e}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ | the sandwich monoid $W_{\tilde P,\tilde Q}$, proper in the endomorphisms |

*Reading the table.* The transpose of a left multiplication of the algebra is the corresponding right multiplication, $L_{\tilde A}^{\approx}=R_{\tilde A}$, because the algebra's form is symmetric and association moves the factor from one side to the other; the self-adjoint left multiplications of the algebra's form are the central ones alone, so its adjoint calculus is confined to the centre. The adjoint of a right multiplication of the sesqualgebra is the right multiplication at the conjugated parameter, $(R^{\star}_{\tilde A})^{\dagger}=R^{\star}_{\tilde A^{*}}$, because the sesqualgebra's form is Hermitian and the involution is what its adjoint moves. This is the operator face of §*The Involution*: the structure whose product contains the involution has the involution in its adjoint calculus, and the structure whose product forgets it has an adjoint calculus confined to the centre. The two-sided operators of the algebra are the plain products $L_{\tilde A}R_{\tilde B}$ and are assembled into the enveloping algebra $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, whereas the two-sided operators of the sesqualgebra are the dagger sandwiches $\Theta_{\tilde Q}$, quadratic in the parameter and multiplicative on the nose, $\Theta_{\tilde Q\tilde R}=\Theta_{\tilde Q}\circ\Theta_{\tilde R}$; the two envelopes are *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure* and *The Enveloping Operator Algebra of the General Plain Sesqualgebra and the Bi-module Structure*.

One further asymmetry follows from the operator law and belongs here. The ideals of the algebra are those of $M_2(\mathbb{C})$: the proper two-sided ideals are absent, the algebra is simple, and its left ideals form the projective line of the minimal left ideals. The sesqualgebra has no proper two-sided ideal either, but its one-sided lattices are not exchanged by the involution: its **left** ideals collapse to the two trivial ones $\{0\}$ and $\mathbb{B}$, while its **right** ideals are exactly the algebra's right ideals, so that the sesqualgebra is right-faithful and left-blind. This is *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*, and its contrast with *Ideals and Peirce Decomposition of the General Plain Algebra* is the ideal-theoretic image of the forward right law of the table.

## The Matrix Models

A single realization carries both products, and the involution is the bridge.

**Theorem (the two products in $\mathsf{M}_2$).** With the realization $\mathsf{M}_2(e_0)=I$, $\mathsf{M}_2(e_k)=-i\sigma_k$, for all $\tilde P,\tilde Q$,
$$
\mathsf{M}_2(\tilde P\tilde Q)=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q),\qquad \mathsf{M}_2(\tilde P\star\tilde Q)=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger},
$$
and the involution is the conjugate transpose,
$$
\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger},\qquad \mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q).
$$
The trace is $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$, and the two forms of §*The Form* are the two trace pairings $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))$ and $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})$.

*Proof.* The first identity says that $\mathsf{M}_2$ is an isomorphism of the algebra onto $M_2(\mathbb{C})$, which is *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the second is the first with $\tilde Q$ replaced by $\tilde Q^{*}$ and the identity $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$. The quaternion conjugation is the adjugate, checked on the basis $\mathsf{M}_2(e_k^{\natural})=-\mathsf{M}_2(e_k)$ against $\operatorname{adj}(-i\sigma_k)=i\sigma_k$ and extended by multiplicativity, and the trace is the classical invariant of the algebra. The sesquilinear reading is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

The same holds on the regular model, with the transposition in place of the adjugate.

| model | algebra $(\mathbb{B},\cdot)$ | sesqualgebra $(\mathbb{B},\star)$ |
|---|---|---|
| product | $\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)$ | $\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$ |
| quaternion conjugation | adjugate | adjugate |
| Hermitian conjugation | conjugate transpose | conjugate transpose |
| trace of the square's image | $2\bigl(Q_0^2-(\mathbf Q,\mathbf Q)\bigr)$ | $2\sum_\mu\lvert Q_\mu\rvert^2$ |
| the form | $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))$ | $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})$ |
| regular model $\mathsf{M}_4$ | $\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)$ | $\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}$ |

In the regular model the two identities are $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf T}$, $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$, $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$; the sesquilinear product is again the product with the adjoint in the second slot. The two models are *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* and *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*.

The model exposes every theorem above in one line. The unit of the algebra is $I$; the sesqualgebra has no unit because $A I^{\dagger}=A$ is a right identity and $IA^{\dagger}=A^{\dagger}$ a left one. The zero divisors are the singular matrices. The idempotents of the algebra are the idempotent matrices, the four-parameter family; those of the sesqualgebra are the orthogonal projections, the Hermitian idempotent matrices, and the nesting of §*Idempotents* is the nesting of the orthogonal projections in the idempotent matrices. The square of the sesqualgebra is $MM^{\dagger}$, positive semidefinite, and the cone of §*Square Roots* is the cone of the positive semidefinite matrices. The forms are the ordinary trace pairing and the Hilbert–Schmidt pairing, indefinite and definite. The operators are left and right matrix multiplication, and the adjoint of the second-slot product is the conjugate transpose. The algebra is the matrix algebra $M_2(\mathbb{C})$ itself, and the sesqualgebra is the same matrix algebra read with the adjoint woven into its second factor.

## Summary

The general plain algebra and the general plain sesqualgebra are two structures on the same four-dimensional complex space $\mathbb{B}$, and every one of their differences is the work of the Hermitian conjugation, which the algebra's product ignores and which the sesqualgebra's product contains in its second slot. The algebra is the associative unital algebra $\mathbb{B}\cong M_2(\mathbb{C})$, with unit $e_0$, multiplicative norm $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$, group of units $\mathrm{GL}_2(\mathbb{C})$, a real four-dimensional family of idempotents, a square map reaching every central value, an indefinite bilinear form of signature $(4,4)$, a faithful operator monoid and the full enveloping algebra. The sesqualgebra is the derived operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of the pair $(\mathbb{B},{}^{*})$, with a right unit only, no associativity, the twisted law $N(\tilde P\star\tilde Q)=N(\tilde P)\overline{N(\tilde Q)}$, an empty group of units beside a surviving one-sided inverse, the two-sphere of Hermitian idempotents inside the algebra's family, a square map confined to the Hermitian cone, a positive definite Hermitian form of signature $(8,0)$, conjugate-linear left multiplications with no monoid beside a forward right monoid, and an ideal lattice that is right-faithful and left-blind.

The two structures share what does not see the involution: the norm and its vanishing criterion, the zero-divisor cone $\{N=0\}$, the non-pure family of zero divisors, the partition of the space into the singular elements and the rest, and the four-dimensional space itself. They differ wherever the involution is read: the unit, associativity, multiplicativity, the group of units, the idempotents, the square roots, the form and the operators. The comparison is thus not a catalogue of accidents but one mechanism read in ten places, and the table collects it.

| heading | $(\mathbb{B},\cdot)$ | $(\mathbb{B},\star)$ |
|---|---|---|
| multiplication and unit | associative unital, $e_0$ two-sided | derived operation, $e_0$ right only, $e_0\star\tilde X=\tilde X^{*}$ |
| associativity | yes | no, witness $(e_0,e_1,e_1)$ |
| involution | anti-automorphism, $(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}$ | reversal law, $(\tilde P\star\tilde Q)^{*}=\tilde Q\star\tilde P$ |
| norm | multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$ | twisted, $N(\tilde P\star\tilde Q)=N(\tilde P)\overline{N(\tilde Q)}$ |
| invertibility | units $\{N\neq0\}\cong\mathrm{GL}_2(\mathbb{C})$, two-sided inverse | no unit, one-sided inverse iff $N\neq0$ |
| zero divisors | $\{N=0\}\setminus\{0\}$ | same set |
| nilpotents | pure isotropic cone, index $2$ | same set, index $3$ |
| idempotents | $\{0,e_0\}$ and $\tfrac12(e_0+\eta)$, $\eta^2=e_0$ | Hermitian ones, $\tfrac12(e_0+i\hat\mu)$ |
| square roots | roots of $-1$, $0$, $+1$ all nonempty | root of $-1$ none, of $0$ only the origin, of $+1$ the unitary family |
| form | $\mathrm{Sc}(\tilde P\tilde Q)$, signature $(4,4)$ | $\mathrm{Sc}(\tilde P\tilde Q^{*})$, signature $(8,0)$ |
| operators | left monoid, commuting families | left conjugate-linear, forward right monoid |
| matrix model | matrix product, idempotent matrices | product with the adjoint, orthogonal projections |

The two structures are the two ends of one construction: the algebra is the reference, and the sesqualgebra is the algebra read through its involution, its multiplication being the derived operation of the pair $(\mathbb{B},{}^{*})$ and its laws the algebra's laws bent by the second slot. Every difference in the table is traced to the involution sitting in that slot, and everything shared is what the involution does not touch. The quaternionic counterparts of the pair, obtained by placing the quaternion conjugation $\natural$ in the first slot, are the subject of *Comparison Between the Four General Products*, where the same table is read on four columns.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_0,e_1,e_2,e_3$, central $i$ |
| $\tilde Q=Q_0e_0+\mathbf Q$ | a biquaternion, scalar part $Q_0$ and vector part $\mathbf Q$ |
| ${}^{\natural},{}^{*}$ | quaternion conjugation and Hermitian conjugation, $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ |
| $\tilde P\tilde Q$ | the general plain product, the algebra's multiplication |
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the general plain sesquilinear product, the derived operation |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$ | the norm, the central square |
| $\mathbb{B}^{\times}=\{N\neq0\}$ | the group of units of the algebra, $\cong\mathrm{GL}_2(\mathbb{C})$ |
| $\tilde X^{-1\star}=(\tilde X^{-1})^{*}$ | the one-sided inverse of the sesqualgebra |
| $\{N=0\}\setminus\{0\}$ | the zero-divisor cone, common to the two structures |
| $\alpha e_0+i\mathbf w$, $\alpha\geq\lvert\mathbf w\rvert$ | the Hermitian cone, the image of the sesquilinear square |
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ | the form of the algebra, signature $(4,4)$ |
| $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | the form of the sesqualgebra, signature $(8,0)$ |
| $L_{\tilde A},R_{\tilde A}$ and $L^{\star}_{\tilde A},R^{\star}_{\tilde A}$ | the one-sided multiplications of the two structures |
| $\mathsf{M}_2,\mathsf{M}_4$ | the $2\times2$ and left regular $4\times4$ realizations |

## Further Reading

- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`) and *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the two structures compared here.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`) and *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the four products and their property table.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`) and *The Specificities of the General Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-general-plain-sesqualgebra.md`), for the isolation of each structure among the twelve.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), *Annihilators in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/idempotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/nilpotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), *Square Roots of Minus One, Zero and Plus One in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`) and *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the element theory the two structures share.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the four forms, their Gram matrices, their signatures and their isometry groups.
- Joseph H. M. Wedderburn, *Lectures on Matrices* (American Mathematical Society, 1934), for the matrix algebra $M_2(\mathbb{C})$ and the conjugations.
