# __Square Roots of Minus One, Zero and Plus One in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space__

## Introduction

Let $\star$ be a product on the biquaternion algebra $\mathbb{B}$. An element $\tilde\Xi$ is a **root of the central value** $\lambda e_0$ when its square in that product is the value,

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 , \qquad \lambda\in\mathbb{C},
$$

and the **root set** of the value is the set of its roots. Three values carry a name, $-1$, $0$ and $+1$, and they are the values on which the element theory of the algebra is built: the roots of $-1$ are the idempotents read through the map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi i)$, the roots of $0$ are the square-zero elements, which are the non-zero nilpotents of the algebra, and the roots of $+1$ are the products of the roots of $-1$ with $i$.

**The twelve names.** The space carries twelve products, so the generic definition poses twelve questions; this article answers them once for all twelve. Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first factor is read through the natural conjugation; the third is the family, $\mathrm A$ the algebra over $\mathbb{C}$ and $\mathrm S$ the sesqualgebra, whose second factor carries the Hermitian conjugation. The twelve are read in the four families of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** The general value $\lambda$, the four existence classes of the twelve structures and the criterion that a root of a non-zero value is a unit are *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the companion of this article, which states them once; the article cites them and applies them at the three named values. The root sets of each of the twelve structures stay owned by their articles, cited one by one in §*The Twelve Structures and the Three Values*, and the classification of the three values for the plain product, which is the one quoted here, is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*. The general vocabulary, the root, the central value, the idempotent and the nilpotent stated once for a general product, is *Definitions for the Study of the 12 Algebraic Structures*. The idempotent sets are *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and the parameter set of the roots of $-1$ is *Idempotents of the General Plain Algebra*; the square-zero sets are *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the cone and the zero-divisor sets are *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; and the unitary group of the third product is *The Unitary Group of the Biquaternion Algebra*.

