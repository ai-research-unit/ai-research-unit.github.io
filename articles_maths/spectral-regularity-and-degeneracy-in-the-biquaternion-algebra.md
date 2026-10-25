# __Spectral Regularity and Degeneracy in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries two quadratic conditions. The first is the reduced norm $N(\tilde Q)=Q_t^2+B^2$, with $B^2=Q_x^2+Q_y^2+Q_z^2$. Its zero locus is the null cone of the reduced norm; the norm is multiplicative and decides invertibility: that is *Norm Regularity and Degeneracy in the Biquaternion Algebra*. The second is $B^2$ itself, the square of the vector part. Its zero locus is the **spectral-degenerate cone** $\mathcal S$; the cone is not multiplicative, and it decides whether the two eigenvalues of the element can be told apart.

The article states the eigenvalue problem without a module or an acting operator. An eigenvalue is a scalar for which a left ideal is proper, an eigenvector is an element of a left annihilator, and a spectral idempotent is a Peirce idempotent adapted to the element. On that vocabulary the spectral criterion is proved: $\lambda$ is an eigenvalue of $\tilde Q$ exactly when $N(\tilde Q-\lambda e_t)=0$. The characteristic polynomial follows, with discriminant $-4B^2$, and the degenerate side $\mathcal S$ is stratified into three regimes: scalar, Jordan and nilpotent. The adapted Peirce decomposition is shown to exist exactly on the non-scalar side where $B^2\neq0$, and to fail on the Jordan and nilpotent regimes. The last sections show that the two degeneration loci are independent: a zero divisor can have distinct eigenvalues, and a unit can have a repeated one. They also give the two operator readings of the cones: the sandwich is singular exactly on the null cone, and the inner derivation is nilpotent exactly on the spectral-degenerate cone.

**Scope and naming.** The two problems are the two quadratic problems of the algebra. The norm problem asks whether the element can be inverted; its degeneration locus is the null cone $\mathcal{N}=\{N=0\}$. The spectral problem asks whether the two eigenvalues can be separated; its degeneration locus is $\mathcal S=\{B^2=0\}$. Three naming rules are held throughout. First, $\mathcal{N}$ is the **null cone of the reduced norm**, qualified at first use, and then the null cone. Second, $\mathcal S$ is the **spectral-degenerate cone** and is never called a null cone: $B^2$ is the square of the vector part, not a norm on $\mathbb{B}$, so $\mathcal S$ is not the null cone of a norm on the algebra. Third, unqualified **regular** means **spectrally regular**, that is $B^2\neq0$; the companion article's regular side, the unit group, is written **norm-regular** wherever the two could collide.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$, and with complex coefficients. The natural conjugation is the $\mathbb{C}$-linear quaternion conjugation $\tilde Q^{\natural}=Q_t-\vec Q$, an anti-involution of order two fixing the centre. The vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t,\qquad N(\tilde Q)=\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}=(Q_t^2+B^2)e_t.
$$

The number $B$ is a fixed complex square root of $Q_x^2+Q_y^2+Q_z^2$; the other root only exchanges the two eigenvalues. The algebra and its conventions are *The Biquaternion Algebra and Its Vector Spaces*; the eigenvalue decomposition, the normality criterion and the spectral theorem are *The Biquaternion Eigenvalue Decomposition*; the Peirce decomposition is *Ideals and Peirce Decompositions of the Biquaternion Algebra*.

## The Spectral Criterion

**Definition (eigenvalue).** A scalar $\lambda\in\mathbb{C}$ is an **eigenvalue** of $\tilde Q$ if the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, that is $\mathbb{B}(\tilde Q-\lambda e_t)\neq\mathbb{B}$.

**Definition (eigenvector).** A non-zero $v\in\mathbb{B}$ is an **eigenvector** of $\tilde Q$ for $\lambda$ if $(\tilde Q-\lambda e_t)v=0$. The eigenvectors for $\lambda$, with the origin, are the left annihilator

$$
\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)=\{v:\ (\tilde Q-\lambda e_t)v=0\},
$$

which is a right ideal of $\mathbb{B}$.

**Definition (spectral idempotent).** A non-zero idempotent $e$ is a **spectral idempotent** of $\tilde Q$ if $e\tilde Q=\tilde Qe=\lambda e$ for some scalar $\lambda$.

**Definition (spectral decomposition).** A **spectral decomposition** of $\tilde Q$ is a pair of orthogonal idempotents $e_+,e_-$ with

$$
e_++e_-=e_t,\qquad e_+e_-=0,\qquad \tilde Qe_\pm=\lambda_\pm e_\pm,\qquad \lambda_+\neq\lambda_-.
$$

No module and no acting operator enters the definitions: the primitives are the left ideal, the left annihilator and the idempotent.

**Theorem (the spectral criterion).** For $\tilde Q\in\mathbb{B}$ and $\lambda\in\mathbb{C}$, the following are equivalent:

1. $\lambda$ is an eigenvalue of $\tilde Q$;
2. $\tilde Q-\lambda e_t$ is not a unit of the plain product;
3. $N(\tilde Q-\lambda e_t)=0$.

*Proof.* Write $a=\tilde Q-\lambda e_t$.

*(1)$\iff$(2).* If $a$ is a unit then $\mathbb{B}a=\mathbb{B}$, and the left ideal is not proper. Conversely, if $\mathbb{B}a=\mathbb{B}$, then $e_t=xa$ for some $x$, so $x$ is a left inverse of $a$. The left multiplication by $a$ is then injective: $ay=0$ gives $y=xay=0$. In finite dimension an injective endomorphism is bijective, so there is $b$ with $ab=e_t$; then

$$
x=x e_t=x(ab)=(xa)b=e_tb=b,
$$

and $a$ has the two-sided inverse $b$. Hence a proper left ideal forces a non-unit.

*(2)$\iff$(3).* If $a$ is not a unit, the left multiplication by $a$ is not surjective, since a surjective endomorphism of the finite-dimensional space $\mathbb{B}$ is bijective and would give a right inverse, hence a unit. By rank–nullity there is $v\neq0$ with $av=0$; then

$$
N(a)v=a^{\natural}av=0,
$$

and $N(a)$ is central, so $N(a)=0$. Conversely, if $a$ were a unit $u$ and $N(a)=0$, then $N(a)N(u)=N(e_t)=1$ by multiplicativity, a contradiction.

**Corollary (the characteristic polynomial).** For every $\lambda$,

$$
N(\tilde Q-\lambda e_t)=(\lambda-Q_t)^2+B^2,
$$

so the characteristic polynomial is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+N(\tilde Q),
$$

of discriminant

$$
\operatorname{disc}p_{\tilde Q}=4Q_t^2-4N(\tilde Q)=-4B^2.
$$

The eigenvalues are

$$
\lambda_\pm=Q_t\pm iB,
$$

and they coincide exactly when $B=0$, that is exactly when $B^2=0$.

**Corollary (the eigenspaces).** For a non-scalar $\tilde Q$ and each eigenvalue $\lambda$, the eigenspace $\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)$ is a right ideal of complex dimension $2$. For $\tilde Q=Q_te_t$ the only eigenvalue is $Q_t$, and its eigenspace is all of $\mathbb{B}$.

*Proof.* A non-zero non-unit in $\mathbb{B}$ has left multiplication of complex rank $2$, by *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Annihilators*; at the scalar the difference $\tilde Q-Q_te_t$ is zero.

**Corollary (Cayley–Hamilton and the inverse).** Every $\tilde Q$ satisfies

$$
\tilde Q^2-2Q_t\tilde Q+N(\tilde Q)e_t=0 ,
$$

and if $N(\tilde Q)\neq0$ then $\tilde Q^{-1}=(2Q_te_t-\tilde Q)/N(\tilde Q)=\tilde Q^{\natural}/N(\tilde Q)$.

*Proof.* With $\tilde Q=Q_te_t+\vec Q$ and $\vec Q^2=-B^2e_t$, $\tilde Q^2=Q_t^2e_t+2Q_t\vec Q-B^2e_t=2Q_t\tilde Q-(Q_t^2+B^2)e_t$. Multiplying by $\tilde Q^{\natural}$ and using $N(\tilde Q)=Q_t^2+B^2$ gives the inverse.

**Remark (left and right eigenvalues).** The centre of $\mathbb{B}$ is $\mathbb{C}$, so complex scalars commute with every element. A left eigenvalue, $\tilde Qv=\lambda v$, and a right eigenvalue, $\tilde Qv=v\lambda$, therefore define the same set when the scalar is required to lie in $\mathbb{C}$, and that set is $\sigma(\tilde Q)$. The distinction between the two eigenvalue problems, which is genuine over a noncommutative division ring (*Quaternion Spectral Theory*, §*The Spectrum of a Quaternion*), collapses here.

## Similarity Classes and the Eigenvalue Dichotomy

**Definition.** Two biquaternions $\tilde Q_1,\tilde Q_2$ are **similar** if $\tilde Q_2=S\tilde Q_1S^{-1}$ for some unit $S\in\mathbb{B}$.

**Theorem (the classification).** Let $T=2Q_t$ and $D=N(\tilde Q)$, and let $\Delta=T^2-4D=-4B^2$.

1. If $B\neq0$, the eigenvalues $Q_t\pm iB$ are distinct, and the similarity class is determined by the unordered pair of eigenvalues, equivalently by $(T,D)$.
2. If $B=0$, the only eigenvalue is $Q_t$, and exactly two similarity classes share $(T,D)=(2Q_t,Q_t^2)$: the **central class** $\tilde Q=Q_te_t$, and the **non-semisimple class** $\vec Q\neq0$ with $\vec Q^2=0$, which is similar to the Jordan block with diagonal $Q_t$.

*Proof.* (1) $p_{\tilde Q}$ has two distinct roots, so $\tilde Q$ is diagonalisable with those roots; any two such elements are conjugate in $\mathbb{B}\cong M_2(\mathbb{C})$. (2) $B=0$ gives $\vec Q^2=0$. If $\vec Q=0$ the element is central. If $\vec Q\neq0$, then $\tilde Q-Q_te_t$ is nonzero with square $0$, so the minimal polynomial is $(X-Q_t)^2$ and the Jordan form is a single block of size $2$; all such elements are conjugate.

**Corollary.** In the non-semisimple class the element is a zero divisor exactly when $Q_t=0$, since $N(\tilde Q)=Q_t^2$.

## The Spectral-Degenerate Cone

