# __The Norm-Regular, Spectrally Regular Sector__

## Introduction

This is cell $11$ of the four-sector arrangement of the two quadratic conditions

$$
N(\tilde Q)=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

the sector on which neither vanishes. It is the complement of the union of the two cones,

$$
\Sigma_{11}=\mathbb{B}\setminus(\mathcal N\cup\mathcal S),
$$

and it is the **generic** sector: the open dense cell in which both problems of the arrangement receive the positive answer. The other three cells are the mixed sectors $\Sigma_{01}=\mathcal N\setminus\mathcal S$ and $\Sigma_{10}=\mathcal S\setminus\mathcal N$, and the doubly degenerate cell $\Sigma_{00}=\mathcal N\cap\mathcal S$, treated in *The Norm-Degenerate, Spectrally Regular Sector*, *The Norm-Regular, Spectrally Degenerate Sector* and *The Norm-Degenerate, Spectrally Degenerate Sector*. The vocabulary, the two cones and the naming convention are those of *Norm Regularity and Degeneracy in the Biquaternion Algebra* and *Spectral Regularity and Degeneracy in the Biquaternion Algebra*.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and $\tilde Q=Q_te_t+\vec Q$; the conjugation is ${}^{\natural}$; the reduced norm is $N(\tilde Q)=\tilde Q^{\natural}\tilde Q$, central; and the product is the plain product unless stated otherwise. The null cone is $\mathcal N=\{N=0\}$; the spectral-degenerate cone is $\mathcal S=\{B^2=0\}$; **regular** means non-zero: $N\neq0$ for the norm, $B^2\neq0$ for the spectrum.

## Definition and Characterisation

**Definition.** The sector $\Sigma_{11}$ is

$$
\Sigma_{11}=\{N\neq0,\ B^2\neq0\}.
$$

