# __Zero Divisors__

## Introduction

Let $\star$ be a product on the biquaternion algebra $\mathbb{B}$. A nonzero $\tilde Q\in\mathbb{B}$ is a **zero divisor of $\star$** when it kills a nonzero partner: when $\tilde Q\star\tilde X=0$ or $\tilde X\star\tilde Q=0$ for some nonzero $\tilde X$. The first case makes it a left zero divisor, the second a right zero divisor, and an element of both kinds a two-sided zero divisor.

**The twelve names.** The algebra carries twelve products, so the generic definition poses twelve questions; this article answers them once for all twelve. Each of the twelve products has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the first slot, $\mathrm P$ plain and $\mathrm Q$ quaternionic; the third is the family, $\mathrm A$ the algebra over $\mathbb{C}$ and $\mathrm S$ the sesqualgebra over $\mathbb{C}$. The twelve are read in the four families of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** The general vocabulary, the zero divisor, the annihilator, the idempotent and the nilpotent stated once for a general product, is *Definitions for the Study of the 12 Algebraic Structures*. The plain-product criterion and the classification of the cone's elements are *Zero Divisors of the General Plain Algebra*. The four general products and their eight parts are *The 12 Products of the Biquaternion Complex Space* and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, whose three-letter code is used throughout. The eight criteria of the derived structures stay owned by their articles, cited one by one in §*The Twelve Structures and the Cone*. The property table and the four unit entries are *Comparison Between the Four General Products*; the four idempotent sets are *Idempotents*; the four root problems are *Square Roots of Minus One, Zero and Plus One* and *Square Roots of a General Element*; the annihilators of one element are *Annihilators*, and the square-zero sets are *Nilpotents*.

## The Zero-Divisor Cone

**Definition.** The **zero-divisor cone** is the vanishing set of the norm,

$$
\mathcal{C}=\{\tilde Q\in\mathbb{B}:\mathrm{Norm}(\tilde Q)=0\} ,
$$

the **generic norm** of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*, after *Conventions in Mathematics* §*The form convention and the norm convention*, the norm of the statement at hand. This article instantiates it by the reduced norm, $\mathrm{Norm}(\tilde Q)=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$. It is the common zero-divisor set of the four general products.

**Definition.** A subset of $\mathbb{B}$ is a **complex cone** when it contains $\lambda\tilde Q$ for every $\tilde Q$ it contains and every $\lambda\in\mathbb{C}$. Its **apex** is the origin.

### The Cone Is the Complement of the Group of Units

The elements of $\mathbb{B}$ fall into three classes. The invertible elements of the plain product, the units, are exactly those of non-vanishing norm, $\mathbb{B}^{\times}=\{\tilde Q:\mathrm{Norm}(\tilde Q)\neq0\}$ (*Zero Divisors of the General Plain Algebra*); the origin is never a zero divisor; and the remaining elements are the zero divisors of the four general products. Hence

$$
\mathbb{B}=\{0\}\cup\mathbb{B}^{\times}\cup\bigl(\mathcal{C}\setminus\{0\}\bigr) .
$$

So an element is a unit exactly when it lies off the cone, and a zero divisor exactly when it lies on the cone and not at the apex. The cone is the complement of the group of units, together with the origin.

## The Twelve Structures and the Cone

The four general products split into the twelve structures through the class-preserving exchange (*The 12 Products of the Biquaternion Complex Space*). A zero divisor names its product, so each of the twelve carries a zero-divisor set of its own; the table of §*Results* records them, one family to a block and, inside a block, the general structure first, the product written by its defining formula.

**Theorem (the cone is the mark of the four general products).** Among the twelve structures the zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$ exactly for the four general structures $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, and for no other. The eight derived sets are strictly larger: the six antisymmetric and scalar-valued symmetric structures $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$, $\mathrm{SQA}$ and $\mathrm{SPS}$ have the whole punctured space, and the two remaining symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$.

The twelve structures are read one by one below; each names the product, its zero-divisor set and the reason. The four general rows are read together in §*Results*.

**Corollary (the cone is the common core).** The punctured cone $\mathcal{C}\setminus\{0\}$ is contained in the zero-divisor set of each of the twelve structures, and it is equal to the set of exactly four of them, the four general products.

