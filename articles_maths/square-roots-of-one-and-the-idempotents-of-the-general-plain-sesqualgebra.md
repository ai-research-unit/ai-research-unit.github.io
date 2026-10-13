# __Square Roots of One and the Idempotents of the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ on the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ (*Introduction to the General Plain Sesqualgebra of Biquaternions*, *The Four General Products of the Biquaternion $\mathbb{C}$ Space*). This article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=e_0 .
$$

The second is the idempotents of the block, the elements $\tilde\Pi$ with $\tilde\Pi\star\tilde\Pi=\tilde\Pi$. The two subjects are one subject, because the **halving map**

$$
\tilde\Xi\longmapsto\tilde\Pi=\tfrac12\bigl(e_0+\tilde\Xi\bigr)
$$

is a bijection from the **Hermitian** roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$. The computation is two lines: if $\tilde\Xi$ is Hermitian with $\tilde\Xi\star\tilde\Xi=e_0$ then $\tilde\Xi^{*}=\tilde\Xi$ and $\tilde\Xi^{2}=\tilde\Xi\tilde\Xi^{*}=e_0$, so $\tilde\Pi$ is Hermitian with $\tilde\Pi\star\tilde\Pi=\tilde\Pi^{2}=\tfrac14(e_0+2\tilde\Xi+e_0)=\tilde\Pi$; and conversely every idempotent of the block is Hermitian, and $\tilde\Xi=2\tilde\Pi-e_0$ is Hermitian with $\tilde\Xi^{2}=4\tilde\Pi-4\tilde\Pi+e_0=e_0$. Every idempotent of the block is read through that map, on the Hermitian roots of $+1$ alone. The non-Hermitian roots of $+1$ do not give idempotents: the halved element is then not Hermitian, and the block detects it.

The article is algebraic. The roots of the general quadratic $\tilde\Xi\star\tilde\Xi=\tilde a$ are the companion article *Square Roots of a General Element in the General Plain Sesqualgebra*; the roots of $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*; the zero-divisor set is *Zero Divisors of the General Plain Sesqualgebra*; and the ideals the projections generate are *Ideals and Peirce Decomposition of the General Plain Algebra*. The roots of $-1$ are a short remark at the end of the roots part, they are used nowhere, and they open nothing.

**The results.** The block-square is the Hermitian element $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}=(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2})e_0+2i(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v)$ in the real halves $\tilde\Xi=q_r+iq_i$, whose scalar part is the definite $\sum_\mu\lvert\Xi_\mu\rvert^{2}\geq0$. The scalar part decides the roots of $+1$: a central value has a root only when it is a non-negative real, the value $0$ forcing the origin, and the roots of $+1$ are exactly the single family $\tilde\Xi=e^{i\theta}w$ over the real unit quaternions $w$, that is $U(1)\cdot S^{3}$, of real dimension four, containing $e_0$, $-e_0$ and the pure imaginary unit vectors $i\hat\mu$. The **Hermitian** roots of $+1$ are $\pm e_0$ and the $i\hat\mu$, and the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from them onto the idempotents of the block, which are $0$, $e_0$ and the $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$: a real two-parameter family of rank-one Hermitian projections.

**Placement.** The article is the fifth entry of the *Common Theory* section of the block, after the zero divisors and the annihilators, and before the roots of zero and the nilpotents and before the general value. It uses the product and the class of the introduction, the algebraic norm and the scalar part of the square from *Norm and Invertibility in the General Plain Sesqualgebra* and *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*, and the Hermitian subspace and the positive cone from *Hermitian and Skew-Hermitian Elements* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; it feeds the general-value article and the nilpotent article.

**Boundaries.** The product, its class and its placement are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the relative definition of the power, the square and the root of a central value, and the designation of the three central values, are *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*; the general definition of an idempotent, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, is the same article, §*The Idempotent, the Projection and the Peirce Decomposition*. The parent's roots of $+1$ and the parent's idempotents are *Square Roots of One and the Idempotents of the General Plain Algebra* and *Idempotents of the General Plain Algebra*; the two-involution arithmetic of the parent is *Square Roots of a General Element in the General Plain Algebra*. The other three general products carry roots and idempotents of their own, and they are *Comparison Between the Four General Products*; the zero-divisor criterion the roots miss is *Zero Divisors of the General Plain Sesqualgebra*; and the matrix model is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. An element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_0}e_0+\overline{\mathbf Q}$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$, with $\varepsilon=(1,-1,-1,-1)$ giving $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$. The product is the block $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. In the imaginary decomposition $\tilde Q=q_r+iq_i$ the halves $q_r,q_i$ are **real** quaternions, with real scalar parts $q_{r0},q_{i0}$ and vector parts $\mathbf u,\mathbf v$. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\Pi$ (§*The Idempotent Convention*), and a generic element $\tilde P$ or $\tilde Q$. The **central square** is $C(\tilde\Xi)=\tilde\Xi\tilde\Xi^{\natural}=\sum_\mu\Xi_\mu^{2}$, and the algebraic norm of the block is $H(\tilde\Xi)=\mathrm{Sc}(\tilde\Xi\star\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$.

The equations name a product, so the roots and the idempotents are relative to it. Throughout this article the square is the one of the general plain sesquilinear product, the Hermitian square $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}$; the unqualified word *idempotent* means an idempotent of that product, and an idempotent of the associative multiplication $\tilde P\tilde Q$ is called an **idempotent of the algebra**.

## The Roots of One

