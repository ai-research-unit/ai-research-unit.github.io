# __Continuity and Limits of the Biquaternion Exponential at the Spectral Cone__

## Introduction

The exponential of a biquaternion is entire, so no point of the spectral-degenerate cone is a singularity of the map. What degenerates at $B^2=0$ is the spectral parametrisation of the exponential: the two eigenvalues coalesce, the element-attached root of $-1$ disappears, the spectral idempotents diverge, and the oscillatory closed form truncates. This article separates three questions that the word *limit* confuses. Which formulas extend continuously? Which spectral objects have limits? Which fail, and at which stratum?

The article assumes the spectral criterion, the cone and its three strata of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; the closed forms and the principal logarithm of *Biquaternion Elementary Functions*; the element-supplied root, the kernel identity and the Hermitian norm of *Relations between the Biquaternion Exponential and the Fourier Kernel*; and the polar factors of *The Polar Decomposition of a N-Regular Biquaternion* and *The Polar Decomposition of a N-Degenerate Biquaternion*. It reproves none of them. It owns the passage to the cone: the entire form of the closed form, the differential and its critical locus, the double pole of the resolvent, the continuity of the Hermitian norm, and the distinction between spectral degeneracy and polar degeneracy. It does not treat the transform theory, which belongs to *Biquaternion Continuous Harmonic Analysis*, nor the physical interpretation, which belongs to the companion article in the physics corpus.

**The result in one table.** The table is the plan of the article.

| object | away from the cone | on the cone | verdict |
|---|---|---|---|
| closed form | root-free, entire | truncated polynomial | **extends** |
| root $\rho=\vec Q/B$ | root of $-1$ | divergent off the scalar stratum | **fails** |
| frequency $B/2\pi$ | non-zero rate | $0$ | **limit exists, no oscillation** |
| eigenvalues $\lambda_\pm$ | distinct | $Q_t$ | **continuous** |
| idempotents $\tilde\Pi_\pm$ | bounded | divergent like $1/B$ | **fail individually** |
| sum $\tilde\Pi_++\tilde\Pi_-$ | $e_t$ | $e_t$ | **survives** |
| two-term decomposition | unique | none off the scalar stratum | **fails** |
| eigenbasis | exists | none off the scalar stratum | **fails** |
| differential $d\exp$ | invertible off $\mathcal R$ | invertible | **survives** |
| resolvent | two simple poles | one double pole on the defective strata | **degenerates** |
| Hermitian norm | closed formula | continuous limit | **survives** |
| principal logarithm | every unit | the units of the cone ($\Sigma_{10}$) | **fails on the nilpotent stratum** |
| two-factor polar | unitary at $N\neq0$ | partial isometry at $N=0$ | **follows the norm** |
| four-factor polar word | every unit | units of the cone | **follows the norm** |
| kernel as a function of the element's root | exists | no root | **fails** |
| kernel at the element's frequency | a value | $e_t-t\vec N$ | **survives as a value** |

The table separates two statements that are often merged. The exponential **follows the discriminant**: its closed form, its differential and its value change regime at $B^2=0$. The polar decomposition **follows the norm**: it changes regime at $N=0$. The spectral cone and the null cone meet only on the nilpotent cone, so the two changes are independent.

## The Cone and Its Strata

**Notation.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$, with

$$
\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad
\vec Q^2=-B^2e_t.
$$

The quaternionic norm is $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$, and $B$ is a fixed square root of $B^2$. The **spectral-degenerate cone** is

$$
\mathcal S=\{B^2=0\}=\{\vec Q^2=0\}=\{\operatorname{disc}p_{\tilde Q}=0\},
$$

the **null cone** is $\mathcal N=\{N=0\}$, and the four **sectors** are

$$
\Sigma_{11}=\{N\neq0,\ B^2\neq0\},\quad
\Sigma_{10}=\{N\neq0,\ B^2=0\},\quad
\Sigma_{01}=\{N=0,\ B^2\neq0\},\quad
\Sigma_{00}=\{N=0,\ B^2=0\}.
$$

The algebra is their disjoint union, and the intersection $\mathcal N\cap\mathcal S=\Sigma_{00}$ is the nilpotent cone.

**The three strata of the cone.** On $\mathcal S$ put

$$
\mathcal S^{\mathrm{s}}=\{\vec Q=0\},\qquad
\mathcal S^{\mathrm{n}}=\{Q_t=0,\ \vec Q\neq0\},\qquad
\mathcal S^{\mathrm{u}}=\{Q_t\neq0,\ \vec Q\neq0\},
$$

the **scalar**, **nilpotent** and **unipotent** strata. The elements of the last two are written $\tilde Q=Q_te_t+\vec N$ with $\vec N=\vec Q$ and $\vec N^2=0$; on the unipotent stratum one also writes $\vec N=Q_t\eta$, with $\eta^2=0$. The classification is that of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Three Strata*.

