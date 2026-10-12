# __The Zero Divisors and the Twelve Structures__

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

**The answer.** The article turns on one set of the algebra, the **zero-divisor cone** $\mathcal{C}$ of §*The Zero-Divisor Cone*, the common zero-divisor set of the four general products. Read against $\mathcal{C}$ and against the whole space, the twelve sets are

| family | structure | the product | the zero-divisor set |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde P\tilde Q$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SPA}$ | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$ |
| | $\mathrm{APA}$ | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\tilde P^{\natural}\tilde Q$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| | $\mathrm{AQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\tilde P\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SPS}$ | $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |
| | $\mathrm{APS}$ | $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\tilde P^{\natural}\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ |
| | $\mathrm{SQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$ |
| | $\mathrm{AQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |

The four general products have one and the same set, the punctured cone. The six structures $\mathrm{APA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ and $\mathrm{AQS}$ have the whole punctured space. The two remaining symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$. The cone is therefore the zero-divisor set of exactly four of the twelve structures, and it is contained in all twelve, so that it is the common core of the twelve. The sections that follow prove the table and read its consequences.

**Scope and owners.** The general vocabulary, the zero divisor, the annihilator, the idempotent and the nilpotent stated once for a general product, is *Definitions for the Study of the 12 Algebraic Structures*. The plain-product criterion and the classification of the cone's elements are *Zero Divisors of the General Plain Algebra*. The four general products and their eight parts are *The 12 Products of the Biquaternion Complex Space* and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, whose three-letter code is used throughout. The eight criteria of the derived structures stay owned by their articles, cited one by one in §*The Twelve Structures and the Cone*. The property table, the four idempotent sets and the four one-sided inverse readings are *Comparison Between the Four General Products*, *The Idempotents of the Twelve Structures* and *The Square Roots of a Central Value in the Twelve Structures*.

## The Zero-Divisor Cone

### The Cone, Its Apex and Its Dimension

**Definition.** The **zero-divisor cone** is the vanishing set of the norm,

$$
\mathcal{C}=\{\tilde Q\in\mathbb{B}:\mathrm{Norm}(\tilde Q)=0\} ,
$$

the **generic norm** of §*The Algebra, Its Products and Its Norms*, instantiated in this article by the general quaternionic bilinear algebraic norm $N$. It is the common zero-divisor set of the four general products. Written on the coordinates, it is one complex equation in the four complex coordinates, $Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}=0$.

**Definition.** A subset of $\mathbb{B}$ is a **complex cone** when it contains $\lambda\tilde Q$ for every $\tilde Q$ it contains and every $\lambda\in\mathbb{C}$. Its **apex** is the origin.

**Proposition (the cone and its singular point).** The set $\mathcal{C}$ is a complex cone with apex at the origin, and the origin is its only singular point. Away from the apex it is a complex manifold of complex dimension three, hence a real manifold of real dimension six.

*Proof.* The norm is homogeneous of degree two, $\mathrm{Norm}(\lambda\tilde Q)=\lambda^{2}\mathrm{Norm}(\tilde Q)$, so its vanishing set is a cone. One complex equation in four complex unknowns cuts a complex hypersurface of $\mathbb{C}^{4}$, of complex dimension three wherever its gradient does not vanish; the gradient of $\mathrm{Norm}$ is proportional to $(Q_0,Q_1,Q_2,Q_3)$, which vanishes only at the origin, so the complement of the apex is smooth of complex dimension three. The origin is singular because the only term of $\mathrm{Norm}$ of degree two is the leading term, so the tangent cone at the origin is $\mathcal{C}$ itself and not a hyperplane.

The zero-divisor set of the four general products is the cone with its apex removed, $\mathcal{C}\setminus\{0\}$.

### The Cone and the Rank-One Elements

In the matrix model the cone is the set of singular matrices, and its nonzero members have rank exactly one.

**Proposition (the rank-one elements).** For $\tilde P\neq0$ the following are equivalent: $\tilde P$ lies on the cone, $\mathrm{Norm}(\tilde P)=0$; the matrix $\mathsf{M}_2(\tilde P)$ is singular; $\mathsf{M}_2(\tilde P)$ has rank one; and the left ideal $\mathbb{B}\tilde P$ is minimal, of complex dimension two.

*Proof.* A nonzero two-by-two matrix is singular exactly when it has rank one, and $\mathrm{Norm}(\tilde P)=\det\mathsf{M}_2(\tilde P)$ is its singularity. The left ideal generated by an element of rank one is the set of matrices whose image lies in the one-dimensional image of $\mathsf{M}_2(\tilde P)$, of complex dimension two, and no smaller nonzero left ideal is contained in it (*Ideals and Peirce Decomposition of the General Plain Algebra*).

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

### The Cone Is the Complement of the Group of Units

The elements of $\mathbb{B}$ fall into three classes. The invertible elements of the plain product, the units, are exactly those of non-vanishing norm, $\mathbb{B}^{\times}=\{\tilde Q:\mathrm{Norm}(\tilde Q)\neq0\}$ (*Zero Divisors of the General Plain Algebra*); the origin is never a zero divisor; and the remaining elements are the zero divisors of the four general products. Hence

$$
\mathbb{B}=\{0\}\cup\mathbb{B}^{\times}\cup\bigl(\mathcal{C}\setminus\{0\}\bigr) .
$$

So an element is a unit exactly when it lies off the cone, and a zero divisor exactly when it lies on the cone and not at the apex. The cone is the complement of the group of units, together with the origin.

## The Algebra, Its Products and Its Norms

**The algebra and its products.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_0=1$, $e_ke_l=-\delta_{kl}e_0+\epsilon_{klm}e_m$ and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$, with $Q_\mu\in\mathbb{C}$, scalar part $Q_0$ and vector part $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\overline{Q_0}e_0-\sum_k\overline{Q_k}e_k$; the two conjugations commute. The **four general products** are

$$
\tilde P\tilde Q , \qquad \tilde P^{\natural}\tilde Q , \qquad \tilde P\tilde Q^{*} , \qquad \tilde P^{\natural}\tilde Q^{*} ,
$$

named the **plain**, the **natural** or quaternionic, the **general plain sesquilinear** and the **general quaternionic sesquilinear** or **fourth** product, and abbreviated $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$.

**The four algebraic norms.** Each general product has an algebraic norm, its scalar part read on the two equal arguments. Writing $\varepsilon_0=1$ and $\varepsilon_k=-1$ for $k=1,2,3$, the four norms are

$$
B(\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2} , \qquad N(\tilde Q)=\sum_\mu Q_\mu^{2} , \qquad H(\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2} , \qquad K(\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2} ,
$$

the **general plain bilinear** norm $B$ of the plain product, the **general quaternionic bilinear** norm $N$ of the natural product, the **general plain sesquilinear** norm $H$ of the general plain sesquilinear product and the **Krein** norm $K$ of the general quaternionic sesquilinear product, all four of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. Each is homogeneous of degree two, $N(\lambda\tilde Q)=\lambda^{2}N(\tilde Q)$ for a complex $\lambda$. Only $N$ is multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, and it is the reduced norm of the algebra; the article writes $\mathrm{Norm}$ for the norm generically, after *Conventions in Mathematics* §*The form convention and the norm convention*, and $N$ for the general quaternionic bilinear algebraic norm, the norm this article reads the cone with; the letter $C(\tilde Q)$ of the sibling articles names the same scalar. The norms $B$, $H$, $K$ have their own vanishing sets and are not used below: $H$ vanishes only at the origin, and $B$ vanishes on the second cone of §*Boundary: the Two Cones*.

## The Criterion for One General Product

**Proposition (the norm and the conjugations).** For all $\tilde P,\tilde Q\in\mathbb{B}$ the norm is multiplicative for the plain product, it is unchanged by the natural conjugation and conjugated by the coefficientwise and the Hermitian conjugations:

$$
N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q) , \qquad N(\tilde P^{\natural})=N(\tilde P) , \qquad N(\overline{\tilde P})=\overline{N(\tilde P)} , \qquad N(\tilde P^{*})=\overline{N(\tilde P)} .
$$

*Proof.* In the matrix model $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, $N(\tilde Q)=\det\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_2$ is an isomorphism of $\mathbb{C}$-algebras, so the norm of a plain product is the product of the norms. The natural conjugation is an anti-automorphism, so it corresponds in the model to a transposition, and a matrix has the determinant of its transpose; the coefficientwise conjugation is entrywise, so it conjugates the determinant; the Hermitian conjugation is the composite of the two, hence it conjugates the determinant as well.

**The central square.** The norm is also the scalar of the plain product of an element with its natural conjugate,

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0 ,
$$

so that product is a multiple of the unit, hence an element of the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$; it is the **central square** of $\tilde Q$, and $N(\tilde Q)$ is its scalar value. The norm is the reduced norm of the algebra, and its non-vanishing is the invertibility criterion of the plain product: for a nonzero $\tilde P$ the element $\tilde P$ is invertible exactly when $N(\tilde P)\neq0$, with $\tilde P^{-1}=\tilde P^{\natural}/N(\tilde P)$ (*Zero Divisors of the General Plain Algebra*). The cone is equally the set where the central square vanishes, $\mathcal{C}=\{\tilde Q:\tilde Q\tilde Q^{\natural}=0\}$.

**Theorem (the criterion for a fixed product).** Let $\star$ be one of the four general products and let $\tilde P\neq0$. Then the following three conditions are equivalent:

1. $\tilde P$ is a left zero divisor of $\star$;
2. $\tilde P$ is a right zero divisor of $\star$;
3. $\mathrm{Norm}(\tilde P)=0$, that is $\tilde P\in\mathcal{C}$.

Moreover $A_\star(\tilde P)$ and $B_\star(\tilde P)$ are complex planes, of complex dimension two, exactly when $\mathrm{Norm}(\tilde P)=0$, and they are zero exactly when $\mathrm{Norm}(\tilde P)\neq0$.

*Proof.* Read $\star$ in the model. Each general product is the plain product with a conjugation in one or both slots, the map $\tilde X\mapsto\mathsf{M}_2(\tilde X)$ and the two conjugations are bijections of $\mathbb{B}$, and a bijection in a slot identifies the kernel of the left multiplication by $\tilde P$ in $\star$ with the kernel of the plain left multiplication by $\tilde P$ or by $\tilde P^{\natural}$. Now $\mathsf{M}_2(\tilde P^{\natural})=\mathsf{M}_2(\tilde P)$ up to conjugation by a fixed invertible matrix, and $N(\tilde P^{\natural})=N(\tilde P)$; the plain left multiplication by $\tilde P$ is singular exactly when $\det\mathsf{M}_2(\tilde P)=N(\tilde P)=0$, by the invertibility criterion of the plain product (*Zero Divisors of the General Plain Algebra*). A singular nonzero two-by-two matrix has rank one and kernel of dimension one over $\mathbb{C}$, and the kernel is zero when the matrix is invertible. The right multiplication is the same read on the transposed matrix, whose determinant is equal. The left, the right and the two-sided zero divisors of $\star$ are therefore one and the same set, the nonzero elements of the cone, $\mathcal{C}\setminus\{0\}$.

## The Four Zero-Divisor Sets Coincide

**Theorem (the four zero-divisor sets coincide, and they are the cone).** For the four general products the zero-divisor sets coincide. A nonzero element $\tilde P$ is a left, a right or a two-sided zero divisor of one of the four general products exactly when $N(\tilde P)=0$, that is exactly when $\tilde P$ lies on the cone $\mathcal{C}$, and then it is a zero divisor of all four, on both sides. In symbols,

$$
\{\tilde P\neq0:\tilde P\text{ admits an annihilating factor in }\star\}=\mathcal{C}\setminus\{0\} \qquad\text{for each of the four general products }\star .
$$

*Proof.* Apply the criterion of §*The Criterion for One General Product* to the four products in turn. In each case the deciding condition is the vanishing of the norm, read from the singularity of $\mathsf{M}_2(\tilde P)$ or of $\mathsf{M}_2(\tilde P^{\natural})$, whose determinants are equal. For the cone itself and for a nonzero $\tilde P$ with $N(\tilde P)=0$, the witness is the natural conjugate, $\tilde P\tilde P^{\natural}=\tilde P^{\natural}\tilde P=N(\tilde P)e_0=0$, on both sides.

The four conditions are thus one condition, and the reason is structural. Each general product is the plain product with a conjugation in one or both slots; each conjugation is a bijection that either fixes or conjugates the norm; and the norm is the single invariant that decides the invertibility of the element. Composing a one-sided multiplication with a bijection changes its kernel by the bijection, so the singularity is transported from product to product.

| product | left condition | right condition | the set |
|---|---|---|---|
| $\mathrm{GPA}$, $\tilde P\tilde Q$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GQA}$, $\tilde P^{\natural}\tilde Q$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GPS}$, $\tilde P\tilde Q^{*}$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GQS}$, $\tilde P^{\natural}\tilde Q^{*}$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |

The four rows are identical, and that is the theorem. **The word is *coincide*, not *independent*.** The zero divisor is defined by an equation that names a product, so the notion belongs to the product and the four products are four definitions, not one. What the theorem says is that in the biquaternion algebra the four definitions select one and the same subset of $\mathbb{B}$; it does not say that they must, and it does not extend to the eight derived structures of §*The Twelve Structures and the Cone*.

## The Twelve Structures and the Cone

The four general products split into the twelve structures through the class-preserving exchange (*The 12 Products of the Biquaternion Complex Space*). A zero divisor names its product, so each of the twelve carries a zero-divisor set of its own; the table of the introduction records them, one family to a block and, inside a block, the general structure first, the product written by its defining formula.

**Theorem (the cone is the mark of the four general products).** Among the twelve structures the zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$ exactly for the four general structures $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, and for no other. The eight derived sets are strictly larger: the six antisymmetric and scalar-valued symmetric structures $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$, $\mathrm{SQA}$ and $\mathrm{SPS}$ have the whole punctured space, and the two remaining symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$.

*Proof.* The four general rows are §*The Four Zero-Divisor Sets Coincide*. On the two antisymmetric bilinear structures $\mathrm{APA}$ and $\mathrm{AQA}$ the product is alternating, $\tilde P\star\tilde P=0$, so every nonzero element annihilates itself. On the two antisymmetric sesquilinear structures the product is the projection of a product of the two elements into the centre or into the vector subspace: on $\mathrm{APS}$ the value is $\mathrm{Vect}(\tilde P\tilde X^{*})$, and the witness $(\tilde P^{-1})^{*}$ gives the central value $e_0$ when $\tilde P$ is invertible while a plain annihilator gives the value $0$ when it is not; on $\mathrm{AQS}$ the value is $\mathbf P\times\overline{\mathbf X}$, whose witness $\overline{\tilde P}$ makes it zero when the vector part $\mathbf P$ is nonzero, while a central $\tilde P$ annihilates every element. On the two scalar-valued symmetric structures $\mathrm{SQA}$ and $\mathrm{SPS}$ the product is a nondegenerate bilinear or Hermitian form read as a central value, so for a nonzero $\tilde P$ the orthogonal complement of $\tilde P$ in the form is a hyperplane of nonzero vectors, each of them an annihilating factor. On $\mathrm{SPA}$ the product is the Jordan product and its left multiplication has determinant $Q_0^{2}N(\tilde Q)$ (*The Trace Form and the Invariance of the Symmetric Plain Algebra*), which vanishes exactly when $Q_0=0$ or $N(\tilde Q)=0$; on $\mathrm{SQS}$ the criterion is read in coordinates in *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* and is the same disjunction. Each derived criterion is owned by its article (§*Further Reading*), and the table records it.