**Theorem (five descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\tilde Q\in\Sigma_{11}$;

(ii) $\tilde Q$ is a unit and its two eigenvalues are distinct;

(iii) $\tilde Q$ is a unit and is semisimple with a non-scalar spectrum;

(iv) $\tilde Q$ admits a spectral decomposition into two non-trivial idempotents with distinct non-zero coefficients;

(v) $\tilde Q$ is invertible, non-scalar, and admits an adapted Peirce decomposition.

*Proof.* (i) $\iff$ (ii): $N\neq0$ is the unit condition, and $B^2\neq0$ is the discriminant condition, so the eigenvalues $\lambda_\pm=Q_t\pm\beta$, with $\beta^2=-B^2$ and $\beta\neq0$, are distinct; conversely distinct eigenvalues give $B^2\neq0$ and $N=\lambda_+\lambda_-\neq0$ makes the element a unit.

(ii) $\iff$ (iii): in two dimensions a semisimple element with a repeated eigenvalue is a scalar, so semisimplicity with a non-scalar spectrum is the same as two distinct eigenvalues.

(ii) $\iff$ (iv): with distinct eigenvalues the spectral idempotents $e_\pm$ exist, are non-trivial, and are unique; the coefficients $\lambda_\pm$ are distinct and non-zero because $N=\lambda_+\lambda_-\neq0$. Conversely such a decomposition exhibits two distinct eigenvalues and a non-zero norm.

(i) $\iff$ (v): for a non-scalar element an adapted Peirce decomposition exists exactly when $B^2\neq0$, by the existence theorem of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; invertibility is exactly $N\neq0$. So both conditions together are exactly (i).

**Corollary (regular semisimple units).** The sector is the set of regular semisimple elements of the unit group:

$$
\Sigma_{11}=\{\tilde Q\in\mathbb{B}^\times\ :\ \lambda_+\neq\lambda_-\},
$$

with $\mathbb{B}^\times=\{N\neq0\}$ the unit group. Its complement in $\mathbb{B}^\times$ is the degenerate half $\Sigma_{10}$, so the unit group splits into a generic part and a unipotent part.

**Corollary (eigenvalue parametrisation).** Every element of the sector is written uniquely as

$$
\tilde Q=\lambda_+e_++\lambda_-e_-,\qquad
\lambda_\pm\in\mathbb{C}^\times,\quad \lambda_+\neq\lambda_-,
$$

with $e_\pm$ the spectral idempotents, $e_+^2=e_+$, $e_-^2=e_-$, $e_+e_-=0$, $e_++e_-=e_t$. Conversely every such choice gives an element of $\Sigma_{11}$. In these terms

$$
Q_t=\frac{\lambda_++\lambda_-}{2},\qquad
B^2=-\left(\frac{\lambda_+-\lambda_-}{2}\right)^2,\qquad
N=\lambda_+\lambda_-.
$$

The two invariants are therefore the two elementary symmetric functions of the spectrum: $N$ is the product, and $B^2$ is minus a quarter of the squared difference.

**Corollary (complement of a hypersurface).** $\Sigma_{11}$ is the complement of the hypersurface $N\,B^2=0$, the union of the two cones. It is Zariski-open and dense in $\mathbb{B}$.

## Geometry

**Theorem (open dense, of full measure).** $\Sigma_{11}$ is open and dense in $\mathbb{B}$, of complex dimension $4$ and real dimension $8$. Its complement $\mathcal N\cup\mathcal S$ is a complex hypersurface, of complex dimension $3$ and real dimension $6$, hence of real codimension $2$ and Lebesgue measure zero.

*Proof.* The functions $N$ and $B^2$ are non-zero polynomials in four complex variables, so each zero locus is a complex hypersurface, and so is their union; the complement is open and dense. The dimension of the complement is $4-1=3$ over $\mathbb{C}$, that of the sector $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$. A complex hypersurface in $\mathbb{C}^4$ has real codimension $2$ and measure zero.

**Proposition (connected).** $\Sigma_{11}$ is connected.

*Proof.* By the eigenvalue parametrisation, $\Sigma_{11}$ is the image of the connected parameter space

$$
\{(\lambda_+,\lambda_-,e_+):\ \lambda_\pm\neq0,\ \lambda_+\neq\lambda_-,\ e_+\text{ a non-trivial idempotent}\}
$$

under the continuous map $(\lambda_+,\lambda_-,e_+)\mapsto\lambda_+e_++\lambda_-e_-$. The eigenvalue parameter space is $\mathbb{C}^2$ minus the diagonal and the two axes, three complex lines through the origin, and its complement is connected. The non-trivial idempotents are $e_+=(e_t+\tilde\Xi)/2$ with $\tilde\Xi^2=e_t$ and $\tilde\Xi\neq\pm e_t$; the quadric $\tilde\Xi^2=e_t$ is a smooth connected complex surface, and deleting the two points $\pm e_t$ leaves it connected. A continuous image of a connected space is connected.

**Proposition (not simply connected).** $\Sigma_{11}$ has non-trivial fundamental group.

*Proof.* For $\varepsilon\neq0$ consider the loop

$$
\tilde Q(t)=e_t+\varepsilon e^{2\pi it}\vec e_x,\qquad 0\le t\le1.
$$

Its invariants are

$$
N(\tilde Q(t))=1+\varepsilon^2e^{4\pi it},\qquad B^2(\tilde Q(t))=\varepsilon^2e^{4\pi it},
$$

both non-zero, so the loop lies in $\Sigma_{11}$. The continuous map $\tilde Q\mapsto(N(\tilde Q),B^2(\tilde Q))$ sends $\Sigma_{11}$ to $\mathbb{C}^\times\times\mathbb{C}^\times$ and sends this loop to one whose two components wind twice around $1$ and around $0$ respectively. That image is not null-homotopic in the torus, so the loop is not null-homotopic in $\Sigma_{11}$.

**Remark (the identity is not generic).** $e_t$ has $B^2=0$, so it lies in $\Sigma_{10}$, not in $\Sigma_{11}$. The sector is not a neighbourhood of the identity and not a subgroup; it is the part of the unit group on which the discriminant does not vanish. Likewise the scalar line $\mathbb{C}^\times e_t$ is entirely outside the sector.

**Remark (where $Q_t$ may vanish).** The sector meets the hyperplane $Q_t=0$: the pure vectors with $B^2\neq0$, such as $\vec e_x+\vec e_y$, have $N=B^2\neq0$ and lie in $\Sigma_{11}$. For such an element the two eigenvalues are opposite, $\lambda_-=-\lambda_+$, and its square is a non-zero scalar. So the sector is not characterised by a non-zero scalar part, only by the non-vanishing of both invariants.

## The Elements

Let $\tilde Q\in\Sigma_{11}$, with $\beta^2=-B^2$, $\beta\neq0$, and eigenvalues $\lambda_\pm=Q_t\pm\beta$. The choice of $\beta$ is the choice of square root, $\beta=\pm i\sqrt{B^2}$; it only exchanges the two eigenvalues.

**Spectrum and minimal polynomial.** The spectrum is $\{\lambda_+,\lambda_-\}$, with $\lambda_+\neq\lambda_-$ and $\lambda_+\lambda_-=N\neq0$. The characteristic and minimal polynomial is

$$
p(X)=X^2-2Q_tX+N,
$$

squarefree, with discriminant $-4B^2\neq0$. The element is semisimple, and regular semisimple: its centraliser has the minimal possible dimension among non-scalar elements.

**Centraliser.** Evaluation gives

$$
\mathbb{C}[\tilde Q]\cong\mathbb{C}[X]/(p)\cong\mathbb{C}\oplus\mathbb{C},
$$

of complex dimension $2$. Under the isomorphism $\mathbb{C}[\tilde Q]\cong\mathbb{C}\oplus\mathbb{C}$ the idempotents correspond to $(0,0)$, $(1,0)$, $(0,1)$ and $(1,1)$, so they are exactly $0$, $e_+$, $e_-$ and $e_t$.

**Spectral idempotents.** They are unique and given by the Lagrange formula

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},
$$