| stratum | condition | normal form | spectrum | minimal polynomial | unit |
|---|---|---|---|---|---|
| scalar | $\vec Q=0$ | $Q_te_t$ | $\{Q_t\}$ | $X-Q_t$ | iff $Q_t\neq0$ |
| nilpotent | $Q_t=0$, $\vec Q\neq0$ | $\vec N$, $\vec N^2=0$ | $\{0\}$ | $X^2$ | no |
| unipotent | $Q_t\neq0$, $\vec Q\neq0$ | $Q_tu$, $u=e_t+\eta$ | $\{Q_t\}$ | $(X-Q_t)^2$ | yes |

The scalar stratum is the vertex, the whole scalar line. The other two are the **Jordan part** of the cone; they are defective, with a two-dimensional eigenspace and no eigenbasis. The unbounded idempotents of §*The Resolvent and the Double Pole* live on the Jordan part; the vertex is the semisimple part of the cone.

**The four sectors.** The two quadratic conditions are independent, and the sectors record their four combinations. The columns that matter below are the unit criterion and the element-supplied root $\rho=\vec Q/B$.

| sector | $N$ | $B^2$ | unit | root $\rho$ | four-factor polar word |
|---|---|---|---|---|---|
| $\Sigma_{11}$ | $\neq0$ | $\neq0$ | yes | yes | yes |
| $\Sigma_{10}$ | $\neq0$ | $=0$ | yes | no | yes |
| $\Sigma_{01}$ | $=0$ | $\neq0$ | no | yes | no |
| $\Sigma_{00}$ | $=0$ | $=0$ | no | no | no |

The two mixed sectors are the independence witnesses. $\Sigma_{10}$ is a unit with a polar word and no root; $\Sigma_{01}$ is a zero divisor with a root and no polar word. §*Spectral Degeneracy and Polar Degeneracy* returns to this table.

## The Closed Form and Its Limit

**Theorem (the entire closed form).** For every $\tilde Q$ and every complex $\theta$,

$$
\boxed{\ \exp(\theta\tilde Q)=\exp(\theta Q_t)\left(\cos(B\theta)\,e_t+\frac{\sin(B\theta)}{B}\,\vec Q\right)\ }.
$$

The right-hand side is entire in $(Q_t,\vec Q,\theta)$.

*Proof.* For $B^2\neq0$ the identity is the closed form of *Biquaternion Elementary Functions*, §*The Closed Form*. Write $z=B^2$. The two series

$$
\cos(B\theta)=\sum_{n\geq0}\frac{(-1)^nz^n\theta^{2n}}{(2n)!},
\qquad
\frac{\sin(B\theta)}{B}=\sum_{n\geq0}\frac{(-1)^nz^n\theta^{2n+1}}{(2n+1)!}
$$

have infinite radius in $z$, hence define entire functions of $\vec Q$. The right-hand side therefore agrees with the entire left-hand side on the open dense set $B^2\neq0$, and by analytic continuation it agrees everywhere.

**Corollary (the value on the cone).** If $\tilde Q=Q_te_t+\vec N$ with $\vec N^2=0$, then, for every $\theta$,

$$
\boxed{\ \exp(\theta\tilde Q)=\exp(\theta Q_t)\left(e_t+\theta\vec N\right)\ }.
$$

*Proof.* Put $\vec Q=\vec N$ and $B=0$ in the theorem. Equivalently, the exponential series truncates because $\vec N^2=0$.

**Remark (the two forms).** The closed form written as a function of the root,

$$
\exp(\theta\tilde Q)=\exp(\theta Q_t)\left(\cos(B\theta)\,e_t+\sin(B\theta)\,\rho\right),
\qquad
\rho=\frac{\vec Q}{B},
$$

is the one that fails at $B=0$: the root does not exist. The form of the theorem is root-free, and it is the one that extends. The root-parametrised form is a chart; the root-free form is the map.

**Theorem (the limit).** Let $\vec N^2=0$ and let $\vec Q_\epsilon=\vec N+\epsilon\vec V$ with $\epsilon\to0$. Then

$$
\exp(\theta(Q_te_t+\vec Q_\epsilon))
=\exp(\theta Q_t)\left(e_t+\theta\vec N\right)+O(\epsilon),
$$

uniformly for $\theta$ in a compact set. The first-order term in the bracket is $\theta$ times the differential of $\exp$ at $\theta\vec N$, evaluated on $\vec V$.

*Proof.* The right-hand side of the theorem is entire, hence Lipschitz on a compact neighbourhood of $Q_te_t+\vec N$; the difference is $O(\epsilon)$. The identification of the linear term is the definition of the Fréchet derivative.

