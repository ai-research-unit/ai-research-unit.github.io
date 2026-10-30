# __Analysis on $\mathbb{C}^2$__

## Introduction

This article treats the analysis of holomorphic functions of two complex variables on the space $\mathbb{C}^2$ itself: the Cauchy–Riemann equations, the ring of entire functions, the maximum principle, the identity theorem, the iterated Cauchy formula on the polydisc, and the one-variable facts that fail. It is the first of the four analytical articles of the category; the model domains are *The Ball and the Bicylinder in $\mathbb{C}^2$*, the inhomogeneous Cauchy–Riemann equation is *The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$*, and the Fourier and Radon analysis is *Harmonic Analysis on $\mathbb{C}^2$*.

The general theory of holomorphic functions of $n$ variables, of domains of holomorphy, of pseudoconvexity and of the Cousin problems is *Several Complex Variables*. That article develops the theory for a variable number of variables and for arbitrary domains; this one fixes the space $\mathbb{C}^2$ and the functions defined on all of it, and it states what the case of two variables adds to the one-variable theory of *Complex Analysis*. The differential forms and the operators $\partial$ and $\bar\partial$ are from *Differential Forms and Stokes' Theorem*, and the notation is that of *Complex Two-Space*: a point is $z=(z_1,z_2)$ with $z_k=x_k+iy_k$, the Hermitian form is $H(z,w)=\sum_kz_k\overline{w_k}$, and the polydisc of multiradius $r=(r_1,r_2)$ about $a$ is
$$
\Delta(a,r)=\{z:\lvert z_k-a_k\rvert<r_k,\ k=1,2\}.
$$

**The analysis of $\mathbb{C}^2$ is not the one-variable theory twice.** Three things change. The Cauchy–Riemann system becomes overdetermined, so holomorphic functions are rigid and a harmonic function need not have a conjugate. The zeros and the singularities cease to be isolated, so the argument principle and the Laurent expansion have no direct analogues. And the boundary of a domain is odd-dimensional, so the Cauchy integral over a contour is replaced by an iterated integral over a torus or by a kernel that is not holomorphic. Everything that survives survives for the same reason: it is a one-variable statement applied on complex lines.

## Holomorphic Functions of Two Variables

**A holomorphic function of two variables is a real differentiable function whose differential is complex-linear at every point; equivalently, it satisfies the two Cauchy–Riemann equations $\bar\partial_kf=0$.**

**Definition.** Let $D\subset\mathbb{C}^2$ be a domain. A function $f:D\to\mathbb{C}$ is **holomorphic** when it is real differentiable at every point of $D$ and its differential $df(a)$ is $\mathbb{C}$-linear for every $a\in D$. The **Wirtinger operators** are
$$
\frac{\partial}{\partial z_k}=\frac12\left(\frac{\partial}{\partial x_k}-i\frac{\partial}{\partial y_k}\right),\qquad
\frac{\partial}{\partial\bar z_k}=\frac12\left(\frac{\partial}{\partial x_k}+i\frac{\partial}{\partial y_k}\right),
$$
and the **Cauchy–Riemann operator** is
$$
\bar\partial f=\frac{\partial f}{\partial\bar z_1}\,d\bar z_1+\frac{\partial f}{\partial\bar z_2}\,d\bar z_2.
$$

**Proposition (the Cauchy–Riemann equations).** A real differentiable function $f=u+iv$ on $D$ is holomorphic exactly when
$$
\frac{\partial f}{\partial\bar z_1}=0,\qquad \frac{\partial f}{\partial\bar z_2}=0,
$$
that is, exactly when the four real equations
$$
\frac{\partial u}{\partial x_k}=\frac{\partial v}{\partial y_k},\qquad
\frac{\partial u}{\partial y_k}=-\frac{\partial v}{\partial x_k},\qquad k=1,2,
$$
hold on $D$.

*Proof.* The differential is
$$
df=\sum_{k=1}^{2}\left(\frac{\partial f}{\partial z_k}dz_k+\frac{\partial f}{\partial\bar z_k}d\bar z_k\right),
$$
and it is $\mathbb{C}$-linear exactly when the coefficients of the anti-holomorphic differentials $d\bar z_k$ vanish. The real form of the two complex equations is the displayed system, obtained by separating $f=u+iv$ into real and imaginary parts.

