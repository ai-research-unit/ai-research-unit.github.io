# __Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space__

## Introduction

Let $\star$ be a product on the biquaternion algebra $\mathbb{B}$. An element $\tilde\Xi$ is a **root of the central value** $\lambda e_t$ when its square in that product is the value,

$$
\tilde\Xi\star\tilde\Xi=\lambda e_t , \qquad \lambda\in\mathbb{C},
$$

and the **root set** of the value is the set of the solutions of the equation. This article reads the value $0$ structure by structure in the twelve structures of the space, and then reads the nilpotents, which are the non-zero roots of $0$ of the structures whose index of nilpotency is two. The value $0$ is the only value every structure reaches, so its root set is the presence common to the twelve; the other two values that carry a name, $+1$ and $-1$, are read by the companion *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the general value with the four existence classes of the twelve structures is *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The general vocabulary — the root of a central value, the nilpotent and the square-zero element stated once for a general product — is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The twelve names.** The space carries twelve products, the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra* and their eight symmetric and antisymmetric parts (*Symmetric and Antisymmetric Decomposition of the Four General Products*). Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first slot is read through the natural conjugation; the third is the family, $\mathrm A$ the algebra over $\mathbb{C}$ and $\mathrm S$ the sesqualgebra, whose second slot carries the Hermitian conjugation. The twelve are read in the four families and the three operations of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,

| the operation | the plain algebra | the plain sesqualgebra | the quaternionic algebra | the quaternionic sesqualgebra |
|---|---|---|---|---|
| the general | $\mathrm{GPA}$ | $\mathrm{GPS}$ | $\mathrm{GQA}$ | $\mathrm{GQS}$ |
| the symmetric | $\mathrm{SPA}$ | $\mathrm{SPS}$ | $\mathrm{SQA}$ | $\mathrm{SQS}$ |
| the antisymmetric | $\mathrm{APA}$ | $\mathrm{APS}$ | $\mathrm{AQA}$ | $\mathrm{AQS}$ |

and every table of the article follows the new order: the four general structures first, then their four symmetric parts, then their four antisymmetric parts; and inside each group the plain algebra, then the plain sesqualgebra, then the quaternionic algebra, then the quaternionic sesqualgebra.

## The Roots of Zero

**Definition (the root of a central value; quoted).** Let $\star$ be a product on $\mathbb{B}$, let $\lambda\in\mathbb{C}$ and let $\tilde\Xi\in\mathbb{B}$. The element is a **root of $\lambda e_t$ of $\star$** when $\tilde\Xi\star\tilde\Xi=\lambda e_t$, and the **root set** of the value is the set of the solutions (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*Powers, the Square and the Roots*). The definition names its product, and every statement below names the product it reads.

### The Four Sets of the Four General Products

The value $0$ is reached by the square of a structure exactly when the square of the element vanishes, so the root set of $0$ of a structure is the set of the elements whose square in it vanishes. On the four general products the four sets are four different pieces of the space, and no one of them is empty.

**Theorem (the four square-zero sets).** Write $Z_1$, $Z_2$, $Z_3$, $Z_4$ for the root sets of $0$ of the plain, the natural, the general plain sesquilinear and the general quaternionic sesquilinear product. Then

$$
\boxed{\;
Z_1=\{\tilde Q:Q_t=0,\ (\vec Q,\vec Q)=0\} , \qquad Z_2=\mathcal{N} , \qquad Z_3=\{0\} , \qquad Z_4=\{\tilde Q:\overline{\tilde Q}\tilde Q=0\}
\;},
$$

and $Z_1$ is the **pure isotropic cone**, of real dimension four; $Z_2$ is the whole cone, of real dimension six; $Z_3$ is the origin alone; and $Z_4$ is a proper subfamily of the cone, of real dimension four, containing the non-zero element $e_t+i\vec e_x$.

