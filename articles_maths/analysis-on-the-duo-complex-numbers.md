# __Analysis on $\mathbb{C}^2$__

## Introduction

This article treats the analysis of holomorphic functions of two complex variables on the space $\mathbb{C}^2$ itself: the Cauchy–Riemann equations, the ring of entire functions, the maximum principle, the identity theorem, the iterated Cauchy formula on the polydisc, and the one-variable facts that fail. It is the first of the four analytical articles of the category; the model domains are *The Ball and the Bicylinder in $\mathbb{C}^2$*, the inhomogeneous Cauchy–Riemann equation is *The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$*, and the Fourier and Radon analysis is *Harmonic Analysis on $\mathbb{C}^2$*.

The general theory of holomorphic functions of $n$ variables, of domains of holomorphy, of pseudoconvexity and of the Cousin problems is *Several Complex Variables*. That article develops the theory for a variable number of variables and for arbitrary domains; this one fixes the space $\mathbb{C}^2$ and the functions defined on all of it, and it states what the case of two variables adds to the one-variable theory of *Complex Analysis*. The differential forms and the operators $\partial$ and $\bar\partial$ are from *Differential Forms and Stokes' Theorem*, and the notation is that of *Duo-Complex Numbers*: a point is $Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the Hermitian form is $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$, and the polydisc of multiradius $r=(r_1,r_2)$ about $Q_0$ is
$$
\Delta(Q_0,r)=\{Q:\lvert Q_{\blacktriangle}-Q_{0\blacktriangle}\rvert<r_1,\ \lvert Q_{\blacktriangledown}-Q_{0\blacktriangledown}\rvert<r_2\}.
$$

**The analysis of $\mathbb{C}^2$ is not the one-variable theory twice.** Three things change. The Cauchy–Riemann system becomes overdetermined, so holomorphic functions are rigid and a harmonic function need not have a conjugate. The zeros and the singularities cease to be isolated, so the argument principle and the Laurent expansion have no direct analogues. And the boundary of a domain is odd-dimensional, so the Cauchy integral over a contour is replaced by an iterated integral over a torus or by a kernel that is not holomorphic. Everything that survives survives for the same reason: it is a one-variable statement applied on complex lines.

## Holomorphic Functions of Two Variables

**A holomorphic function of two variables is a real differentiable function whose differential is complex-linear at every point; equivalently, it satisfies the two Cauchy–Riemann equations $\bar\partial_{\blacktriangle}f=\bar\partial_{\blacktriangledown}f=0$.**