**Conventions.** $\mathbb{B}$ has basis $e_0,e_1,e_2,e_3$, central scalar imaginary $i$ with $i^2=-1$, and a general element is $\tilde\Xi=\Xi_0e_0+\mathbf\Xi$ with $\Xi_0\in\mathbb{C}$ and $\mathbf\Xi=\sum_k\Xi_ke_k$. The natural conjugation is $\tilde\Xi^{\natural}=\Xi_0-\mathbf\Xi$, the star is $\tilde\Xi^{*}=\overline{\tilde\Xi^{\natural}}$, the **central square** is $C(\tilde\Xi)e_0=\tilde\Xi^{\natural}\tilde\Xi=\tilde\Xi\tilde\Xi^{\natural}$ with $C(\tilde\Xi)=\sum_\mu\Xi_\mu^{2}$, the **Hermitian square** is $H(\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$, and the **Krein value** is $\Delta(\tilde\Xi)=\lvert\Xi_0\rvert^{2}-\sum_k\lvert\Xi_k\rvert^{2}$. A **central value** is an element $\lambda e_0$ with $\lambda\in\mathbb{C}$. The root is defined in *Definitions for the Study of the 12 Algebraic Structures* §*Powers, the Square and the Roots* as a **non-zero** element with $\tilde\Xi\star\tilde\Xi=\lambda e_0$; a root set is read here as a solution set, so the origin is counted with the roots of $0$, and the places where an owner counts the non-zero roots alone are read as the origin alone.

## The Three Named Values

**Definition.** The **root set of the value** $\lambda e_0$ in the structure $\star$ is

$$
\mathcal R_\lambda=\{\tilde\Xi:\tilde\Xi\star\tilde\Xi=\lambda e_0\} ,
$$

and the three **named values** are $\lambda=-1$, $\lambda=0$ and $\lambda=+1$.

**Definition.** A subset of $\mathbb{B}$ is a **complex cone** when it contains $\mu\tilde\Xi$ for every $\tilde\Xi$ it contains and every $\mu\in\mathbb{C}$. Its **apex** is the origin.

**The root set of $0$ is a complex cone, and the root sets of the two signed values are not.** The square of a scaled element is $\mu^{2}(\tilde\Xi\star\tilde\Xi)$ for the six bilinear structures and $\lvert\mu\rvert^{2}(\tilde\Xi\star\tilde\Xi)$ for the six sesquilinear ones, so a root of $0$ scaled is again a root of $0$, while $\mu\tilde\Xi$ is a root of $\mu^{2}\lambda$ and not of $\lambda$ unless $\mu^{2}=1$ or $\lvert\mu\rvert^{2}=1$. The root set of $0$ is therefore the cone of the structure, cut by the vanishing of the square and carrying the apex, and the root sets of $-1$ and of $+1$ are the affine level sets of the square, cut by the two values and carrying no apex.

### The Roots of $\pm1$ Are Units and the Non-Zero Roots of $0$ Are Zero Divisors

The central square decides the nature of every root, and it decides it the same way for all four general products.

**Theorem (a root of a non-zero central value is a unit; quoted).** Let $\tilde\Xi$ be a root of the central value $\lambda$ in one of the four general products. Then $C(\tilde\Xi\star\tilde\Xi)=C(\tilde\Xi)^{2}$ for the two bilinear products and $C(\tilde\Xi\star\tilde\Xi)=\lvert C(\tilde\Xi)\rvert^{2}$ for the two sesquilinear ones, so that $C(\tilde\Xi)\neq0$ exactly when $\lambda\neq0$; consequently a root of a non-zero central value is a unit of the algebra and a non-zero root of $0$ is a zero divisor (*Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Roots Are Units, or Zero Divisors*).

The invertibility criterion of the algebra is the non-vanishing of the central square (*Norm and Invertibility in the General Plain Algebra*), and the zero-divisor set of the four general products is the punctured cone $\mathcal{C}\setminus\{0\}$ with $\mathcal{C}=\{C=0\}$ (*Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). At the three values the theorem therefore reads, for the four general products,

$$
\mathcal R_{-1}\cup\mathcal R_{+1}\subseteq\mathbb{B}^{\times} , \qquad \mathcal R_{0}\setminus\{0\}\subseteq\mathcal{C} , \qquad \mathbb{B}=\mathbb{B}^{\times}\sqcup\mathcal{C} ,
$$

the last relation being the partition of the algebra by the central square and the second holding for the four general products, whose zero-divisor set is the punctured cone and whose non-zero elements off the cone are the units. So an element is a unit exactly when it lies off the vanishing set of the central square, the roots of $-1$ and of $+1$ lie in the group of units, the non-zero roots of $0$ lie in the cone, and the two questions — where is the square zero, and where is it minus the unit — are answered at the two ends of the same criterion.

**Remark (the two structures outside the coincidence).** The first relation is not read by all twelve. The two symmetric bilinear structures $\mathrm{SPA}$ and $\mathrm{SQA}$ inherit the root sets of their general partners, so their signed roots are units too, and the four antisymmetric structures have no signed root; but the two symmetric sesquilinear structures $\mathrm{SPS}$ and $\mathrm{SQS}$ lose the rigidity of the square under the symmetrisation, and a signed root there may lie on the cone. The element $\tfrac{1}{\sqrt2}(e_1+ie_2)$ is the witness on both: it is a root of $+1$ in $\mathrm{SPS}$, a root of $-1$ in $\mathrm{SQS}$, and it has $C=0$, so it is a zero divisor of the algebra and not a unit.

## The Twelve Structures and the Three Values

The square of a structure is its operation read at the two equal arguments, so each of the twelve carries a root problem of its own, and the problem is decided by the sweep of that square. The four existence classes are the theorem of *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; at the three named values they read as follows.

**Theorem (the four existence classes of the twelve structures; quoted).** Among the twelve structures of the biquaternion complex space, a root of $-1$ and a root of $+1$ exist for the four bilateral structures $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$, $\mathrm{SQA}$ and for the two indefinite sesquilinear structures $\mathrm{GQS}$, $\mathrm{SQS}$, none exists for the two definite sesquilinear structures $\mathrm{GPS}$, $\mathrm{SPS}$ at $-1$ and none for the four antisymmetric structures $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$ at either signed value; and a root of $0$ exists for every one of the twelve.

**Corollary (the values that fail).** The value $-1$ has no root in the two definite sesquilinear structures, whose scalar part is non-negative, and the two signed values have no root in the four antisymmetric structures, whose square vanishes identically. Every failure of a named value is one of those two: the sign of the square, or the parity of the square.

*Proof.* The two definite sesquilinear squares take the non-negative values $H$ and $\lvert a\rvert^{2}$, so neither reaches $-1$; the four antisymmetric squares vanish, so neither reaches $-1$ nor $+1$; and for the remaining structures the witnesses are those of §*The Twelve Structures and the Three Values* below, read from the theorem quoted above.

The twelve are read one by one below; each names the product, the square and the three root sets, and cites the article that owns them. The four general rows are the four root problems of §*Results*.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\Xi\tilde Q$, and its square is the plain square $\tilde\Xi^{2}=\bigl(\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)\bigr)e_0+2\Xi_0\mathbf\Xi$; the vector part $2\Xi_0\mathbf\Xi$ vanishes when $\Xi_0=0$ or $\mathbf\Xi=0$, and the scalar part then gives the value.