**Corollary (the cone is the common core).** The punctured cone $\mathcal{C}\setminus\{0\}$ is contained in the zero-divisor set of each of the twelve structures, and it is equal to the set of exactly four of them, the four general products.

*Proof.* Every row of the table of the introduction contains the cone: the four general rows equal it, the rows of $\mathrm{SPA}$ and $\mathrm{SQS}$ contain it by their second clause, and the remaining six rows are the whole punctured space. Equality for the four general rows is the theorem above.

Two consequences follow. First, because the cone lies in every set, an element of vanishing norm admits an annihilating factor in all twelve products, and the cone is the largest subset on which the twelve agree; the converse fails, since the derived sets are strictly larger. Second, the ring-theoretic picture breaks on the derived structures: the unit $e_1$, whose norm is $1$, is a zero divisor of $\mathrm{SPA}$ and of $\mathrm{SQS}$, because $e_1\bullet e_2=\tfrac12(e_1e_2+e_2e_1)=0$ for the Jordan product and $e_1\star e_2=0$ for the symmetric quaternionic sesquilinear product, and it is invertible in the algebra. A zero divisor need not be a non-unit unless the product has a two-sided unit.

The invariant is common to the twelve and the detection is not: the central square $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0$ is written with the plain multiplication and the natural conjugation alone, so no derived product deforms it, but only the four general products read its vanishing as the exact zero-divisor condition.

