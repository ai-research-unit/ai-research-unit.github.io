# __Spinors and Dirac Spinors in the Biquaternion Algebra__

## Introduction

The word spinor names three different objects in this algebra, and the three are the three levels of one chain: a carrier, the closure of that
carrier, and the sum of two copies of the closure. The conventions of this section give each level a name, and the article fixes them.

A **spinor** is an element of the plane $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+(\vec u_{\mathrm r})$, of real dimension $2$. A **spinor
space** is the first closure $S_+(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_+(\vec u_{\mathrm r})$, of real dimension $4$. A **Dirac spinor** is an
element of a bispinor space, the second closure $\mathbb{B}=S_+\oplus S_-$, of real dimension $8$. The three levels are nested,
$\Sigma\subset S_+\subset\mathbb{B}$, and each is the closure of the one before.

Each level answers the two questions of the section. The weight question is answered by the generator $\tfrac12 i\vec u_{\mathrm r}$ and gives the
string $(\pm\tfrac12)$, of length $2=2s+1$. The sector question is answered by the two predicates $N\neq0$ and $B^{2}\neq0$, and it answers
differently at each level: a nonzero spinor lies in $\Sigma_{01}$ and the zero spinor in $\Sigma_{00}$, so no spinor lies in a regular sector; a
spinor-space element obeys the same rule; and a Dirac spinor lies in any of the four. The reason for the difference is one theorem, *a spinor is null*,
and its analogue for the ideal: on the plane and on the ideal the norm vanishes everywhere, so the first index of the sector is fixed at zero, and only
at the bispinor level does the norm become the pairing of two parts and with it a free index.

The article also records what the two definitions do not need. They use no array, no second triple of operators, no conjugate module, and no separate
parameter for the coupling of the two parts: the coupling is a right multiplication, the exchanges between the parts form a single complex line, and
one complex number times a fixed exchange is the whole datum the pair costs.

The predicates, the sectors and the strata are those of *Relations between the N Norm and Spectral Regularity and Degeneracy*, and they are defined
again below so that the article stands alone. The carriers are *The Carriers, the Representation, the Spin and the Closure*. The levels themselves
are *Introduction to the Spin-Zero Centre Subspace*, *Introduction to the Spin-Half Bispinors* and *Introduction to the Spin-One Anti-Hermitian
Subspace*.

Nothing below is a statement of physics. The elements are written $X,Y$. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the
basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $e_t$ the identity, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, with complex coefficients. The
element $i$ commutes with the units and satisfies $i^{2}=-e_t$. A general element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex and
$\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. A unit real axis is $\vec u_{\mathrm r}$, with $\vec u_2,\vec u_3$ an oriented orthonormal pair
completing it. The star is the Hermitian conjugation, $u$ is a unitary element, one with $uu^{*}=e_t$, and $\operatorname{Ad}_u$ is the inner automorphism
$X\mapsto uXu^{-1}$, which on $G$ reads $X\mapsto uXu^{*}$.

## The Two Predicates and the Four Sectors

**Definition (the norm and the square of the vector part).** For $\tilde Q=Q_te_t+\vec Q$,

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

with the polar form $B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$, symmetric and complex-bilinear. The two differ by the scalar square:

$$
N(\tilde Q)-B^{2}(\tilde Q)=Q_t^{2}.
$$

**Lemma (the discriminant identity).** If $\lambda_1,\lambda_2$ are the eigenvalues of $\tilde Q$, then

$$
(\lambda_1-\lambda_2)^{2}=\operatorname{tr}(\tilde Q)^{2}-4N(\tilde Q)=-4B^{2}(\tilde Q).
$$

*Proof.* The trace is $2Q_t$ and the determinant is $N(\tilde Q)$; for a two-by-two element $\operatorname{tr}^{2}-4\det=(\lambda_1-\lambda_2)^{2}$,
and substituting $N=Q_t^{2}+B^{2}$ gives $4Q_t^{2}-4Q_t^{2}-4B^{2}$.

**Corollary (the spectral predicate is the coincidence of the eigenvalues).** $B^{2}(\tilde Q)=0$ exactly when the two eigenvalues coincide.

**Definition (the two predicates and the four sectors).** An element is **norm-regular** when $N(\tilde Q)\neq0$ and **spectrally regular** when
$B^{2}(\tilde Q)\neq0$. The zero loci are the **null cone** $\mathcal N=\{N=0\}$ and the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$. For
$i,j\in\{0,1\}$ the sector $\Sigma_{ij}$ is the set of elements with $N\neq0$ if $i=1$, and with $B^{2}\neq0$ if $j=1$.

| sector | conditions | name |
|---|---|---|
| $\Sigma_{11}$ | $N\neq0$, $B^{2}\neq0$ | doubly regular |
| $\Sigma_{10}$ | $N\neq0$, $B^{2}=0$ | norm-regular, spectrally degenerate |
| $\Sigma_{01}$ | $N=0$, $B^{2}\neq0$ | norm-degenerate, spectrally regular |
| $\Sigma_{00}$ | $N=0$, $B^{2}=0$ | doubly degenerate |

## The Three Levels of a Spinor

**Definition (the idempotent of the axis).** For a unit real axis $\vec u_{\mathrm r}$,

$$
\tilde\Pi_\pm(\vec u_{\mathrm r})=\tfrac12\bigl(e_t\pm i\vec u_{\mathrm r}\bigr),
$$

so that $\tilde\Pi_\pm^{2}=\tilde\Pi_\pm$, $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$.

**Definition (the three levels).**

$$
\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+(\vec u_{\mathrm r}),\qquad
S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_\pm(\vec u_{\mathrm r}),\qquad
\mathbb{B}=S_+(\vec u_{\mathrm r})\oplus S_-(\vec u_{\mathrm r}).
$$

The plane is the carrier of spin $\tfrac12$. Its first closure is the ideal $S_+(\vec u_{\mathrm r})$, one of the two minimal left ideals of the
algebra at the axis; its second closure is the sum of the two ideals, a bispinor space, which as a set is the whole algebra.

**Theorem (the three levels are nested).** $\Sigma(\vec u_{\mathrm r})\subset S_+(\vec u_{\mathrm r})\subset\mathbb{B}$, and the dimensions double
at each step.

*Proof.* The plane is the complex line generated by the idempotent, and the idempotent lies in the ideal it generates. The ideal is one of the two
summands of the direct sum. The dimensions are computed in the table below.

| level | space | $\dim_{\mathbb{R}}$ | $\dim_{\mathbb{C}}$ | generator |
|---|---|---|---|---|
| spinor | $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+$ | $2$ | $1$ | the idempotent $\tilde\Pi_+$ |
| spinor space | $S_+(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_+$ | $4$ | $2$ | $\tilde\Pi_+$ and $\vec u_2\tilde\Pi_+$ |
| Dirac spinor | $\mathbb{B}=S_+\oplus S_-$ | $8$ | $4$ | both ideals together |

**Remark (why the plane is the carrier and the ideal is its closure).** The plane is invariant under the rotations about its own axis only, and the
ideal is invariant under every left multiplication, hence under the whole group. The closure is what makes the object a module of the algebra; the
plane is what makes the object irreducible, and the two properties are not the same property.

## The Weight

**Definition (the generator).** The spin generators are $\tilde S_k=\tfrac12 i\vec e_k$, and the generator of the axis is
$\vec u_{\mathrm r}\cdot\vec S=\tfrac12 i\vec u_{\mathrm r}$.

**Theorem (the axis identity).** $\vec u_{\mathrm r}\,\tilde\Pi_\pm(\vec u_{\mathrm r})=\mp i\,\tilde\Pi_\pm(\vec u_{\mathrm r})$.

*Proof.* The product is $\tfrac12(\vec u_{\mathrm r}+i\vec u_{\mathrm r}^{2})=\tfrac12(\vec u_{\mathrm r}-ie_t)$, which equals
$-i\cdot\tfrac12(e_t+i\vec u_{\mathrm r})$; the other sign is the same computation at $-\vec u_{\mathrm r}$.

**Theorem (the weights).** On the plane the generator acts as the number $+\tfrac12$:

$$
\bigl(\tfrac12 i\vec u_{\mathrm r}\bigr)\tilde\Pi_+(\vec u_{\mathrm r})=\tfrac12\tilde\Pi_+(\vec u_{\mathrm r}).
$$

On the ideal the generator has the two eigenvalues $+\tfrac12$ and $-\tfrac12$, each once. The $-\tfrac12$ vector of $S_+(\vec u_{\mathrm r})$ is the
companion nilpotent

$$
\nu(\vec u_{\mathrm r})=\tilde\Pi_-(\vec u_{\mathrm r})\,\vec u_2\,\tilde\Pi_+(\vec u_{\mathrm r}),
$$

which is square-zero. At $\vec u_{\mathrm r}=\vec e_z$ it is $\nu=\tfrac12(i\vec e_x+\vec e_y)$.

*Proof.* The first display follows from the axis identity, which gives $\tfrac12 i\vec u_{\mathrm r}\tilde\Pi_+=\tfrac12\tilde\Pi_+$, and the second
sign from the same identity at $\tilde\Pi_-$. For $\nu$: it is one-dimensional because it lies in the corner $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$, and
every element of that corner satisfies $\nu=\tilde\Pi_-\nu$, whence $\tfrac12 i\vec u_{\mathrm r}\nu=-\tfrac12\nu$; and
$\nu^{2}=\tilde\Pi_-\vec u_2\tilde\Pi_+\tilde\Pi_-\vec u_2\tilde\Pi_+=0$ because $\tilde\Pi_+\tilde\Pi_-=0$.

**Corollary (the weight string and the dimension).** The string of the ideal is $(+\tfrac12,-\tfrac12)$, of length $2$, and

$$
2s+1=2=\dim_{\mathbb{C}}S_+(\vec u_{\mathrm r})=\dim_{\mathbb{R}}\Sigma(\vec u_{\mathrm r}).
$$

**Remark (the half angle).** The rotation through $\theta$ about $\vec u_{\mathrm r}$ is the left multiplication by

$$
\exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r},
$$

which acts on the plane as the scalar $e^{-i\theta/2}$, by the axis identity. At $\theta=2\pi$ the multiplier is $-e_t$ and the spinor returns with
the opposite sign; at $\theta=4\pi$ it returns unchanged. No vector does this: the adjoint action of the same multiplier turns a vector through the
full angle $\theta$ and returns it to itself at $\theta=2\pi$.

## The Sector of a Spinor

**Theorem (a spinor is null).** For every complex $\lambda$,

$$
N\bigl(\lambda\tilde\Pi_+(\vec u_{\mathrm r})\bigr)=0,\qquad B^{2}\bigl(\lambda\tilde\Pi_+(\vec u_{\mathrm r})\bigr)=-\tfrac14\lambda^{2}.
$$

With $Q_t=\lambda/2$ the scalar coordinate of the spinor, the second display reads $B^{2}=-Q_t^{2}$.

*Proof.* The norm is multiplicative and $N(\tilde\Pi_+)=\tfrac14(1-\lvert\vec u_{\mathrm r}\rvert^{2})=0$. For the second display, the eigenvalues
sum to $2Q_t=\lambda$ and their product is $N=0$, so they are $0$ and $\lambda$; the discriminant identity then reads $\lambda^{2}=-4B^{2}$, whence
$B^{2}=-\lambda^{2}/4$.

**Theorem (a spinor is neither invertible nor of norm one).** Every nonzero spinor is a zero divisor, so no spinor is norm-regular and no spinor lies in
$\Sigma_{11}$ or in $\Sigma_{10}$.

*Proof.* An invertible element has $N\neq0$, and a unit element has $N=1$; the norm of a spinor vanishes.

### The Sector $\Sigma_{01}$

**Theorem.** The punctured plane lies in the sector:

$$
\Sigma(\vec u_{\mathrm r})\cap\Sigma_{01}=\{\lambda\tilde\Pi_+(\vec u_{\mathrm r}):\lambda\neq0\}.
$$

*Proof.* On the plane $N=0$, so the first index is zero, and $B^{2}=-\lambda^{2}/4$ is nonzero exactly for $\lambda\neq0$.

**Corollary (the spectrum of a spinor).** For $\lambda\neq0$ the spectrum is $\{0,\lambda\}$, with distinct eigenvalues, and the eigenvector of the
eigenvalue $\lambda$ is the spinor itself, since $\tilde\Pi_+^{2}=\tilde\Pi_+$.

### The Sector $\Sigma_{00}$

**Theorem.** $\Sigma(\vec u_{\mathrm r})\cap\Sigma_{00}=\{0\}$, and the origin is the only point of the plane at which the second predicate fails.

*Proof.* The origin is the point $\lambda=0$, where both predicates fail.

### The Two Intersections in One Table

| sector | condition on $\lambda$ | intersection |
|---|---|---|
| $\Sigma_{11}$ | impossible, $N=0$ | $\varnothing$ |
| $\Sigma_{10}$ | impossible, $N=0$ | $\varnothing$ |
| $\Sigma_{01}$ | $\lambda\neq0$ | $\mathbb{C}^{\times}\tilde\Pi_+(\vec u_{\mathrm r})$ |
| $\Sigma_{00}$ | $\lambda=0$ | $\{0\}$ |

**Remark (the spinor against the vector).** A carrier of spin $1$ is the vector part, on which $N=B^{2}=\lvert\vec v\rvert^{2}$ and every nonzero
element is invertible; a carrier of spin $\tfrac12$ is the plane, on which $N=0$ and no nonzero element is invertible. The difference is not an
accident of the axis: $N(\tilde\Pi_+)=\tfrac14(1-\lvert\vec u_{\mathrm r}\rvert^{2})$ cancels exactly because the axis is a real unit vector, so
the vanishing is the geometry of the axis and not a coincidence of a frame.

## The Spinor Space and Its Two Planes

**The coordinates.** In the basis $(\tilde\Pi_+(\vec u_{\mathrm r}),\vec u_2\tilde\Pi_+(\vec u_{\mathrm r}))$ an element of the spinor space is

$$
Y=\alpha\tilde\Pi_+(\vec u_{\mathrm r})+\beta\,\vec u_2\tilde\Pi_+(\vec u_{\mathrm r}),
$$

with $\alpha,\beta$ complex, and its scalar coordinate is $Q_t(Y)=\alpha/2$.

**Theorem (the ideal is null, and one number decides its sector).** For every $Y$,

$$
N(Y)=0,\qquad B^{2}(Y)=-Q_t(Y)^{2}.
$$

So the ideal meets $\Sigma_{01}$ where $\alpha\neq0$ and $\Sigma_{00}$ where $\alpha=0$, and it meets the two regular sectors nowhere.

*Proof.* The ideal is $\mathbb{B}\tilde\Pi_+$ and the norm is multiplicative, so the norm vanishes. The spectrum of $Y$ is $\{0,2Q_t(Y)\}$ by the
quadratic relation $Y^{2}-2Q_t(Y)Y+N(Y)e_t=0$ together with $N(Y)=0$, so the difference of the two eigenvalues is $-2Q_t(Y)$ and $B^{2}=-Q_t^{2}$.

### The Sector $\Sigma_{01}$

**Theorem.** The intersection is the ideal minus a real plane:

$$
S_+(\vec u_{\mathrm r})\cap\Sigma_{01}=\{Y:Q_t(Y)\neq0\}.
$$

*Proof.* On the ideal the first index is zero and the second is decided by $Q_t$, which is nonzero exactly when $\alpha\neq0$.

### The Sector $\Sigma_{00}$

**Theorem (the doubly degenerate part of the ideal is a real plane).**

$$
S_+(\vec u_{\mathrm r})\cap\Sigma_{00}=\mathbb{C}\bigl(\vec u_2-i\vec u_3\bigr)=\mathbb{C}\,\vec u_2\tilde\Pi_+(\vec u_{\mathrm r}),
$$

of real dimension $2$.

*Proof.* The condition is $\alpha=0$, that is $Q_t=0$. And $\vec u_2\tilde\Pi_+(\vec u_{\mathrm r})=\tfrac12(\vec u_2-i\vec u_3)$, whose scalar
coordinate vanishes.

**Theorem (the doubly degenerate part is the square-zero part).** For an element $Y$ of the ideal,

$$
Y^{2}=0\iff Y\in\Sigma_{00}.
$$

*Proof.* On the ideal the quadratic relation reduces to $Y^{2}=2Q_t(Y)Y$, so a vanishing square forces $Q_t(Y)Y=0$ and hence $Q_t(Y)=0$ unless
$Y=0$; conversely $Q_t(Y)=0$ gives $Y^{2}=0$.

**Remark (the two planes of the ideal).** The carrier plane is generated by an idempotent and lies in $\Sigma_{01}$ away from the origin; the
degenerate plane is generated by a square-zero element and lies entirely in $\Sigma_{00}$. The two meet only at the origin, and the second is the
part of the ideal that the first does not see.

## The Dirac Spinor Is a Pair

**Definition (Dirac spinor).** A **Dirac spinor** is an element

$$
X=X_++X_-,\qquad X_\pm\in S_\pm(\vec u_{\mathrm r}),
$$

of a bispinor space at the declared axis $\vec u_{\mathrm r}$. The two summands are the **parts** of the Dirac spinor, and each part is an element of
a spinor space.

**Theorem (the parts exhaust the algebra).** Every element of $\mathbb{B}$ is a Dirac spinor at every axis, and only the zero element has both parts
zero. The four complex coordinates of an element are two pairs, one pair per part.

*Proof.* $\tilde\Pi_+$ and $\tilde\Pi_-$ are orthogonal idempotents summing to $e_t$, so $\mathbb{B}=S_+\oplus S_-$ and the decomposition is unique.
The count $4=2+2$ is the sum $\dim_{\mathbb{C}}S_++\dim_{\mathbb{C}}S_-$.

**Theorem (the norm of a Dirac spinor is the pairing of the parts).** $N(X)=2B(X_+,X_-)$.

*Proof.* The norm is quadratic with polar form $B$, so $N(X_++X_-)=N(X_+)+N(X_-)+2B(X_+,X_-)$, and the two pure terms vanish because each spinor
space is null.

**Corollary (the weight string of the pair).** On each of the two parts the generator $\tfrac12 i\vec u_{\mathrm r}$ has the weights $+\tfrac12$ and
$-\tfrac12$ once, so on the Dirac spinor each weight occurs twice.

## The Sector of a Dirac Spinor

**Theorem (the two indices are independent).** The first index of the sector of a Dirac spinor is the vanishing of the pairing of its two parts, and
the second is the vanishing of $B^{2}$. Neither is a function of the other, and all four combinations occur.

*Proof.* The first index is $N=2B(X_+,X_-)$ by the theorem above and the second is $B^{2}$ by definition; the witnesses below supply one element of
each sector.

### The Sector $\Sigma_{11}$

**Theorem.** The intersection is

$$
\mathbb{B}\cap\Sigma_{11}=\{X:2B(X_+,X_-)\neq0,\ B^{2}(X)\neq0\},
$$

which is open and dense in the algebra, of real dimension $8$.

*Proof.* Each of the two conditions fails on a complex hypersurface, so the intersection of their complements is open and dense in the algebra, whose
real dimension is $8$.

**Witness.** $X=e_t+2\vec e_x$ has $N=5$ and $B^{2}=4$.

### The Sector $\Sigma_{10}$

**Theorem.** The intersection is

$$
\mathbb{B}\cap\Sigma_{10}=\{X:2B(X_+,X_-)\neq0,\ B^{2}(X)=0\},
$$

of real dimension $6$: the invertible elements whose two eigenvalues coincide.

*Proof.* The conditions are a non-vanishing pairing and a vanishing $B^{2}$, and the vanishing of $B^{2}$ is the coincidence of the two eigenvalues by
the criterion of the spectral predicate.

**Witness.** $X=e_t=\tilde\Pi_++\tilde\Pi_-$ has $N=1$ and $B^{2}=0$, and its two parts pair to $\tfrac12$.

### The Sector $\Sigma_{01}$

**Theorem.** The intersection is the null cone without its apex:

$$
\mathbb{B}\cap\Sigma_{01}=\{X:2B(X_+,X_-)=0,\ B^{2}(X)\neq0\},
$$

of real dimension $6$. It contains the punctured plane of each ideal and the two ideals minus their degenerate planes.

*Proof.* The pairing vanishes and $B^{2}$ does not.

**Witness.** $X=\tilde\Pi_+(\vec u_{\mathrm r})$ has $N=0$ and $B^{2}=-\tfrac14$.

### The Sector $\Sigma_{00}$

**Theorem.** The intersection is the nilpotent cone:

$$
\mathbb{B}\cap\Sigma_{00}=\{X:X^{2}=0\},
$$

of real dimension $4$.

*Proof.* The two predicates fail exactly when $Q_t=0$ and $\vec Q^{2}=0$, and these two conditions are $X^{2}=0$.

**Witness.** $X=\vec u_2-i\vec u_3$ has a vanishing square, and it generates the degenerate plane of the ideal.

**The Four Intersections in One Table.**

| sector | pairing | $B^{2}$ | witness | $\dim_{\mathbb{R}}$ |
|---|---|---|---|---|
| $\Sigma_{11}$ | $\neq0$ | $\neq0$ | $e_t+2\vec e_x$ | $8$ |
| $\Sigma_{10}$ | $\neq0$ | $=0$ | $e_t$ | $6$ |
| $\Sigma_{01}$ | $=0$ | $\neq0$ | $\tilde\Pi_+(\vec u_{\mathrm r})$ | $6$ |
| $\Sigma_{00}$ | $=0$ | $=0$ | $\vec u_2-i\vec u_3$ | $4$ |

**Corollary (a Dirac spinor is invertible exactly when its parts pair).** By $N(X)=2B(X_+,X_-)$, the element $X$ is invertible if and only if
$B(X_+,X_-)\neq0$, and in that case both parts are nonzero.

## The Two Parts Are Exchanged on the Right

**Theorem (no left multiplication crosses).** For every $a\in\mathbb{B}$,

$$
a\,S_+(\vec u_{\mathrm r})\subseteq S_+(\vec u_{\mathrm r}),\qquad a\,S_-(\vec u_{\mathrm r})\subseteq S_-(\vec u_{\mathrm r}).
$$

*Proof.* Each summand is a left ideal.

**Theorem (a perpendicular unit vector exchanges the parts).** Let $\vec v$ be a real unit vector perpendicular to $\vec u_{\mathrm r}$, read as an
element of the algebra. Then the right multiplication $X\mapsto X\vec v$ is left-linear, carries $S_+(\vec u_{\mathrm r})$ bijectively onto
$S_-(\vec u_{\mathrm r})$ and $S_-(\vec u_{\mathrm r})$ bijectively onto $S_+(\vec u_{\mathrm r})$, and satisfies $(X\vec v)\vec v=-X$ on the
whole algebra.

*Proof.* Left-linearity: $(aX)\vec v=a(X\vec v)$. The product $\tilde\Pi_+(\vec u_{\mathrm r})\vec v$ equals
$\tfrac12(\vec v+i\vec u_{\mathrm r}\vec v)$, and $\vec u_{\mathrm r}\vec v=-\vec v\vec u_{\mathrm r}$ at a perpendicular pair, so the product is a
nonzero element of the ideal $S_-(\vec u_{\mathrm r})$; hence $S_+(\vec u_{\mathrm r})\vec v\subseteq S_-(\vec u_{\mathrm r})$. The map is injective
because $\vec v$ is invertible, with $\vec v^{-1}=-\vec v$, and the two ideals have the same real dimension $4$, so the image is the whole of
$S_-(\vec u_{\mathrm r})$. The same computation at $-\vec u_{\mathrm r}$ gives the other direction. Finally $\vec v^{2}=-e_t$, so
$(X\vec v)\vec v=-X$, which also proves the two maps inverse to each other.

**Corollary (the pair is one spinor space taken twice).** As a left module $\mathbb{B}\cong S\oplus S$ with $S$ the simple module, and the exchange is
a left-linear isomorphism of the two summands. So the Dirac spinor is not the carrier of a four-dimensional irreducible module: the left action on it
is two-dimensional and repeats.

**Theorem (the exchanges form a complex line).** The left-linear maps $S_+(\vec u_{\mathrm r})\to S_-(\vec u_{\mathrm r})$ form a complex vector
space of dimension $1$.

*Proof.* A right multiplication $X\mapsto XM$ carries $S_+(\vec u_{\mathrm r})$ into $S_-(\vec u_{\mathrm r})$ exactly when
$\tilde\Pi_+M\tilde\Pi_+=0$: the image is $\mathbb{B}\tilde\Pi_+M$, which lies in $\mathbb{B}\tilde\Pi_-$ exactly when
$\tilde\Pi_+M=\tilde\Pi_+M\tilde\Pi_-$. On the four corners of the algebra at the axis this condition kills the corner
$\tilde\Pi_+\mathbb{B}\tilde\Pi_+$ and nothing else, so the multipliers that give such a map form a complex vector space of dimension $3$. Two of
them give the same map exactly when their difference is annihilated on the left by $\tilde\Pi_+$, that is exactly when the difference lies in
$\tilde\Pi_-\mathbb{B}$, of complex dimension $2$. The maps form a space of dimension $3-2=1$, and each of them is the map $X\mapsto XE$ attached to
a single element $E$ of the corner $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$.

**Corollary (the multiplier is one corner element, and the perpendicular axes differ by a phase).** The maps are exactly the maps $X\mapsto XE$ with
$E$ in the corner $\tilde\Pi_+(\vec u_{\mathrm r})\mathbb{B}\tilde\Pi_-(\vec u_{\mathrm r})$, a complex line, and the correspondence is bijective. A
perpendicular real unit vector gives $E=\tilde\Pi_+(\vec u_{\mathrm r})\vec v$, and for $\vec v=\cos\varphi\,\vec u_2+\sin\varphi\,\vec u_3$
that corner element runs once round the circle of elements of modulus one. So the perpendicular real axes carry the phase of the exchange, and not a
direction of it.

**Remark (the exchange preserves the norm and not the spectral predicate).** Since $N(X\vec v)=N(X)N(\vec v)=N(X)$ at a real unit vector, the exchange
preserves invertibility and carries the null cone to itself. It does not preserve $B^{2}$, and it is therefore not an automorphism of the sector
structure. At $\vec u_{\mathrm r}=\vec e_z$ and $\vec v=\vec e_x$ the element $e_t$ has $B^{2}=0$ and its image $\vec e_x$ has $B^{2}=1$, so
$\Sigma_{10}$ is carried to $\Sigma_{11}$; and $\tilde\Pi_+(\vec e_z)$ has $B^{2}=-\tfrac14$ and goes to an element with $B^{2}=0$, so
$\Sigma_{01}$ is carried to $\Sigma_{00}$. The sector of a Dirac spinor is not an invariant of the exchange; only the first index is.

## The Axis Is a Parameter of the Family

**Theorem (the conjugation carries one axis to another).** Let $u$ be a unitary element with $\operatorname{Ad}_u(\vec u_{\mathrm r})=\vec u_{\mathrm r}'$. Then
$\operatorname{Ad}_u$ carries $\tilde\Pi_\pm(\vec u_{\mathrm r})$ to $\tilde\Pi_\pm(\vec u_{\mathrm r}')$, the plane to the plane, each ideal to the
corresponding ideal, and each of the four sectors to itself.

*Proof.* The conjugation by a unitary element is an automorphism of the algebra; it carries $\vec u_{\mathrm r}$ to $\vec u_{\mathrm r}'$ and hence
the idempotent to the idempotent, a complex line to a complex line and a left ideal to a left ideal. Both predicates are invariant: the norm is
multiplicative and $N(u)N(u^{*})=N(uu^{*})=N(e_t)=1$ at a unitary element, so $N(uXu^{*})=N(X)$, and the trace is invariant under conjugation, so $Q_t$ and hence
$B^{2}=N-Q_t^{2}$ are unchanged.

**Corollary (what the family is indexed by).** The planes and the ideals are indexed by the sphere of unit axes; the unordered pair
$\{S_+(\vec u_{\mathrm r}),S_-(\vec u_{\mathrm r})\}$, which is a bispinor space, is indexed by the pair $\pm\vec u_{\mathrm r}$, that is by the real
projective plane.

**Remark (the axis is the only datum the definitions cost).** The weight, the dimension, the pairing, the sector of each level and the exchange are
the same at every axis. What the axis fixes is which two summands are called the parts; the substitution $\vec u_{\mathrm r}\mapsto-\vec u_{\mathrm r}$
swaps them, since $\tilde\Pi_+(\vec u_{\mathrm r})=\tilde\Pi_-(-\vec u_{\mathrm r})$. So the pair is unordered and the ordering is a name.

## What the Definitions Do Not Use

**No array.** The idempotent, the weights, the plane, the ideals and the pairing are elements and identities of the algebra. No matrix is needed to
state them, and none is used above. An array can be written afterwards, as the coordinates of an element in a chosen frame, and then the two parts of a
Dirac spinor are two columns; the columns are a consequence of the decomposition and not its definition.

**No second triple.** The two parts are not distinguished by a second family of operators with opposite signs. The generator
$\tfrac12 i\vec u_{\mathrm r}$ has the same weights on both parts, and what separates them is the idempotent that generates them, that is a datum
of the axis.

**No separate coupling parameter.** The two parts are coupled by a right multiplication, and the multiplications that exchange them form a single
complex line, spanned by the corner element the axis produces. A coupling is one complex number times that exchange; no new scalar is introduced, and
none is needed, because the line is already an object of the algebra.

**No conjugate module.** The second part is not a conjugate copy of the first. It is a copy of the first, isomorphic as a left module and exchanged
with it by a left-linear map. Nothing in the construction uses a module on which the scalars act by their conjugates.

**No Peirce basis and no volume element.** The four corners of the algebra at the axis exist and are useful, and the article does not need them: the
whole content is carried by the two idempotents, the generator and the two predicates.

## Summary

The three levels are the plane $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+(\vec u_{\mathrm r})$ of real dimension $2$, the spinor space
$S_+(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_+(\vec u_{\mathrm r})$ of real dimension $4$, and the bispinor space $\mathbb{B}=S_+\oplus S_-$ of real
dimension $8$, nested in that order. The generator $\tfrac12 i\vec u_{\mathrm r}$ acts on the plane as $+\tfrac12$ and on the ideal with the two
weights $\pm\tfrac12$, so $2s+1=2$; the rotation through $\theta$ is the left multiplication by
$\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\vec u_{\mathrm r}$, which returns the spinor with the opposite sign at a full turn.

The sector question has one answer on the plane and on the ideal and another on the pair. The plane and the ideal are null, so a spinor lies in
$\Sigma_{01}$ away from the origin and in $\Sigma_{00}$ at it, and the doubly degenerate part of the ideal is the real plane
$\mathbb{C}(\vec u_2-i\vec u_3)$ of square-zero elements. A Dirac spinor lies in any of the four sectors, because its norm is the pairing of its two
parts, $N(X)=2B(X_+,X_-)$, so the first index asks whether the parts pair and the second whether $B^{2}$ survives; the witnesses are
$e_t+2\vec e_x$, $e_t$, $\tilde\Pi_+$ and $\vec u_2-i\vec u_3$.

The two parts are exchanged on the right, by a real unit vector perpendicular to the axis, which is left-linear and squares to $-1$; no left
multiplication crosses. The pair is therefore one spinor space taken twice, the exchanges form a complex line spanned by the corner element of the
axis, and the axis is the only datum the definitions cost, with the pair unordered and indexed by the real projective plane. The exchange preserves
the norm and not $B^{2}$, so it moves elements between sectors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, real dimension $8$, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t^{2}=e_t$, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $\tilde Q=Q_te_t+\vec Q$ | a general element, with $Q_\mu$ complex |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the norm, the first predicate |
| $B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part, the second predicate |
| $B(X,Y)$ | the polar form of the norm, $\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$ |
| $N-B^{2}=Q_t^{2}$ | the difference of the two conditions |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |
| $\vec u_{\mathrm r}$, $\vec u_2,\vec u_3$ | a unit real axis and an oriented orthonormal pair completing it |
| $\tilde\Pi_\pm(\vec u_{\mathrm r})=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ | the idempotents of the axis |
| $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+(\vec u_{\mathrm r})$ | the plane, a spinor, real dimension $2$; the letter takes the axis as argument, while a sector $\Sigma_{ij}$ takes subscripts |
| $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_\pm(\vec u_{\mathrm r})$ | the spinor spaces, real dimension $4$ |
| $\mathbb{B}=S_+\oplus S_-$ | a bispinor space, real dimension $8$ |
| $\tilde S_k=\tfrac12 i\vec e_k$ | the spin generators, $\vec u_{\mathrm r}\cdot\vec S=\tfrac12 i\vec u_{\mathrm r}$ |
| $\nu(\vec u_{\mathrm r})=\tilde\Pi_-\vec u_2\tilde\Pi_+$ | the companion nilpotent, the $-\tfrac12$ vector of the ideal |
| $\vec u_2-i\vec u_3$ | the square-zero element spanning the doubly degenerate plane of the ideal |
| $X=X_++X_-$ | a Dirac spinor and its two parts |
| $Q_t=\tfrac12\lambda$ | the scalar coordinate of a spinor |

## Further Reading

- [Introduction to the Spin-Half Bispinors](the-spin-half-bispinor-spaces.html), for the plane, the two spinor spaces and the family of bispinor
spaces.
- [The Spin-Half Bispinors and N Norm Regularity](the-spin-half-bispinor-spaces-and-n-norm-regularity.html), for the nullity of the plane and of
the ideals, and the pairing of the two halves.
- [The Spin-Half Bispinors and Spectral Regularity](the-spin-half-bispinor-spaces-and-spectral-regularity.html), for the spectrum $\{0,\lambda\}$
of the plane and the degenerate plane inside an ideal.
- [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity](the-spin-half-bispinor-spaces-and-the-sectors-of-n-and-spectral-regularity.html),
for the four intersections of the bispinor space with the sectors, with their dimensions.
- [The Carriers, the Representation, the Spin and the Closure](the-carriers-the-representation-the-spin-and-the-closure.html), for the definition of
spin as a maximal weight, the two identities from which the spectra are read, and the double cover.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html),
for the two predicates, the four sectors and the strata.
- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the carrier of spin $0$ and the degenerate case of the
same construction.
- [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the carrier of spin $1$ and the closure in
the anti-Hermitian space.
- [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity.html),
for the sector count at the smallest carrier.
- [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity.html),
for the sector count at the largest of the three carriers.