*Proof.* Every row of the table of §*Results* contains the cone: the four general rows equal it, the rows of $\mathrm{SPA}$ and $\mathrm{SQS}$ contain it by their second clause, and the remaining six rows are the whole punctured space.

Two consequences follow. First, because the cone lies in every set, an element of vanishing norm admits an annihilating factor in all twelve products, and the cone is the largest subset on which the twelve agree; the converse fails, since the derived sets are strictly larger. Second, the ring-theoretic picture breaks on the derived structures: the unit $e_1$, whose norm is $1$, is a zero divisor of $\mathrm{SPA}$ and of $\mathrm{SQS}$, because $e_1\bullet e_2=\tfrac12(e_1e_2+e_2e_1)=0$ for the Jordan product and $e_1\star e_2=0$ for the symmetric quaternionic sesquilinear product, and it is invertible in the algebra. A zero divisor need not be a non-unit unless the product has a two-sided unit.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde P\tilde Q$, its conjugate is $\tilde P^{\natural}$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q) .
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the scalar of the central element $\tilde P^{\natural}\tilde P$. Write $\tilde P=P_0e_0+\mathbf P$ with $\mathbf P=P_1e_1+P_2e_2+P_3e_3$ and $\tilde P^{\natural}=P_0e_0-\mathbf P$. Since $e_ke_l+e_le_k=0$ for $k\neq l$ and $e_k^{2}=-e_0$, the vector part squares to $\mathbf P^{2}=-(P_1^{2}+P_2^{2}+P_3^{2})e_0$, so

$$
\tilde P^{\natural}\tilde P=(P_0e_0-\mathbf P)(P_0e_0+\mathbf P)=P_0^{2}e_0-\mathbf P^{2}=(P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2})e_0 ,
$$

and its scalar is the norm $\mathrm{Norm}(\tilde P)=P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2}$.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The cone is the vanishing set of the norm, $\mathcal{C}=\{\tilde P:P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2}=0\}$, one complex quadric in the four coordinates, of complex dimension three. On $\mathcal{C}$ the product $\tilde P\tilde P^{\natural}$ vanishes with $\tilde P^{\natural}\neq0$, so every nonzero element of the cone is a zero divisor; off $\mathcal{C}$ the norm is nonzero and $\tilde P^{-1}=\tilde P^{\natural}/\mathrm{Norm}(\tilde P)$ is a two-sided inverse.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, the symmetrisation of the plain product, so its form is the same,

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q) ,
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the reduced norm $\mathrm{Norm}(\tilde P)=P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2}$ of §*The General Plain Algebra (GPA)*.

**The zero-divisor set is the enlarged set**

$$
\bigl(\{P_0=0\}\cup\mathcal{C}\bigr)\setminus\{0\} .
$$

Read the Jordan product from the quaternion table, $\tilde P\circ\tilde Q=P_0Q_0e_0+P_0\mathbf Q+Q_0\mathbf P-(\mathbf P,\mathbf Q)e_0$. If $P_0\neq0$ the vector part forces $\mathbf Q=-(Q_0/P_0)\mathbf P$, and the scalar part becomes $Q_0\,\mathrm{Norm}(\tilde P)/P_0$; a nonzero annihilator therefore exists exactly when $\mathrm{Norm}(\tilde P)=0$, and it is then $\tilde P^{\natural}$. If $P_0=0$ and $\tilde P\neq0$, any nonzero $\mathbf Q$ orthogonal to $\mathbf P$ annihilates.

