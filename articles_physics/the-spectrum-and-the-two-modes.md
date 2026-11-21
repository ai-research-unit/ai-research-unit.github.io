# __The Spectrum and the Two Modes__

## Introduction

The question is what a single element does when it multiplies. Left multiplication by $\tilde Q$ is a linear operator on the algebra, so it has eigenvalues and eigenspaces; the section computes them, decides when an eigenbasis exists, and classifies the elements for which it does not.

The answer has two branches and one number between them.

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2,\qquad \operatorname{disc}p_{\tilde Q}=-4B^2,\qquad \lambda_\pm=Q_t\pm iB .
$$

The number is $B^2=Q_x^2+Q_y^2+Q_z^2$, the square of the vector part. It involves no scalar part, so the whole classification is blind to the trace and depends only on the direction and the modulus of the vector part.

If $B^2\neq0$ the eigenvalues are distinct, the element is semisimple, the spectral idempotents exist, and an eigenbasis exists. If $B^2=0$ the eigenvalues have coalesced, the two-term decomposition fails, and a Jordan basis replaces the eigenbasis.

The single idea is that the spectrum is two numbers and the element is eight parameters. The spectrum fixes the trace and the norm and nothing else about the vector part; the eigenbasis is attached to the direction of the vector part, so it is a frame, and what the spectrum leaves free is exactly the frame. Every reading below is a consequence of that division.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the spectral criterion, eigenvalues and eigenvectors, the characteristic and minimal polynomials, the two cases, the spectral-degenerate cone, the isotropic flag, the similarity classification, the restrictions to the six subspaces | [The Spectrum](../articles_maths/the-spectrum-of-a-biquaternion.html) |
| the centraliser, its three cases, the double centraliser, the uniqueness of the semisimple–nilpotent split | [The Centraliser](../articles_maths/the-centraliser-in-the-biquaternion-algebra.html) |
| the Jordan–Chevalley decomposition, the four types, the Peirce form, the multiplicative form, the two bases, five worked examples | [The Semisimple–Nilpotent Split](../articles_maths/the-semisimple-nilpotent-split-of-a-biquaternion.html) |
| the root, the spectral idempotents, the corners, the nilpotent pair, the normalisation, the eigenbasis, the Fourier reading, the four labels, the matrix model, the expansion theorem, the dependence on the line, spinors and the Peirce index | [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html) |
| eight computed cases, the regimes, the eigenbasis table, the matrix table | [Worked Examples of an Eigenbasis of a Biquaternion](../articles_maths/worked-examples-of-an-eigenbasis-of-a-biquaternion.html) |
| the sector, its three strata, the obstruction, the adapted and canonical frames, the Jordan pair, the Jordan basis, the matrix model, inversion and the truncated exponential, the relation to the regular sector | [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html) |

The rows are the entry's order. The criterion first, because it states the eigenvalue problem without a module; then the centraliser, which is what commutes with the element; then the split; then the two bases, one per branch; then the worked cases.

## The Results in Brief

### The Criterion

**An eigenvalue is a scalar for which a left ideal is proper, and the criterion turns that into one equation.**

$$\lambda\ \text{is an eigenvalue of}\ \tilde Q\iff\tilde Q-\lambda e_t\ \text{is not invertible}\iff(\lambda-Q_t)^2+B^2=0 .$$

The proof uses no matrix. If $\tilde Q-\lambda e_t$ is invertible, the left ideal it generates is the algebra; if it generates the algebra, injectivity of left multiplication in finite dimension gives a two-sided inverse. The unit condition is decided by the conjugate product,

$$
(\tilde Q-\lambda e_t)(\tilde Q-\lambda e_t)^{\natural}=\bigl((\lambda-Q_t)^2+B^2\bigr)e_t ,
$$

which is a scalar, non-zero exactly off the two roots.

The characteristic polynomial is quadratic, and its coefficients are the trace and the norm.

$$
p_{\tilde Q}(X)=X^2-2Q_tX+(Q_t^2+B^2),\qquad \lambda_\pm=Q_t\pm iB,\qquad \lambda_++\lambda_-=2Q_t,\qquad \lambda_+\lambda_-=Q_t^2+B^2 .
$$

Cayley–Hamilton is the same identity, and it gives the inverse.

$$
\tilde Q^2-2Q_t\tilde Q+(Q_t^2+B^2)e_t=0,\qquad \tilde Q^{-1}=\frac{\tilde Q^{\natural}}{Q_t^2+B^2}\quad\text{when } Q_t^2+B^2\neq0 .
$$

The eigenspaces are right ideals. For a non-scalar element and an eigenvalue $\lambda$, the eigenvectors form $\operatorname{Ann}_\ell(\tilde Q-\lambda e_t)$, which is a non-zero proper right ideal, hence of complex dimension two.

Left and right eigenvalues agree. The scalars are central, so $\tilde Qv=\lambda v$ and $\tilde Qv=v\lambda$ define the same set for $\lambda\in\mathbb{C}$, and that set is the spectrum.

### The Discriminant and the Two Cases

Four descriptions of one condition.

| case | condition | spectrum | spectral decomposition | eigenbasis |
| --- | --- | --- | --- | --- |
| regular | $B^2\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | two terms, unique | exists |
| degenerate | $B^2=0$ | $\{Q_t\}$ | one term iff $\vec Q=0$ | every basis iff $\vec Q=0$, else none |

The equivalence is the whole content of the split.

$$
B^2\neq0\iff\lambda_+\neq\lambda_-\iff\tilde Q\ \text{semisimple}\iff L_{\tilde Q}\ \text{diagonalisable} .
$$

