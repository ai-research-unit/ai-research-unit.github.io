# __The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$__

## Introduction

The inhomogeneous Cauchy–Riemann equation on a domain $D\subset\mathbb{C}^2$ is
$$
\bar\partial u=g,
$$
where $g$ is a $(0,1)$-form and $u$ is a function. In one variable the equation is solved by the Cauchy–Green integral, and its solvability is governed by the single integrability condition $\bar\partial g=0$. In two variables the equation is a system of two equations for one unknown, the integrability condition is again $\bar\partial g=0$, and the solution exists on every polydisc and on the whole space $\mathbb{C}^2$. The solution is not given by a holomorphic kernel: it is given by the **Bochner–Martinelli kernel**, a $(2,1)$-form whose denominator is the fourth power of the distance and which integrates over the full three-dimensional boundary.

This article treats the $(p,q)$-forms and the Dolbeault complex, the $\bar\partial$-Poincaré lemma on the polydisc, the Bochner–Martinelli kernel and its formula, the jump formula across the boundary, the Hartogs extension theorem as an application, and the vanishing of the Dolbeault cohomology of $\mathbb{C}^2$. The analysis of holomorphic functions is *Analysis on $\mathbb{C}^2$*; the model domains are *The Ball and the Bicylinder in $\mathbb{C}^2$*; the general theory of the $\bar\partial$-equation, of domains of holomorphy and of Stein manifolds is *Several Complex Variables*; and the differential forms are from *Differential Forms and Stokes' Theorem*.

**The $\bar\partial$-problem on $\mathbb{C}^2$ is always solvable, and the solution is not unique.** The obstruction of one variable, the singularities of the domain, disappears because $\mathbb{C}^2$ is a domain of holomorphy; the non-uniqueness is the addition of an arbitrary holomorphic function. The Bochner–Martinelli kernel makes both statements effective: it solves the equation with a boundary integral and it exhibits the jump that measures the failure of the boundary values to be holomorphic.

## Forms of Type $(p,q)$

**On $\mathbb{C}^2$ the complexified exterior algebra splits by bidegree, and the operator $\bar\partial$ raises the second degree by one and squares to zero.**

**Definition.** Let $D\subset\mathbb{C}^2$ be open. A **form of type $(p,q)$** on $D$ is a sum of terms
$$
f\,dz_{i_1}\wedge\cdots\wedge dz_{i_p}\wedge d\bar z_{j_1}\wedge\cdots\wedge d\bar z_{j_q},\qquad 1\le i_1<\cdots<i_p\le2,\quad 1\le j_1<\cdots<j_q\le2,
$$
with $f\in C^\infty(D)$. The space of such forms is $\Omega^{p,q}(D)$, and
$$
\Omega^{m}(D)=\bigoplus_{p+q=m}\Omega^{p,q}(D).
$$

**Proposition (the dimensions).** The dimension of $\Omega^{p,q}$ at a point is
$$
\binom{2}{p}\binom{2}{q}.
$$
In particular the nontrivial types are
$$
\Omega^{0,0},\ \Omega^{1,0},\ \Omega^{0,1},\ \Omega^{1,1},\ \Omega^{2,0},\ \Omega^{0,2},\ \Omega^{2,1},\ \Omega^{1,2},\ \Omega^{2,2},
$$
of dimensions $1,2,2,4,1,1,2,2,1$.

*Proof.* A $(p,q)$-form is determined by the choice of $p$ holomorphic and $q$ anti-holomorphic coordinate differentials among the two of each kind; the choices are independent.

**Definition.** The **Dolbeault operators** are
$$
\partial f=\sum_{k=1}^{2}\frac{\partial f}{\partial z_k}\,dz_k,\qquad
\bar\partial f=\sum_{k=1}^{2}\frac{\partial f}{\partial\bar z_k}\,d\bar z_k,
$$
extended to forms by linearity and the Leibniz rule with the sign $(-1)^{p+q}$ for a form of type $(p,q)$.

**Proposition (the bidegrees).** The operator $\partial$ raises $p$ by one and leaves $q$ fixed; the operator $\bar\partial$ raises $q$ by one and leaves $p$ fixed; and
$$
\partial^2=0,\qquad \bar\partial^2=0,\qquad \partial\bar\partial+\bar\partial\partial=0.
$$