The plane $P_0=0$ of the pure elements is a second family beside the cone.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$. It is alternating, so at the two equal arguments it vanishes, $\tilde P\star\tilde P=\tfrac12(\tilde P\tilde P-\tilde P\tilde P)=0$; there is no form there and no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** Every nonzero element is annihilated by itself.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde P^{\natural}\tilde Q$, its conjugate is $\tilde P^{\natural}$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q) .
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the scalar of the central element $\tilde P^{\natural}\tilde P$ of §*The General Plain Algebra (GPA)*, $\mathrm{Norm}(\tilde P)=P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2}$; the natural conjugation sends $\mathbf P$ to $-\mathbf P$, so $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$. Here the norm is the criterion.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The cone is the quadric $\mathcal{C}$ of §*The General Plain Algebra (GPA)*. If $\mathrm{Norm}(\tilde P)=0$ the partner $\tilde Q=\tilde P^{\natural}$ annihilates, since $\tilde P^{\natural}\tilde P^{\natural}=\mathrm{Norm}(\tilde P^{\natural})e_0=0$; conversely, multiplying $\tilde P^{\natural}\tilde Q=0$ on the left by $\tilde P$ gives $\mathrm{Norm}(\tilde P)\tilde Q=0$.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$, central, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q) ,
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the reduced norm $\mathrm{Norm}(\tilde P)=P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2}$.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** The value is the central read of the form, $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)e_0$; check on $\tilde P=\tilde Q=e_1$: $\tilde P^{\natural}\tilde P=e_0$, of scalar $1=0+1$. The form is nondegenerate, its matrix being the identity in the four coordinates, so for $\tilde P\neq0$ the equation $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=0$ is one complex linear equation in the four components of $\tilde Q$ and its solutions fill a complex hyperplane of nonzero vectors.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$. It is alternating, $\tilde P\star\tilde P=\tfrac12(\tilde P^{\natural}\tilde P-\tilde P^{\natural}\tilde P)=0$, so at the two equal arguments there is no form and no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** Every nonzero element is annihilated by itself.

### $\mathrm{GPS}$, the general plain sesqualgebra

The product is $\tilde P\tilde Q^{*}$, its conjugate is $\tilde P^{*}$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q}) .
$$

The norm is the form at the two equal arguments, $H(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P\tilde P^{*})=|P_0|^{2}+|\mathbf P|^{2}$, definite.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The definite norm $H$ vanishes at the origin alone and cuts no cone. Put $\tilde Q=\tilde Y^{*}$; then $\tilde P\tilde Q^{*}=\tilde P\tilde Y$ is the plain product, whose form is $\mathrm{Sc}(\tilde P^{\natural}\tilde Y)$ and whose scalar at the two equal arguments is the reduced norm $\mathrm{Norm}(\tilde P)=P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2}$ of §*The General Plain Algebra (GPA)*. The criterion is therefore $\mathrm{Norm}(\tilde P)=0$, the witness is $\tilde Q=(\tilde P^{\natural})^{*}$, since $\tilde P\tilde Q^{*}=\tilde P\tilde P^{\natural}=\mathrm{Norm}(\tilde P)e_0=0$ on the cone.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra

The product is $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$, central, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q}) ,
$$

The norm is the form at the two equal arguments, $H(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)=|P_0|^{2}+|\mathbf P|^{2}$, definite.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** The value is the central read of the form, $\mathrm{Sc}(\tilde P\tilde Q^{*})e_0$. The norm $H$ is definite and does not decide; the equation $\mathrm{Sc}(\tilde P\tilde Q^{*})=0$ is one complex linear equation in the conjugated components of $\tilde Q$, and its solutions fill a complex hyperplane.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra

The product is $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})=\mathrm{Vect}(\tilde P\tilde Q^{*})$. At the two equal arguments it gives the vector part of $\tilde P\tilde P^{*}$, not a scalar; there is no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** Off the cone, $\mathrm{Norm}(\tilde P)\neq0$ and $\tilde Q=(\tilde P^{-1})^{*}$ gives $\tilde P\tilde Q^{*}=e_0$, whose vector part is zero; on the cone, $\tilde Q=\tilde P^{\natural}$ gives $\tilde P\tilde Q^{*}=0$. Every nonzero element is a zero divisor.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra

The product is $\tilde P^{\natural}\tilde Q^{*}$, its conjugates are $\natural$ and $*$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q}) .
$$

The norm is the form at the two equal arguments, $K(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P^{\natural}\tilde P^{*})=|P_0|^{2}-|\mathbf P|^{2}$, indefinite.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The indefinite norm $K$ vanishes on a real cone of its own, distinct from $\mathcal{C}$. Put $\tilde Q=\tilde Y^{*}$; then $\tilde P^{\natural}\tilde Q^{*}=\tilde P^{\natural}\tilde Y$ is the plain product of $\tilde P^{\natural}$, whose form is $\mathrm{Sc}(\tilde P\tilde Y)$ and whose scalar at the two equal arguments is $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$ of §*The General Plain Algebra (GPA)*. The criterion is therefore $\mathrm{Norm}(\tilde P)=0$, the witness is $\tilde Q=(\tilde P^{\natural})^{*}$.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra

