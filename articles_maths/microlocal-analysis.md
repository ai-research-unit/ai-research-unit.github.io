
# __Microlocal Analysis__

## Introduction

A function can be smooth at a point and still have a singularity of a definite oscillatory character there; the singularity of a distribution is carried not only by a position $x$ but by a direction $\xi$ in the frequency space, and the right answer to "where is $u$ singular?" is a subset of the cotangent bundle. The **wavefront set** $WF(u)$ is that subset: a distribution is smooth near $x$ exactly when the fibre of $WF(u)$ over $x$ is empty, and the additional frequencies in the fibre record the directions in which the Fourier transform is not rapidly decreasing after localisation. The definition is local and conic, and it is stable under the operations of the calculus: a pseudodifferential operator of order $m$ cannot create singularities, it can transform them only by its symbol, an elliptic operator removes none, and the **microlocal elliptic regularity** $Pu$ smooth at $(x,\xi)$ and $P$ elliptic there $\Rightarrow u$ smooth at $(x,\xi)$ is the sharp form of the elliptic regularity of *Pseudodifferential Operators*. The intersection of wavefront sets decides when two distributions can be multiplied, which is the criterion of Hörmander for the product; and when the symbol of an operator is real, the singularities of a solution propagate along the flow of its Hamiltonian vector field — the **propagation of singularities**, whose integral curves are the bicharacteristics.

The article develops the local theory. It defines $WF(u)$, identifies it with the conormal bundle for the standard examples (the delta distribution and the indicator of a smooth domain), and proves that the projection of $WF(u)$ to the base is the singular support. It states the transformation law under a pseudodifferential operator, the microlocal form of elliptic regularity, the Sobolev wavefront sets that refine $WF$ by regularity, and the product and pullback criteria. It states the propagation theorem of Hörmander and identifies the bicharacteristics, leaving the applications to hyperbolic equations. It closes with the analytic wavefront set, where the singularities are those of holomorphic extension.

Throughout, $M$ is a smooth manifold of dimension $n$ (initially an open subset of $\mathbb{R}^n$), $T^*M$ is its cotangent bundle, $T^*M\setminus0$ is the complement of the zero section, and points of $T^*M$ are written $(x,\xi)$ with $\xi \neq0$. The pseudodifferential calculus, its symbol classes $S^m$, the principal symbol $\sigma_m$, the Poisson bracket and ellipticity are those of *Pseudodifferential Operators*; the distributions, the Fourier transform and the oscillatory integrals are those of *Distributions and Fundamental Solutions*; the Sobolev and Bessel spaces are those of *Interpolation Theory*; and the Fredholm property of an elliptic operator is that of *Fredholm Theory*. The bicharacteristics of a real principal-type operator are the integral curves of a Hamiltonian flow, and in the geometric case of a metric symbol that flow is the geodesic flow; the wavefront set of a solution of a hyperbolic equation and the propagation of singularities for the Cauchy problem belong, and the semiclassical form of the same phenomena. The analytic theory is the domain of the Sato–Kawai–Kashiwara school, cited below as standard.

No physics is invoked.

## The Wavefront Set

### Definition

**Definition.** Let $u \in \mathcal D'(\mathbb{R}^n)$ and $(x_0,\xi_0) \in \mathbb{R}^n\times(\mathbb{R}^n\setminus0)$. One says that $u$ is **smooth at $(x_0,\xi_0)$**, written $(x_0,\xi_0)\notin WF(u)$, if there is $\chi \in C_c^\infty(\mathbb{R}^n)$ with $\chi \equiv1$ near $x_0$ and an open cone $\Gamma \subseteq \mathbb{R}^n$ containing $\xi_0$ (a cone in the sense $\xi \in \Gamma,\ t>0\Rightarrow t\xi \in \Gamma$) such that

$$
|\widehat{\chi u}(\xi)| \le C_N(1+|\xi|)^{-N} \qquad \text{for all } N \text{ and all } \xi \in \Gamma .
$$

Equivalently, the localised Fourier transform $\widehat{\chi u}$ is rapidly decreasing along a conic neighbourhood of $\xi_0$. The **wavefront set** $WF(u)$ is the complement in $\mathbb{R}^n\times(\mathbb{R}^n\setminus0)$ of the set of smooth points, and it is independent of the choice of the cutoff functions used to test it.