## The Annihilators of One Element of the Cone

Fix an element of the cone, $\tilde P\neq0$ with $\mathrm{Norm}(\tilde P)=0$. Each of the four general products has two one-sided annihilators of it, $A_\star(\tilde P)$ and $B_\star(\tilde P)$, each a complex plane by §*The Criterion for One General Product*, so that the four products carry eight planes.

**Theorem (the four annihilators are related by the conjugations).** Write $A_{\text{plain}},A_{\natural},A_{*},A_{\natural*}$ for the left annihilators of $\tilde P$ in the plain, the natural, the general plain sesquilinear and the general quaternionic sesquilinear product. Then

$$
A_{\natural}(\tilde P)=A_{\text{plain}}(\tilde P^{\natural}) , \qquad A_{*}(\tilde P)=A_{\text{plain}}(\tilde P)^{*} , \qquad A_{\natural*}(\tilde P)=A_{\text{plain}}(\tilde P^{\natural})^{*} ,
$$

and the two sides coincide for the natural product and for the general plain sesquilinear product, $A_{\natural}=B_{\natural}$ and $A_{*}=B_{*}$, while for the plain product and for the general quaternionic sesquilinear product they differ in general.

*Proof.* The first identity is $\tilde P^{\natural}\tilde X=0$ read as the plain product of $\tilde P^{\natural}$ and $\tilde X$. For the second, the substitution $\tilde X=\tilde Y^{*}$ turns $\tilde P\tilde X^{*}=0$ into $\tilde P\tilde Y=0$, and ${}^{*}$ is a bijection, so the plane is the star-image of the plane of the plain product; the third is the first and the second composed. For the coincidences, the natural conjugation makes the natural product conjugate-commutative and the Hermitian conjugation makes the general plain sesquilinear one conjugate-commutative, so the two sides of each are exchanged by a bijection that fixes the vanishing; the plain and the fourth products have no such exchange.

**Example.** For the pure zero divisor $\tilde P=e_1+ie_2$, the plane of the plain product is $\mathbb{C}\{e_1+ie_2,\ e_3-ie_0\}$: both displayed vectors are annihilated by $e_1+ie_2$ on the left, and the plane is the one computed in *Zero Divisors of the General Quaternionic Algebra* for the natural product, whose two sides coincide.

## The Square-Zero Sets

### The Four Square-Zero Sets

The square-zero sets are the diagonal part of the annihilation theory: an element is square-zero when it annihilates itself. The four equations are