The product is $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$, central, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q}) ,
$$

The norm is the form at the two equal arguments, $K(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)=|P_0|^{2}-|\mathbf P|^{2}$, indefinite.

**The zero-divisor set is the enlarged set $\left(\{P_0=0\}\cup\mathcal{C}\right)\setminus\{0\}$.** Put $\tilde Y=\tilde Q^{*}$; the two conjugations commute and the product becomes the Jordan product of $\tilde P^{\natural}$ with $\tilde Y$,

$$
\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})=\tfrac12(\tilde P^{\natural}\tilde Y+\tilde Y\tilde P^{\natural}).
$$

By §*The Symmetric Plain Algebra (SPA)* the criterion is read on $\tilde P^{\natural}$: the natural conjugation leaves $P_0$ unchanged and $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$, so the condition is $P_0=0$ or $P_0^{2}+P_1^{2}+P_2^{2}+P_3^{2}=0$, (*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*).

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra

The product is $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})=\mathbf P\times\overline{\mathbf Q}$. At the two equal arguments it gives $\mathbf P\times\overline{\mathbf P}$, a pure vector; there is no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** If $\mathbf P\neq0$, take $\tilde Q=\overline{\tilde P}$: its vector part $\overline{\mathbf P}$ is parallel to $\mathbf P$, and a cross product of parallel vectors vanishes. If $\mathbf P=0$ the element is central and the product vanishes for every $\tilde Q$. Every nonzero element is a zero divisor.

## Results

The four general products share one zero-divisor set, the punctured cone $\mathcal{C}\setminus\{0\}$ of §*The Zero-Divisor Cone*. The twelve structures are tabulated against it, the four that coincide are separated out, and the cone itself is read in coordinates and in its two families.

### The Twelve Zero-Divisor Sets

Read against the cone $\mathcal{C}$ and against the whole space, the twelve sets are

| family | structure | the product | the zero-divisor set |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde P\tilde Q$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SPA}$ | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $(\{P_0=0\}\cup\mathcal{C})\setminus\{0\}$ |
| | $\mathrm{APA}$ | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\tilde P^{\natural}\tilde Q$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| | $\mathrm{AQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\tilde P\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SPS}$ | $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |
| | $\mathrm{APS}$ | $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\tilde P^{\natural}\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $(\{P_0=0\}\cup\mathcal{C})\setminus\{0\}$ |
| | $\mathrm{AQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |

The four general products have one and the same set, the punctured cone. The six structures $\mathrm{APA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ and $\mathrm{AQS}$ have the whole punctured space. The two remaining symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$. The cone is therefore the zero-divisor set of exactly four of the twelve structures, and it is contained in all twelve, so that it is the common core of the twelve. The theorem below and §*The Twelve Structures and the Cone* prove the table, and the sections that follow read its consequences.

### The Four General Products Coincide

**Theorem (the four zero-divisor sets coincide, and they are the cone).** For the four general products the zero-divisor sets coincide. A nonzero element $\tilde P$ is a left, a right or a two-sided zero divisor of one of the four general products exactly when $\mathrm{Norm}(\tilde P)=0$, that is exactly when $\tilde P$ lies on the cone $\mathcal{C}$, and then it is a zero divisor of all four, on both sides. In symbols,

$$
\{\tilde P\neq0:\tilde P\text{ admits an annihilating factor in }\star\}=\mathcal{C}\setminus\{0\} \qquad\text{for each of the four general products }\star .
$$

*Proof.* Read each product in the model $\mathsf{M}_2$. Each general product is the plain product with a conjugation in one or both slots, a bijection of $\mathbb{B}$; a bijection in a slot identifies the kernel of the left multiplication by $\tilde P$ with the kernel of the plain left multiplication by $\tilde P$ or by $\tilde P^{\natural}$. Now $\mathsf{M}_2(\tilde P^{\natural})$ is $\mathsf{M}_2(\tilde P)$ up to conjugation by a fixed invertible matrix, and $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$, so the plain left multiplication is singular exactly when $\mathrm{Norm}(\tilde P)=0$. In each case the deciding condition is the vanishing of the norm, read from the singularity of $\mathsf{M}_2(\tilde P)$ or of its conjugate $\mathsf{M}_2(\tilde P^{\natural})$. For the cone itself and for a nonzero $\tilde P$ with $\mathrm{Norm}(\tilde P)=0$, the witness is the natural conjugate, $\tilde P\tilde P^{\natural}=\tilde P^{\natural}\tilde P=\mathrm{Norm}(\tilde P)e_0=0$, on both sides.

The four conditions are thus one condition, and the reason is structural. Each general product is the plain product with a conjugation in one or both slots; each conjugation is a bijection that either fixes or conjugates the norm; and the norm is the single invariant that decides the invertibility of the element. Composing a one-sided multiplication with a bijection changes its kernel by the bijection, so the singularity is transported from product to product.

| product | left condition | right condition | the set |
|---|---|---|---|
| $\mathrm{GPA}$, $\tilde P\tilde Q$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GQA}$, $\tilde P^{\natural}\tilde Q$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GPS}$, $\tilde P\tilde Q^{*}$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GQS}$, $\tilde P^{\natural}\tilde Q^{*}$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |

The four rows are identical, and that is the theorem. **The word is *coincide*, not *independent*.** The zero divisor is defined by an equation that names a product, so the notion belongs to the product and the four products are four definitions, not one. What the theorem says is that in the biquaternion algebra the four definitions select one and the same subset of $\mathbb{B}$; it does not say that they must, and it does not extend to the eight derived structures of §*The Twelve Structures and the Cone*.

### The Cone in Coordinates and Its Apex

Written on the coordinates, the cone common to the four general products is one complex equation in the four complex coordinates,

$$
Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}=0 .
$$

**Proposition (the cone and its singular point).** The set $\mathcal{C}$ is a complex cone with apex at the origin, and the origin is its only singular point. Away from the apex it is a complex manifold of complex dimension three, hence a real manifold of real dimension six.

*Proof.* The norm is homogeneous of degree two, $\mathrm{Norm}(\lambda\tilde Q)=\lambda^{2}\mathrm{Norm}(\tilde Q)$, so its vanishing set is a cone. One complex equation in four complex unknowns cuts a complex hypersurface of $\mathbb{C}^{4}$, of complex dimension three wherever its gradient does not vanish; the gradient of $\mathrm{Norm}$ is proportional to $(Q_0,Q_1,Q_2,Q_3)$, which vanishes only at the origin, so the complement of the apex is smooth of complex dimension three. The origin is singular because the only term of $\mathrm{Norm}$ of degree two is the leading term, so the tangent cone at the origin is $\mathcal{C}$ itself and not a hyperplane.

### The Two Families

The scalar part cuts the cone into two families, and the criterion and the square read differently on each.

**Definition.** An element is **pure** when its scalar part vanishes, $Q_0=0$, and **non-pure** when $Q_0\neq0$.

On a pure element the scalar square $Q_0^{2}$ drops out of the criterion, which becomes $(\mathbf Q,\mathbf Q)=0$; on a non-pure element the criterion is the full vanishing of the norm.

| | pure, $Q_0=0$ | non-pure, $Q_0\neq0$ |
|---|---|---|
| criterion | $(\mathbf Q,\mathbf Q)=0$ | $\mathrm{Norm}(\tilde Q)=0$ |
| square in the plain product | $\tilde Q^{2}=0$ | $\tilde Q^{2}=2Q_0\tilde Q$ |
| structure | the nilpotents | the complex multiples of the nontrivial idempotents |
| real dimension | $4$ | $6$ |

The square of a pure zero divisor vanishes because $\tilde Q^{2}=-(Q_1^{2}+Q_2^{2}+Q_3^{2})e_0=0$; the square of a non-pure one satisfies $\tilde Q^{2}=2Q_0\tilde Q-\mathrm{Norm}(\tilde Q)e_0=2Q_0\tilde Q$, and the element $\tilde\Pi=\tilde Q/(2Q_0)$ is then a nontrivial idempotent of the plain product. The two families are read in the remarkable subspaces in *Introduction to the Remarkable Subspaces*: the pure ones fill the nilpotent cone of the vector subspace, the non-pure ones the double cones of the two Hermitian subspaces, and a generic point of the cone lies in none of the remarkable subspaces.