**Definition.** Let $D\subset\mathbb{C}^2$ be a domain. A function $f:D\to\mathbb{C}$ is **holomorphic** when it is real differentiable at every point of $D$ and its differential $df(Q)$ is $\mathbb{C}$-linear for every $Q\in D$. The **Wirtinger operators** are
$$
\frac{\partial}{\partial Q_{\blacktriangle}}=\frac12\left(\frac{\partial}{\partial q_{\blacktriangle}}-i\frac{\partial}{\partial q'_{\blacktriangle}}\right),\qquad
\frac{\partial}{\partial\overline{Q}_{\blacktriangle}}=\frac12\left(\frac{\partial}{\partial q_{\blacktriangle}}+i\frac{\partial}{\partial q'_{\blacktriangle}}\right),
$$
and the same formulas with the descending triangle, and the **Cauchy–Riemann operator** is
$$
\bar\partial f=\frac{\partial f}{\partial\overline{Q}_{\blacktriangle}}\,d\overline{Q}_{\blacktriangle}+\frac{\partial f}{\partial\overline{Q}_{\blacktriangledown}}\,d\overline{Q}_{\blacktriangledown}.
$$

**Proposition (the Cauchy–Riemann equations).** A real differentiable function $f=u+iv$ on $D$ is holomorphic exactly when
$$
\frac{\partial f}{\partial\overline{Q}_{\blacktriangle}}=0,\qquad \frac{\partial f}{\partial\overline{Q}_{\blacktriangledown}}=0,
$$
that is, exactly when the four real equations
$$
\frac{\partial u}{\partial q_{\blacktriangle}}=\frac{\partial v}{\partial q'_{\blacktriangle}},\qquad
\frac{\partial u}{\partial q'_{\blacktriangle}}=-\frac{\partial v}{\partial q_{\blacktriangle}},\qquad
\frac{\partial u}{\partial q_{\blacktriangledown}}=\frac{\partial v}{\partial q'_{\blacktriangledown}},\qquad
\frac{\partial u}{\partial q'_{\blacktriangledown}}=-\frac{\partial v}{\partial q_{\blacktriangledown}}
$$
hold on $D$.

*Proof.* The differential is
$$
df=\frac{\partial f}{\partial Q_{\blacktriangle}}dQ_{\blacktriangle}+\frac{\partial f}{\partial\overline{Q}_{\blacktriangle}}d\overline{Q}_{\blacktriangle}
+\frac{\partial f}{\partial Q_{\blacktriangledown}}dQ_{\blacktriangledown}+\frac{\partial f}{\partial\overline{Q}_{\blacktriangledown}}d\overline{Q}_{\blacktriangledown},
$$
and it is $\mathbb{C}$-linear exactly when the coefficients of the anti-holomorphic differentials $d\overline{Q}_{\blacktriangle}$ and $d\overline{Q}_{\blacktriangledown}$ vanish. The real form of the two complex equations is the displayed system, obtained by separating $f=u+iv$ into real and imaginary parts.

**Remark (the count of the equations).** In one variable the Cauchy–Riemann system is two real equations for the two functions $u$ and $v$, and it is determined. **In two variables it is four real equations for two functions, and it is overdetermined.** The overdetermination is not a defect of the presentation: it is the source of the rigidity of the theory, and it is the reason a harmonic function of two variables need not have a harmonic conjugate.

**Theorem (the power series).** A function $f$ on the polydisc $\Delta(Q_0,r)$ is holomorphic if and only if it is the sum of a power series
$$
f(Q)=\sum_{\alpha\in\mathbb{N}^2}c_\alpha(Q-Q_0)^\alpha,\qquad c_\alpha=\frac{1}{\alpha!}\,\frac{\partial^{\lvert\alpha\rvert}f}{\partial Q^\alpha}(Q_0),
$$
convergent absolutely and uniformly on every compact subset of $\Delta(Q_0,r)$.

*Proof.* A convergent power series is holomorphic, because it is holomorphic in each variable and the derivative of a uniformly convergent series may be taken term by term. Conversely, the iterated Cauchy formula of the section below represents a holomorphic function as an integral over the distinguished boundary of a smaller polydisc; expanding each Cauchy factor as a geometric series gives the coefficients and the convergence.

**Proposition (the complex Jacobian and the real Jacobian).** Let $f=(f_1,f_2)$ be holomorphic on $D$ and let
$$
J_f=\begin{pmatrix}\partial f_1/\partial Q_{\blacktriangle}&\partial f_1/\partial Q_{\blacktriangledown}\\ \partial f_2/\partial Q_{\blacktriangle}&\partial f_2/\partial Q_{\blacktriangledown}\end{pmatrix}
$$
be its complex Jacobian. Then $f$ is real differentiable, and its real Jacobian determinant is
$$
\det J_{\mathbb{R}}f=\lvert\det J_f\rvert^2.
$$
In particular $f$ is a local biholomorphism at $Q_0$ exactly when $\det J_f(Q_0)\neq0$.

*Proof.* Write $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ and read the real Jacobian as a block matrix $\begin{pmatrix}A&-B\\B&A\end{pmatrix}$, where $A$ and $B$ are the real and imaginary parts of $J_f$. The determinant of such a block matrix is $\lvert\det(A+iB)\rvert^2=\lvert\det J_f\rvert^2$. The inverse function theorem applied to the real map, together with the $\mathbb{C}$-linearity of the differential, gives the local biholomorphism.

## The Cauchy–Riemann Equations and Harmonicity

**The real and imaginary parts of a holomorphic function are harmonic, but the converse fails: a harmonic function has a conjugate only when it is pluriharmonic.**

**Definition.** The **Laplacian** on $\mathbb{C}^2$ is
$$
\Delta=\frac{\partial^2}{\partial q_{\blacktriangle}^2}+\frac{\partial^2}{\partial q'^2_{\blacktriangle}}+\frac{\partial^2}{\partial q_{\blacktriangledown}^2}+\frac{\partial^2}{\partial q'^2_{\blacktriangledown}}
=4\left(\frac{\partial^2}{\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}}+\frac{\partial^2}{\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangledown}}\right).
$$
A $C^2$ function is **harmonic** when $\Delta u=0$.

**Proposition (holomorphic implies harmonic).** If $f=u+iv$ is holomorphic on $D$, then $u$ and $v$ are harmonic on $D$.

*Proof.* From the Cauchy–Riemann equations, $\partial u/\partial q_{\blacktriangle}=\partial v/\partial q'_{\blacktriangle}$ and $\partial u/\partial q'_{\blacktriangle}=-\partial v/\partial q_{\blacktriangle}$, and the same with the descending triangle. Differentiating the first equation in $q_{\blacktriangle}$ and the second in $q'_{\blacktriangle}$ and adding gives
$$
\frac{\partial^2u}{\partial q_{\blacktriangle}^2}+\frac{\partial^2u}{\partial q'^2_{\blacktriangle}}
=\frac{\partial^2v}{\partial q_{\blacktriangle}\partial q'_{\blacktriangle}}-\frac{\partial^2v}{\partial q'_{\blacktriangle}\partial q_{\blacktriangle}}=0,
$$
because the mixed partials commute. The same computation with the descending triangle, added to this one, gives $\Delta u=0$; exchanging $u$ and $v$ gives $\Delta v=0$.

**Definition.** A $C^2$ function $u$ is **pluriharmonic** when its restriction to every complex line is harmonic, equivalently when all four mixed derivatives vanish:
$$
\frac{\partial^2u}{\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}}
=\frac{\partial^2u}{\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangledown}}
=\frac{\partial^2u}{\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangle}}
=\frac{\partial^2u}{\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangledown}}=0.
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

**Remark (harmonic against pluriharmonic).** Every pluriharmonic function is harmonic, because $\Delta=4(\partial^2/\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}+\partial^2/\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangledown})$ is the trace of the Hermitian matrix of the four mixed derivatives. **The converse fails**: the function
$$
u(Q)=\lvert Q_{\blacktriangle}\rvert^2-\lvert Q_{\blacktriangledown}\rvert^2
$$
is harmonic, since the Laplacians of the two terms cancel, but
$$
\frac{\partial^2u}{\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}}=1\neq0,
$$
so $u$ is not pluriharmonic and has no conjugate. **This is the first one-variable fact that fails in two variables**: in the plane every harmonic function on a simply connected domain has a harmonic conjugate.