**Remark (the count of the equations).** In one variable the Cauchy–Riemann system is two real equations for the two functions $u$ and $v$, and it is determined. **In two variables it is four real equations for two functions, and it is overdetermined.** The overdetermination is not a defect of the presentation: it is the source of the rigidity of the theory, and it is the reason a harmonic function of two variables need not have a harmonic conjugate.

**Theorem (the power series).** A function $f$ on the polydisc $\Delta(a,r)$ is holomorphic if and only if it is the sum of a power series
$$
f(z)=\sum_{\alpha\in\mathbb{N}^2}c_\alpha(z-a)^\alpha,\qquad c_\alpha=\frac{1}{\alpha!}\,\frac{\partial^{\lvert\alpha\rvert}f}{\partial z^\alpha}(a),
$$
convergent absolutely and uniformly on every compact subset of $\Delta(a,r)$.

*Proof.* A convergent power series is holomorphic, because it is holomorphic in each variable and the derivative of a uniformly convergent series may be taken term by term. Conversely, the iterated Cauchy formula of the section below represents a holomorphic function as an integral over the distinguished boundary of a smaller polydisc; expanding each Cauchy factor as a geometric series gives the coefficients and the convergence.

**Proposition (the complex Jacobian and the real Jacobian).** Let $f=(f_1,f_2)$ be holomorphic on $D$ and let $J_f=\bigl(\partial f_j/\partial z_k\bigr)$ be its complex Jacobian. Then $f$ is real differentiable, and its real Jacobian determinant is
$$
\det J_{\mathbb{R}}f=\lvert\det J_f\rvert^2.
$$
In particular $f$ is a local biholomorphism at $a$ exactly when $\det J_f(a)\neq0$.

*Proof.* Write $z_k=x_k+iy_k$ and read the real Jacobian as a block matrix $\begin{pmatrix}A&-B\\B&A\end{pmatrix}$, where $A$ and $B$ are the real and imaginary parts of $J_f$. The determinant of such a block matrix is $\lvert\det(A+iB)\rvert^2=\lvert\det J_f\rvert^2$. The inverse function theorem applied to the real map, together with the $\mathbb{C}$-linearity of the differential, gives the local biholomorphism.

## The Cauchy–Riemann Equations and Harmonicity

**The real and imaginary parts of a holomorphic function are harmonic, but the converse fails: a harmonic function has a conjugate only when it is pluriharmonic.**

**Definition.** The **Laplacian** on $\mathbb{C}^2$ is
$$
\Delta=\frac{\partial^2}{\partial x_1^2}+\frac{\partial^2}{\partial y_1^2}+\frac{\partial^2}{\partial x_2^2}+\frac{\partial^2}{\partial y_2^2}
=4\left(\frac{\partial^2}{\partial z_1\partial\bar z_1}+\frac{\partial^2}{\partial z_2\partial\bar z_2}\right).
$$
A $C^2$ function is **harmonic** when $\Delta u=0$.

**Proposition (holomorphic implies harmonic).** If $f=u+iv$ is holomorphic on $D$, then $u$ and $v$ are harmonic on $D$.

*Proof.* From the Cauchy–Riemann equations, $\partial u/\partial x_k=\partial v/\partial y_k$ and $\partial u/\partial y_k=-\partial v/\partial x_k$. Differentiating the first equation in $x_k$ and the second in $y_k$ and adding gives
$$
\frac{\partial^2u}{\partial x_k^2}+\frac{\partial^2u}{\partial y_k^2}
=\frac{\partial^2v}{\partial x_k\partial y_k}-\frac{\partial^2v}{\partial y_k\partial x_k}=0,
$$
because the mixed partials commute. The sum over $k$ gives $\Delta u=0$, and the same computation with $u$ and $v$ exchanged gives $\Delta v=0$.

**Definition.** A $C^2$ function $u$ is **pluriharmonic** when its restriction to every complex line is harmonic, equivalently when
$$
\frac{\partial^2u}{\partial z_j\partial\bar z_k}=0\qquad\text{for all }j,k.
$$

**Theorem (the conjugate exists exactly for pluriharmonic functions).** Let $u$ be a real $C^2$ function on $\mathbb{C}^2$. There is a real $C^2$ function $v$ with $u+iv$ holomorphic if and only if $u$ is pluriharmonic, and then $v$ is unique up to an additive real constant.

