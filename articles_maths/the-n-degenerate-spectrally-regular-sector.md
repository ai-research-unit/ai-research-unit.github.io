# __The N-Degenerate, Spectrally Regular Sector__

## Introduction

This is cell $01$ of the four-sector arrangement of the two quadratic conditions

$$
\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

the sector on which the quaternionic norm vanishes and the vector square does not. It is the difference of the null cone and the spectral-degenerate cone,

$$
\Sigma_{01}=\mathcal{N}\setminus\mathcal S,
$$

and it is one of the two **mixed** sectors: the two cells on which the norm problem and the spectral problem give different answers. The vocabulary, the two cones and the naming convention are those of *N-Regularity and N-Degeneracy in the Biquaternion Algebra* and *The Spectrum*. The opposite corner $\Sigma_{00}$ is treated in *The N-Degenerate, Spectrally Degenerate Sector*.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and $\tilde Q=Q_te_t+\vec Q$; the conjugation is ${}^{\natural}$; the quaternionic norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q^{\natural}\tilde Q$, central; and the product is the plain product unless stated otherwise. The null cone is $\mathcal{N}=\{N=0\}$; the spectral-degenerate cone is $\mathcal S=\{B^2=0\}$; **spectrally regular** means $B^2\neq0$.

## Definition and Characterisation

**Definition.** The sector $\Sigma_{01}$ is

$$
\Sigma_{01}=\{N=0,\ B^2\neq0\}=\{Q_t^2+B^2=0,\ B^2\neq0\}.
$$