## The Maximum Principle and the Identity Theorem

**The maximum modulus principle and the identity theorem hold in two variables, and both are proved by restricting the function to complex lines.**

**Theorem (the maximum principle).** Let $D\subset\mathbb{C}^2$ be a domain and let $f$ be holomorphic on $D$. If $\lvert f\rvert$ attains a local maximum at a point of $D$, then $f$ is constant on $D$. If $D$ is bounded and $f$ is continuous on $\overline{D}$, then
$$
\max_{\overline{D}}\lvert f\rvert=\max_{\partial D}\lvert f\rvert.
$$

*Proof.* Suppose $\lvert f\rvert$ has a local maximum at $Q_0\in D$. For every direction $V\in\mathbb{C}^2$, the function $\lambda\mapsto f(Q_0+\lambda V)$ is holomorphic on a disc about $0$, and its modulus has a maximum at $0$; the one-variable maximum principle gives $f(Q_0+\lambda V)=f(Q_0)$ for $\lvert\lambda\rvert$ small. The differential of $f$ at $Q_0$ therefore vanishes, and, varying $V$, $f$ is constant on a neighbourhood of $Q_0$. The identity theorem below extends the constancy to $D$. The boundary statement follows: a maximum on $\overline{D}$ is either on $\partial D$ or at an interior point, where $f$ is constant and the two maxima agree.

**Corollary (Liouville).** A bounded holomorphic function on $\mathbb{C}^2$ is constant.

*Proof.* Fix $Q_0\in\mathbb{C}^2$. For every direction $V\in\mathbb{C}^2$, the function $\lambda\mapsto f(Q_0+\lambda V)$ is entire and bounded, hence constant by the one-variable Liouville theorem. Varying $V$ and using the identity theorem, $f$ is constant on $\mathbb{C}^2$.