**Remark (the period at the limit).** Off the cone the oscillatory factor has period $2\pi/B$, because $\exp(2\pi\rho)=e_t$; the full flow is periodic only when the scalar factor matches. As $B\to0$ the period of the oscillation tends to infinity and the oscillatory factor tends to $e_t+\theta\vec N$. This is the precise reading of *no frequency* on the cone: the frequency tends to zero, the period diverges, and the oscillation is replaced by a secular term. The word *zero frequency* is more accurate than *no frequency*, and §*The Fourier Dictionary at the Limit* makes the distinction precise.

## The Three Flows

**Proposition (the exponential on each stratum).** The three normal forms give three flows.

| stratum | $\tilde Q$ | $\exp(\theta\tilde Q)$ | period | injective in $\theta$ |
|---|---|---|---|---|
| scalar | $Q_te_t$ | $\exp(\theta Q_t)\,e_t$ | $2\pi i/Q_t$ if $Q_t\neq0$; arbitrary at $0$ | no |
| nilpotent | $\vec N$, $\vec N^2=0$ | $e_t+\theta\vec N$ | none | yes |
| unipotent | $Q_t(e_t+\eta)$ | $\exp(\theta Q_t)\left(e_t+\theta Q_t\eta\right)$ | none | yes |

*Proof.* The scalar row is the complex exponential. The nilpotent row is the truncated form with $Q_t=0$. The unipotent row is the truncated form with $\vec N=Q_t\eta$. For injectivity on the defective strata, compare the coefficients of $\vec N$: if $\exp(\theta\tilde Q)=\exp(\theta'\tilde Q)$ with $\vec N\neq0$, the scalar parts give $\exp((\theta-\theta')Q_t)=1$ and the $\vec N$ coefficients give $\theta=\theta'$. On the scalar stratum the flow is periodic with period $2\pi i/Q_t$ for $Q_t\neq0$, and constant at the origin.

**Remark (the exponential of a zero divisor is a unit).** On the nilpotent stratum $\vec N\neq0$ and $\vec N^2=0$, the element is a zero divisor. For every $\theta$, its exponential $e_t+\theta\vec N$ is a unit, with inverse $e_t-\theta\vec N$. The flow lies in the unit group even though the element does not.

**Remark (the direction of the period).** On the defective strata the parameter $\theta$ is a complex number. On the nilpotent stratum the flow is the polynomial curve $e_t+\theta\vec N$, whose image is the complex line $e_t+\mathbb{C}\vec N$. On the unipotent stratum the flow is $\exp(\theta Q_t)(e_t+\theta Q_t\eta)$, a scalar exponential times a linear term. Neither is a circle, and neither is periodic. The scalar stratum is the only stratum of the cone on which the flow is periodic.

**Proposition (the principal logarithm).** On $\Sigma_{10}$, with $\eta=\vec Q/Q_t$ (zero on the scalar stratum),

$$
\operatorname{Log}\tilde Q=\operatorname{Log}Q_t\,e_t+\eta
=\operatorname{Log}Q_t\,e_t+\frac{\vec Q}{Q_t},
$$

where $\operatorname{Log}$ on the right is the principal complex logarithm. It is real-analytic on $\Sigma_{10}$ and satisfies $\lVert\vec Q/Q_t\rVert\to\infty$ as $Q_t\to0$. On the nilpotent stratum and at the origin no logarithm exists.

*Proof.* Exponentiate the display: $\exp(\operatorname{Log}Q_t)(e_t+\eta)=Q_te_t+\vec Q$. The divergence is the factor $1/Q_t$. A logarithm is an element whose exponential is $\tilde Q$; the exponential lands in the unit group, and the nilpotent stratum and the origin are not units.

**Remark (the local inverse is not the principal branch).** The exponential is a local biholomorphism at every point of the cone (§*The Differential and the Critical Locus*), so a local inverse exists at the nilpotent stratum. It is not the principal logarithm: the principal branch is defined on the units, and it diverges as the unipotent stratum approaches the non-unit $\vec N$. The divergence is a property of the branch, not of the exponential.

## The Differential and the Critical Locus

**The Fréchet derivative.** For $X\in\mathbb{B}$,

$$
d\exp_{\tilde Q}(X)=\int_0^1\exp\bigl((1-s)\tilde Q\bigr)\,X\,\exp(s\tilde Q)\,ds.
$$

**Proposition (the derivative off the cone).** Let $B^2\neq0$, $\lambda_\pm=Q_t\pm iB$, and $\tilde\Pi_\pm$ the spectral idempotents. Then

$$
d\exp_{\tilde Q}(X)
=\exp(\lambda_+)\tilde\Pi_+X\tilde\Pi_+
+\exp(\lambda_-)\tilde\Pi_-X\tilde\Pi_-
+\frac{\exp(\lambda_+)-\exp(\lambda_-)}{\lambda_+-\lambda_-}
\left(\tilde\Pi_+X\tilde\Pi_-+\tilde\Pi_-X\tilde\Pi_+\right).
$$