**The roots of $+1$ are exactly the elements $\tilde\Xi=e^{i\theta}w$ over the real unit quaternions $w$, that is the single family $U(1)\cdot S^{3}$ of real dimension four, containing $e_0$, $-e_0$ and the pure imaginary unit vectors $i\hat\mu$; no root of $+1$ is a zero divisor.**

A **root of $+1$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\star\tilde\Xi=e_0$, the square being the one of the block.

### The Reduction

**The block-square is Hermitian with scalar part $\mathrm{Sc}(\tilde\Xi\star\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}\geq0$, and equating it to a central value $\lambda e_0$ requires $\lambda$ to be a non-negative real number, so the negative and the non-real scalars are excluded, and so is the value $0$.**

**Theorem (the Hermitian square and its scalar part).** For $\tilde\Xi=q_r+iq_i$ with $q_r,q_i$ real quaternions,

$$
\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}=\bigl(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}\bigr)e_0+2i\Bigl(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v\Bigr),
$$

where $q_{r0},q_{i0}$ are the real scalar parts of $q_r,q_i$ and $\mathbf u,\mathbf v$ their vector parts. The square is **Hermitian**, its scalar part is

$$
\mathrm{Sc}\bigl(\tilde\Xi\star\tilde\Xi\bigr)=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=\sum_{\mu=0}^{3}\lvert\Xi_\mu\rvert^{2}\geq0,
$$

a real non-negative number vanishing only at $\tilde\Xi=0$.

*Proof.* The involution is $(\ )^{*}=\overline{\ }\,\circ\,{}^{\natural}$, and $q_r,q_i$ are real, so $\tilde\Xi^{*}=q_r^{\natural}-iq_i^{\natural}$. Expanding $\tilde\Xi\tilde\Xi^{*}=(q_r+iq_i)(q_r^{\natural}-iq_i^{\natural})$ and using $q_rq_r^{\natural}=\lvert q_r\rvert^{2}$, $q_iq_i^{\natural}=\lvert q_i\rvert^{2}$, and the product rule of the real quaternions for $q_iq_r^{\natural}-q_rq_i^{\natural}$ — whose scalar part vanishes and whose vector part is $-2q_{i0}\mathbf u+2q_{r0}\mathbf v+2\mathbf u\times\mathbf v$, giving the display after a sign change — yields the formula. The Hermitianness is $(\tilde\Xi\tilde\Xi^{*})^{*}=\tilde\Xi\tilde\Xi^{*}$, and the scalar part is read off the display.

**Corollary (the scalar trichotomy).** The equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$ requires, for a complex scalar $\lambda$,

$$
\sum_{\mu=0}^{3}\lvert\Xi_\mu\rvert^{2}=\lambda\qquad\text{and}\qquad q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v=0 .
$$

Consequently a central value $\lambda$ has a root only when $\lambda$ is a **non-negative real number**: the negative and the non-real scalars are excluded, and the value $0$ forces $\tilde\Xi=0$, which the definition of a root excludes.

*Proof.* The two sides are equal exactly when the scalar and the vector parts are equal, and the scalar part of $\lambda e_0$ is $\lambda$. The scalar equation forces $\lambda=\sum_\mu\lvert\Xi_\mu\rvert^{2}$, a real number $\geq0$, so a negative or a non-real $\lambda$ is excluded and $\lambda=0$ gives $\tilde\Xi=0$. The value $0$ is treated in *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*.

### The Roots of Plus One

**Theorem (the roots of $+1$).** The roots of $+1$ are exactly the elements

$$
\tilde\Xi=e^{i\theta}w,\qquad \theta\in\mathbb{R},\ w\in\mathbb{H}\ \text{real with}\ \lvert w\rvert=1,
$$

that is, the family $\{e^{i\theta}w\}=U(1)\cdot S^{3}$, of real dimension four, containing $e_0$, $-e_0$ and the pure imaginary unit vectors $i\hat\mu$ over the real unit vectors $\hat\mu$.

*Proof.* By the reduction the square is $e_0$ exactly when $\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=1$ and $q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v=0$. Dot the vector equation with $\mathbf u\times\mathbf v$: the first two terms are orthogonal to $\mathbf u\times\mathbf v$ and the third is $\lvert\mathbf u\times\mathbf v\rvert^{2}$, so $\mathbf u\times\mathbf v=0$; hence $\mathbf u$ and $\mathbf v$ are parallel, and the vector equation reads $q_{r0}\mathbf v=q_{i0}\mathbf u$. If $\mathbf u\neq0$ then $\mathbf v=\lambda\mathbf u$ for a real $\lambda$, the equation gives $q_{i0}=\lambda q_{r0}$ and therefore $q_i=q_{i0}+\mathbf v=\lambda(q_{r0}+\mathbf u)=\lambda q_r$: the halves are parallel as full quaternions, $\tilde\Xi=q_r+iq_i=(1+i\lambda)q_r$, and writing $1+i\lambda=\sqrt{1+\lambda^{2}}\,e^{i\theta}$ and $w=\sqrt{1+\lambda^{2}}\,q_r$, a real quaternion since $q_r$ is one, gives $\tilde\Xi=e^{i\theta}w$ with $\lvert w\rvert=1$ from the scalar equation. If $\mathbf u=0$ then $q_r=q_{r0}$ is a real scalar and the equation reads $q_{r0}\mathbf v=0$: either $\mathbf v=0$, and $\tilde\Xi=(q_{r0}+iq_{i0})e_0=e^{i\theta}e_0$ with $q_{r0}^{2}+q_{i0}^{2}=1$ is already of the required form with $w=e_0$, or $q_{r0}=0$, and $\tilde\Xi=iq_i=i(q_{i0}+\mathbf v)$ is of the required form with $\theta=\pi/2$ and the real unit $w=q_{i0}+\mathbf v$. In both cases $\tilde\Xi=e^{i\theta}w$ with $w$ a real unit quaternion. Conversely every $e^{i\theta}w$ with $w$ real unit has $q_r=\cos\theta\,w$, $q_i=\sin\theta\,w$, hence $\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=1$ and $q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v=\cos\theta\sin\theta(w_0\mathbf w-\mathbf w_0w)=0$, so it is a root. The parametrisation $(\theta,w)\mapsto e^{i\theta}w$ has kernel $\{(0,e_0),(\pi,-e_0)\}$, of order two, so the root set is a single real four-dimensional family, and the named elements are the cases $\theta=0$, $\theta=\pi$ and $\theta=\pi/2$ with $w=\hat\mu$.

