# __Square Roots of One and the Idempotents of the General Quaternionic Algebra__

## Introduction

This article classifies the square roots of the central value $+1$ in the general quaternionic bilinear product, and then the **idempotents** of that product, the elements the same squaring map keeps on their own square.

Both notions name a product, and throughout this article the product is the general quaternionic bilinear product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ of the general quaternionic algebra, the $\mathrm{GQA}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the square of the article is the square of $\star$, and an unqualified *idempotent* is an idempotent of $\star$. The general definition of the square and of the roots of a central value is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*, and the general definition of an idempotent is §*The Idempotent, the Hermitian Idempotent and the Peirce Decomposition* of the same article.

The whole problem is decided by one identity. The square of every element of this product is the central element $\langle\tilde\Xi\rangle_{\natural}e_t$, so the root equation of the value $\lambda$ reduces to the single complex equation $\langle\tilde\Xi\rangle_{\natural}=\lambda$, and the idempotent equation collapses to a quadratic on the scalar line. The roots of $+1$ are the level set $N=1$, a nondegenerate complex quadric of real dimension six; the idempotents are as small as they can be, the two trivial ones $0$ and $e_t$.

**The results.** The roots of $+1$ in the general quaternionic product are the solutions of $\langle\tilde\Xi\rangle_{\natural}=\Xi_t^2+(\vec\Xi,\vec\Xi)=1$, a nondegenerate complex quadric of complex dimension three and real dimension six; they contain the central pair $\pm e_t$, the real vector roots $\vec u$ over the real unit vectors, and a mixed family carrying both a scalar part and a vector part. The idempotents of the product are $0$ and $e_t$ alone, and the product has no nontrivial idempotent. The two sets are not related by the halving map that carries the roots of $+1$ onto the idempotents of the plain product: the map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ produces an idempotent of $\star$ only at $\pm e_t$, and every other root of $+1$ is sent out of the idempotent set. The plain Hermitian idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ are idempotents of the plain product and square-zero here, so the plain idempotents are roots of $0$ of this product; on the operator side they recover their role, the left multiplication $L_{\tilde Q}$ being a projector exactly when $\tilde Q$ is a plain idempotent, so the product carries a family of projectors of complex dimension two indexed by elements that are not its own idempotents. Read on the remarkable subspaces, the idempotent equation leaves the two trivial idempotents in the centre, the quaternion subspace and the Hermitian subspace, and only $0$ in the vector, anti-quaternion and anti-Hermitian subspaces.

## The Root Equation and Its Reduction

**Definition.** Let $\lambda\in\mathbb{C}$. A **square root of the central value $\lambda$** in the general quaternionic product is an element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\lambda e_t .
$$

The root is relative to the product, and this article uses the one of $\star$ throughout; the general definition of the square and of the roots of a central value is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*.

**Theorem (the reduction).** For every $\tilde\Xi\in\mathbb{B}$,

$$
\boxed{\; \tilde\Xi\star\tilde\Xi=\lambda e_t \iff \langle\tilde\Xi\rangle_{\natural}=\lambda \;}.
$$

**Proof.** The square is $\langle\tilde\Xi\rangle_{\natural}e_t$ by §*The Square Lies in the Scalar Line* of *Introduction to the General Quaternionic Algebra*, and $e_t\neq0$.

The reduction is a single complex equation in the four complex coordinates, and it holds for every $\lambda$ at once. It has no case split and no vanishing condition: the plain product reduces the same problem to the pair $\Xi_t^2-(\vec\Xi,\vec\Xi)=\lambda$, $2\Xi_t\vec\Xi=0$, whose second equation forces $\Xi_t=0$ or $\vec\Xi=0$ and produces a central pair and a vector family (*Square Roots of a General Element in the Biquaternion Algebra*); the quaternionic square is central for every element, so the second equation does not arise and the root set is the quadric itself.

**Corollary (the level set).** The roots of the central value $\lambda$ are the level set $\{\tilde\Xi:\langle\tilde\Xi\rangle_{\natural}=\lambda\}$. With the four coefficients written $\Xi_\mu=p_\mu+ip'_\mu$ in real and imaginary parts, and $\lambda=\lambda_1+i\lambda_2$, the equation is the pair of real equations

