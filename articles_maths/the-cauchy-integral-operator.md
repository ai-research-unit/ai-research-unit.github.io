
# __The Cauchy Integral Operator__

## Introduction

The Cauchy kernel $E(x-y)=\omega_m^{-1}(x-y)^{\natural}|x-y|^{-m-1}$ of *Clifford Analysis* defines
an operator, and this article treats that operator at its own layer. The setting is the one of *The
Dirac Operator*: a Clifford algebra $A=\mathrm{Cl}_{0,m}$ with frame $1,e_1,\dots,e_m$, a left
Clifford module $\mathcal{S}$ of values, the vector variable $x\in\mathbb{R}^{m+1}$, and the
Cauchy–Riemann operator $D=\sum_{\mu=0}^{m}e_\mu\partial_\mu$ with conjugate $\bar D$ and
fundamental solution $E$.

Two operators are built from the kernel. The first is the **boundary transform**, the integral of a
density on a surface against the kernel and the conormal element; it maps a datum on the boundary to
a function away from it, it has one-sided traces, and its traces differ by the datum itself — the
Plemelj–Sokhotski formulae — so that the odd part of the transform is an involution of the boundary
density space, the **singular Cauchy operator**. The second is the **volume transform**, the
integral of a function on a domain against the kernel, which inverts the operator $D$ and turns the
Cauchy–Pompeiu formula into the statement that the boundary transform and the volume transform
together reproduce every $C^1$ function. The article establishes the algebraic identities of these
operators, their boundedness on the classical spaces, and the description of the monogenic Hardy
space as the range of a projection.

The function theory is not repeated: the Cauchy–Pompeiu and Cauchy integral formulae and the kernel
computation are *Clifford Analysis*'s, the general integration theory of a hypercomplex system is
*Hypercomplex Integration*'s, and the boundary-value problems to which the operator is applied are
*Riemann Boundary Value Problems and Singular Integral Equations*'. What belongs here is the
operator: its definition, its traces, the involution property of the singular part, its mapping
properties, and its relation to the projection onto boundary values. The Hermitian refinement of the
operator is *The Hermitian Cauchy Integral and the Boundary Values* and *The Hermitian Cauchy Kernel
as an Adjoint*; the measure-theoretic and fractal boundary theory is a section of *Clifford
Analysis* and is cited, not developed; the Fourier and Calderón–Zygmund reading of the singular
integral is *Harmonic Analysis over Hypercomplex Systems*.

## The Boundary Transform

### The Cauchy Transform of a Density

**Definition.** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be a bounded domain with smooth boundary
$\Gamma$, oriented as the boundary of $\Omega$, and let $h:\Gamma\to\mathcal{S}$ be a continuous
density. The **Cauchy transform** of $h$ is

$$
(\mathcal{C}_\Gamma h)(x) = \int_\Gamma E(x-y)\,\nu_B(y)\,h(y)\,dS(y) , \qquad x\notin\Gamma ,
$$

where $\nu_B(y)=\sum_\mu\nu_\mu(y)e_\mu$ is the conormal element of *The Dirac Operator*. The
transform is defined off the surface and is monogenic on each side: $D(\mathcal{C}_\Gamma h)=0$ on
$\mathbb{R}^{m+1}\setminus\Gamma$, because $E(x-y)$ is monogenic in $x$ away from $y$, and the
differentiation passes under the integral sign.

