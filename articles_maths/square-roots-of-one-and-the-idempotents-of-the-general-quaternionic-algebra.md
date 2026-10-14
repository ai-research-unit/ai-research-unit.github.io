# __Square Roots of One and the Idempotents of the General Quaternionic Algebra__

## Introduction

This article classifies the square roots of the central value $+1$ in the general quaternionic bilinear product, and then the **idempotents** of that product, the elements the same squaring map keeps on their own square.

Both notions name a product, and throughout this article the product is the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ of the general quaternionic algebra, the $\mathrm{GQA}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the square of the article is the square of $\star$, and an unqualified *idempotent* is an idempotent of $\star$. The general definition of the square and of the roots of a central value is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*, and the general definition of an idempotent is §*The Idempotent, the Projection and the Peirce Decomposition* of the same article.

The whole problem is decided by one identity. The square of every element of this product is the central element $N(\tilde\Xi)e_0$, so the root equation of the value $\lambda$ reduces to the single complex equation $N(\tilde\Xi)=\lambda$, and the idempotent equation collapses to a quadratic on the scalar line. The roots of $+1$ are the level set $N=1$, a nondegenerate complex quadric of real dimension six; the idempotents are as small as they can be, the two trivial ones $0$ and $e_0$.

**The results.** The roots of $+1$ in the general quaternionic product are the solutions of $N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)=1$, a nondegenerate complex quadric of complex dimension three and real dimension six; they contain the central pair $\pm e_0$, the real vector roots $\hat u$ over the real unit vectors, and a mixed family carrying both a scalar part and a vector part. The idempotents of the product are $0$ and $e_0$ alone, and the product has no nontrivial idempotent. The two sets are not related by the halving map that carries the roots of $+1$ onto the idempotents of the plain product: the map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ produces an idempotent of $\star$ only at $\pm e_0$, and every other root of $+1$ is sent out of the idempotent set. The plain Hermitian idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ are idempotents of the plain product and square-zero here, so the plain idempotents are roots of $0$ of this product; on the operator side they recover their role, the left multiplication $L_{\tilde P}$ being a projector exactly when $\tilde P$ is a plain idempotent, so the product carries a family of projectors of complex dimension two indexed by elements that are not its own idempotents. Read on the remarkable subspaces, the idempotent equation leaves the two trivial idempotents in the centre, the quaternion subspace and the Hermitian subspace, and only $0$ in the vector, anti-quaternion and anti-Hermitian subspaces.

**Boundaries.** The product, the square and the algebraic norm are *Introduction to the General Quaternionic Algebra of Biquaternions* and *Norm and Invertibility in the General Quaternionic Algebra*; the general root problem for an arbitrary radicand is *Square Roots of a General Element in the General Quaternionic Algebra*; the roots of $0$ and the nilpotents of the product are *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*; the zero divisors and their two families are *Zero Divisors of the General Quaternionic Algebra*; the idempotents of the plain product, the Hermitian idempotents, the orthogonality and the Peirce decomposition are *Square Roots of One and the Idempotents of the General Plain Algebra* and *Ideals and Peirce Decomposition of the General Plain Algebra*; the projectors and the operator theory are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Specificities of the General Quaternionic Algebra*; and the four root problems of the four general products side by side are *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product and $\star$ the general quaternionic bilinear product $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$, with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\vec Q$. An element is $\tilde\Xi=\Xi_0e_0+\vec\Xi$ with $\vec\Xi=\sum_{k=1}^{3}\Xi_ke_k$, the **algebraic norm** is $N(\tilde\Xi)=\sum_\mu \Xi_\mu^2=\Xi_0^2+(\vec\Xi,\vec\Xi)$, and $(\vec\Xi,\vec\Xi)=\sum_k\Xi_k^2$ is the complex bilinear form of the vector part. A **central value** is an element $\lambda e_0$ with $\lambda\in\mathbb{C}$, and $\hat u$ denotes a real unit vector of $\mathbb{R}^3$. The scalar line is written $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$.

## The Root Equation and Its Reduction

**Definition.** Let $\lambda\in\mathbb{C}$. A **square root of the central value $\lambda$** in the general quaternionic product is an element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 .
$$