**The condition is not multiplicative.** Neither branch is closed under products, and the two witnesses are

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2i\vec e_z,\qquad (e_t+\vec e_x)(e_t-\vec e_x)=2e_t ,
$$

the first taking two cone elements off the cone and the second taking two regular elements onto it. The regular case is therefore not a subgroup, and the spectral condition is not preserved by multiplication in either direction.

### The Four Minimal Polynomials

The characteristic polynomial has two coefficients; the minimal polynomial separates what it cannot.

| type | condition | $p_{\tilde Q}$ | $m_{\tilde Q}$ |
| --- | --- | --- | --- |
| semisimple, non-scalar | $B^2\neq0$ | $(X-Q_t)^2+B^2$ | $(X-Q_t)^2+B^2$ |
| scalar | $B^2=0$, $\vec Q=0$ | $(X-Q_t)^2$ | $X-Q_t$ |
| Jordan | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $(X-Q_t)^2$ | $(X-Q_t)^2$ |
| nilpotent | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $X^2$ | $X^2$ |

Two rows share the characteristic polynomial and two share $X^2$ after translation. The scalar row and the Jordan row have the same $p$, and only the minimal polynomial separates them; the Jordan row and the nilpotent row have the same $m$ up to the scalar shift, and only the scalar part separates them. No single invariant does both jobs.

### The Operator Form

The discriminant also reads on the operators, and there it decides between a complex structure and a nilpotent.

$$
L_{\vec Q}^{\,2}=R_{\vec Q}^{\,2}=-B^2\,\mathrm{id},\qquad
m_{L_{\vec Q}}=m_{R_{\vec Q}}=
\begin{cases}X^2+B^2,&B^2\neq0,\\ X^2,&B^2=0,\ \vec Q\neq0,\\ X,& \vec Q=0.\end{cases}
$$

**Off the cone the directional part is a complex structure.** With $J=L_{\vec Q}/B$ one has $J^2=-\mathrm{id}$ and the eigenvalues of $L_{\vec Q}$ are $\pm iB$. On the cone the directional part is nilpotent of index two.

The same dichotomy in the commutator form is $\mathrm{ad}_{\vec Q}^{\,3}=-4B^2\mathrm{ad}_{\vec Q}$, nilpotent exactly on $\mathcal S$.

### The Spectral Decomposition and the Eigenbasis

**Off the cone the root exists, and it is the vector part rescaled to square one.**

$$
\vec Z=-\frac{i\vec Q}{B},\qquad \vec Z^2=e_t,\qquad \tilde Q=Q_te_t+iB\vec Z .
$$

The spectral idempotents are the Lagrange idempotents, and they are unique.

$$
\tilde\Pi_\pm=\frac{e_t\pm\vec Z}{2}=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},\qquad
\tilde\Pi_\pm^2=\tilde\Pi_\pm,\qquad \tilde\Pi_+\tilde\Pi_-=0,\qquad \tilde\Pi_++\tilde\Pi_-=e_t ,
$$

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_- .
$$

The eigenspaces of $L_{\tilde Q}$ are the right ideals generated by the idempotents, each of complex dimension two.

$$
\ker(L_{\tilde Q}-\lambda_\pm)=\tilde\Pi_\pm\mathbb{B} .
$$

An eigenbasis is one vector in each corner, and the left and right actions are both diagonal in it.

$$
\mathcal{B}(\tilde Q)=(\tilde\Pi_+,\ \vec\Upsilon_-,\ \vec\Upsilon_+,\ \tilde\Pi_-),\qquad
L_{\tilde Q}=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),\qquad
R_{\tilde Q}=\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-) .
$$

The four vectors are the matrix units, and their multiplication is the corner rule.

| product | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |
| --- | --- | --- | --- | --- |
| $\tilde\Pi_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $0$ | $0$ |
| $\vec\Upsilon_-$ | $0$ | $0$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ |
| $\vec\Upsilon_+$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ | $0$ | $0$ |
| $\tilde\Pi_-$ | $0$ | $0$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |

The pair is fixed only up to one scale.

$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad \vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad \vec\Upsilon_\pm^2=0,\qquad
(\vec\Upsilon_+,\vec\Upsilon_-)\longmapsto(\mu\vec\Upsilon_+,\mu^{-1}\vec\Upsilon_-) .
$$

Every element has a unique expansion in that basis, and the coordinate map is an algebra isomorphism.

$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

What the basis diagonalises is exactly the pencil generated by the element.

$$
\tilde Q_2\ \text{diagonal in}\ \mathcal{B}(\tilde Q)\iff\tilde Q_2\in\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-\iff\tilde Q_2\in\operatorname{span}\{e_t,\tilde Q\} .
$$

The four labels are independent, and they are the corner indices.

| vector | corner | $L_{\tilde Q}$ | $R_{\tilde Q}$ | $L_{\vec Z}$ | $R_{\vec Z}$ |
| --- | --- | --- | --- | --- | --- |
| $\tilde\Pi_+$ | $\mathbb{B}_{++}$ | $\lambda_+$ | $\lambda_+$ | $+1$ | $+1$ |
| $\vec\Upsilon_-$ | $\mathbb{B}_{+-}$ | $\lambda_+$ | $\lambda_-$ | $+1$ | $-1$ |
| $\vec\Upsilon_+$ | $\mathbb{B}_{-+}$ | $\lambda_-$ | $\lambda_+$ | $-1$ | $+1$ |
| $\tilde\Pi_-$ | $\mathbb{B}_{--}$ | $\lambda_-$ | $\lambda_-$ | $-1$ | $-1$ |

### The Centraliser