**Definition.** The **spectral-degenerate cone** is

$$
\mathcal S=\{B^2=0\}=\{\vec Q^2=0\}=\{\operatorname{disc}p_{\tilde Q}=0\}.
$$

**Theorem (three readings of one equation).** The equation $B^2=0$ is simultaneously:

- **geometric:** the vector part is isotropic for the quaternionic bilinear form, $\langle\vec Q,\vec Q\rangle_{\natural}=Q_x^2+Q_y^2+Q_z^2=0$;
- **algebraic:** the vector part is square-zero, $\vec Q^2=0$, hence nilpotent of index two when it is non-zero;
- **spectral:** the discriminant vanishes, and the two eigenvalues coalesce at $Q_t$.

**Theorem (the geometry).** The cone is the product of the scalar line and the isotropic cone of the vector subspace,

$$
\mathcal S=\mathbb{C}e_t\times\{\vec Q\in\operatorname{Vect}(\mathbb{B}):\vec Q^2=0\}.
$$

It is a complex cone of complex dimension $3$ and real dimension $6$. Its singular locus is the **vertex** $\{\vec Q=0\}$, the whole scalar line; off the vertex it is a smooth hypersurface.

*Proof.* The equation $B^2=0$ is one complex equation in the four complex coefficients, homogeneous of degree two. Its gradient with respect to $(Q_t,Q_x,Q_y,Q_z)$ is

$$
(0,\,2Q_x,\,2Q_y,\,2Q_z),
$$

which vanishes exactly when $\vec Q=0$. Off the vertex the gradient is non-zero and the equation cuts a smooth hypersurface, of complex dimension $4-1=3$ and real dimension $8-2=6$. On the vertex the cone is $\mathbb{C}e_t\times C$, with $C$ the isotropic cone of $\mathbb{C}^3$, which is singular at its apex; the product is singular along the whole line.

**The cone is not a subspace.** The elements $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ lie on $\mathcal S$, since their vector squares are $1+i^2=0$, but their sum $2\vec e_x$ has $B^2=4$ and lies off it.

**Warning (the vertex is not defective).** A point of the vertex is a scalar $\tilde Q=Q_te_t$. Its only eigenvalue is $Q_t$, repeated, and its minimal polynomial is $X-Q_t$: it is semisimple and diagonalisable. The cone $\mathcal S$ is therefore the set of elements with a repeated eigenvalue, not the set of non-diagonalisable elements. The defective elements of $\mathcal S$ are the Jordan and nilpotent regimes of §*The Three Regimes of the Cone*. This distinction is invisible in the equation $B^2=0$.

**Warning (the name).** The form $B^2$ is the restriction of the quaternionic bilinear algebraic norm to the vector subspace. It does not see the scalar part, so it is degenerate as a form on $\mathbb{B}$ and is not a norm on $\mathbb{B}$. The only multiplicative norm of the algebra is the reduced norm $N$, whose null cone is $\mathcal{N}$. The cone $\mathcal S$ is the zero set of a quadratic form that does not involve $Q_t$, and it is never called a null cone.

## The Adapted Peirce Decomposition

**Two Peirce objects.** Let $e$ be an idempotent and $f=e_t-e$. The **weak Peirce decomposition** of an element $X$ is

$$
X=eXe+eXf+fXe+fXf,
$$

and it holds for every $X$ and every idempotent $e$: its availability is a property of the algebra, not of $X$. The **adapted Peirce decomposition** of $\tilde Q$ relative to $e$ is the stronger statement that the two off-diagonal components vanish,

$$
e\tilde Qf=f\tilde Qe=0,
$$

which is equivalent to $e\tilde Q=\tilde Qe$: the idempotent commutes with the element. The equivalence uses that the algebra is split: every non-trivial idempotent of $\mathbb{B}$ is primitive, by *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*Idempotents and Orthogonal Idempotents*, so its corner $e\mathbb{B}e$ is a finite-dimensional complex division algebra, hence $\mathbb{C}e$. Then $e\tilde Q=\tilde Qe$ forces $\tilde Qe\in\mathbb{C}e$ and $\tilde Qf\in\mathbb{C}f$, and the two off-diagonal blocks vanish.

**Theorem (existence).** Let $\tilde Q$ be non-scalar. The following are equivalent:

1. $B^2\neq0$;
2. $\tilde Q$ has a spectral decomposition;
3. there is a non-trivial idempotent $e$ with $e\tilde Q=\tilde Qe$;
4. $\tilde Q$ is semisimple.

*Proof.* (1)$\Rightarrow$(2). When the eigenvalues are distinct, the Lagrange idempotents

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}
$$

are defined. The algebra identities give

$$
e_\pm^2=e_\pm,\qquad e_+e_-=0,\qquad e_++e_-=e_t,\qquad \tilde Qe_\pm=\lambda_\pm e_\pm,
$$

so they form a spectral decomposition.

(2)$\Rightarrow$(3). The idempotent $e_+$ is non-trivial: if $e_+=0$ then $\tilde Q=\lambda_-e_t$, and if $e_+=e_t$ then $\tilde Q=\lambda_+e_t$; both are contrary to the hypothesis. It commutes with $\tilde Q$ because $\tilde Qe_+=\lambda_+e_+=e_+\tilde Q$.

(3)$\Rightarrow$(1). Suppose $B^2=0$. Since $\tilde Q$ is non-scalar, $\vec Q\neq0$ and $\vec Q^2=0$. The minimal polynomial is then $(X-Q_t)^2$, and the centraliser of $\tilde Q$ is

$$
\mathbb{C}[\tilde Q]=\mathbb{C}[\varepsilon]/(\varepsilon^2),\qquad \varepsilon=\tilde Q-Q_te_t=\vec Q,
$$

by *The Biquaternion Eigenvalue Decomposition*, §*The Degenerate Regimes*. An idempotent $ae_t+b\varepsilon$ satisfies $a^2=a$ and $2ab=b$, so $a=b=0$ or $a=1$, $b=0$: the only idempotents are $0$ and $e_t$, and there is no non-trivial one. Contradiction.

(1)$\iff$(4). For a non-scalar element the minimal polynomial is the characteristic polynomial, of degree two. It is squarefree exactly when the two roots are distinct, that is exactly when $B^2\neq0$.

**Corollary (uniqueness).** If $B^2\neq0$, the spectral decomposition is unique. The centraliser of $\tilde Q$ is $\mathbb{C}[\tilde Q]\cong\mathbb{C}\times\mathbb{C}$, whose only idempotents are $0,e_t,e_+,e_-$, and every adapted Peirce decomposition uses the pair $e_+,e_-$.

*Proof.* The minimal polynomial has two distinct roots, so the Chinese remainder theorem gives $\mathbb{C}[X]/((X-\lambda_+)(X-\lambda_-))\cong\mathbb{C}\times\mathbb{C}$, and the idempotents of the product are the four listed. An idempotent adapted to $\tilde Q$ lies in its centraliser and is therefore one of them.

**The scalar exception.** The theorem excludes the scalar elements, and it must: if $\tilde Q=Q_te_t$ is central, every idempotent commutes with it, so condition (3) holds while $B^2=0$. The scalar regime is treated separately below.

## The Two Cases

**The discriminant of $p_{\tilde Q}=X^2-2Q_tX+N$ is $-4B^2$. The vanishing of $B^2$ therefore cuts the algebra into two spectral cases.**

| case | condition | spectrum | spectral decomposition | eigenbasis |
|---|---|---|---|---|
| **non-degenerate** | $B^2\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | two terms, unique | exists, §*The Q-Adapted Peirce Basis* |
| **degenerate** | $B^2=0$ | one eigenvalue | one term at the vertex, none off it | none |

The non-degenerate case is the complement of the cone $\mathcal S$: it is the spectral-regular case, treated from the Peirce side in §*The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis*. The degenerate case is the cone itself, and its points are classified in §*The Degenerate Case*. The zero element is degenerate, and it is the one degenerate element that is not a zero divisor: it is treated in §*The Zero Element*.

## The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis

**Fix $\tilde Q$ with $Q_x^2+Q_y^2+Q_z^2\neq0$. Its own root carries a Peirce pair, the two mixed corners carry a pair of nilpotents, and the four elements form a basis in which left multiplication by $\tilde Q$ is diagonal. The basis is an eigenbasis of left multiplication; the two minimal left ideals are the eigenspaces of right multiplication, not of left multiplication.** This is the Q-dependent specialisation of the Peirce decomposition of *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Peirce Decompositions*: the four corner lines are the same construction, read relative to the pair of $\tilde Q$'s own root.

### The Root, the Idempotents, and the Eigenvalues

Let
$$
\tilde Q=Q_te_t+\vec Q,\qquad
\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad
Q_x^2+Q_y^2+Q_z^2\neq0,
$$
and fix a square root of $Q_x^2+Q_y^2+Q_z^2$. Define
$$
\vec U=\frac{\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}},\qquad
\vec\Xi=-i\vec U=-\frac{i\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}.
$$
Then
$$
\vec\Xi^2=e_t,\qquad
\tilde\Pi_\pm^2=\tilde\Pi_\pm,\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
$$
and
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$
The pair $(\tilde\Pi_+,\tilde\Pi_-)$ is attached to $\tilde Q$: it is the pair of the root $\vec\Xi$, not an arbitrary pair of idempotents. The signs are fixed by
$$
\vec\Xi\tilde\Pi_\pm=\tilde\Pi_\pm\vec\Xi=\pm\tilde\Pi_\pm,\qquad
\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm.
$$
Choosing the negative square root sends $\vec\Xi$ to $-\vec\Xi$, exchanges $\tilde\Pi_+$ and $\tilde\Pi_-$, and exchanges $\lambda_+$ and $\lambda_-$; the unordered pair and the unordered spectrum are unchanged.

### The Peirce Corners and the Nilpotents

Define the four **Peirce corners**
$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t,\qquad s,t\in\{+,-\}.
$$
Each is one complex line. The two diagonal corners are the lines of the idempotents, and the two mixed corners are square-zero: an element $x\in\mathbb{B}_{st}$ with $s\neq t$ has zero scalar part, because its trace is zero, and its square is zero, because
$$
x^2\in\tilde\Pi_s\mathbb{B}\tilde\Pi_t\tilde\Pi_s\mathbb{B}\tilde\Pi_t=0
\qquad(s\neq t).
$$