*Proof.* The element is diagonalisable, with the four Peirce corners $\tilde\Pi_iX\tilde\Pi_j$. On the corner $(i,j)$ the derivative acts as the divided difference $(\exp\lambda_i-\exp\lambda_j)/(\lambda_i-\lambda_j)$, which is $\exp\lambda_i$ when $i=j$.

**Proposition (the derivative on the cone).** Let $\tilde Q=Q_te_t+\vec N$ with $\vec N^2=0$. Then

$$
\boxed{\ d\exp_{\tilde Q}(X)=\exp(Q_t)\left[X+\frac12\left(X\vec N+\vec N X\right)+\frac16\,\vec N X\vec N\right]\ }.
$$

The bracket is $\mathrm{id}+T$ with $T$ nilpotent, $T^3=0$. In particular $d\exp_{\tilde Q}$ is invertible, with determinant $\exp(4Q_t)$.

*Proof.* Insert $\exp((1-s)\tilde Q)=\exp((1-s)Q_t)(e_t+(1-s)\vec N)$ and $\exp(s\tilde Q)=\exp(sQ_t)(e_t+s\vec N)$ in the integral. The product is

$$
\exp(Q_t)\left[X+sX\vec N+(1-s)\vec N X+s(1-s)\vec N X\vec N\right],
$$

and integrating $s$ over $[0,1]$ gives the display. For the nilpotency, approximate $\tilde Q$ by regular elements. On a regular element the four eigenvalues of $d\exp$ are $\exp\lambda_+$, $\exp\lambda_-$ and the divided difference twice; all four tend to $\exp(Q_t)$ as the approximating elements tend to $\tilde Q$. The eigenvalues depend continuously on the matrix, so at $\tilde Q$ all four are $\exp(Q_t)$, and $T$ is nilpotent. The index is three off the scalar stratum: all non-zero square-zero elements are conjugate, so it suffices to take $\vec N=\vec e_x+i\vec e_y$ and the basis $(\vec N,-\vec e_t-i\vec e_z,\vec e_x,-i\vec e_z)$, in which

$$
T=\begin{pmatrix}
0&-1&-\tfrac13&0\\
0&0&1&0\\
0&0&0&0\\
0&0&-1&0
\end{pmatrix},
$$

whose square is non-zero and whose cube is zero. On the scalar stratum $T=0$. The determinant is the product of the four eigenvalues.

**Corollary (the cone is regular).** The exponential is a local biholomorphism at every point of $\mathcal S$.

**Theorem (the critical locus).** The differential $d\exp_{\tilde Q}$ is singular exactly when

$$
\lambda_+-\lambda_-\in2\pi i\mathbb{Z}\setminus\{0\},
$$

that is, exactly when

$$
B\in\pi\mathbb{Z}\setminus\{0\},
\qquad
B^2\in\pi^2\mathbb{Z}\setminus\{0\}.
$$

The critical locus is the union of the complex quadrics $B^2=\pi^2k^2$, $k\neq0$. The spectral cone $B=0$ is disjoint from it.

*Proof.* The divided difference vanishes exactly when $\exp\lambda_+=\exp\lambda_-$ and $\lambda_+\neq\lambda_-$, that is when $\lambda_+-\lambda_-=2\pi ik$ with $k\neq0$. Since $\lambda_+-\lambda_-=2iB$, this is $B=\pi k$. On the cone $B=0$, and the divided difference is $\exp(Q_t)\neq0$.

**Corollary (the determinant).** For every $\tilde Q$,

$$
\det d\exp_{\tilde Q}
=\exp(2Q_t)\left(\frac{\exp(\lambda_+)-\exp(\lambda_-)}{\lambda_+-\lambda_-}\right)^2,
$$

with the divided difference read as $\exp(Q_t)$ on the cone. On the cone the determinant is $\exp(4Q_t)$.

**Remark (resonance, not collision).** The cone is a collision of the two eigenvalues. The critical locus is a collision modulo $2\pi i$. The exponential is singular at the second and regular at the first, which reverses the naive expectation. The two loci are disjoint. The spectral cone is the worst place to look for a singularity of the exponential and the best place to look for a singularity of its spectral chart.

**Corollary (the kernel on the cone).** Let $\tilde Q\in\mathcal S$. Then $\exp(\tilde Q)=e_t$ exactly when $\tilde Q=2\pi ik\,e_t$ with $k\in\mathbb{Z}$.

*Proof.* Write $\tilde Q=Q_te_t+\vec N$ with $\vec N^2=0$. The equation $\exp(Q_t)(e_t+\vec N)=e_t$ gives $\exp(Q_t)=1$ and $\vec N=0$.

## The Resolvent and the Double Pole