**Theorem (five descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\tilde Q\in\Sigma_{01}$;

(ii) $\langle\tilde Q\rangle_{\natural}=0$ and $Q_t\neq0$;

(iii) $\tilde Q^2=2Q_t\tilde Q$ with $Q_t\neq0$;

(iv) $\tilde Q=c\,\tilde\Pi$ with $c\in\mathbb{C}^\times$ and $\tilde\Pi$ a non-trivial idempotent;

(v) the spectrum of $\tilde Q$ is $\{\lambda,0\}$ with $\lambda\neq0$.

*Proof.* (i) $\iff$ (ii): on $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=0$, one has $B^2=-Q_t^2$, so $B^2\neq0$ exactly when $Q_t\neq0$.

(ii) $\iff$ (iii): the identity $\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q$, with $B^2=-Q_t^2$, gives $\tilde Q^2=2Q_t^2e_t+2Q_t\vec Q=2Q_t\tilde Q$. Conversely, $\tilde Q^2=2Q_t\tilde Q$ with $Q_t\neq0$ compares central parts and gives $Q_t^2-B^2=2Q_t^2$, hence $B^2=-Q_t^2\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$.

(ii) $\iff$ (iv): put $\tilde\Pi=\tilde Q/(2Q_t)$; then $\tilde\Pi^2=\tilde\Pi$ is (iii), and $\tilde\Pi\notin\{0,e_t\}$ because $\tilde Q\neq0$ and $B^2\neq0$. Conversely, a non-trivial idempotent has scalar part $\tfrac12$: writing $\tilde\Pi=p e_t+\vec\Pi$ with $\vec\Pi\neq0$, the equation $\tilde\Pi^2=\tilde\Pi$ gives $2p\vec\Pi=\vec\Pi$, hence $p=\tfrac12$; then $B^2(\tilde\Pi)=-\tfrac14$ and $\langle\tilde\Pi\rangle_{\natural}=0$. So $c\tilde\Pi$ has $\langle\tilde Q\rangle_{\natural}=0$ and $B^2=-c^2/4\neq0$.

(ii) $\iff$ (v): the characteristic polynomial is $X^2-2Q_tX+N$. When $\langle\tilde Q\rangle_{\natural}=0$ it is $X(X-2Q_t)$, so the spectrum is $\{0,2Q_t\}$, and exactly one eigenvalue is zero exactly when $Q_t\neq0$.

**Corollary (a positive characterisation).** The sector is the set of non-zero complex multiples of non-trivial idempotents:

$$
\Sigma_{01}=\{c\,\tilde\Pi\ :\ c\in\mathbb{C}^\times,\ \tilde\Pi^2=\tilde\Pi,\ \tilde\Pi\neq0,e_t\}.
$$

The scalar is fixed by the element: $c=2Q_t$ and $\tilde\Pi=\tilde Q/(2Q_t)$. So the description is a bijection, not merely a parametrisation.

**Corollary (spectral character).** The sector is characterised by the spectrum alone: it is the set of elements whose spectrum is $\{\lambda,0\}$ with $\lambda\neq0$.

## Geometry

**Theorem (an open subset of the null cone).** $\Sigma_{01}=\mathcal{N}\setminus\Sigma_{00}$ is a Zariski-open subset of the null cone, of complex dimension $3$ and real dimension $6$. It is smooth, connected, and not closed in $\mathbb{B}$; its closure is $\mathcal{N}$, and the boundary it loses is exactly $\Sigma_{00}$.

*Proof.* In $\mathcal{N}$ one has $B^2=-Q_t^2$, so $B^2=0$ is equivalent to $Q_t=0$, which is $\Sigma_{00}$. Hence $\Sigma_{01}=\mathcal{N}\setminus\{Q_t=0\}$ is Zariski-open in $\mathcal{N}$. The null cone is cut out by $\langle\tilde Q\rangle_{\natural}=0$, whose gradient $2\tilde Q$ does not vanish off the origin; the origin lies in $\Sigma_{00}$, so every point of $\Sigma_{01}$ is smooth. Its dimension is that of $\mathcal{N}$, namely $4-1=3$ over $\mathbb{C}$, hence $6$ over $\mathbb{R}$. The closure of a non-empty open subset of the irreducible variety $\mathcal{N}$ is $\mathcal{N}$ itself.

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
The writing has two terms with one coefficient vanishing: it is not the one-term writing $c\,e_+$, because $e_-$ is present and non-trivial. It is unique. An eigenbasis exists, since $B^2\neq0$; the construction in full generality is in *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Eigenbasis*, and its specialisation to $\Sigma_{11}$ is in *The N-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners*.

**Powers.** For $n\geq1$, $\tilde Q^n=c^n e_+$, and the polynomial calculus reads $f(\tilde Q)=f(c)e_++f(0)e_-=f(c)\tilde\Pi+f(0)\tilde\Pi'$. There is no inverse, since $\langle\tilde Q\rangle_{\natural}=0$; the image of the eigenvalue map on the sector is the set of pairs $(c,0)$ with $c\neq0$, so it is not surjective onto $\mathbb{C}^\times\times\mathbb{C}^\times$.

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

**The Peirce decomposition relative to $\tilde Q$ exists and is unique. It has two non-trivial idempotents and one vanishing coefficient: the $2\times2$ Peirce matrix of $\tilde Q$ on the two idempotents is $\operatorname{diag}(c,0)$.**

Let $\tilde Q=c\tilde\Pi$ with $c=2Q_t\neq0$ and $\tilde\Pi$ a non-trivial idempotent, and put $\tilde\Pi'=e_t-\tilde\Pi$. The spectral idempotents are $e_+=\tilde\Pi$ and $e_-=\tilde\Pi'$. The four corners $\mathbb{B}_{st}=e_s\mathbb{B}e_t$ are one-dimensional lines, and the Peirce form is

$$
e_+\tilde Qe_+=c\,e_+,\qquad
e_+\tilde Qe_-=0,\qquad
e_-\tilde Qe_+=0,\qquad
e_-\tilde Qe_-=0.
$$

In the Peirce basis $(\tilde\Pi,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi')$, with the nilpotents normalised by $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi'$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi$, the $2\times2$ Peirce matrix on the two idempotents is

$$
\begin{pmatrix}c&0\\0&0\end{pmatrix}.
$$

The zero coefficient is the only trace of the norm degeneracy in the Peirce data. The idempotent $e_-$ is present and non-trivial, and the decomposition is genuinely two-term: the vanishing coefficient is a value, not a missing idempotent. Both mixed corners are non-zero, so both nilpotents exist.

**The eigenbasis.** Since $B^2\neq0$, the root $\vec\Xi=-i\vec Q/B$ and the pair $(\tilde\Pi_+,\tilde\Pi_-)$ are defined, and the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ exists. The pair is the pair $\{\tilde\Pi,\tilde\Pi'\}$, with the labels fixed by the chosen square root; the construction in full generality is in *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Eigenbasis*, and its specialisation to $\Sigma_{11}$ is in *The N-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners*. With the branch $B=-iQ_t$ one has $\lambda_+=c=2Q_t$, and the left action in the basis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ has the diagonal values $(c,c,0,0)$. The other branch exchanges the labels and gives $(0,0,c,c)$. The zero eigenvalue is carried by the two basis vectors of the $\lambda_-$-eigenspace $\tilde\Pi_-\mathbb{B}$, namely $\vec\Upsilon_+$ and $\tilde\Pi_-$; the spectral decomposition, by contrast, has one zero coefficient.

## Spinors and Chirality

**Each spinor space is a Peirce carrier, a complex plane with a basis made of one idempotent and one nilpotent; in this sector it is also a minimal left ideal. In this sector one eigenvalue is zero, so left multiplication acts on each chirality as $\operatorname{diag}(c,0)$, and the second chirality is the right annihilator.**

The two spinor spaces are
$$
S_+=\mathbb{B}e_+=\mathbb{C}e_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}e_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}e_-,
\qquad
\mathbb{B}=S_+\oplus S_-,
$$
each of complex dimension two. A **spinor of first chirality** is an element of $S_+$, a **spinor of second chirality** an element of $S_-$. The labelling is the one of §*Peirce Data*, with the branch $B=-iQ_t$, so that $\lambda_+=c=2Q_t$ and $\lambda_-=0$. This is the specialisation of §*Spinors and Chirality* of *The Eigenbasis of a Spectrally Regular Biquaternion*.

### The Left Action

Write a general element in the eigenbasis as
$$
\tilde Q_2=Q_{2,11}e_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}e_-,
\qquad Q_{2,ij}\in\mathbb{C}.
$$
A spinor of first chirality is
$$
\xi_+=Q_{2,11}e_++Q_{2,21}\vec\Upsilon_+,
$$
with coordinates $(Q_{2,11},Q_{2,21})$ in the basis $(e_+,\vec\Upsilon_+)$. Since $e_+\in\mathbb{B}_{++}$ and $\vec\Upsilon_+\in\mathbb{B}_{-+}$, left multiplication by $\tilde Q=c\,e_+$ gives
$$
\tilde Q\xi_+=c\,Q_{2,11}e_+,
\qquad
(Q_{2,11},Q_{2,21})\longmapsto(c\,Q_{2,11},0).
$$
A spinor of second chirality is
$$
\xi_-=Q_{2,12}\vec\Upsilon_-+Q_{2,22}e_-,
$$
with coordinates $(Q_{2,12},Q_{2,22})$ in the basis $(\vec\Upsilon_-,e_-)$. Since $\vec\Upsilon_-\in\mathbb{B}_{+-}$ and $e_-\in\mathbb{B}_{--}$,
$$
\tilde Q\xi_-=c\,Q_{2,12}\vec\Upsilon_-,
\qquad
(Q_{2,12},Q_{2,22})\longmapsto(c\,Q_{2,12},0).
$$
Thus
$$
L_{\tilde Q}|_{S_+}=L_{\tilde Q}|_{S_-}=\operatorname{diag}(c,0).
$$
Each chirality carries both eigenvalues, and one component of each is annihilated. This is the spinorial form of the Peirce matrix $\operatorname{diag}(c,0)$: the zero coefficient is a value on a component, not a missing direction.