*Proof.* The plain square has central coefficient $Q_t^{2}-(\vec Q,\vec Q)$ and vector coefficient $2Q_t\vec Q$, and the two must vanish separately: $Q_t\vec Q=0$ gives $Q_t=0$ or $\vec Q=0$, and $\vec Q=0$ forces $Q_t=0$, so $Q_t=0$ and $(\vec Q,\vec Q)=0$, the pure isotropic cone (*N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*). The natural square is $C(\tilde Q)e_t$, whose vanishing is the cone $\mathcal{N}$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The general plain sesquilinear square has scalar part $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$, a sum of squares of moduli, which vanishes only at the origin. The general quaternionic sesquilinear square is $\tilde Q^{\natural}\tilde Q^{*}$, and the equation $\overline{\tilde Q}\tilde Q=0$ is the same equation read through the coefficientwise conjugation; its solutions form a proper subfamily of the cone, the element $e_t+i\vec e_x$ being a non-zero solution, and the element $ie_t+\vec e_x+\vec e_y+i\vec e_z$ lying in the cone and not in the set (*The Square of the General Quaternionic Sesquilinear Product and the Two Halves*).

The four solutions are of four kinds. $Z_3$ is a single point, the smallest root set of the table. $Z_1$ is the pure part of the cone, the component on which the scalar part vanishes. $Z_4$ is a family of the same real dimension as $Z_1$ and a different set, meeting $Z_1$ at the origin alone. $Z_2$ is the largest of the four: it is the cone itself, the zero-divisor set of the algebra read with its apex, and the three others are proper subfamilies of it.

### Self-Annihilation

The equation of the root of $0$ is the equation of the self-annihilator, so the root set of $0$ of a product is the set of the elements that annihilate themselves in it.

**Corollary (self-annihilation).** For each of the four general products the root set of $0$ is the set of the elements that lie in their own annihilator,

$$
\boxed{\;
\tilde Q\star\tilde Q=0 \iff \tilde Q\in A_\star(\tilde Q) \iff \tilde Q\in B_\star(\tilde Q)
\;},
$$

the annihilator being read in the same product, on the left and on the right (*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The converse that fails is the one of the cone: for the natural product every element of the cone lies in its own annihilator, while for the fourth product the element $ie_t+\vec e_x+\vec e_y+i\vec e_z$ lies in the cone and not in the set.

### The Order of the Four Sets

**Theorem (the order of the sets).** With $Z_1$, $Z_2$, $Z_3$, $Z_4$ the four root sets of $0$ of the general products,

$$
\boxed{\;
Z_3=\{0\}\subsetneq Z_1\subsetneq Z_2 , \qquad Z_3\subsetneq Z_4\subsetneq Z_2 , \qquad Z_1\cap Z_4=\{0\}
\;},
$$

so that $Z_1$ and $Z_4$ are incomparable and the four sets are ordered only by the two chains through the whole cone $Z_2$.

*Proof.* The inclusions $Z_1\subseteq Z_2$ and $Z_4\subseteq Z_2$ are the theorem above, and both are strict: the element $e_t+i\vec e_x$ lies in the cone and not in the pure isotropic cone, while $ie_t+\vec e_x+\vec e_y+i\vec e_z$ lies in the cone and not in $Z_4$. The two sets $Z_1$ and $Z_4$ are non-empty beyond the origin, the elements $\vec e_x+i\vec e_y$ and $e_t+i\vec e_x$ being witnesses of the two, and their intersection is the origin because a pure element of $Z_1$ has vanishing scalar part while a non-zero element of $Z_4$ has a non-vanishing one.

The order is the whole of the comparison of the four sets: one set is the smallest, one is the largest, and the two whose real dimension is four are the incomparable pair. The two sets of real dimension four are therefore two different proper subfamilies of the cone, incomparable with each other, and a reader who identifies the square-zero elements with the cone forgets $Z_1$ and $Z_4$ both.

### The Root Set of Zero Is a Cone

**Proposition (the root set of $0$ is a cone).** Let $\star$ be one of the twelve products. The root set of $0$ is a complex cone whose apex is the origin: a complex multiple of a root of $0$ is again a root of $0$. For the two structures of a definite square the cone is the origin alone, and for the four structures of a vanishing square it is the whole space (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*).

*Proof.* The square of a scaled element is read from the bilinearity of the products: $\mu\tilde\Xi\star\mu\tilde\Xi=\mu^{2}(\tilde\Xi\star\tilde\Xi)$ for the six bilinear structures and $\lvert\mu\rvert^{2}(\tilde\Xi\star\tilde\Xi)$ for the six sesquilinear ones. At the value $0$ the scalar factor disappears, so the property of being a root of $0$ is invariant under every scaling; and the apex is the origin because the square's vanishing set is homogeneous.

The cone is the reason the value $0$ is the only value whose root set is invariant under the scaling of §*The Scaling of the Cone*, and the reason the root set of $0$ is the only root set the scaling does not move. The two definite sesquilinear structures are the only ones whose cone is a point, and the four antisymmetric structures the only ones whose cone is the space.

### The Non-Zero Roots of Zero Are the Zero Divisors

**Theorem (the non-zero roots of zero are the zero divisors; quoted).** A non-zero root of $0$ of a general product is a zero divisor of the algebra, and the two-sided, the left and the right conditions coincide there: the non-zero roots of $0$ of the four general products lie in the punctured cone, $\mathcal R_0\setminus\{0\}\subseteq\mathcal{N}$ (*Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Roots Are Units, or Zero Divisors*). Neither equation $\tilde\Xi\star\tilde Q_1=e_t$ nor $\tilde Q_1\star\tilde\Xi=e_t$ has a solution at a root of $0$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The One-Sided Inverse Equations*).