*Proof.* The bidegree is read on the definition. The squares vanish because the partial derivatives commute and the wedge product of a repeated differential is zero; the last identity is $d^2=0$ for $d=\partial+\bar\partial$, separated by bidegree.

**Remark (the real and the holomorphic reading).** A function is holomorphic exactly when $\bar\partial f=0$, which is the Cauchy–Riemann system of *Analysis on $\mathbb{C}^2$*. **A $(0,1)$-form is the datum of the $\bar\partial$-problem**, and a $(1,0)$-form is the datum of a holomorphic differential; the two are conjugate, and the real forms are the fixed points of the conjugation that exchanges $dz_k$ and $d\bar z_k$.

## The Dolbeault Complex

**The operator $\bar\partial$ makes the forms of fixed $p$ into a complex, the Dolbeault complex, whose cohomology measures the obstruction to solving $\bar\partial u=g$.**

**Definition.** For fixed $p$, the **Dolbeault complex** is
$$
0\longrightarrow\Omega^{p,0}(D)\stackrel{\bar\partial}{\longrightarrow}\Omega^{p,1}(D)\stackrel{\bar\partial}{\longrightarrow}\Omega^{p,2}(D)\longrightarrow0,
$$
and its cohomology is
$$
H^{p,q}_{\bar\partial}(D)=\frac{\ker\bigl(\bar\partial:\Omega^{p,q}(D)\to\Omega^{p,q+1}(D)\bigr)}{\operatorname{im}\bigl(\bar\partial:\Omega^{p,q-1}(D)\to\Omega^{p,q}(D)\bigr)}.
$$

**Proposition (the two ends).** In two variables the complex has length two: $H^{p,q}_{\bar\partial}=0$ for $q\notin\{0,1,2\}$, and $H^{p,0}_{\bar\partial}(D)$ is the space of holomorphic $p$-forms on $D$.

*Proof.* There are only two anti-holomorphic directions, so $\Omega^{p,q}=0$ for $q>2$; and the kernel of $\bar\partial$ on $\Omega^{p,0}$ consists of the forms with holomorphic coefficients.

**Theorem (the Dolbeault theorem).** For every domain $D\subset\mathbb{C}^2$ and every $p,q$,
$$
H^{p,q}_{\bar\partial}(D)\cong H^{q}(D,\Omega^{p}),
$$
the sheaf cohomology of $D$ with coefficients in the sheaf $\Omega^p$ of holomorphic $p$-forms.

*Proof.* This is the Dolbeault isomorphism, proved by the fine resolution of $\Omega^p$ by the Dolbeault complex and the acyclicity of the sheaves of $C^\infty$ forms (*Several Complex Variables* and *Sheaf Cohomology*).

**Remark (the meaning of the vanishing).** The group $H^{0,1}_{\bar\partial}(D)$ vanishes exactly when every $\bar\partial$-closed $(0,1)$-form is $\bar\partial$-exact, that is, exactly when the inhomogeneous Cauchy–Riemann equation is solvable on $D$ for every datum. **The vanishing is a property of the domain and not of the equation**: it holds on the polydisc and on $\mathbb{C}^2$, and it fails on domains with holes in the appropriate sense.

## The $\bar\partial$-Poincaré Lemma on the Polydisc

**On a polydisc every $\bar\partial$-closed $(0,1)$-form is exact; the proof solves the equation one variable at a time and uses the integrability condition to remove the second component.**

**Theorem (the $\bar\partial$-Poincaré lemma).** Let $\Delta(a,r)\subset\mathbb{C}^2$ be a polydisc and let
$$
g=g_1\,d\bar z_1+g_2\,d\bar z_2
$$
be a $C^\infty$ $(0,1)$-form on $\Delta(a,r)$ with $\bar\partial g=0$. Then there is $u\in C^\infty(\Delta(a,r))$ with $\bar\partial u=g$.