**Proposition.** (i) $WF(u)$ is closed and conic: $(x,\xi)\in WF(u)$ and $t>0$ imply $(x,t\xi)\in WF(u)$; the fibre $WF(u)_x=\{\xi:(x,\xi)\in WF(u)\}$ is a closed cone in $\mathbb{R}^n\setminus0$. (ii) $WF(u)=\varnothing$ exactly when $u \in C^\infty$, and $\operatorname{sing\,supp}u$ is the projection of $WF(u)$ to $\mathbb{R}^n$. (iii) $WF(u)$ is a subset of $T^*M\setminus0$ when $u$ is a distribution on a manifold, the local definitions agreeing on overlaps by the invariance of the principal symbol.

*Proof.* The conicity and closedness are immediate from the definition, since a cone containing $\xi_0$ contains a neighbourhood of the ray through $\xi_0$. For (ii), if all pairs are smooth one can cover a compact set by finitely many localisations with rapidly decreasing Fourier transforms in the relevant cones, and the sum is $C^\infty$; conversely the rapid decrease of $\widehat{\chi u}$ in a neighbourhood of a point where $u$ is $C^\infty$ follows by integration by parts. For (iii) the transformation of the definition under a diffeomorphism is exactly the cotangent lift appearing in the invariance theorem of *Pseudodifferential Operators*. $\square$

**Definition.** For $s \in \mathbb{R}$ define $(x_0,\xi_0)\notin WF^s(u)$ if there are $\chi$ and a cone $\Gamma$ as above with

$$
\int_\Gamma(1+|\xi|^2)^s\,|\widehat{\chi u}(\xi)|^2\,d\xi<\infty ,
$$

the **Sobolev wavefront set** of order $s$. Then $WF^s(u)=\varnothing$ exactly when $u \in H^s_{\mathrm{loc}}$, the sets decrease as $s$ increases, and

$$
WF(u)=\overline{\bigcup_{s \in \mathbb{R}}WF^s(u)},
$$

so the wavefront set is the union of the regularity-specific pieces; the data of all the $WF^s(u)$ is the full microlocal regularity of $u$.

### The Standard Examples

**Example (the delta distribution).** For $u=\delta_0$ and $\chi$ equal to $1$ near $0$, $\widehat{\chi u}=1$, which is not rapidly decreasing in any direction; hence

$$
WF(\delta_0)=\{(0,\xi):\xi \in \mathbb{R}^n\setminus0\}=N^*\{0\}\setminus0,
$$

and $\delta_0$ is smooth in no direction at the origin. It is the extreme case: a distribution whose fibre at the origin is the whole frequency space.

**Example (the indicator of a domain).** Let $\Omega \subseteq \mathbb{R}^n$ be a domain with smooth boundary $\Sigma=\partial\Omega$ and let $u=\mathbf{1}_\Omega$. Then

$$
WF(\mathbf{1}_\Omega)=N^*\Sigma\setminus0=\{(x,\xi):x \in \Sigma,\ \xi \perp T_x\Sigma,\ \xi \neq0\},
$$

the conormal bundle of the boundary minus the zero section: the singularity at a boundary point is concentrated in the direction normal to the boundary, all other directions being smooth. This is the prototype of a **conormal distribution**, one whose wavefront set lies in the conormal bundle of a submanifold, and the edge behaviour of a solution across the boundary is the corresponding microlocal datum.

**Example (the Heaviside function).** On $\mathbb{R}$ the function $H=\mathbf{1}_{(0,\infty)}$ has $\widehat{H}(\xi)$ behaving like $1/\xi$ near $\xi=0$ but decaying in every direction away from $\xi=0$ after localisation at a point $x \neq0$; at $x=0$ the singular frequency directions fill $\mathbb{R}\setminus0$, so

$$
WF(H)=\{(0,\xi):\xi \in \mathbb{R}\setminus0\}.
$$

The jump is a single point and the singular directions fill the fibre.

**Example (a smooth function).** $WF(u)=\varnothing$ for $u \in C^\infty$; a distribution that is smooth off a closed set $K$ has $WF(u)\subseteq K\times(\mathbb{R}^n\setminus0)$.

## Microlocal Regularity and the Calculus

### Action of Pseudodifferential Operators

**Theorem (microlocal action).** Let $P=a(x,D)$ be pseudodifferential of order $m$ and let $u \in \mathcal E'$. Then

$$
WF(Pu)\subseteq WF(u),
$$