**The roots of $-1$** are the pair of trivial roots $\pm i$, the real family $\pm\hat\mu$ of the pure real unit vectors, of real dimension two, and the complex quadric $(\mathbf\Xi,\mathbf\Xi)=1$ of the vector subspace, that is the four-parameter family $\mathbf p+i\mathbf p'$ with $\mathbf p,\mathbf p'$ real, $\mathbf p^{2}-\mathbf p'^{2}=1$ and $\mathbf p\cdot\mathbf p'=0$, which contains the real family; every root other than $\pm i$ is pure, hence lies in the vector subspace.

**The roots of $0$** are the origin together with the nilpotent cone $\{\Xi_0=0,\ \Xi_1^{2}+\Xi_2^{2}+\Xi_3^{2}=0\}$, of real dimension four, whose non-zero elements are the nilpotents of the algebra.

**The roots of $+1$** are the images $\tilde\Xi i$ of the roots of $-1$; they are the central pair $\pm e_0$ and the pure elements with $(\mathbf\Xi,\mathbf\Xi)=-1$.

The classification is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the roots of $0$ are *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\Xi\bullet\tilde Q=\tfrac12(\tilde\Xi\tilde Q+\tilde Q\tilde\Xi)$, and its square is the plain square, $\tilde\Xi\bullet\tilde\Xi=\tilde\Xi^{2}$, so the three root sets are exactly the three of $\mathrm{GPA}$.

**The zero-divisor reading of the roots is not the algebra's.** The pure roots of $-1$ and of $+1$ lie in the vector subspace, which is the zero-divisor set of the block, so those roots are zero divisors of $\mathrm{SPA}$ although they are units of the algebra; and the pure roots of $+1$ are in bijection with the non-trivial idempotents by $\mathbf u\mapsto\tfrac12(e_0+\mathbf u)$.

The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\Xi\wedge\tilde Q=\tfrac12(\tilde\Xi\tilde Q-\tilde Q\tilde\Xi)=\mathbf\Xi\times\mathbf Q$, the cross product of the two vector parts. It is alternating, so at the two equal arguments it vanishes, $\tilde\Xi\wedge\tilde\Xi=0$, and the three equations reduce to $0=-e_0$, $0=0$ and $0=+e_0$.

**There is no root of $-1$ and no root of $+1$**, the value $0$ alone being read by the vanishing square. **The roots of $0$** are every element of the space; the non-zero ones are at once the square-zero set, the nilpotent set and the zero-divisor set of the block, all three being the punctured space.

The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\Xi^{\natural}\tilde Q$, and its square is the central square, $\tilde\Xi^{\natural}\tilde\Xi=C(\tilde\Xi)e_0$, so the three root problems are the three level sets of the one quadratic form $C$.

**The roots of $-1$** are the quadric $C=-1$, a nondegenerate complex quadric of real dimension six, containing the central pair $\pm i$, the imaginary vector roots $i\hat\mu$ over the real unit vectors, and the mixed family whose real and imaginary vector directions are the ones the plain product assigns to the opposite value.

**The roots of $0$** are the whole zero-divisor cone $\mathcal{C}=\{C=0\}$, of real dimension six, the union of the pure isotropic elements and the complex multiples of the non-trivial idempotents of the plain product.

**The roots of $+1$** are the quadric $C=+1$, of real dimension six, containing the central pair $\pm e_0$ and the real vector roots $\hat\mu$; the set is the image of the root set of $-1$ under the multiplication by $i$.

The article is *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $\tfrac12(\tilde\Xi^{\natural}\tilde Q+\tilde Q^{\natural}\tilde\Xi)=C(\tilde\Xi,\tilde Q)e_0$, the form read as a product, and its square is the central square, so the three root sets are the three level sets of $C$, the same three as the ones of $\mathrm{GQA}$: the quadric $C=-1$, containing the pair $\pm ie_0$; the isotropic cone $C=0$; and the quadric $C=+1$, containing the four basis elements.

**Two readings are the block's own.** The root set of $0$ is the isotropic cone of the form, which is the zero-divisor set of the parent algebra and not the block's own, the zero-divisor set of $\mathrm{SQA}$ being the whole punctured space. And the three root sets are pairwise disjoint, invariant under the three conjugations, and related by the scaling $\tilde\Xi\mapsto\mu\tilde\Xi$, which multiplies the value by $\mu^{2}$.