**Construction of the two nilpotents.** Choose a nonzero
$$
\vec\Upsilon_+\in\mathbb{B}_{-+}=\tilde\Pi_-\mathbb{B}\tilde\Pi_+.
$$
Consider the map
$$
\mathbb{B}_{+-}\longrightarrow\mathbb{C}\tilde\Pi_-,\qquad x\longmapsto\vec\Upsilon_+x.
$$
It is linear between complex lines, and it is nonzero. Otherwise $\vec\Upsilon_+x=0$ for every $x\in\mathbb{B}_{+-}$, hence $\vec\Upsilon_+\tilde\Pi_-\mathbb{B}\tilde\Pi_-=0$, and then $\mathbb{B}\vec\Upsilon_+\mathbb{B}\tilde\Pi_-=0$. But $\vec\Upsilon_+\neq0$, so the two-sided ideal $\mathbb{B}\vec\Upsilon_+\mathbb{B}$ is the whole simple algebra $\mathbb{B}$, and $\mathbb{B}\tilde\Pi_-\neq0$, a contradiction. A nonzero linear map between complex lines is an isomorphism. Hence there is a unique
$$
\vec\Upsilon_-\in\mathbb{B}_{+-}
\qquad\text{with}\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-.
$$
The other product is then forced. It lies in $\mathbb{C}\tilde\Pi_+$, say $\vec\Upsilon_-\vec\Upsilon_+=\alpha\tilde\Pi_+$, and
$$
\vec\Upsilon_+=\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+(\vec\Upsilon_-\vec\Upsilon_+)=\alpha\vec\Upsilon_+\tilde\Pi_+=\alpha\vec\Upsilon_+,
$$
so $\alpha=1$. Therefore
$$
\boxed{\ \vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0.\ }
$$
**The two-line normalisation.** If one starts from arbitrary nonzero $u\in\mathbb{B}_{-+}$ and $v\in\mathbb{B}_{+-}$, then $uv=c\tilde\Pi_-$ for some $c\neq0$. Choose $\alpha$ with $\alpha^2=c$ and set $\vec\Upsilon_+=u/\alpha$, $\vec\Upsilon_-=v/\alpha$; the argument above applied to $u/\alpha$ and $v/\alpha$ gives $vu=c\tilde\Pi_+$, and the boxed identities hold. This is the same construction read from two arbitrary generators instead of one, and the residual freedom is the reciprocal rescaling of the pair.

The construction from $\vec\Upsilon_+$ alone makes one choice, the nonzero element $\vec\Upsilon_+$ of the line $\mathbb{B}_{-+}$. That choice determines $\vec\Upsilon_-$ uniquely. In that construction no intermediate scalar and no square root enter. A square root appears when the pair is parametrised by two arbitrary generators, as in the two-line normalisation above, or by a transverse vector, as in the closed forms below.

The corners and their generators are collected in the table.

| Corner | Definition | Generator |
|---|---|---|
| $\mathbb{B}_{++}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_+$ | $\tilde\Pi_+$ |
| $\mathbb{B}_{+-}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ | $\vec\Upsilon_-$ |
| $\mathbb{B}_{-+}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$ | $\vec\Upsilon_+$ |
| $\mathbb{B}_{--}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_-$ | $\tilde\Pi_-$ |

**The two signs.** The index is fixed by the left ideal, not by the corner: $\vec\Upsilon_+$ lies in $\mathbb{B}_{-+}$ and, together with $\tilde\Pi_+$, generates $S_+=\mathbb{B}\tilde\Pi_+$; $\vec\Upsilon_-$ lies in $\mathbb{B}_{+-}$ and, together with $\tilde\Pi_-$, generates $S_-=\mathbb{B}\tilde\Pi_-$. Thus
$$
S_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,\qquad
S_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-.
$$

**Uniqueness up to rescaling.** The pair is determined by the products and squares only up to
$$
\vec\Upsilon_+\longmapsto\mu\,\vec\Upsilon_+,\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,\qquad
\mu\in\mathbb{C}^{\times},
$$
which preserves both products and both squares. Indeed, $\mu^{-1}\vec\Upsilon_-$ is the unique element of $\mathbb{B}_{+-}$ whose product with $\mu\vec\Upsilon_+$ is $\tilde\Pi_-$, so the construction forces $\vec\Upsilon_-'=\mu^{-1}\vec\Upsilon_-$. Conversely every pair with the same products and squares arises this way, because the mixed corners are lines. The construction therefore defines the pair up to this one rescaling, and no further choice enters.

**The corner, without a preferred axis.** For every pure biquaternion $\vec X$,
$$
\tilde\Pi_-\vec X\tilde\Pi_+=\frac12\left(\vec X_\perp+i\,\vec U\times\vec X\right)
=\frac12\left(\vec X-\frac{\vec X\cdot\vec Q}{B^2}\vec Q\right)+\frac{i}{4B}\,[\vec Q,\vec X],
$$
$$
\tilde\Pi_+\vec X\tilde\Pi_-=\frac12\left(\vec X_\perp-i\,\vec U\times\vec X\right)
=\frac12\left(\vec X-\frac{\vec X\cdot\vec Q}{B^2}\vec Q\right)-\frac{i}{4B}\,[\vec Q,\vec X],
$$
where $\vec X_\perp=\vec X-\dfrac{\vec X\cdot\vec Q}{B^2}\vec Q$. No axis is singled out. When $\vec X_\perp^2\neq0$ both projections are nonzero.

**The two nilpotents from a transverse vector.** Let $\vec X$ be a pure vector with $\vec X_\perp^2\neq0$, and put
$$
u_+=\tilde\Pi_-\vec X\tilde\Pi_+,\qquad u_-=\tilde\Pi_+\vec X\tilde\Pi_-.
$$
Then
$$
u_+u_-=\vec X_\perp^2\,\tilde\Pi_-,\qquad
u_-u_+=\vec X_\perp^2\,\tilde\Pi_+,\qquad
u_\pm^2=0,
$$
as the expansion of the two projections shows: the cross terms cancel because $\vec X_\perp\cdot(\vec U\times\vec X_\perp)=0$. Then
$$
\vec\Upsilon_\pm=\frac{u_\pm}{\sqrt{\vec X_\perp^2}}
$$
satisfy $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, $\vec\Upsilon_\pm^2=0$. Every admissible pair arises this way, and two choices of $\vec X$ give pairs differing by the reciprocal rescaling. The scalar is
$$
\vec X_\perp^2=\vec X^2+\frac{(\vec X\cdot\vec Q)^2}{B^2}.
$$

**The transverse unit vector.** If $\vec V$ is a pure unit vector with $\vec V\cdot\vec U=0$, then $\vec V\tilde\Pi_+\in\mathbb{B}_{-+}$ and $\vec V\tilde\Pi_-\in\mathbb{B}_{+-}$, and, up to the reciprocal rescaling,
$$
\vec\Upsilon_+=i\,\vec V\tilde\Pi_+,\qquad
\vec\Upsilon_-=i\,\vec V\tilde\Pi_-.
$$
For $\vec V=\vec e_x$ and $\vec U=\vec e_z$ one has $\vec V\tilde\Pi_+=(\vec e_x+i\vec e_y)/2$ and $\vec V\tilde\Pi_-=(\vec e_x-i\vec e_y)/2$, and direct multiplication, using $\vec V^2=-e_t$, gives
$$
(\vec V\tilde\Pi_+)(\vec V\tilde\Pi_-)=-\tilde\Pi_-,
\qquad
(\vec V\tilde\Pi_-)(\vec V\tilde\Pi_+)=-\tilde\Pi_+.
$$
A general transverse unit is $\vec V=\lambda\vec e_x+\mu\vec e_y$ with $\lambda^2+\mu^2=1$; the factor $\lambda-i\mu$ cancels in the normalised pair, so the same products hold. The factor $i$ on both generators restores the plus signs. This is the transverse-vector construction with $\vec X=\vec V$ and $\sqrt{\vec V_\perp^2}=i$.

**The symmetric closed form.** The vector $\vec w=\vec e_x+\vec e_y+\vec e_z$ is the only nonzero vector fixed by every permutation of the axes. Put $\sigma=\vec w\cdot\vec Q=Q_x+Q_y+Q_z$. Then
$$
\vec w_\perp=\vec w-\frac{\Sigma}{B^2}\vec Q,\qquad
\vec w_\perp^2=\vec w^2+\frac{\Sigma^2}{B^2}=-3+\frac{\Sigma^2}{B^2}=\frac{\Sigma^2-3B^2}{B^2}.
$$
Therefore
$$
\boxed{\ \vec\Upsilon_\pm=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}}\ }
$$
with $\vec w=\vec e_x+\vec e_y+\vec e_z$ and $\Sigma=Q_x+Q_y+Q_z$. In full coordinates,
$$
\vec\Upsilon_\pm=\frac{\Bigl(B-\dfrac{\Sigma Q_x}{B}\pm i(Q_y-Q_z)\Bigr)\vec e_x+\Bigl(B-\dfrac{\Sigma Q_y}{B}\pm i(Q_z-Q_x)\Bigr)\vec e_y+\Bigl(B-\dfrac{\Sigma Q_z}{B}\pm i(Q_x-Q_y)\Bigr)\vec e_z}{2\sqrt{\Sigma^2-3B^2}}.
$$
A permutation of the axes permutes the three components and leaves $B$ and $\Sigma$ unchanged, so the formula is symmetric in $x,y,z$. Expanding the brackets gives
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0,
$$
and the denominator is
$$
2\sqrt{\Sigma^2-3B^2}=2\sqrt{-\bigl((Q_x-Q_y)^2+(Q_y-Q_z)^2+(Q_z-Q_x)^2\bigr)}.
$$

**The exceptional cone and the chart.** The symmetric formula degenerates exactly on the cone
$$
\Sigma^2=3B^2,
\qquad\text{that is,}\qquad
(Q_x-Q_y)^2+(Q_y-Q_z)^2+(Q_z-Q_x)^2=0,
$$
which for real $\vec Q$ is the line $Q_x=Q_y=Q_z$. On that cone use the axis chart: for $\mu\in\{x,y,z\}$,
$$
\vec\Upsilon_\pm=\frac{B\,\vec e_\mu-\dfrac{Q_\mu}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_\mu]}{2\sqrt{Q_\mu^2-B^2}},
$$
which is the transverse-vector construction with $\vec X=\vec e_\mu$. The chart with axis $\mu$ is defined when $Q_\mu^2\neq B^2$, that is, when $Q_\nu^2+Q_\rho^2\neq0$ for the two other coordinates. At least one of the three is defined whenever $B\neq0$: if all three failed, then $Q_x^2+Q_y^2=Q_y^2+Q_z^2=Q_z^2+Q_x^2=0$, hence $Q_x^2=Q_y^2=Q_z^2$ and $2Q_x^2=0$, so $B=0$. The charts are the one formula read with $\mu=x,y,z$, and the ones that are defined give pairs differing by the reciprocal rescaling. The symmetric formula off the cone and the axis charts on it cover every $\vec Q$ with $B\neq0$.