and the inclusion is locally sharp at the elliptic points of $P$: if $(x_0,\xi_0)\notin WF(Pu)$ and $a$ is elliptic at $(x_0,\xi_0)$, then $(x_0,\xi_0)\notin WF(u)$. In general

$$
WF(u)\subseteq WF(Pu)\cup\operatorname{Char}(P), \qquad \operatorname{Char}(P)=\{(x,\xi)\in T^*M\setminus0:\sigma_m(P)(x,\xi)=0\}.
$$

*Proof.* The first inclusion is the statement that multiplication by a symbol of order $m$ maps the rapidly decreasing class into itself in each conic direction: after localisation the composition with $a$ is a convolution in frequency with a kernel whose Fourier transform decays rapidly off the diagonal, so a rapid decrease in a cone is preserved. For the second, if $a$ is elliptic at $(x_0,\xi_0)$ choose a microlocal parametrix $Q$ with symbol $b \in S^{-m}$ equal to $a^{-1}$ in a conic neighbourhood of $(x_0,\xi_0)$; then $u=Q Pu+(I-QP)u$, the second term is smoothing near $(x_0,\xi_0)$ by the construction of $b$, and $Q$ cannot create a singularity at $(x_0,\xi_0)$ by the first inclusion. $\square$

**Corollary (microlocal elliptic regularity).** If $P$ is elliptic on an open conic set $U \subseteq T^*M\setminus0$ and $Pu \in C^\infty$ microlocally on $U$, in the sense $U\cap WF(Pu)=\varnothing$, then $U\cap WF(u)=\varnothing$. In particular an elliptic operator has $WF(Pu)=WF(u)$, so the wavefront set is a microlocal invariant of the solutions of an elliptic equation.

Elliptic regularity in the form "$Pu$ smooth $\Rightarrow u$ smooth" is the case $U=T^*M\setminus0$; the microlocal statement localises it to a single point of the cotangent bundle and is the precise form of the principle that an elliptic operator is invertible microlocally.

### Composition and Invariance

**Theorem.** Let $P,Q$ be pseudodifferential operators. Then (i) $WF(PQu)\subseteq WF(Qu)\subseteq WF(u)$, with equality at the elliptic points of both; (ii) under an elliptic Fourier integral operator $A$ with homogeneous canonical relation $\chi \subseteq (T^*M\setminus0)\times(T^*M\setminus0)$, the wavefront set transforms by the action of $\chi$, $WF(Au)\subseteq\chi(WF(u))$, with equality at the elliptic points; in particular a pseudodifferential operator with nowhere-vanishing principal symbol acts on $WF(u)$ by the identity map on $T^*M\setminus0$.

The second statement is the invariance property of the wavefront set under changes of coordinates and under the action of the variables: it is what makes $WF(u)$ a geometric object. The Fourier integral operators, their canonical relations and the composition law that pairs a wavefront set with a canonical relation are the standard calculus of Hörmander and Duistermaat–Hörmander, cited below.

## Products, Pullbacks and the Criterion

### The Product of Two Distributions

The product of two distributions is generally undefined, since one cannot multiply two singular functions pointwise; the wavefront set gives a sharp criterion for when the product extends from the smooth case.

**Theorem (product criterion).** Let $u,v \in \mathcal D'(\mathbb{R}^n)$ and suppose

$$
WF(u)\cap(-WF(v))=\varnothing, \qquad -WF(v)=\{(x,-\xi):(x,\xi)\in WF(v)\} .
$$

Then the bilinear form $(u,v)\mapsto\langle uv,\varphi\rangle$, defined for $\varphi \in C_c^\infty$ by the tensor product $u\otimes v$ paired with $\varphi(x)\delta(x-y)$, extends uniquely to a distribution $uv \in \mathcal D'$, and

$$
WF(uv)\subseteq WF(u)\cup WF(v)\cup\bigl(WF(u)+WF(v)\bigr),
$$

where the sum is the conic sumset in the fibres. If the intersection is nonempty there are pairs for which no extension exists, so the condition is sharp.

*Proof (sketch).* Near the diagonal the tensor product $u\otimes v$ has wavefront set contained in $WF(u)\times WF(v)$ together with the pieces carrying the zero section of one factor over the support of the other; the product is the pullback of $u\otimes v$ by the diagonal map $x\mapsto(x,x)$, and the pullback criterion below applies. The conormal bundle of the diagonal is $\{((x,x),(\xi,-\xi))\}$, and the transversality required by the pullback criterion is exactly $WF(u)\cap(-WF(v))=\varnothing$; the computation of the wavefront set of the pullback gives the displayed inclusion. The sharpness is proved by constructing, for each pair of conic directions meeting with opposite signs, distributions whose product has no canonical extension. $\square$