**Theorem (the identity theorem).** Let $D\subset\mathbb{C}^2$ be a domain and let $f$ be holomorphic on $D$. If $f$ vanishes on a nonempty open subset of $D$, then $f\equiv0$ on $D$. Equivalently, if $f$ is not identically zero, its zero set has empty interior.

*Proof.* Let $S$ be the set of points at which $f$ and all its partial derivatives vanish. The set $S$ is closed, because the derivatives are continuous, and it is open, because at a point of $S$ the power series of $f$ has all coefficients zero and therefore vanishes on a polydisc about the point. A nonempty open subset on which $f$ vanishes is contained in $S$, so $S$ is nonempty; a nonempty subset of a domain that is open and closed is the whole domain, and $f=0$ there.

**Remark (what survives and what does not).** The maximum principle, the identity theorem and Liouville's theorem survive, because each is a one-variable statement applied on the complex lines through a point. **The statements that fail are those that count zeros or describe a singularity**, and they fail because the zero set and the singular set are no longer discrete. The one-variable form of the identity theorem, in which an accumulation point of the zero set suffices, also fails: the function $f(Q_{\blacktriangle},Q_{\blacktriangledown})=Q_{\blacktriangle}$ vanishes on the complex line $\{Q_{\blacktriangle}=0\}$, which has accumulation points, and is not identically zero.

## The Iterated Cauchy Formula on the Polydisc

**The Cauchy formula on a polydisc is the one-variable formula applied twice; it integrates over the distinguished boundary, a real two-dimensional torus, and not over the topological boundary.**

**Definition.** The **distinguished boundary** of the polydisc $\Delta(Q_0,r)$ is the torus
$$
T(Q_0,r)=\{Q:\lvert Q_{\blacktriangle}-Q_{0\blacktriangle}\rvert=r_1,\ \lvert Q_{\blacktriangledown}-Q_{0\blacktriangledown}\rvert=r_2\},
$$
oriented by the increasing arguments of $Q_{\blacktriangle}-Q_{0\blacktriangle}$ and $Q_{\blacktriangledown}-Q_{0\blacktriangledown}$.

**Theorem (the iterated Cauchy formula).** Let $f$ be holomorphic on a neighbourhood of the closed polydisc $\overline{\Delta(Q_0,r)}$. Then for every $Q\in\Delta(Q_0,r)$,
$$
f(Q)=\frac{1}{(2\pi i)^2}\int_{T(Q_0,r)}\frac{f(\zeta)}{(\zeta_{\blacktriangle}-Q_{\blacktriangle})(\zeta_{\blacktriangledown}-Q_{\blacktriangledown})}\,d\zeta_{\blacktriangledown}\,d\zeta_{\blacktriangle}.
$$

*Proof.* For fixed $Q_{\blacktriangle}$ with $\lvert Q_{\blacktriangle}-Q_{0\blacktriangle}\rvert<r_1$, the function $\zeta_{\blacktriangledown}\mapsto f(Q_{\blacktriangle},\zeta_{\blacktriangledown})$ is holomorphic near the closed disc $\lvert\zeta_{\blacktriangledown}-Q_{0\blacktriangledown}\rvert\le r_2$, so the one-variable Cauchy formula gives
$$
f(Q_{\blacktriangle},Q_{\blacktriangledown})=\frac{1}{2\pi i}\int_{\lvert\zeta_{\blacktriangledown}-Q_{0\blacktriangledown}\rvert=r_2}\frac{f(Q_{\blacktriangle},\zeta_{\blacktriangledown})}{\zeta_{\blacktriangledown}-Q_{\blacktriangledown}}\,d\zeta_{\blacktriangledown}.
$$
The integrand is holomorphic in $Q_{\blacktriangle}$ near $\lvert Q_{\blacktriangle}-Q_{0\blacktriangle}\rvert\le r_1$, uniformly in $\zeta_{\blacktriangledown}$, so the one-variable formula applies again in the first variable:
$$
f(Q_{\blacktriangle},\zeta_{\blacktriangledown})=\frac{1}{2\pi i}\int_{\lvert\zeta_{\blacktriangle}-Q_{0\blacktriangle}\rvert=r_1}\frac{f(\zeta_{\blacktriangle},\zeta_{\blacktriangledown})}{\zeta_{\blacktriangle}-Q_{\blacktriangle}}\,d\zeta_{\blacktriangle}.
$$
Substituting and using Fubini gives the display.