**Why no formula is axis-free everywhere.** A closed form with no auxiliary vector would be a map $F$ with $F(R\vec Q)=R\,F(\vec Q)$ for every rotation $R$, rational in $\vec Q$ and $B$. By invariant theory the only such maps are $F(\vec Q)=f(B^2)\vec Q$: the invariant tensors are $\delta_{ij}$ and $\epsilon_{ijk}$, and $\epsilon$ cannot build a vector from a single vector. But the corner is transverse to $\vec Q$, so $F$ would vanish. Every explicit generator therefore uses an auxiliary vector: the symmetric formula uses the permutation-invariant $\vec w$, the axis charts use $\vec e_x,\vec e_y,\vec e_z$. The corner line is a spinor line, and a spinor is not a function of $\vec Q$ alone.

**The standard pair.** For the opposite root, $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, the corner generators of *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Biquaternion Case*, are
$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2}\in\mathbb{B}_{+-},\qquad
\vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2}\in\mathbb{B}_{-+},
$$
with $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-$. These are the $\vec\Upsilon_1,\vec\Upsilon_2$ of *Conventions in Mathematics*, §*The Nilpotent Convention*, indexed by direction. The present root is $\vec\Xi=-i\vec e_z$ when $Q_z>0$ with the choice $B=Q_z$, which is the negative of that one; the two corner labels and the two idempotent labels are therefore exchanged. In the present indexing
$$
\vec\Upsilon_+=\vec\Upsilon_x,\qquad \vec\Upsilon_-=\vec\Upsilon_y,
$$
and the products are $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, as required.

### The Q-Adapted Peirce Basis

The four elements
$$
\tilde\Pi_+,\qquad \vec\Upsilon_-,\qquad \vec\Upsilon_+,\qquad \tilde\Pi_-
$$
form a $\mathbb{C}$-basis of $\mathbb{B}$. It is the **Q-adapted Peirce basis**. In this basis the multiplication by $\tilde Q$ is diagonal:
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
The diagonal values are
$$
\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The reason is the corner rule: an element of $\mathbb{B}_{st}$ has left sign $s$ and right sign $t$ under multiplication by the root $\vec\Xi$, and $\tilde Q=Q_te_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec\Xi$ acts on it on the left by $Q_t+i\,s\sqrt{Q_x^2+Q_y^2+Q_z^2}=\lambda_s$ and on the right by $Q_t+i\,t\sqrt{Q_x^2+Q_y^2+Q_z^2}=\lambda_t$. The four basis elements, their corners, and the two diagonal readings are collected in the table.

| Basis element | Corner | Left eigenvalue $L_{\tilde Q}$ | Right eigenvalue $R_{\tilde Q}$ |
|---|---|---|---|
| $\tilde\Pi_+$ | $\mathbb{B}_{++}$ | $\lambda_+$ | $\lambda_+$ |
| $\vec\Upsilon_-$ | $\mathbb{B}_{+-}$ | $\lambda_+$ | $\lambda_-$ |
| $\vec\Upsilon_+$ | $\mathbb{B}_{-+}$ | $\lambda_-$ | $\lambda_+$ |
| $\tilde\Pi_-$ | $\mathbb{B}_{--}$ | $\lambda_-$ | $\lambda_-$ |

Thus the left action is diagonal with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$, and the right action is diagonal with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$, in the same basis.

### The Action of the Four Basis Elements

**In the eigenbasis $\mathcal{B}=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the multiplication of the four basis elements is the table, and the left and right actions on the basis are read from it.**

The multiplication is the table.

| $PX$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |
|---|---|---|---|---|
| $\tilde\Pi_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $0$ | $0$ |
| $\vec\Upsilon_-$ | $0$ | $0$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ |
| $\vec\Upsilon_+$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ | $0$ | $0$ |
| $\tilde\Pi_-$ | $0$ | $0$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |

**The left action.** For $\tilde Q_{\mathrm{sp}}\in\mathbb{B}$ write $L_{\tilde Q_{\mathrm{sp}}}(X)=\tilde Q_{\mathrm{sp}}X$. Reading the table row by row,
$$
L_{\tilde\Pi_+}(\tilde\Pi_+)=\tilde\Pi_+,\quad
L_{\tilde\Pi_+}(\vec\Upsilon_-)=\vec\Upsilon_-,\quad
L_{\tilde\Pi_+}(\vec\Upsilon_+)=0,\quad
L_{\tilde\Pi_+}(\tilde\Pi_-)=0,
$$
$$
L_{\vec\Upsilon_-}(\tilde\Pi_+)=0,\quad
L_{\vec\Upsilon_-}(\vec\Upsilon_-)=0,\quad
L_{\vec\Upsilon_-}(\vec\Upsilon_+)=\tilde\Pi_+,\quad
L_{\vec\Upsilon_-}(\tilde\Pi_-)=\vec\Upsilon_-,
$$
$$
L_{\vec\Upsilon_+}(\tilde\Pi_+)=\vec\Upsilon_+,\quad
L_{\vec\Upsilon_+}(\vec\Upsilon_-)=\tilde\Pi_-,\quad
L_{\vec\Upsilon_+}(\vec\Upsilon_+)=0,\quad
L_{\vec\Upsilon_+}(\tilde\Pi_-)=0,
$$
$$
L_{\tilde\Pi_-}(\tilde\Pi_+)=0,\quad
L_{\tilde\Pi_-}(\vec\Upsilon_-)=0,\quad
L_{\tilde\Pi_-}(\vec\Upsilon_+)=\vec\Upsilon_+,\quad
L_{\tilde\Pi_-}(\tilde\Pi_-)=\tilde\Pi_-.
$$
The four lists are the Peirce identities read as left multiplication: $\tilde\Pi_+$ keeps the two vectors of $S_+$ and kills $S_-$, $\tilde\Pi_-$ does the reverse, and the two nilpotents exchange the two spinor spaces in the two directions. In particular
$$
L_{\tilde\Pi_+}+L_{\tilde\Pi_-}=\mathrm{id},
\qquad
L_{\vec\Upsilon_+}L_{\vec\Upsilon_-}=L_{\tilde\Pi_-},
\qquad
L_{\vec\Upsilon_-}L_{\vec\Upsilon_+}=L_{\tilde\Pi_+},
\qquad
L_{\vec\Upsilon_\pm}^2=0,
$$
which are $\tilde\Pi_++\tilde\Pi_-=e_t$, $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_\pm^2=0$.

For $\tilde Q$ itself the left action is diagonal,
$$
L_{\tilde Q}(\tilde\Pi_+)=\lambda_+\tilde\Pi_+,\quad
L_{\tilde Q}(\vec\Upsilon_-)=\lambda_+\vec\Upsilon_-,\quad
L_{\tilde Q}(\vec\Upsilon_+)=\lambda_-\vec\Upsilon_+,\quad
L_{\tilde Q}(\tilde\Pi_-)=\lambda_-\tilde\Pi_-,
$$
with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$ on the four basis vectors in the order $\mathcal{B}$. This is the eigenbasis property of the article: each basis vector is an eigenvector of $L_{\tilde Q}$.

**The right action.** For $R_{\tilde Q_{\mathrm{sp}}}(X)=X\tilde Q_{\mathrm{sp}}$ the same table read column by column gives
$$
R_{\tilde\Pi_+}(\tilde\Pi_+)=\tilde\Pi_+,\quad
R_{\tilde\Pi_+}(\vec\Upsilon_-)=0,\quad
R_{\tilde\Pi_+}(\vec\Upsilon_+)=\vec\Upsilon_+,\quad
R_{\tilde\Pi_+}(\tilde\Pi_-)=0,
$$
$$
R_{\vec\Upsilon_-}(\tilde\Pi_+)=\vec\Upsilon_-,\quad
R_{\vec\Upsilon_-}(\vec\Upsilon_-)=0,\quad
R_{\vec\Upsilon_-}(\vec\Upsilon_+)=\tilde\Pi_-,\quad
R_{\vec\Upsilon_-}(\tilde\Pi_-)=0,
$$
$$
R_{\vec\Upsilon_+}(\tilde\Pi_+)=0,\quad
R_{\vec\Upsilon_+}(\vec\Upsilon_-)=\tilde\Pi_+,\quad
R_{\vec\Upsilon_+}(\vec\Upsilon_+)=0,\quad
R_{\vec\Upsilon_+}(\tilde\Pi_-)=\vec\Upsilon_+,
$$
$$
R_{\tilde\Pi_-}(\tilde\Pi_+)=0,\quad
R_{\tilde\Pi_-}(\vec\Upsilon_-)=\vec\Upsilon_-,\quad
R_{\tilde\Pi_-}(\vec\Upsilon_+)=0,\quad
R_{\tilde\Pi_-}(\tilde\Pi_-)=\tilde\Pi_-,
$$
and for $\tilde Q$
$$
R_{\tilde Q}(\tilde\Pi_+)=\lambda_+\tilde\Pi_+,\quad
R_{\tilde Q}(\vec\Upsilon_-)=\lambda_-\vec\Upsilon_-,\quad
R_{\tilde Q}(\vec\Upsilon_+)=\lambda_+\vec\Upsilon_+,\quad
R_{\tilde Q}(\tilde\Pi_-)=\lambda_-\tilde\Pi_-,
$$
with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$. The left and right actions do not coincide: $R_{\tilde Q}$ and $L_{\tilde Q}$ agree on an element exactly when the element is central, that is, on $\mathbb{C}e_t$.