$$
\tilde P\tilde P=0 , \qquad \tilde P^{\natural}\tilde P=0 , \qquad \tilde P\tilde P^{*}=0 , \qquad \tilde P^{\natural}\tilde P^{*}=0 ,
$$

one to a general product, and they range from a single point to the whole cone.

**Theorem (the four square-zero sets).** Write $Z_1,Z_2,Z_3,Z_4$ for the square-zero sets of the plain, the natural, the general plain sesquilinear and the general quaternionic sesquilinear product. Then

$$
Z_1=\{P_0=0,\ (\mathbf P,\mathbf P)=0\} , \qquad Z_2=\mathcal{C} , \qquad Z_3=\{0\} , \qquad Z_4=\{\tilde P:\overline{\tilde P}\tilde P=0\} ,
$$

and $Z_1$ is the **pure isotropic cone**, of real dimension four; $Z_2$ is the whole cone; $Z_3$ is the origin alone; and $Z_4$ is a proper subfamily of the cone, containing the nonzero element $e_0+ie_1$.

*Proof.* The first is the vanishing of the plain square, $\bigl(P_0^{2}-(\mathbf P,\mathbf P)\bigr)e_0+2P_0\mathbf P$, whose central coefficient and vector coefficient must vanish separately: $P_0\mathbf P=0$ gives $P_0=0$ or $\mathbf P=0$, and $\mathbf P=0$ forces $P_0=0$, so $P_0=0$ and $(\mathbf P,\mathbf P)=0$, a real cone of real dimension four (*Zero Divisors of the General Plain Algebra*). The second is the vanishing of the central square, which is the norm. The third is the definiteness of $\sum_\mu\lvert P_\mu\rvert^{2}$, the scalar part of the Hermitian square $\tilde P\tilde P^{*}$ (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*), so only the origin vanishes. The fourth is the equation $\overline{\tilde P}\tilde P=0$, equivalent to $\tilde P^{\natural}\tilde P^{*}=0$ through ${}^{\natural}$, and it is satisfied by $e_0+ie_1$ while its scalar part $\lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$ vanishes there, so it lies on the cone (*The Square of the General Quaternionic Sesquilinear Product and the Two Halves*).

**Corollary (the diagonal reading).** For each of the four general products the square-zero set is the set of elements that lie in their own annihilator,

$$
\tilde P\star\tilde P=0 \iff \tilde P\in A_\star(\tilde P) \iff \tilde P\in B_\star(\tilde P) ,
$$

the annihilator being read in the same product. The natural product gives the converse that fails for the fourth: for the natural product every element of the cone lies in its own annihilator, while for the fourth the element $ie_0+e_1+e_2+ie_3$ does not.

**Theorem (the order of the sets).** With $Z_1,Z_2,Z_3,Z_4$ the square-zero sets above,

$$
Z_3=\{0\}\subsetneq Z_1\subsetneq Z_2 , \qquad Z_3\subsetneq Z_4\subsetneq Z_2 , \qquad Z_1\cap Z_4=\{0\} ,
$$

so that $Z_1$ and $Z_4$ are incomparable, and the four sets are ordered only by the two chains through $Z_2$.

*Proof.* The inclusions $Z_1\subseteq Z_2$ and $Z_4\subseteq Z_2$ are the theorem above, and both are strict: $e_0+ie_1$ lies in $Z_2$ and not in $Z_1$, so $Z_1\subsetneq Z_2$, while $ie_0+e_1+e_2+ie_3$ lies in $Z_2$ and not in $Z_4$, so $Z_4\subsetneq Z_2$. The sets $Z_1$ and $Z_4$ are non-empty beyond the origin, $e_1+ie_2$ and $e_0+ie_1$ being witnesses, and $Z_1\cap Z_4=\{0\}$ because a pure element of $Z_4$ has $\sum_k\lvert P_k\rvert^{2}=0$, hence vanishes.

### The Twelve Square-Zero Sets

The four products are four of the twelve structures of the space, and the equation $\tilde P\star\tilde P=0$ is written in the operation of the structure, so each of the twelve carries a square-zero set of its own. The set is the diagonal of the zero-divisor theory, and it is read in the same family order.

| family | structure | the square-zero set | against its zero-divisor set |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | the pure isotropic cone, $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ | a proper subfamily of the cone |
| | $\mathrm{SPA}$ | the pure isotropic cone, $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ | a proper subfamily of the enlarged set |
| | $\mathrm{APA}$ | the whole space | the zero-divisor set, with the origin |
| the quaternionic algebra | $\mathrm{GQA}$ | the whole cone $\mathcal{C}$ | the zero-divisor set, with the origin |
| | $\mathrm{SQA}$ | the whole cone $\mathcal{C}$ | a proper subfamily of the punctured space |
| | $\mathrm{AQA}$ | the whole space | the zero-divisor set, with the origin |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\{0\}$ alone | a proper subfamily |
| | $\mathrm{SPS}$ | $\{0\}$ alone | a proper subfamily |
| | $\mathrm{APS}$ | the subfamily with $\tilde P\tilde P^{*}$ central | not inside the cone; contains $e_0$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | the subfamily $\overline{\tilde P}\tilde P=0$ | a proper subfamily of the cone |
| | $\mathrm{SQS}$ | the subfamily $\overline{\tilde P}\tilde P=0$ | a proper subfamily of the enlarged set |
| | $\mathrm{AQS}$ | the subfamily with $\tilde P^{\natural}\tilde P^{*}$ fixed by $\overline{\cdot}$ | not inside the cone; contains $e_0$ |

