# __The Local Complex Structure and the Speed of Light__

## Introduction

The biquaternion framework reads the Lorentzian signature of spacetime as a consequence of a complex structure rather than as an independent postulate. The minus sign in the Minkowski interval
$$
ds^2=-c^2\,dt^2+d\mathbf x^2
$$
is, in this reading, the sign of $i^2$; it is not put into the metric by hand. That much is inherited. This article isolates the structure that does the work and asks what, precisely, it is a structure *on*. The answer turns on a distinction that is easy to blur: **no global complex structure compatible with the Minkowski metric is available on spacetime, but a local one is**, and the speed of light $c$ is the single scale that converts the local structure into the Minkowski metric.

The parent of this article is *Electromagnetism in Media — The Local Complex Structure at Work*, where the local structure is used in a material medium. There the medium supplies the general case and the vacuum is its limit. Here the subject is the structure itself and its relation to the speed of light; the medium appears only as the setting in which the local structure is seen to vary from point to point. The distinction between the global and the local statement is the organising theme, and every step below says which of the two is being claimed.

Throughout, the notation is inherited unchanged from the read-list articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$ and scalar imaginary $i$ commuting with the quaternion units. The two complementary four-dimensional real subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector; the material sector) and $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector; the informational sector), with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$. The real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, the scalar subspace is $\mathbb{C}_{\mathbb{B}}$, and the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. The norm form is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$. The speed of light in the medium is $c=1/\sqrt{\epsilon\mu}$ and the vacuum speed is $c_0=1/\sqrt{\epsilon_0\mu_0}$; in vacuum $c=c_0$. One symbol is introduced here and used only here: $J$ denotes an abstract complex structure, and $J_{\mathbb{B}}$ the specific map $\tilde{Q}\mapsto i\tilde{Q}$ on $\mathbb{B}$.

## Two Senses of "Complex Structure"

A **complex structure** on a real vector space $V$ is a real-linear map $J:V\to V$ with
$$
J^2=-I .
$$
Its effect is to make $V$ a complex vector space: defining $(a+bi)v=av+b\,Jv$ gives a product that is complex-linear in the scalar $a+bi$. A complex structure therefore forces $\dim_{\mathbb R}V$ to be even; on $\mathbb R^4$ it is the algebraic content of simultaneous rotations by $90^\circ$ in two independent planes.

The biquaternion algebra carries one such map, and it is part of the algebra rather than a choice imposed on it: left multiplication by the scalar imaginary,
$$
J_{\mathbb{B}}:\tilde{Q}\longmapsto i\,\tilde{Q}, \qquad J_{\mathbb{B}}^2=-e_0 .
$$
This $J_{\mathbb{B}}$ is defined on all of $\mathbb{B}$ and is the same everywhere. On the eight-real-dimensional algebra it is a genuine complex structure, global in the strongest sense: it depends on no medium and no frame, and it is exactly the $i$ of the $ict$ convention.

The question of this article is whether $J_{\mathbb{B}}$ — or any other complex structure — is a complex structure **on spacetime**. Three distinct levels must be kept apart, because a statement at one level is easily mistaken for a statement at another.

1. **The algebra $\mathbb{B}$.** Here $J_{\mathbb{B}}$ is a complex structure, globally and exactly.
2. **Spacetime, the material sector $\mathbb{M}_-$.** This is a four-dimensional *real* vector space carrying the norm form of signature $(3,1)$. Here the question is whether a complex structure exists that is compatible with that form.
3. **The complexified local tangent space.** Here multiplication by $i$ is again a complex structure, but on a larger space; it is not a structure *on* the real tangent space.

A local statement can be true while the corresponding global statement is false, and the two are not interchangeable. The next two sections separate the levels.

## Why the Global Structure Is Not Available

### The algebra's complex structure does not preserve spacetime

The material sector $\mathbb{M}_-$ consists of the elements with imaginary scalar part and real vector part, so a real basis is $\{ie_0,e_1,e_2,e_3\}$. Multiplication by $i$ exchanges the two sectors:
$$
i\,\mathbb{M}_-=\mathbb{M}_+, \qquad i\,\mathbb{M}_+=\mathbb{M}_- .
$$
A general element $i q_0e_0+\mathbf q$ of $\mathbb{M}_-$ is sent to $-q_0e_0+i\mathbf q$, which has a real scalar part and an imaginary vector part, hence lies in $\mathbb{M}_+$ and not in $\mathbb{M}_-$ unless it vanishes. Therefore $J_{\mathbb{B}}$ is not an endomorphism of $\mathbb{M}_-$: it does not map spacetime to itself, so it cannot be a complex structure *on* spacetime. Geometrically it is the map that exchanges the material and informational sectors.