**A general element.** For $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$ the left action on the basis is
$$
L_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_+)=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+,\qquad
L_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_-)=Q_{\mathrm{sp},11}\vec\Upsilon_-+Q_{\mathrm{sp},21}\tilde\Pi_-,
$$
$$
L_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_+)=Q_{\mathrm{sp},12}\tilde\Pi_++Q_{\mathrm{sp},22}\vec\Upsilon_+,\qquad
L_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_-)=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-,
$$
and the right action is
$$
R_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_+)=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-,\qquad
R_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_-)=Q_{\mathrm{sp},21}\tilde\Pi_++Q_{\mathrm{sp},22}\vec\Upsilon_-,
$$
$$
R_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_+)=Q_{\mathrm{sp},11}\vec\Upsilon_++Q_{\mathrm{sp},12}\tilde\Pi_-,\qquad
R_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_-)=Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-.
$$
The two actions are diagonal exactly on the diagonal subalgebra $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-$, of which $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ is the member with the prescribed eigenvalues. This is the precise sense in which the Peirce coordinates of $\tilde Q$ are the eigenvalues: $Q_{\mathrm{sp},12}=Q_{\mathrm{sp},21}=0$ is the condition that both actions be diagonal, and $\tilde Q$ is the member with $Q_{\mathrm{sp},11}=\lambda_+$ and $Q_{\mathrm{sp},22}=\lambda_-$.

**The four elements of the fixed basis.** The coordinates of $e_t,\vec e_x,\vec e_y,\vec e_z$ in $\mathcal{B}$ are read from the expansions. In the standard case, $Q_x=Q_y=0$ with the standard root $i\vec e_z$, that is $B=-Q_z$ and $\lambda_\pm=Q_t\mp iQ_z$, the nilpotents are
$$
\vec\Upsilon_-=\frac{i\vec e_x-\vec e_y}{2},\qquad
\vec\Upsilon_+=\frac{i\vec e_x+\vec e_y}{2},
$$
and
$$
e_t=\tilde\Pi_++\tilde\Pi_-,\qquad
\vec e_x=-i(\vec\Upsilon_-+\vec\Upsilon_+),\qquad
\vec e_y=\vec\Upsilon_+-\vec\Upsilon_-,\qquad
\vec e_z=-i\tilde\Pi_++i\tilde\Pi_-.
$$
Their coordinates are
$$
e_t=(1,0,0,1),\qquad
\vec e_x=(0,-i,-i,0),\qquad
\vec e_y=(0,-1,1,0),\qquad
\vec e_z=(-i,0,0,i),
$$
and the left action of the four on the basis is read from the table. In particular $\vec e_x,\vec e_y,\vec e_z$ satisfy $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, as the fixed basis does, so the same identities hold for their left actions.

**A general pure element.** Off the axis the coordinates of $\vec e_x,\vec e_y,\vec e_z$ depend on $\vec Q$. For any pure $\vec X$,
$$
\vec X=i\,\frac{\vec X\cdot\vec Q}{B}\,(\tilde\Pi_+-\tilde\Pi_-)+X_{12}\vec\Upsilon_-+X_{21}\vec\Upsilon_+,
\qquad
X_{12}\tilde\Pi_-=\vec\Upsilon_+\vec X\tilde\Pi_-,
\qquad
X_{21}\tilde\Pi_+=\vec\Upsilon_-\vec X\tilde\Pi_+,
$$
so its coordinates in $\mathcal{B}$ are
$$
\vec X=\Bigl(i\,\frac{\vec X\cdot\vec Q}{B},\;X_{12},\;X_{21},\;-i\,\frac{\vec X\cdot\vec Q}{B}\Bigr).
$$
The standard case is $\vec Q=Q_z\vec e_z$, $B=-Q_z$.

### The Eigenbasis of Left Multiplication

**A basis of $\mathbb{B}$ is an eigenbasis of $L_{\tilde Q}$ if each of its vectors $b$ satisfies $\tilde Qb=\mu b$ for some scalar $\mu$. The Q-adapted Peirce basis is one; because each eigenspace is two-dimensional, it is not unique.**

Write
$$
L_{\tilde Q}(\tilde Q_{\mathrm{sp}})=\tilde Q\tilde Q_{\mathrm{sp}},\qquad R_{\tilde Q}(\tilde Q_{\mathrm{sp}})=\tilde Q_{\mathrm{sp}}\tilde Q.
$$
An eigenvector of $L_{\tilde Q}$ with eigenvalue $\mu$ is a nonzero element $\tilde Q_{\mathrm{sp}}$ with $\tilde Q\tilde Q_{\mathrm{sp}}=\mu\tilde Q_{\mathrm{sp}}$. The diagonal property of the Q-adapted basis reads
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-,
$$
so the basis is an eigenbasis; the left action in it is diagonal with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$.

**The two eigenspaces.** The eigenspaces are two-dimensional:
$$
\ker(L_{\tilde Q}-\lambda_+)=\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-,
\qquad
\ker(L_{\tilde Q}-\lambda_-)=\tilde\Pi_-\mathbb{B}=\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-.
$$
These are the two minimal **right** ideals. The basis $(\tilde\Pi_+,\vec\Upsilon_-)$ is a basis of the first, $(\vec\Upsilon_+,\tilde\Pi_-)$ a basis of the second.

**Uniqueness.** An eigenbasis of $L_{\tilde Q}$ is any pair of bases of these two eigenspaces. It is therefore unique only up to an invertible change of basis on each eigenspace. The Q-adapted basis is the choice singled out by the Peirce structure: it orders each eigenspace as $(\tilde\Pi_+,\vec\Upsilon_-)$ and $(\vec\Upsilon_+,\tilde\Pi_-)$, the diagonal idempotent of the Peirce pair first.

**The left ideals are eigenspaces of right multiplication.** The two minimal left ideals
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-
$$
are not eigenspaces of $L_{\tilde Q}$: each contains one eigenvector for $\lambda_+$ and one for $\lambda_-$. They are the eigenspaces of $R_{\tilde Q}$,
$$
\ker(R_{\tilde Q}-\lambda_+)=S_+,\qquad
\ker(R_{\tilde Q}-\lambda_-)=S_-,
$$
and the right action in the same basis is diagonal with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$.
The reason is the side of the multiplication: $L_{\tilde Q}$ multiplies on the left and preserves each right ideal, $R_{\tilde Q}$ multiplies on the right and preserves each left ideal.

The two readings are compared in the table.

| Operator | Eigenvalue | Eigenspace | Dimension over $\mathbb{C}$ | Basis |
|---|---|---|---|---|
| $L_{\tilde Q}$ | $\lambda_+$ | $\tilde\Pi_+\mathbb{B}$ | $2$ | $(\tilde\Pi_+,\vec\Upsilon_-)$ |
| $L_{\tilde Q}$ | $\lambda_-$ | $\tilde\Pi_-\mathbb{B}$ | $2$ | $(\vec\Upsilon_+,\tilde\Pi_-)$ |
| $R_{\tilde Q}$ | $\lambda_+$ | $\mathbb{B}\tilde\Pi_+=S_+$ | $2$ | $(\tilde\Pi_+,\vec\Upsilon_+)$ |
| $R_{\tilde Q}$ | $\lambda_-$ | $\mathbb{B}\tilde\Pi_-=S_-$ | $2$ | $(\vec\Upsilon_-,\tilde\Pi_-)$ |

**Restriction to one left ideal.** On $S_+$ the operator $L_{\tilde Q}$ has the two distinct eigenvalues $\lambda_+,\lambda_-$, with eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$; on $S_-$ it has the same two eigenvalues, with eigenbasis $(\vec\Upsilon_-,\tilde\Pi_-)$. On each, the eigenvalues are distinct, so the eigenbasis is unique up to two independent scales.

**The eigenprojection and the projector.** The element $\tilde\Pi_+$ is the eigenprojection of the eigenvalue decomposition. The operator $L_{\tilde\Pi_+}$ is the spectral projector onto the $\lambda_+$-eigenspace of $L_{\tilde Q}$: it sends $\tilde Q_{\mathrm{sp}}$ to $\tilde\Pi_+\tilde Q_{\mathrm{sp}}$, the first Peirce component, and its image is the two-dimensional right ideal $\tilde\Pi_+\mathbb{B}$. The two objects must not be confused: $L_{\tilde\Pi_+}$ is an operator on the four-dimensional algebra, while the spectral projector of the multiplication map is defined on the algebra itself.

### The Spinor Spaces and their Coordinates

**A spinor space of $\mathbb{B}$ is a minimal nonzero left ideal. The two spinor spaces are $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$, each a complex plane, and the algebra is their direct sum.**

The two spaces are
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
each of complex dimension two, and
$$
\mathbb{B}=S_+\oplus S_-.
$$
A **spinor of first chirality** is an element of $S_+$; a **spinor of second chirality** is an element of $S_-$.

**The module structure.** Left multiplication makes $S_+$ and $S_-$ left $\mathbb{B}$-modules, and each is a complex plane: a spinor has two complex coordinates. The two are isomorphic as left modules: right multiplication by $\vec\Upsilon_-$ maps $S_+$ onto $S_-$, with inverse right multiplication by $\vec\Upsilon_+$, because
$$
\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
\qquad
\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+.
$$
They are nevertheless distinct subspaces of $\mathbb{B}$, and the direct sum is the whole algebra.

In the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$ of $S_+$, a spinor of first chirality is
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+,\qquad Q_{\mathrm{sp},11},Q_{\mathrm{sp},21}\in\mathbb{C},
$$
with the coordinate pair $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$, the first column of the matrix model of §*Matrices and the Column Correspondence*. Under left multiplication by $\tilde Q$,
$$
\tilde Q\xi_+=\lambda_+Q_{\mathrm{sp},11}\tilde\Pi_++\lambda_-Q_{\mathrm{sp},21}\vec\Upsilon_+,
$$
so the coordinate pair is sent to
$$
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\;\lambda_-Q_{\mathrm{sp},21}).
$$
A spinor of second chirality is an element of $S_-$,
$$
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-,\qquad Q_{\mathrm{sp},12},Q_{\mathrm{sp},22}\in\mathbb{C}.
$$
The order of the coefficients follows the eigenbasis $(\vec\Upsilon_-,\tilde\Pi_-)$ of $S_-$, in which the eigenvalues are $(\lambda_+,\lambda_-)$, so the coordinate pair is $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$, the second column of the matrix model of §*Matrices and the Column Correspondence*, and
$$
\tilde Q\xi_-=\lambda_+Q_{\mathrm{sp},12}\vec\Upsilon_-+\lambda_-Q_{\mathrm{sp},22}\tilde\Pi_-
\longmapsto
(\lambda_+Q_{\mathrm{sp},12},\;\lambda_-Q_{\mathrm{sp},22}).
$$
**Left versus right multiplication.** The diagonal action displayed above is the action of $L_{\tilde Q}$ on each spinor space, and it carries both eigenvalues. The space $S_+$ is not an eigenspace of $L_{\tilde Q}$; it is the $\lambda_+$-eigenspace of the right multiplication $R_{\tilde Q}$, and $S_-$ is the $\lambda_-$-eigenspace. The distinction is the side on which $\tilde Q$ multiplies: $R_{\tilde Q}$ is scalar on each $S_\pm$, while $L_{\tilde Q}$ carries the two eigenvalues on each. This is the content of §*The Eigenbasis of Left Multiplication*.