with $e_\pm^2=e_\pm$, $e_+e_-=0$, $e_++e_-=e_t$, $\tilde Qe_\pm=\lambda_\pm e_\pm$. Each is a non-trivial idempotent, since $\lambda_+\neq\lambda_-$ and $\tilde Q$ is not a scalar.

**Adapted Peirce decomposition.** Relative to $(e_+,e_-)$ the Peirce form is diagonal with both diagonal entries non-zero:

$$
e_+\tilde Qe_+=\lambda_+e_+,\qquad
e_+\tilde Qe_-=0,\qquad
e_-\tilde Qe_+=0,\qquad
e_-\tilde Qe_-=\lambda_-e_-.
$$

This is the only sector in which the adapted decomposition has two non-zero coefficients and two non-trivial idempotents. In $\Sigma_{01}$ one coefficient vanishes; on the scalar line of $\Sigma_{10}$ the two coefficients coincide and the refinement is non-unique; in $\Sigma_{10}^{\mathrm{J}}$ and in $\Sigma_{00}$ no adapted decomposition exists.

**Annihilators.** Since $\tilde Q$ is a unit,

$$
A(\tilde Q)=B(\tilde Q)=\{0\},
$$

and left and right multiplication are bijections of $\mathbb{B}\cong\mathbb{C}^4$, of complex rank $4$.

**Inverse.** $\tilde Q^{-1}=\tilde Q^{\natural}/N$, and

$$
N(\tilde Q^{-1})=\frac{1}{N(\tilde Q)},\qquad
B^2(\tilde Q^{-1})=\frac{B^2(\tilde Q)}{N(\tilde Q)^2}\neq0,
$$

so the inverse lies in the sector.

## Multiplication and Inversion

