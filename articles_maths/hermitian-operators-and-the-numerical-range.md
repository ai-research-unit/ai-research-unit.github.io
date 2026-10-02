# __Hermitian Operators and the Numerical Range__

## Introduction

The **numerical range** of a bounded operator is the set of scalars $\langle Tx,x\rangle$ taken on the unit sphere, and the **numerical radius** is its largest modulus. The numerical range is the smallest convex set that contains the spectrum, and it detects self-adjointness outright: $T$ is Hermitian exactly when every $\langle Tx,x\rangle$ is real. This gives a second route to the self-adjoint spectral theory, one that begins with a scalar-valued set rather than with an operator identity, and it is the route that generalises to operators that are not self-adjoint, where the numerical range remains convex but the spectrum need not be real. The two facts that organise the theory are the **Toeplitz–Hausdorff theorem**, which says that the numerical range is convex, and the equivalence of the numerical radius with the operator norm up to the factor $2$, which is sharp and which is the reason the numerical range controls the norm.

This article fixes the numerical range, the Toeplitz–Hausdorff theorem, the numerical radius and its relation to the norm, the Hermitian operators as the operators with real numerical range, and the normal operators as those whose numerical range is the convex hull of the spectrum. The self-adjoint spectral theory is *Self-Adjoint Operators and the Spectral Theorem*; the positivity and the square root are *Positive Operators and the Square Root*; the convexity and the spectral containment use the Hilbert-space structure of *Hilbert Spaces*; the sesquilinear forms underlying the numerical range are *Sesquilinear Forms and the Lax–Milgram Theorem*.

Throughout, $H$ is a complex Hilbert space with inner product linear in the first argument, $T\in B(H)$ is bounded, and the **numerical range** and **numerical radius** are

$$
W(T)=\{\langle Tx,x\rangle:\|x\|=1\},\qquad w(T)=\sup_{z\in W(T)}|z| .
$$

The closure of $W(T)$ is $\overline{W(T)}$, and the spectrum is $\sigma(T)$.

## The Numerical Range

**Definition.** The **numerical range** of $T$ is $W(T)=\{\langle Tx,x\rangle:\|x\|=1\}$ and the **numerical radius** is $w(T)=\sup_{z\in W(T)}|z|$.

**Proposition (elementary properties).** For $T,S\in B(H)$ and $\lambda\in\mathbb{C}$,

$$
W(T+S)\subseteq W(T)+W(S),\qquad W(\lambda T)=\lambda W(T),\qquad W(T^*)=\overline{W(T)} ,
$$

and $W(T)$ is a bounded subset of the disc of radius $\|T\|$; the numerical radius satisfies

$$
w(T)\le\|T\| .
$$

*Proof.* The set statements are immediate from the linearity of the form, and $\langle T^*x,x\rangle=\overline{\langle Tx,x\rangle}$ gives the third; the bound is Cauchy–Schwarz, $|\langle Tx,x\rangle|\le\|T\|\|x\|^2=\|T\|$.

**Proposition (the diagonal determines the form).** The numerical range determines the operator through the polarisation identity: for every $x$,

$$
\langle Tx,y\rangle=\tfrac14\bigl(\langle T(x+y),x+y\rangle-\langle T(x-y),x-y\rangle+i\langle T(x+iy),x+iy\rangle-i\langle T(x-iy),x-iy\rangle\bigr),
$$

so two operators with the same sesquilinear form have the same numerical range, and conversely an operator is determined by its numerical range as a function on pairs, not merely by the set $W(T)$.

*Proof.* The four terms are the expansion of the sesquilinear form of $T$ at the four points, and the identity is the standard polarisation; the remaining statement is the uniqueness of the form for an operator.

## The Toeplitz–Hausdorff Theorem

**Theorem (convexity).** For every $T\in B(H)$ the numerical range $W(T)$ is convex, and its closure is convex and compact.

*Proof.* Convexity is inherited by compression: if $P$ is the orthogonal projection onto a subspace $M$, then for $x\in M$ of norm one one has $\langle PTPx,x\rangle=\langle TPx,Px\rangle=\langle Tx,x\rangle$, so $W(PTP)\subseteq W(T)$. Given two unit vectors $x,y$, let $M$ be the span of $x$ and $y$, of dimension at most two, and let $T_2=PTP$ be the compression. The numerical range of a $2\times2$ matrix is an ellipse with foci at its eigenvalues, by the elliptical range theorem, hence convex; it contains $\langle Tx,x\rangle$ and $\langle Ty,y\rangle$, and it lies in $W(T)$ by the compression inclusion. Therefore $W(T)$ contains the segment joining any two of its points, and since the points were arbitrary it is convex.