*Proof.* The function $f=u+iv$ is holomorphic exactly when $\bar\partial u+i\bar\partial v=0$, which for real $u$ and $v$ is the pair of equations
$$
\partial v=-i\,\partial u,\qquad \bar\partial v=i\,\bar\partial u,
$$
the second being the conjugate of the first. A real $v$ with these prescribed $\partial v$ and $\bar\partial v$ exists exactly when the $1$-form $\partial v+\bar\partial v$ is closed, that is, when
$$
0=d(\partial v+\bar\partial v)=\bar\partial\partial v+\partial\bar\partial v
=i\,\partial\bar\partial u+i\,\partial\bar\partial u=2i\,\partial\bar\partial u.
$$
Hence the condition is $\partial\bar\partial u=0$, which is pluriharmonicity. On $\mathbb{C}^2$, which is simply connected, the primitive $v$ exists and is unique up to a constant.

**Remark (harmonic against pluriharmonic).** Every pluriharmonic function is harmonic, because $\Delta=4\sum_k\partial^2/\partial z_k\partial\bar z_k$ is the trace of the Hermitian matrix of the four mixed derivatives. **The converse fails**: the function
$$
u(z)=\lvert z_1\rvert^2-\lvert z_2\rvert^2
$$
is harmonic, since each term is harmonic, but
$$
\frac{\partial^2u}{\partial z_1\partial\bar z_1}=1\neq0,
$$
so $u$ is not pluriharmonic and has no conjugate. **This is the first one-variable fact that fails in two variables**: in the plane every harmonic function on a simply connected domain has a harmonic conjugate.

## The Maximum Principle and the Identity Theorem

**The maximum modulus principle and the identity theorem hold in two variables, and both are proved by restricting the function to complex lines.**

**Theorem (the maximum principle).** Let $D\subset\mathbb{C}^2$ be a domain and let $f$ be holomorphic on $D$. If $\lvert f\rvert$ attains a local maximum at a point of $D$, then $f$ is constant on $D$. If $D$ is bounded and $f$ is continuous on $\overline{D}$, then
$$
\max_{\overline{D}}\lvert f\rvert=\max_{\partial D}\lvert f\rvert.
$$

*Proof.* Suppose $\lvert f\rvert$ has a local maximum at $a\in D$. For every direction $v\in\mathbb{C}^2$, the function $\lambda\mapsto f(a+\lambda v)$ is holomorphic on a disc about $0$, and its modulus has a maximum at $0$; the one-variable maximum principle gives $f(a+\lambda v)=f(a)$ for $\lvert\lambda\rvert$ small. The differential of $f$ at $a$ therefore vanishes, and, varying $v$, $f$ is constant on a neighbourhood of $a$. The identity theorem below extends the constancy to $D$. The boundary statement follows: a maximum on $\overline{D}$ is either on $\partial D$ or at an interior point, where $f$ is constant and the two maxima agree.

**Corollary (Liouville).** A bounded holomorphic function on $\mathbb{C}^2$ is constant.

*Proof.* Fix $a\in\mathbb{C}^2$. For every direction $v\in\mathbb{C}^2$, the function $\lambda\mapsto f(a+\lambda v)$ is entire and bounded, hence constant by the one-variable Liouville theorem. Varying $v$ and using the identity theorem, $f$ is constant on $\mathbb{C}^2$.

**Theorem (the identity theorem).** Let $D\subset\mathbb{C}^2$ be a domain and let $f$ be holomorphic on $D$. If $f$ vanishes on a nonempty open subset of $D$, then $f\equiv0$ on $D$. Equivalently, if $f$ is not identically zero, its zero set has empty interior.

*Proof.* Let $S$ be the set of points at which $f$ and all its partial derivatives vanish. The set $S$ is closed, because the derivatives are continuous, and it is open, because at a point of $S$ the power series of $f$ has all coefficients zero and therefore vanishes on a polydisc about the point. A nonempty open subset on which $f$ vanishes is contained in $S$, so $S$ is nonempty; a nonempty subset of a domain that is open and closed is the whole domain, and $f=0$ there.

**Remark (what survives and what does not).** The maximum principle, the identity theorem and Liouville's theorem survive, because each is a one-variable statement applied on the complex lines through a point. **The statements that fail are those that count zeros or describe a singularity**, and they fail because the zero set and the singular set are no longer discrete. The one-variable form of the identity theorem, in which an accumulation point of the zero set suffices, also fails: the function $f(z_1,z_2)=z_1$ vanishes on the complex line $\{z_1=0\}$, which has accumulation points, and is not identically zero.