$$
\sum_{\mu\in\{t,x,y,z\}}\bigl(p_\mu^2-(p'_\mu)^2\bigr)=\lambda_1 , \qquad 2\sum_{\mu\in\{t,x,y,z\}}p_\mu p'_\mu=\lambda_2 ,
$$

and the set is never empty: the central element $\tilde\Xi=\sqrt\lambda\,e_t$ is a root for either square root of $\lambda$. The root set of a general central value is treated in *Square Roots of a General Element in the General Quaternionic Algebra*, and the value $0$ is the subject of *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

## The Roots of Plus One

**The roots of $+1$ are exactly the solutions of $\langle\tilde\Xi\rangle_{\natural}=\Xi_t^2+(\vec\Xi,\vec\Xi)=1$, a nondegenerate complex quadric of complex dimension three and real dimension six, containing the two central roots $\pm e_t$, the real vector roots $\vec u$ over the real unit vectors, and a mixed family.**

### Statement and Dimension

**Theorem.** The roots of $+1$ in the general quaternionic product are the solutions of

$$
\boxed{\; \langle\tilde\Xi\rangle_{\natural}=\Xi_t^2+(\vec\Xi,\vec\Xi)=1 \;}.
$$

The set is a nondegenerate complex quadric of complex dimension three, hence of real dimension six. It contains the two central roots $\pm e_t$ and the elements $\vec u$ over the real unit vectors.

**Proof.** The criterion is the reduction. With $\Xi_\mu=p_\mu+ip'_\mu$ the equation is the pair $\sum_{\mu\in\{t,x,y,z\}}(p_\mu^2-(p'_\mu)^2)=1$, $\sum_{\mu\in\{t,x,y,z\}}p_\mu p'_\mu=0$ of two independent real equations on the eight real coordinates; the gradient of $\langle\cdot\rangle_{\natural}$ does not vanish on the level set, so the quadric is nondegenerate off the origin and has real dimension $8-2=6$. The elements $\pm e_t$ have $N=(\pm1)^2=1$; a real unit vector $\vec u$ has $\Xi_t=0$, $(\vec\Xi,\vec\Xi)=\sum_\mu u_\mu^2=1$ and satisfies the equation.

### The Families

The roots of $+1$ split into three entries according to the vector part.