### The Minkowski metric admits no compatible complex structure

The second obstruction is independent of the algebra and concerns any real complex structure on the material sector. Suppose a real-linear $J$ satisfied both $J^2=-I$ and the compatibility
$$
N(JX,JY)=N(X,Y) \qquad \text{for all } X,Y,
$$
which is the condition that the complex structure be an isometry of the norm form. Two elementary identities follow. Taking $Y=JX$ and using $J^2=-I$ and the symmetry of $N$,
$$
N(JX,-X)=N(X,JX) \;\Longrightarrow\; -N(X,JX)=N(X,JX) \;\Longrightarrow\; N(X,JX)=0 ,
$$
so a vector and its image under $J$ are orthogonal. Taking $Y=X$,
$$
N(JX,JX)=N(X,X).
$$
Hence on the two-dimensional plane $\mathrm{span}\{X,JX\}$, whenever $N(X,X)\neq0$, the form is definite with the sign of $N(X,X)$: the plane has signature $(2,0)$ or $(0,2)$, never $(1,1)$. The orthogonal complement of a $J$-invariant plane is itself $J$-invariant, because for $Y$ orthogonal to the plane and $Z$ in the plane,
$$
N(JY,Z)=N(J^2Y,JZ)=-N(Y,JZ)=0,
$$
using compatibility in the first equality and $JZ$ in the plane in the last. Iterating, a four-dimensional space is an orthogonal direct sum of two such planes, so its signature is $(4,0)$, $(2,2)$ or $(0,4)$. The norm form of $\mathbb{M}_-$ has signature $(3,1)$: three positive directions and one negative. It is not in the list. Therefore **no complex structure compatible with the Minkowski metric exists**, neither globally nor at a single point.

The obstruction is easy to check directly. In two dimensions, writing $g=\begin{pmatrix}p&q\\q&r\end{pmatrix}$ and $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, the condition $J^{\mathsf T}gJ=g$ forces $p=r$ and $q=0$: the compatible form is a multiple of the identity, hence definite, of signature $(2,0)$ or $(0,2)$, never $(1,1)$. In four dimensions the forms compatible with a complex structure have eigenvalues each of multiplicity two, so each sign occurs an even number of times — the signature is $(4,0)$, $(2,2)$ or $(0,4)$; a symbolic solution of $J_0^{\mathsf T}GJ_0=G$ for the standard $J_0$ returns a form whose eigenvalues each occur twice. A count of three positives and one negative cannot arise, and the signature $(3,1)$ is exactly the excluded case.

The way out is not to look for a better $J$ but to change the space: **complexify**. On the complexified tangent space the form is complex, and multiplication by $i$ is a complex structure there. This is what the $ict$ notation does, and it is why the framework complexifies spacetime rather than placing a real $J$ on it. The distinction is not pedantic: a complex structure on the complexified tangent space is a different object from a complex structure on spacetime compatible with the Minkowski metric, and the second does not exist. Calling $ict$ "a complex structure on spacetime" is the conflation this article is written to avoid.

### The global $ict$ is a coordinate device

The $ict$ convention is often described as making the complex structure global. It is worth being exact about what is global there. The substitution $x^0=ic_0t$ is a change of coordinates, and it converts the Minkowski interval into a Euclidean form,
$$
ds^2=(ic_0\,dt)^2+d\mathbf x^2 .
$$
As a device it requires two things that are not generally available: a single time coordinate defined everywhere, and a single constant scale $c_0$. Flat spacetime with a fixed inertial frame supplies both, which is why the convention works in the vacuum of special relativity. It fails for a curved metric, it sits awkwardly with spinors, and — the case that matters here — it fails when the scale $c$ is a field rather than a constant. In a medium with $\epsilon=\epsilon(\mathbf x)$ and $\mu=\mu(\mathbf x)$ the complex time coordinate is $i\,c(\mathbf x)t$, defined only pointwise. The global $ict$ is therefore the constant-$c$, flat-space limit of a local structure; it is not a global complex structure on spacetime. The companion article *Why Complexify Spacetime?* records the first two limitations.

## The Local Structure That Is Available