**Corollary (Cauchy estimates).** If $\lvert f\rvert\le M$ on $T(Q_0,r)$, then the coefficients of the power series of $f$ about $Q_0$ satisfy
$$
\lvert c_\alpha\rvert\le M\,r^{-\alpha}=M\,r_1^{-\alpha_1}r_2^{-\alpha_2}.
$$

*Proof.* Differentiate the integral formula under the sign, or bound the coefficients $c_\alpha$ obtained by expanding the Cauchy factors; the modulus of the denominator is $r_1^{\alpha_1+1}r_2^{\alpha_2+1}$ on the torus.

**Corollary (holomorphic implies analytic).** A holomorphic function on a domain is real analytic, and its power series about a point converges on every polydisc about that point whose closure lies in the domain.

*Proof.* The formula gives the power series on every polydisc whose closure lies in the domain; the union of those polydiscs is the domain.

**Theorem (Weierstrass and Montel).** A sequence of holomorphic functions on a domain that converges uniformly on every compact subset has a holomorphic limit, and so do all its derivatives. A locally bounded family of holomorphic functions is normal.

*Proof.* The Cauchy estimates bound the derivatives uniformly on compact sets, so the sequence is equicontinuous and the limit is holomorphic by Morera's theorem applied on polydiscs; Montel's theorem follows from the Arzelà–Ascoli theorem and the Cauchy estimates.

**Remark (the dimension of the boundary).** The polydisc has real dimension $4$, its topological boundary has real dimension $3$, and its distinguished boundary $T(Q_0,r)$ has real dimension $2$. **The Cauchy formula integrates over the two-dimensional torus, not over the three-dimensional boundary**, and the torus is the set on which both Cauchy factors are simultaneously non-singular. For a general domain there is no distinguished boundary of this product form, and the replacement is the Bochner–Martinelli kernel of *The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$*, which integrates over the full boundary and is not holomorphic in $Q$.

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

**Theorem (the evaluation ideals).** For every $Q_0\in\mathbb{C}^2$ the set
$$
\mathfrak{m}_{Q_0}=\{f\in\mathcal{O}(\mathbb{C}^2):f(Q_0)=0\}
$$
is a maximal ideal with quotient $\mathcal{O}(\mathbb{C}^2)/\mathfrak{m}_{Q_0}\cong\mathbb{C}$, the isomorphism being evaluation at $Q_0$. Conversely, every maximal ideal of the polynomial ring $\mathbb{C}[Q_{\blacktriangle},Q_{\blacktriangledown}]$ is $\mathfrak{m}_{Q_0}$ for a unique $Q_0$, and the finitely generated maximal ideals of $\mathcal{O}(\mathbb{C}^2)$ are exactly the $\mathfrak{m}_{Q_0}$.

*Proof.* The evaluation map is a surjective ring homomorphism with kernel $\mathfrak{m}_{Q_0}$, so the quotient is $\mathbb{C}$ and the ideal is maximal; the point $Q_0$ is recovered as the common zero set of the ideal. For the polynomial ring, the converse is the Hilbert Nullstellensatz. For $\mathcal{O}(\mathbb{C}^2)$, a finitely generated ideal with no common zero is the unit ideal by the holomorphic Nullstellensatz (*Several Complex Variables*); hence a finitely generated maximal ideal has a nonempty zero set, which must be a single point $Q_0$, and the ideal is $\mathfrak{m}_{Q_0}$. The ring has further maximal ideals, and they are not finitely generated; the general theory is *Several Complex Variables*.

**Proposition (not a principal ideal domain).** The ideal $\mathfrak{m}_0=(Q_{\blacktriangle},Q_{\blacktriangledown})$ is not principal. Hence $\mathcal{O}(\mathbb{C}^2)$ is not a principal ideal domain.