- **The central roots $\pm e_t$.** These have $\vec\Xi=0$ and $\Xi_t=\pm1$, and $\Xi_t^2=1$. They are the two elements of the root set in the centre $\mathbb{C}_{\mathbb{B}}$.
- **The real vector roots.** These have $\Xi_t=0$ and $\vec\Xi$ a real vector with $(\vec\Xi,\vec\Xi)=1$. They are the elements $\vec u$ over the real unit vectors, a quadric of real dimension two in the real vector subspace; the complex solutions with $\Xi_t=0$ form a family of real dimension four, the solutions of $\sum_\mu(p_\mu^2-(p'_\mu)^2)=1$ together with $\sum_\mu p_\mu p'_\mu=0$.
- **The mixed roots.** These have both $\Xi_t$ and the vector part nonzero, and they fill the rest of the quadric.

The contrast with the plain product is a change of sign in the vector direction. The plain square of a pure element is $-(\vec\Xi,\vec\Xi)e_t$, so there the imaginary unit vectors $\tilde\Xi$ are the vector roots of $+1$; the conjugation in the first slot removes the sign, so here the **real** unit vectors $\vec u$ are the vector roots of $+1$. The central pair $\pm e_t$ has no plain analogue of the pure kind.

### Verification

The two central roots and the real vector roots are read from the algebraic norm directly. For the mixed family the equations above are the general pair, and the elements whose vector part has real and imaginary parts $\vec p,\vec p'$ with $|\vec p|=r$, $|\vec p'|=s$ and $\vec p\perp\vec p'$ have $N=\Xi_t^2+r^2-s^2$ when $\Xi_t$ is real; the value $1$ is reached for every real $\Xi_t$ by choosing $s^2-r^2=\Xi_t^2-1$, so the mixed family is non-empty over every real scalar, and the parametrics confirm the real dimension six.

### The Comparison with the Plain Product

The value $+1$ is read side by side with the plain product, and the change of sign in the vector direction is the whole of the difference. In the general quaternionic product the level set $N=1$ is one quadric of real dimension $6$, containing the central pair $\pm e_t$ and the real vector roots $\vec u$; in the plain product it is the central pair $\pm e_t$, the imaginary vector roots $\tilde\Xi$ over the real unit vectors, and a four-parameter family, and the plain column is quoted from *Square Roots of One and the Idempotents of the Biquaternion Algebra*. The value $0$ is the subject of *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, and the case-by-case comparison of the four general products, with the criterion by which the roots of a non-zero value are units, is *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The roots of $\pm1$ have $N=\pm1$, so they are units of the algebra and are never zero divisors; the one-sided inverse equations are soluble for them (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*).

Two structural differences are worth naming. The plain root sets are stratified by the vanishing of the scalar part, because the plain square is scalar only on the vector part; the quaternionic root sets are single quadrics, because the quaternionic square is always scalar. And the plain roots of $+1$ carry the idempotents of the plain product through the halving map of §*The Halving Map and the Roots of One*, whereas the roots of $+1$ of $\star$ carry no nontrivial element of the algebra, the idempotents of $\star$ being the two trivial ones; the two sets are different objects, and §*The Idempotents of the Product* reads the second.

**The roots of $-1$.** Multiplication by the central imaginary flips the sign of the square, because the product is $\mathbb{C}$-bilinear and $i$ is central,

$$
(i\tilde\Xi)\star(i\tilde\Xi)=i^{2}\bigl(\tilde\Xi\star\tilde\Xi\bigr)=-\tilde\Xi\star\tilde\Xi ,
$$

so it is a bijection of the roots of $+1$ onto the roots of $-1$, and the roots of $-1$ are read off the classification above: they are the elements $i\tilde\Xi$ with $\tilde\Xi$ a root of $+1$, that is the solutions of $N=-1$, containing the central pair $\pm i$, the imaginary vector roots $\tilde\Xi$ over the real unit vectors, and the $i$-images of the mixed family. The set is never empty. It is quoted here and used nowhere below, and the plain product reads its own roots of $-1$ from its roots of $+1$ by the same map, with the central pair $\pm i$ and the real vector roots $\vec u$ (*Square Roots of One and the Idempotents of the Biquaternion Algebra*).

## The Idempotents of the Product

**The idempotents of the general quaternionic product are $0$ and $e_t$ alone; the product has no nontrivial idempotent.**

### Definition and the Square

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde\Pi\in\mathbb{B}$. The element $\tilde\Pi$ is **idempotent of $\star$** when $\tilde\Pi\star\tilde\Pi=\tilde\Pi$; the **trivial idempotents** are $0$ and the left unit $e_t$, and an idempotent different from both is **nontrivial**. The definition is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Idempotent, the Hermitian Idempotent and the Peirce Decomposition*, and it names the product. Throughout this part the product is $\star$.

**Lemma (the square is central).** For every $\tilde Q\in\mathbb{B}$,

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}\,e_t , \qquad \langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2 .
$$

**Proof.** With $\tilde Q=Q_te_t+\vec Q$ the product has scalar part $Q_t^2+(\vec Q,\vec Q)$ and vector part $Q_t\vec Q-Q_t\vec Q-\vec Q\times\vec Q=0$ at equal arguments; the statement is §*The Square Lies in the Scalar Line* of *Introduction to the General Quaternionic Algebra*.

The lemma is the reason the idempotent equation is trivial here and nontrivial for the plain product. The plain square of the same element is $Q_t^2e_t+2Q_t\vec Q+\vec Q^2$, whose vector part is not obliged to vanish, and its idempotents are the Hermitian idempotents; the quaternionic square carries no vector part at all, and the equation is a quadratic in one complex variable.

### The Classification

**Theorem (idempotents).** The solutions of $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ are $\tilde\Pi=0$ and $\tilde\Pi=e_t$; the general quaternionic product has no nontrivial idempotent.

**Proof.** By the lemma the left-hand side is $\langle\tilde\Pi\rangle_{\natural}e_t$, an element of the centre, so an idempotent is central, $\tilde\Pi=Ae_t$ with $A\in\mathbb{C}$. For a central element the equation reads $A^2e_t=Ae_t$, that is $A^2=A$, or $A(A-1)=0$; the field $\mathbb{C}$ gives $A\in\{0,1\}$. Both values satisfy the equation.

**Remark (the equation is weaker than centrality).** The single equation $\langle\tilde\Pi\rangle_{\natural}=\Pi_t$ is not idempotence; it must be read with centrality attached. Every **pure** isotropic element, an element with $\vec Q\neq0$, $Q_t=0$ and $(\vec Q,\vec Q)=0$, satisfies $\langle\tilde Q\rangle_{\natural}=Q_t=0$ and is not an idempotent, its square being $0$ while it is itself neither $0$ nor central; and a non-pure element of algebraic norm zero, with $Q_t\neq0$, satisfies no scalar equation of the kind at all, since $\langle\tilde Q\rangle_{\natural}=0$ and $Q_t\neq0$. The nilpotents are the subject of *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*; here they matter as the warning that the scalar equation is necessary and not sufficient.

**Corollary.** The image of the squaring map is the scalar line and contains every idempotent; the idempotents of the product are exactly the central elements whose scalar coordinate is a root of $X^2-X$; and the central element $-e_t$, of algebraic norm $1$, shows that the algebraic norm alone does not decide idempotence.

### The Halving Map and the Roots of One

**The halving map carries the plain roots of $+1$ onto the plain idempotents, but it is not a bijection of the roots of $+1$ of $\star$ onto the idempotents of $\star$: $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ yields an idempotent of $\star$ only at $\tilde\Xi=\pm e_t$.**

**Proposition (the plain halving map).** For the plain product the map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ is a bijection of the plain roots of $+1$ onto the plain idempotents, with inverse $\tilde\Pi\mapsto2\tilde\Pi-e_t$. The plain idempotents of the algebra are therefore the Hermitian idempotents of §*The Standard Idempotents of the Algebra* and the trivial pair (*Square Roots of One and the Idempotents of the Biquaternion Algebra*).

**Proof.** If $\tilde\Xi\tilde\Xi=e_t$ then $\bigl(\tfrac12(e_t+\tilde\Xi)\bigr)^2=\tfrac14\bigl(e_t+2\tilde\Xi+e_t\bigr)=\tfrac12(e_t+\tilde\Xi)$; conversely from $\tilde\Pi^2=\tilde\Pi$ the element $\tilde\Xi=2\tilde\Pi-e_t$ has $\tilde\Xi^2=4\tilde\Pi-4\tilde\Pi+e_t=e_t$. The two maps are inverse to each other, and the count of the plain idempotents is the cited classification.

The map is stated on the plain product, and it is the map the plain architecture uses. It does not survive the change of product, and the failure is computable.

**Proposition (the map misses here).** Let $\tilde\Xi$ be a root of $+1$ of $\star$ and put $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$. Then

$$
\tilde\Pi\star\tilde\Pi-\tilde\Pi=\tfrac14\bigl(\tilde\Xi^{\natural}-\tilde\Xi\bigr)=-\tfrac12\vec\Xi ,
$$

so $\tilde\Pi$ is an idempotent of $\star$ exactly when $\vec\Xi=0$, that is exactly for $\tilde\Xi=\pm e_t$.

**Proof.** The product is $\mathbb{C}$-bilinear, so

$$
(e_t+\tilde\Xi)\star(e_t+\tilde\Xi)=e_t\star e_t+e_t\star\tilde\Xi+\tilde\Xi\star e_t+\tilde\Xi\star\tilde\Xi=e_t+\tilde\Xi+\tilde\Xi^{\natural}+\langle\tilde\Xi\rangle_{\natural}e_t ,
$$

and $\langle\tilde\Xi\rangle_{\natural}=1$; dividing by four and subtracting $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$ leaves $\tfrac14(\tilde\Xi^{\natural}-\tilde\Xi)$. Since $\tilde\Xi^{\natural}-\tilde\Xi=-2\vec\Xi$, the difference vanishes exactly when the vector part of $\tilde\Xi$ does, and the roots of $+1$ with vanishing vector part are $\pm e_t$. The halving map sends the two central roots onto $0$ and $e_t$ and every other root of $+1$ out of the idempotent set.

The two propositions are the whole of the relation between the roots of one and the idempotents in this section: the parametrisation that the plain product enjoys is broken here by the conjugation in the first slot, and the idempotents are read from the squaring map directly, in §*The Classification*.

### The Standard Idempotents of the Algebra

**The plain Hermitian idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ over the real unit vectors are nontrivial plain idempotents in $\mathbb{M}_{+}$, and they are square-zero in $\star$, $\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=0$, so the product fails to keep them.**

The idempotents of the plain product are the standard family of the algebra, and they are the elements the product fails to keep.

**Definition.** For a **real unit vector** $\vec u=u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$, $u_x^2+u_y^2+u_z^2=1$, the **Hermitian idempotent** is

$$
\tilde\Pi_+(\tilde\Xi)=\tfrac12\bigl(e_t+\tilde\Xi\bigr) .
$$

**Proposition.** Every Hermitian idempotent is a nontrivial idempotent of the plain product and lies in the Hermitian subspace: $\tilde\Pi_+(\tilde\Xi)\tilde\Pi_+(\tilde\Xi)=\tilde\Pi_+(\tilde\Xi)$ and $\tilde\Pi_+(\tilde\Xi)\in\mathbb{M}_{+}$.

**Proof.** The vector $\tilde\Xi$ has $(\tilde\Xi)^2=\tilde\Xi^{2}=(-1)(-e_t)=e_t$, so $\tilde\Pi^2=\tfrac14(e_t+2\tilde\Xi+e_t)=\tilde\Pi$; and the element has real scalar part and purely imaginary vector part, which is the coordinate condition of $\mathbb{M}_{+}$ (*Introduction to the Remarkable Subspaces*). It is not $0$ and not $e_t$.

By *Square Roots of One and the Idempotents of the Biquaternion Algebra* the nontrivial idempotents of the plain product are exactly these, one for each real unit vector, so the plain idempotent set is the family $\tilde\Pi_+(\tilde\Xi)$, a quadric of complex dimension two, together with $0$ and $e_t$. The general quaternionic product answers differently.

**Proposition (the standard idempotents are square-zero here).** For every real unit vector $\vec u$,

$$
\boxed{\; \tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=0 , \qquad \langle\tilde\Pi_+(\tilde\Xi)\rangle_{\natural}=0 \;}.
$$

**Proof.** The natural conjugation negates the vector part, $\tilde\Pi_+(\tilde\Xi)^{\natural}=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)$, the **complementary idempotent**. Hence