**Corollary (the roots of $+1$ are never zero divisors).** Every root of $+1$ has $\mathrm{Sc}(\tilde\Xi\star\tilde\Xi)=1$, hence $H(\tilde\Xi)=1$, and its central square is a complex number of modulus one,

$$
C(e^{i\theta}w)=e^{2i\theta},\qquad\text{in particular}\qquad C(\pm e_0)=1,\qquad C(i\hat\mu)=-1 .
$$

Every root of $+1$ is therefore one-sidedly invertible, and the root set of $+1$ is **disjoint** from the zero-divisor cone.

*Proof.* The normalisation is the scalar equation $\mathrm{Sc}=1$ and the algebraic norm $H$ of the reduction. For the central square, $C(\tilde\Xi)=\sum_\mu\Xi_\mu^{2}$ with $\Xi_\mu=e^{i\theta}w_\mu$ and $w_\mu$ real, so $C(\tilde\Xi)=e^{2i\theta}\sum_\mu w_\mu^{2}=e^{2i\theta}$, of modulus one and never zero; the named values are the cases $\theta=0,\pi$ and $\theta=\pi/2$. The zero-divisor criterion is $C=0$ (*Zero Divisors of the General Plain Sesqualgebra*), so the root set misses the cone; the one-sided invertibility of the roots is *Norm and Invertibility in the General Plain Sesqualgebra*.

**Remark (the shape of the root set).** The parent's root set of $+1$ is several families together with the isolated elements $\pm i$; the block has its roots of $+1$ in the single family $U(1)\cdot S^{3}$, of real dimension four, and no root of the other two values. The block's set is a single orbit and the parent's is not, and the parent's two isolated roots have no counterpart in the block.

### The Hermitian Roots of One

**Definition (the Hermitian roots of $+1$).** A root of $+1$ is **Hermitian** when $\tilde\Xi^{*}=\tilde\Xi$.

**Theorem (the Hermitian roots of $+1$).** The Hermitian roots of $+1$ are the two central scalars $\pm e_0$ together with the pure imaginary unit vectors $i\hat\mu$ over the real unit vectors $\hat\mu$, a real two-parameter family.

*Proof.* A Hermitian element is $\xi_0e_0+i\boldsymbol\xi'$ with $\xi_0\in\mathbb{R}$ and $\boldsymbol\xi'$ a real vector, and its square in the algebra is $\xi_0^{2}e_0+\lvert\boldsymbol\xi'\rvert^{2}e_0+2\xi_0i\boldsymbol\xi'$ (since $(i\boldsymbol\xi')^{2}=-(\boldsymbol\xi')^{2}=\lvert\boldsymbol\xi'\rvert^{2}e_0$). Since the element is Hermitian its block-square is its algebra square, and the equation is $(\xi_0^{2}+\lvert\boldsymbol\xi'\rvert^{2})e_0+2\xi_0i\boldsymbol\xi'=e_0$, whose solution is $\xi_0=\pm1$ with $\boldsymbol\xi'=0$, or $\xi_0=0$ with $\lvert\boldsymbol\xi'\rvert=1$. The last is $i\hat\mu$.

**Remark (the Hermitian roots are the involutions of the block).** A Hermitian root of $+1$ is the element form of an involution of the Hermitian subspace, and the three kinds are the two central involutions $\pm e_0$ and the family $i\hat\mu$ over the real unit vectors. These are exactly the roots that the halving map turns into idempotents, and the non-Hermitian roots of $+1$ are dropped by the idempotent theory.

**The roots of minus one.** In a product that is two-sidedly linear the central imaginary carries the roots of $+1$ to the roots of $-1$, because $(i\tilde\Xi)\star(i\tilde\Xi)=i^{2}(\tilde\Xi\star\tilde\Xi)=-\tilde\Xi\star\tilde\Xi$; the mechanism is not universal. The block is sesquilinear, so the second slot conjugates and $(i\tilde\Xi)\star(i\tilde\Xi)=i\,\tilde\Xi\star\tilde\Xi\,\overline{i}=\tilde\Xi\star\tilde\Xi$: the scalar multiplication changes nothing, the roots of $-1$ are not read off the roots of $+1$ by such a map, and the root set of $-1$ is **empty**, as §*The Reduction* already shows.

## The Idempotents