*Proof.* Suppose $\mathfrak{m}_0=(g)$, so that $Q_{\blacktriangle}=gh_1$ and $Q_{\blacktriangledown}=gh_2$. Evaluate $Q_{\blacktriangle}=gh_1$ on the complex line $\{Q_{\blacktriangle}=0\}$, a copy of $\mathbb{C}$: for every $Q_{\blacktriangledown}$,
$$
g(0,Q_{\blacktriangledown})h_1(0,Q_{\blacktriangledown})=0.
$$
The product of two entire functions of one variable is identically zero only when one factor is, so either $g$ or $h_1$ vanishes on the line. If $g(0,Q_{\blacktriangledown})=0$ for all $Q_{\blacktriangledown}$, then $g$ is divisible by $Q_{\blacktriangle}$, say $g=Q_{\blacktriangle}q$; then $Q_{\blacktriangledown}=gh_2=Q_{\blacktriangle}qh_2$ vanishes on the line, which is false. Hence $h_1(0,Q_{\blacktriangledown})=0$ for all $Q_{\blacktriangledown}$, so $h_1=Q_{\blacktriangle}q$ and $Q_{\blacktriangle}=Q_{\blacktriangle}gq$, which gives $1=gq$ because the ring is a domain. Then $g$ is a unit and $\mathfrak{m}_0$ is the whole ring, which is false because every element of $\mathfrak{m}_0$ vanishes at the origin and $1$ does not.

**Remark (the polynomial subring and the local ring).** The polynomial ring $\mathbb{C}[Q_{\blacktriangle},Q_{\blacktriangledown}]$ is a subring of $\mathcal{O}(\mathbb{C}^2)$, and its units are the nonzero constants, while the units of $\mathcal{O}(\mathbb{C}^2)$ are the exponentials $e^g$; the two rings share the evaluation ideals, but $\mathcal{O}(\mathbb{C}^2)$ has further maximal ideals, and their unit groups differ. The **local ring** at a point is the ring $\mathbb{C}\{Q_{\blacktriangle},Q_{\blacktriangledown}\}$ of convergent power series, a regular local ring of Krull dimension $2$ and, by the theorem of Auslander and Buchsbaum, a unique factorisation domain. **The global ring is neither a unique factorisation domain nor Noetherian**: the entire function $\sin(\pi Q_{\blacktriangle})$ is divisible by each of the pairwise non-associate primes $Q_{\blacktriangle}-n$, $n\in\mathbb{Z}$, so it has no finite factorisation into irreducibles, and the infinitely many minimal primes over the principal ideal $(\sin\pi Q_{\blacktriangle})$ rule out the Noetherian property.

**Remark (the ideals and the geometry).** The passage from ideals to their common zero sets is the beginning of analytic geometry: a proper ideal defines a complex analytic subset, an ideal generated by one element defines a hypersurface, and the maximal ideals define the points. **The failure of the principal ideal property is the algebraic shadow of the codimension**: in $\mathbb{C}$ the maximal ideal at a point is generated by the single function $Q-Q_0$, while at the origin of $\mathbb{C}^2$ it needs the two functions $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$.

## What Fails in Two Variables

**Five one-variable facts fail: singularities are never isolated, zeros are not isolated, the argument principle has no direct analogue, the Riemann mapping theorem fails, and the boundary is not a contour.**

**Theorem (Hartogs: no isolated singularities).** Let $D\subset\mathbb{C}^2$ be a domain and let $K\subset D$ be compact with $D\setminus K$ connected. Then every holomorphic function on $D\setminus K$ extends holomorphically to $D$. In particular, a function holomorphic on $\mathbb{C}^2\setminus\{0\}$ extends to $\mathbb{C}^2$.

*Proof.* This is the Hartogs extension theorem, proved in *Several Complex Variables* by the Hartogs figure and the iterated Cauchy formula. The complement of the origin is connected, so the corollary follows.

**Remark (the Laurent expansion disappears).** In one variable a function holomorphic on a punctured disc has a Laurent expansion with a possibly infinite negative part, and the negative part measures the singularity. **In two variables the punctured ball is not a domain of holomorphy**: every function on it extends, so there is no negative part and no classification of singularities by Laurent coefficients. A singularity can occur only along a complex hypersurface, and its local model is a pole transverse to the hypersurface, such as $1/Q_{\blacktriangle}$ along $\{Q_{\blacktriangle}=0\}$.