The centraliser is the set of elements that commute with the element, and it has three cases.

| case | element | $C(\tilde Q)$ | type | complex dimension |
| --- | --- | --- | --- | --- |
| $B^2\neq0$ | general, non-central | $\mathbb{C}[\tilde Q]$ | $\mathbb{C}\times\mathbb{C}$ | $2$ |
| $B^2=0$, $\vec Q=0$ | $Q_te_t$ | $\mathbb{B}$ | the algebra | $4$ |
| $B^2=0$, $\vec Q\neq0$ | $Q_te_t+\vec\Upsilon$, $\vec\Upsilon^2=0$ | $\mathbb{C}[\tilde Q]$ | the dual numbers $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ | $2$ |

The equality $C(\tilde Q)=\mathbb{C}[\tilde Q]$ is the statement that the element is nonderogatory, and it fails only at the centre, where the minimal polynomial has degree one and the centraliser has dimension four.

The double centraliser is the subalgebra itself, except at the centre, where it is the centre.

$$
C(C(\tilde Q))=C(\tilde Q)\ (Q_t^2+B^2\neq0),\qquad C(\mathbb{B})=\mathbb{C}e_t .
$$

The centraliser is what makes the split unique. Both parts of a Jordan–Chevalley decomposition lie in $\mathbb{C}[\tilde Q]$, which is commutative, so two decompositions agree.

### The Semisimple–Nilpotent Split

**Every element is a semisimple part plus a commuting nilpotent part, uniquely, and both are polynomials in the element.**

$$
\tilde Q=\tilde Q_s+\vec\Upsilon,\qquad \tilde Q_s\vec\Upsilon=\vec\Upsilon\tilde Q_s,\qquad \tilde Q_s,\vec\Upsilon\in\mathbb{C}[\tilde Q] .
$$

The four types are the four positions of the pair.

| type | $\tilde Q_s$ | $\vec\Upsilon$ | frame | $m_{\tilde Q}$ |
| --- | --- | --- | --- | --- |
| semisimple | $\tilde Q$ | $0$ | spectral | $(X-Q_t)^2+B^2$ |
| scalar | $\tilde Q$ | $0$ | $\{e_t\}$ | $X-Q_t$ |
| Jordan | $Q_te_t$ | $\vec Q$ | defective | $(X-Q_t)^2$ |
| nilpotent | $0$ | $\tilde Q$ | defective | $X^2$ |

In a frame adapted to the element the split is a corner pattern.

$$
\tilde Q_s=e\tilde Q_se+e'\tilde Q_se',\qquad \vec\Upsilon=e\vec\Upsilon e',\qquad \vec\Upsilon^2=0 .
$$

The nilpotent index is two, never higher, and the reason is the corner rule.

$$
(e\mathbb{B}e')(e\mathbb{B}e')=e\mathbb{B}(e'e)\mathbb{B}e'=0 .
$$

For an invertible element the additive split has a multiplicative form.

$$
\tilde Q=\tilde Q_s\tilde U,\qquad \tilde U=e_t+\tilde Q_s^{-1}\vec\Upsilon,\qquad \tilde U^{-1}=e_t-\tilde Q_s^{-1}\vec\Upsilon .
$$

The hypothesis is not removable. A semisimple zero divisor has a non-invertible semisimple part, so no product exists beyond the trivial one; a nilpotent element has no semisimple factor at all.

### The Degenerate Cone and the Jordan Basis

The cone is one equation read three ways.

$$
\mathcal S=\{B^2=0\}=\{\vec Q^2=0\}=\{\operatorname{disc}p_{\tilde Q}=0\} .
$$

Geometrically the vector part is isotropic; algebraically it is square-zero; spectrally the two eigenvalues have coalesced.

**It is a cone, not a subspace, and its singular locus is the whole scalar line.**

$$
\mathcal S=\mathbb{C}e_t\times\{\vec Q:\vec Q^2=0\},\qquad \dim_{\mathbb{C}}\mathcal S=3,\qquad \dim_{\mathbb{R}}\mathcal S=6 .
$$

It has three strata, disjoint and exhaustive.

$$
\mathcal S^{\mathrm{s}}=\{\vec Q=0\},\qquad \mathcal S^{\mathrm{n}}=\{\vec Q\neq0,\,Q_t=0\},\qquad \mathcal S^{\mathrm{u}}=\{\vec Q\neq0,\,Q_t\neq0\} .
$$

On the cone the quaternionic norm is the square of the scalar part, so the cone contains units.

$$
\langle\tilde Q\rangle_{\natural}=Q_t^2,\qquad \tilde Q^{-1}=Q_t^{-1}\Bigl(e_t-\frac{\vec Q}{Q_t}\Bigr)\ (Q_t\neq0) .
$$

The isotropic line admits no canonical complement; it flags the space instead.

$$
0\subset\mathbb{C}\vec Q\subset\ker L_{\vec Q}=\operatorname{im}L_{\vec Q}\subset\mathbb{B},\qquad 0\subset\mathbb{C}\vec Q\subset\vec Q^{\perp}\subset\mathbb{C}^3 .
$$

A frame adapted to the element splits the flag, and the definite Hermitian form selects one such frame.

$$
\tilde\Pi_+=\frac{\vec Q\vec Q^*}{2\langle\vec Q\rangle_*},\qquad \tilde\Pi_-=\frac{\vec Q^*\vec Q}{2\langle\vec Q\rangle_*},\qquad \vec\Upsilon_+=\frac{\vec Q^*}{2\langle\vec Q\rangle_*},\qquad \vec\Upsilon_-=\vec Q .
$$

The Jordan basis is a pair of blocks, and the two chains are the two mixed corners.

$$
\mathcal{J}(\tilde Q)=(\vec\Upsilon_-,\ \tilde\Pi_-,\ \tilde\Pi_+,\ \vec\Upsilon_+),\qquad L_{\tilde Q}=\operatorname{diag}\bigl(J_2(Q_t),J_2(Q_t)\bigr),\qquad J_2(Q_t)=\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}.
$$