The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde\Xi\wedge^{\natural}\tilde Q=\tfrac12(\tilde\Xi^{\natural}\tilde Q-\tilde Q^{\natural}\tilde\Xi)$. It is alternating, $\tilde\Xi\wedge^{\natural}\tilde\Xi=0$, so there is no root of $-1$ and none of $+1$.

**The roots of $0$** are every element of the space; the non-zero ones are at once the square-zero set, the nilpotent set and the zero-divisor set of the block, all three being the punctured space.

The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra*.

### $\mathrm{GPS}$, the general plain sesqualgebra

The product is $\tilde\Xi\tilde Q^{*}$, and its square is the Hermitian element $\tilde\Xi\tilde\Xi^{*}$, whose scalar part is the definite sum $H(\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$.

**There is no root of $-1$**, the scalar part of $-e_0$ being negative while $H$ is non-negative. **The roots of $0$** are the origin alone, $H$ vanishing only there, so the owner counts no non-zero root of $0$.

**The roots of $+1$** are the unitary family $\{\tilde\Xi:\tilde\Xi\tilde\Xi^{*}=e_0\}$, which is the unitary group $U(2)$ of *The Unitary Group of the Biquaternion Algebra*, of real dimension four, described as the family $e^{i\theta}w$ over the real unit quaternions $w$; it contains $e_0$, $-e_0$ and the pure imaginary unit vectors $i\hat\mu$.

The article is *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra

The product is the symmetrisation $\tfrac12(\tilde\Xi\tilde Q^{*}+\overline{\tilde Q\tilde\Xi^{*}})$, central, and its square is $H(\tilde\Xi)e_0$, so the root problem is the single scalar equation $H=\lambda$.

**There is no root of $-1$** and **the root set of $0$ is the origin alone**, for the same definiteness. **The roots of $+1$** are the quadric $H=1$, that is the sphere $\sum_\mu\lvert\Xi_\mu\rvert^{2}=1$ in $\mathbb{C}^{4}$, of real dimension seven.

The symmetrisation keeps the existence class of its general partner and loses the rigidity of the root set: the root set of $+1$ grows from the group $U(2)$ to the sphere, the symmetrisation forgetting the vector part of the square.

The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra*.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra

The product is the antisymmetrisation $\tfrac12(\tilde\Xi\tilde Q^{*}-\overline{\tilde Q\tilde\Xi^{*}})$, whose values are pure vectors, so the square never takes a central value.

**There is no root of $-1$ and no root of $+1$**, the obstruction being the centrality of the value and not the vanishing of the square: it is a parity of the scalar part.

**The roots of $0$** are the non-zero elements whose square is central, that is the non-zero square-zero elements; they form the complex cone on the real unit sphere of the quaternion subspace, of real dimension five.

The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Sesqualgebra*.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra

The product is $\tilde\Xi^{\natural}\tilde Q^{*}$, and its square has scalar part the Krein value $\Delta(\tilde\Xi)=\lvert\Xi_0\rvert^{2}-\sum_k\lvert\Xi_k\rvert^{2}$, real for every element, so the value has a root exactly when it is real, and every real value has roots. For a real value the roots are the family

$$
\tilde\Xi=c(\hat\mu+it) , \qquad (t^{2}-1)\lvert c\rvert^{2}=\lambda ,
$$

of scalar part $ict$ and vector part $c\hat\mu$, over the real unit vectors $\hat\mu$, of real dimension four, together with the central circle $\lvert a\rvert^{2}=\lambda$ when the value is positive. The three named values are the three ranges of the slope $t$.

**The roots of $-1$** are the family at the slopes $\lvert t\rvert<1$, with $\lvert c\rvert^{2}=1/(1-t^{2})$; they contain $e_1,e_2,e_3$ and the real unit vectors $\hat\mu$.

**The roots of $0$** are the family at the slopes $\lvert t\rvert=1$, that is the square-zero family $c(\hat\mu\pm i)$; they contain the element $e_0+ie_1$.

**The roots of $+1$** are the family at the slopes $\lvert t\rvert>1$, with $\lvert c\rvert^{2}=1/(t^{2}-1)$, beside the central circle $\lvert a\rvert^{2}=1$; they contain $e_0$ and $i$.

The article is *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra*.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra

The product is the symmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde\Xi^{*}})$, and its square is the Hermitian part of the unsplit square.