**The operator.** Let $L_{\tilde Q}(X)=\tilde QX$ be left multiplication. Off the cone the spectral idempotents give the partial fraction decomposition of the resolvent; on the defective strata the nilpotent part gives a double pole.

**Proposition (two simple poles).** For $B^2\neq0$,

$$
(z-L_{\tilde Q})^{-1}
=\frac{L_{\tilde\Pi_+}}{z-\lambda_+}
+\frac{L_{\tilde\Pi_-}}{z-\lambda_-}.
$$

**Proposition (one double pole on the defective strata).** For $\tilde Q=Q_te_t+\vec N$ with $\vec N^2=0$,

$$
(z-L_{\tilde Q})^{-1}
=\frac{\mathrm{id}}{z-Q_t}
+\frac{L_{\vec N}}{(z-Q_t)^2}.
$$

If $\vec N=0$ the second term vanishes and the pole is simple.

*Proof.* On the cone $L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec N}$ and $L_{\vec N}^2=0$. The Neumann series $(z-Q_t)^{-1}\sum_{n\geq0}(L_{\vec N}/(z-Q_t))^n$ truncates at $n=1$.

**Theorem (the merging of the poles).** As $B\to0$, the two simple poles at $\lambda_\pm$ merge at $Q_t$. The sum of the two residues is

$$
L_{\tilde\Pi_+}+L_{\tilde\Pi_-}=\mathrm{id},
$$

which is the residue of the double pole; the coefficient of $(z-Q_t)^{-2}$ is $L_{\vec N}$. The individual residues diverge like $1/B$.

*Proof.* The Lagrange idempotents are $\tilde\Pi_\pm=(e_t\mp i\vec Q/B)/2$, which diverge like $\mp i\vec Q/(2B)$ when $\vec Q\neq0$. Their sum is $e_t$, and their difference is $-i\vec Q/B$, whose product with $B$ is finite. The resolvent identity is the proposition above. On the scalar stratum $\vec N=0$, the second term vanishes and the merged pole is simple.

**Remark (the spectral resolution degenerates).** Off the cone the resolvent has two simple poles with residues $L_{\tilde\Pi_\pm}$, the two spectral projectors. On the defective strata it has one double pole: one residue $\mathrm{id}$ and one nilpotent coefficient $L_{\vec N}$. On the scalar stratum the second coefficient vanishes and the pole is simple. The two-term splitting of the identity is lost; the identity itself and the nilpotent direction survive. This is the analytic form of the flag of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Isotropic Line and the Flag*: a line and a filtration, not a direct sum.

## The Hermitian Norm

**The Hermitian norm.** For a biquaternion $X$, $\langle X\rangle_*=\operatorname{Sc}(XX^*)=\sum_\mu\lvert X_\mu\rvert^2$, the positive Hermitian form of *Conventions in Mathematics*, §*The Form Convention, the Norm Convention and the Unitary Convention*. It is a scalar, not an element.

**Proposition (the norm off the cone).** Let $B^2\neq0$, let $\rho=\vec Q/B$, and let $\theta$ be real. Then

$$
\langle\exp(\theta\tilde Q)\rangle_*
=\lvert\exp(\theta Q_t)\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\rho\rVert^2\right),
\qquad
\lVert\rho\rVert^2=\sum_k\lvert\rho_k\rvert^2.
$$

This is *Relations between the Biquaternion Exponential and the Fourier Kernel*, §*Normality, Unitarity and the Hermitian Norm of the Flow*.

**Theorem (the norm on the cone).** Let $\tilde Q=Q_te_t+\vec N$ with $\vec N^2=0$, and let $\theta$ be real. Then

$$
\langle\exp(\theta\tilde Q)\rangle_*
=\exp(2\theta\operatorname{Re}Q_t)
\left(1+\theta^2\lVert\vec N\rVert^2\right),
\qquad
\lVert\vec N\rVert^2=\sum_k\lvert N_k\rvert^2.
$$

The norm is continuous across the cone, and its limit is the value at the truncated exponential.

*Proof.* The truncated form gives $\exp(\theta\tilde Q)=\exp(\theta Q_t)(e_t+\theta\vec N)$. The scalar part of $(e_t+\theta\vec N)(e_t+\theta\vec N^*)$ is $1+\theta^2\lVert\vec N\rVert^2$, because the cross terms are pure vectors and $\operatorname{Sc}(\vec N\vec N^*)=\lVert\vec N\rVert^2$.

**Remark (the decomposition diverges, the norm does not).** In the regular formula the factor $\lVert\rho\rVert^2$ diverges like $1/\lvert B\rvert^2$ at the cone, while the product $\lvert\sin(B\theta)\rvert^2\lVert\rho\rVert^2$ tends to $\theta^2\lVert\vec N\rVert^2$. The norm has a limit; its decomposition into oscillation amplitude and norm deficit does not. The deficit $\lVert\rho\rVert^2-1$ is an amplitude that diverges, not a rate. The rates are $\operatorname{Re}Q_t$, which survives, and $\operatorname{Im}B$, which tends to zero.