The exponential truncates on the cone, so there is no frequency.

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\bigl(e_t+\theta\vec Q\bigr),
$$

and the exponential of every element of the cone lies in the unit half $\Sigma_{10}$.

### The Similarity Classification

Similar elements have the same spectrum, and off the cone the converse holds.

$$
\tilde Q_2=S\tilde Q_1S^{-1}\ (S\ \text{an invertible element})\quad\Longrightarrow\quad \sigma(\tilde Q_2)=\sigma(\tilde Q_1) ,
$$

and off the cone the class is determined by the unordered pair $\{\lambda_+,\lambda_-\}$. On the cone the spectrum is the singleton $\{Q_t\}$ and carries no information beyond the scalar part: exactly two classes share it, the central class and the Jordan class.

### The Worked Cases

Eight elements, one per regime.

| case | $\tilde Q$ | $B$ | $\lambda_+$ | $\lambda_-$ | regime |
| --- | --- | --- | --- | --- | --- |
| 1 | $e_t$ | $0$ | $1$ | $1$ | scalar |
| 2 | $\vec e_x$ | $1$ | $i$ | $-i$ | distinct |
| 3 | $\frac{1}{\sqrt2}(e_t+\vec e_x)$ | $\frac{1}{\sqrt2}$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | distinct |
| 4 | $\sqrt2\,e_t+i\vec e_x$ | $i$ | $\sqrt2-1$ | $\sqrt2+1$ | distinct |
| 5 | $(1-\frac{i}{\sqrt2})e_t+(1+\frac{i}{\sqrt2})\vec e_x$ | $1+\frac{i}{\sqrt2}$ | $a(1+i)$ | $b(1-i)$ | distinct |
| 6 | $e_t+\vec e_y+\frac{i}{\sqrt2}\vec e_x+\frac{i}{\sqrt2}\vec e_z$ | $0$ | $1$ | $1$ | Jordan |
| 7 | $(1-\frac{i}{2})e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $\sqrt{\frac14+i}$ | $1-\frac{i}{2}+iB$ | $1-\frac{i}{2}-iB$ | distinct |
| 8 | $(1+i)e_t+\vec e_x+i\vec e_y$ | $0$ | $1+i$ | $1+i$ | Jordan |

Cases 2 to 5 share one eigenbasis. All four have $\vec Q$ a complex multiple of $\vec e_x$ with the branch chosen so that $\vec Z=-i\vec e_x$, so the idempotents are

$$
\tilde\Pi_+=\tfrac12\bigl(e_t-i\vec e_x\bigr),\qquad \tilde\Pi_-=\tfrac12\bigl(e_t+i\vec e_x\bigr),
$$

for all four, and only the diagonal values differ: $(\pm i,\pm i)$ in case 2, the pair $\frac{1\pm i}{\sqrt2}$ in case 3, the real pair $\sqrt2\mp1$ in case 4, and a complex pair in case 5.

Cases 6 and 8 are the two halves of the Jordan type. Case 6 is unipotent with a real scalar part; case 8 is unipotent with a complex scalar part, and its vector part is null while its norm is not, so a null vector part does not give a degenerate norm.

Case 4 is the warning about the root. Its $B$ is imaginary and its spectrum is real, so the root need not be real for the spectrum to be real.

## The Interpretations

### I.5.a — The Eigenvalue Is a Complex Frequency, and $B$ Is the Half-Gap

Read: the spectrum is the pair $\lambda_\pm=Q_t\pm iB$, so the two eigenvalues differ by $2iB$ and their product is the norm.

The half-gap is $iB$, not $B$. The difference is $\lambda_+-\lambda_-=2iB$; the factor $i$ is the one in the characteristic polynomial and it is not decoration. Writing the eigenvalues as complex frequencies in the convention $e^{-i\lambda t}$,

$$
\lambda_\pm=\omega_\pm-i\gamma_\pm,\qquad B=\frac{\gamma_--\gamma_+}{2}-\frac{i}{2}\bigl(\omega_+-\omega_-\bigr),
$$

so the real part of $B$ is half the difference of the damping rates and the imaginary part is minus half the difference of the oscillation frequencies. In the convention $e^{+i\lambda t}$ the two roles are exchanged.

The physical reading is that one algebraic number has three sector names. On the material sector $B$ is a momentum magnitude; on the informational sector it is a half-gap; for a complex $B$ it is a complex half-splitting, and the case is the general one, since normality is not implied by spectral regularity.

The boundary. The frequency reading needs an evolution convention, and the algebra supplies none. For an observable the eigenvalues are outcomes rather than frequencies, and the word *gap* is then the difference of two outcomes.

### I.5.b — Reality of the Spectrum Is a Property of the Sector, Not of the Algebra

Read: the eigenvalues are $Q_t\pm iB$ with $B^2=Q_x^2+Q_y^2+Q_z^2$. Whether they are real depends on the sign of that sum, and the sign is fixed by the sector the element lives in.