**Theorem (the twelve square-zero sets).** Among the twelve structures the square-zero set is the whole space for $\mathrm{APA}$ and $\mathrm{AQA}$; the whole cone $\mathcal{C}$ for $\mathrm{GQA}$ and $\mathrm{SQA}$; the pure isotropic cone for $\mathrm{GPA}$ and $\mathrm{SPA}$; a proper subfamily of the cone for $\mathrm{GQS}$ and $\mathrm{SQS}$; the origin alone for $\mathrm{GPS}$ and $\mathrm{SPS}$; and a subfamily outside the cone, containing the unit, for $\mathrm{APS}$ and $\mathrm{AQS}$.

*Proof.* The plain square is that of §*The Four Square-Zero Sets* for $\mathrm{SPA}$, and the central square for $\mathrm{SQA}$, so the two symmetric bilinear structures inherit the sets of their general partners while their zero-divisor sets enlarge. For the sesquilinear pair the symmetric parts are the central forms, so their square-zero sets are those of the general structures on the diagonal, and the antisymmetric parts are half the difference between the square and its conjugate transpose, which vanishes exactly when the square is fixed by that involution. Each entry is the theorem of the owner article named in §*Further Reading*.

**Remark (where the square detects the zero divisors).** A vanishing square is an annihilating factor, so the square-zero set without the origin lies in the zero-divisor set of every structure; the converse is the property that fails, and the gap is a property of the structure and not of the element. The two sets agree, origin included, exactly for the three structures whose square vanishes identically or is the central square: $\mathrm{GQA}$, whose square is the norm, and $\mathrm{APA}$ and $\mathrm{AQA}$, which are alternating. For the other nine the square-zero set is strictly smaller, and it shrinks to the origin alone on the plain sesquilinear pair $\mathrm{GPS}$ and $\mathrm{SPS}$ while their zero-divisor set is the whole punctured space.

## The Square, the Idempotents and the Units

The zero-divisor set is the one row of the element theory on which the four general products agree; the square, the idempotents and the unit are three rows on which they separate. The three rows are collected here because the twelve-structure comparison is read against them, and the general theory of each is its owner's.

| reading | $\tilde P\tilde Q$ | $\tilde P^{\natural}\tilde Q$ | $\tilde P\tilde Q^{*}$ | $\tilde P^{\natural}\tilde Q^{*}$ |
|---|---|---|---|---|
| square-zero set | the pure cone $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ | the whole cone $\mathcal{C}$ | $\{0\}$ alone | the solutions of $\overline{\tilde P}\tilde P=0$ |
| idempotent set | $0$, $e_0$ and $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$ | $0$ and $e_0$ alone | $0$, $e_0$ and the Hermitian family $\tfrac12(e_0+i\hat\mu)$ | $0$, $e_0$ and the family $-\tfrac12e_0+\mu$ with $(\mu,\mu)=\tfrac34$ |
| identity | $e_0$, left and right | $e_0$, left only | $e_0$, right only | none |

Every entry is a set of elements of the cone or beside it, and each of the three rows separates the four products where the zero-divisor set does not. The square-zero row is §*The Four Square-Zero Sets*; the idempotent row is *The Idempotents of the Twelve Structures*; and the unit row is the unit table of *Comparison Between the Four General Products*.

The four idempotent sets are of four different kinds, and the norm separates them. The trivial pair $0,e_0$ belongs to all four. Beyond the pair, every nontrivial idempotent of the plain product is rank one in the matrix model, hence lies on the cone: the plain family $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$, of which the Hermitian family $\tfrac12(e_0+i\hat\mu)$ of the general plain sesquilinear product is the subfamily parametrised by the real unit vectors. The fourth product's family $-\tfrac12e_0+\mu$ over the real vectors of square three quarters is off the cone, where the norm equals $1$, and the general quaternionic bilinear product has no nontrivial idempotent at all.

## The One-Sided Inverse Equations

Only the plain product has a two-sided unit, so the classical equivalence *zero divisor if and only if not a unit* is available for it alone, and there it is exact: for a nonzero $\tilde P$ the statements *$\tilde P$ is a zero divisor of the plain product*, *$N(\tilde P)=0$* and *$\tilde P$ is not invertible* are equivalent (*Zero Divisors of the General Plain Algebra*). The substitute for the other three products is the one-sided inverse criterion.