**Example.** (i) $\delta_0^2$ is undefined: $WF(\delta_0)=\{(0,\xi):\xi \neq0\}$ and $-WF(\delta_0)$ is the same set, so the intersection is nonempty. A squared delta has no distributional meaning.

(ii) If $u \in C^\infty$ then $WF(u)=\varnothing$ and the criterion holds for every $v$, giving the ordinary product $uv$ of a smooth function and a distribution; this is the trivial case.

(iii) The criterion is sufficient, not necessary for products that already exist by other means: the two Heaviside functions $H$ have $WF(H)\cap(-WF(H))=\{(0,\xi):\xi \neq0\}\neq\varnothing$, so the criterion does not apply, yet $H^2=H$ is defined as an $L^\infty_{\mathrm{loc}}$ function. The criterion is the exact condition for the canonical extension by continuity from the smooth case, not for every product that happens to have a meaning.

(iv) If $u$ has $WF(u)\subseteq N^*\Sigma$ and $v$ has $WF(v)\subseteq N^*\Sigma$ for a hypersurface $\Sigma$, the criterion fails along $N^*\Sigma$; but if $v$ is smooth near $\Sigma$ then the intersection is empty and the product is defined. This is the microlocal form of the familiar rule that a distribution may be multiplied by a smooth factor.

### Pullbacks

**Theorem (pullback criterion).** Let $f:X\to Y$ be a smooth map of manifolds and let $u \in \mathcal D'(Y)$. Then the pullback $f^*u \in \mathcal D'(X)$ is defined whenever

$$
WF(u)\cap N_f=\varnothing, \qquad N_f=\{(f(x),\eta):d f(x)^{\mathsf T}\eta=0,\ \eta \neq0\},
$$

the conormal bundle of $f$; when defined,

$$
WF(f^*u)\subseteq f^*(WF(u)), \qquad f^*(x,\xi)=\bigl(x,\,d f(x)^{\mathsf T}\xi\bigr),
$$

the pullback of the cotangent bundle by $f$. If $f$ is a submersion the condition is automatically satisfied; if $f$ is the diagonal the criterion is the product criterion above.

*Proof (sketch).* The pullback is the composition of $u$ with $f$ and is a Fourier integral operator with canonical relation the graph of the cotangent lift of $f$; the composition of a Fourier integral operator with a distribution is defined when the wavefront set of the distribution meets the conormal of the relation transversally, which for the pullback is the displayed condition, and the transformation of the wavefront set follows from the composition law. $\square$

**Corollary (restriction and trace).** The restriction of $u \in \mathcal D'(Y)$ to a submanifold $S \subseteq Y$ is defined whenever the fibre of $WF(u)$ over $S$ contains no conormal vector of $S$; in that case $WF(u|_S)\subseteq$ the image of $WF(u)$ under the projection $T^*_SY\to T^*S$. This is the microlocal form of the trace theorems used in the theory of boundary-value problems, which belongs.

## Propagation of Singularities

### Real Principal-Type Operators

**Definition.** A pseudodifferential operator $P$ with real principal symbol $p_m=\sigma_m(P)$ is of **real principal type** if $dp_m$ does not vanish at any point of the characteristic set $\operatorname{Char}(P)=\{p_m=0\}\subseteq T^*M\setminus0$. The **Hamiltonian vector field** of $p_m$ is

$$
H_{p_m}=\sum_{j=1}^{n}\Bigl(\partial_{\xi_j}p_m\,\partial_{x_j}-\partial_{x_j}p_m\,\partial_{\xi_j}\Bigr),
$$

and its integral curves in $\operatorname{Char}(P)$ are the **bicharacteristics** of $P$. The field is related to the Poisson bracket by $H_{p_m}q=\{p_m,q\}$, with the bracket of *Pseudodifferential Operators*.

**Theorem (propagation of singularities).** Let $P$ be a pseudodifferential operator of real principal type and let $u \in \mathcal D'(M)$ satisfy $Pu \in C^\infty$ (or, more generally, $Pu \in H^s_{\mathrm{loc}}$). Then

$$
WF(u)\setminus WF(Pu)\subseteq\operatorname{Char}(P),
$$