| subspace | restriction of $B^2$ | consequence for $B$ |
| --- | --- | --- |
| $\mathbb{B}_{H}$, quaternion | $q_x^2+q_y^2+q_z^2$, real $\ge0$ | $B$ real or imaginary, never complex |
| $\mathbb{B}_{iH}$, anti-quaternion | $-(q_x^2+q_y^2+q_z^2)$ | $B$ imaginary or real |
| $\mathbb{B}_{\Psi}$, Hermitian | $-(a_x^2+a_y^2+a_z^2)$, $a_k$ real | $B=i\lvert\vec a\rvert$: eigenvalues $Q_t\mp\lvert\vec a\rvert$, real |
| $\mathbb{B}_{\Phi}$, anti-Hermitian | $a_x^2+a_y^2+a_z^2$, $a_k$ real | $B=\lvert\vec a\rvert$: eigenvalues $i\bigl(\frac{E}{c}\pm\lvert\vec p\rvert\bigr)$ |

The two physical sectors give the two familiar realities. On $\mathbb{B}_\Psi$ the spectrum is real because $B$ is purely imaginary; on $\mathbb{B}_\Phi$ the spectrum is purely imaginary because $B$ is real. Neither sentence uses a matrix and neither uses a Hermiticity axiom: each is the sign of a sum of three squares in a real basis.

The physical reading is that "real energies" and "imaginary frequencies" are one computation. The Hermitian element has real outcomes and a complex frequency; the material element has an imaginary frequency and a real, indefinite norm. The two are not two postulates but two signs of the same expression.

The boundary. The sign table is a table of real bases; an element that is neither Hermitian nor anti-Hermitian has a complex $B$ and a genuinely complex pair, and no reality statement applies to it.

### I.5.c — The Spectrum Is Frame-Blind, and the Frame Is What It Does Not See

Read: the spectrum has two complex numbers and the element has eight real parameters. It fixes the trace and the norm and nothing else.

$$
\lambda_++\lambda_-=2Q_t,\qquad \lambda_+\lambda_-=Q_t^2+B^2 ,
$$

and the axis $\vec Z$ carries two free complex angles, four real parameters, on which the two eigenvalues are silent.

The similarity theorem is the sharp form of the blindness. Off the cone the similarity class is the unordered spectrum, so the spectrum is a complete invariant of the element up to a change of frame, and an incomplete invariant of the element. A measurement that reads the spectrum therefore determines the element up to conjugation and no further.

The physical reading is that a spectral measurement reads the rates and leaves the frame free. For a four-momentum the family at fixed spectrum is the two-sphere of directions at fixed energy and momentum magnitude; for a two-level system it is the sphere of Bloch directions at fixed gap. The spectrum is a frame-blind observable, and the axis is the frame.

The boundary. *Not fixed* is not *not constrained*. The spectrum constrains the element to a quadric and, for a four-momentum, to a sphere. And a measurement that resolves the idempotents as well is a different measurement: it reads the frame as well as the rates.

### I.5.d — The Eigenbasis Belongs to the Direction, Not to the Element

Read: $\tilde Q'=a\tilde Q+be_t$ has the same root, the same idempotents and the same eigenbasis; only the eigenvalues change, affinely.

$$
\vec Z'=\vec Z,\qquad \mathcal{B}(\tilde Q')=\mathcal{B}(\tilde Q),\qquad \lambda_\pm'=a\lambda_\pm+b .
$$

So the eigenbasis is a function on the projective space of the vector part, minus the conic. The element projects to $[\vec Q]$, the fibre of the projection is the affine line $\{a\tilde Q+be_t\}$, and on that fibre the basis is constant while the spectrum is affine.

The worked cases are the demonstration. Cases 2 to 5 have one direction, one root $\vec Z=-i\vec e_x$, one pair of idempotents, one eigenbasis, and four different spectra: imaginary, diagonal-complex, real, and generic-complex. Scaling the element and shifting its scalar part moved the diagonal and left the frame alone.

The physical reading is that a frame of modes is a frame. A change of amplitude and of zero does not change the normal modes; a change of axis does. The eigenbasis is the frame in which the element is diagonal, and the frame is attached to the direction the element points in.

The boundary. The basis is equivariant under inner automorphisms only up to the reciprocal rescaling of $\vec\Upsilon_\pm$, because the auxiliary vector that fixes the normalisation is fixed in the frame and is not invariant. The construction is covariant, its representative is not.

### I.5.e — Two Eigenvalues Are Two Modes of One Element, Not Two Particles

Read: each eigenvalue has multiplicity two on the algebra, because each eigenspace is a right ideal of complex dimension two. The spectrum is two numbers repeated, and the element is one object.

$$
\ker(L_{\tilde Q}-\lambda_\pm)=\tilde\Pi_\pm\mathbb{B},\qquad \dim_{\mathbb{C}}=2,\qquad
L_{\tilde Q}\ \text{has eigenvalues}\ (\lambda_+,\lambda_+,\lambda_-,\lambda_-) .
$$

**The arithmetic of a sum rules out a particle count.** In the lightlike decomposition of a four-momentum the two coefficients add to twice the energy, not to the energy, and the two terms are imaginary multiples of idempotents, so neither is a positive-energy state. The element carries one mass-shell condition, not two.

The physical reading is that a two-term spectral writing is a decomposition of one object. A second particle would need a second independent element, a tensor product, and a second mass-shell condition; the spectral writing supplies none of them.

The boundary. The two terms are the two lightlike components of one momentum, and the reading is licensed for the material sector. In the informational sector the same two numbers are two outcomes, and the multiplicity two is then the degeneracy of the measurement and not a pair of systems.

### I.5.f — The Diagonal Is the Rate and the Mixed Corner Is the Shear, and on the Cone the Clock Stops