The root is relative to the product, and this article uses the one of $\star$ throughout; the general definition of the square and of the roots of a central value is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*.

**Theorem (the reduction).** For every $\tilde\Xi\in\mathbb{B}$,

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 \iff N(\tilde\Xi)=\lambda .
$$

**Proof.** The square is $N(\tilde\Xi)e_0$ by §*The Square Lies in the Scalar Line* of *Introduction to the General Quaternionic Algebra of Biquaternions*, and $e_0\neq0$.

The reduction is a single complex equation in the four complex coordinates, and it holds for every $\lambda$ at once. It has no case split and no vanishing condition: the plain product reduces the same problem to the pair $\Xi_0^2-(\vec\Xi,\vec\Xi)=\lambda$, $2\Xi_0\vec\Xi=0$, whose second equation forces $\Xi_0=0$ or $\vec\Xi=0$ and produces a central pair and a vector family (*Square Roots of a General Element in the General Plain Algebra*); the quaternionic square is central for every element, so the second equation does not arise and the root set is the quadric itself.

**Corollary (the level set).** The roots of the central value $\lambda$ are the level set $\{\tilde\Xi:N(\tilde\Xi)=\lambda\}$. With the four coefficients written $\Xi_\mu=p_\mu+ip'_\mu$ in real and imaginary parts, and $\lambda=\lambda_1+i\lambda_2$, the equation is the pair of real equations

$$
\sum_{\mu=0}^{3}\bigl(p_\mu^2-(p'_\mu)^2\bigr)=\lambda_1 , \qquad 2\sum_{\mu=0}^{3}p_\mu p'_\mu=\lambda_2 ,
$$

and the set is never empty: the central element $\tilde\Xi=\sqrt\lambda\,e_0$ is a root for either square root of $\lambda$. The root set of a general central value is treated in *Square Roots of a General Element in the General Quaternionic Algebra*, and the value $0$ is the subject of *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

## The Roots of Plus One

**The roots of $+1$ are exactly the solutions of $N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)=1$, a nondegenerate complex quadric of complex dimension three and real dimension six, containing the two central roots $\pm e_0$, the real vector roots $\hat u$ over the real unit vectors, and a mixed family.**

### Statement and Dimension

**Theorem.** The roots of $+1$ in the general quaternionic product are the solutions of

$$
N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)=1 .
$$

The set is a nondegenerate complex quadric of complex dimension three, hence of real dimension six. It contains the two central roots $\pm e_0$ and the elements $\hat u$ over the real unit vectors.

**Proof.** The criterion is the reduction. With $\Xi_\mu=p_\mu+ip'_\mu$ the equation is the pair $\sum_{\mu=0}^{3}(p_\mu^2-(p'_\mu)^2)=1$, $\sum_{\mu=0}^{3}p_\mu p'_\mu=0$ of two independent real equations on the eight real coordinates; the gradient of $N$ does not vanish on the level set, so the quadric is nondegenerate off the origin and has real dimension $8-2=6$. The elements $\pm e_0$ have $N=(\pm1)^2=1$; a real unit vector $\hat u$ has $\Xi_0=0$, $(\vec\Xi,\vec\Xi)=\sum_kn_k^2=1$ and satisfies the equation.

### The Families

The roots of $+1$ split into three entries according to the vector part.