**The roots of $-1$** are the disjoint union of the pure unit vectors, a real five-sphere, and the family $\mathcal R_{-1}$ of real dimension four.

**The roots of $0$** are the nilpotent cone $\alpha(e_0+i\hat\mu)$, of real dimension four, containing no pure element.

**The roots of $+1$** are the family $\mathcal R_{+1}$ with $\lvert\alpha\rvert\geq1$, of real dimension four, containing $e_0$. The three root sets are pairwise disjoint, and the idempotents $-\tfrac12e_0+\hat\mu$ lie on none of them.

The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Sesqualgebra*.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra

The product is the antisymmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde\Xi^{*}})$, whose values are pure vectors, so the square never takes a central value.

**There is no root of $-1$ and no root of $+1$**, for the parity of the value, the unit of the parent algebra being the witness: its square in the block is zero.

**The roots of $0$** are the non-zero elements whose vector part is a complex multiple of a real vector, a cone of real dimension six with free scalar coordinate and the vector part running over the complex multiples of the real directions; they split into the central family and the non-central family, and they are the square-zero elements of the block, hence its nilpotents of index two and a strict subset of its zero-divisor set.

The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Sesqualgebra*.

## Results

The three named values are the three level sets of the square, tabulated below over the twelve structures, proved for the four general products, read in coordinates and in the two families of the plain reduction.

### The Twelve Root Sets at the Three Values

Read against the empty set and against the whole space, the twelve root sets are

| the family | the structure | the square | the roots of $-1$ | the roots of $0$ | the roots of $+1$ |
|---|---|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde\Xi^{2}$ | the pair $\pm i$ and the pure families | the origin and the nilpotent cone, real dimension $4$ | the images $\tilde\Xi i$ of the roots of $-1$ |
| | $\mathrm{SPA}$ | $\tilde\Xi^{2}$ | the three sets of $\mathrm{GPA}$ | the three sets of $\mathrm{GPA}$ | the three sets of $\mathrm{GPA}$ |
| | $\mathrm{APA}$ | $0$ | none | the whole space | none |
| the quaternionic algebra | $\mathrm{GQA}$ | $C(\tilde\Xi)e_0$ | the quadric $C=-1$, real dimension $6$ | the cone $C=0$, real dimension $6$ | the quadric $C=+1$, real dimension $6$ |
| | $\mathrm{SQA}$ | $C(\tilde\Xi)e_0$ | the quadric $C=-1$ | the cone $C=0$ | the quadric $C=+1$ |
| | $\mathrm{AQA}$ | $0$ | none | the whole space | none |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\tilde\Xi\tilde\Xi^{*}$ | none | the origin alone | the unitary group $U(2)$, real dimension $4$ |
| | $\mathrm{SPS}$ | $H(\tilde\Xi)e_0$ | none | the origin alone | the sphere $H=1$, real dimension $7$ |
| | $\mathrm{APS}$ | the pure part of the square | none | the cone on the unit sphere of $\mathrm{Vect}(\mathbb{H})$, real dimension $5$ | none |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | the Krein value | the family at the slopes $\lvert t\rvert<1$, real dimension $4$ | the family at the slopes $\lvert t\rvert=1$, real dimension $4$ | the family at the slopes $\lvert t\rvert>1$ and the central circle, real dimension $4$ |
| | $\mathrm{SQS}$ | the Hermitian part of the square | the pure unit sphere and $\mathcal R_{-1}$ | the cone $\alpha(e_0+i\hat\mu)$, real dimension $4$ | $\mathcal R_{+1}$ with $\lvert\alpha\rvert\geq1$, real dimension $4$ |
| | $\mathrm{AQS}$ | the pure part of the square | none | the cone of the real directions, real dimension $6$ | none |

Two structures reduce the root set of $0$ to the origin alone, the two definite sesquilinear ones, whose square is a definite form; the four antisymmetric structures have no square to read, so under them the value $0$ is reached by everything when the square vanishes identically and by a pair of cones otherwise; and the remaining six carry the cone of their square, the nilpotent cone of the plain family, of real dimension four, the whole cone $C=0$ of the quaternionic family, of real dimension six, and the square-zero families of the two indefinite sesquilinear ones, of real dimension four. The table is proved section by section in §*The Twelve Structures and the Three Values*, and §*The Four General Products at the Three Values* and §*The Three Values in Coordinates and the Roots of Zero* read its consequences.

### The Four General Products at the Three Values