## Spectral Degeneracy and Polar Degeneracy

**The two conditions are independent.** The spectral cone is $B^2=0$; the null cone is $N=0$. Their intersection is $\Sigma_{00}$, and the four sectors of §*The Cone and Its Strata* separate them. The modulus–unit polar decomposition is defined on the complement of the null cone, $N\neq0$.

**Theorem (the polar word follows the norm).** The four-factor exponential polar decomposition

$$
\tilde Q=r\,\exp(i\alpha)\,\exp\left(i\frac{\psi}{2}\vec u_{\mathrm b}\right)\exp\left(\frac{\theta}{2}\vec u_{\mathrm r}\right)
$$

exists exactly on the unit group $N\neq0$, that is on $\Sigma_{11}\cup\Sigma_{10}$. On $\Sigma_{10}$ it exists, and the two-factor polar decomposition $\tilde Q=Q_HQ_0$ has $Q_H$ of rank two and $Q_0$ unitary. On $\Sigma_{01}$ the two-factor decomposition exists, with $Q_H$ of rank one and $Q_0$ a partial isometry, but the modulus–unit decomposition does not. On $\Sigma_{00}$ the same holds, with both factors zero at the origin.

*Proof.* The modulus of the exponential polar decomposition is a non-zero square root of $N=\langle\tilde Q\rangle_{\natural}$, which exists exactly when $N\neq0$. On the unit group, $QQ^*$ is invertible, so $Q_H=(QQ^*)^{1/2}$ is positive definite of rank two and $Q_0=Q_H^{-1}Q$ is unitary. On the null cone, $QQ^*$ has rank one for $\tilde Q\neq0$, by *The Polar Decomposition of a N-Degenerate Biquaternion*, §*The Two-Factor Decomposition*; the square root has rank one and $Q_0$ is a partial isometry, not unitary.

**Corollary (the correct discontinuity).** The isometry factor is discontinuous at the null cone, not at the spectral cone; the Hermitian factor is continuous across the null cone. On $\Sigma_{10}=\mathcal S\setminus\mathcal N$ both factors are analytic.

*Proof.* The polar formula $Q_H=(QQ^*)^{1/2}$, $Q_0=Q_H^{-1}Q$ is analytic wherever $QQ^*$ is invertible, and $\det(QQ^*)=\lvert N\rvert^2$. On $\Sigma_{10}$, $N=Q_t^2\neq0$. On the null cone the Hermitian factor has the continuous limit of *The Polar Decomposition of a N-Degenerate Biquaternion*, §*Continuity*, while the isometry factor does not.

**Example (a unit on the spectral cone).** Let

$$
\tilde Q=e_t+\vec e_x+i\vec e_y.
$$

Then $B^2=1+i^2=0$ and $N=1+0=1$. The element is a unit, its spectrum is $\{1\}$, its minimal polynomial is $(X-1)^2$, and it has no element-supplied root. Its polar factors are the regular ones: $Q_H$ has rank two and $Q_0$ is unitary. The element is spectrally degenerate and polar-regular at the same time.

**Example (a zero divisor on the spectral cone).** Let $\tilde Q=\vec e_x+i\vec e_y$. Then $B^2=0$ and $N=0$. The element is a non-zero square-zero element, a zero divisor, not a unit. Its polar factors are $Q_H$ of rank one and $Q_0$ a partial isometry, and the polar word does not exist.

**Remark (the correction of a false identification).** The spectral cone alone does not destroy the polar decomposition, the modulus or the four-factor word. It destroys the root, the frequency, the idempotents and the eigenbasis. The modulus–unit polar decomposition is destroyed by the null cone, and the two cones meet only at $\Sigma_{00}$. A statement that reads *the polar decomposition fails at $B=0$* is true only at the nilpotent stratum and at the origin; at the unipotent stratum it is false.

## The Fourier Dictionary at the Limit

**The dictionary off the cone.** With $\rho=\vec Q/B$, $\omega=B/2\pi$ and $W(t,\omega)=\exp(-2\pi\rho\omega t)$,

$$
\exp(\theta\tilde Q)=\exp(\theta Q_t)\,W\left(-\theta,\frac{B}{2\pi}\right).
$$

This is *Relations between the Biquaternion Exponential and the Fourier Kernel*, §*The Kernel Identity*.

**Proposition (the composite kernel).** With the element's own root and frequency,

$$
W\left(t,\frac{B}{2\pi}\right)
=\exp(-\rho Bt)
=\exp(-t\vec Q)
=\cos(Bt)\,e_t-\sin(Bt)\,\rho,
$$

and