- **The central roots $\pm e_0$.** These have $\vec\Xi=0$ and $\Xi_0=\pm1$, and $\Xi_0^2=1$. They are the two elements of the root set in the centre $\mathbb{C}_{\mathbb{B}}$.
- **The real vector roots.** These have $\Xi_0=0$ and $\vec\Xi$ a real vector with $(\vec\Xi,\vec\Xi)=1$. They are the elements $\hat u$ over the real unit vectors, a quadric of real dimension two in the real vector subspace; the complex solutions with $\Xi_0=0$ form a family of real dimension four, the solutions of $\sum_k(p_k^2-(p'_k)^2)=1$ together with $\sum_k p_kp'_k=0$.
- **The mixed roots.** These have both $\Xi_0$ and the vector part nonzero, and they fill the rest of the quadric.

The contrast with the plain product is a change of sign in the vector direction. The plain square of a pure element is $-(\vec\Xi,\vec\Xi)e_0$, so there the imaginary unit vectors $\tilde\Xi$ are the vector roots of $+1$; the conjugation in the first slot removes the sign, so here the **real** unit vectors $\hat u$ are the vector roots of $+1$. The central pair $\pm e_0$ has no plain analogue of the pure kind.

### Verification

The two central roots and the real vector roots are read from the algebraic norm directly. For the mixed family the equations above are the general pair, and the elements whose vector part has real and imaginary parts $\vec p,\vec p'$ with $|\vec p|=r$, $|\vec p'|=s$ and $\vec p\perp\vec p'$ have $N=\Xi_0^2+r^2-s^2$ when $\Xi_0$ is real; the value $1$ is reached for every real $\Xi_0$ by choosing $s^2-r^2=\Xi_0^2-1$, so the mixed family is non-empty over every real scalar, and the parametrics confirm the real dimension six.

### The Comparison with the Plain Product

The value $+1$ is read side by side with the plain product, and the change of sign in the vector direction is the whole of the difference. In the general quaternionic product the level set $N=1$ is one quadric of real dimension $6$, containing the central pair $\pm e_0$ and the real vector roots $\hat u$; in the plain product it is the central pair $\pm e_0$, the imaginary vector roots $\tilde\Xi$ over the real unit vectors, and a four-parameter family, and the plain column is quoted from *Square Roots of One and the Idempotents of the General Plain Algebra*. The value $0$ is the subject of *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, and the case-by-case comparison of the four general products, with the criterion by which the roots of a non-zero value are units, is *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The roots of $\pm1$ have $N=\pm1$, so they are units of the algebra and are never zero divisors; the one-sided inverse equations are soluble for them (*Norm and Invertibility in the General Quaternionic Algebra*).

Two structural differences are worth naming. The plain root sets are stratified by the vanishing of the scalar part, because the plain square is scalar only on the vector part; the quaternionic root sets are single quadrics, because the quaternionic square is always scalar. And the plain roots of $+1$ carry the idempotents of the plain product through the halving map of §*The Halving Map and the Roots of One*, whereas the roots of $+1$ of $\star$ carry no nontrivial element of the algebra, the idempotents of $\star$ being the two trivial ones; the two sets are different objects, and §*The Idempotents of the Product* reads the second.

**The roots of $-1$.** Multiplication by the central imaginary flips the sign of the square, because the product is $\mathbb{C}$-bilinear and $i$ is central,

$$
(i\tilde\Xi)\star(i\tilde\Xi)=i^{2}\bigl(\tilde\Xi\star\tilde\Xi\bigr)=-\tilde\Xi\star\tilde\Xi ,
$$

so it is a bijection of the roots of $+1$ onto the roots of $-1$, and the roots of $-1$ are read off the classification above: they are the elements $i\tilde\Xi$ with $\tilde\Xi$ a root of $+1$, that is the solutions of $N=-1$, containing the central pair $\pm i$, the imaginary vector roots $\tilde\Xi$ over the real unit vectors, and the $i$-images of the mixed family. The set is never empty. It is quoted here and used nowhere below, and the plain product reads its own roots of $-1$ from its roots of $+1$ by the same map, with the central pair $\pm i$ and the real vector roots $\hat u$ (*Square Roots of One and the Idempotents of the General Plain Algebra*).

## The Idempotents of the Product

**The idempotents of the general quaternionic product are $0$ and $e_0$ alone; the product has no nontrivial idempotent.**

### Definition and the Square

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde\Pi\in\mathbb{B}$. The element $\tilde\Pi$ is **idempotent of $\star$** when $\tilde\Pi\star\tilde\Pi=\tilde\Pi$; the **trivial idempotents** are $0$ and the left unit $e_0$, and an idempotent different from both is **nontrivial**. The definition is *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*, and it names the product. Throughout this part the product is $\star$.

**Lemma (the square is central).** For every $\tilde Q\in\mathbb{B}$,

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=N(\tilde Q)\,e_0 , \qquad N(\tilde Q)=Q_0^2+Q_1^2+Q_2^2+Q_3^2 .
$$

**Proof.** With $\tilde Q=Q_0e_0+\vec Q$ the product has scalar part $Q_0^2+(\vec Q,\vec Q)$ and vector part $Q_0\vec Q-Q_0\vec Q-\vec Q\times\vec Q=0$ at equal arguments; the statement is §*The Square Lies in the Scalar Line* of *Introduction to the General Quaternionic Algebra of Biquaternions*.

The lemma is the reason the idempotent equation is trivial here and nontrivial for the plain product. The plain square of the same element is $Q_0^2e_0+2Q_0\vec Q+\vec Q^2$, whose vector part is not obliged to vanish, and its idempotents are the Hermitian idempotents; the quaternionic square carries no vector part at all, and the equation is a quadratic in one complex variable.

### The Classification

**Theorem (idempotents).** The solutions of $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ are $\tilde\Pi=0$ and $\tilde\Pi=e_0$; the general quaternionic product has no nontrivial idempotent.

**Proof.** By the lemma the left-hand side is $N(\tilde\Pi)e_0$, an element of the centre, so an idempotent is central, $\tilde\Pi=Ae_0$ with $A\in\mathbb{C}$. For a central element the equation reads $A^2e_0=Ae_0$, that is $A^2=A$, or $A(A-1)=0$; the field $\mathbb{C}$ gives $A\in\{0,1\}$. Both values satisfy the equation.

**Remark (the equation is weaker than centrality).** The single equation $N(\tilde\Pi)=\Pi_0$ is not idempotence; it must be read with centrality attached. Every **pure** isotropic element, an element with $\vec Q\neq0$, $Q_0=0$ and $(\vec Q,\vec Q)=0$, satisfies $N(\tilde Q)=Q_0=0$ and is not an idempotent, its square being $0$ while it is itself neither $0$ nor central; and a non-pure element of algebraic norm zero, with $Q_0\neq0$, satisfies no scalar equation of the kind at all, since $N(\tilde Q)=0$ and $Q_0\neq0$. The nilpotents are the subject of *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*; here they matter as the warning that the scalar equation is necessary and not sufficient.

**Corollary.** The image of the squaring map is the scalar line and contains every idempotent; the idempotents of the product are exactly the central elements whose scalar coordinate is a root of $X^2-X$; and the central element $-e_0$, of algebraic norm $1$, shows that the algebraic norm alone does not decide idempotence.

### The Halving Map and the Roots of One

**The halving map carries the plain roots of $+1$ onto the plain idempotents, but it is not a bijection of the roots of $+1$ of $\star$ onto the idempotents of $\star$: $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ yields an idempotent of $\star$ only at $\tilde\Xi=\pm e_0$.**

**Proposition (the plain halving map).** For the plain product the map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection of the plain roots of $+1$ onto the plain idempotents, with inverse $\tilde\Pi\mapsto2\tilde\Pi-e_0$. The plain idempotents of the algebra are therefore the Hermitian idempotents of §*The Standard Idempotents of the Algebra* and the trivial pair (*Square Roots of One and the Idempotents of the General Plain Algebra*).

**Proof.** If $\tilde\Xi\tilde\Xi=e_0$ then $\bigl(\tfrac12(e_0+\tilde\Xi)\bigr)^2=\tfrac14\bigl(e_0+2\tilde\Xi+e_0\bigr)=\tfrac12(e_0+\tilde\Xi)$; conversely from $\tilde\Pi^2=\tilde\Pi$ the element $\tilde\Xi=2\tilde\Pi-e_0$ has $\tilde\Xi^2=4\tilde\Pi-4\tilde\Pi+e_0=e_0$. The two maps are inverse to each other, and the count of the plain idempotents is the cited classification.

The map is stated on the plain product, and it is the map the plain architecture uses. It does not survive the change of product, and the failure is computable.

**Proposition (the map misses here).** Let $\tilde\Xi$ be a root of $+1$ of $\star$ and put $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$. Then

$$
\tilde\Pi\star\tilde\Pi-\tilde\Pi=\tfrac14\bigl(\tilde\Xi^{\natural}-\tilde\Xi\bigr)=-\tfrac12\vec\Xi ,
$$

so $\tilde\Pi$ is an idempotent of $\star$ exactly when $\vec\Xi=0$, that is exactly for $\tilde\Xi=\pm e_0$.

**Proof.** The product is $\mathbb{C}$-bilinear, so

$$
(e_0+\tilde\Xi)\star(e_0+\tilde\Xi)=e_0\star e_0+e_0\star\tilde\Xi+\tilde\Xi\star e_0+\tilde\Xi\star\tilde\Xi=e_0+\tilde\Xi+\tilde\Xi^{\natural}+N(\tilde\Xi)e_0 ,
$$

and $N(\tilde\Xi)=1$; dividing by four and subtracting $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ leaves $\tfrac14(\tilde\Xi^{\natural}-\tilde\Xi)$. Since $\tilde\Xi^{\natural}-\tilde\Xi=-2\vec\Xi$, the difference vanishes exactly when the vector part of $\tilde\Xi$ does, and the roots of $+1$ with vanishing vector part are $\pm e_0$. The halving map sends the two central roots onto $0$ and $e_0$ and every other root of $+1$ out of the idempotent set.

The two propositions are the whole of the relation between the roots of one and the idempotents in this section: the parametrisation that the plain product enjoys is broken here by the conjugation in the first slot, and the idempotents are read from the squaring map directly, in §*The Classification*.

### The Standard Idempotents of the Algebra

**The plain Hermitian idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ over the real unit vectors are nontrivial plain idempotents in $\mathbb{M}_{+}$, and they are square-zero in $\star$, $\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=0$, so the product fails to keep them.**

The idempotents of the plain product are the standard family of the algebra, and they are the elements the product fails to keep.

**Definition.** For a **real unit vector** $\hat u=n_1e_1+n_2e_2+n_3e_3$, $n_1^2+n_2^2+n_3^2=1$, the **Hermitian idempotent** is

$$
\tilde\Pi_+(\tilde\Xi)=\tfrac12\bigl(e_0+\tilde\Xi\bigr) .
$$

**Proposition.** Every Hermitian idempotent is a nontrivial idempotent of the plain product and lies in the Hermitian subspace: $\tilde\Pi_+(\tilde\Xi)\tilde\Pi_+(\tilde\Xi)=\tilde\Pi_+(\tilde\Xi)$ and $\tilde\Pi_+(\tilde\Xi)\in\mathbb{M}_{+}$.

**Proof.** The vector $\tilde\Xi$ has $(\tilde\Xi)^2=\tilde\Xi^{2}=(-1)(-e_0)=e_0$, so $\tilde\Pi^2=\tfrac14(e_0+2\tilde\Xi+e_0)=\tilde\Pi$; and the element has real scalar part and purely imaginary vector part, which is the coordinate condition of $\mathbb{M}_{+}$ (*Introduction to the Remarkable Subspaces*). It is not $0$ and not $e_0$.

By *Square Roots of One and the Idempotents of the General Plain Algebra* the nontrivial idempotents of the plain product are exactly these, one for each real unit vector, so the plain idempotent set is the family $\tilde\Pi_+(\tilde\Xi)$, a quadric of complex dimension two, together with $0$ and $e_0$. The general quaternionic product answers differently.

**Proposition (the standard idempotents are square-zero here).** For every real unit vector $\hat u$,

$$
\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=0 , \qquad N\bigl(\tilde\Pi_+(\tilde\Xi)\bigr)=0 .
$$

**Proof.** The natural conjugation negates the vector part, $\tilde\Pi_+(\tilde\Xi)^{\natural}=\tfrac12(e_0-\tilde\Xi)=e_0-\tilde\Pi_+(\tilde\Xi)$, the **complementary idempotent**. Hence

$$
\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=\tilde\Pi_+(\tilde\Xi)^{\natural}\tilde\Pi_+(\tilde\Xi)=\tfrac14\bigl(e_0-(\tilde\Xi)^2\bigr)=\tfrac14(e_0-e_0)=0 ,
$$

and the algebraic norm of the left factor is the scalar of the square, $N(\tilde\Pi_+(\tilde\Xi))=0$.

### The Plain Idempotents as Roots of Zero

**The plain Hermitian idempotents are roots of $0$ of the quaternionic product, and more generally every nontrivial plain idempotent is; the plain idempotents are therefore invisible to the idempotent equation of $\star$ and reappear in its nilpotent cone.**

The plain classification of the idempotents is the bijection of §*The Halving Map and the Roots of One* from the plain roots of $+1$ to the plain idempotents. In the general quaternionic product that bijection has no analogue, and the two statements below record what replaces it.

**Proposition (the plain idempotents are roots of $0$).** For every real unit vector $\hat u$ the Hermitian idempotent is a root of $0$ of the quaternionic product, $\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=0$, and its algebraic norm vanishes. More generally every nontrivial plain idempotent $\tilde\Pi$ satisfies $\tilde\Pi\star\tilde\Pi=0$.

**Proof.** The first statement is the preceding proposition. A nontrivial plain idempotent is a zero divisor of the plain product, so $N(\tilde\Pi)=0$ (*Zero Divisors of the General Plain Algebra*), and the square in the product is $N(\tilde\Pi)e_0=0$.

The plain idempotents are thus carried by the product into its nilpotent cone, and not into its idempotent set: the parameter set of the plain idempotents is invisible to the idempotent equation of $\star$ and reappears as the non-pure part of the nilpotent cone (*Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*).

### Idempotents as Projections

**The left multiplication $L_{\tilde P}$ is a projector exactly when $\tilde P$ is an idempotent of the plain product, so the product has a family of projectors of complex dimension two indexed by elements that are not its own idempotents.**

On the operator side the idempotents of the algebra recover their usual role, with the index conjugated.

**Theorem (the projector criterion).** The left multiplication $L_{\tilde P}(\tilde X)=\tilde P\star\tilde X$ is a projector, $L_{\tilde P}^{2}=L_{\tilde P}$, if and only if $\tilde P$ is an idempotent of the plain product. Consequently the product has a family of projectors of complex dimension two, indexed by the plain idempotents, while its own idempotents are $0$ and $e_0$ alone.

**Proof.** $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$ by the isotope identity, and the plain left multiplications are faithful; so $L_{\tilde P}^{2}=L_{\tilde P}$ exactly when $(\tilde P^{\natural})^2=\tilde P^{\natural}$, that is when $\tilde P$ is a plain idempotent. The family is the plain family of complex dimension two. The theorem and the monoid law $L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$ are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Specificities of the General Quaternionic Algebra*.

**Corollary (a projector on a square-zero element).** Every nontrivial plain idempotent is a nilpotent of $\star$ whose left multiplication is a projector,

$$
\tilde\Pi\star\tilde\Pi=0 , \qquad L_{\tilde\Pi}^{2}=L_{\tilde\Pi}\neq0 ,
$$

so the element is square-zero and the operator it defines is a projector with a two-dimensional image.

**Proof.** The element statement is §*The Plain Idempotents as Roots of Zero*; the operator statement is the theorem at the element $\tilde\Pi$.

**Remark (the two levels).** The plain product forbids the combination: there an idempotent and a nonzero nilpotent are disjoint, so no element is square-zero with an idempotent left multiplication (*Square Roots of Zero and the Nilpotents of the General Plain Algebra*). The quaternionic product separates the two properties and assigns them to different levels: the element $\tilde\Pi$ has vanishing square, and the operator $L_{\tilde\Pi}$ is a projector. The pair $\tilde\Pi$ and $e_0-\tilde\Pi$ gives the decomposition $\mathbb{B}=(\tilde\Pi\star\mathbb{B})\oplus((e_0-\tilde\Pi)\star\mathbb{B})$ into minimal left ideals of the plain algebra, which is the left-ideal theory of *The Specificities of the General Quaternionic Algebra*.

### The Idempotents and the Non-Pure Zero Divisors

**A non-pure element $\tilde Q=Q_0e_0+\vec Q$ is a zero divisor of $\star$ exactly when it is a complex multiple $\tilde Q=2Q_0\tilde\Pi$ of a nontrivial plain idempotent, and then $\tilde Q\star\tilde Q=0$ while $\tilde Q\tilde Q=2Q_0\tilde Q\neq0$.**

The displacement of the Hermitian idempotents is a statement about the zero divisors of the product.

**Theorem.** Let $\tilde Q=Q_0e_0+\vec Q$ with $Q_0\neq0$. Then $\tilde Q$ is a zero divisor of the product if and only if it is a complex multiple of a nontrivial plain idempotent, $\tilde Q=2Q_0\tilde\Pi$ with $\tilde\Pi$ a plain idempotent; and then

$$
\tilde Q\star\tilde Q=0 , \qquad \tilde Q\tilde Q=2Q_0\tilde Q\neq0 .
$$

**Proof.** The non-pure zero divisors are exactly the multiples of the nontrivial plain idempotents (*Zero Divisors of the General Quaternionic Algebra*, §*Non-Pure Zero Divisors*): the criterion $N(\tilde Q)=0$ is $(\vec Q,\vec Q)=-Q_0^2$, and the plain square is $(Q_0^2-(\vec Q,\vec Q))e_0+2Q_0\vec Q=2Q_0\tilde Q$, which makes $\tilde Q/(2Q_0)$ a plain idempotent.

**Corollary (the two products on the same element).** A nontrivial plain idempotent is an idempotent of the plain product and a nilpotent of the quaternionic product; and conversely a nonzero nilpotent of the quaternionic product which is non-pure is, up to a complex scalar, an idempotent of the plain product. No element is a nontrivial idempotent of both products.

**Proof.** The first clause is the theorem with $Q_0=\tfrac12$, and the second is the same reading. A nontrivial idempotent of $\star$ does not exist, by the classification.

### The Idempotent Equation on the Remarkable Subspaces

**The centre, the quaternion subspace and the Hermitian subspace carry the two trivial idempotents, while the vector, the anti-quaternion and the anti-Hermitian subspaces carry only $0$; no remarkable subspace carries a nontrivial idempotent.**

Since the square is always central, the equation $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ can hold inside a subspace only when the subspace contains the two trivial idempotents; reading it on each remarkable subspace records which ones do.

| subspace | element | $\tilde\Pi\star\tilde\Pi$ | idempotents |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $Ae_0$ | $A^2e_0$ | $0$, $e_0$ |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $\vec P$ | $(\vec P,\vec P)e_0$ | $0$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $h$ | $\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)e_0$ | $0$, $e_0$ |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $ih$ | $-\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)e_0$ | $0$ |
| $\mathbb{M}_{+}$, the Hermitian subspace | $a_0e_0+i\vec p$ | $\bigl(a_0^2-(\vec p,\vec p)\bigr)e_0$ | $0$, $e_0$ |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $ib_0e_0+\vec q$ | $\bigl(-b_0^2+(\vec q,\vec q)\bigr)e_0$ | $0$ |