$$
\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=\tilde\Pi_+(\tilde\Xi)^{\natural}\tilde\Pi_+(\tilde\Xi)=\tfrac14\bigl(e_t-(\tilde\Xi)^2\bigr)=\tfrac14(e_t-e_t)=0 ,
$$

and the algebraic norm of the left factor is the scalar of the square, $\langle\tilde\Pi_+(\tilde\Xi)\rangle_{\natural}=0$.

### The Plain Idempotents as Roots of Zero

**The plain Hermitian idempotents are roots of $0$ of the quaternionic product, and more generally every nontrivial plain idempotent is; the plain idempotents are therefore invisible to the idempotent equation of $\star$ and reappear in its nilpotent cone.**

The plain classification of the idempotents is the bijection of §*The Halving Map and the Roots of One* from the plain roots of $+1$ to the plain idempotents. In the general quaternionic product that bijection has no analogue, and the two statements below record what replaces it.

**Proposition (the plain idempotents are roots of $0$).** For every real unit vector $\vec u$ the Hermitian idempotent is a root of $0$ of the quaternionic product, $\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=0$, and its algebraic norm vanishes. More generally every nontrivial plain idempotent $\tilde\Pi$ satisfies $\tilde\Pi\star\tilde\Pi=0$.

**Proof.** The first statement is the preceding proposition. A nontrivial plain idempotent is a zero divisor of the plain product, so $\langle\tilde\Pi\rangle_{\natural}=0$ (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*), and the square in the product is $\langle\tilde\Pi\rangle_{\natural}e_t=0$.