**Every idempotent of the block is a Hermitian idempotent of the algebra, and the idempotents of the block are $0$, $e_0$ and the projections $\tilde\Pi_1(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$, a real two-parameter family; the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the Hermitian roots of $+1$ onto them.**

### The Definition

**Definition.** An element $\tilde\Pi$ is **idempotent for the product** $\star$, or a **$\star$-idempotent**, when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The equation names a product, so the notion is relative to it; the general definition, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, is *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*, and throughout this article the product is the general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of the block. The idempotents of the associative product $\tilde P\tilde Q$ are called the **idempotents of the algebra**, and they are written $\tilde\Pi$ with $\tilde\Pi^{2}=\tilde\Pi$.

Idempotents of an associative product encode direct summands: an idempotent $\tilde\Pi$ of the algebra and its complement $e_0-\tilde\Pi$ split the underlying $\mathbb{C}$-module,

$$
\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_0-\tilde\Pi),\qquad \mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B},
$$

and every such decomposition arises from an idempotent. A **primitive** idempotent, one that is not a sum of two nonzero orthogonal idempotents, generates a minimal left ideal; the general statements are *Definitions for the Study of the 12 Algebraic Structures*, and the decomposition carried by a plain idempotent is *Ideals and Peirce Decomposition of the General Plain Algebra*.

### Every Idempotent of the Block Is Hermitian

**Theorem.** Let $\tilde\Pi$ satisfy $\tilde\Pi\star\tilde\Pi=\tilde\Pi$. Then $\tilde\Pi$ is Hermitian,

$$
\tilde\Pi^{*}=\tilde\Pi .
$$

*Proof.* The equation reads $\tilde\Pi\tilde\Pi^{*}=\tilde\Pi$. The square $\tilde\Pi\tilde\Pi^{*}$ is fixed by the involution for every element, $(\tilde\Pi\tilde\Pi^{*})^{*}=\tilde\Pi\tilde\Pi^{*}$ (*Introduction to the General Plain Sesqualgebra of Biquaternions*, §*The Squares and the Positive Cone*). Applying ${}^{*}$ to the equation therefore gives $\tilde\Pi\tilde\Pi^{*}=\tilde\Pi^{*}$, and the left-hand sides of the equation and of its conjugate are the same, so the right-hand sides are equal, $\tilde\Pi=\tilde\Pi^{*}$.

**Remark.** The proof uses two things and no more: the square is Hermitian, and the involution is injective. The self-adjointness is therefore forced on every idempotent of the block, and it is the reason the equation reduces to the algebra's: a Hermitian element has $\tilde\Pi\star\tilde\Pi=\tilde\Pi\tilde\Pi^{*}=\tilde\Pi\tilde\Pi=\tilde\Pi^{2}$, so its two squares coincide.

### The Reduction

**Corollary.** An element is idempotent for the multiplication $\star$ if and only if it is a Hermitian idempotent of the algebra:

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi \quad\Longleftrightarrow\quad \tilde\Pi=\tilde\Pi^{*}\ \text{ and }\ \tilde\Pi^{2}=\tilde\Pi .
$$

*Proof.* If $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ then $\tilde\Pi$ is Hermitian by the theorem, and $\tilde\Pi\star\tilde\Pi=\tilde\Pi\tilde\Pi^{*}=\tilde\Pi^{2}$, so $\tilde\Pi^{2}=\tilde\Pi$. Conversely a Hermitian idempotent has $\tilde\Pi\star\tilde\Pi=\tilde\Pi\tilde\Pi^{*}=\tilde\Pi\tilde\Pi=\tilde\Pi^{2}=\tilde\Pi$.

**Proposition (the scalar part of the equation).** Let $\tilde\Pi$ satisfy $\tilde\Pi\star\tilde\Pi=\tilde\Pi$. Then the scalar part of $\tilde\Pi$ is the sum of the modulus squares of its coordinates,

$$
\Pi_0=\mathrm{Sc}\bigl(\tilde\Pi\star\tilde\Pi\bigr)=\sum_{\mu=0}^{3}\Pi_\mu\overline{\Pi_\mu}=\sum_{\mu=0}^{3}\lvert\Pi_\mu\rvert^{2},
$$

a real number, and it is nonzero unless $\tilde\Pi=0$.

*Proof.* The scalar part of the square is $\sum_\mu\lvert\Pi_\mu\rvert^{2}$ by the reduction of the roots part; taking the scalar part of $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ gives the display. The sum of the modulus squares is a nonnegative real number, and it vanishes only when every coordinate vanishes.

**Remark.** The display is a constraint and not a definition: it rules out at once the algebra idempotents with a non-real scalar part, and it is the idempotent reading of the nonnegativity of the sesquilinear square that *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* develops.

### The Classification

**Theorem (the idempotents of the block).** The idempotents of the sesquilinear multiplication $\star$ are $0$, $e_0$ and the elements

$$
\tilde\Pi_1(\hat\mu)=\tfrac12\bigl(e_0+i\hat\mu\bigr) , \qquad \hat\mu\in\mathbb{R}^{3},\ (\hat\mu,\hat\mu)=1 ,
$$

where $\hat\mu=\sum_{k=1}^{3}\hat\mu_ke_k$ ranges over the real vectors of the vector subspace with $(\hat\mu,\hat\mu)=\sum_k\hat\mu_k^{2}=1$. There are no others.

*Proof.* By the reduction the idempotents of the block are the Hermitian elements with $\tilde\Pi^{2}=\tilde\Pi$. A Hermitian element is $\tilde\Pi=\alpha e_0+i\mathbf w$ with $\alpha\in\mathbb{R}$ and $\mathbf w$ a real vector, and its square in the algebra is

$$
\tilde\Pi^{2}=\alpha^{2}e_0+2\alpha\,i\mathbf w+(i\mathbf w)^{2}=\bigl(\alpha^{2}+\lvert\mathbf w\rvert^{2}\bigr)e_0+2\alpha\,i\mathbf w ,
$$