The basis $(\vec\Upsilon_-,\tilde\Pi_-)$ is part of the definition: writing the two vectors in the other order would exchange the two diagonal values.

The two spinor spaces and their coordinates are collected in the table.

| Spinor space | Eigenbasis | Spinor | Coordinates |
|---|---|---|---|
| $S_+=\mathbb{B}\tilde\Pi_+$ | $(\tilde\Pi_+,\vec\Upsilon_+)$ | $Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+$ | $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$, column $1$ |
| $S_-=\mathbb{B}\tilde\Pi_-$ | $(\vec\Upsilon_-,\tilde\Pi_-)$ | $Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-$ | $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$, column $2$ |

**A general element is a pair of spinors.** Every $\tilde Q_{\mathrm{sp}}\in\mathbb{B}$ splits as
$$
\tilde Q_{\mathrm{sp}}=\tilde Q_{\mathrm{sp}}\tilde\Pi_++\tilde Q_{\mathrm{sp}}\tilde\Pi_-,
$$
and the two summands are a spinor of first chirality and a spinor of second chirality. In the Q-adapted coordinates they are
$$
\tilde Q_{\mathrm{sp}}\longmapsto(Q_{\mathrm{sp},11},Q_{\mathrm{sp},12},Q_{\mathrm{sp},21},Q_{\mathrm{sp},22}),
\qquad
\tilde Q_{\mathrm{sp}}\tilde\Pi_+\longmapsto(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21}),
\qquad
\tilde Q_{\mathrm{sp}}\tilde\Pi_-\longmapsto(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22}).
$$
A general element is therefore not a spinor: it has one spinor component of each chirality.

**Complex dimensions.** Each spinor has two complex components, hence four real parameters. The two spinor spaces have complex dimension two and real dimension four each, and their direct sum has the complex dimension four and the real dimension eight of $\mathbb{B}$. The label "first" versus "second" is fixed by the convention $\tilde\Pi_+=(e_t+\vec\Xi)/2$; replacing the square root by its negative, or exchanging the two labels, exchanges the two chiralities.

### Matrices and the Column Correspondence

Fix the assignment
$$
\tilde\Pi_+\mapsto E_{11},\qquad
\vec\Upsilon_-\mapsto E_{12},\qquad
\vec\Upsilon_+\mapsto E_{21},\qquad
\tilde\Pi_-\mapsto E_{22},
$$
where $E_{ij}$ is the matrix unit with $1$ in row $i$ and column $j$. Then every $P\in\mathbb{B}$ has a unique expansion
$$
P=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_-+a_{21}\vec\Upsilon_++a_{22}\tilde\Pi_-,
\qquad a_{ij}\in\mathbb{C},
$$
and is represented by
$$
M_2^Q(P)=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}.
$$
In the notation of the spinor coordinates, $a_{11}=Q_{\mathrm{sp},11}$, $a_{12}=Q_{\mathrm{sp},12}$, $a_{21}=Q_{\mathrm{sp},21}$ and $a_{22}=Q_{\mathrm{sp},22}$.
The element $\tilde Q$ itself has $a_{11}=\lambda_+$, $a_{22}=\lambda_-$ and $a_{12}=a_{21}=0$, so
$$
M_2^Q(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

The two columns are the two spinor spaces:
$$
S_+=\mathbb{B}\tilde\Pi_+\longleftrightarrow\operatorname{span}\{E_{11},E_{21}\}=\text{column }1,
\qquad
S_-=\mathbb{B}\tilde\Pi_-\longleftrightarrow\operatorname{span}\{E_{12},E_{22}\}=\text{column }2.
$$
The first column of $M_2^Q(P)$ is the coordinate vector of $P\tilde\Pi_+$, the second is the coordinate vector of $P\tilde\Pi_-$.

A spinor of first chirality
$$
\xi_+=\alpha\tilde\Pi_++\beta\vec\Upsilon_+
\longleftrightarrow
\begin{pmatrix}\alpha\\\beta\end{pmatrix}
$$
is represented by the matrix
$$
\begin{pmatrix}\alpha&0\\\beta&0\end{pmatrix},
$$
whose first column is $\xi_+$ and whose second column is zero. A spinor of second chirality
$$
\xi_-=\gamma\vec\Upsilon_-+\delta\tilde\Pi_-
\longleftrightarrow
\begin{pmatrix}\gamma\\\delta\end{pmatrix}
$$
is represented by the matrix
$$
\begin{pmatrix}0&\gamma\\0&\delta\end{pmatrix},
$$
whose first column is zero and whose second column is $\xi_-$. The order $(\vec\Upsilon_-,\tilde\Pi_-)$ is the eigenbasis of $S_-$ used above; it is the order in which the diagonal values are $(\lambda_+,\lambda_-)$.

Multiplication by $\tilde Q$ acts on the first column by $M_2^Q(\tilde Q)$,
$$
\tilde Q\xi_+\longleftrightarrow
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\end{pmatrix}
=
\begin{pmatrix}\lambda_+\alpha\\\lambda_-\beta\end{pmatrix},
$$
and on the second column by the same matrix,
$$
\tilde Q\xi_-\longleftrightarrow
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\gamma\\\delta\end{pmatrix}
=
\begin{pmatrix}\lambda_+\gamma\\\lambda_-\delta\end{pmatrix}.
$$
This is the precise statement that the two spinor spaces are the two columns and that multiplication by $\tilde Q$ acts on both by the same diagonal matrix. A general element of $\mathbb{B}$ is not a spinor: its matrix has two nonzero columns, one in each spinor space.

### What Depends on $\tilde Q$ and What Does Not

The Q-adapted data depend on $\tilde Q$ through its root. The comparison is collected in the table.

| Object | Depends on $\tilde Q$? |
|---|---|
| Root $\vec\Xi$ and idempotents $\tilde\Pi_\pm$ | yes |
| Corner lines $\mathbb{B}_{+-},\mathbb{B}_{-+}$ as subspaces | yes |
| Left ideals $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$ | yes |
| Pair $(\vec\Upsilon_+,\vec\Upsilon_-)$ | up to the reciprocal $\mathbb{C}^{\times}$ |
| Diagonal values $(\lambda_+,\lambda_-)$ of $L_{\tilde Q}$ | yes |
| Peirce coordinates of a general element $\tilde Q_{\mathrm{sp}}$ | yes |

The Q-adapted basis is not the standard Peirce basis attached to the fixed root $i\vec e_z$. The two coincide, up to the reciprocal rescaling, exactly when $\vec Q$ is parallel to $\vec e_z$, that is, when $Q_x=Q_y=0$. In that case $\vec\Xi=\pm i\vec e_z$, the pair is the standard pair up to the exchange of its two members, and the nilpotents are $\vec\Upsilon_x,\vec\Upsilon_y$, in one order or the other, up to the reciprocal rescaling.

### The Degenerate Case of the Basis

The construction uses $Q_x^2+Q_y^2+Q_z^2\neq0$. When $Q_x^2+Q_y^2+Q_z^2=0$ and $\vec Q\neq0$:
- the root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$ is undefined;
- no Peirce pair is attached to $\tilde Q$;
- there is no Q-adapted Peirce basis;
- the nilpotents $\vec\Upsilon_\pm$ adapted to $\tilde Q$ do not exist;
- there is no eigenbasis of $L_{\tilde Q}$.

The standard Peirce decomposition of the root $i\vec e_z$ still exists, with its two nilpotents, but it is not attached to $\tilde Q$. In any Peirce basis the Peirce coordinates of $\tilde Q$ have trace $2Q_t$ and determinant $Q_t^2$, because the characteristic polynomial is $(X-Q_t)^2$. They are not diagonalisable, since the minimal polynomial is $(X-Q_t)^2$ when $\vec Q\neq0$. In the Jordan regime $Q_t\neq0$ the Peirce matrix of $\tilde Q$ is a single $2\times2$ Jordan block with eigenvalue $Q_t$, so $L_{\tilde Q}$ is not diagonalisable; in the nilpotent regime $Q_t=0$ it is a nonzero nilpotent.
The nilpotent construction of the standard pair remains available, but it is not the construction of the present section: the present construction takes the nilpotents from the mixed corners of the pair of $\tilde Q$'s own root, and that root does not exist when $Q_x^2+Q_y^2+Q_z^2=0$.

For $\vec Q=0$ the element is scalar, $\tilde Q=Q_te_t$, and $L_{\tilde Q}=Q_t\,\mathrm{id}$ on the whole algebra: every basis is an eigenbasis, the Q-adapted construction is absent, and there is no Jordan or nilpotent regime.

### Summary Block

Given $\tilde Q$ with $Q_x^2+Q_y^2+Q_z^2\neq0$, the following data are attached to $\tilde Q$:
$$
\vec\Xi=-\frac{i\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2},
$$
$$
\vec\Upsilon_+\in\mathbb{B}_{-+},\qquad
\vec\Upsilon_-\in\mathbb{B}_{+-},\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0,
$$
with the symmetric closed form
$$
\vec\Upsilon_\pm=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}},
\qquad
\vec w=\vec e_x+\vec e_y+\vec e_z,\quad \Sigma=Q_x+Q_y+Q_z,
$$
valid off the cone $\Sigma^2=3B^2$; on that cone the axis charts
$$
\vec\Upsilon_\pm=\frac{B\,\vec e_\mu-\dfrac{Q_\mu}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_\mu]}{2\sqrt{Q_\mu^2-B^2}},
\qquad \mu=x,y,z,
$$
cover the pair, at least one of the three being defined, and the defined readings differ by the reciprocal rescaling.
$$
\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-,
$$
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
and every $\tilde Q_{\mathrm{sp}}\in\mathbb{B}$ has the unique expansion
$$
\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-,
\qquad Q_{\mathrm{sp},ij}\in\mathbb{C},
$$
with $\tilde Q$ itself having $Q_{\mathrm{sp},11}=\lambda_+$, $Q_{\mathrm{sp},22}=\lambda_-$ and $Q_{\mathrm{sp},12}=Q_{\mathrm{sp},21}=0$.