The plain idempotents are thus carried by the product into its nilpotent cone, and not into its idempotent set: the parameter set of the plain idempotents is invisible to the idempotent equation of $\star$ and reappears as the non-pure part of the nilpotent cone (*Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*).

### Idempotents and Their Projectors

**The left multiplication $L_{\tilde Q}$ is a projector exactly when $\tilde Q$ is an idempotent of the plain product, so the product has a family of projectors of complex dimension two indexed by elements that are not its own idempotents.**

On the operator side the idempotents of the algebra recover their usual role, with the index conjugated.

**Theorem (the projector criterion).** The left multiplication $L_{\tilde Q}(\tilde Q_1)=\tilde Q\star\tilde Q_1$ is a projector, $L_{\tilde Q}^{2}=L_{\tilde Q}$, if and only if $\tilde Q$ is an idempotent of the plain product. Consequently the product has a family of projectors of complex dimension two, indexed by the plain idempotents, while its own idempotents are $0$ and $e_t$ alone.

**Proof.** $L_{\tilde Q}=L^{\mathrm{plain}}_{\tilde Q^{\natural}}$ by the isotope identity, and the plain left multiplications are faithful; so $L_{\tilde Q}^{2}=L_{\tilde Q}$ exactly when $(\tilde Q^{\natural})^2=\tilde Q^{\natural}$, that is when $\tilde Q$ is a plain idempotent. The family is the plain family of complex dimension two. The theorem and the monoid law $L_{\tilde Q}L_{\tilde Q_2}=L_{\tilde Q_2\tilde Q}$ are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Specificities of the General Quaternionic Algebra*.