**Theorem (the four general products at the three values).** At the value $-1$ three of the four general products have roots, $\mathrm{GPA}$, $\mathrm{GQA}$ and $\mathrm{GQS}$, and the general plain sesqualgebra $\mathrm{GPS}$ has none. At the value $0$ all four have roots. At the value $+1$ all four have roots. The four root sets are pairwise different at each of the three values.

*Proof.* The plain product has the three families of its classification, the natural product the quadric $C=-1$, and the fourth product the family at the slopes $\lvert t\rvert<1$: three non-empty sets, pairwise distinct. The general plain sesqualgebra is excluded at $-1$ because the scalar part of its square is the non-negative $H$. At the value $0$ the four sets are the nilpotent cone of the plain product, of real dimension four, the whole cone of the natural product, of real dimension six, the origin alone for the general plain sesqualgebra, and the square-zero family of the fourth product: four distinct sets. At the value $+1$ they are the images of the plain roots of $-1$ by $i$, the quadric $C=+1$, the unitary group $U(2)$ of real dimension four, and the family at the slopes $\lvert t\rvert>1$ with the central circle: four distinct sets.

| product | the roots of $-1$ | the roots of $0$ | the roots of $+1$ |
|---|---|---|---|
| $\mathrm{GPA}$, $\tilde\Xi\tilde Q$ | the pair $\pm i$ and the two pure families | the nilpotent cone, real dimension $4$ | the images by $i$ of the roots of $-1$ |
| $\mathrm{GQA}$, $\tilde\Xi^{\natural}\tilde Q$ | the quadric $C=-1$ | the cone $C=0$ | the quadric $C=+1$ |
| $\mathrm{GPS}$, $\tilde\Xi\tilde Q^{*}$ | none | the origin alone | the unitary group $U(2)$ |
| $\mathrm{GQS}$, $\tilde\Xi^{\natural}\tilde Q^{*}$ | the family at $\lvert t\rvert<1$ | the family at $\lvert t\rvert=1$ | the family at $\lvert t\rvert>1$ and the central circle |

The four rows are four different answers, and that is the theorem. **The word is *differ*, not *coincide*.** The zero-divisor sets of §*The Four General Products Coincide* of *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* are one set read four times, because the four general products read the same norm; the root sets are not, because the square of a product is not the norm of a product. The four squares are the plain square, the central square, the Hermitian square and the Krein square, and they differ in the sign of the vector part and in the presence of the conjugation; the three named values are exactly the values at which the four differences are visible, the sign showing at $-1$ and $+1$ and the conjugation showing at $0$.

### The Three Values in Coordinates and the Roots of Zero

Written on the coordinates, the three values are the three equations of the squares, one per family:

| the family | the equation of the root of $\lambda$ |
|---|---|
| the plain algebra | $\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)=\lambda$ with $2\Xi_0\mathbf\Xi=0$ |
| the quaternionic algebra | $C(\tilde\Xi)=\lambda$ |
| the plain sesqualgebra | $H(\tilde\Xi)=\lambda$, that is $\sum_\mu\lvert\Xi_\mu\rvert^{2}=\lambda$ |
| the quaternionic sesqualgebra | $\Delta(\tilde\Xi)=\lambda$, that is $\sum_\mu\varepsilon_\mu\lvert\Xi_\mu\rvert^{2}=\lambda$ with $\varepsilon=(1,-1,-1,-1)$ |
| the four antisymmetric structures | $0=\lambda e_0$ |

**Proposition (the root set of $0$ is the cone, and the root sets of the two signed values carry no apex).** The set $\mathcal R_0$ is a complex cone whose apex is the origin: a complex multiple of a root of $0$ is again a root of $0$. For the two quaternionic families the apex is the only singular point of $\mathcal R_0$: the set is the cone $C=0$, of real dimension six, for the algebra, and the cone $\alpha(e_0+i\hat\mu)$, of real dimension four, for the sesqualgebra, which is a proper subcone of the Krein cone $\Delta=0$. The sets $\mathcal R_{-1}$ and $\mathcal R_{+1}$ carry no apex: a scaling by $\mu$ carries the value $\lambda$ to $\mu^{2}\lambda$ or to $\lvert\mu\rvert^{2}\lambda$, so no non-zero multiple of a root of $\lambda$ is again a root of $\lambda$ unless $\mu^{2}=1$ or $\lvert\mu\rvert^{2}=1$.