The value $0$ is therefore the value at which the roots of the plain product stop being invertible: the inverse $\tilde\Xi^{\natural}/C(\tilde\Xi)$ of §*The Inverse Equations at One* of the companion *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* has the vanishing central square in its denominator, and the vanishing of $C$ is the criterion of *N-Regularity and Degeneracy in the Biquaternion Algebra*. The theorem is quoted for the four general products; outside them the two symmetric sesquilinear structures keep a root of $0$ at the origin alone, and the four antisymmetric structures reach no central value other than $0$, with a square that vanishes identically for the two bilinear ones and cuts a proper subfamily for the two sesquilinear ones.

## The Twelve Structures and the Roots of Zero

The twelve root sets of $0$ are read one by one, each quoted from the article that owns it. The product, the square and the root set are named for each, and the two structures with the same square have the same root set.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\Xi\tilde Q_2$, and its square is the plain square. The root set of $0$ is the pure isotropic cone $\{Q_t=0,\ (\vec Q,\vec Q)=0\}$, of real dimension four, the component of the cone singled out by the vanishing of the scalar part; its non-zero members are the nilpotents of the algebra, and they are a strict part of its zero-divisor set, the cone beyond the pure part being made of the complex multiples of the non-trivial idempotents. The article is *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*.

### $\mathrm{GPS}$, the general plain sesqualgebra

The product is $\tilde\Xi\tilde Q_2^{*}$, and its square is the Hermitian element $\tilde\Xi\tilde\Xi^{*}$, of scalar part $\langle\tilde\Xi\rangle_{*}=\sum_\mu\lvert\Xi_\mu\rvert^{2}$. The equation of the value $0$ forces every coordinate to vanish, so the root set of $0$ is the origin alone; the zero-divisor set of the structure is the whole punctured space, so the square detects no zero divisor there at all. The article is *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\Xi^{\natural}\tilde Q_2$, and its square is the central square $C(\tilde\Xi)e_t$; the equation of the value $0$ is the vanishing of the central square, and the root set of $0$ is the whole cone $\mathcal{N}$, of real dimension six, which is also the whole zero-divisor set of the algebra together with the origin. The article is *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra

The product is $\tilde\Xi^{\natural}\tilde Q_2^{*}$, and its square has scalar part the Krein value $\Delta(\tilde\Xi)$. The equation of the value $0$ is the square-zero family $c(\vec u\pm i)$ over the real unit vectors, the slope family at $\lvert t\rvert=1$, a proper subfamily of the cone cut out by $\overline{\tilde Q}\tilde Q=0$; it is of real dimension four and contains the element $e_t+i\vec e_x$. The article is *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\Xi\bullet\tilde Q_2=\tfrac12(\tilde\Xi\tilde Q_2+\tilde Q_2\tilde\Xi)$, whose square is the plain square, so the root set of $0$ is the pure isotropic cone, element for element that of $\mathrm{GPA}$. The zero-divisor set of the structure is larger than that of $\mathrm{GPA}$, so the square detects the cone only in part there. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra

The product is the symmetrisation $\tfrac12(\tilde\Xi\tilde Q_2^{*}+\overline{\tilde Q_2\tilde\Xi^{*}})$, whose value is central, and its square is $\langle\tilde\Xi\rangle_{*}e_t$, a real and non-negative central value. The root set of $0$ is the origin alone, for the same definiteness. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde\Xi)=C(\tilde\Xi,\tilde Q_2)e_t$, whose value is central, and its square is the central square; the root set of $0$ is the whole cone, as for $\mathrm{GQA}$. The zero-divisor set of the structure is the whole punctured space, so the square detects only the cone there. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra

The product is the symmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q_2^{*}+\overline{\tilde Q_2^{\natural}\tilde\Xi^{*}})$, and its square is the coefficientwise real part of the unsplit square, a real element. The root set of $0$ is the cone $\alpha(e_t+\tilde\Xi)$ over the real unit vectors, the same subfamily of the cone as that of $\mathrm{GQS}$, of real dimension four, containing no pure element. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\Xi\wedge\tilde Q_2=\vec\Xi\times\vec Q_2$, alternating, so its square vanishes identically. The root set of $0$ is the whole space and every element is a root of $0$; the zero-divisor set is the punctured space, so the two coincide on the non-zero elements. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra

The product is the antisymmetrisation $\tfrac12(\tilde\Xi\tilde Q_2^{*}-\overline{\tilde Q_2\tilde\Xi^{*}})$, whose values are pure elements, so the square of an element is the pure part of its Hermitian square; the equation of the value $0$ is the centrality of the Hermitian square, $\tilde Q\tilde Q^{*}$ central, and the root set of $0$ is the subfamily the centrality cuts out, a complex cone on the real unit sphere of the quaternion subspace, of real dimension five. It is not inside the cone: it contains the unit $e_t$, which lies off the cone, and the cone meets it at the origin alone. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde\Xi\wedge^{\natural}\tilde Q_2=\tfrac12(\tilde\Xi^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde\Xi)$, alternating, so its square vanishes identically. The root set of $0$ is the whole space, the punctured space being the zero-divisor set. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra

The product is the antisymmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q_2^{*}-\overline{\tilde Q_2^{\natural}\tilde\Xi^{*}})$, whose values are pure elements; the equation of the value $0$ is the vanishing of the coefficientwise imaginary part of the Hermitian square, and the root set of $0$ is the set of the elements whose vector part is a complex multiple of a real direction, a cone of real dimension six with a free scalar coordinate. It is not inside the cone and it meets the cone: it contains the unit $e_t$, which lies off the cone, and the element $e_t+i\vec e_x$, which lies on it. The article is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Nilpotents

The nilpotent is the root of $0$ read as an element of the element theory, and the class the twelve structures compare is the class of index two.

**Definition (the nilpotent of a product; quoted).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,

$$
\tilde\Upsilon\star\tilde\Upsilon\star\cdots\star\tilde\Upsilon=0 ,
$$

the least such $k$ being the **index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, a **square-zero element of $\star$** (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Nilpotent*). The origin is a nilpotent, the trivial one, and the article is concerned with the others.

### The Twelve Square-Zero Sets

The root set of $0$ of a structure is the set of its square-zero elements, the origin included, so the comparison of the twelve root sets of $0$ of §*The Twelve Structures and the Roots of Zero* is the comparison of the twelve square-zero sets.

**Theorem (the twelve square-zero sets).** Among the twelve structures the square-zero set is the pure isotropic cone for $\mathrm{GPA}$ and $\mathrm{SPA}$; the origin alone for $\mathrm{GPS}$ and $\mathrm{SPS}$; the whole cone $\mathcal{N}$ for $\mathrm{GQA}$ and $\mathrm{SQA}$; the proper subfamily $\overline{\tilde Q}\tilde Q=0$ of the cone for $\mathrm{GQS}$ and $\mathrm{SQS}$; the subfamily the centrality of the Hermitian square cuts out for $\mathrm{APS}$; the subfamily the vanishing of its coefficientwise imaginary part cuts out for $\mathrm{AQS}$; and the whole space for $\mathrm{APA}$ and $\mathrm{AQA}$.

*Proof.* The plain square is that of §*The Four Sets of the Four General Products* for $\mathrm{SPA}$, and the central square for $\mathrm{SQA}$, so the two symmetric bilinear structures inherit the sets of their general partners. For the sesquilinear pairs the symmetric parts are the central forms, so their square-zero sets are those of the general structures at the two equal arguments, which is *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* for the fourth product. The two alternating structures are the whole space by definition, and the two definite sesquilinear structures are the origin alone by the definiteness of their scalar part.