## The Iterated Cauchy Formula on the Polydisc

**The Cauchy formula on a polydisc is the one-variable formula applied twice; it integrates over the distinguished boundary, a real two-dimensional torus, and not over the topological boundary.**

**Definition.** The **distinguished boundary** of the polydisc $\Delta(a,r)$ is the torus
$$
T(a,r)=\{z:\lvert z_k-a_k\rvert=r_k,\ k=1,2\},
$$
oriented by the increasing arguments of $z_1-a_1$ and $z_2-a_2$.

**Theorem (the iterated Cauchy formula).** Let $f$ be holomorphic on a neighbourhood of the closed polydisc $\overline{\Delta(a,r)}$. Then for every $z\in\Delta(a,r)$,
$$
f(z)=\frac{1}{(2\pi i)^2}\int_{T(a,r)}\frac{f(\zeta_1,\zeta_2)}{(\zeta_1-z_1)(\zeta_2-z_2)}\,d\zeta_2\,d\zeta_1.
$$

*Proof.* For fixed $z_1$ with $\lvert z_1-a_1\rvert<r_1$, the function $\zeta_2\mapsto f(z_1,\zeta_2)$ is holomorphic near the closed disc $\lvert\zeta_2-a_2\rvert\le r_2$, so the one-variable Cauchy formula gives
$$
f(z_1,z_2)=\frac{1}{2\pi i}\int_{\lvert\zeta_2-a_2\rvert=r_2}\frac{f(z_1,\zeta_2)}{\zeta_2-z_2}\,d\zeta_2.
$$
The integrand is holomorphic in $z_1$ near $\lvert z_1-a_1\rvert\le r_1$, uniformly in $\zeta_2$, so the one-variable formula applies again in the first variable:
$$
f(z_1,\zeta_2)=\frac{1}{2\pi i}\int_{\lvert\zeta_1-a_1\rvert=r_1}\frac{f(\zeta_1,\zeta_2)}{\zeta_1-z_1}\,d\zeta_1.
$$
Substituting and using Fubini gives the display.

**Corollary (Cauchy estimates).** If $\lvert f\rvert\le M$ on $T(a,r)$, then the coefficients of the power series of $f$ about $a$ satisfy
$$
\lvert c_\alpha\rvert\le M\,r^{-\alpha}=M\,r_1^{-\alpha_1}r_2^{-\alpha_2}.
$$

*Proof.* Differentiate the integral formula under the sign, or bound the coefficients $c_\alpha$ obtained by expanding the Cauchy factors; the modulus of the denominator is $r_1^{\alpha_1+1}r_2^{\alpha_2+1}$ on the torus.

**Corollary (holomorphic implies analytic).** A holomorphic function on a domain is real analytic, and its power series about a point converges on every polydisc about that point whose closure lies in the domain.

*Proof.* The formula gives the power series on every polydisc whose closure lies in the domain; the union of those polydiscs is the domain.

**Theorem (Weierstrass and Montel).** A sequence of holomorphic functions on a domain that converges uniformly on every compact subset has a holomorphic limit, and so do all its derivatives. A locally bounded family of holomorphic functions is normal.

*Proof.* The Cauchy estimates bound the derivatives uniformly on compact sets, so the sequence is equicontinuous and the limit is holomorphic by Morera's theorem applied on polydiscs; Montel's theorem follows from the Arzelà–Ascoli theorem and the Cauchy estimates.

**Remark (the dimension of the boundary).** The polydisc has real dimension $4$, its topological boundary has real dimension $3$, and its distinguished boundary $T(a,r)$ has real dimension $2$. **The Cauchy formula integrates over the two-dimensional torus, not over the three-dimensional boundary**, and the torus is the set on which both Cauchy factors are simultaneously non-singular. For a general domain there is no distinguished boundary of this product form, and the replacement is the Bochner–Martinelli kernel of *The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$*, which integrates over the full boundary and is not holomorphic in $z$.

## The Ring $\mathcal{O}(\mathbb{C}^2)$

**The entire functions of two variables form an integral domain; its units are the functions $e^g$, its finitely generated maximal ideals are the ideals of functions vanishing at a point, and it is neither a unique factorisation domain nor Noetherian.**

**Definition.** The **ring of entire functions** is
$$
\mathcal{O}(\mathbb{C}^2)=\{f:\mathbb{C}^2\to\mathbb{C}:f\text{ holomorphic}\},
$$
with pointwise addition and multiplication.