since $\mathbf w^{2}=-\lvert\mathbf w\rvert^{2}e_0$ and $(i\mathbf w)^{2}=i^{2}\mathbf w^{2}=\lvert\mathbf w\rvert^{2}e_0$. Equating this to $\tilde\Pi=\alpha e_0+i\mathbf w$ splits the equation into the vector part $(2\alpha-1)\mathbf w=0$ and the scalar part $\alpha^{2}+\lvert\mathbf w\rvert^{2}=\alpha$. If $\mathbf w=0$ the scalar equation is $\alpha^{2}=\alpha$, so $\alpha=0$ or $\alpha=1$, giving the trivial idempotents $0$ and $e_0$. If $\mathbf w\neq0$ then $\alpha=\tfrac12$, the scalar equation gives $\lvert\mathbf w\rvert^{2}=\tfrac14$, and writing $\mathbf w=\tfrac12\hat\mu$ with $(\hat\mu,\hat\mu)=1$ gives $\tilde\Pi=\tfrac12(e_0+i\hat\mu)$. No other case occurs, and every listed element is a Hermitian idempotent of the algebra and therefore an idempotent of the block.

**Remark.** The word **projection** is used for a Hermitian idempotent of the algebra and for nothing else, and the idempotents of the block are exactly the projections of $\mathbb{B}$; the name *pure state* of *Idempotents of the General Plain Algebra* is the same element read in the Hermitian subspace. The two families of algebra idempotents that are not Hermitian are the ones the block discards, and they are treated in §*The Contrast With the Algebra*.

### The Coordinates

**Proposition (the coordinate form).** For a real vector $\hat\mu$ with $(\hat\mu,\hat\mu)=1$ and coordinates $\hat\mu_k\in\mathbb{R}$,

$$
\tilde\Pi_1(\hat\mu)=\tfrac12e_0+\tfrac{i}{2}\sum_{k=1}^{3}\hat\mu_ke_k ,
$$

so its scalar part is $\tfrac12$, its vector part is $\tfrac{i}{2}\hat\mu$, and its four coordinates are $\bigl(\tfrac12,\tfrac{i}{2}\hat\mu_1,\tfrac{i}{2}\hat\mu_2,\tfrac{i}{2}\hat\mu_3\bigr)$. Its scalar part is the sum of the modulus squares of its coordinates,

$$
\tfrac12=\tfrac14+\tfrac14\sum_k\hat\mu_k^{2},
$$

which is the scalar-part identity of the reduction read on this family.

*Proof.* The coordinates are read from the display, and $\sum_k\hat\mu_k^{2}=1$ gives the scalar-part identity $\Pi_0=\sum_\mu\lvert\Pi_\mu\rvert^{2}$.

**Remark.** The scalar part $\tfrac12$ is forced by the normalisation $(\hat\mu,\hat\mu)=1$ and is the same for the whole family; the family is the whole set of the projections and not a proper subfamily of it.

### The Complement and the Pairing of the Directions

**Proposition (the complement is the antipode).** For every real vector $\hat\mu$ with $(\hat\mu,\hat\mu)=1$,

$$
e_0-\tilde\Pi_1(\hat\mu)=\tilde\Pi_1(-\hat\mu),
$$

and the two are idempotents of the algebra, orthogonal and summing to the unit,

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(-\hat\mu)=0 , \qquad \tilde\Pi_1(\hat\mu)+\tilde\Pi_1(-\hat\mu)=e_0 .
$$

*Proof.* The first identity is $e_0-\tfrac12(e_0+i\hat\mu)=\tfrac12(e_0-i\hat\mu)=\tilde\Pi_1(-\hat\mu)$. For the orthogonality, multiply out, using $\hat\mu^{2}=-(\hat\mu,\hat\mu)e_0=-e_0$:

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(-\hat\mu)=\tfrac14\bigl(e_0+i\hat\mu\bigr)\bigl(e_0-i\hat\mu\bigr)=\tfrac14\bigl(e_0-(i\hat\mu)^{2}\bigr)=\tfrac14\bigl(e_0+\hat\mu^{2}\bigr)=\tfrac14\bigl(e_0-e_0\bigr)=0 ,
$$

and the sum is immediate.

**Proposition (when two projections are orthogonal).** For real vectors $\hat\mu,\hat\nu$ with $(\hat\mu,\hat\mu)=(\hat\nu,\hat\nu)=1$,

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(\hat\nu)=0 \quad\Longleftrightarrow\quad \hat\nu=-\hat\mu .
$$

*Proof.* Multiplying out and using $\hat\mu\hat\nu=-(\hat\mu,\hat\nu)e_0+\hat\mu\times\hat\nu$ for the product of two pure real vectors gives

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(\hat\nu)=\tfrac14\Bigl(\bigl(1+(\hat\mu,\hat\nu)\bigr)e_0-\hat\mu\times\hat\nu+i\bigl(\hat\mu+\hat\nu\bigr)\Bigr).
$$

The scalar part vanishes when $(\hat\mu,\hat\nu)=-1$, and for two real unit vectors this forces $\hat\nu=-\hat\mu$, because then $(\hat\mu+\hat\nu,\hat\mu+\hat\nu)=(\hat\mu,\hat\mu)+2(\hat\mu,\hat\nu)+(\hat\nu,\hat\nu)=0$ and a real vector whose square vanishes is zero. With $\hat\nu=-\hat\mu$ the vector part is $-\hat\mu\times(-\hat\mu)+i(\hat\mu-\hat\mu)=0$ as well. Conversely $\hat\nu=-\hat\mu$ gives $0$ by the previous proposition.