**Products stay in the unit group.** The norm is multiplicative, so for $\tilde P,\tilde Q\in\Sigma_{11}$,

$$
N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)\neq0,
$$

and the product lies in $\mathbb{B}^\times=\Sigma_{10}\sqcup\Sigma_{11}$. Both outcomes occur.

**Theorem (both outcomes).**

$$
\Sigma_{11}\cdot\Sigma_{11}\subseteq\Sigma_{10}\cup\Sigma_{11},
$$

and the product of two elements of the sector can lie in $\Sigma_{11}$ and can lie in $\Sigma_{10}$.

*Witnesses.* For the first, $\tilde Q=e_t+\vec e_x$ has $N=2$ and $B^2=1$, and

$$
\tilde Q^2=e_t+2\vec e_x+\vec e_x^2=2\vec e_x,
$$

with $N=4$ and $B^2=4$: it stays in the sector. For the second, $\tilde P=e_t+2\vec e_x$ and $\tilde Q=e_t-2\vec e_x$ both have $N=5$ and $B^2=4$, and

$$
\tilde P\tilde Q=e_t-4\vec e_x^2=5e_t,
$$

with $B^2=0$ and $N=25$: the product lies on the scalar line, in $\Sigma_{10}^{\mathrm{s}}$.

**Squares.** The square of an element of the sector has eigenvalues $\lambda_+^2,\lambda_-^2$ and

$$
B^2(\tilde Q^2)=4Q_t^2B^2(\tilde Q).
$$

Hence

$$
\tilde Q^2\in\Sigma_{11}\ \text{if }Q_t\neq0,\qquad
\tilde Q^2=-B^2(\tilde Q)\,e_t\in\Sigma_{10}^{\mathrm{s}}\ \text{if }Q_t=0.
$$

The second case is exactly $\lambda_-=-\lambda_+$; the pure vector $\vec e_x+\vec e_y$ is the standard witness,

$$
(\vec e_x+\vec e_y)^2=-2e_t.
$$

So squaring can leave the sector, and it leaves it precisely through the vertex of the spectral cone.

**Inversion and closure.** The sector is inverse-closed, because $N(\tilde Q^{-1})\neq0$ and $B^2(\tilde Q^{-1})\neq0$; it is not product-closed, by the theorem. It is therefore a **symmetric subset** of the unit group, not a subgroup. In fact it contains no subgroup at all, since every subgroup contains the identity and $e_t\notin\Sigma_{11}$.

**Caveat on the parametrisation.** Although $\lambda_+e_++\lambda_-e_-$ is unique, products do not add eigenvalues: the eigenvalues of $\tilde P\tilde Q$ are not determined by those of $\tilde P$ and $\tilde Q$ separately. Only their product is, through the norm.

## Relation to the Two Cones

**The sector is the complement of both cones.** As point sets,

$$
\Sigma_{11}=\mathbb{B}\setminus(\mathcal N\cup\mathcal S),\qquad
\mathbb{B}=\Sigma_{11}\sqcup\Sigma_{01}\sqcup\Sigma_{10}\sqcup\Sigma_{00}.
$$

It is the only cell off both cones, and its closure is all of $\mathbb{B}$.

**The two cones are tangent exactly on the common stratum.** The defining functions satisfy the identity

$$
N-B^2=Q_t^2,
$$

so their gradients,

$$
\nabla N=2(Q_t,\vec Q),\qquad \nabla B^2=2(0,\vec Q),
$$

coincide whenever $Q_t=0$. At a common point of the two cones one has $Q_t=0$ and $B^2=0$, which is $\Sigma_{00}$; there the gradients are both $2(0,\vec Q)$, equal and non-zero off the origin. So the cones are tangent along $\Sigma_{00}\setminus\{0\}$ and both singular at the origin. On $\Sigma_{11}$ there is nothing to be tangent to: the sector is disjoint from both cones.