*Proof.* The integrability condition is
$$
\frac{\partial g_2}{\partial\bar z_1}=\frac{\partial g_1}{\partial\bar z_2}.
$$
By the one-variable $\bar\partial$-Poincaré lemma on the disc in the $z_1$ direction, with $z_2$ as a parameter, there is $u_1$ with $\partial u_1/\partial\bar z_1=g_1$; the solution is given by the Cauchy–Green integral and depends smoothly on the parameter. Then
$$
\bar\partial u_1-g=\Bigl(\frac{\partial u_1}{\partial\bar z_2}-g_2\Bigr)d\bar z_2=h\,d\bar z_2,
$$
and $h$ is holomorphic in $z_1$, because $\bar\partial(h\,d\bar z_2)=0$ and $\bar\partial g=0$ give $\partial h/\partial\bar z_1=0$. The one-variable lemma in the $z_2$ direction, applied with the holomorphic parameter $z_1$, gives $v$ with $\partial v/\partial\bar z_2=h$ and $v$ holomorphic in $z_1$. Then $u=u_1-v$ satisfies $\bar\partial u=g$.

**Corollary (the general bidegree).** On a polydisc, every $\bar\partial$-closed $(p,q)$-form with $q\ge1$ is $\bar\partial$-exact.

*Proof.* Write the form as a sum of terms $f\,dz_I\wedge d\bar z_J$ and apply the lemma to the coefficient form of type $(0,q)$ for each multi-index $I$; the operators commute with the holomorphic factor $dz_I$.

**Remark (the shape of the solution).** The proof is an induction on the number of variables, and it is the same induction that gives the Hartogs phenomenon. **The polydisc is a product of discs, and the $\bar\partial$-problem on a product is solved one factor at a time**; on a domain that is not a product, the induction fails and the solvability becomes a condition on the domain, the condition of pseudoconvexity.

## The Bochner–Martinelli Kernel

**The Bochner–Martinelli kernel is a $(2,1)$-form on the boundary that plays the role of the Cauchy kernel; it is not holomorphic in the interior variable, and its denominator is the squared distance.**

**Definition.** For $z,\zeta\in\mathbb{C}^2$ with $\zeta\neq z$, the **Bochner–Martinelli kernel** is
$$
K_{BM}(z,\zeta)=\frac{1}{(2\pi i)^2}\,
\frac{(\bar\zeta_1-\bar z_1)\,d\bar\zeta_2-(\bar\zeta_2-\bar z_2)\,d\bar\zeta_1}{\lVert\zeta-z\rVert^4}
\wedge d\zeta_1\wedge d\zeta_2.
$$

**Proposition (the bidegree and the singularity).** The kernel is a form of type $(2,1)$ in $\zeta$, of real degree $3$. Near the diagonal $\zeta=z$ its numerator vanishes to first order and its denominator is of order $\lVert\zeta-z\rVert^4$, so the kernel is of order $\lVert\zeta-z\rVert^{-3}$; the angular factor in the numerator has zero mean, so the boundary integral is defined as a Cauchy principal value.

*Proof.* The numerator is a $(0,1)$-form and $d\zeta_1\wedge d\zeta_2$ is a $(2,0)$-form, so the type is $(2,1)$. The numerator is a sum of terms linear in $\bar\zeta_j-\bar z_j$, and the denominator is the square of the squared norm; the quotient is of order $\lVert\zeta-z\rVert^{-3}$.

**Theorem (the one-variable reduction).** For $n=1$ the same formula reduces to the Cauchy kernel,
$$
K_{BM}(z,\zeta)=\frac{1}{2\pi i}\,\frac{d\zeta}{\zeta-z}.
$$

*Proof.* In one variable the numerator is $(\bar\zeta-\bar z)\,d\zeta$ and the denominator is $\lvert\zeta-z\rvert^2=(\zeta-z)(\bar\zeta-\bar z)$, so the quotient is $d\zeta/(\zeta-z)$ times $1/(2\pi i)$.

**Remark (why the kernel is not holomorphic).** The numerator contains $\bar\zeta_j-\bar z_j$, so the kernel is not holomorphic in $\zeta$. **It cannot be replaced by a kernel holomorphic in $\zeta$ alone**: the boundary of a domain in $\mathbb{C}^2$ has real dimension three, while a holomorphic $2$-form integrates over a real two-dimensional set, so the one-variable contour integral has no direct analogue over the whole boundary. The Bochner–Martinelli kernel is the replacement, and its non-holomorphicity is exactly what allows it to reproduce a function from data on a three-dimensional boundary.

## The Bochner–Martinelli Formula

**For a $C^1$ function on a bounded domain with smooth boundary, the boundary integral of $f$ against the Bochner–Martinelli kernel reproduces $f$ inside the domain up to the integral of $\bar\partial f$ over the domain.**