**Remark.** Orthogonality is therefore as sparse as it can be: a projection is orthogonal, as an algebra idempotent, to one other projection of the family and to no third one, so the family is a family of complementary pairs and not an orthogonal set. The Peirce decomposition of the algebra relative to the standard pair is *Ideals and Peirce Decomposition of the General Plain Algebra*.

### The Standard Pair

**Example.** The two projections at the directions $\pm e_3$ are the standard idempotents of the algebra,

$$
\tilde\Pi_1(\hat e_3)=\tfrac12(e_0+ie_3)=\tilde\Pi_1 , \qquad \tilde\Pi_1(-\hat e_3)=\tfrac12(e_0-ie_3)=\tilde\Pi_2 ,
$$

and they are the images under $\mathsf{M}_2$ of the two diagonal matrix units of the matrix model: $\tilde\Pi_1(\hat e_3)$ corresponds to $E_{11}$ and $\tilde\Pi_1(-\hat e_3)$ to $E_{22}$, as the transport of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* records. Since the equalities are equalities in the algebra, they hold for the block as well, a Hermitian element having the same square in the two products.

### The Halving Map and the Bijection With the Roots of One

**Theorem (the idempotents of the block are the halved Hermitian roots of $+1$).** The map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the Hermitian roots of $+1$ onto the idempotents of the block, with inverse $\tilde\Xi=2\tilde\Pi-e_0$,

$$
0=\tfrac12(e_0-e_0),\qquad e_0=\tfrac12(e_0+e_0),\qquad \tfrac12(e_0+i\hat\mu),\ \ \hat\mu\in\mathbb{R}^{3},\ (\hat\mu,\hat\mu)=1 .
$$

*Proof.* A Hermitian root $\tilde\Xi$ of $+1$ satisfies $\tilde\Xi^{*}=\tilde\Xi$ and $\tilde\Xi^{2}=\tilde\Xi\tilde\Xi^{*}=e_0$, so $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ is Hermitian and has square $\tfrac14(e_0+2\tilde\Xi+\tilde\Xi^{2})=\tfrac14(2e_0+2\tilde\Xi)=\tilde\Pi$: it is a Hermitian idempotent of the algebra, hence an idempotent of the block by the reduction. Conversely an idempotent $\tilde\Pi$ of the block is a Hermitian idempotent of the algebra, and $\tilde\Xi=2\tilde\Pi-e_0$ is Hermitian with square $(2\tilde\Pi-e_0)^{2}=4\tilde\Pi-4\tilde\Pi+e_0=e_0$, a Hermitian root of $+1$. The two maps are inverse, and the list is the classification of §*The Hermitian Roots of One* and §*The Classification*.

**Remark (the family and the pair).** The halving map carries the two trivial Hermitian roots $\pm e_0$ to the trivial idempotents $e_0$ and $0$, and the family $i\hat\mu$ to the projections; the pair $\{\tilde\Xi,-\tilde\Xi\}$ of Hermitian roots becomes the complementary pair $\{\tilde\Pi,e_0-\tilde\Pi\}$ of idempotents, which is the pair of antipodal directions of §*The Complement and the Pairing of the Directions*. The Hermitian roots of $+1$ are the spine of the idempotent theory.

### The Contrast With the Algebra

**The idempotents of the algebra are the halving map applied to its own roots of $+1$, a real four-parameter family together with the trivial pair; the idempotents of the block are the Hermitian ones, so the two sets agree exactly on the trivial pair and the projections, and every non-Hermitian idempotent of the algebra is dropped by the block.**

The idempotents of the associative product are the elements $\tilde\Pi=\tfrac12(e_0+\tilde\Sigma)$ over the roots $\tilde\Sigma$ of $+1$ of the algebra, $\tilde\Sigma^{2}=e_0$, by the halving map of *Square Roots of One and the Idempotents of the General Plain Algebra*, where those roots are classified; the map $\tilde\Sigma\mapsto\tilde\Pi$ is a bijection from the algebra's roots of $+1$ onto its idempotents, and the non-trivial roots give the non-trivial idempotents, a real four-parameter family. The block's idempotents are the **Hermitian** idempotents of the algebra, by the reduction, and they are the subfamily with $\tilde\Sigma$ Hermitian.

| idempotent set | description | size |
|---|---|---|
| of the associative product $\tilde P\tilde Q$ | the elements $\tfrac12(e_0+\tilde\Sigma)$ over the roots $\tilde\Sigma$ of $+1$ of the algebra | a real four-parameter family together with two isolated points |
| of the block $\star$ | the trivial pair and the projections $\tilde\Pi_1(\hat\mu)$ over the real unit vectors | a real two-parameter family together with two isolated points |
| in common | the trivial pair $0,e_0$ and the projections | the whole block set |

**Example (the simplest non-Hermitian idempotent).** Take the root of $+1$ of the algebra $\tilde\Sigma=\sqrt2\,ie_1-e_2$, so that $\tilde\Sigma^{2}=e_0$ and

$$
\tilde\Pi=\tfrac12(e_0+\tilde\Sigma)=\tfrac12e_0+\tfrac12\bigl(\sqrt2\,ie_1-e_2\bigr)
$$