**The cell where the answers agree.** Every element of the sector is a unit with distinct eigenvalues: both questions — is it invertible, and are its eigenvalues separated — receive the positive answer. This is the fourth corner of the $2\times2$ table and the reason the independence of the two problems is not vacuous: the doubly regular case exists, and it exists on a dense open set.

**Independence, restated.** $\Sigma_{01}$ and $\Sigma_{10}$ show that neither cone contains the other. $\Sigma_{11}$ shows that the two conditions are simultaneously satisfiable, and $\Sigma_{00}$ shows that they are simultaneously violable. The four cells together are the complete truth table of the pair of predicates $(N\neq0,\ B^2\neq0)$.

## Comparison with the Other Three Sectors

| sector | conditions | elements | spectrum | adapted Peirce | product |
|---|---|---|---|---|---|
| **doubly regular** $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | $\lambda_+e_++\lambda_-e_-$ with $\lambda_\pm$ distinct and non-zero | $\{\lambda_+,\lambda_-\}$ | exists, unique; both terms non-zero | stays in $\mathbb{B}^\times$; lands in $\Sigma_{11}$ or $\Sigma_{10}$ |
| **norm-degenerate, spectrally regular** $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | $c\tilde\Pi$, $\tilde\Pi$ a non-trivial idempotent | $\{c,0\}$ | exists, unique; one term vanishes | stays on $\mathcal N$; all three outcomes |
| **norm-regular, spectrally degenerate** $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | $Q_tu$, $u$ unipotent | $\{Q_t\}$, repeated | fails on $\Sigma_{10}^{\mathrm{J}}$; one-term and non-unique on $\Sigma_{10}^{\mathrm{s}}$ | stays in $\mathbb{B}^\times$; lands in $\Sigma_{10}$ or $\Sigma_{11}$ |
| **doubly degenerate** $\Sigma_{00}$ | $N=0$, $B^2=0$ | non-zero nilpotents of index two, plus the origin | $\{0\}$ | fails off the origin | $0$ or $\Sigma_{01}$ |

The four cells are exhaustive and disjoint. $\Sigma_{11}$ is the unique cell in which both predicates hold, $\Sigma_{00}$ the unique cell in which both fail, and the two mixed cells are the remaining two rows of the truth table.

**Position in the five-zone refinement.** The five zones of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Five Zones*, are the distinct, zero-divisor, scalar, Jordan and nilpotent zones.

| zone | condition | sector |
|---|---|---|
| **distinct** | $B^2\neq0$, $N\neq0$ | $\Sigma_{11}$ |
| **zero divisor** | $B^2\neq0$, $N=0$ | $\Sigma_{01}$ |
| **scalar** | $\vec Q=0$ | $\Sigma_{10}^{\mathrm{s}}\cup\{0\}$ |
| **Jordan** | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\Sigma_{10}^{\mathrm{J}}$ |
| **nilpotent** | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\Sigma_{00}\setminus\{0\}$ |

Sector $11$ is exactly the **distinct zone**. The refinement of the five zones touches only the other cells: it splits $\Sigma_{10}$ and moves the origin out of the nilpotent zone into the scalar one. On this sector the two classifications coincide, because the sector is homogeneous: every element has two distinct non-zero eigenvalues and a unique adapted Peirce decomposition.

## Consequences

**Eigenbasis.** It exists, it is unique, and it is the genuine two-term spectral decomposition

$$
\tilde Q=\lambda_+e_++\lambda_-e_-,\qquad
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}.
$$

Both eigenvalues are non-zero and distinct, both idempotents are non-trivial, and the decomposition is unique. This is the only sector in which all four of these hold at once.

**Polar decomposition.** It exists and is finite: the modulus $\Rho=\sqrt{N(\tilde Q)}=\sqrt{\lambda_+\lambda_-}\neq0$, so the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Biquaternions* applies. The sector is the only one in which the polar word and the spectral decomposition are simultaneously available: in $\Sigma_{01}$ the polar word fails while the spectral decomposition survives, and in $\Sigma_{10}$ the spectral decomposition fails while the polar word survives.