and $WF(u)\setminus WF(Pu)$ is a union of bicharacteristics: if $(x_0,\xi_0)\in WF(u)\setminus WF(Pu)$ then the whole bicharacteristic through $(x_0,\xi_0)$ lies in $WF(u)\setminus WF(Pu)$. The same statement holds with $WF^s$ in place of $WF$.

*Proof (sketch).* One proves the microlocal regularity at a bicharacteristic from the regularity at a neighbouring point by the **positive commutator** method: construct a pseudodifferential operator $A$ of order $0$ whose symbol is supported in a small cone near the current point of the bicharacteristic and is a monotone function along $H_{p_m}$; the commutator $[P,A]$ has principal symbol $\frac1i\{p_m,a\}$, which has a definite sign by the monotonicity along the flow, while the quadratic form of $P$ contributes a boundary term controlled by the known regularity. The inequality that results is the energy estimate that transports the regularity one step along the bicharacteristic, and iterating along the flow gives the invariance. The full argument is given in the works cited below. $\square$

**Corollary.** If $P$ is real principal type and $Pu$ is smooth, then $u$ is smooth off the characteristic set, by microlocal elliptic regularity, and on the characteristic set the singularities of $u$ are constant along the bicharacteristics; consequently the singular support of $u$ is a union of projections of bicharacteristics, and the singularities cannot be confined to a proper subset of one.

**Example (the wave operator).** Let $P=\partial_t^2-\Delta_x$ on $\mathbb{R}^{1+n}$, with principal symbol $p=-\tau^2+|\xi|^2$; the characteristic set is the union of the two cones $\tau=\pm|\xi|$, the bicharacteristics are the straight lines along which $x \mp t\xi/|\xi|$ is constant, and the propagation theorem says that a singularity of a solution of the wave equation travels along the characteristics with speed one. This is the microlocal form of the propagation of the leading edge of a wave, and the detailed theory of the Cauchy problem, the domain of dependence and the energy estimates belongs.

**Example (the Laplacian).** For $P=-\Delta$ the principal symbol $|\xi|^2$ is elliptic, the characteristic set is empty, and the propagation theorem degenerates to elliptic regularity: $WF(u)\subseteq WF(Pu)$, so that smoothness of $-\Delta u$ gives smoothness of $u$.

## The Analytic Wavefront Set

**Definition.** Replacing rapid decrease by exponential decrease, or equivalently testing holomorphic extendability of the localised Fourier transform, defines the **analytic wavefront set** $WF_a(u)$: $(x_0,\xi_0)\notin WF_a(u)$ if there is a cutoff $\chi$ and a cone $\Gamma$ about $\xi_0$ with $|\widehat{\chi u}(\xi)|\le Ce^{-c|\xi|}$ on $\Gamma$. One has $WF(u)\subseteq WF_a(u)$, the projection of $WF_a(u)$ is the analytic singular support, and $WF_a(u)=\varnothing$ exactly when $u$ is real analytic.

**Theorem (analytic propagation; Sato–Kawai–Kashiwara).** Let $P$ be of real principal type with real analytic coefficients and let $Pu$ be real analytic. Then $WF_a(u)\setminus WF_a(Pu)$ is contained in $\operatorname{Char}(P)$ and is invariant under the bicharacteristic flow of $p_m$; in particular the analytic singularities of a solution of an analytic real principal-type equation propagate along bicharacteristics.

The analytic theory is proved with the FBI transform, which replaces the Fourier transform by a Gaussian localisation and turns microlocalisation into the boundary values of holomorphic functions; the theory of hyperfunctions and of the analytic wavefront set is the standard body of work cited below, and the Cauchy–Kovalevskaya theorem, its classical application, belongs to the same literature. The Gevrey wavefront sets and their propagation refine the intermediate regularity and are treated in the same literature.

## Summary

The wavefront set $WF(u)$ of a distribution is the closed conic subset of $T^*M\setminus0$ consisting of the points $(x,\xi)$ at which the localised Fourier transform of $u$ fails to be rapidly decreasing along the cone through $\xi$; its projection is the singular support, and it is empty exactly for smooth $u$. The Sobolev wavefront sets $WF^s(u)$ refine it so that $WF^s(u)=\varnothing$ exactly for $u \in H^s_{\mathrm{loc}}$, and $WF(u)$ is the closure of their union. The delta distribution has $WF(\delta_0)=N^*\{0\}\setminus0$, the indicator of a smooth domain has wavefront set the conormal bundle of its boundary, and the Heaviside function has its singularity in all directions at the origin; conormal distributions are those whose wavefront set lies in a conormal bundle.