**Proposition (zeros are hypersurfaces).** If $f$ is holomorphic and not identically zero on a domain $D\subset\mathbb{C}^2$, then its zero set $Z(f)$ has empty interior. At every point where $df\neq0$, the set $Z(f)$ is a complex submanifold of complex dimension $1$.

*Proof.* The empty interior is the identity theorem. At a point with $df\neq0$, one of the partial derivatives, say $\partial f/\partial Q_{\blacktriangledown}$, is nonzero, and the holomorphic implicit function theorem solves $f(Q_{\blacktriangle},Q_{\blacktriangledown})=0$ for $Q_{\blacktriangledown}=\varphi(Q_{\blacktriangle})$ near the point; the graph is a complex curve.

**Remark (the argument principle has no direct analogue).** In one variable the zeros of $f$ are isolated and the integral of $f'/f$ over a contour counts them. **In two variables the zeros form a complex curve, and the count is not a number but a divisor**, an integer attached to each irreducible component; the replacement of the contour integral is the theory of positive currents and Lelong numbers, which integrates the Poincaré–Lelong form of $\log\lvert f\rvert$ over a hypersurface (*Several Complex Variables*). The one-variable statement is recovered by restricting to a complex line that meets the zero curve transversely.

**Remark (the Riemann mapping theorem fails).** In one variable every simply connected proper domain of $\mathbb{C}$ is biholomorphic to the disc. **In two variables the ball and the bicylinder are both simply connected, bounded and contractible, and they are not biholomorphic**; the dimension of the automorphism group separates them (*The Ball and the Bicylinder in $\mathbb{C}^2$*).

**Remark (no holomorphic Cauchy kernel over the boundary).** The topological boundary of a bounded domain in $\mathbb{C}^2$ is a real three-manifold, while the holomorphic volume form $f\,dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}$ is a $2$-form, which integrates over a real two-dimensional set. **The one-variable contour integral therefore has no direct analogue over the whole boundary**: the polydisc formula uses the two-dimensional distinguished boundary, and a general domain needs the Bochner–Martinelli kernel, which is a $3$-form and is not holomorphic.

**Proposition (a system of two equations need not have isolated zeros).** The holomorphic map $F(Q_{\blacktriangle},Q_{\blacktriangledown})=(Q_{\blacktriangle},Q_{\blacktriangle})$ has the complex line $\{Q_{\blacktriangle}=0\}$ as its zero set, and the holomorphic map $G(Q_{\blacktriangle},Q_{\blacktriangledown})=(e^{Q_{\blacktriangle}},Q_{\blacktriangledown})$ has no zero at all.

*Proof.* $F(Q)=0$ exactly when $Q_{\blacktriangle}=0$, with $Q_{\blacktriangledown}$ free; $G(Q)=0$ would require $e^{Q_{\blacktriangle}}=0$, which never holds.

**Remark (the fundamental theorem of algebra fails for maps).** A nonconstant polynomial map $\mathbb{C}^2\to\mathbb{C}^2$ need not be surjective: the map $(Q_{\blacktriangle},Q_{\blacktriangledown})\mapsto(Q_{\blacktriangle}Q_{\blacktriangledown},Q_{\blacktriangle})$ misses every point $(Q_{0\blacktriangle},0)$ with $Q_{0\blacktriangle}\neq0$. **Bézout's theorem counts the intersections of two projective curves, not the zeros of a polynomial map of the affine plane**, and the affine count requires the compactification of *The Compactifications of $\mathbb{C}^2$*.

## Summary

A holomorphic function of two variables is a real differentiable function with a $\mathbb{C}$-linear differential, equivalently a solution of the two complex Cauchy–Riemann equations $\bar\partial_{\blacktriangle}f=\bar\partial_{\blacktriangledown}f=0$, equivalently a convergent power series on every polydisc. The system is four real equations for two functions, hence overdetermined; the real and imaginary parts are harmonic, but a harmonic function has a conjugate only when it is pluriharmonic, and $\lvert Q_{\blacktriangle}\rvert^2-\lvert Q_{\blacktriangledown}\rvert^2$ is the standard counterexample.