**Theorem (the spectrum lies in the closure).** For every $T\in B(H)$,

$$
\sigma(T)\subseteq\overline{W(T)} ,
$$

and the boundary of the spectrum is contained in the boundary of the closure of the numerical range, $\partial\sigma(T)\subseteq\partial\overline{W(T)}$.

*Proof.* If $\lambda\notin\overline{W(T)}$ then the distance $d=\operatorname{dist}(\lambda,\overline{W(T)})$ is positive, and for $\|x\|=1$ one has $\|(\lambda I-T)x\|\ge|\langle(\lambda I-T)x,x\rangle|\ge d$, so $\lambda I-T$ is injective with closed range; the same estimate for $T^*$ shows the range is dense, so $\lambda\notin\sigma(T)$. The boundary statement is the standard improvement using the resolvent's analyticity.

## The Numerical Radius and the Norm

**Theorem (equivalence of the norms).** For every $T\in B(H)$,

$$
\tfrac12\|T\|\le w(T)\le\|T\| ,
$$

and the constant $\tfrac12$ is sharp: on the two-dimensional Hilbert space the shift matrix $T=\begin{pmatrix}0&2\\0&0\end{pmatrix}$ has $\|T\|=2$ and $w(T)=1$.

*Proof.* The upper bound is Cauchy–Schwarz. For the lower bound, the norm is recovered from the diagonal by polarisation and the identity $|\langle Tx,y\rangle|\le\frac12 w(T)(\|x\|^2+\|y\|^2)$, obtained from the two-point computation with the phase chosen so that $\langle Tx,y\rangle$ is real; optimising over $x,y$ of norm one gives $\|T\|\le2w(T)$. The claimed example has $W(T)$ the disc of radius $1$ and operator norm $2$, so the bound is attained.

**Proposition (power inequalities).** $w(T)^n\le\|T^n\|$ and $w(T^n)\le w(T)^n$, so the spectral radius is bounded by the numerical radius,

$$
r(T)\le w(T)\le\|T\| ,
$$

and the numerical radius does not exceed the norm; the lower bound on the norm is the only inequality that cannot be improved to an equality.

*Proof.* $\|T^n\|\ge|\langle T^nx,x\rangle|$ gives the first inequality; the second is the Cauchy–Schwarz estimate on the powers; the spectral radius bound is $\sigma(T^n)\subseteq\overline{W(T^n)}$ together with the limit formula $r(T)=\lim\|T^n\|^{1/n}$.

## Hermitian Operators

**Theorem (real numerical range characterises self-adjointness).** For $T\in B(H)$ the following are equivalent:

(i) $T$ is Hermitian, $T^*=T$;

(ii) $W(T)\subseteq\mathbb{R}$;

(iii) $\langle Tx,x\rangle\in\mathbb{R}$ for every $x$.

*Proof.* If $T=T^*$ then $\langle Tx,x\rangle=\overline{\langle Tx,x\rangle}$ is real, giving (i) $\Rightarrow$ (iii); (iii) $\Rightarrow$ (ii) is trivial; for (ii) $\Rightarrow$ (i), the polarisation identity shows that the sesquilinear form of $T$ equals that of $T^*$, and an operator is determined by its form, so $T=T^*$.

**Corollary.** For Hermitian $T$,

$$
\|T\|=w(T)=\sup_{x\in W(T)}|x| ,
$$

and the numerical range is the interval $[m,M]$ with $m=\inf W(T)$ and $M=\sup W(T)$ equal to the infimum and supremum of the spectrum; in particular $T$ is positive exactly when $W(T)\subseteq[0,\infty)$ and $T$ is positive and invertible exactly when $W(T)\subseteq[c,\infty)$ for some $c>0$.

*Proof.* The equality of the norm and the numerical radius is the norm formula of the self-adjoint theory; the endpoints of the interval are the infimum and supremum of the spectrum because $\sigma(T)\subseteq\overline{W(T)}$ and the extreme spectral values are extreme values of the quadratic form; the positivity statements translate the interval.

**Example (the sharpness of the spectral containment).** For the shift matrix $\begin{pmatrix}0&2\\0&0\end{pmatrix}$ the spectrum is $\{0\}$ but the numerical range is the closed disc of radius $1$; so the spectrum may be strictly inside the numerical range, and the containment $\sigma(T)\subseteq\overline{W(T)}$ cannot be reversed. For a normal operator the two coincide, as the next section records.