**Proof.** Each entry is the algebraic norm on the subspace of the same row, by the table of *Norm and Invertibility in the General Quaternionic Algebra*. In the centre the equation leaves $A^2=A$, hence $A\in\{0,1\}$. In the vector subspace a central element equals a vector only at $0$; a nonzero isotropic element has square $0$ and is not idempotent. In the quaternion subspace the square is a **real** scalar multiple of $e_0$, so an idempotent is a real multiple of $e_0$ with $h_0^2=h_0$. In the anti-quaternion subspace the square is a real multiple of $e_0$ with the opposite sign, so $h=0$. In $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ the scalar parts are constrained to be real combinations, and the equation forces the vector part to vanish, then leaves the trivial pair or the origin as displayed.

**Remark.** Three subspaces, the centre, the quaternion subspace and the Hermitian subspace, carry the two trivial idempotents, and three, the vector, the anti-quaternion and the anti-Hermitian subspaces, carry only $0$; no remarkable subspace carries a nontrivial idempotent. The plain reading is the opposite: there the nontrivial idempotents are the Hermitian idempotents and lie in $\mathbb{M}_{+}$. The change of product moves them out of the idempotent set altogether.

### The Peirce Decomposition It Does Not Carry

**The quaternionic product carries no Peirce decomposition: its only nonzero idempotent is the left unit $e_0$, whose left multiplication is the identity, so the only Peirce piece is the whole algebra.**