Read: in the adapted frame the semisimple part occupies the two diagonal corners and the nilpotent part a single mixed corner. The diagonal acts as a rate; the mixed corner acts as a shift with no rate of its own.

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-+\vec\Upsilon\quad(\vec\Upsilon=0\ \text{off the cone}),\qquad
\tilde Q\tilde\Pi_-=Q_t\tilde\Pi_-+\vec\Upsilon_- .
$$

On the cone the exponential is polynomial.

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\bigl(e_t+\theta\vec Q\bigr),
$$

so there is no oscillation, no frequency and no periodic term. The root-parametrised form $\cos(B\theta)e_t+\sin(B\theta)\rho$ does not extend to $B=0$, because $\rho=\vec Q/B$ does not exist; only the entire function in $B$ does.

The physical reading is a rate with a shear, and at the limit a rate with no clock. The unipotent stratum is a reversible process with a defective mode; the nilpotent stratum is a pure shift with no rate at all. The two are the two halves of the cone, separated by the scalar part.

The boundary. The truncated exponential is exact on the cone and is not a limit of oscillating forms in a root; the boundary is a change of functional form, not a degeneration of a formula.

### I.5.g — The Centraliser Is What No Frame Can Change

Read: the centraliser is $\mathbb{C}[\tilde Q]$ off the centre, of complex dimension two, and it is $\mathbb{C}\times\mathbb{C}$ or the dual numbers according to the discriminant.

$$
C(\tilde Q)=\mathbb{C}[\tilde Q]\cong
\begin{cases}\mathbb{C}\times\mathbb{C},&B^2\neq0,\\ \mathbb{C}[\varepsilon]/(\varepsilon^2),&B^2=0,\ \vec Q\neq0 .\end{cases}
$$

The dimension is the statement. Two complex dimensions means that the only elements that commute with a non-central element are $e_t$ and the element itself: there is no other invariant of the element, and no larger algebra attached to it.

The physical reading is a statement about what can be known together. Commuting with an element is what makes a second quantity a function of the first, so the centraliser is the set of quantities that the element does not disturb. Off the cone it is a pair of scalars — the two eigenvalues, or equivalently the trace and the norm; on the cone it is a scalar and a nilpotent, which is one number and one direction, and there is no second independent invariant.

The sharp case is the centre. For $\tilde Q=Q_te_t$ the centraliser is the whole algebra but the double centraliser collapses to $\mathbb{C}e_t$: a central element carries no information, and the only thing that commutes with everything is the centre.

The boundary. *Commuting* is not *simultaneously measurable* in general. Off the cone the centraliser is a product of two fields, and the two spectral idempotents diagonalise it; on the cone it is the dual numbers, which have no non-trivial idempotents, so the two quantities cannot be separated by a projection.

### I.5.h — The Two Outcomes Exist, and They Are Not Projectors

Read: the spectral idempotents $\tilde\Pi_\pm$ are unique, orthogonal and complete, and they are the Lagrange idempotents of the element. They are idempotents, not Hermitian projectors.

$$
\tilde\Pi_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},\qquad \tilde\Pi_+^{2}=\tilde\Pi_+,\qquad \tilde\Pi_+\tilde\Pi_-=0,\qquad \tilde\Pi_++\tilde\Pi_-=e_t .
$$

The two properties are different. A Hermitian idempotent satisfies $\tilde\Pi^{*}=\tilde\Pi$; the spectral idempotent of a non-normal element does not, and the two spectral idempotents are then not orthogonal in the Hilbert form:

$$
\operatorname{Sc}\bigl(\tilde\Pi_+^{*}\tilde\Pi_-\bigr)\neq0\quad\text{unless}\ \tilde Q\ \text{is normal}.
$$

The Petermann factor measures the failure.

$$
\kappa=\operatorname{tr}\bigl(P_\pm^{\dagger}P_\pm\bigr)=\frac{(r^{\dagger}r)(\ell^{\dagger}\ell)}{\lvert\ell^{\dagger}r\rvert^{2}}\ge1,
$$

with equality exactly in the normal case.

The physical reading is a measurement with two outcomes and a metric that depends on the observable. The outcome pair and the projectors exist for every element off the cone; what fails for a non-normal element is orthogonality, so the probability rule needs a second basis and a metric built from it, and that metric changes when the observable changes. The Born rule is the normal case of that rule, not the general one.

The boundary. The biorthogonal rule is a rule per observable, not a replacement for a Hilbert space: two observables give two inner products on the same space, and no state has an element-independent norm.

### I.5.i — The Spectrum Is Copy-Blind, So Chirality Is Not a Spectral Label

Read: left multiplication by $\tilde Q$ acts on each spinor space with the same two eigenvalues, while right multiplication is scalar on each.

$$
L_{\tilde Q}\big|_{S_+}=\operatorname{diag}(\lambda_+,\lambda_-),\qquad L_{\tilde Q}\big|_{S_-}=\operatorname{diag}(\lambda_+,\lambda_-),\qquad
\zeta_+\tilde Q=\lambda_+\zeta_+,\qquad \zeta_-\tilde Q=\lambda_-\zeta_- .
$$

So the two gradings coexist and are not the same grading.

$$
\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B}\ \ (\text{eigenspaces of }L_{\tilde Q}),\qquad
\mathbb{B}=S_+\oplus S_-\ \ (\text{eigenspaces of }R_{\tilde Q}),\qquad
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\cap S_t .
$$

The physical reading is that the Peirce index is a right eigenvalue. Which column a component sits in is the eigenvalue of a right multiplication; which frequency it carries is the eigenvalue of a left multiplication. A chirality label is of the first kind and an energy label of the second, and each column of a Dirac spinor holds both frequencies.