### The Right Action and Chirality

Right multiplication by $\tilde Q=c\,e_+$ is
$$
\xi_+\tilde Q=c\,\xi_+\quad(\xi_+\in S_+),
\qquad
\xi_-\tilde Q=0\quad(\xi_-\in S_-),
$$
because $e_+$ acts as the identity on the right of $S_+$ and $S_-e_+=0$. Chirality is the right eigenvalue, as in the general article: here $R_{\tilde Q}$ is $c$ on $S_+$ and $0$ on $S_-$. The second chirality is therefore the right annihilator,
$$
S_-=\ker R_{\tilde Q}=B(\tilde Q),
$$
while the left annihilator $A(\tilde Q)=\ker L_{\tilde Q}$ is the other plane, spanned by $\vec\Upsilon_+$ and $e_-$, which is the $\lambda_-$-eigenspace of $L_{\tilde Q}$.

The spinor spaces and the eigenspaces of $L_{\tilde Q}$ are transverse: each spinor space contains one vector of each eigenspace, and each eigenspace contains one vector of each spinor space. A chirality is therefore not an eigenspace of $L_{\tilde Q}$.

### The Matrix Picture

Under the assignment
$$
e_+\mapsto E_{11},\qquad
\vec\Upsilon_-\mapsto E_{12},\qquad
\vec\Upsilon_+\mapsto E_{21},\qquad
e_-\mapsto E_{22},
$$
a general element is represented by
$$
\mathsf M_2^{Q}(\tilde Q_2)=
\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix},
\qquad
\mathsf M_2^{Q}(\tilde Q)=
\begin{pmatrix}c&0\\0&0\end{pmatrix}.
$$
The first column is $S_+$, the second is $S_-$, and the two rows are the two spectral eigenspaces of $L_{\tilde Q}$. A general element is a pair of spinors, one of each chirality, and is not itself a spinor.