What is available at every point is the following. The material tangent space at a point has the real basis $\{ie_0,e_1,e_2,e_3\}$. Choose the temporal direction of the local frame and map it to the imaginary scalar generator by
$$
t \;\longmapsto\; i\,c\,t\,e_0 ,
$$
with $c>0$ a local scale. Equivalently, the temporal coordinate of $\mathbb{M}_-$ is $ict$, with $c$ allowed to depend on the point — and, in a dispersive medium, on the frequency. This is the **local complex structure**: the phase is the algebra's fixed $i$, and the scale is the local $c$.

Three features of this definition are the content of its locality.

- **Only the scale varies.** Because $c$ is real and positive, the map is a rescaling of the imaginary axis, not a rotation of it. The phase of the complex structure is the same $i$ at every point; the structure does not point in different directions in different places. This is the precise sense, used in the parent article, in which the structure is local: the algebra is fixed, and the embedding of physical time into it carries the local factor $c(\mathbf x)$.
- **It is pointwise, not holomorphic.** The local structure is an identification on the local tangent space at each point. It is not a system of holomorphic coordinates and it does not make spacetime a complex manifold, since by the previous section no such structure exists. In flat spacetime with constant $c$ the pointwise identifications fit together and the structure becomes global; in general they do not.
- **It requires a scale.** The coordinate $ict$ is a length and $t$ is a time, so the map $t\mapsto ict$ is dimensionally consistent only because $c$ is a speed. Without a scale, the statement "the temporal direction is imaginary" has no metric content. The local complex structure is therefore not a structure that merely *has* a scale; it is a structure *with* a scale, and that scale is $c$.

At each point the local structure induces the quadratic form of the material sector. With $d\tilde{X}=ic\,dt\,e_0+d\mathbf x$,
$$
N(d\tilde{X})=(ic\,dt)^2+d\mathbf x^2=-c^2\,dt^2+d\mathbf x^2 .
$$
This is the Minkowski interval with the local speed $c$. The signature is produced by the complex structure, and the one number that remains free — the scale of the imaginary time axis — becomes the coefficient $c^2$ in the metric.

## The Scale $c$ and the Minkowski Metric

The sentence "the complex structure produces the metric" has two parts, and it is worth separating them.

1. **The signature is algebraic.** The sign of the coefficient on $dt^2$ is $(i)^2$. It comes from the scalar imaginary and is the same for every value of $c$. In the metric formalism the signature is an input; here it is a consequence of the algebra.
2. **The magnitude is local.** The coefficient is $-c^2$, with $c$ the scale of the imaginary time axis. In the coordinate basis $(\partial_t,\partial_x,\partial_y,\partial_z)$,
$$
g_{\mu\nu}=\mathrm{diag}\!\left(-c^2,\,1,\,1,\,1\right),
\qquad
ds^2=g_{\mu\nu}\,dx^\mu dx^\nu=-c^2\,dt^2+d\mathbf x^2 .
$$

So $c$ is the conversion factor that turns the statement "time is imaginary" into a statement about lengths. The phase $i$ says that the temporal direction is the imaginary one; the scale $c$ says how much imaginary time corresponds to a unit of physical time, and therefore how the temporal direction is measured against the three spatial directions. Given the phase and the scale, the metric is determined.

For constant $c$ the metric is $c^2\left(-dt^2+d\mathbf x^2/c^2\right)$, so after the constant rescaling $\mathbf x\to\mathbf x/c$ it is $c^2$ times the Minkowski metric: the null structure is Minkowski's and the coordinate speed of light is $c$. For varying $c$ the metric is a field of local forms,
$$
g(\mathbf x)=\mathrm{diag}\!\left(-c(\mathbf x)^2,\,1,\,1,\,1\right),
$$
and at each point the null directions are those with $|d\mathbf x/dt|=c(\mathbf x)$. The metric is not postulated alongside the complex structure; it is read off from the phase and the local scale.

Two cautions belong here. First, this is not a claim that a medium produces the Gordon-type effective metric of a moving dielectric. The local structure considered here is isotropic and is written in the local rest frame of the material; the constitutive relations of a moving or anisotropic medium carry more data than the local complex structure, and their geometric reading is a separate question. Second, the field $g(\mathbf x)$ is obtained pointwise. Nothing global is asserted about it: there is no claim that the pointwise forms are the coordinate components of a single smooth metric in a preferred global frame, nor that a global Lorentz invariance survives the variation of $c$. That last point is taken up again below.

## Two Routes by Which $c$ Is Fixed

The local structure leaves one number undetermined: the scale $c$. The physics does not leave it undetermined. Two independent requirements fix it, and they agree.