$$
W\left(t,\frac{B}{2\pi}\right)\longrightarrow e_t-t\vec N
\qquad(B\to0).
$$

*Proof.* The first identity is $\rho B=\vec Q$; the second is the closed form of the exponential of $-t\vec Q$; the limit is the truncated form.

**Theorem (what the dictionary keeps).** The kernel identity extends to the cone as

$$
\exp(\theta\tilde Q)=\exp(\theta Q_t)\exp(\theta\vec N).
$$

The kernel as a function of the element's root has no limit; the composite with the element's frequency has the limit $e_t-t\vec N$.

*Proof.* The right-hand side is the truncated form. The kernel $W(t,\omega)$ is a function of a root $\rho$; on the cone no element-supplied root exists. The composite uses the product $\rho\omega=\vec Q/2\pi$, which has a finite limit.

**Remark (zero frequency is not no frequency).** The frequency $B/2\pi$ tends to zero and the period $2\pi/B$ to infinity. At fixed $\omega=0$ the kernel is $e_t$, because $\cos0=1$ and $\sin0=0$; at the element's frequency the kernel tends to $e_t-t\vec N$. The two limits differ by the $0\cdot\infty$ product $\rho\omega=\vec Q/2\pi$. The frequency and the root are not independent variables on the cone, and the correct statement is *zero frequency with an infinite root*, not *no kernel*.

**Remark (the two characters merge).** Off the cone the spectral form of the flow is

$$
\exp(\theta\tilde Q)
=\exp(\theta\lambda_+)\tilde\Pi_+
+\exp(\theta\lambda_-)\tilde\Pi_-.
$$

The two characters have exponents $\lambda_\pm=Q_t\pm iB$; on the cone they merge at $\exp(\theta Q_t)$. The two idempotents diverge individually, but their sum is $e_t$ and their difference carries the nilpotent direction. The two-frequency reading becomes one frequency with a nilpotent multiplicity: a double character, not a pair of characters.

## What Fails and What Survives

**What fails at the cone.**

- The root $\rho=\vec Q/B$: it has no limit at a non-scalar point of the cone, because $\lVert\rho\rVert$ diverges.
- The frequency as a non-zero rate: it tends to zero and the period to infinity; the oscillatory factor is replaced by a polynomial or exponential-times-linear term.
- The spectral idempotents $\tilde\Pi_\pm$: they diverge like $1/B$.
- The two-term spectral decomposition: none off the scalar stratum.
- The eigenbasis: none off the scalar stratum; the canonical objects are the line and the flag.
- The kernel as a function of the element's root: no root, no kernel.
- The principal logarithm on $\Sigma_{00}$: its elements are not units.
- The four-factor polar word on $\Sigma_{01}$ and $\Sigma_{00}$: the modulus vanishes.

**What survives at the cone.**

- The exponential and the flow: entire, polynomial in $\theta$ on the cone.
- The root-free closed form: entire in the coefficients.
- The three strata and their normal forms.
- The similarity classification: the scalar class, the nilpotent class and the unipotent class.
- The differential: invertible on the whole cone, with $d\exp_{\tilde Q}=\exp(Q_t)(\mathrm{id}+T)$ and $T^3=0$.
- The Hermitian norm of the flow: continuous limit.
- The two-factor polar decomposition: unitary on $\Sigma_{10}$, a partial isometry on $\Sigma_{00}$.
- The principal logarithm on $\Sigma_{10}$: real-analytic, divergent as $Q_t\to0$.
- The kernel as a value at the element's frequency: $e_t-t\vec N$.
- The flag, the line and the nilpotent direction.

**The one-line summary.** At $B=0$ the exponential is regular and the spectral chart is not: the two eigenvalues coalesce at $Q_t$, the root diverges, the frequency vanishes, the idempotents merge into a double pole, the flow truncates to the dual-number form, the Hermitian norm stays continuous, and the polar decomposition follows the norm rather than the discriminant.

## Summary

The exponential of a biquaternion is entire, and the spectral cone is not a singularity of the map. The root-free closed form

$$
\exp(\theta\tilde Q)=\exp(\theta Q_t)\left(\cos(B\theta)e_t+\frac{\sin(B\theta)}{B}\vec Q\right)
$$

is entire in the coefficients and tends to the truncated form $\exp(\theta Q_t)(e_t+\theta\vec N)$ on the cone. The root-parametrised form does not extend, because the root $\rho=\vec Q/B$ does not exist. The frequency tends to zero, the period to infinity, and the oscillation is replaced by a linear term.

The three strata carry three flows. The scalar stratum is periodic, with period $2\pi i/Q_t$ when $Q_t\neq0$; the nilpotent and unipotent strata are injective in $\theta$ and have no period. The principal logarithm is real-analytic on the units of the cone and diverges as the scalar part tends to zero; the nilpotent stratum has no logarithm, because it is not a unit.

