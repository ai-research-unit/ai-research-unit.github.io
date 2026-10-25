# __The Quaternionic Norm-Degenerate, Spectrally Regular Sector__

## Introduction

This is cell $01$ of the four-sector arrangement of the two quadratic conditions

$$
N(\tilde Q)=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

the sector on which the quaternionic norm vanishes and the vector square does not. It is the difference of the null cone and the spectral-degenerate cone,

$$
\Sigma_{01}=\mathcal{N}\setminus\mathcal S,
$$

and it is one of the two **mixed** sectors: the two cells on which the norm problem and the spectral problem give different answers. The vocabulary, the two cones and the naming convention are those of *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra* and *Spectral Regularity and Degeneracy in the Biquaternion Algebra*. The opposite corner $\Sigma_{00}$ is treated in *The Quaternionic Norm-Degenerate, Spectrally Degenerate Sector*.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and $\tilde Q=Q_te_t+\vec Q$; the conjugation is ${}^{\natural}$; the quaternionic norm is $N(\tilde Q)=\tilde Q^{\natural}\tilde Q$, central; and the product is the plain product unless stated otherwise. The null cone is $\mathcal{N}=\{N=0\}$; the spectral-degenerate cone is $\mathcal S=\{B^2=0\}$; **spectrally regular** means $B^2\neq0$.

## Definition and Characterisation

**Definition.** The sector $\Sigma_{01}$ is

$$
\Sigma_{01}=\{N=0,\ B^2\neq0\}=\{Q_t^2+B^2=0,\ B^2\neq0\}.
$$