**Corollary (a projector on a square-zero element).** Every nontrivial plain idempotent is a nilpotent of $\star$ whose left multiplication is a projector,

$$
\tilde\Pi\star\tilde\Pi=0 , \qquad L_{\tilde\Pi}^{2}=L_{\tilde\Pi}\neq0 ,
$$

so the element is square-zero and the operator it defines is a projector with a two-dimensional image.

**Proof.** The element statement is §*The Plain Idempotents as Roots of Zero*; the operator statement is the theorem at the element $\tilde\Pi$.

**Remark (the two levels).** The plain product forbids the combination: there an idempotent and a nonzero nilpotent are disjoint, so no element is square-zero with an idempotent left multiplication (*Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*). The quaternionic product separates the two properties and assigns them to different levels: the element $\tilde\Pi$ has vanishing square, and the operator $L_{\tilde\Pi}$ is a projector. The pair $\tilde\Pi$ and $e_t-\tilde\Pi$ gives the decomposition $\mathbb{B}=(\tilde\Pi\star\mathbb{B})\oplus((e_t-\tilde\Pi)\star\mathbb{B})$ into minimal left ideals of the plain algebra, which is the left-ideal theory of *The Specificities of the General Quaternionic Algebra*.

### The Idempotents and the Non-Pure Zero Divisors

**A non-pure element $\tilde Q=Q_te_t+\vec Q$ is a zero divisor of $\star$ exactly when it is a complex multiple $\tilde Q=2Q_t\tilde\Pi$ of a nontrivial plain idempotent, and then $\tilde Q\star\tilde Q=0$ while $\tilde Q\tilde Q=2Q_t\tilde Q\neq0$.**

The displacement of the Hermitian idempotents is a statement about the zero divisors of the product.

**Theorem.** Let $\tilde Q=Q_te_t+\vec Q$ with $Q_t\neq0$. Then $\tilde Q$ is a zero divisor of the product if and only if it is a complex multiple of a nontrivial plain idempotent, $\tilde Q=2Q_t\tilde\Pi$ with $\tilde\Pi$ a plain idempotent; and then

$$
\tilde Q\star\tilde Q=0 , \qquad \tilde Q\tilde Q=2Q_t\tilde Q\neq0 .
$$

**Proof.** The non-pure zero divisors are exactly the multiples of the nontrivial plain idempotents (*Zero Divisors of the General Quaternionic Algebra*, §*Non-Pure Zero Divisors*): the criterion $\langle\tilde Q\rangle_{\natural}=0$ is $(\vec Q,\vec Q)=-Q_t^2$, and the plain square is $(Q_t^2-(\vec Q,\vec Q))e_t+2Q_t\vec Q=2Q_t\tilde Q$, which makes $\tilde Q/(2Q_t)$ a plain idempotent.