The differential is the divided difference of the exponential. On the cone it is

$$
d\exp_{\tilde Q}(X)=\exp(Q_t)\left[X+\frac12(X\vec N+\vec N X)+\frac16\vec N X\vec N\right],
$$

which is $\exp(Q_t)(\mathrm{id}+T)$ with $T^3=0$; hence the exponential is a local biholomorphism on the whole cone, with determinant $\exp(4Q_t)$. The true critical locus is the resonance set $B\in\pi\mathbb{Z}\setminus\{0\}$, where the two eigenvalues differ by a non-zero multiple of $2\pi i$. The cone is a collision of eigenvalues; the resonance is a collision modulo $2\pi i$; the two loci are disjoint. The resolvent reads the degeneration as the merging of two simple poles into one double pole on the defective strata, or one simple pole on the scalar stratum: the residue $\mathrm{id}$ survives, the nilpotent coefficient $L_{\vec N}$ survives, and the two projectors diverge.

The Hermitian norm is continuous across the cone, with limit $\exp(2\theta\operatorname{Re}Q_t)(1+\theta^2\lVert\vec N\rVert^2)$ for real $\theta$. Its decomposition into oscillation amplitude and norm deficit is not continuous: the deficit diverges while the norm stays finite. The spectral cone destroys the root, the non-zero frequency, the idempotents and the eigenbasis; it does not destroy the exponential, the flow, the differential, the norm or the flag. The polar decomposition follows the norm, not the discriminant: the two-factor form is unitary on $\Sigma_{10}$ and a partial isometry on $\Sigma_{01}\cup\Sigma_{00}$, while the four-factor modulus–unit word exists exactly on the units and so is absent on $\Sigma_{01}$ and $\Sigma_{00}$. The kernel identity extends as a value, $e_t-t\vec N$, but not as a dictionary of objects, because the root does not exist.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $B$ | a fixed square root of $B^2$; the other exchanges $\lambda_+$ and $\lambda_-$ |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathcal N=\{N=0\}$ | the null cone |
| $\mathcal S^{\mathrm{s}},\mathcal S^{\mathrm{n}},\mathcal S^{\mathrm{u}}$ | the scalar, nilpotent and unipotent strata |
| $\Sigma_{11},\Sigma_{10},\Sigma_{01},\Sigma_{00}$ | the four sectors of the pair $(N\neq0,B^2\neq0)$ |
| $\vec N=\vec Q$ on $\mathcal S$, $\vec N^2=0$ | the nilpotent part of a degenerate element |
| $\eta=\vec N/Q_t$ | the unipotent direction on $\mathcal S^{\mathrm{u}}$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\rho=\vec Q/B$ | the root of $-1$ supplied by a spectrally regular element |
| $\tilde\Pi_\pm=(e_t\mp i\rho)/2$ | the spectral idempotents |
| $L_{\tilde Q}(X)=\tilde QX$ | left multiplication |
| $d\exp_{\tilde Q}$ | the Fréchet derivative of the exponential |
| $T$ | the nilpotent part of $d\exp_{\tilde Q}/\exp(Q_t)$ on the cone |
| $\mathcal R=\{B\in\pi\mathbb{Z}\setminus\{0\}\}$ | the resonance locus, the critical locus of $\exp$ |
| $\langle X\rangle_*=\operatorname{Sc}(XX^*)$ | the Hermitian norm, $\sum_\mu\lvert X_\mu\rvert^2$ |
| $\lVert\vec N\rVert^2=\sum_k\lvert N_k\rvert^2$ | the Euclidean square of the nilpotent vector |
| $W(t,\omega)=\exp(-2\pi\rho\omega t)$ | the biquaternion Fourier kernel |
| $Q_H=(QQ^*)^{1/2},\ Q_0=Q_H^{+}Q$ | the two polar factors |
| $\operatorname{Log}$ | the principal logarithm |

## Further Reading

- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the cone, the three strata, the flag and the similarity classification.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the closed forms, the exponential, the logarithm and the principal branch.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the root, the kernel identity, the Hermitian norm and the Fourier dictionary.
- [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), for the transform pair, inversion, Plancherel and the kernel.
- [Biquaternion Discrete Harmonic Analysis](biquaternion-discrete-harmonic-analysis.html), for the discrete transform and the condition on the root.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus, the unit factor and the four-factor word.
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the two-factor decomposition on the null cone, the rank-one Hermitian factor and the partial isometry.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the independence of the two conditions.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the exponential as a map of Lie groups and the Cartan decomposition.
- [Dual Numbers Harmonic Analysis](dual-numbers-harmonic-analysis.html), for the truncated characters of the nilpotent regime.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the conjugations, the Hermitian norm and the notation.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the spectral projectors, the Jordan form and the resolvent.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, 2008), for the Fréchet derivative of the exponential, the divided differences and the critical locus.