**Route 1: the null cone of the norm form.** The local quadratic form vanishes on
$$
(ic\,dt)^2+d\mathbf x^2=0
\;\Longleftrightarrow\;
|d\mathbf x|=c\,|dt| ,
$$
so the aperture of the local null cone is exactly $c$. These null directions are the zero divisors of the algebra at the point, and they are the local light cone. Read as a statement about the structure alone, this fixes what $c$ has to be for a null signal: of the scales that could be attached to the imaginary time axis, the ones whose zero-divisor cone is the light cone are those with aperture $c$. The null-cone route uses the quadratic form and nothing else.

**Route 2: the characteristics of the wave operator.** The biquaternionic gradient and its quaternion conjugate multiply to the d'Alembertian,
$$
\Box=\tilde{\nabla}\bar{\tilde{\nabla}}
=\partial_{ict}^2+\Delta
=\Delta-\frac{1}{c^2}\,\partial_t^2 ,
$$
which is the wave operator of a medium whose light speed is $c$. Independently, Maxwell's equations in a linear medium reduce to
$$
\Box_{em}=\Delta-\frac{1}{c_{em}^2}\,\partial_t^2,
\qquad
c_{em}=\frac{1}{\sqrt{\epsilon\mu}},
$$
and plane waves satisfy $k^2=\omega^2\epsilon\mu$, so the characteristic speed of the medium's operator is $c_{em}$. The local complex structure's operator has characteristic speed $c$; the medium's has characteristic speed $c_{em}$. They are the same operator only if
$$
c=c_{em}=\frac{1}{\sqrt{\epsilon\mu}} .
$$
The wave-operator route uses the field equation and the constitutive relations, and nothing about the null cone of the norm form.

**Independence and agreement.** Route 1 is geometric: it reads $c$ off a quadratic form. Route 2 is dynamical: it reads the same $c$ off a differential operator and the medium's constitutive relations. Neither determines the numerical value of $c$ — that is empirical, as it is in the metric formalism — but together they fix what $c$ is *for*: it is at once the aperture of the local light cone and the characteristic speed of the medium's electrodynamics, and there is exactly one number doing both jobs. This is the precise sense in which $c$ is fixed by the local structure rather than postulated alongside it. In the metric formalism one writes $-c^2dt^2$ and, separately, $\mathbf D=\epsilon\mathbf E$ and $\mathbf B=\mu\mathbf H$; the appearance of the same $c$ in both places is a consistency to be checked. Here it is a single scale with a single role.

## Limits of the Local Reading

Four boundaries should be stated, so that the local claim is not read as a global one.

1. **No empirical content is added.** The algebraicity of the signature and the identity $c=1/\sqrt{\epsilon\mu}$ are both known. The local structure is a repackaging of them, not a new prediction, and it does not distinguish the framework from standard electromagnetism in a medium. Whether the framework has any empirical consequence remains the open question it is elsewhere in the corpus.
2. **The scale must be real.** In a transparent frequency window $c(\omega)$ is real and the rescaling of the imaginary axis is a real one. Near an absorption line $\epsilon$ and $\mu$ become complex, so $c$ becomes complex, and the rescaling becomes a complex rotation; the scale can no longer be read as the aperture of a real null cone. This is a boundary of the structure as written, recorded in the parent article and not repaired here.
3. **Only the pointwise Lorentz invariance survives when $c$ varies.** For constant $c$ the interval is invariant under the full Lorentz group and the invariance is global. For $c=c(\mathbf x)$, a constant Lorentz transformation mixes $t$ and $\mathbf x$ and therefore does not preserve $g(\mathbf x)$: only the pointwise invariance remains. No global Lorentz invariance of a variable metric is claimed here. This is the same local/global caution in group-theoretic form.
4. **Curved spacetime is a further step.** The structure described here is a tangent-space statement at a point. Its extension to a curved manifold requires a tetrad or spin connection, and it is treated separately in the corpus; nothing in the present article assumes or establishes that extension.

## Summary

The Lorentzian signature of spacetime is algebraic in the biquaternion framework: the minus sign in $ds^2=-c^2dt^2+d\mathbf x^2$ is the sign of $i^2$. What this article has separated is the sense in which the complex structure that produces it is, and is not, available.