*Proof.* The square of a scaled element is $\mu^{2}(\tilde\Xi\star\tilde\Xi)$ for the six bilinear structures and $\lvert\mu\rvert^{2}(\tilde\Xi\star\tilde\Xi)$ for the six sesquilinear ones, so the vanishing of the square is preserved by every $\mu$ while the value $\lambda$ is preserved only by the $\mu$ with $\mu^{2}=1$ or $\lvert\mu\rvert^{2}=1$. The gradient of $C$ is proportional to $(\Xi_0,\Xi_1,\Xi_2,\Xi_3)$ and vanishes at the origin alone, so the cone $C=0$ is smooth away from its apex; the cone $\alpha(e_0+i\hat\mu)$ is the cone on the real unit sphere of the vector subspace, which meets the scalar line only at the origin, so it is smooth away from the apex as well, and it is a proper part of the Krein cone because the vanishing of the whole square is stronger than the vanishing of its scalar part.

The dimension count reads the table of §*The Twelve Root Sets at the Three Values*: the cone of the natural product is of real dimension six and its two level sets are of the same dimension, the nilpotent cone of the plain product is of real dimension four, the cone of the antisymmetric plain sesqualgebra is of real dimension five, and the cones of the two quaternionic sesquilinear structures $\mathrm{GQS}$ and $\mathrm{SQS}$ are of real dimension four.

### The Two Families

The plain reduction cuts the space into two families, and the root sets respect the cut.

**Definition.** An element is **pure** when its scalar part vanishes, $\Xi_0=0$, and **central** when its vector part vanishes, $\mathbf\Xi=0$.

The reduction of the plain square is the vanishing of the vector part, $2\Xi_0\mathbf\Xi=0$, and the two factors give the two families: the pure one, on which the reduction is satisfied identically, and the central one, on which it forces the vector part to vanish.

| | pure, $\Xi_0=0$ | central, $\Xi_0\neq0$ |
|---|---|---|
| the reduction $2\Xi_0\mathbf\Xi=0$ | satisfied identically | forces $\mathbf\Xi=0$ |
| the roots of $0$ | the nilpotent cone $(\mathbf\Xi,\mathbf\Xi)=0$, real dimension $4$ | the origin alone |
| the roots of $-1$ | the pure families of the value $-1$ | the pair $\pm i$ |
| the roots of $+1$ | the pure family $(\mathbf\Xi,\mathbf\Xi)=-1$ | the pair $\pm e_0$ |
| the dimension | $6$ | $2$ |

The non-zero roots of $0$ lie in the pure family alone, and the roots of the two signed values have one central pair together with their pure part. The square of a pure element is the central element $-(\mathbf\Xi,\mathbf\Xi)e_0$, a multiple of $e_0$, so the pure square never vanishes except on the nilpotent cone, and the vanishing of a root of $0$ is carried by the pair of equations and not by the element alone. The two families are the scalar line and the vector subspace of *Introduction to the Remarkable Subspaces*.

## The Inverse Equations

At the three values the inverse equations are read on the roots. Of the two general products only the plain one has a two-sided unit, so the classical equivalence *a root of a non-zero value if and only if a unit* is available for it alone, and there it is exact; the substitute for the other three is the one-sided criterion, whose four tables of solutions are *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The One-Sided Inverse Equations*, quoted and not restated. The three named values then read as follows.

**Theorem (the inverse equations at the three values).** Let $\star$ be one of the four general products. A root of $-1$ or of $+1$ has a solution of each of the two equations

$$
\tilde\Xi\star\tilde X=e_0 , \qquad \tilde X\star\tilde\Xi=e_0 ,
$$

the solution being the inverse $\tilde\Xi^{-1}=\tilde\Xi^{\natural}/C(\tilde\Xi)$ for the plain product and one of the conjugated inverses of the table for the other three. A root of $0$ has no solution on either side, the non-zero one because it lies on the cone and the origin because the left member vanishes there.