## Normal Operators

**Theorem (the numerical range of a normal operator).** If $T$ is normal then

$$
W(T)=\operatorname{conv}\sigma(T) ,
$$

the closed convex hull of the spectrum; conversely, an operator whose numerical range equals the convex hull of its spectrum on every invariant subspace is normal, and in finite dimension normality is equivalent to $W(T)=\operatorname{conv}\sigma(T)$.

*Proof.* For normal $T$ the spectral theorem writes $T=\int\lambda\,dE(\lambda)$, whence $\langle Tx,x\rangle=\int\lambda\,d\mu_x(\lambda)$ for the measure $\mu_x=\langle E(\cdot)x,x\rangle$ of total mass $\|x\|^2=1$; the integral of the identity over a probability measure lies in the closed convex hull of the support, which is contained in the convex hull of the spectrum, giving one inclusion, and the reverse inclusion follows by concentrating $\mu_x$ near each spectral value with an appropriate choice of $x$. The converse is the standard characterisation and is quoted.

**Corollary.** Hermitian operators are normal and their numerical range is the interval of the spectrum; unitary operators are normal with spectrum on the circle, so their numerical range is the closed convex hull of the spectrum, and for a unitary with spectrum the whole circle the numerical range is the closed unit disc.

*Proof.* Self-adjoint and unitary operators are normal, and the convex-hull formula applies; the examples are the corresponding spectral pictures.

**Example (matrices).** For a $2\times2$ matrix the numerical range is the ellipse with foci at the eigenvalues and minor axis determined by the off-diagonal entry; for a Hermitian matrix it degenerates to the interval between the extreme eigenvalues, for a normal matrix to the segment or polygon joining the eigenvalues, and for a non-normal matrix to a region strictly containing the convex hull of the spectrum. This is the finite-dimensional picture of the sharpness of the spectral containment.

## Summary

The numerical range $W(T)=\{\langle Tx,x\rangle:\|x\|=1\}$ of a bounded operator is a bounded subset of the disc of radius $\|T\|$, its adjoint conjugates it, and it is convex: the Toeplitz–Hausdorff theorem. The spectrum is contained in its closure, and its boundary is contained in the boundary of that closure, but the containment can be strict, as the shift matrix shows. The numerical radius satisfies $\tfrac12\|T\|\le w(T)\le\|T\|$ with the constant $\tfrac12$ sharp, so the numerical range controls the norm; the spectral radius satisfies $r(T)\le w(T)$. A bounded operator is Hermitian exactly when its numerical range is real, and then its norm equals its numerical radius and its numerical range is the interval between the extreme spectral values, so positivity is the statement that the interval lies in $[0,\infty)$. A normal operator has $W(T)=\operatorname{conv}\sigma(T)$, and for Hermitian and unitary operators this is the interval of the spectrum and the convex hull of the spectral points on the circle; for a general non-normal operator the numerical range is strictly larger than the convex hull of the spectrum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $W(T)=\{\langle Tx,x\rangle:\|x\|=1\}$ | the numerical range |
| $w(T)=\sup|W(T)|$ | the numerical radius |
| $W(T)$ convex | Toeplitz–Hausdorff theorem |
| $\sigma(T)\subseteq\overline{W(T)}$ | spectral containment |
| $\tfrac12\|T\|\le w(T)\le\|T\|$ | norm equivalence, $\tfrac12$ sharp |
| $r(T)\le w(T)$ | spectral radius bound |
| $W(T)\subseteq\mathbb{R}$ | characterises Hermitian operators |
| $\|T\|=w(T)$ | self-adjoint norm formula |
| $W(T)=[m,M]$ | numerical range of a Hermitian operator |
| $W(T)=\operatorname{conv}\sigma(T)$ | normal operators |

## Further Reading

- Otto Toeplitz, "Das algebraische Analogon zu einem Satze von Fejér", *Mathematische Zeitschrift* **2** (1918), 187–197, for the convexity of the numerical range.
- Felix Hausdorff, "Der Wertvorrat einer Bilinearform", *Mathematische Zeitschrift* **3** (1919), 314–316, for the convexity theorem in its general form.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the numerical range, its convexity and its elementary examples.
- Karl E. Gustafson and Duggirala K. M. Rao, *Numerical Range: The Field of Values of Linear Operators and Matrices* (Springer, 1997), for the systematic theory and the sharp constant of the norm equivalence.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the numerical range of matrices and the elliptical range theorem.