**Theorem (the inverse equations).** Let $\star$ be one of the four general products and let $\tilde P\neq0$. Then $\tilde P$ is a zero divisor of $\star$ exactly when neither of the two equations

$$
\tilde P\star\tilde X=e_0 , \qquad \tilde X\star\tilde P=e_0
$$

has a solution; equivalently, both have a solution exactly when $N(\tilde P)\neq0$.

*Proof.* If $\tilde P\star\tilde X=e_0$ holds, then in the model the equation is $\mathsf{M}_2(\tilde P)M=\mathrm{I}_2$ or $\mathsf{M}_2(\tilde P^{\natural})M=\mathrm{I}_2$ for an invertible $M$, so $\mathsf{M}_2(\tilde P)$ is invertible and $N(\tilde P)\neq0$. Conversely, if $N(\tilde P)\neq0$ then $\tilde P$ is invertible and the four solutions are those of the table below.

The solutions are written with the inverse $\tilde P^{-1}=\tilde P^{\natural}/N(\tilde P)$ of the algebra, which exists for $N(\tilde P)\neq0$. The two conjugations commute, ${}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural}=\overline{\cdot}$, so the order of the two superscripts in the last row is immaterial.

| product | $\tilde X$ with $\tilde P\star\tilde X=e_0$ | $\tilde X$ with $\tilde X\star\tilde P=e_0$ |
|---|---|---|
| $\tilde P\tilde Q$ | $\tilde P^{-1}$ | $\tilde P^{-1}$ |
| $\tilde P^{\natural}\tilde Q$ | $(\tilde P^{-1})^{\natural}$ | $(\tilde P^{-1})^{\natural}$ |
| $\tilde P\tilde Q^{*}$ | $(\tilde P^{-1})^{*}$ | $(\tilde P^{-1})^{*}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $(\tilde P^{-1})^{\natural*}$ | $(\tilde P^{-1})^{\natural*}$ |

The criterion uses the fixed element $e_0$, invariant under both conjugations, and makes no appeal to a unit of the product; it reads the same in the four products, and it says that the zero divisors are exactly the elements that cannot be inverted on either side.

## The Zero Divisors and the Remarkable Subspaces

Whether a remarkable subspace contains zero divisors is the question of where the norm vanishes on it, and the answer is common to the four products because their sets are common (*Zero Divisors of the General Plain Algebra*, *Introduction to the Remarkable Subspaces*).

| subspace | zero divisors |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | none |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | none |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | the nilpotent cone, of real dimension four |
| $\mathbb{M}_{+}$, the Hermitian subspace | a double cone |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | a double cone |

On the centre $N(\tilde P)=P_0^{2}$ vanishes only at the origin; on the two quaternion subspaces it is a sum of squares of real coefficients of a definite sign, which vanishes only at the origin; on the vector subspace it is $(\mathbf P,\mathbf P)$, whose vanishing set is the pure cone of the nilpotents; and on the two Hermitian subspaces it is indefinite and cuts a double cone. A generic zero divisor therefore lies in none of the remarkable subspaces.

## Boundary: the Two Cones

The cone $\mathcal{C}$ has the shape of a cone, and the chapter carries a second cone on the same space, the isotropic cone of the general plain bilinear form $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ of *The Four Pairings of the Biquaternion Algebra*. The two are different and must not be conflated. Their diagonals are the two quadratic forms

$$
N(\tilde Q)=Q_0^{2}+(\mathbf Q,\mathbf Q) , \qquad \langle\tilde Q,\tilde Q\rangle=Q_0^{2}-(\mathbf Q,\mathbf Q) ,
$$

which differ by the sign of the vector part, and the two cones cross: the unit $e_0+e_1$ has $N=2$ and $\langle e_0+e_1,e_0+e_1\rangle=0$, so it is isotropic for the form and off the cone, while the zero divisor $e_0+ie_1$ has $N=0$ and $\langle e_0+ie_1,e_0+ie_1\rangle=2$. The element theory is built on the first cone and the geometry of the form on the second; the form is the subject of *The Isotropic Structure of the General Quaternionic Algebra*.

## Summary

A zero divisor is defined by an equation that names a product, so the twelve products of the biquaternion algebra define twelve zero-divisor sets. For the four general products the sets coincide: for each of them, and for a nonzero element, being a left zero divisor, being a right zero divisor and lying on the cone are the same condition, the cone being the vanishing set of the norm $N(\tilde Q)=\sum_\mu Q_\mu^{2}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)$ of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

The common set is the zero-divisor set $\mathcal{C}\setminus\{0\}$, a complex cone with apex at the origin, smooth away from the apex, of complex dimension three and real dimension six, whose nonzero members are the rank-one elements of the matrix model and whose left ideals are the minimal left ideals. Its complement is the group of units together with the origin, and it splits by the scalar part into the pure family of the nilpotents, of real dimension four, and the non-pure family of the complex multiples of the nontrivial idempotents, which fills the cone in real dimension six.