**Proposition (domain and units).** The ring $\mathcal{O}(\mathbb{C}^2)$ is an integral domain. Its group of units is
$$
\mathcal{O}(\mathbb{C}^2)^{\times}=\{e^g:g\in\mathcal{O}(\mathbb{C}^2)\}.
$$

*Proof.* A product of nonzero holomorphic functions is nonzero by the identity theorem, so there are no zero divisors. If $f$ is a unit, then $f$ never vanishes; the form $df/f$ is closed on $\mathbb{C}^2$, which is simply connected, so it has a primitive $g$ with $dg=df/f$, and $fe^{-g}$ is constant; hence $f=e^{g+c}$. The converse is immediate.

**Theorem (the evaluation ideals).** For every $a\in\mathbb{C}^2$ the set
$$
\mathfrak{m}_a=\{f\in\mathcal{O}(\mathbb{C}^2):f(a)=0\}
$$
is a maximal ideal with quotient $\mathcal{O}(\mathbb{C}^2)/\mathfrak{m}_a\cong\mathbb{C}$, the isomorphism being evaluation at $a$. Conversely, every maximal ideal of the polynomial ring $\mathbb{C}[z_1,z_2]$ is $\mathfrak{m}_a$ for a unique $a$, and the finitely generated maximal ideals of $\mathcal{O}(\mathbb{C}^2)$ are exactly the $\mathfrak{m}_a$.

*Proof.* The evaluation map is a surjective ring homomorphism with kernel $\mathfrak{m}_a$, so the quotient is $\mathbb{C}$ and the ideal is maximal; the point $a$ is recovered as the common zero set of the ideal. For the polynomial ring, the converse is the Hilbert Nullstellensatz. For $\mathcal{O}(\mathbb{C}^2)$, a finitely generated ideal with no common zero is the unit ideal by the holomorphic Nullstellensatz (*Several Complex Variables*); hence a finitely generated maximal ideal has a nonempty zero set, which must be a single point $a$, and the ideal is $\mathfrak{m}_a$. The ring has further maximal ideals, which are not finitely generated: the ideal of entire functions vanishing on a discrete set is proper, and a maximal ideal containing it is not an evaluation ideal.

**Proposition (not a principal ideal domain).** The ideal $\mathfrak{m}_0=(z_1,z_2)$ is not principal. Hence $\mathcal{O}(\mathbb{C}^2)$ is not a principal ideal domain.

*Proof.* Suppose $\mathfrak{m}_0=(g)$, so that $z_1=gh_1$ and $z_2=gh_2$. Evaluate $z_1=gh_1$ on the complex line $\{z_1=0\}$, a copy of $\mathbb{C}$: for every $z_2$,
$$
g(0,z_2)h_1(0,z_2)=0.
$$
The product of two entire functions of one variable is identically zero only when one factor is, so either $g$ or $h_1$ vanishes on the line. If $g(0,z_2)=0$ for all $z_2$, then $g$ is divisible by $z_1$, say $g=z_1q$; then $z_2=gh_2=z_1qh_2$ vanishes on the line, which is false. Hence $h_1(0,z_2)=0$ for all $z_2$, so $h_1=z_1q$ and $z_1=z_1gq$, which gives $1=gq$ because the ring is a domain. Then $g$ is a unit and $\mathfrak{m}_0$ is the whole ring, which is false because every element of $\mathfrak{m}_0$ vanishes at the origin and $1$ does not.

**Remark (the polynomial subring and the local ring).** The polynomial ring $\mathbb{C}[z_1,z_2]$ is a subring of $\mathcal{O}(\mathbb{C}^2)$, and its units are the nonzero constants, while the units of $\mathcal{O}(\mathbb{C}^2)$ are the exponentials $e^g$; the two rings share the evaluation ideals, but $\mathcal{O}(\mathbb{C}^2)$ has further maximal ideals, and their unit groups differ. The **local ring** at a point is the ring $\mathbb{C}\{z_1,z_2\}$ of convergent power series, a regular local ring of Krull dimension $2$ and, by the theorem of Auslander and Buchsbaum, a unique factorisation domain. **The global ring is neither a unique factorisation domain nor Noetherian**: the entire function $\sin(\pi z_1)$ is divisible by each of the pairwise non-associate primes $z_1-n$, $n\in\mathbb{Z}$, so it has no finite factorisation into irreducibles, and the infinitely many minimal primes over the principal ideal $(\sin\pi z_1)$ rule out the Noetherian property.