The maximum principle, Liouville's theorem and the identity theorem hold, and they are proved by restricting to complex lines. The Cauchy formula on the polydisc is the one-variable formula applied twice; it integrates over the distinguished boundary $T(Q_0,r)$, a real two-dimensional torus, and it yields the power series and the Cauchy estimates. The ring $\mathcal{O}(\mathbb{C}^2)$ is an integral domain; its units are the exponentials $e^g$, its maximal ideals are the evaluation ideals $\mathfrak{m}_{Q_0}$, and it is not a principal ideal domain, the origin requiring the two generators $Q_{\blacktriangle},Q_{\blacktriangledown}$; it is neither a unique factorisation domain nor Noetherian, although the local ring $\mathbb{C}\{Q_{\blacktriangle},Q_{\blacktriangledown}\}$ is a regular local ring and a unique factorisation domain.

Five one-variable facts fail. There are no isolated singularities: a holomorphic function on the complement of a compact set with connected complement extends across it. The zeros are not isolated: they form a complex curve. The argument principle has no direct analogue: the zeros form a divisor, counted by a current. The Riemann mapping theorem fails: the ball and the bicylinder are not biholomorphic. And the boundary is not a contour: the Cauchy integral over the topological boundary has no holomorphic kernel, and the polydisc formula uses the torus instead.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ | a point of $\mathbb{C}^2$ and its real coordinates |
| $\partial/\partial Q_{\blacktriangle}$, $\partial/\partial\overline{Q}_{\blacktriangle}$ | the Wirtinger operators |
| $\bar\partial=(\partial/\partial\overline{Q}_{\blacktriangle})\,d\overline{Q}_{\blacktriangle}+(\partial/\partial\overline{Q}_{\blacktriangledown})\,d\overline{Q}_{\blacktriangledown}$ | the Cauchy–Riemann operator |
| $\Delta(Q_0,r)=\{\lvert Q_{\blacktriangle}-Q_{0\blacktriangle}\rvert<r_1,\ \lvert Q_{\blacktriangledown}-Q_{0\blacktriangledown}\rvert<r_2\}$ | the polydisc of multiradius $r$ |
| $T(Q_0,r)=\{\lvert Q_{\blacktriangle}-Q_{0\blacktriangle}\rvert=r_1,\ \lvert Q_{\blacktriangledown}-Q_{0\blacktriangledown}\rvert=r_2\}$ | the distinguished boundary, a torus |
| $\Delta=4(\partial^2/\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}+\partial^2/\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangledown})$ | the Laplacian |
| pluriharmonic | the four mixed derivatives $\partial^2u/\partial Q\partial\overline{Q}$ vanish |
| $\mathcal{O}(\mathbb{C}^2)$ | the ring of entire functions |
| $\mathfrak{m}_{Q_0}=\{f:f(Q_0)=0\}$ | the maximal ideal at $Q_0$ |
| $\mathbb{C}\{Q_{\blacktriangle},Q_{\blacktriangledown}\}$ | the local ring of convergent power series |

## Further Reading

- [Duo-Complex Numbers](the-duo-complex-numbers.html), for the space, the coordinates and the Hermitian form.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-duo-complex-numbers.html), for the real coordinates and the operators $\partial$ and $\bar\partial$.
- [The Ball and the Bicylinder in $\mathbb{C}^2$](the-ball-and-the-bicylinder.html), the next article, for the model domains and the failure of the Riemann mapping theorem.
- [The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$](the-dbar-problem-and-the-bochner-martinelli-integral.html), for the inhomogeneous equation and the boundary kernel.
- [Harmonic Analysis on $\mathbb{C}^2$](harmonic-analysis-on-the-duo-complex-numbers.html), for the Fourier and Radon transforms and the Laplacian.
- [Several Complex Variables](several-complex-variables.html), for the general theory, the Hartogs phenomenon, domains of holomorphy and the Weierstrass preparation theorem.
- [Complex Analysis](complex-analysis.html), for the one-variable Cauchy theory, the maximum principle and the argument principle.
- [Differential Forms and Stokes' Theorem](differential-forms-and-stokes-theorem.html), for the operators $\partial$ and $\bar\partial$ and the integration of forms.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs and the typographic conventions of the corpus.