**Corollary (the two products on the same element).** A nontrivial plain idempotent is an idempotent of the plain product and a nilpotent of the quaternionic product; and conversely a nonzero nilpotent of the quaternionic product which is non-pure is, up to a complex scalar, an idempotent of the plain product. No element is a nontrivial idempotent of both products.

**Proof.** The first clause is the theorem with $Q_t=\tfrac12$, and the second is the same reading. A nontrivial idempotent of $\star$ does not exist, by the classification.

### The Idempotent Equation on the Remarkable Subspaces

**The centre, the quaternion subspace and the Hermitian subspace carry the two trivial idempotents, while the vector, the anti-quaternion and the anti-Hermitian subspaces carry only $0$; no remarkable subspace carries a nontrivial idempotent.**

Since the square is always central, the equation $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ can hold inside a subspace only when the subspace contains the two trivial idempotents; reading it on each remarkable subspace records which ones do.

| subspace | element | $\tilde\Pi\star\tilde\Pi$ | idempotents |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $Ae_t$ | $A^2e_t$ | $0$, $e_t$ |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $\vec Q$ | $(\vec Q,\vec Q)e_t$ | $0$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $h$ | $\bigl(h_t^2+h_x^2+h_y^2+h_z^2\bigr)e_t$ | $0$, $e_t$ |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $ih$ | $-\bigl(h_t^2+h_x^2+h_y^2+h_z^2\bigr)e_t$ | $0$ |
| $\mathbb{M}_{+}$, the Hermitian subspace | $a_te_t+i\vec p$ | $\bigl(a_t^2-(\vec p,\vec p)\bigr)e_t$ | $0$, $e_t$ |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $ib_te_t+\vec q$ | $\bigl(-b_t^2+(\vec q,\vec q)\bigr)e_t$ | $0$ |

**Proof.** Each entry is the algebraic norm on the subspace of the same row, by the table of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*. In the centre the equation leaves $A^2=A$, hence $A\in\{0,1\}$. In the vector subspace a central element equals a vector only at $0$; a nonzero isotropic element has square $0$ and is not idempotent. In the quaternion subspace the square is a **real** scalar multiple of $e_t$, so an idempotent is a real multiple of $e_t$ with $h_t^2=h_t$. In the anti-quaternion subspace the square is a real multiple of $e_t$ with the opposite sign, so $h=0$. In $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ the scalar parts are constrained to be real combinations, and the equation forces the vector part to vanish, then leaves the trivial pair or the origin as displayed.

**Remark.** Three subspaces, the centre, the quaternion subspace and the Hermitian subspace, carry the two trivial idempotents, and three, the vector, the anti-quaternion and the anti-Hermitian subspaces, carry only $0$; no remarkable subspace carries a nontrivial idempotent. The plain reading is the opposite: there the nontrivial idempotents are the Hermitian idempotents and lie in $\mathbb{M}_{+}$. The change of product moves them out of the idempotent set altogether.

### The Peirce Decomposition It Does Not Carry

**The quaternionic product carries no Peirce decomposition: its only nonzero idempotent is the left unit $e_t$, whose left multiplication is the identity, so the only Peirce piece is the whole algebra.**

A nonzero idempotent $e$ of an associative unital algebra carries the Peirce decomposition $A=A_1\oplus A_{1/2}\oplus A_0$ with $A_\lambda=\{x:ex=\lambda x\}$, and the decomposition is the source of the minimal ideals and the matrix units (*Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*). The construction uses associativity twice, in reading the two maps as projections and in verifying that their images add.

For the quaternionic product there is nothing to attach it to. The only nonzero idempotent is the left unit $e_t$, and $L_{e_t}$ is the identity, so the only Peirce piece is the whole algebra. The nontrivial decomposition of the algebra — the frame of two orthogonal idempotents, the four Peirce lines, the minimal left ideals — is a property of the plain product alone, and what the quaternionic product has in its place is the centrality of the square and the projectors of §*Idempotents and Their Projectors*, which are indexed by the plain idempotents rather than computed from the idempotents of the product.

## Summary