**Remark (the ideals and the geometry).** The passage from ideals to their common zero sets is the beginning of analytic geometry: a proper ideal defines a complex analytic subset, an ideal generated by one element defines a hypersurface, and the maximal ideals define the points. **The failure of the principal ideal property is the algebraic shadow of the codimension**: in $\mathbb{C}$ the maximal ideal at a point is generated by the single function $z-a$, while at the origin of $\mathbb{C}^2$ it needs the two functions $z_1$ and $z_2$.

## What Fails in Two Variables

**Five one-variable facts fail: singularities are never isolated, zeros are not isolated, the argument principle has no direct analogue, the Riemann mapping theorem fails, and the boundary is not a contour.**

**Theorem (Hartogs: no isolated singularities).** Let $D\subset\mathbb{C}^2$ be a domain and let $K\subset D$ be compact with $D\setminus K$ connected. Then every holomorphic function on $D\setminus K$ extends holomorphically to $D$. In particular, a function holomorphic on $\mathbb{C}^2\setminus\{0\}$ extends to $\mathbb{C}^2$.

*Proof.* This is the Hartogs extension theorem, proved in *Several Complex Variables* by the Hartogs figure and the iterated Cauchy formula. The complement of the origin is connected, so the corollary follows.

**Remark (the Laurent expansion disappears).** In one variable a function holomorphic on a punctured disc has a Laurent expansion with a possibly infinite negative part, and the negative part measures the singularity. **In two variables the punctured ball is not a domain of holomorphy**: every function on it extends, so there is no negative part and no classification of singularities by Laurent coefficients. A singularity can occur only along a complex hypersurface, and its local model is a pole transverse to the hypersurface, such as $1/z_1$ along $\{z_1=0\}$.

**Proposition (zeros are hypersurfaces).** If $f$ is holomorphic and not identically zero on a domain $D\subset\mathbb{C}^2$, then its zero set $Z(f)$ has empty interior. At every point where $df\neq0$, the set $Z(f)$ is a complex submanifold of complex dimension $1$.

*Proof.* The empty interior is the identity theorem. At a point with $df\neq0$, one of the partial derivatives, say $\partial f/\partial z_2$, is nonzero, and the holomorphic implicit function theorem solves $f(z_1,z_2)=0$ for $z_2=\varphi(z_1)$ near the point; the graph is a complex curve.

**Remark (the argument principle has no direct analogue).** In one variable the zeros of $f$ are isolated and the integral of $f'/f$ over a contour counts them. **In two variables the zeros form a complex curve, and the count is not a number but a divisor**, an integer attached to each irreducible component; the replacement of the contour integral is the theory of positive currents and Lelong numbers, which integrates the Poincaré–Lelong form of $\log\lvert f\rvert$ over a hypersurface (*Several Complex Variables*). The one-variable statement is recovered by restricting to a complex line that meets the zero curve transversely.

**Remark (the Riemann mapping theorem fails).** In one variable every simply connected proper domain of $\mathbb{C}$ is biholomorphic to the disc. **In two variables the ball and the bicylinder are both simply connected, bounded and contractible, and they are not biholomorphic**; the dimension of the automorphism group separates them (*The Ball and the Bicylinder in $\mathbb{C}^2$*).

**Remark (no holomorphic Cauchy kernel over the boundary).** The topological boundary of a bounded domain in $\mathbb{C}^2$ is a real three-manifold, while the holomorphic volume form $f\,dz_1\wedge dz_2$ is a $2$-form, which integrates over a real two-dimensional set. **The one-variable contour integral therefore has no direct analogue over the whole boundary**: the polydisc formula uses the two-dimensional distinguished boundary, and a general domain needs the Bochner–Martinelli kernel, which is a $3$-form and is not holomorphic.

**Proposition (a system of two equations need not have isolated zeros).** The holomorphic map $F(z_1,z_2)=(z_1,z_1)$ has the complex line $\{z_1=0\}$ as its zero set, and the holomorphic map $G(z_1,z_2)=(e^{z_1},z_2)$ has no zero at all.

*Proof.* $F(z)=0$ exactly when $z_1=0$, with $z_2$ free; $G(z)=0$ would require $e^{z_1}=0$, which never holds.