The twelve sets read the ways a square operator can be too large, too small, or outside the cone. The two alternating squares are the whole space, because they vanish identically; the two **central** squares are the whole cone, because the central square is the vanishing of the norm; the two **plain** squares are the pure isotropic cone, one component of the cone singled out by the vanishing of the scalar part. The two **fourth** squares are a proper subfamily of the cone, cut out by the one-sided equation $\overline{\tilde Q}\tilde Q=0$, and the two **symmetric sesquilinear** squares are the origin alone, their scalar part being definite. The two **antisymmetric sesquilinear** squares are the two sets that lie outside the cone, the centrality of the Hermitian square for one, the vanishing of its coefficientwise imaginary part for the other, and those two are the sets of §*The Twelve Structures and the Roots of Zero* that are neither inside the cone nor disjoint from it.

### Where the Square Detects the Zero Divisors

**Proposition (where the square detects the zero divisors).** The root set of $0$ of a structure and its zero-divisor set agree on the non-zero elements exactly for $\mathrm{APA}$, $\mathrm{AQA}$ and $\mathrm{GQA}$: for the two alternating structures, whose zero-divisor set is the whole punctured space and whose square vanishes identically, and for the natural product, whose square is the central square and whose zero-divisor set is the cone. Every other structure has a square-zero set strictly smaller than its zero-divisor set, and the four of them that carry a square of an antisymmetric sesquilinear structure or of a definite sesquilinear structure see their zero divisors in a part that either crosses the cone or misses it entirely (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*).

The remark is the sharpest form of the warning that the square is not the norm. The square-zero elements are the zero divisors the square can see, and the square sees all of them only when it vanishes identically or is the central square. The plain product sees its pure nilpotents and misses the complex multiples of its non-trivial idempotents; the general plain sesquilinear product and the general quaternionic sesquilinear product miss the cone entirely or in part; and the two structures of a definite square, whose square is the best behaved of the twelve, see none of the zero divisors they have.

## Results

The three tables below collect the root sets of $0$, the four sets of the general products and the twelve square-zero sets, and the scaling that leaves the cone in place.

### The Twelve Root Sets of Zero

| the family | the structure | the square | the root set of $0$ |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde\Xi^{2}$ | the pure isotropic cone $Q_t=0$, $(\vec Q,\vec Q)=0$, real dimension $4$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\tilde\Xi\tilde\Xi^{*}$ | the origin alone |
| the quaternionic algebra | $\mathrm{GQA}$ | $C(\tilde\Xi)e_t$ | the cone $\mathcal{N}$, real dimension $6$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | of scalar part $\Delta$ | the family $\overline{\tilde Q}\tilde Q=0$, real dimension $4$ |
| the plain algebra | $\mathrm{SPA}$ | $\tilde\Xi^{2}$ | the pure isotropic cone, the set of $\mathrm{GPA}$ |
| the plain sesqualgebra | $\mathrm{SPS}$ | $\langle\tilde\Xi\rangle_{*}e_t$ | the origin alone |
| the quaternionic algebra | $\mathrm{SQA}$ | $C(\tilde\Xi)e_t$ | the cone $\mathcal{N}$, real dimension $6$ |
| the quaternionic sesqualgebra | $\mathrm{SQS}$ | the coefficientwise real part | the cone $\alpha(e_t+\tilde\Xi)$, real dimension $4$ |
| the plain algebra | $\mathrm{APA}$ | $0$ | the whole space |
| the plain sesqualgebra | $\mathrm{APS}$ | a pure element | the elements with $\tilde Q\tilde Q^{*}$ central, real dimension $5$ |
| the quaternionic algebra | $\mathrm{AQA}$ | $0$ | the whole space |
| the quaternionic sesqualgebra | $\mathrm{AQS}$ | a pure element | the elements of real dimension $6$ whose vector part is a complex multiple of a real direction |

Read against the whole space, the table has three kinds of entry: the whole space for the two alternating structures, whose square vanishes; the origin alone for the two definite sesquilinear structures, whose square is definite; and a genuine cone in the other eight rows, the cone being the whole cone for the two central squares, its pure part for the two plain squares, the subfamily $\overline{\tilde Q}\tilde Q=0$ for the two fourth squares, and the two crossing subfamilies for the two antisymmetric sesquilinear squares.