**Theorem (five descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\tilde Q\in\Sigma_{01}$;

(ii) $N(\tilde Q)=0$ and $Q_t\neq0$;

(iii) $\tilde Q^2=2Q_t\tilde Q$ with $Q_t\neq0$;

(iv) $\tilde Q=c\,\tilde\Pi$ with $c\in\mathbb{C}^\times$ and $\tilde\Pi$ a non-trivial idempotent;

(v) the spectrum of $\tilde Q$ is $\{\lambda,0\}$ with $\lambda\neq0$.

*Proof.* (i) $\iff$ (ii): on $N=Q_t^2+B^2=0$, one has $B^2=-Q_t^2$, so $B^2\neq0$ exactly when $Q_t\neq0$.

(ii) $\iff$ (iii): the identity $\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q$, with $B^2=-Q_t^2$, gives $\tilde Q^2=2Q_t^2e_t+2Q_t\vec Q=2Q_t\tilde Q$. Conversely, $\tilde Q^2=2Q_t\tilde Q$ with $Q_t\neq0$ compares central parts and gives $Q_t^2-B^2=2Q_t^2$, hence $B^2=-Q_t^2\neq0$ and $N=0$.

(ii) $\iff$ (iv): put $\tilde\Pi=\tilde Q/(2Q_t)$; then $\tilde\Pi^2=\tilde\Pi$ is (iii), and $\tilde\Pi\notin\{0,e_t\}$ because $\tilde Q\neq0$ and $B^2\neq0$. Conversely, a non-trivial idempotent has scalar part $\tfrac12$: writing $\tilde\Pi=p e_t+\vec\Pi$ with $\vec\Pi\neq0$, the equation $\tilde\Pi^2=\tilde\Pi$ gives $2p\vec\Pi=\vec\Pi$, hence $p=\tfrac12$; then $B^2(\tilde\Pi)=-\tfrac14$ and $N(\tilde\Pi)=0$. So $c\tilde\Pi$ has $N=0$ and $B^2=-c^2/4\neq0$.

(ii) $\iff$ (v): the characteristic polynomial is $X^2-2Q_tX+N$. When $N=0$ it is $X(X-2Q_t)$, so the spectrum is $\{0,2Q_t\}$, and exactly one eigenvalue is zero exactly when $Q_t\neq0$.

**Corollary (a positive characterisation).** The sector is the set of non-zero complex multiples of non-trivial idempotents:

$$
\Sigma_{01}=\{c\,\tilde\Pi\ :\ c\in\mathbb{C}^\times,\ \tilde\Pi^2=\tilde\Pi,\ \tilde\Pi\neq0,e_t\}.
$$

The scalar is fixed by the element: $c=2Q_t$ and $\tilde\Pi=\tilde Q/(2Q_t)$. So the description is a bijection, not merely a parametrisation.

**Corollary (spectral character).** The sector is characterised by the spectrum alone: it is the set of elements whose spectrum is $\{\lambda,0\}$ with $\lambda\neq0$.

## Geometry

**Theorem (an open subset of the null cone).** $\Sigma_{01}=\mathcal{N}\setminus\Sigma_{00}$ is a Zariski-open subset of the null cone, of complex dimension $3$ and real dimension $6$. It is smooth, connected, and not closed in $\mathbb{B}$; its closure is $\mathcal{N}$, and the boundary it loses is exactly $\Sigma_{00}$.

*Proof.* In $\mathcal{N}$ one has $B^2=-Q_t^2$, so $B^2=0$ is equivalent to $Q_t=0$, which is $\Sigma_{00}$. Hence $\Sigma_{01}=\mathcal{N}\setminus\{Q_t=0\}$ is Zariski-open in $\mathcal{N}$. The null cone is cut out by $N=0$, whose gradient $2\tilde Q$ does not vanish off the origin; the origin lies in $\Sigma_{00}$, so every point of $\Sigma_{01}$ is smooth. Its dimension is that of $\mathcal{N}$, namely $4-1=3$ over $\mathbb{C}$, hence $6$ over $\mathbb{R}$. The closure of a non-empty open subset of the irreducible variety $\mathcal{N}$ is $\mathcal{N}$ itself.

**Parametrisation.** The map

$$
\mathbb{C}^\times\times\{\text{non-trivial idempotents}\}\longrightarrow\Sigma_{01},\qquad (c,\tilde\Pi)\mapsto c\,\tilde\Pi
$$

is a bijection. The non-trivial idempotents are $\tilde\Pi=(e_t+\tilde\Xi)/2$ with $\tilde\Xi^2=e_t$ and $\tilde\Xi\neq\pm e_t$; writing $\tilde\Xi=\xi\vec e$ for $\xi\in\mathbb{C}^3$, the root equation is

$$
\xi_x^2+\xi_y^2+\xi_z^2=1,
$$

a smooth affine quadric of complex dimension $2$. Deleting the two roots $\pm e_t$ and multiplying by $\mathbb{C}^\times$ gives complex dimension $1+2=3$ and real dimension $2+4=6$. The roots $\tilde\Xi=i\vec u$, $\vec u\in S^2$, are the Hermitian ones and form a two-sphere in the quadric.

**Remark (a cone with the apex removed).** The sector is stable under every non-zero complex scalar and under no zero scalar: $0\cdot\tilde Q=0$ lies in $\Sigma_{00}$. It is a cone with its apex deleted, and the apex belongs to its closure.

**Remark (homogeneity).** The sector is a single orbit of $\mathbb{C}^\times\times\mathbb{B}^\times$ acting by scaling and inner automorphisms, because the unit group acts transitively on the non-trivial idempotents. Nothing in the sector is distinguished from anything else except by the value of $c$.

## The Elements

Let $\tilde Q=c\tilde\Pi\in\Sigma_{01}$, with $c=2Q_t\neq0$ and $\tilde\Pi$ a non-trivial idempotent.

**Spectrum and minimal polynomial.** The spectrum is $\{c,0\}$, with distinct roots, and the minimal polynomial is $X(X-c)$. The element is semisimple: its two spectral idempotents are

$$
e_+=\tilde\Pi=\frac{\tilde Q}{2Q_t},\qquad e_-=e_t-\tilde\Pi,
$$

with $\tilde Qe_+=c\,e_+$, $\tilde Qe_-=0$, $e_+^2=e_+$, $e_-^2=e_-$, $e_+e_-=0$, $e_++e_-=e_t$.

**Adapted Peirce decomposition.** Relative to the pair $(e_+,e_-)$ the Peirce form is diagonal:

$$
e_+\tilde Qe_+=c\,e_+,\qquad
e_+\tilde Qe_-=0,\qquad
e_-\tilde Qe_+=0,\qquad
e_-\tilde Qe_-=0.
$$

The decomposition is a two-term writing with one coefficient zero, not a one-term writing: $e_-$ is present and non-trivial, although its coefficient vanishes. It is unique, because the spectral idempotents of an element with distinct eigenvalues are unique. This is the exact contrast with $\Sigma_{00}\setminus\{0\}$, where no Peirce decomposition relative to $\tilde Q$ exists.

**The spectral decomposition.** The eigenvalues are $\lambda_+=c=2Q_t$ and $\lambda_-=0$, distinct, and
$$
\tilde Q=c\,e_++0\cdot e_-,\qquad e_+=\tilde\Pi,\quad e_-=\tilde\Pi'.
$$
The writing has two terms with one coefficient vanishing: it is not the one-term writing $c\,e_+$, because $e_-$ is present and non-trivial. It is unique, and an eigenbasis exists, since $B^2\neq0$; the construction is in *The Quaternionic Norm-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners*.

**Powers.** For $n\geq1$, $\tilde Q^n=c^n e_+$, and the polynomial calculus reads $f(\tilde Q)=f(c)e_++f(0)e_-=f(c)\tilde\Pi+f(0)\tilde\Pi'$. There is no inverse, since $N=0$; the image of the eigenvalue map on the sector is the set of pairs $(c,0)$ with $c\neq0$, so it is not surjective onto $\mathbb{C}^\times\times\mathbb{C}^\times$.

**Centraliser.** The centraliser is the plane

$$
\mathbb{C}[\tilde Q]=\mathbb{C}[\tilde\Pi]=\{a\tilde\Pi+b\tilde\Pi'\ :\ a,b\in\mathbb{C}\}\cong\mathbb{C}\oplus\mathbb{C},
$$

with $\tilde\Pi'=e_t-\tilde\Pi$. Its idempotents are exactly $0$, $e_t$, $\tilde\Pi$ and $\tilde\Pi'$: an element $a e_t+b\tilde\Pi$ is idempotent when $a^2=a$ and $2ab+b^2=b$, which gives $(a,b)=(0,0)$, $(1,0)$, $(0,1)$ or $(1,-1)$.

**Annihilators.** Let $A(\tilde Q)=\ker L_{\tilde Q}$ and $B(\tilde Q)=\ker R_{\tilde Q}$ be the left and right annihilators. Since $\tilde Q\tilde X=c\,\tilde\Pi\tilde X$, the left annihilator is

$$
A(\tilde Q)=\{\tilde X:\tilde\Pi\tilde X=0\}=\mathbb{B}_{-+}\oplus\mathbb{B}_{--},
$$

and the right annihilator is

$$
B(\tilde Q)=\{\tilde X:\tilde X\tilde\Pi=0\}=\mathbb{B}_{--}\oplus\mathbb{B}_{+-},
$$

where the corners are taken relative to $(\tilde\Pi,\tilde\Pi')$. Each is a complex plane, and they meet in

$$
A(\tilde Q)\cap B(\tilde Q)=\mathbb{B}_{--}=\mathbb{C}\tilde\Pi',
$$

the line of the **kernel projector** $e_-=\tilde\Pi'$, which is the eigenspace of the eigenvalue $0$ and satisfies $e_-\tilde Q=\tilde Qe_-=0$. The line of $\tilde Q$ lies in neither annihilator, since $\tilde Q^2=c\tilde Q\neq0$. In this sector the annihilators are built from the Peirce lines of the spectral decomposition; in $\Sigma_{00}$ they are the two planes through $\tilde Q$ itself.

**Conjugation.** From $\tilde X\tilde Q=0\iff\tilde Q^{\natural}\tilde X^{\natural}=0$,

$$
A(\tilde Q)^{\natural}=B(\tilde Q^{\natural}).
$$

When $\tilde Q^{\natural}$ is proportional to $\tilde Q$ — in particular when $\tilde\Pi$ is Hermitian, so that $\tilde Q^{\natural}=\bar c\,\tilde\Pi$ — the conjugation exchanges the two annihilators. For a non-Hermitian idempotent it exchanges the annihilator of $\tilde Q$ with that of a different element of the sector.

**One-sided multiplication.** Left multiplication is $L_{\tilde Q}=c\,L_{\tilde\Pi}$, and $L_{\tilde\Pi}$ is a projection, $L_{\tilde\Pi}^2=L_{\tilde\Pi}$. Hence

$$
L_{\tilde Q}^2=c\,L_{\tilde Q}=2Q_tL_{\tilde Q},\qquad R_{\tilde Q}^2=2Q_tR_{\tilde Q}.
$$

Both operators have complex rank $2$, with images the minimal left and right ideals $\mathbb{B}\tilde\Pi$ and $\tilde\Pi\mathbb{B}$, and kernels the two annihilator planes. They are **not** square-zero, in contrast with $\Sigma_{00}$: the element is a zero divisor, but its multiplication is a projection up to scale, not a nilpotent operator.

## Peirce Data

**The Peirce decomposition relative to $\tilde Q$ exists and is unique. It has two non-trivial idempotents and one vanishing coefficient: the Peirce matrix of $\tilde Q$ is $\operatorname{diag}(c,0)$.**

Let $\tilde Q=c\tilde\Pi$ with $c=2Q_t\neq0$ and $\tilde\Pi$ a non-trivial idempotent, and put $\tilde\Pi'=e_t-\tilde\Pi$. The spectral idempotents are $e_+=\tilde\Pi$ and $e_-=\tilde\Pi'$. The four corners $\mathbb{B}_{st}=e_s\mathbb{B}e_t$ are one-dimensional lines, and the Peirce form is

$$
e_+\tilde Qe_+=c\,e_+,\qquad
e_+\tilde Qe_-=0,\qquad
e_-\tilde Qe_+=0,\qquad
e_-\tilde Qe_-=0.
$$

In the Peirce basis $(\tilde\Pi,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi')$, with the nilpotents normalised by $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi'$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi$, the Peirce matrix is

$$
\begin{pmatrix}c&0\\0&0\end{pmatrix}.
$$

The zero coefficient is the only trace of the norm degeneracy in the Peirce data. The idempotent $e_-$ is present and non-trivial, and the decomposition is genuinely two-term: the vanishing coefficient is a value, not a missing idempotent. Both mixed corners are non-zero, so both nilpotents exist.

**The eigenbasis.** Since $B^2\neq0$, the root $\vec\Xi=-i\vec Q/B$ and the pair $(\tilde\Pi_+,\tilde\Pi_-)$ are defined, and the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ exists. The pair is the pair $\{\tilde\Pi,\tilde\Pi'\}$, with the labels fixed by the chosen square root; the construction is that of *The Quaternionic Norm-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners*. In that basis the diagonal values are $(c,0)$ in one order or the other. The zero eigenvalue is carried by one diagonal entry and by one only.

## Multiplication

**Products stay on the null cone.** The norm is multiplicative, so for $\tilde P,\tilde Q\in\Sigma_{01}$,

$$
N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)=0,
$$

and the product lies in $\mathcal{N}=\Sigma_{00}\sqcup\Sigma_{01}$.

**Theorem (all three outcomes occur).**

$$
\Sigma_{01}\cdot\Sigma_{01}\subseteq\mathcal{N},
$$

and the product of two elements of the sector can lie in $\Sigma_{01}$, can be $0$, and can be a non-zero element of $\Sigma_{00}$.

*Witnesses.* Take the standard pair of a root, $\tilde\Pi_\pm=(e_t\pm\tilde\Xi)/2$, and the Peirce element of the mixed corner,

$$
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2},\qquad
\tilde\Pi_-=\frac{e_t-i\vec e_z}{2},\qquad
E_{12}=\frac{\vec e_x+i\vec e_y}{2},
$$

which satisfy $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $E_{12}^2=0$, and $\tilde\Pi_+E_{12}=E_{12}=E_{12}\tilde\Pi_-$, $\tilde\Pi_-E_{12}=0=E_{12}\tilde\Pi_+$. Then:

- $\tilde\Pi_+^2=\tilde\Pi_+\in\Sigma_{01}$: the product stays in the sector.
- $\tilde\Pi_+\tilde\Pi_-=0$: the product is the origin.
- with $\tilde\Pi'=\tilde\Pi_-+bE_{12}$ for $b\neq0$, the element $\tilde\Pi'$ is a non-trivial idempotent, hence lies in $\Sigma_{01}$, and

$$
\tilde\Pi_+\tilde\Pi'=bE_{12}=\frac{b}{2}(\vec e_x+i\vec e_y)
$$

is a non-zero nilpotent of index two, hence lies in $\Sigma_{00}\setminus\{0\}$.

So the sector is not closed under multiplication, and its product set meets both pieces of the null cone and contains the origin.

**Remark (a frequent confusion).** The pair $\vec e_x\pm i\vec e_y$ does **not** witness a product inside $\Sigma_{01}$: both factors are pure isotropic vectors, with $B^2=0$, so both lie in $\Sigma_{00}$, and their product

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2e_t-2i\vec e_z
$$

lies in $\Sigma_{01}$. That is the $\Sigma_{00}\times\Sigma_{00}\to\Sigma_{01}$ witness, not the reverse. The correct $\Sigma_{01}\times\Sigma_{01}\to\Sigma_{00}$ witness is the Peirce product above.

**Products of squares.** For $\tilde Q\in\Sigma_{01}$,

$$
\tilde Q^2=2Q_t\tilde Q,\qquad B^2(\tilde Q^2)=4Q_t^2B^2(\tilde Q)\neq0,
$$

so the square of an element of the sector stays in the sector.

## Relation to the Two Cones

**The sector is the complement of one cone inside the other.** As point sets,

$$
\Sigma_{01}=\mathcal{N}\setminus\mathcal S,\qquad
\mathcal{N}=\Sigma_{00}\sqcup\Sigma_{01}.
$$

The closure of $\Sigma_{01}$ is $\mathcal{N}$; the boundary it loses is exactly its intersection with $\mathcal S$, which is $\Sigma_{00}$.

**No tangency.** The two cones are **transverse along the sector**, not tangent. Their gradients are

$$
\nabla N=2(Q_t,\vec Q),\qquad \nabla B^2=2(0,\vec Q),
$$

and they are proportional only if $Q_t=0$. On $\Sigma_{01}$ one has $Q_t\neq0$, so the gradients are independent and the intersection $\mathcal{N}\cap\mathcal S$ is nowhere dense in $\mathcal{N}$ there. The tangency of the two cones is a phenomenon of the boundary $\Sigma_{00}$, where both gradients become $2(0,\vec Q)$.

**Independence witness.** Every element of the sector is a **non-unit** with **distinct eigenvalues**: $N=0$, so it is a zero divisor of the plain product, while $B^2=-Q_t^2\neq0$, so its two eigenvalues $0$ and $2Q_t$ are separated. The standard example is

$$
\tilde Q=e_t+i\vec e_x,\qquad N=0,\qquad B^2=-1,\qquad \tilde Q^2=2\tilde Q,
$$

with spectral idempotents $\tilde\Pi_\pm=(e_t\pm i\vec e_x)/2$, spectrum $\{2,0\}$ and Peirce form $2\tilde\Pi_+ + 0\cdot\tilde\Pi_-$ relative to $\tilde Q$. This is the element that prevents the null cone from being identified with the spectral-degenerate cone.

## Comparison with the Other Three Sectors

| sector | conditions | elements | spectrum | Peirce decomposition | product |
|---|---|---|---|---|---|
| **doubly regular** $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | units with distinct eigenvalues | $\{\lambda_+,\lambda_-\}$, distinct and non-zero | exists, unique | stays in $\mathbb{B}^\times$; can land in $\Sigma_{10}$ |
| **norm-degenerate, spectrally regular** $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | $c\tilde\Pi$, $c\neq0$, $\tilde\Pi$ a non-trivial idempotent | $\{c,0\}$ | exists, unique | stays on $\mathcal{N}$; all three outcomes |
| **norm-regular, spectrally degenerate** $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | units with a repeated eigenvalue, plus the scalar line minus $0$ | $\{Q_t\}$ | fails off the scalar line, one term on it | stays in $\mathbb{B}^\times$; can land in $\Sigma_{11}$ |
| **doubly degenerate** $\Sigma_{00}$ | $N=0$, $B^2=0$ | non-zero nilpotents of index two, plus the origin | $\{0\}$ | fails off the origin | $0$ or $\Sigma_{01}$ |

**The two mixed sectors.** $\Sigma_{01}$ and $\Sigma_{10}$ are the independence witnesses: $\Sigma_{01}$ is a zero divisor with a full eigenbasis, $\Sigma_{10}$ is a unit with none. Neither cone contains the other, and these are the cells that show it.

**Position among the four sectors.** Sector $01$ is the **idempotent stratum** of the null cone: the elements $c\tilde\Pi$ with $c\neq0$ and $\tilde\Pi$ a non-trivial idempotent. It is the only sector on which the norm vanishes while the spectrum stays separated, so it is one of the two independence witnesses. The finer split inside $\Sigma_{10}$ and $\Sigma_{00}$ is by the minimal polynomial, not by the two predicates; it is recorded in *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*, §*The Chain of Invariants*.

## Consequences

**Eigenbasis.** It exists and is unique: $e_+=\tilde Q/(2Q_t)$, $e_-=e_t-e_+$. The Peirce decomposition relative to $\tilde Q$ is the only one.

**Polar decomposition.** The modulus is $\Rho=\sqrt{N(\tilde Q)}=0$, so the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Biquaternions* has no value on the sector. The failure is caused by the norm, not by the spectrum.

**One-sided operators.** Rank $2$, equal to $2Q_t$ times a projection, with kernel the corresponding annihilator plane. Neither multiplication is invertible on either side.

**The "clean degenerate" cell.** It is the cell in which invertibility fails and nothing else does: the eigenvalues are separated, the Peirce decomposition relative to $\tilde Q$ exists and is unique, the annihilators are the two Peirce planes, and the only pathology is the zero eigenvalue, which is exactly the norm condition.

## Summary

| question | answer |
|---|---|
| definition | $\Sigma_{01}=\{N=0,\ B^2\neq0\}$ |
| descriptions | $\mathcal{N}\setminus\mathcal S$; $Q_t\neq0$ on $\mathcal{N}$; $\tilde Q^2=2Q_t\tilde Q$; $c\tilde\Pi$ with $c\neq0$ and $\tilde\Pi$ a non-trivial idempotent; spectrum $\{c,0\}$ |
| geometry | Zariski-open and dense in $\mathcal{N}$; complex cone of complex dimension $3$ and real dimension $6$; smooth, connected; apex removed |
| elements | semisimple zero divisors; minimal polynomial $X(X-c)$ |
| Peirce decomposition | exists, unique, diagonal on $(e_+,e_-)$ |
| centraliser | $\mathbb{C}[\tilde\Pi]\cong\mathbb{C}\oplus\mathbb{C}$, with the four idempotents $0,e_t,\tilde\Pi,\tilde\Pi'$ |
| annihilators | two distinct planes meeting in $\mathbb{C}\tilde\Pi'$, the kernel projector; $\tilde Q$ lies in neither |
| multiplication | $\Sigma_{01}\cdot\Sigma_{01}\subseteq\mathcal{N}$, with $\Sigma_{01}$, $0$ and $\Sigma_{00}\setminus\{0\}$ all attained |
| relation to the cones | $\Sigma_{01}=\mathcal{N}\setminus\mathcal S$; transverse along the sector; tangency only on $\Sigma_{00}$ |
| place in the arrangement | the zero-divisor sector: non-invertibility with full spectral regularity |

The sector is the idempotent sector. It is the set of non-zero scalar multiples of non-trivial idempotents, the complement of the nilpotent stratum inside the null cone, and the one place in the degenerate half of the arrangement where the spectrum is as clean as it can be. Its elements are exactly those whose eigenvalues are one zero and one non-zero: the zero makes them zero divisors, the non-zero makes their spectral decomposition exist.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{ij}$ | the sector with $i=1$ iff $N\neq0$, $j=1$ iff $B^2\neq0$ |
| $\Sigma_{01}$ | the norm-degenerate, spectrally regular sector, this article |
| $\mathcal{N}=\{N=0\}$ | the null cone of the quaternionic norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathcal{N}_{\mathrm{np}}=\Sigma_{01}$ | the non-pure stratum of the null cone |
| $\tilde\Pi,\tilde\Pi'=e_t-\tilde\Pi$ | a non-trivial idempotent and its complement |
| $\tilde\Xi=2\tilde\Pi-e_t$ | the root of $+1$ attached to the idempotent, $\tilde\Xi^2=e_t$ |
| $\tilde\Pi_\pm=(e_t\pm\tilde\Xi)/2$ | the standard pair of a root |
| $E_{12}=(\vec e_x+i\vec e_y)/2$ | the nilpotent of the mixed corner $\mathbb{B}_{+-}$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication, with $L_{\tilde Q}^2=2Q_tL_{\tilde Q}$ |
| $A(\tilde Q)=\ker L_{\tilde Q}$ | the left annihilator, a right ideal |
| $B(\tilde Q)=\ker R_{\tilde Q}$ | the right annihilator, a left ideal |

## Further Reading

- [The Quaternionic Norm-Degenerate, Spectrally Degenerate Sector](the-quaternionic-norm-degenerate-spectrally-degenerate-sector.html), for the opposite corner $\Sigma_{00}$, the nilpotents and the origin.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the null cone and its two strata.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion and the spectral-degenerate cone.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the comparison of the two cones.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the Peirce corners and the nilpotents $E_{ij}$.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the root variety $\tilde\Xi^2=e_t$ and the idempotent manifold.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus $\Rho=\sqrt N$ and its failure at $N=0$.