*Proof.* A root of a non-zero central value has $C(\tilde\Xi)\neq0$ by §*The Roots of $\pm1$ Are Units and the Non-Zero Roots of $0$ Are Zero Divisors*, and the criterion of invertibility is the non-vanishing of the central square; the solutions are those of the table. A non-zero root of $0$ has $C=0$ and lies in the cone, and the elements of the cone are exactly the elements that admit an annihilating factor on one side (*Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The origin has no solution either, the equation $\tilde\Xi\star\tilde X=e_0$ reading $0=e_0$ there.

So the two signed values are the values at which the roots are units, and the value $0$ is the value at which the roots are the zero divisors: for the four general products the three named values are the two ends of the invertibility criterion of the algebra, read on the square, with the two exceptions of §*The Roots of $\pm1$ Are Units and the Non-Zero Roots of $0$ Are Zero Divisors* outside them.

## Summary

The root of the central value $\lambda e_0$ in a structure is the solution of the equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$, and the three values that carry a name are $-1$, $0$ and $+1$. The root set of $0$ is a complex cone with the origin as its apex, the root sets of $-1$ and of $+1$ are the affine level sets of the square and carry no apex, and the central square places every root: a root of $-1$ or of $+1$ is a unit of the algebra and a non-zero root of $0$ is a zero divisor, for each of the four general products, the two symmetric sesquilinear structures lying outside that reading (§*The Roots of $\pm1$ Are Units and the Non-Zero Roots of $0$ Are Zero Divisors*).

The plain product reduces to the pair $\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)=\lambda$, $2\Xi_0\mathbf\Xi=0$: its roots of $-1$ are the pair $\pm i$ and the two pure families, its roots of $0$ are the origin together with the nilpotent cone of real dimension four, and its roots of $+1$ are the images of the roots of $-1$ by $i$. The natural product reads the one equation $C(\tilde\Xi)=\lambda$: the quadric $C=-1$, the whole cone $C=0$ and the quadric $C=+1$, each of real dimension six. The general plain sesqualgebra has no root of $-1$, the origin alone as its root of $0$ and the unitary group $U(2)$ as its roots of $+1$, and the general quaternionic sesqualgebra has the three slope families of the Krein square, of real dimension four each.

Among the twelve structures the four bilateral ones $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$, $\mathrm{SQA}$ and the two indefinite sesquilinear ones $\mathrm{GQS}$, $\mathrm{SQS}$ have a root of each of the three values; the two definite sesquilinear ones $\mathrm{GPS}$, $\mathrm{SPS}$ refuse $-1$, their scalar part being non-negative, and keep $0$ and $+1$; and the four antisymmetric ones $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$ have no root of either signed value, their square vanishing or being pure, and read the value $0$ alone, the whole space for the two alternating ones. The symmetrisation keeps the existence class of its general partner and loses the rigidity of the root set, the root of $+1$ growing from the group $U(2)$ to the sphere of $\mathbb{C}^{4}$. The roots of $-1$ of the plain product are the parameter set of the idempotents, read through the map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi i)$, and the non-zero roots of $0$ are the nilpotents of the algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_0$ | a central value, $\lambda\in\mathbb{C}$ |
| $-1$, $0$, $+1$ | the three named central values |
| $\mathcal R_\lambda$ | the root set of the value $\lambda$, the solutions of $\tilde\Xi\star\tilde\Xi=\lambda e_0$ |
| $C(\tilde\Xi)e_0 = \tilde\Xi^{\natural}\tilde\Xi = \tilde\Xi\tilde\Xi^{\natural}$ | the central square, with $C(\tilde\Xi)=\sum_\mu\Xi_\mu^{2}$ |
| $H(\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$ | the Hermitian square, the scalar part of the third product's square |
| $\Delta(\tilde\Xi)=\lvert\Xi_0\rvert^{2}-\sum_k\lvert\Xi_k\rvert^{2}$ | the Krein value, the scalar part of the fourth product's square |
| $\hat\mu$ | the real unit vectors, the real part of the pure roots of $-1$ |
| $\mathbb{B}^{\times}$, $\mathcal{C}=\{C=0\}$ | the group of units of the algebra, the elements off the cone, and the cone, their complement |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space, the four general products and their eight parts |

## Further Reading

- *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), the companion of this article, for the root problem at a general central value, the four existence classes of the twelve structures and the theorem that a root of a non-zero value is a unit.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the classification of the three values in the plain product, quoted here.
- *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/idempotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`) and *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the idempotents, which are the roots of $-1$ read through the halving map.
- *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/nilpotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the square-zero sets, which are the roots of $0$.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the cone, which is the root set of $0$ of the natural product and whose non-zero part is the zero-divisor set of the four general products, and for the table of the one-sided inverse equations.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve names, the three letters of each and the class of each.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the four general products and their eight symmetric and antisymmetric parts.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the tabulation of the four root problems and the four squares.
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the unitary family, which is the root set of $+1$ of the general plain sesqualgebra.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the non-negative scalar part $H$ and the sphere of the third family.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the Krein value and the square-zero family of the fourth product.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the pure value of the antisymmetric plain sesqualgebra and its cone of square-zero elements.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the criterion $C\neq0$ with which the roots are classified as units or zero divisors.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the scalar line and the vector subspace, the two families of the plain reduction.