is an idempotent of the algebra, not Hermitian: $\tilde\Sigma^{*}=\sqrt2\,ie_1+e_2\neq\tilde\Sigma$, so $\tilde\Pi^{*}\neq\tilde\Pi$. Its square in the block is

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi\tilde\Pi^{*}=e_0+\tfrac{\sqrt2}{2}\,ie_1+\tfrac{\sqrt2}{2}\,ie_3\neq\tilde\Pi .
$$

*Proof.* The idempotence for the algebra is the halving map at the root $\tilde\Sigma$ of $+1$; the failure of Hermitianness is read from $\tilde\Sigma^{*}=\sqrt2\,ie_1+e_2$. For the square, $\tilde\Pi\tilde\Pi^{*}=\tfrac14(e_0+\tilde\Sigma)(e_0+\tilde\Sigma^{*})=\tfrac14(e_0+\tilde\Sigma+\tilde\Sigma^{*}+\tilde\Sigma\tilde\Sigma^{*})$. Here $\tilde\Sigma+\tilde\Sigma^{*}=2\sqrt2\,ie_1$ and

$$
\tilde\Sigma\tilde\Sigma^{*}=\bigl(\sqrt2\,ie_1-e_2\bigr)\bigl(\sqrt2\,ie_1+e_2\bigr)=3e_0+2\sqrt2\,ie_3 ,
$$

by the multiplication of the basis, so the sum is $\tfrac14(4e_0+2\sqrt2\,ie_1+2\sqrt2\,ie_3)=e_0+\tfrac{\sqrt2}{2}ie_1+\tfrac{\sqrt2}{2}ie_3$, which differs from $\tilde\Pi$.

**Remark.** The element is the distinguishing case of *Introduction to the General Plain Sesqualgebra of Biquaternions*: it is idempotent for the bilinear product and not for the sesquilinear one. Its scalar part is $\tfrac12$, but $\mathrm{Sc}(\tilde\Pi\star\tilde\Pi)=1$, so the scalar-part identity of §*The Reduction* fails at the same element, which is a second reading of the same failure.

### The Matrix Model

**Under the isomorphism $\mathsf{M}_2$ the projections are the rank-one Hermitian idempotents of $M_2(\mathbb{C})$, $\mathsf{M}_2(\tilde\Pi_1(\hat\mu))=\tfrac12(I+i\mathsf{M}_2(\hat\mu))$, and the family is exactly the set of those idempotents.**

**Proposition.** Under the isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, which satisfies $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$ and $\mathsf{M}_2(\tilde P\tilde Q^{*})=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$, the projections are the rank-one Hermitian idempotents of the matrix algebra,

$$
\mathsf{M}_2\bigl(\tilde\Pi_1(\hat\mu)\bigr)=\tfrac12\bigl(I+i\mathsf{M}_2(\hat\mu)\bigr),
$$

and the family is the set of the rank-one Hermitian idempotents of $M_2(\mathbb{C})$.

*Proof.* The image of a Hermitian idempotent is Hermitian, $\mathsf{M}_2(\tilde\Pi)^{\dagger}=\mathsf{M}_2(\tilde\Pi^{*})=\mathsf{M}_2(\tilde\Pi)$, and idempotent, $\mathsf{M}_2(\tilde\Pi)^{2}=\mathsf{M}_2(\tilde\Pi^{2})=\mathsf{M}_2(\tilde\Pi)$. The image of $\tilde\Pi_1(\hat\mu)$ is computed from $\mathsf{M}_2(\tilde Q)=\sum_\mu Q_\mu\mathsf{M}_2(e_\mu)$ on the coordinates of §*The Coordinates*, and $\mathsf{M}_2(i\hat\mu)=i\mathsf{M}_2(\hat\mu)$ because $\mathsf{M}_2$ is $\mathbb{C}$-linear. The matrices $i\mathsf{M}_2(e_1),i\mathsf{M}_2(e_2),i\mathsf{M}_2(e_3)$ are Hermitian, traceless and $i\mathsf{M}_2(e_k)^{2}=I$, and they form a real basis of the traceless Hermitian matrices; hence $i\mathsf{M}_2(\hat\mu)=\sum_k\hat\mu_k\,i\mathsf{M}_2(e_k)$ is traceless Hermitian with square $(\hat\mu,\hat\mu)I$, and for $(\hat\mu,\hat\mu)=1$ the element $\tfrac12(I+i\mathsf{M}_2(\hat\mu))$ is a Hermitian idempotent of rank one because its trace is one. Conversely every rank-one Hermitian idempotent of $M_2(\mathbb{C})$ is $\tfrac12(I+H)$ with $H$ traceless Hermitian and $H^{2}=I$, and every such $H$ is $i\mathsf{M}_2(\hat\mu)$ for a real vector $\hat\mu$ with $(\hat\mu,\hat\mu)=1$.

**Remark.** The matrix image is the standard rank-one projection of a two-dimensional space, and the parametrisation by the real unit vectors $\hat\mu$ is the parametrisation of those projections by the traceless Hermitian involutions. The standard pair is $\mathsf{M}_2(\tilde\Pi_1)=E_{11}$ and $\mathsf{M}_2(\tilde\Pi_2)=E_{22}$.

### The Operator Interpretation

**An element idempotent for $\star$ has its right multiplication $R^{\star}_{\tilde\Pi}$ a projector, while its left multiplication is a projector only for $\tilde\Pi=0$; the elements whose right multiplication is a projector are the idempotents of the plain product, a family of complex dimension two that strictly contains the idempotents of the block.**

The idempotents of the block are a class of **elements**, and they must not be confused with the projectors of the block, which are a class of **operators**. An element idempotent for the block gives a projector under its right multiplication, and the converse fails, because the right projectors are the idempotents of the **plain** product; on the left the only projector is the zero operator.