A nonzero idempotent of an associative unital algebra carries the Peirce decomposition $A=A_1\oplus A_{1/2}\oplus A_0$ with $A_\lambda=\{x:\Pi x=\lambda x\}$, and the decomposition is the source of the minimal ideals and the matrix units (*Ideals and Peirce Decomposition of the General Plain Algebra*). The construction uses associativity twice, in reading the two maps as projections and in verifying that their images add.

For the quaternionic product there is nothing to attach it to. The only nonzero idempotent is the left unit $e_0$, and $L_{e_0}$ is the identity, so the only Peirce piece is the whole algebra. The nontrivial decomposition of the algebra — the frame of two orthogonal idempotents, the four Peirce lines, the minimal left ideals — is a property of the plain product alone, and what the quaternionic product has in its place is the centrality of the square and the projectors of §*Idempotents as Projections*, which are indexed by the plain idempotents rather than computed from the idempotents of the product.

## Summary

In the general quaternionic bilinear product the square of every element is the central element $N(\tilde\Xi)e_0$, so the root equation of a central value reduces to the single complex equation $N(\tilde\Xi)=\lambda$ and the idempotent equation forces centrality. The roots of $+1$ are the solutions of $N=1$, a nondegenerate complex quadric of real dimension six; they contain the central pair $\pm e_0$, the real vector roots $\hat u$ over the real unit vectors, and a mixed family, and their real and imaginary vector directions are the ones the plain product assigns to the opposite value. The roots of $-1$ are the images of the roots of $+1$ under multiplication by the central imaginary $i$, and they are quoted here alone. The idempotents of the product are $0$ and $e_0$ alone, and the product has no nontrivial idempotent; the halving map that carries the plain roots of $+1$ onto the plain idempotents produces an idempotent of $\star$ only at $\pm e_0$, so the plain idempotents are invisible to the idempotent equation and reappear as roots of $0$ of the product. On the operator side the plain idempotents recover their role: $L_{\tilde P}$ is a projector exactly when $\tilde P$ is a plain idempotent, so the product has a family of projectors of complex dimension two indexed by elements that are not its idempotents, and each of them is a square-zero element whose operator is a projector. The non-pure zero divisors of the product are exactly the complex multiples of the nontrivial plain idempotents, so a nontrivial plain idempotent is an idempotent of the plain product and a nilpotent of this one. Read on the remarkable subspaces, the idempotent equation leaves the two trivial idempotents in the centre, the quaternion subspace and the Hermitian subspace, and only $0$ in the vector, anti-quaternion and anti-Hermitian subspaces.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2=-e_0$ |
| $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| ${}^{\natural}$ | the natural conjugation $\tilde Q^{\natural}=Q_0-\vec Q$ |
| $N(\tilde\Xi)=\sum_\mu \Xi_\mu^2=\Xi_0^2+(\vec\Xi,\vec\Xi)$ | the algebraic norm, $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$ |
| $\lambda e_0$ | a central value, $\lambda\in\mathbb{C}$ |
| $\hat u$ | a real unit vector of $\mathbb{R}^3$, a real vector root of $+1$ |
| $\tilde\Xi$ | the imaginary vector roots of $-1$ |
| $\tilde\Pi$ | an idempotent of the product; the nonzero ones are $e_0$ alone |
| $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ | the Hermitian idempotent over a real unit vector $\hat u$ |
| $L_{\tilde P}$ | the left multiplication $\tilde X\mapsto\tilde P\star\tilde X$, a projector iff $\tilde P$ is a plain idempotent |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_{+},\mathbb{M}_{-}$ | the remarkable subspaces |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the square roots of a central value in an algebra with a quadratic form, and for idempotents and square-zero elements in a non-associative algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quadratic form $\sum_\mu Q_\mu^2$ of the complex quaternion algebra and its level sets.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the idempotent equation and the Peirce decomposition in the absence of associativity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the conjugations of an algebra and the elements they fix.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots* and §*The Idempotent, the Projection and the Peirce Decomposition*, for the general definitions of the root of a central value and of an idempotent.
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the product, the square and the left unit.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the algebraic norm and its table on the remarkable subspaces.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra.md`), for the Hermitian idempotents, the halving map from the roots of $+1$, the plain classification and the plain roots of $+1$ and $-1$.
- *Square Roots of a General Element in the General Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-quaternionic-algebra.md`), for the root problem of an arbitrary radicand and the scaling of the root set.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra.md`), for the roots of $0$, the quadratic cone and the displacement of the plain idempotents into the nilpotents.
- *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the four root problems side by side and the criterion by which a root of a non-zero value is a unit.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the criterion, the two families and the non-pure zero divisors.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the monoid law and the projectors.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the projectors, the left ideals and the decomposition.