**One-sided operators.** $L_{\tilde Q}$ and $R_{\tilde Q}$ are bijections of complex rank $4$ with zero kernel, and both annihilators vanish. Together with the eigenbasis, this is the full non-degenerate package.

**The generic case.** Every statement proved for a generic element of $\mathbb{B}$ — invertible, semisimple, with distinct eigenvalues, unique eigenprojectors and a finite polar word — holds on $\Sigma_{11}$ and fails somewhere on its complement. The sector has full measure, and its complement is the arrangement of the two cones.

## Summary

| question | answer |
|---|---|
| definition | $\Sigma_{11}=\{N\neq0,\ B^2\neq0\}$ |
| descriptions | $\mathbb{B}\setminus(\mathcal N\cup\mathcal S)$; a unit with distinct eigenvalues; $\lambda_+e_++\lambda_-e_-$ with $\lambda_\pm$ distinct and non-zero; invertible with a non-trivial adapted Peirce decomposition |
| geometry | open dense, of full measure; complex dimension $4$ and real dimension $8$; connected; complement the hypersurface $NB^2=0$ |
| elements | regular semisimple units; minimal polynomial $X^2-2Q_tX+N$, squarefree; centraliser $\mathbb{C}\oplus\mathbb{C}$ |
| adapted Peirce | exists, unique, both coefficients non-zero |
| annihilators | both zero; left and right multiplication bijective |
| inversion | closed: $\tilde Q^{-1}\in\Sigma_{11}$ |
| multiplication | $\Sigma_{11}\cdot\Sigma_{11}\subseteq\Sigma_{10}\cup\Sigma_{11}$, with both outcomes; not product-closed |
| squares | in $\Sigma_{11}$ when $Q_t\neq0$, on the scalar line when $Q_t=0$ |
| relation to the cones | off both cones; the cones are tangent along $\Sigma_{00}\setminus\{0\}$ |
| place in the arrangement | the distinct zone: the one cell where both answers are positive |

The sector is the generic sector. It is the set of units with distinct non-zero eigenvalues, the complement of the union of the two cones, and the only cell of the arrangement in which both questions — is the element invertible, and can its eigenvalues be told apart — receive the positive answer. It is what the algebra looks like when nothing degenerates. Its complement is the arrangement, and the three other sectors are the three ways the doubly regular case can fail: by losing invertibility, by losing spectral separation, or by losing both.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{ij}$ | the sector with $i=1$ iff $N\neq0$, $j=1$ iff $B^2\neq0$ |
| $\Sigma_{11}$ | the norm-regular, spectrally regular sector, this article |
| $\mathcal N=\{N=0\}$ | the null cone of the reduced norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathbb{B}^\times=\{N\neq0\}$ | the unit group |
| $\lambda_\pm=Q_t\pm\beta$, $\beta^2=-B^2$ | the two eigenvalues |
| $e_\pm$ | the spectral idempotents, unique |
| $\Rho=\sqrt{N}$ | the modulus |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication, both bijective on the sector |

## Further Reading

- [The Norm-Degenerate, Spectrally Degenerate Sector](the-norm-degenerate-spectrally-degenerate-sector.html), for $\Sigma_{00}$, the nilpotents and the origin.
- [The Norm-Degenerate, Spectrally Regular Sector](the-norm-degenerate-spectrally-regular-sector.html), for $\Sigma_{01}$, the scaled idempotents and the zero-divisor zone.
- [The Norm-Regular, Spectrally Degenerate Sector](the-norm-regular-spectrally-degenerate-sector.html), for $\Sigma_{10}$, the unipotents and the Jordan zone.
- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the null cone, its strata and the unit group.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the discriminant, the spectral criterion and the five zones.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the Peirce corners and the minimal ideals.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus $\Rho=\sqrt N$ and the unit factor.