**Corollary (idempotent elements and their operators).** An element $\tilde\Pi$ idempotent for $\star$ has $R^{\star}_{\tilde\Pi}$ a projector, because $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ gives $(R^{\star}_{\tilde\Pi})^{2}=R^{\star}_{\tilde\Pi}$. The left multiplication is **not** a projector unless $\tilde\Pi=0$. The elements whose right multiplication is a projector are the idempotents of the **plain** product, a family of complex dimension two, and they strictly contain the idempotents of the block.

*Proof.* The operator statement on the right is the right-composition law $R^{\star}_{\tilde P}R^{\star}_{\tilde Q}=R^{\star}_{\tilde P\tilde Q}$ read at $\tilde P=\tilde Q=\tilde\Pi$ (*The Specificities of the General Plain Sesqualgebra*). The class of the projectors is the projector criterion of the same article: $R^{\star}_{\tilde P}$ is a projector exactly when $\tilde P$ is a plain idempotent, and the plain idempotents are the halved plain roots of $+1$, a complex quadric of which the block's idempotents are the Hermitian subfamily of real dimension two. On the left there is no composition law, and a conjugate-linear projector is the zero operator, so $L^{\star}_{\tilde\Pi}$ is a projector only for $\tilde\Pi=0$.

**Remark (the half that the block keeps).** On the element level the block keeps the Hermitian idempotents and drops the rest; on the operator level the right multiplications recover the whole plain idempotent set, read at the conjugated index. The gap between the two is the gap between the block's element theory and its right-operator theory, and it is the mirror of the gap that the general quaternionic product shows on its left side. The projectors themselves, their images and their kernels, are treated in the operator articles of the block.

## Summary

The square of an element of the general plain sesqualgebra is the Hermitian element $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}=(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2})e_0+2i(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v)$ in the real halves $\tilde\Xi=q_r+iq_i$, whose scalar part is the definite quantity $\sum_\mu\lvert\Xi_\mu\rvert^{2}$. The scalar part decides the central values: no negative real or non-real scalar has a root, the scalar part being non-negative, and **plus one has a root**, the root set being exactly the family $e^{i\theta}w$ over the real unit quaternions $w$, that is $U(1)\cdot S^{3}$, a single real four-parameter family containing $e_0$, $-e_0$ and the pure imaginary unit vectors $i\hat\mu$. The **Hermitian** roots of $+1$ are $\pm e_0$ and the $i\hat\mu$, and the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from them onto the idempotents of the block, which are $0$, $e_0$ and the $\tfrac12(e_0+i\hat\mu)$: an element is idempotent for the block exactly when it is a Hermitian idempotent of the algebra, the complement of a projection is the antipodal projection, and under the matrix model the family is the set of the rank-one Hermitian idempotents.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the block |
| $\tilde\Xi=q_r+iq_i$ | the imaginary decomposition, $q_r,q_i$ real quaternions |
| $\mathbf u,\mathbf v$ | the vector parts of $q_r,q_i$ |
| $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}$ | the Hermitian square |
| $\mathrm{Sc}(\tilde\Xi\star\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$ | the scalar part, definite |
| $H(\tilde\Xi)=\mathrm{Sc}(\tilde\Xi\star\tilde\Xi)$ | the algebraic norm of the block, the scalar part of the square |
| $C(\tilde\Xi)=\tilde\Xi\tilde\Xi^{\natural}=\sum_\mu\Xi_\mu^{2}$ | the central square, the zero-divisor criterion |
| $U(1)\cdot S^{3}=\{e^{i\theta}w\}$ | the roots of $+1$, real dimension four |
| $\pm e_0,\ i\hat\mu$ | the Hermitian roots of $+1$ |
| $\tilde\Pi$ | an idempotent, a Hermitian idempotent of the algebra |
| $\tilde\Pi_1(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ | the projections, $\hat\mu$ a real vector with $(\hat\mu,\hat\mu)=1$ |
| $\tfrac12(e_0+\tilde\Xi)$, $\tilde\Xi=2\tilde\Pi-e_0$ | the halving map and its inverse |
| $\tilde\Sigma^{2}=e_0$ | a root of $+1$ of the algebra |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$ |
| $E_{11},E_{22}$ | the diagonal matrix units, $\mathsf{M}_2(\tilde\Pi_1),\mathsf{M}_2(\tilde\Pi_2)$ |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, its class, its two slot involutions and the positive cone of the square that the reduction uses.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the root, the idempotent, the projection and the Peirce decomposition.
- *Norm and Invertibility in the General Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-sesqualgebra.md`), for the algebraic norm, the square and the definiteness of its scalar part.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the positive cone that the square of the block generates.
- *Square Roots of a General Element in the General Plain Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-sesqualgebra.md`), for the general reduction of the root equation of which the roots of $+1$ are one central case.
- *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-sesqualgebra.md`), for the roots of $0$, which the same square excludes, and the nilpotents of index three.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra.md`), for the parent's roots of $+1$ and the halving map, whose Hermitian half is the set computed here.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), for the idempotents of the associative product, whose Hermitian half the block keeps.
- *Zero Divisors of the General Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-plain-sesqualgebra.md`), for the criterion $C=0$ that no root of $+1$ satisfies and among which the projections sit.
- *The Specificities of the General Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-general-plain-sesqualgebra.md`), for the right-composition law and the projector criterion whose projector family is the whole plain idempotent set.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model in which the projections are the rank-one Hermitian idempotents $E_{11},E_{22}$ and their conjugates.