**Theorem (the Bochner–Martinelli formula).** Let $D\subset\mathbb{C}^2$ be a bounded domain with $C^1$ boundary, oriented as the boundary of $D$, and let $f\in C^1(\overline{D})$. Then for $z\in D$,
$$
f(z)=\int_{\partial D}f(\zeta)\,K_{BM}(z,\zeta)-\int_{D}\bar\partial f(\zeta)\wedge K_{BM}(z,\zeta),
$$
and for $z\notin\overline{D}$,
$$
0=\int_{\partial D}f(\zeta)\,K_{BM}(z,\zeta)-\int_{D}\bar\partial f(\zeta)\wedge K_{BM}(z,\zeta).
$$

*Proof.* The proof is the application of Stokes' theorem to the form $fK_{BM}$ on $D$ with a small ball around $z$ removed. The kernel is $\bar\partial$-closed in $\zeta$ off the diagonal, so $d(fK_{BM})=\bar\partial f\wedge K_{BM}$ there; the boundary of the small ball contributes $f(z)$ in the limit, by the one-variable reduction and the Bochner–Martinelli computation. The details are in *Several Complex Variables*.

**Corollary (the Cauchy–Fantappiè formula).** If $f$ is holomorphic on a neighbourhood of $\overline{D}$, then for $z\in D$,
$$
f(z)=\int_{\partial D}f(\zeta)\,K_{BM}(z,\zeta).
$$

*Proof.* The second term vanishes because $\bar\partial f=0$ on $D$.

**Remark (the polydisc against the ball).** For the polydisc, the iterated Cauchy formula of *Analysis on $\mathbb{C}^2$* integrates over the two-dimensional distinguished boundary $T^2$, while the Bochner–Martinelli formula integrates over the full three-dimensional boundary $\partial\Delta^2$. **Both reproduce a holomorphic function, although the integrals are taken over sets of different dimension.** For the ball there is no distinguished boundary of product form, and the Bochner–Martinelli formula is the only one of the two that applies.

## The Jump Formula

**The boundary integral defines a function on both sides of the boundary, and the two boundary values differ by the value of $f$: this is the jump formula.**

**Definition.** For $f\in C^1(\overline{D})$ and $z\notin\partial D$, the **Bochner–Martinelli integral** is
$$
Sf(z)=\int_{\partial D}f(\zeta)\,K_{BM}(z,\zeta).
$$
For $z_0\in\partial D$, the **principal value** $\mathrm{PV}\,Sf(z_0)$ is the limit of $Sf(z)$ as $z$ tends to $z_0$ through a ball with a small piece of the boundary removed, averaged over the two sides.

**Theorem (the jump formula).** Let $f\in C^1(\overline{D})$ and $z_0\in\partial D$ a smooth boundary point. Then the boundary values from inside and outside exist and satisfy
$$
S^{+}f(z_0)=\mathrm{PV}\,Sf(z_0)+\tfrac12 f(z_0),\qquad
S^{-}f(z_0)=\mathrm{PV}\,Sf(z_0)-\tfrac12 f(z_0),
$$
so that
$$
S^{+}f(z_0)-S^{-}f(z_0)=f(z_0).
$$

*Proof.* The Bochner–Martinelli formula gives, for $z\in D$,
$$
Sf(z)=f(z)+\int_{D}\bar\partial f\wedge K_{BM}(z,\zeta),
$$
and for $z\notin\overline{D}$,
$$
Sf(z)=\int_{D}\bar\partial f\wedge K_{BM}(z,\zeta).
$$
The domain integral is continuous across the boundary, because its kernel is integrable and the singularity lies on the boundary of the domain of integration; hence the two boundary values differ by $f(z_0)$. The principal value is the average of the two.

**Corollary (the holomorphic case).** If $f$ is holomorphic on a neighbourhood of $\overline{D}$, then $Sf=f$ inside $D$ and $Sf=0$ outside $\overline{D}$; the jump across the boundary is $f$.

*Proof.* The domain integral vanishes, so the two formulas of the theorem reduce to $S^{+}f=f$ and $S^{-}f=0$.

**Remark (the meaning of the jump).** The jump formula is the two-variable form of the Plemelj–Sokhotski formula of one variable. **The boundary integral of a holomorphic function is a holomorphic function inside and zero outside, and the discontinuity across the boundary is the function itself**; the boundary data determine the function, and the jump is the measure of the failure of the boundary values to be the restriction of a holomorphic function.