**The consequence is a prohibition.** No spectral reading can produce a chirality, because the spectrum is copy-blind: knowing the frequency of a component says nothing about its copy, and knowing the copy says nothing about the frequency of the components inside it.

The boundary. The two spinor spaces are isomorphic as left modules and distinct as subspaces, so the copy index is a property of the embedding and not of the module. The reading is therefore about the matrix model of the element, not about an invariant of the category.

### I.5.j — Degeneracy Is Not Non-Invertibility

Read: on the cone the determinant is $Q_t^2$, so the cone contains units and the scalar part cuts it in two.

$$
\mathcal S=\Sigma_{10}\sqcup\Sigma_{00},\qquad \Sigma_{10}=\{Q_t\neq0\},\qquad \Sigma_{00}=\{Q_t=0\},\qquad \langle\tilde Q\rangle_{\natural}=Q_t^2\ \text{on}\ \mathcal S .
$$

The four sectors of the two conditions make the independence explicit.

| sector | $\langle\cdot\rangle_{\natural}$ | $B^2$ | description |
| --- | --- | --- | --- |
| $\Sigma_{11}$ | $\neq0$ | $\neq0$ | the generic unit, distinct non-zero eigenvalues |
| $\Sigma_{10}$ | $\neq0$ | $=0$ | the unit of the cone: scalar line and unipotents |
| $\Sigma_{01}$ | $=0$ | $\neq0$ | a zero divisor with distinct eigenvalues, one of them zero |
| $\Sigma_{00}$ | $=0$ | $=0$ | the nilpotents, with the origin |

The physical reading is that reversibility and a mode basis are independent. The generic element has both; a massless element has a mode basis without being invertible; a unipotent element is invertible without a mode basis; a nilpotent has neither. The mass is a norm condition, the mode basis is a spectral condition, and no one of them implies the other.

The boundary. The identification of $\Sigma_{01}$ with *massless* is a material-sector dictionary and not an algebraic theorem; the algebra states $Q_t^2+B^2=0$, and the physical word for that is supplied by the sector.

### I.5.k — The Hermitian Sector Admits Only Diabolic Degeneracies

Read: on $\mathbb{B}_\Psi$ the restriction of $B^2$ is $-(a_x^2+a_y^2+a_z^2)$ with real $a_k$, so $B^2=0$ forces $\vec Q=0$. The Hermitian sector meets the cone only on the scalar line.

The two degeneracies are therefore different normal forms, and only one of them is available to a Hermitian element.

| question | diabolic | exceptional |
| --- | --- | --- |
| condition | $\vec Q=0$ | $B^2=0$, $\vec Q\neq0$ |
| minimal polynomial | $X-Q_t$ | $(X-Q_t)^2$ |
| eigenvectors | every vector | one, up to scale |
| spectral idempotents | every complete pair | none |
| centraliser | all of $\mathbb{B}$ | $\mathbb{C}[\tilde Q]$, the dual numbers |
| response to a linear perturbation | linear | square root |

The square-root law is the observable mark.

$$
B(\epsilon)=\sqrt{2\epsilon(\vec Q_0,\vec Q_1)}\,\bigl(1+O(\epsilon)\bigr),\qquad \lambda_\pm(\epsilon)=Q_t(\epsilon)\pm iB(\epsilon),
$$

so a linear perturbation of the parameter produces a square-root response, because the two eigenvalues are the two branches of one square root.

The physical reading is a theorem about where exceptional points can occur. A degeneracy that keeps the algebra semisimple is a coincidence of two eigenvalues with the states still independent; a degeneracy that destroys the projections is a coalescence of the states themselves. The first is the Hermitian case, the second needs a non-Hermitian element, and the reason is a sign in a sum of three squares.

The boundary. The $\sqrt{\epsilon}$ law is generic for a family, not universal: the coefficient depends on the direction, and a direction orthogonal to $\vec Q_0$ gives a higher order. The algebra supplies the normal form at the point, not the family.

### I.5.l — A Real Spectrum Is Not a Stable System

Read: case 4 of the worked examples is $\sqrt2 e_t+i\vec e_x$, with $B=i$ and eigenvalues $\sqrt2-1$ and $\sqrt2+1$. The root is $\vec Z=-i\vec e_x$, an imaginary root, and the spectrum is real.

The lesson is that reality of the eigenvalues is a statement about oscillation, not about stability. A real $\lambda$ in the convention $e^{-i\lambda t}$ gives a pure exponential and no oscillation; a complex $\lambda$ gives an oscillation modulated by a rate. Which of the two is stable is decided by the sign of the real part of $\lambda$, that is by $\operatorname{Re}Q_t$ together with the imaginary part of $B$, and not by the reality of the pair.

The same element shows that the root need not be real. $\vec Z$ is a square root of $e_t$ in the algebra, and it can be imaginary, real or complex; the branch is a convention and the two branches exchange the two eigenvalues.

The physical reading is that a purely exponential mode is a rate and not a non-physical solution. A pair of real eigenvalues is a pair of amplification and attenuation factors; a pair of imaginary eigenvalues is a pair of oscillations. Both are physical, and the corpus's use of imaginary frequencies for propagation and real ones for damping is the same distinction read in the two sectors.

The boundary. The reading depends on the evolution convention and on the sector. In the material sector the eigenvalues are imaginary for a real four-momentum, and the word *real spectrum* would describe the informational sector instead.

## The Limits

The frequency reading is a convention. Every statement about oscillation, damping and growth depends on whether the evolution is written $e^{-i\lambda t}$ or $e^{+i\lambda t}$, and the algebra fixes neither. The entry states the algebra and names the convention when it uses one.