## Multiplication

**Products stay on the null cone.** The norm is multiplicative, so for $\tilde P,\tilde Q\in\Sigma_{01}$,

$$
\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}=0,
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

and they are proportional only if $Q_t=0$ or $\vec Q=0$. On $\Sigma_{01}$ one has $Q_t\neq0$ and $\vec Q\neq0$, so the gradients are independent and the intersection $\mathcal{N}\cap\mathcal S$ is nowhere dense in $\mathcal{N}$ there. The tangency of the two cones is a phenomenon of the boundary $\Sigma_{00}$, where both gradients become $2(0,\vec Q)$.

**Independence witness.** Every element of the sector is **$\natural$-degenerate** and a **non-unit**, with **distinct eigenvalues**: $\langle\tilde Q\rangle_{\natural}=0$, so it is a zero divisor of the plain product, while $B^2=-Q_t^2\neq0$, so its two eigenvalues $0$ and $2Q_t$ are separated. The standard example is

$$
\tilde Q=e_t+i\vec e_x,\qquad N=0,\qquad B^2=-1,\qquad \tilde Q^2=2\tilde Q,
$$

with spectral idempotents $\tilde\Pi_\pm=(e_t\pm i\vec e_x)/2$, spectrum $\{2,0\}$ and Peirce form $2\tilde\Pi_+ + 0\cdot\tilde\Pi_-$ relative to $\tilde Q$. This is the element that prevents the null cone from being identified with the spectral-degenerate cone.

## Comparison with the Other Three Sectors