### The Four General Products at Zero

| the product | the root set of $0$ | the real dimension | a witness |
|---|---|---|---|
| $\mathrm{GPA}$, $\tilde\Xi\tilde Q_2$ | the pure isotropic cone | $4$ | $\vec e_x+i\vec e_y$ |
| $\mathrm{GPS}$, $\tilde\Xi\tilde Q_2^{*}$ | the origin | $0$ | none |
| $\mathrm{GQA}$, $\tilde\Xi^{\natural}\tilde Q_2$ | the cone $\mathcal{N}$ | $6$ | $e_t+i\vec e_x$ |
| $\mathrm{GQS}$, $\tilde\Xi^{\natural}\tilde Q_2^{*}$ | the subfamily $\overline{\tilde Q}\tilde Q=0$ | $4$ | $e_t+i\vec e_x$ |

The four sets are ordered by the two chains of §*The Order of the Four Sets*, and no one of them is empty, which is the presence common to the twelve structures of the space: the value $0$ is the only value at which all twelve have a root.

### The Two Families of the Plain Reduction at Zero

The plain reduction $\Xi_t^{2}-(\vec\Xi,\vec\Xi)=\lambda$, $2\Xi_t\vec\Xi=0$ reads at the value $0$ as follows.

| | pure, $\Xi_t=0$ | central, $\Xi_t\neq0$ |
|---|---|---|
| the roots of $0$ | the pure isotropic cone $(\vec\Xi,\vec\Xi)=0$, the nilpotents | the origin alone |
| the real dimension | $4$ | $0$, the one point |

The two families are disjoint except at the shared origin, and both are needed for the table of the plain product: the nilpotent cone carries all the non-zero roots of $0$, and the central family contributes the origin alone. The two families are those of the companion *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, where they carry the root set of $+1$.

### The Scaling of the Cone

**Theorem (the scaling of the cone; quoted).** Let $\mu\in\mathbb{C}$ and let $\tilde\Xi$ be a root of $0$ of one of the twelve products. Then $\mu\tilde\Xi$ is a root of $0$ of the same product, so the root set of $0$ is a cone invariant under every scaling (*Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Scaling of the Root Set*). For a non-zero value the same scaling carries the value $\lambda$ to $\mu^{2}\lambda$ in the six bilinear structures and to $\lvert\mu\rvert^{2}\lambda$ in the six sesquilinear ones, so no non-zero multiple of a root of $\lambda$ is again a root of $\lambda$ unless $\mu^{2}=1$ or $\lvert\mu\rvert^{2}=1$; the value $0$ is the only value whose root set the scaling does not move.

## Summary

The root of the central value $\lambda e_t$ in a structure is the solution of the equation $\tilde\Xi\star\tilde\Xi=\lambda e_t$, and this article reads the value $0$, the only value every one of the twelve structures reaches. For the four general products the root sets of $0$ are four sets: the pure isotropic cone $Q_t=0$, $(\vec Q,\vec Q)=0$, of real dimension four, which is the nilpotent cone of the plain product; the origin alone for the general plain sesquilinear product, whose square has the definite scalar part $H$; the whole cone $\mathcal{N}=\{C=0\}$, of real dimension six, for the natural product; and the subfamily $\overline{\tilde Q}\tilde Q=0$ of the cone, of real dimension four, for the general quaternionic sesquilinear product. The four are ordered by $Z_3=\{0\}\subsetneq Z_1\subsetneq Z_2$ and $Z_3\subsetneq Z_4\subsetneq Z_2$, with $Z_1$ and $Z_4$ incomparable and meeting at the origin, and each is a complex cone with the origin as its apex.

Among the twelve structures the square-zero set is the pure isotropic cone for $\mathrm{GPA}$ and $\mathrm{SPA}$, the origin alone for $\mathrm{GPS}$ and $\mathrm{SPS}$, the whole cone for $\mathrm{GQA}$ and $\mathrm{SQA}$, the subfamily $\overline{\tilde Q}\tilde Q=0$ of the cone for $\mathrm{GQS}$ and $\mathrm{SQS}$, for the two antisymmetric sesquilinear structures two subfamilies, one each, that lie outside the cone: the elements whose Hermitian square is central for $\mathrm{APS}$, with the origin its only element of the cone, and the elements whose Hermitian square has vanishing coefficientwise imaginary part for $\mathrm{AQS}$, which contains the unit $e_t$ off the cone and the element $e_t+i\vec e_x$ on it, and the whole space for the two alternating structures $\mathrm{APA}$ and $\mathrm{AQA}$. The non-zero roots of $0$ are the zero divisors of the algebra, and the square detects the zero-divisor set whole only for the two alternating structures and the natural product.