## The Hartogs Extension Theorem

**The Bochner–Martinelli formula solves the $\bar\partial$-equation with compact support, and the solution gives the Hartogs extension theorem: a holomorphic function on the complement of a compact set extends across it.**

**Lemma (the compactly supported $\bar\partial$-lemma).** Let $g$ be a $\bar\partial$-closed $(0,1)$-form on $\mathbb{C}^2$ with compact support. Then there is $u\in C^\infty_c(\mathbb{C}^2)$ with $\bar\partial u=g$.

*Proof.* The compactly supported Dolbeault cohomology of $\mathbb{C}^2$ vanishes in bidegree $(0,1)$, by Serre duality from the vanishing of $H^{2,1}(\mathbb{C}^2)$ and the Dolbeault theorem; the solution is constructed explicitly with the Bochner–Martinelli kernel and a cut-off. The lemma is proved in *Several Complex Variables*.

**Theorem (Hartogs extension).** Let $D\subset\mathbb{C}^2$ be a domain and let $K\subset D$ be compact with $D\setminus K$ connected. Then every holomorphic function on $D\setminus K$ extends holomorphically to $D$.

*Proof.* Let $f$ be holomorphic on $D\setminus K$. Choose $\chi\in C^\infty_c(D)$ with $\chi=1$ on a neighbourhood of $K$, and define
$$
f_0=\begin{cases}(1-\chi)f & \text{on } D\setminus K,\\ 0 & \text{on } K.\end{cases}
$$
Then $f_0\in C^\infty_c(D)$, because $1-\chi$ vanishes near $K$ and $\chi$ is compactly supported; and $f_0=f$ near $\partial D$, because $\chi=0$ there. The form $\bar\partial f_0$ is a $\bar\partial$-closed $(0,1)$-form with compact support in $D$. By the lemma, there is $u\in C^\infty_c(\mathbb{C}^2)$ with $\bar\partial u=\bar\partial f_0$. Then $F=f_0-u$ is holomorphic on $D$. Near $\partial D$ the form $\bar\partial f_0$ vanishes, so $u$ is holomorphic there; being compactly supported, $u$ vanishes on the unbounded component of its domain, hence near $\partial D$ by the identity theorem. Therefore $F=f$ near $\partial D$, and by the identity theorem on the connected set $D\setminus K$, $F=f$ there. Hence $F$ is the required extension.

**Corollary (no isolated singularities).** A function holomorphic on $\mathbb{C}^2\setminus\{0\}$ extends to $\mathbb{C}^2$.

*Proof.* Take $K=\{0\}$, a compact set whose complement is connected.

**Remark (the role of the kernel).** The Hartogs theorem is usually proved by the Hartogs figure and the iterated Cauchy formula; **the proof by the Bochner–Martinelli kernel is the same theorem read through the $\bar\partial$-equation**. The kernel produces the compactly supported solution, and the solution absorbs the $\bar\partial$-obstruction of the cutoff; what remains is holomorphic and agrees with $f$ near the boundary of the domain.

## The Dolbeault Cohomology of $\mathbb{C}^2$

**The space $\mathbb{C}^2$ is Stein, so its Dolbeault cohomology vanishes in every positive anti-holomorphic degree, and the $\bar\partial$-problem is solvable globally for every bidegree.**

**Theorem (the vanishing).** For every $p\in\{0,1,2\}$ and every $q\ge1$,
$$
H^{p,q}_{\bar\partial}(\mathbb{C}^2)=0.
$$
In particular every $\bar\partial$-closed $(0,1)$-form on $\mathbb{C}^2$ is $\bar\partial$-exact.

*Proof.* The space $\mathbb{C}^2$ is a Stein manifold, and Cartan's theorem B gives $H^q(\mathbb{C}^2,\mathcal{F})=0$ for $q\ge1$ and every coherent analytic sheaf $\mathcal{F}$; the sheaf $\Omega^p$ is coherent. The Dolbeault theorem identifies $H^{p,q}_{\bar\partial}$ with $H^q(\mathbb{C}^2,\Omega^p)$, which therefore vanishes.

**Corollary (the equation with prescribed data).** For every $g\in\Omega^{0,1}(\mathbb{C}^2)$ with $\bar\partial g=0$ there is $u\in C^\infty(\mathbb{C}^2)$ with $\bar\partial u=g$, and $u$ is unique up to the addition of a holomorphic function.