| sector | conditions | elements | spectrum | Peirce decomposition | product |
|---|---|---|---|---|---|
| **doubly regular** $\Sigma_{11}$ | $\langle\tilde Q\rangle_{\natural}\neq0$, $B^2\neq0$ | units with distinct eigenvalues | $\{\lambda_+,\lambda_-\}$, distinct and non-zero | exists, unique | stays in $\mathbb{B}^\times$; can land in $\Sigma_{10}$ |
| **$\natural$-degenerate, spectrally regular** $\Sigma_{01}$ | $\langle\tilde Q\rangle_{\natural}=0$, $B^2\neq0$ | $c\tilde\Pi$, $c\neq0$, $\tilde\Pi$ a non-trivial idempotent | $\{c,0\}$ | exists, unique | stays on $\mathcal{N}$; all three outcomes |
| **$\natural$-regular, spectrally degenerate** $\Sigma_{10}$ | $\langle\tilde Q\rangle_{\natural}\neq0$, $B^2=0$ | units with a repeated eigenvalue, plus the scalar line minus $0$ | $\{Q_t\}$ | fails off the scalar line, one term on it | stays in $\mathbb{B}^\times$; can land in $\Sigma_{11}$ |
| **doubly degenerate** $\Sigma_{00}$ | $\langle\tilde Q\rangle_{\natural}=0$, $B^2=0$ | non-zero nilpotents of index two, plus the origin | $\{0\}$ | fails off the origin | $0$ or $\Sigma_{01}$ |

**The two mixed sectors.** $\Sigma_{01}$ and $\Sigma_{10}$ are the independence witnesses: $\Sigma_{01}$ is a zero divisor with a full eigenbasis, $\Sigma_{10}$ is a unit with none. Neither cone contains the other, and these are the cells that show it.

**Position among the four sectors.** Sector $01$ is the **idempotent stratum** of the null cone: the elements $c\tilde\Pi$ with $c\neq0$ and $\tilde\Pi$ a non-trivial idempotent. It is the only sector on which the norm vanishes while the spectrum stays separated, so it is one of the two independence witnesses. The finer split inside $\Sigma_{10}$ and $\Sigma_{00}$ is by the minimal polynomial, not by the two predicates; it is recorded in *Relations between the N Norm and Spectral Regularity and Degeneracy*, §*The Chain of Invariants*.

## Consequences

**Eigenbasis.** It exists. The spectral idempotents are $e_+=\tilde Q/(2Q_t)$ and $e_-=e_t-e_+$, and they are unique. The normalised Peirce eigenbasis is unique with the normalisation fixed. The Peirce decomposition relative to $\tilde Q$ is the only one.

**The flow.** The root $\vec U=\vec Q/B$ exists and is pure, and $e^{\theta\tilde Q}=e^{\theta Q_t}W(-\theta,B/2\pi)$, with $W$ the Fourier kernel of *Biquaternion Continuous Harmonic Analysis*, §*The Fourier Kernel*. This holds even though $\langle\tilde Q\rangle_{\natural}=0$ and the element is a zero divisor. The exponential is a unit, like every exponential. The Hermitian norm, $\langle\tilde X\rangle_*=\operatorname{Sc}(\tilde X\tilde X^*)$, is

$$
\langle e^{\theta\tilde Q}\rangle_*
=\lvert e^{\theta Q_t}\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\vec U\rVert_E^2\right),
\qquad
\lVert\vec U\rVert_E^2\ge1,
$$

with equality exactly when the element is normal: $\tilde Q\tilde Q^*=\tilde Q^*\tilde Q$, with $\tilde X^*=\overline{\tilde X^\natural}$ (*The Biquaternion Eigenvalue Decomposition*, §*The Hermitian Case*). The flow is $*$-unitary for the Hermitian form exactly when $Q_t\in i\mathbb{R}$ and $\vec Q\in\mathbb{R}^3$ — the massless material case — and self-adjoint exactly when $Q_t\in\mathbb{R}$ and $\vec Q\in i\mathbb{R}^3$. Spectral regularity, not invertibility, is what the Fourier dictionary needs.

**Polar decomposition.** The modulus is $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}=0$, so the modulus–unit polar decomposition of *The Polar Decomposition of a N-Regular Biquaternion* has no value on the sector. The failure is caused by the norm, not by the spectrum.

**One-sided operators.** Rank $2$, equal to $2Q_t$ times a projection, with kernel the corresponding annihilator plane. Neither multiplication is invertible on either side.