A **global** complex structure on spacetime, in the sense the question requires — an endomorphism of $\mathbb{M}_-$ compatible with its norm form — is not available, on two independent grounds. First, the algebra's complex structure $J_{\mathbb{B}}:\tilde{Q}\mapsto i\tilde{Q}$ exchanges the two sectors, $i\mathbb{M}_-=\mathbb{M}_+$, so it is not an endomorphism of the material sector. Second, and independently of the algebra, no real complex structure compatible with the Minkowski metric exists at all: compatibility with $J^2=-I$ forces the metric to be an orthogonal sum of definite two-planes, in which each sign occurs an even number of times, while the norm form of $\mathbb{M}_-$ has signature $(3,1)$. The $ict$ convention is not a counterexample; it is a complexification of the coordinates, a different object, and its global use is limited to flat spacetime with a constant scale.

A **local** structure is available, and it is the following pointwise data: the temporal direction is identified with the imaginary scalar generator with a local scale $c$, so that the temporal coordinate is $ict$ with $c=c(\mathbf x)$ — and $c(\omega)$ in a dispersive medium. The phase is the algebra's fixed $i$; only the scale varies, and because $c$ is real and positive the map rescales the imaginary axis rather than rotating it. At each point the induced quadratic form is $-c^2dt^2+d\mathbf x^2$, so the local complex structure produces the local Minkowski metric with its one free number, $c$.

That number is fixed by the local structure on two independent routes, and they agree. The null cone of the norm form has aperture $c$. The characteristic speed of the local wave operator $\Box=\partial_{ict}^2+\Delta=\Delta-c^{-2}\partial_t^2$ must equal the characteristic speed $c_{em}=1/\sqrt{\epsilon\mu}$ of the medium's Maxwell equations, so $c=c_{em}$. The numerical value of $c$ remains empirical, as in the metric formalism; what is fixed is its role.

The reading closes no empirical gap and claims no global structure. Its content is that the signature is algebra, the scale is local, and the one scale is the speed of light.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{C}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}$ | Scalar subspace, real-quaternion subspace |
| $\mathbb{M}_+,\mathbb{M}_-$ | Hermitian (informational), anti-Hermitian (material) subspaces |
| $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ | Sector decomposition; $i\mathbb{M}_-=\mathbb{M}_+$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$ | Norm form; zero divisors where $N=0$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula |
| $J^2=-I$ | Abstract complex structure |
| $J_{\mathbb{B}}:\tilde{Q}\mapsto i\tilde{Q}$ | Complex structure of the algebra |
| $\tilde{X}=ic\,t\,e_0+\mathbf x$ | Four-position of the material sector |
| $g_{\mu\nu}=\mathrm{diag}(-c^2,1,1,1)$ | Local metric induced by the local complex structure |
| $ds^2=-c^2dt^2+d\mathbf x^2$ | Interval; null cone $|d\mathbf x/dt|=c$ |
| $c=1/\sqrt{\epsilon\mu}$, $c_0=1/\sqrt{\epsilon_0\mu_0}$ | Medium speed, vacuum speed |
| $\tilde{\nabla}=e_0\partial_{ict}+\nabla$, $\bar{\tilde{\nabla}}$ | Biquaternionic gradient and its quaternion conjugate |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta=\Delta-c^{-2}\partial_t^2$ | d'Alembertian |
| $x^0=ict$ | Complex time coordinate |

## Further Reading

- *Introduction to the Biquaternion Universe*, for the two sectors, the local complex structure, and the statement that $c=1/\sqrt{\epsilon\mu}$ is the local scale factor of the structure.
- *Why Complexify Spacetime?*, for the $ict$ convention, the $SO(4,\mathbb C)$ rotation picture, and the limitations of the global convention.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the norm form of signature $(3,1)$, the basis $\{ie_0,e_1,e_2,e_3\}$, and the zero-divisor light cone.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the complementary sector and the exchange $i\mathbb{M}_-=\mathbb{M}_+$ by multiplication by $i$.
- *A Brief History of Biquaternions in Physics*, for the displacement of the $ict$ convention and its relation to the abandonment of the complex formalism.
- *Electromagnetism in Media — The Local Complex Structure at Work*, the parent article, for the medium conventions, the local and spectral scale $c(\omega)$, and the boundaries of the structure near absorption.
- *Maxwell's Equations in the Biquaternionic Formulation*, for the biquaternionic gradient, the d'Alembertian, and the medium form of Maxwell's equations.
- *The Field-Strength Biquaternion and Its Invariants*, for the field-strength normalisation that uses the same scale $c$ and the two medium parameters.
- *The Wick Rotation in the Biquaternion Universe*, for the Euclidean continuation and the sense in which the imaginary time direction carries thermodynamic content.
- *Curved Spacetime and the Biquaternion Framework*, for the tetrad and spin-connection extension that the local structure requires beyond a single tangent space.