## The One-Sided Inverse Equations

Only the plain product has a two-sided unit, so the classical equivalence *zero divisor if and only if not a unit* is available for it alone, and there it is exact: for a nonzero $\tilde P$ the statements *$\tilde P$ is a zero divisor of the plain product*, *$\mathrm{Norm}(\tilde P)=0$* and *$\tilde P$ is not invertible* are equivalent (*Zero Divisors of the General Plain Algebra*). The substitute for the other three products is the one-sided inverse criterion.

**Theorem (the inverse equations).** Let $\star$ be one of the four general products and let $\tilde P\neq0$. Then $\tilde P$ is a zero divisor of $\star$ exactly when neither of the two equations

$$
\tilde P\star\tilde X=e_0 , \qquad \tilde X\star\tilde P=e_0
$$

has a solution; equivalently, both have a solution exactly when $\mathrm{Norm}(\tilde P)\neq0$.

*Proof.* If $\tilde P\star\tilde X=e_0$ holds, then in the model the equation is $\mathsf{M}_2(\tilde P)M=\mathrm{I}_2$ or $\mathsf{M}_2(\tilde P^{\natural})M=\mathrm{I}_2$ for an invertible $M$, so $\mathsf{M}_2(\tilde P)$ is invertible and $\mathrm{Norm}(\tilde P)\neq0$. Conversely, if $\mathrm{Norm}(\tilde P)\neq0$ then $\tilde P$ is invertible and the four solutions are those of the table below.

The solutions are written with the inverse $\tilde P^{-1}=\tilde P^{\natural}/\mathrm{Norm}(\tilde P)$ of the algebra, which exists for $\mathrm{Norm}(\tilde P)\neq0$. The two conjugations commute, ${}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural}=\overline{\cdot}$, so the order of the two superscripts in the last row is immaterial.

| product | $\tilde X$ with $\tilde P\star\tilde X=e_0$ | $\tilde X$ with $\tilde X\star\tilde P=e_0$ |
|---|---|---|
| $\tilde P\tilde Q$ | $\tilde P^{-1}$ | $\tilde P^{-1}$ |
| $\tilde P^{\natural}\tilde Q$ | $(\tilde P^{-1})^{\natural}$ | $(\tilde P^{-1})^{\natural}$ |
| $\tilde P\tilde Q^{*}$ | $(\tilde P^{-1})^{*}$ | $(\tilde P^{-1})^{*}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $(\tilde P^{-1})^{\natural*}$ | $(\tilde P^{-1})^{\natural*}$ |

This criterion uses the fixed element $e_0$, invariant under both conjugations, and makes no appeal to a unit of the product; it reads the same in the four products, and it says that the zero divisors are exactly the elements that cannot be inverted on either side.

## Summary

A zero divisor is defined by an equation that names a product, so the twelve products of the biquaternion algebra define twelve zero-divisor sets. For the four general products the sets coincide: for each of them, and for a nonzero element, being a left zero divisor, being a right zero divisor and lying on the cone are the same condition, the cone being the vanishing set of the norm $\mathrm{Norm}(\tilde Q)=\sum_\mu Q_\mu^{2}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)$ of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

The common set is the zero-divisor set $\mathcal{C}\setminus\{0\}$, a complex cone with apex at the origin, smooth away from the apex, of complex dimension three and real dimension six, whose nonzero members are the rank-one elements of the matrix model and whose left ideals are the minimal left ideals. Its complement is the group of units together with the origin, and it splits by the scalar part into the pure family of the nilpotents, of real dimension four, and the non-pure family of the complex multiples of the nontrivial idempotents, which fills the cone in real dimension six.