The nilpotents are the non-zero square-zero elements, that is the nilpotents of index two. Self-annihilation, $\tilde Q\star\tilde Q=0$ exactly when $\tilde Q$ lies in its own annihilator, holds in each of the four general products; the converse that fails is the cone for the fourth product, the element $ie_t+\vec e_x+\vec e_y+i\vec e_z$ lying in the cone and not in the set. The root set of $0$ is the only root set the scaling does not move, and it is the cone of the square: the whole space where the square vanishes, the whole cone where the square is the central square, one component of the cone where the square is the plain square, and the origin alone where the square is definite.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_t$ | a central value, $\lambda\in\mathbb{C}$ |
| $\mathcal R_0$ | the root set of the value $0$, the solutions of $\tilde\Xi\star\tilde\Xi=0$ |
| $Z_1$, $Z_2$, $Z_3$, $Z_4$ | the root sets of $0$ of the plain, the natural, the general plain sesquilinear and the general quaternionic sesquilinear product |
| $\mathcal{N}=\{C(\tilde\Xi)=0\}$ | the cone, the vanishing set of the central square |
| $C(\tilde\Xi)e_t=\tilde\Xi^{\natural}\tilde\Xi$ | the central square, with $C(\tilde\Xi)=\sum_\mu\Xi_\mu^{2}$ |
| $\langle\tilde\Xi\rangle_{*}=\sum_\mu\lvert\Xi_\mu\rvert^{2}$ | the Hermitian square, the scalar part of the second product's square |
| $\Delta(\tilde\Xi)=\lvert\Xi_t\rvert^{2}-\sum_{\mu\in\{x,y,z\}}\lvert\Xi_\mu\rvert^{2}$ | the Krein value, the scalar part of the fourth product's square |
| $\tilde\Upsilon\star\tilde\Upsilon=0$, $\tilde\Upsilon\neq0$ | a square-zero element, or nilpotent of index two, of the product at hand |
| $A_\star(\tilde Q)$, $B_\star(\tilde Q)$ | the left and right annihilators of $\tilde Q$ in the product at hand |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space, the four general products and their eight parts |

## Further Reading

- [Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.html), the companion of this article, for the general value, the four existence classes and the theorem that a non-zero root of $0$ is a zero divisor.
- [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), the other companion, for the value $+1$, the idempotents and the inverse equations.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the root of a central value and the nilpotent of a product stated once for a general product.
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), and its siblings [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), *… of the Antisymmetric Plain Algebra*, *… of the General Quaternionic Algebra*, *… of the Symmetric Quaternionic Algebra*, *… of the Antisymmetric Quaternionic Algebra*, *… of the General Plain Sesqualgebra*, *… of the Symmetric Plain Sesqualgebra*, *… of the Antisymmetric Plain Sesqualgebra*, *… of the General Quaternionic Sesqualgebra*, *… of the Symmetric Quaternionic Sesqualgebra* and *… of the Antisymmetric Quaternionic Sesqualgebra* (the twelve files of `articles_maths/` whose names begin `square-roots-of-zero-and-the-nilpotents-of-the-`), for the square-zero set of each structure, quoted one by one.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html) and [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html), for the four general products, their eight parts and the twelve names.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the cone, the zero-divisor sets, the one-sided inverse equations and the theorem that the four general products have one zero-divisor set.
- [Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the two annihilators the self-annihilation corollary names.
- [The Square of the General Quaternionic Sesquilinear Product and the Two Halves](the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.html), for the scalar part $\Delta$ and the square-zero family of the fourth product.
- [The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra](the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.html), for the pure value of the antisymmetric plain sesqualgebra and its cone of square-zero elements.
- [N-Regularity and Degeneracy in the Biquaternion Algebra](n-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the criterion $C\neq0$ with which a root of $0$ is separated from a unit.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four squares read as norms and the vanishing sets that carry the cone.