In the general quaternionic bilinear product the square of every element is the central element $\langle\tilde\Xi\rangle_{\natural}e_t$, so the root equation of a central value reduces to the single complex equation $\langle\tilde\Xi\rangle_{\natural}=\lambda$ and the idempotent equation forces centrality. The roots of $+1$ are the solutions of $N=1$, a nondegenerate complex quadric of real dimension six; they contain the central pair $\pm e_t$, the real vector roots $\vec u$ over the real unit vectors, and a mixed family, and their real and imaginary vector directions are the ones the plain product assigns to the opposite value. The roots of $-1$ are the images of the roots of $+1$ under multiplication by the central imaginary $i$, and they are quoted here alone. The idempotents of the product are $0$ and $e_t$ alone, and the product has no nontrivial idempotent; the halving map that carries the plain roots of $+1$ onto the plain idempotents produces an idempotent of $\star$ only at $\pm e_t$, so the plain idempotents are invisible to the idempotent equation and reappear as roots of $0$ of the product. On the operator side the plain idempotents recover their role: $L_{\tilde Q}$ is a projector exactly when $\tilde Q$ is a plain idempotent, so the product has a family of projectors of complex dimension two indexed by elements that are not its idempotents, and each of them is a square-zero element whose operator is a projector. The non-pure zero divisors of the product are exactly the complex multiples of the nontrivial plain idempotents, so a nontrivial plain idempotent is an idempotent of the plain product and a nilpotent of this one. Read on the remarkable subspaces, the idempotent equation leaves the two trivial idempotents in the centre, the quaternion subspace and the Hermitian subspace, and only $0$ in the vector, anti-quaternion and anti-Hermitian subspaces.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_\mu^2=-e_t$ |
| $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| ${}^{\natural}$ | the natural conjugation $\tilde Q^{\natural}=Q_t-\vec Q$ |
| $\langle\tilde\Xi\rangle_{\natural}=\sum_\mu \Xi_\mu^2=\Xi_t^2+(\vec\Xi,\vec\Xi)$ | the algebraic norm, $\tilde\Xi\star\tilde\Xi=\langle\tilde\Xi\rangle_{\natural}e_t$ |
| $\lambda e_t$ | a central value, $\lambda\in\mathbb{C}$ |
| $\vec u$ | a real unit vector of $\mathbb{R}^3$, a real vector root of $+1$ |
| $\tilde\Xi$ | the imaginary vector roots of $-1$ |
| $\tilde\Pi$ | an idempotent of the product; the nonzero ones are $e_t$ alone |
| $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ | the Hermitian idempotent over a real unit vector $\vec u$ |
| $L_{\tilde Q}$ | the left multiplication $\tilde Q_1\mapsto\tilde Q\star\tilde Q_1$, a projector iff $\tilde Q$ is a plain idempotent |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_{+},\mathbb{M}_{-}$ | the remarkable subspaces |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the square roots of a central value in an algebra with a quadratic form, and for idempotents and square-zero elements in a non-associative algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quadratic form $\sum_\mu Q_\mu^2$ of the complex quaternion algebra and its level sets.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the idempotent equation and the Peirce decomposition in the absence of associativity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the conjugations of an algebra and the elements they fix.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*Powers, the Square and the Roots* and §*The Idempotent, the Hermitian Idempotent and the Peirce Decomposition*, for the general definitions of the root of a central value and of an idempotent.
- [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra.html), for the product, the square and the left unit.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the algebraic norm and its table on the remarkable subspaces.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the Hermitian idempotents, the halving map from the roots of $+1$, the plain classification and the plain roots of $+1$ and $-1$.
- [Square Roots of a General Element in the General Quaternionic Algebra](square-roots-of-a-general-element-in-the-general-quaternionic-algebra.html), for the root problem of an arbitrary radicand and the scaling of the root set.
- [Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra](square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra.html), for the roots of $0$, the quadratic cone and the displacement of the plain idempotents into the nilpotents.
- [Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the four root problems side by side and the criterion by which a root of a non-zero value is a unit.
- [Zero Divisors of the General Quaternionic Algebra](zero-divisors-of-the-general-quaternionic-algebra.html), for the criterion, the two families and the non-pure zero divisors.
- [The Left Multiplications of the Quaternionic Product and the Opposite Monoid](the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.html), for the monoid law and the projectors.
- [The Specificities of the General Quaternionic Algebra](the-specificities-of-the-general-quaternionic-algebra.html), for the projectors, the left ideals and the decomposition.