The annihilators of a fixed element of the cone, two complex planes per product, are *Annihilators*; the square-zero sets are *Nilpotents*. The cone is the zero-divisor set of the four general products alone: the four antisymmetric structures and the two scalar-valued symmetric structures $\mathrm{SQA}$ and $\mathrm{SPS}$ have the whole punctured space, and $\mathrm{SPA}$ and $\mathrm{SQS}$ have $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$. The cone is contained in all twelve sets and is the largest subset on which they agree. What a product does not change is the detection of the units: an element off the cone is invertible, and the one-sided inverse equations replace the classical equivalence for the three products that have no two-sided unit.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | one of the twelve products of $\mathbb{B}$; the four general products in the theorems |
| $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | the four general products |
| $\mathrm{Form}(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | the general quaternionic bilinear form, the polar form of the norm |
| $\mathrm{Norm}(\tilde Q)$ | the norm of the statement, written where a statement holds for all four norms; this article instantiates it by the reduced norm, $\mathrm{Norm}(\tilde Q)=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$ |
| $\mathrm{Norm}(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the reduced norm, the general quaternionic bilinear algebraic norm, the scalar of the central square $\tilde Q\tilde Q^{\natural}=\mathrm{Norm}(\tilde Q)e_0$ |
| $\mathcal{C}=\{\tilde Q:\mathrm{Norm}(\tilde Q)=0\}$ | the zero-divisor cone, of complex dimension three and real dimension six |
| $\mathcal{C}\setminus\{0\}$ | the zero-divisor set of the four general products |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, where the central square lies |
| pure, non-pure | scalar part zero, scalar part nonzero |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\tilde P^{-1}=\tilde P^{\natural}/\mathrm{Norm}(\tilde P)$ | the inverse of an element with $\mathrm{Norm}(\tilde P)\neq0$ |
| $(\mathbf P,\mathbf Q)$ | the general plain bilinear dot product of the two vector parts |
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ | the general plain bilinear form, whose isotropic cone is not $\mathcal{C}$ |
| $H(\tilde P)=\mathrm{Sc}(\tilde P\tilde P^{*})$ | the general plain sesquilinear algebraic norm, definite |
| $K(\tilde P)=\mathrm{Sc}(\tilde P^{\natural}\tilde P^{*})$ | the general quaternionic sesquilinear algebraic norm, indefinite |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space: the four general products and their eight symmetric and antisymmetric parts |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general vocabulary: the zero divisor, the annihilator, the idempotent, the nilpotent and the rest, each stated once for a general product.
- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the form $N$ and the four algebraic norms read at the two equal arguments.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the plain-product criterion, the classification of the cone's elements and the parametrisation of the pure family.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the four idempotent sets, the four square-root problems and the four unit entries.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the four general products and their symmetric and antisymmetric parts.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve names, the three letters of each and the class of each.
- *Idempotents* (`articles_maths/idempotents.md`), for the four idempotent sets of the four general products and their reading among the twelve.
- *Square Roots of Minus One, Zero and Plus One* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one.md`) and *Square Roots of a General Element* (`articles_maths/square-roots-of-a-general-element.md`), for the four root problems.
- *Annihilators* (`articles_maths/annihilators.md`), for the two one-sided annihilators of one element of the cone and their relation by the conjugations.
- *Nilpotents* (`articles_maths/nilpotents.md`), for the four square-zero sets and the twelve square-zero readings.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism and the singular matrices.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the general plain bilinear form and its isotropic cone.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the subspaces, the pure cone and the non-pure families.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra.md`), for the criterion $Q_0=0$ or $\mathrm{Norm}(\tilde Q)=0$ of the enlarged set of $\mathrm{SPA}$.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the same criterion of the enlarged set of $\mathrm{SQS}$ and its two families.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`) and *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the two scalar-valued symmetric structures whose zero-divisor set is the whole punctured space.
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra.md`), *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), *Zero Divisors of the Antisymmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-sesqualgebra.md`) and *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the four alternating structures whose zero-divisor set is the whole punctured space.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the natural product's criterion and the coincidence of its two annihilators.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the equation $\overline{\tilde P}\tilde P=0$ and its two halves.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the definiteness of the general plain sesquilinear square.
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra.md`), for the minimal left ideals of the rank-one elements.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra.md`), for the isotropic cones of the two bilinear forms, which are not the cone $\mathcal{C}$.
- *The Topology of the Zero-Divisor Cone* (`articles_maths/the-topology-of-the-zero-divisor-cone.md`), for the cone as a topological space.