One set, four annihilators: of a fixed element of the cone each general product has two one-sided annihilators, each a complex plane; the four pairs are related by the two conjugations, the general plain sesquilinear plane being the star-image of the plane of the plain product and the general quaternionic plane the star-image of the plane of the natural product.

The four square-zero sets, the four idempotent sets and the four unit structures do not follow from the annihilated set and are tabulated here with their owners. The square-zero sets are the plain product's pure isotropic cone, of real dimension four, the natural product's whole cone, the general plain sesquilinear product's origin alone, and the general quaternionic sesquilinear product's proper subfamily of the cone. The cone is the zero-divisor set of the four general products alone: the four antisymmetric structures and the two scalar-valued symmetric structures $\mathrm{SQA}$ and $\mathrm{SPS}$ have the whole punctured space, and $\mathrm{SPA}$ and $\mathrm{SQS}$ have $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$. The cone is contained in all twelve sets and is the largest subset on which they agree. What a product does not change is the detection of the units: an element off the cone is invertible, and the one-sided inverse equations replace the classical equivalence for the three products that have no two-sided unit.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | one of the twelve products of $\mathbb{B}$; the four general products in the theorems |
| $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | the four general products |
| $N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | the general quaternionic bilinear form |
| $\mathrm{Norm}(\tilde Q)$ | the generic norm of the article, instantiated by the general quaternionic bilinear algebraic norm $N$ |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the general quaternionic bilinear algebraic norm, the scalar of the central square $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0$ |
| $\mathcal{C}=\{\tilde Q:\mathrm{Norm}(\tilde Q)=0\}$ | the zero-divisor cone, of complex dimension three and real dimension six |
| $\mathcal{C}\setminus\{0\}$ | the zero-divisor set of the four general products |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, where the central square lies |
| pure, non-pure | scalar part zero, scalar part nonzero |
| $A_\star(\tilde P)$, $B_\star(\tilde P)$ | the two one-sided annihilators of $\tilde P$ for the product $\star$ |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, with $\det\mathsf{M}_2(\tilde P)=N(\tilde P)$ |
| $\tilde P^{-1}=\tilde P^{\natural}/N(\tilde P)$ | the inverse of an element with $N(\tilde P)\neq0$ |
| $Z_1,Z_2,Z_3,Z_4$ | the square-zero sets of the plain, natural, general plain sesquilinear and general quaternionic sesquilinear products |
| $\overline{\tilde P}\tilde P$ | the coefficientwise conjugate times the element, the square of the fourth product up to ${}^{\natural}$ |
| $(\mathbf P,\mathbf Q)$ | the general plain bilinear dot product of the two vector parts |
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ | the general plain bilinear form, whose isotropic cone is not $\mathcal{C}$ |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space: the four general products and their eight symmetric and antisymmetric parts |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general vocabulary: the zero divisor, the annihilator, the idempotent, the nilpotent and the rest, each stated once for a general product.
- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the form $N$ and the four algebraic norms read on the diagonals of the four forms.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the plain-product criterion, the classification of the cone's elements and the parametrisation of the pure family.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the four idempotent sets, the four square-root problems and the four unit entries.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the four general products and their symmetric and antisymmetric parts.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve names, the three letters of each and the class of each.
- *The Idempotents of the Twelve Structures* (`articles_maths/the-idempotents-of-the-twelve-structures.md`), for the four idempotent sets of the four general products and their reading among the twelve.
- *The Square Roots of a Central Value in the Twelve Structures* (`articles_maths/the-square-roots-of-a-central-value-in-the-twelve-structures.md`), for the four root problems and the criterion that places every square-zero set inside the cone.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism, the determinant and the rank-one elements.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the general plain bilinear form and its isotropic cone.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the subspaces, the pure cone and the non-pure families.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra.md`), for the criterion $Q_0=0$ or $N(\tilde Q)=0$ of the enlarged set of $\mathrm{SPA}$.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the same criterion of the enlarged set of $\mathrm{SQS}$ and its two families.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`) and *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the two scalar-valued symmetric structures whose zero-divisor set is the whole punctured space.
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra.md`), *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), *Zero Divisors of the Antisymmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-sesqualgebra.md`) and *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the four alternating structures whose zero-divisor set is the whole punctured space.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the natural product's criterion and the coincidence of its two annihilators.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the equation $\overline{\tilde P}\tilde P=0$ and its two halves.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the definiteness of the general plain sesquilinear square.
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra.md`), for the minimal left ideals of the rank-one elements.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra* (`articles_maths/the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra.md`), for the determinant $Q_0^{2}N(\tilde Q)$ of the left multiplication of $\mathrm{SPA}$.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra.md`), for the isotropic cones of the two bilinear forms, which are not the cone $\mathcal{C}$.
- *The Topology of the Zero-Divisor Cone* (`articles_maths/the-topology-of-the-zero-divisor-cone.md`), for the cone as a topological space.