**Remark (the fundamental theorem of algebra fails for maps).** A nonconstant polynomial map $\mathbb{C}^2\to\mathbb{C}^2$ need not be surjective: the map $(z_1,z_2)\mapsto(z_1z_2,z_1)$ misses every point $(a,0)$ with $a\neq0$. **Bézout's theorem counts the intersections of two projective curves, not the zeros of a polynomial map of the affine plane**, and the affine count requires the compactification of *The Compactifications of $\mathbb{C}^2$*.

## Summary

A holomorphic function of two variables is a real differentiable function with a $\mathbb{C}$-linear differential, equivalently a solution of the two complex Cauchy–Riemann equations $\bar\partial_1f=\bar\partial_2f=0$, equivalently a convergent power series on every polydisc. The system is four real equations for two functions, hence overdetermined; the real and imaginary parts are harmonic, but a harmonic function has a conjugate only when it is pluriharmonic, and $\lvert z_1\rvert^2-\lvert z_2\rvert^2$ is the standard counterexample.

The maximum principle, Liouville's theorem and the identity theorem hold, and they are proved by restricting to complex lines. The Cauchy formula on the polydisc is the one-variable formula applied twice; it integrates over the distinguished boundary $T^2$, a real two-dimensional torus, and it yields the power series and the Cauchy estimates. The ring $\mathcal{O}(\mathbb{C}^2)$ is an integral domain; its units are the exponentials $e^g$, its maximal ideals are the evaluation ideals $\mathfrak{m}_a$, and it is not a principal ideal domain, the origin requiring the two generators $z_1,z_2$; it is neither a unique factorisation domain nor Noetherian, although the local ring $\mathbb{C}\{z_1,z_2\}$ is a regular local ring and a unique factorisation domain.

Five one-variable facts fail. There are no isolated singularities: a holomorphic function on the complement of a compact set with connected complement extends across it. The zeros are not isolated: they form a complex curve. The argument principle has no direct analogue: the zeros form a divisor, counted by a current. The Riemann mapping theorem fails: the ball and the bicylinder are not biholomorphic. And the boundary is not a contour: the Cauchy integral over the topological boundary has no holomorphic kernel, and the polydisc formula uses the torus instead.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $z=(z_1,z_2)$, $z_k=x_k+iy_k$ | a point of $\mathbb{C}^2$ and its real coordinates |
| $\partial/\partial z_k$, $\partial/\partial\bar z_k$ | the Wirtinger operators |
| $\bar\partial=\sum_k(\partial/\partial\bar z_k)\,d\bar z_k$ | the Cauchy–Riemann operator |
| $\Delta(a,r)=\{\lvert z_k-a_k\rvert<r_k\}$ | the polydisc of multiradius $r$ |
| $T(a,r)=\{\lvert z_k-a_k\rvert=r_k\}$ | the distinguished boundary, a torus |
| $\Delta=4\sum_k\partial^2/\partial z_k\partial\bar z_k$ | the Laplacian |
| pluriharmonic | $\partial^2u/\partial z_j\partial\bar z_k=0$ for all $j,k$ |
| $\mathcal{O}(\mathbb{C}^2)$ | the ring of entire functions |
| $\mathfrak{m}_a=\{f:f(a)=0\}$ | the maximal ideal at $a$ |
| $\mathbb{C}\{z_1,z_2\}$ | the local ring of convergent power series |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space, the coordinates and the Hermitian form.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-complex-two-space.html), for the real coordinates and the operators $\partial$ and $\bar\partial$.
- [The Ball and the Bicylinder in $\mathbb{C}^2$](the-ball-and-the-bicylinder.html), the next article, for the model domains and the failure of the Riemann mapping theorem.
- [The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$](the-dbar-problem-and-the-bochner-martinelli-integral.html), for the inhomogeneous equation and the boundary kernel.
- [Harmonic Analysis on $\mathbb{C}^2$](harmonic-analysis-on-the-complex-two-space.html), for the Fourier and Radon transforms and the Laplacian.
- [Several Complex Variables](several-complex-variables.html), for the general theory, the Hartogs phenomenon, domains of holomorphy and the Weierstrass preparation theorem.
- [Complex Analysis](complex-analysis.html), for the one-variable Cauchy theory, the maximum principle and the argument principle.
- [Differential Forms and Stokes' Theorem](differential-forms-and-stokes-theorem.html), for the operators $\partial$ and $\bar\partial$ and the integration of forms.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs and the typographic conventions of the corpus.