**The "clean degenerate" cell.** It is the cell in which invertibility fails and nothing else does: the eigenvalues are separated, the Peirce decomposition relative to $\tilde Q$ exists and is unique, the annihilators are the two Peirce planes, and the only pathology is the zero eigenvalue, which is exactly the norm condition.

## The Generators, the Eigenvalues, and the Element

**The two idempotents and the root.**

$$
\boxed{\ e_+=\tilde\Pi=\frac{\tilde Q}{2Q_t}=\frac12 e_t+\frac{Q_x}{2Q_t}\vec e_x+\frac{Q_y}{2Q_t}\vec e_y+\frac{Q_z}{2Q_t}\vec e_z\ }
$$

$$
\boxed{\ e_-=\tilde\Pi'=e_t-\frac{\tilde Q}{2Q_t}=\frac12 e_t-\frac{Q_x}{2Q_t}\vec e_x-\frac{Q_y}{2Q_t}\vec e_y-\frac{Q_z}{2Q_t}\vec e_z\ }
$$

$$
\boxed{\ \vec\Xi=2\tilde\Pi-e_t=\frac{\vec Q}{Q_t}=\frac{Q_x}{Q_t}\vec e_x+\frac{Q_y}{Q_t}\vec e_y+\frac{Q_z}{Q_t}\vec e_z,\qquad \vec\Xi^2=e_t\ }
$$

**The two nilpotents.** They are the closed form of *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Transverse-Vector Construction*, read with $B=-iQ_t$, the branch that puts $\lambda_+=2Q_t$; the other branch exchanges the two labels. With $\vec w=\vec e_x+\vec e_y+\vec e_z$ and $\Sigma=Q_x+Q_y+Q_z$,

$$
\boxed{\ \vec\Upsilon_+=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q+\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}},\qquad B=-iQ_t\ }
$$

$$
\boxed{\ \vec\Upsilon_-=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q-\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}},\qquad B=-iQ_t\ }
$$

with the normalisation $\vec\Upsilon_+\vec\Upsilon_-=e_-$ and $\vec\Upsilon_-\vec\Upsilon_+=e_+$ for one fixed branch of the square root; on the exceptional cone the axis charts replace the symmetric formula.

**The two eigenvalues.**

$$
\boxed{\ \lambda_+=2Q_t\ }
$$

$$
\boxed{\ \lambda_-=0\ }
$$

The other branch, $B=+iQ_t$, gives $\lambda_+=0$ and $\lambda_-=2Q_t$ and exchanges the two labels; the unordered spectrum is unchanged.

**The element.** In the eigenbasis $(e_+,\vec\Upsilon_-,\vec\Upsilon_+,e_-)$,

$$
\boxed{\ \tilde Q=2Q_t\,e_++0\cdot\vec\Upsilon_-+0\cdot\vec\Upsilon_++0\cdot e_-\ }
$$

$$
\boxed{\ \tilde Q=2Q_t\,e_++0\cdot e_-=2Q_t\,\tilde\Pi\ }
$$

In this basis $L_{\tilde Q}$ has the values $(2Q_t,2Q_t,0,0)$ and $R_{\tilde Q}$ the values $(2Q_t,0,2Q_t,0)$. In the fixed basis,

$$
\boxed{\ \tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_t\neq0,\quad B^2=-Q_t^2\ }
$$

## Summary