Pseudodifferential operators do not create singularities, $WF(Pu)\subseteq WF(u)$; an elliptic $P$ preserves the wavefront set, $WF(Pu)=WF(u)$, and microlocal elliptic regularity states that $u$ is smooth at $(x,\xi)$ exactly when $Pu$ is, for $P$ elliptic there. The product $uv$ extends canonically from the smooth case whenever $WF(u)\cap(-WF(v))=\varnothing$, with $WF(uv)\subseteq WF(u)\cup WF(v)\cup(WF(u)+WF(v))$, so that $\delta_0^2$ is undefined but the product of a distribution with a smooth function is always defined; the pullback $f^*u$ is defined whenever $WF(u)\cap N_f=\varnothing$, with $WF(f^*u)\subseteq f^*(WF(u))$, and the restriction and trace theorems are the special case of a submanifold. For a real principal-type operator $P$ the set $WF(u)\setminus WF(Pu)$ lies in the characteristic set and is a union of bicharacteristics, the integral curves of the Hamiltonian field $H_{p_m}=\sum_j(\partial_{\xi_j}p_m\partial_{x_j}-\partial_{x_j}p_m\partial_{\xi_j})$; this propagation theorem is the microlocal form of the propagation of waves, and its applications to hyperbolic equations belong. Replacing rapid decay by exponential decay gives the analytic wavefront set, whose singularities propagate along the same bicharacteristics, the theorem of Sato–Kawai–Kashiwara proved with the FBI transform.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $u$, $\mathcal D'$, $\mathcal E'$ | distributions and compactly supported distributions |
| $\widehat{\chi u}$ | localised Fourier transform |
| $WF(u)$ | wavefront set, conic subset of $T^*M\setminus0$ |
| $WF_x(u)$ | fibre of the wavefront set over $x$ |
| $WF^s(u)$ | Sobolev wavefront set of order $s$ |
| $WF_a(u)$ | analytic wavefront set |
| $N^*\Sigma$, $N_f$ | conormal bundle of a submanifold, of a map |
| $\operatorname{sing\,supp}u$ | singular support |
| $\operatorname{Char}(P)$ | characteristic set of a pseudodifferential operator |
| $p_m=\sigma_m(P)$ | real principal symbol |
| $H_{p_m}$ | Hamiltonian vector field |
| $(x,\xi)$ | point of the cotangent bundle $T^*M\setminus0$ |
| $-WF(v)$ | reflection $\xi\mapsto-\xi$ of a wavefront set |
| $f^*u$, $f^*$ | pullback of a distribution and of the cotangent bundle |
| $\mathbf{1}_\Omega$, $H$ | indicator of a domain and Heaviside function |
| $\delta_0$ | delta distribution at the origin |



## Further Reading

- Lars Hörmander, "Fourier integral operators I", *Acta Mathematica* 127 (1971), 79–183, for the calculus of Fourier integral operators and the transformation of wavefront sets.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the wavefront set, its definition and its calculus properties.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators III* (Springer, 1985), for the microlocal theory of products, pullbacks and the propagation of singularities.
- Johannes J. Duistermaat and Lars Hörmander, "Fourier integral operators II", *Acta Mathematica* 128 (1972), 183–269, for the composition of Fourier integral operators and the invariance of the wavefront set.
- Mikio Sato, Takahiro Kawai and Masaki Kashiwara, "Microfunctions and pseudo-differential equations", in *Hyperfunctions and Pseudo-Differential Equations* (Springer Lecture Notes in Mathematics 287, 1973), 265–529, for the analytic wavefront set and its propagation.
- François Trèves, *Introduction to Pseudodifferential and Fourier Integral Operators*, vol. 1 (Plenum, 1980), for a detailed exposition of microlocal analysis.
- Michael E. Taylor, *Pseudodifferential Operators* (Princeton University Press, 1981), for the wavefront set under changes of coordinates and the classical applications.
- Jean-Michel Bony, "Propagation et interaction des singularités pour les solutions des équations aux dérivées partielles non-linéaires", *Séminaire Goulaouic–Meyer–Schwartz* (1981), for the second microlocalisation and the interaction of singularities.
- Lars Hörmander, "The analysis of linear partial differential operators IV" (Springer, 1985), for the analytic wavefront sets and Gevrey classes.