*Proof.* The existence is the theorem in bidegree $(0,1)$. If $u_1$ and $u_2$ are two solutions, then $\bar\partial(u_1-u_2)=0$, so $u_1-u_2$ is holomorphic.

**Remark (the vanishing is not true on every domain).** The unit ball and the bicylinder are Stein, so the vanishing holds there too; but a domain with a hole in the appropriate sense can have $H^{0,1}\neq0$. **The vanishing is a theorem about the domain, and the Bochner–Martinelli formula is the effective form of the theorem on domains with smooth boundary.** The general criterion is pseudoconvexity, and the general theorem is the solution of the Levi problem (*Several Complex Variables*).

## Summary

A $(p,q)$-form on $\mathbb{C}^2$ is a sum of terms with $p$ holomorphic and $q$ anti-holomorphic differentials, of dimension $\binom{2}{p}\binom{2}{q}$ at a point, and the Dolbeault operator $\bar\partial$ raises $q$ by one and squares to zero. The Dolbeault complex has length two in the anti-holomorphic direction, and its cohomology $H^{p,q}_{\bar\partial}$ is the obstruction to solving $\bar\partial u=g$; by the Dolbeault theorem it is the sheaf cohomology $H^q(D,\Omega^p)$.

On a polydisc the $\bar\partial$-Poincaré lemma holds: every $\bar\partial$-closed $(0,1)$-form is exact, and the proof solves the equation one variable at a time. The solution on a general domain is given by the Bochner–Martinelli kernel, a $(2,1)$-form with denominator $\lVert\zeta-z\rVert^4$ that integrates over the three-dimensional boundary; the Bochner–Martinelli formula reproduces a $C^1$ function inside the domain up to the integral of $\bar\partial f$, and the jump formula states that the boundary integral has boundary values differing by $f$. The compactly supported $\bar\partial$-lemma, applied to a cutoff of a function holomorphic off a compact set, gives the Hartogs extension theorem. The space $\mathbb{C}^2$ is Stein, so $H^{p,q}_{\bar\partial}(\mathbb{C}^2)=0$ for $q\ge1$, and the $\bar\partial$-problem is solvable globally for every datum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega^{p,q}(D)$ | the $C^\infty$ forms of type $(p,q)$ on $D$ |
| $\partial,\bar\partial$ | the Dolbeault operators, of bidegrees $(1,0)$ and $(0,1)$ |
| $H^{p,q}_{\bar\partial}(D)$ | the Dolbeault cohomology |
| $\Delta(a,r)$ | the polydisc of multiradius $r$ about $a$ |
| $K_{BM}(z,\zeta)$ | the Bochner–Martinelli kernel, a $(2,1)$-form in $\zeta$ |
| $Sf(z)$ | the Bochner–Martinelli integral of $f$ |
| $\mathrm{PV}\,Sf$ | its principal value on the boundary |
| $S^{+}f,S^{-}f$ | the boundary values from inside and outside |
| $\Omega^p$ | the sheaf of holomorphic $p$-forms |
| Stein manifold | a domain of holomorphy with the separation and convexity properties |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space and the coordinates.
- [Analysis on $\mathbb{C}^2$](analysis-on-the-complex-two-space.html), the previous article, for the Cauchy–Riemann equations, the polydisc and the Cauchy formula.
- [The Ball and the Bicylinder in $\mathbb{C}^2$](the-ball-and-the-bicylinder.html), the previous article, for the model domains and their boundaries.
- [Harmonic Analysis on $\mathbb{C}^2$](harmonic-analysis-on-the-complex-two-space.html), the next article, for the Fourier transform and the Laplacian.
- [Several Complex Variables](several-complex-variables.html), for the Dolbeault complex, the $\bar\partial$-equation, pseudoconvexity, the Hartogs theorem and the solution of the Levi problem.
- [Differential Forms and Stokes' Theorem](differential-forms-and-stokes-theorem.html), for the calculus of forms, the operators $\partial$ and $\bar\partial$ and Stokes' theorem.
- [Sheaf Cohomology](sheaf-cohomology.html), for the cohomological form of the Dolbeault theorem and Cartan's theorem B.
- [Complex Analysis](complex-analysis.html), for the one-variable Cauchy–Green formula and the Cauchy kernel.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs and the typographic conventions of the corpus.