The identification of the spectrum with a physical quantity is a sector dictionary. On $\mathbb{B}_\Phi$ the pair is a Doppler pair; on $\mathbb{B}_\Psi$ it is an outcome pair. The algebra supplies the same two numbers in both cases, and the entry does not claim that a spectral measurement of an arbitrary element has a physical meaning.

**The eigenbasis exists only off the cone.** Every statement about the modes, the projectors and the diagonal basis is a statement on $\{B^2\neq0\}$, which is open and dense and therefore generic, but which excludes exactly the loci the physics cares about: rest frames, null fields, and exceptional points.

The normalisation is not canonical. The pair $\vec\Upsilon_\pm$ is fixed only up to a reciprocal rescaling, and the two normalisations offered by the mathematics — the transverse vector and the antisymmetric part — are different choices of representative. Nothing in the entry depends on which is used, but a numerical claim about a component does.

The Jordan frame is chosen. On the cone the two idempotents that split the flag are not determined by the element; the definite Hermitian form selects one pair, which is a choice of a metric and not a consequence of the algebra.

## Summary

- The spectrum is $\lambda_\pm=Q_t\pm iB$ with $B^2=Q_x^2+Q_y^2+Q_z^2$, and the discriminant of the characteristic polynomial is $-4B^2$.
- An eigenvalue is a scalar for which $\tilde Q-\lambda e_t$ is not invertible; the criterion needs no module and no matrix.
- $B^2\neq0$ is equivalent to distinct eigenvalues, semisimplicity and diagonalisability; $B^2=0$ is the spectral-degenerate cone.
- The characteristic polynomial has two coefficients and the minimal polynomial separates the four types; two pairs of types share a characteristic polynomial.
- Off the cone the root $\vec Z=-i\vec Q/B$ exists, the spectral idempotents are the Lagrange idempotents, and each eigenspace is a right ideal of complex dimension two.
- The eigenbasis is one vector in each of the four Peirce corners, and both the left and the right actions are diagonal in it.
- The eigenbasis is attached to the direction of the vector part: scaling the element and shifting its scalar part leave the basis unchanged and move the spectrum affinely.
- The centraliser is $\mathbb{C}[\tilde Q]$ off the centre, of dimension two, and is $\mathbb{C}\times\mathbb{C}$ or the dual numbers according to the discriminant.
- The semisimple–nilpotent split is unique, and in an adapted frame it is a corner pattern with the nilpotent part in a single mixed corner of index two.
- On the cone the determinant is $Q_t^2$, the eigenvalues have coalesced, no eigenbasis exists, and the exponential is polynomial with no frequency.
- Off the cone the spectrum determines the similarity class; on the cone it carries no information beyond the scalar part.
- The two eigenvalues are two modes of one element, with multiplicity two, not two particles.
- The spectrum is frame-blind; the frame is what it does not see, and the axis is the frame.
- The Hermitian sector meets the cone only on the scalar line, so it admits diabolic degeneracies and not exceptional ones.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $Q_t$, $\vec Q$ | scalar and vector parts of $\tilde Q$ |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | square of the vector part; $B^2=-\vec Q^2$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\vec Z=-i\vec Q/B$ | the root, a pure square root of $e_t$ off the cone |
| $\tilde\Pi_\pm=\frac12(e_t\pm\vec Z)$ | the spectral idempotents |
| $\vec\Upsilon_\pm$ | the two nilpotents of the eigenbasis, in the mixed corners |
| $\mathcal{B}(\tilde Q)$ | the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ |
| $\mathcal{J}(\tilde Q)$ | the Jordan basis $(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$ |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathcal S^{\mathrm{s}},\mathcal S^{\mathrm{n}},\mathcal S^{\mathrm{u}}$ | the scalar, nilpotent and unipotent strata |
| $\Sigma_{11},\Sigma_{10},\Sigma_{01},\Sigma_{00}$ | the four sectors of $(\langle\cdot\rangle_{\natural},B^2)$ |
| $C(\tilde Q)$ | the centraliser |
| $\tilde Q_s$, $\vec\Upsilon$ | the semisimple and nilpotent parts |
| $J_2(Q_t)$ | the Jordan block $\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}$ |
| $\kappa$ | the Petermann factor |

## Further Reading

In the mathematics corpus. The six articles of the source table, and inside them *The Spectral Criterion*, which states the eigenvalue problem without a module, and *The Three Strata*, which is the normal-form table of the cone.

In this category. *The Modules: What the Algebra Acts On* supplies the right ideals that are the eigenspaces and the two spinor spaces that are the columns. *The Four Forms and the Four Norms* supplies the norm whose vanishing is the cone $\Sigma_{01}$ and the positivity the cone lacks. *The H Norm* and *The N Norm* carry the two conditions that the sector table keeps apart.

The sources of this entry. [Exceptional Points and the Nilpotent Regime in the Biquaternion Spectrum](exceptional-points-and-the-nilpotent-regime-in-the-biquaternion-spectrum.html) is the diabolic–exceptional table and the square-root law. [Four-Vectors and the Interval](four-vectors-and-the-interval.html) is the Doppler pair and the warning that two eigenvalues are not two particles. [The Group of Invertibles, the Cone and the Orders](the-group-of-invertibles-the-cone-and-the-orders.html) is the independence of the cone from invertibility. [Biorthogonal Quantum Mechanics and the Biquaternion Spectrum](biorthogonal-quantum-mechanics-and-the-biquaternion-spectrum.html) treats the non-Hermitian projectors and the Petermann factor. The gap, the three rates and the degenerate strata are stated here.