| question | answer |
|---|---|
| definition | $\Sigma_{01}=\{N=0,\ B^2\neq0\}$ |
| descriptions | $\mathcal{N}\setminus\mathcal S$; $Q_t\neq0$ on $\mathcal{N}$; $\tilde Q^2=2Q_t\tilde Q$; $c\tilde\Pi$ with $c\neq0$ and $\tilde\Pi$ a non-trivial idempotent; spectrum $\{c,0\}$ |
| geometry | Zariski-open and dense in $\mathcal{N}$; complex cone of complex dimension $3$ and real dimension $6$; smooth, connected; apex removed |
| elements | semisimple zero divisors; minimal polynomial $X(X-c)$ |
| Peirce decomposition | exists, unique, diagonal on $(e_+,e_-)$ |
| eigenbasis | normalised Peirce basis; unique with the normalisation fixed |\n| spinors | $S_\pm=\mathbb{B}e_\pm$, Peirce carriers (minimal left ideals here); $L_{\tilde Q}=\operatorname{diag}(c,0)$ on each, $R_{\tilde Q}=c$ on $S_+$ and $0$ on $S_-$ |
| centraliser | $\mathbb{C}[\tilde\Pi]\cong\mathbb{C}\oplus\mathbb{C}$, with the four idempotents $0,e_t,\tilde\Pi,\tilde\Pi'$ |
| annihilators | two distinct planes meeting in $\mathbb{C}\tilde\Pi'$, the kernel projector; $\tilde Q$ lies in neither |
| multiplication | $\Sigma_{01}\cdot\Sigma_{01}\subseteq\mathcal{N}$, with $\Sigma_{01}$, $0$ and $\Sigma_{00}\setminus\{0\}$ all attained |
| relation to the cones | $\Sigma_{01}=\mathcal{N}\setminus\mathcal S$; transverse along the sector; tangency only on $\Sigma_{00}$ |
| place in the arrangement | the zero-divisor sector: non-invertibility with full spectral regularity |

The sector is the idempotent sector. It is the set of non-zero scalar multiples of non-trivial idempotents, the complement of the nilpotent stratum inside the null cone, and the one place in the degenerate half of the arrangement where the spectrum is as clean as it can be. Its elements are exactly those whose eigenvalues are one zero and one non-zero: the zero makes them zero divisors, the non-zero makes their spectral decomposition exist.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{ij}$ | the sector with $i=1$ iff $\langle\tilde Q\rangle_{\natural}\neq0$, $j=1$ iff $B^2\neq0$ |
| $\Sigma_{01}$ | the $\natural$-degenerate, spectrally regular sector, this article |
| $\mathcal{N}=\{N=0\}$ | the null cone of the quaternionic norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathcal{N}_{\mathrm{np}}=\Sigma_{01}$ | the non-pure stratum of the null cone |
| $\tilde\Pi,\tilde\Pi'=e_t-\tilde\Pi$ | a non-trivial idempotent and its complement |
| $\vec\Xi=2\tilde\Pi-e_t$ | the pure root of $+1$ attached to the idempotent, $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$ | the standard pair of a root |
| $E_{12}=(\vec e_x+i\vec e_y)/2$ | the nilpotent of the mixed corner $\mathbb{B}_{+-}$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication, with $L_{\tilde Q}^2=2Q_tL_{\tilde Q}$ |
| $A(\tilde Q)=\ker L_{\tilde Q}$ | the left annihilator, a right ideal |
| $B(\tilde Q)=\ker R_{\tilde Q}$ | the right annihilator, a left ideal; equal to $S_-$ |\n| $S_\pm=\mathbb{B}e_\pm$ | the spinor spaces, the two chiralities |\n| $Q_{2,ij}$ | the coordinates of a general element in the eigenbasis |\n| $\mathsf M_2^{Q}$ | the matrix model attached to the eigenbasis |

## Further Reading

- [The Eigenbasis of a Spectrally Regular Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the construction in full generality, the normalisation, the expansion of an arbitrary biquaternion and the spinor reading.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the opposite corner $\Sigma_{00}$, the nilpotents and the origin.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null cone and its two strata.
- [The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion and the spectral-degenerate cone.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the comparison of the two cones.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-in-the-biquaternion-algebra.html), for the Peirce corners and the nilpotents $E_{ij}$.
- [Idempotents](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the root variety $\tilde\Xi^2=e_t$ and the idempotent manifold.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus $\Rho=\sqrt N$ and its failure at $\langle\tilde Q\rangle_{\natural}=0$.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the exponential as a Fourier kernel, the root supplied by the element and the Hermitian norm of the flow.