**Diagonal property.**
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
The Q-adapted Peirce basis is an eigenbasis of $L_{\tilde Q}$ with eigenvalues
$$
(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The $\lambda_+$-eigenspace of $L_{\tilde Q}$ is the right ideal $\tilde\Pi_+\mathbb{B}$, with basis $(\tilde\Pi_+,\vec\Upsilon_-)$; the $\lambda_-$-eigenspace is $\tilde\Pi_-\mathbb{B}$, with basis $(\vec\Upsilon_+,\tilde\Pi_-)$. The two left ideals $S_+,S_-$ are the eigenspaces of $R_{\tilde Q}$, with eigenvalues $\lambda_+,\lambda_-$ respectively. On each left ideal the restriction of $L_{\tilde Q}$ has the distinct eigenvalues $(\lambda_+,\lambda_-)$, so the eigenbasis of that restriction is unique up to scale.

**Spinors.**
A spinor of first chirality is an element of $S_+$,
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+,
\qquad (Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\in\mathbb{C}^2,
$$
and under left multiplication
$$
\tilde Q\xi_+=\lambda_+Q_{\mathrm{sp},11}\tilde\Pi_++\lambda_-Q_{\mathrm{sp},21}\vec\Upsilon_+,
\qquad\text{that is,}\qquad
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\;\lambda_-Q_{\mathrm{sp},21}).
$$
A spinor of second chirality is an element of $S_-$,
$$
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-,
\qquad (Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\in\mathbb{C}^2,
$$
and under left multiplication
$$
\tilde Q\xi_-=\lambda_+Q_{\mathrm{sp},12}\vec\Upsilon_-+\lambda_-Q_{\mathrm{sp},22}\tilde\Pi_-,
\qquad\text{that is,}\qquad
(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\longmapsto(\lambda_+Q_{\mathrm{sp},12},\;\lambda_-Q_{\mathrm{sp},22}).
$$
The two spinor spaces are the two minimal left ideals; under left multiplication each is a complex plane carrying the two eigenvalues $\lambda_+,\lambda_-$.

**Matrices.**
With
$$
\tilde\Pi_+\mapsto E_{11},\qquad
\vec\Upsilon_-\mapsto E_{12},\qquad
\vec\Upsilon_+\mapsto E_{21},\qquad
\tilde\Pi_-\mapsto E_{22},
$$
a general element has the matrix
$$
M_2^Q(P)=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix},
\qquad
M_2^Q(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
The first column is $S_+$, the second is $S_-$, and multiplication by $\tilde Q$ acts on both by $\operatorname{diag}(\lambda_+,\lambda_-)$.

**Degenerate case.**
$$
Q_x^2+Q_y^2+Q_z^2=0:\quad
\text{no Q-adapted Peirce basis and no Q-adapted nilpotents.}
$$
For $\vec Q\neq0$ there is no eigenbasis of $L_{\tilde Q}$: in any Peirce basis the Peirce matrix of $\tilde Q$ is a single $2\times2$ Jordan block when $Q_t\neq0$ and a nonzero nilpotent when $Q_t=0$, so it is not diagonal. For $\vec Q=0$ the element is scalar, $L_{\tilde Q}=Q_t\,\mathrm{id}$, and every basis is an eigenbasis; the Q-adapted construction is then absent, but an eigenbasis is not.

## The Degenerate Case $Q_x^2+Q_y^2+Q_z^2=0$

**On the cone $B^2=0$ the two eigenvalues have coalesced. Two further questions decide the geometry of a point: whether the scalar part vanishes, and whether the vector part vanishes.**

| regime | condition | spectrum | minimal polynomial | adapted Peirce | the element is |
|---|---|---|---|---|---|
| **scalar** | $\vec Q=0$ | $\{Q_t\}$ | $X-Q_t$ | every idempotent | central, semisimple; a unit iff $Q_t\neq0$ |
| **Jordan** | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\{Q_t\}$ | $(X-Q_t)^2$ | none non-trivial | a unit, defective, one Jordan block |
| **nilpotent** | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\{0\}$ | $X^2$ | none non-trivial | a non-unit, $\tilde Q^2=0$ |

### The Scalar Regime and the Vertex

Let $\tilde Q=Q_te_t$. The element is central, its minimal polynomial is $X-Q_t$, and it is semisimple with the single eigenvalue $Q_t$. Every idempotent commutes with it, so every idempotent is adapted. The spectral decomposition in the sense of the general theory has one term, $\tilde Q=Q_te_t$, and it is unique; a two-term writing with two orthogonal idempotents summing to $e_t$ has the equal coefficient $Q_t$ on both terms and is not determined by $\tilde Q$. This is the only regime in which a two-term writing exists without being a spectral decomposition.

The vertex is the singular locus of $\mathcal S$: it is the line of elements of $\mathcal S$ with the mildest spectral degeneration, where the eigenvalue is repeated but the element still has a spectral decomposition, with one term.

### The Zero Element

**The zero element is degenerate, and it is the one degenerate element that is not a zero divisor.**

At $\tilde Q=0$ one has $B^2=0$ and $N=0$, so $0$ lies in the degenerate case and on the null cone. It is the apex of $\mathcal S$: the only point at which both the scalar and the vector part vanish, and the only point of $\mathcal{N}$ that annihilates nothing non-zero. Its spectrum is $\{0\}$, its minimal polynomial is $X$, every idempotent is adapted to it, and its spectral decomposition is the one-term writing $0=0\cdot e_t$. Both translations $L_0$ and $R_0$ are the zero map, so both annihilators are all of $\mathbb{B}$ and both ranks are $0$. The origin lies in neither stratum of the null cone, the pure stratum excluding it and the non-pure stratum requiring $Q_t\neq0$; it lies in the closure of both.

### The Jordan Regime

Let $\tilde Q=Q_te_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$, and let $Q_t\neq0$. The minimal polynomial is $(X-Q_t)^2$, the spectrum is the single eigenvalue $Q_t$, and the element is a unit, since $N(\tilde Q)=Q_t^2\neq0$. Its centraliser is $\mathbb{C}[\tilde Q]=\{ae_t+b\vec\Upsilon\}$, whose only idempotents are $0$ and $e_t$, so no non-trivial adapted Peirce decomposition exists. The element is a single Jordan block: it is defective, and the two eigenvalues of the non-degenerate side have coalesced at $Q_t$ without the element becoming scalar.

The closest available structure is the Peirce form relative to an idempotent $e$ with $\vec\Upsilon\in e\mathbb{B}f$, where $f=e_t-e$. Such an idempotent exists, and for it

$$
e\tilde Qe=Q_te,\qquad e\tilde Qf=\vec\Upsilon,\qquad f\tilde Qe=0,\qquad f\tilde Qf=Q_tf,
$$

so the element is diagonal on the two Peirce corners and carries its nilpotent part in one off-diagonal corner.

### The Nilpotent Regime

Let $\tilde Q=\vec\Upsilon$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$. The spectrum is $\{0\}$, the minimal polynomial is $X^2$, and the element is not a unit: it lies on the null cone of the reduced norm, and it is a zero divisor. The centraliser and the absence of a non-trivial adapted Peirce decomposition are the same as in the Jordan regime. Relative to an idempotent $e$ with $\vec\Upsilon\in e\mathbb{B}f$, the Peirce form is purely off-diagonal,

$$
e\tilde Qe=0,\qquad e\tilde Qf=\vec\Upsilon,\qquad f\tilde Qe=0,\qquad f\tilde Qf=0.
$$

This regime is the pure stratum of the null cone, with the origin removed.

## Independence of the Two Cones

The two cones are independent: neither contains the other.

### The Two Witnesses

The witnesses are the mixed cells.

- **A zero divisor with distinct eigenvalues.** Let $\tilde Q=e_t+i\vec e_x$. Then $N(\tilde Q)=1+i^2=0$, so $\tilde Q$ lies on the null cone, and $B^2=i^2=-1\neq0$, so it lies off the spectral-degenerate cone. Its eigenvalues are $1\pm i\cdot i$, that is $0$ and $2$; they are distinct, and the spectral decomposition exists, with the idempotents $\tilde Q/2$ and $e_t-\tilde Q/2$. A zero divisor can be spectrally regular.
- **A unit with a repeated eigenvalue.** Let $\tilde Q=e_t+\vec e_x+i\vec e_y$. Then $B^2=1+i^2=0$, so $\tilde Q$ lies on the spectral-degenerate cone, and $N(\tilde Q)=1+1+i^2=1\neq0$, so it lies off the null cone. Its only eigenvalue is $1$, its minimal polynomial is $(X-1)^2$, and it is a unit with no spectral decomposition. This is the Jordan regime, and it is the cell that proves the independence.

### The Intersection

The two cones meet exactly on the pure stratum of the null cone, with the origin adjoined. Here $\mathcal{N}_{\mathrm p}=\{Q_t=0,\ \vec Q^2=0,\ \vec Q\neq0\}$ is the pure stratum of the companion article, so

$$
\mathcal{N}\cap\mathcal S=\{Q_t^2+B^2=0,\ B^2=0\}=\{Q_t=0,\ \vec Q^2=0\}=\mathcal{N}_{\mathrm p}\cup\{0\}.
$$

As a scheme, the intersection is

$$
(Q_t^2+B^2,\ B^2)=(Q_t^2,\ B^2),
$$

an ideal generated by two squares: its reduction is the pure stratum with the origin adjoined, and the scheme is non-reduced along both defining hypersurfaces. The two defining equations have equal gradients along the smooth part of the intersection: the gradients are $2(Q_t,Q_x,Q_y,Q_z)$ and $(0,2Q_x,2Q_y,2Q_z)$, which agree where $Q_t=0$.

### The Non-Multiplicativity

The null cone is a semigroup, because $N$ is multiplicative. The spectral-degenerate cone is not. The witness

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2e_t-2i\vec e_z
$$

is a product of two points of $\mathcal S$, since $1+i^2=0$ in both factors, and the product has $B^2=(-2i)^2=-4\neq0$, so it lies off $\mathcal S$; its reduced norm is $4-4=0$, so it lies on $\mathcal{N}$. The cone $\mathcal S$ is a discriminant locus attached to the eigenvalue map, not a multiplicative subset.

### The Five Zones

The joint refinement of the two cones partitions the algebra into the **distinct** zone ($B^2\neq0$, $N\neq0$), the **zero-divisor** zone ($B^2\neq0$, $N=0$), the **scalar** zone ($\vec Q=0$), the **Jordan** zone ($B^2=0$, $\vec Q\neq0$, $Q_t\neq0$) and the **nilpotent** zone ($B^2=0$, $\vec Q\neq0$, $Q_t=0$):

| zone | condition | norm | spectral data |
|---|---|---|---|
| **distinct** | $B^2\neq0$, $N\neq0$ | unit | two distinct eigenvalues |
| **zero divisor** | $B^2\neq0$, $N=0$ | zero divisor | two distinct eigenvalues, $0$ one of them |
| **scalar** | $\vec Q=0$ | $N=Q_t^2$ | one eigenvalue, semisimple |
| **Jordan** | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | unit | one eigenvalue, defective |
| **nilpotent** | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | zero divisor | one eigenvalue $0$, defective |

The origin belongs to the scalar zone; the nilpotent zone excludes it. The norm problem puts the zero-divisor zone, the nilpotent zone and the origin on one side, and the distinct zone, the non-zero scalar line and the Jordan zone on the other. The spectral problem separates all five zones, because its data include the minimal polynomial: the eigenvalues give $Q_t$ and $B^2$, and the minimal polynomial separates the scalar line from the Jordan regime. The norm problem is therefore the coarser projection: it cannot separate the scalar line from the Jordan zone, because both have $N=Q_t^2$. The independence is between the loci, not between the information: the product of the eigenvalues is $N$, so the spectrum determines the norm, but the norm does not determine $B^2$.

## The Two Failures Compared

The independence of the loci has a concrete form in the two decompositions the corpus uses.

### The Eigenbasis

The spectral decomposition exists on the distinct zone and on the zero-divisor zone, where $B^2\neq0$, and it fails on the Jordan and nilpotent zones. On the null cone it exists on the non-pure stratum, where $N=0$, $B^2=-Q_t^2\neq0$ and the eigenvalues are $2Q_t$ and $0$; it fails on the nilpotent stratum, which is the pure stratum. On the Jordan regime it fails although the element is a unit: the modulus–unit polar decomposition exists and the eigenbasis does not.

### The Polar Decomposition

The modulus–unit polar decomposition $\tilde Q=\Rho\tilde U$ requires $\Rho^2=N(\tilde Q)$ with $\Rho\neq0$, so it exists exactly off the null cone. It therefore fails on the zero-divisor zone, where the eigenbasis exists, and it exists on the Jordan zone, where the eigenbasis fails. On the scalar zone it exists exactly when $Q_t\neq0$, that is everywhere except the origin.

### The Operators

The left and the right multiplication by $\tilde Q$ have complex rank $4$ when $N\neq0$, rank $2$ when $\tilde Q$ is a non-zero point of the null cone, and rank $0$ at the origin. The discriminant does not change these ranks: the distinct zone and the Jordan zone both have rank $4$, and the zero-divisor zone and the nilpotent zone both have rank $2$. The rank follows the norm, not the discriminant.

**The sandwich and the derivation.** The two cones are also the two loci of the two-sided operators. For the sandwich $\Theta_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}$, suppose first that $N(\tilde Q)=0$ with $\tilde Q\neq0$. Then $\tilde Q^{\natural}\neq0$, since $\tilde Q^{\natural}=Q_te_t-\vec Q=0$ forces $Q_t=0$ and $\vec Q=0$, hence $\tilde Q=0$; and

$$
\Theta_{\tilde Q}(\tilde Q^{\natural})=\tilde Q\,\tilde Q^{\natural}\,\tilde Q^{*}=N(\tilde Q)\,\tilde Q^{*}=0 .
$$

So $\Theta_{\tilde Q}$ is singular. Conversely, if $N(\tilde Q)\neq0$ then $\tilde Q$ is a unit and $\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}$. Hence $\Theta_{\tilde Q}$ is singular exactly on the null cone.

For the inner derivation $\mathrm{ad}_{\tilde Q}(X)=\tilde QX-X\tilde Q$, the scalar part is central, so $\mathrm{ad}_{\tilde Q}=\mathrm{ad}_{\vec Q}$, and

$$
\mathrm{ad}_{\vec Q}^{2}(X)=\vec Q^{2}X-2\vec QX\vec Q+X\vec Q^{2}=-2\vec QX\vec Q
$$

because $\vec Q^{2}=-B^{2}e_t$. When $B^{2}=0$ the binomial expansion gives $\mathrm{ad}_{\vec Q}^{3}=0$, because every term of $\mathrm{ad}_{\vec Q}^{3}(X)=\vec Q^{3}X-3\vec Q^{2}X\vec Q+3\vec QX\vec Q^{2}-X\vec Q^{3}$ carries a factor $\vec Q^{2}$. The derivation is nilpotent, of index at most three. Conversely, if $B^{2}\neq0$ the eigenvalues of the derivation are $0,0,\pm2iB$, and the two nonzero ones forbid nilpotence. Hence $\mathrm{ad}_{\tilde Q}$ is nilpotent exactly on the spectral-degenerate cone.

The two criteria are cone-level and do not separate the strata: the derivation vanishes on the whole scalar line, and the sandwich is singular at the origin as well.

| zone | spectral decomposition | polar decomposition | rank of left multiplication | $\Theta_{\tilde Q}$ singular | $\mathrm{ad}_{\tilde Q}$ nilpotent |
|---|---|---|---|---|---|
| distinct | yes | yes | $4$ | no | no |
| zero divisor | yes | no | $2$ | yes | no |
| scalar, $Q_t\neq0$ | one term | yes | $4$ | no | yes |
| origin | one term | no | $0$ | yes | yes |
| Jordan | no | yes | $4$ | no | yes |
| nilpotent | no | no | $2$ | yes | yes |

## Summary

The biquaternion algebra carries two quadratic conditions. The reduced norm $N=Q_t^2+B^2$ is multiplicative and decides invertibility; its zero locus is the null cone $\mathcal{N}$. The discriminant of the characteristic polynomial is $-4B^2$; its zero locus is the spectral-degenerate cone $\mathcal S$, and it decides whether the two eigenvalues $Q_t\pm iB$ can be separated.

The spectral problem is stated without a module or an acting operator. An eigenvalue is a scalar for which the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, equivalently for which $\tilde Q-\lambda e_t$ is a non-unit, equivalently for which $N(\tilde Q-\lambda e_t)=0$. The eigenspace is the left annihilator, a right ideal of complex dimension $2$ for a non-scalar element. A spectral idempotent is an idempotent commuting with the element, and on the regular side the spectral decomposition is the pair of Lagrange idempotents. Cayley–Hamilton gives the inverse off the null cone, and the unordered spectrum determines the similarity class except at $B=0$, where the scalar and the non-semisimple nilpotent share it.

The cone $\mathcal S$ is $\mathbb{C}e_t$ times the isotropic cone of the vector subspace, of complex dimension $3$ and real dimension $6$. It is smooth off the scalar vertex and singular along it. It is not a subspace, and it is not the set of defective elements: the vertex is semisimple. It is not a null cone, because $B^2$ is not a norm on the algebra; the only multiplicative norm is $N$.

On the non-scalar side, the adapted Peirce decomposition exists exactly when $B^2\neq0$, and then it is unique. The degenerate side is stratified into the scalar regime, where every idempotent is adapted and the spectral decomposition has one term; the Jordan regime, where the element is a unit, defective and without a non-trivial adapted idempotent; and the nilpotent regime, where the element is a zero divisor and a nilpotent of index two. The vertex is the scalar line.

The two cones are independent: neither contains the other. A zero divisor can have distinct eigenvalues, and a unit can have a repeated one. The cones meet exactly on the pure stratum of the null cone, with the origin adjoined, and their defining equations have equal gradients along it. The spectral cone is not multiplicative, while the null cone is. The joint refinement is the five zones. The spectral problem is the finer one: its eigenvalues determine the norm, since $N=\lambda_+\lambda_-$, but the norm does not determine $B^2$. The independence is between the loci, not between the information: the norm cannot separate the scalar from the Jordan regime, while the spectral problem separates all five zones, through the minimal polynomial. The polar decomposition follows the norm and the eigenbasis follows the discriminant, so the Jordan regime, a unit with no eigenbasis, is the sharpest witness of the independence. The same two cones are the two operator loci: the sandwich $\Theta_{\tilde Q}$ is singular exactly on the null cone, and the inner derivation $\mathrm{ad}_{\tilde Q}$ is nilpotent exactly on the spectral-degenerate cone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, not a norm on $\mathbb{B}$ |
| $N(\tilde Q)=Q_t^2+B^2$ | the reduced norm, the only multiplicative one |
| $p_{\tilde Q}(X)=X^2-2Q_tX+N(\tilde Q)$ | the characteristic polynomial |
| $\operatorname{disc}p_{\tilde Q}=-4B^2$ | the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mathcal{N}=\{N=0\}$ | the null cone of the reduced norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\operatorname{Ann}_{\ell}(a)=\{v:av=0\}$ | the left annihilator, a right ideal |
| $e_\pm=(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$ | the spectral idempotents |
| $\vec\Upsilon$ | a non-zero vector with $\vec\Upsilon^2=0$ |
| $\mathcal{N}_{\mathrm p}=\{Q_t=0,\ \vec Q^2=0,\ \vec Q\neq0\}$ | the pure stratum of the null cone, the nilpotents |
| $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ | the sandwich; singular exactly on the null cone |
| $\mathrm{ad}_{\tilde Q}(X)=\tilde QX-X\tilde Q$ | the inner derivation; nilpotent exactly on $\mathcal S$ |

## Further Reading

- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the reduced norm, the null cone, its pure and non-pure strata, the unit group and the zero divisors.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition, the eigenprojections, the degenerate regimes, the Hermitian case and the spectral theorem.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the weak Peirce decomposition, the Peirce corners and the minimal left ideals.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the existence and uniqueness of the spectral decomposition in the general theory.
- [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), for the interpolating idempotents.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block behind the Jordan regime.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the semisimple and nilpotent parts.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the polar decomposition that the null cone obstructs.