**Definition.** The **one-sided extensions** are
$\mathcal{C}^+h(x)=\lim_{x'\to x,\,x'\in\Omega} \mathcal{C}_\Gamma h(x')$ and
$\mathcal{C}^-h(x)=\lim_{x'\to x,\,x'\notin\overline\Omega} \mathcal{C}_\Gamma h(x')$, taken at
points of $\Gamma$ at which the surface is smooth and the limits exist.

### The Plemelj–Sokhotski Formulae

**Theorem (Plemelj–Sokhotski; standard).** For a $C^{0,\alpha}$ density $h$ on a smooth surface
$\Gamma$ the one-sided extensions exist at every point of $\Gamma$, and

$$
\mathcal{C}^+h = \tfrac12 h + \mathcal{S}h , \qquad
\mathcal{C}^-h = -\tfrac12 h + \mathcal{S}h ,
$$

where

$$
(\mathcal{S}h)(x) = 2\,\mathrm{p.v.}\!\int_\Gamma E(x-y)\,\nu_B(y)\,h(y)\,dS(y)
$$

is the **singular Cauchy operator**, the principal value being taken over the intersection of
$\Gamma$ with the complement of a small ball about $x$.

*Proof.* The kernel is written as the sum of its value at $y=x$ plus the difference; the difference
is integrable by the homogeneity of $E$, and the excision of a small ball about $x$ isolates the
principal value. Inside the ball the kernel is that of the Laplacian's fundamental solution, and its
flux over the half-sphere gives the terms $\pm\tfrac12 h$; the outside contribution is the principal
value. The computation is the classical one, carried out in the Clifford setting in *Clifford
Analysis* and *Hypercomplex Integration*; the two displays are quoted there and used here. $\square$

**Corollary (the jump and the sum).** The two formulae give

$$
\mathcal{C}^+h-\mathcal{C}^-h = h , \qquad \mathcal{C}^+h+\mathcal{C}^-h = 2\,\mathcal{S}h ,
$$

so the jump of the transform across the surface is the density, and the singular operator is the
mean of the two traces.

**Corollary (reality of the surface for a monogenic function).** If $F$ is monogenic on $\Omega$
with continuous extension to $\bar\Omega$, its Cauchy integral is $F$ itself, so the first formula
reads $F^+=\tfrac12 F|_\Gamma+\mathcal{S}(F|_\Gamma)$, the boundary version of the Cauchy integral
formula.

### The Involution

**Theorem (the singular operator is an involution).** On a smooth surface $\Gamma$ the singular
Cauchy operator satisfies

$$
\mathcal{S}^2 = I
$$

on the space of densities for which it is defined as a bounded operator.

*Proof.* Apply the Plemelj formulae to the two functions $\mathcal{C}^+h$ and $\mathcal{C}^-h$; both
are monogenic off $\Gamma$ and are themselves represented by the Cauchy transform of their boundary
values. The double-layer potentials of a monogenic function reproduce it, which expresses
$\mathcal{C}^\pm$ as the projections of the trace space onto the two complementary subspaces; since
$\mathcal{C}^\pm=\tfrac12(\mathcal{S}\pm I)$, idempotency of either projection is equivalent to
$\mathcal{S}^2=I$. The Clifford proof is the one of the classical complex case, with the kernel and
the conormal element in place of $dz/(z-\zeta)$. $\square$

**Corollary (the projections).** The operators

$$
P^+ = \tfrac12(I+\mathcal{S}) = \mathcal{C}^+ , \qquad
P^- = \tfrac12(I-\mathcal{S}) = -\mathcal{C}^- , \qquad
P^+ + P^- = I , \qquad P^+P^- = P^-P^+ = 0
$$

are the **complementary projections** of the trace space, and they are orthogonal when the surface
is smooth and the space is $L^2(\Gamma)$. The image of $P^+$ is the space of boundary values of
monogenic functions on $\Omega$, and the image of $P^-$ is the space of boundary values of monogenic
functions vanishing at infinity on the exterior.

**Remark (the complex case).** For $m=1$ and $A\cong\mathbb{C}$ the surface is a contour, the kernel
is $1/(2\pi i(\zeta-z))$, the singular operator $\mathcal{S}$ is the classical Hilbert transform on
the contour, and the projections $P^\pm$ are the Szegő projections onto the boundary values of
holomorphic functions inside and outside. The whole of the classical boundary theory of holomorphic
functions is the case $m=1$ of the statements above.

## The Volume Transform

### The Teodorescu Transform

**Definition.** On a bounded domain $\Omega$ the **Teodorescu transform** of a continuous function
$f:\Omega\to\mathcal{S}$ is

$$
(\mathcal{T}_\Omega f)(x) = \int_\Omega E(x-y)\,f(y)\,dy , \qquad x\in\Omega .
$$

**Theorem (the volume transform inverts the operator).** On a domain $\Omega$ with sufficiently
regular boundary,

$$
D\,\mathcal{T}_\Omega = I , \qquad \mathcal{T}_\Omega\,D = I - \mathcal{C}_{\partial\Omega}
$$

on the classes for which the operators are defined; the second identity is the operator form of the
Cauchy–Pompeiu formula.

*Proof.* The kernel satisfies $D_xE(x-y)=\delta_0(x-y)$ by the theorem on the fundamental solution
of *The Dirac Operator*; differentiating under the integral sign gives the first identity. The
second is the Cauchy–Pompeiu formula of *Clifford Analysis*,
$f=\mathcal{C}_{\partial\Omega}f-\mathcal{T}_\Omega(Df)$, read as an operator identity on $f$.
$\square$

**Corollary (a right inverse and the monogenic class).** The Teodorescu transform is a right inverse
of $D$ on $\Omega$, and its kernel is exactly the boundary transform's: a function $f$ on $\Omega$
is monogenic precisely when $f=\mathcal{C}_{\partial\Omega}f$, that is, when
$\mathcal{T}_\Omega(Df)=0$.

**Remark (the volume transform on all of $\mathbb{R}^{m+1}$).** On the whole space the Teodorescu
transform is the convolution with $E$, the distributional inverse of $D$; it is the operator whose
symbol is $\sigma(\xi)^{-1}$ in the sense of *The Dirac Operator*, and its study on
$\mathbb{R}^{m+1}$ is the study of the elliptic operator $D$ by its parametrix, as in *Harmonic
Analysis over Hypercomplex Systems*.

## Mapping Properties

### Boundedness of the Singular Operator

**Theorem (Coifman–McIntosh–Meyer, quoted).** Let $\Gamma$ be a Lipschitz surface with a small
Lipschitz constant. Then the singular Cauchy operator $\mathcal{S}$ extends to a bounded operator on
$L^2(\Gamma;\mathcal{S})$ and, with the kernel $E(x-y)\nu_B(y)$ homogeneous of degree $-(m-1)$ on
$\Gamma$ and odd, to a bounded operator on $L^p(\Gamma;\mathcal{S})$ for a range of $p$ around $2$.

*Proof.* Quoted from the Clifford form of the Calderón–Zygmund theory; the kernel of $\mathcal{S}$
is a singular integral kernel of the standard type, its restriction to the surface is homogeneous of
degree $-(m-1)$ and odd, and the theorem of Coifman–McIntosh–Meyer supplies the $L^2$ boundedness
for Lipschitz surfaces with small constant; the $L^p$ statement follows from the $L^2$ result by
interpolation and duality in the range in which the operator is of weak type. The Clifford case with
operator-valued kernels is the one developed in *Harmonic Analysis over Hypercomplex Systems* and
*Clifford Analysis*. $\square$

**Remark (the measure-theoretic refinements).** When the boundary carries only a Federer normal, or
is a fractal of Hausdorff dimension $d$ strictly between $m$ and $m+1$, there is no boundary measure
to integrate against, and the boundary transform is replaced by the Teodorescu transform together
with a Whitney extension of the datum; the trace of the new transform is the fractal Hilbert
transform, and the Plemelj calculus holds with an approximate dimension in place of the metric one.
This is the measure-theoretic boundary theory of *Clifford Analysis*, and it is not repeated here.

### The Range and the Hardy Space

**Definition.** For a domain $\Omega$ with smooth boundary $\Gamma$, the **monogenic Hardy space**
is

$$
H^2(\Omega) = \{F:\Omega\to\mathcal{S} \text{ monogenic}\ :\ \sup_{t>0}\textstyle\int_{\Gamma_t}|F|^2\,dS<\infty\} ,
$$

where $\Gamma_t$ are the level surfaces receding from $\Gamma$ inside $\Omega$.

**Theorem (the boundary values and the projection).** The space $H^2(\Omega)$ is a Hilbert space,
the boundary trace $F\mapsto F|_\Gamma$ is an isometry onto a closed subspace of $L^2(\Gamma)$, and
that subspace is the range of $P^+$; the orthogonal projection of $L^2(\Gamma)$ onto it is
$P^+=\tfrac12(I+\mathcal{S})$.

*Proof.* The hard part is that $P^+$ is a projection, which is the involution theorem above; given
it, the reproducing kernel of the range is the Cauchy kernel, and the Cauchy integral formula
identifies the monogenic extensions with the elements of the range. The statement is the Clifford
form of the classical Hardy-space theorem; its development is *Clifford Analysis*'s and the general
theory of the boundary value map is *Hypercomplex Integration*'s. $\square$

**Remark (the two realisations of one operator).** The Cauchy integral operator has two faces. As a
boundary operator, $\mathcal{S}=2\,\mathcal{C}^+-I$ is the odd part of the traces, and it is the
Hilbert transform of the surface; as a volume operator, $\mathcal{T}_\Omega$ inverts $D$ and
reconstructs the function from its data. The link between them is the Cauchy–Pompeiu formula, which
reads the failure of $\mathcal{T}_\Omega D$ to be the identity as the boundary projection. Without
the surface — on all of $\mathbb{R}^{m+1}$ — only the second face survives, and the operator is the
parametrix of $D$.

## Summary

The Cauchy kernel $E$ of *Clifford Analysis* defines two operators. The boundary Cauchy transform
$\mathcal{C}_\Gamma h(x)=\int_\Gamma E(x-y)\nu_B(y)h(y)dS(y)$ maps a density on a surface $\Gamma$
to a monogenic function off it, with one-sided traces $\mathcal{C}^\pm h=\pm\tfrac12h+\mathcal{S}h$,
whose difference is the density and whose mean is the singular Cauchy operator
$\mathcal{S}h=2\,\mathrm{p.v.}\!\int_\Gamma E\nu_Bh\,dS$. On a smooth surface $\mathcal{S}^2=I$, so
$P^\pm=\tfrac12(I\pm\mathcal{S})=\pm\mathcal{C}^\pm$ are complementary projections of the trace
space, the joint statement of the Plemelj–Sokhotski formulae and the classical continuation
principle; the image of $P^+$ is the monogenic Hardy space $H^2(\Omega)$, and the orthogonal
projection onto it is the Cauchy transform. On a Lipschitz surface with small constant,
$\mathcal{S}$ is bounded on $L^2$ and on an interval of $L^p$ spaces by the Clifford form of the
Coifman–McIntosh–Meyer theorem, the kernel being homogeneous of degree $-(m-1)$ and odd. The volume
Teodorescu transform $\mathcal{T}_\Omega f(x)=\int_\Omega E(x-y)f(y)dy$ is a right inverse of $D$,
and $\mathcal{T}_\Omega D=I-\mathcal{C}_{\partial\Omega}$ is the Cauchy–Pompeiu formula read as an
operator identity. For $m=1$ the article is the classical theory of the Hilbert transform and the
Szegő projection. The function theory is *Clifford Analysis*'s, the general integration theory is
*Hypercomplex Integration*'s, the boundary-value problems are *Riemann Boundary Value Problems and
Singular Integral Equations*', the Fourier and Calderón–Zygmund reading is *Harmonic Analysis over
Hypercomplex Systems*', and the Hermitian refinement is *The Hermitian Cauchy Integral and the
Boundary Values*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E(x-y)=\omega_m^{-1}(x-y)^{\natural}|x-y|^{-m-1}$ | Cauchy kernel |
| $\nu_B=\sum_\mu\nu_\mu e_\mu$ | Conormal element |
| $\mathcal{C}_\Gamma h$ | Boundary Cauchy transform of a density |
| $\mathcal{C}^\pm h=\pm\tfrac12 h+\mathcal{S}h$ | One-sided traces; Plemelj–Sokhotski |
| $\mathcal{S}=2\,\mathrm{p.v.}\!\int_\Gamma E\nu_B(\cdot)dS$ | Singular Cauchy operator, the Hilbert transform of $\Gamma$ |
| $P^\pm=\tfrac12(I\pm\mathcal{S})$ | Complementary projections; $\mathcal{S}^2=I$ |
| $\mathcal{T}_\Omega f=\int_\Omega E(x-\cdot)f$ | Teodorescu transform; $D\mathcal{T}_\Omega=I$ |
| $H^2(\Omega)$ | Monogenic Hardy space; range of $P^+$ |
| $\Gamma,\ dS$ | Boundary surface and surface measure |

## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy transform, the Plemelj formulae and the Hardy space.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the boundary value theory of monogenic functions.
- Ronald R. Coifman, Alan McIntosh and Yves Meyer, "L'integrale de Cauchy définit un opérateur borné sur les courbes lipschitziennes", *Annals of Mathematics* 116 (1982), for the $L^2$ boundedness of the singular Cauchy operator.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the Teodorescu transform and its applications.
- John Ryan (ed.), *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the boundary-value problems of the theory.
- Marius Mitrea, *Clifford Wavelets, Singular Integrals, and Hardy Spaces* (Springer, 1994), for the Hardy-space and singular-integral theory of the Clifford Cauchy operator.
