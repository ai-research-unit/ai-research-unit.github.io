# __The Fubini–Study Geometry and the Biquaternion Norm Form__

## Introduction

The state space of the qubit is a ball, and the geometry of its boundary is the Fubini–Study geometry of the projective line $\mathbb{P}^1(\mathbb{C})$. The companion articles established the ball as the trace-one slice of the future light cone of the norm form of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the pure states on the boundary and the mixed states in the interior. The present article establishes the **metric geometry** of that slice: the Fubini–Study metric on the pure states and its standard Bures extension to the mixed states are read off from the two forms the algebra already supplies, the norm form and the trace pairing.

The result is a division of labour between the two forms, and it is worth stating before any algebra is written.

- The **trace pairing** fixes the *transition probability*. On pure states it gives $\mathrm{Tr}(\tilde{P}(\hat{\mu})\tilde{P}(\hat{\nu})) = \tfrac12(1+\hat{\mu}\cdot\hat{\nu}) = \cos^2(\theta/2)$, the squared overlap of the corresponding rays.
- The **norm form** fixes the *metric*. It vanishes identically on the pure states, so it cannot itself be a metric there; what it gives is the line element at second order, and the result is

$$
ds^2_{\mathrm{FS}} \;=\; -\,N\!\left(\delta\tilde{P}\right)\Big|_{\text{tangential}} \;=\; \tfrac14\,\bigl|d\hat{\mu}\bigr|^2 \;=\; \tfrac14\left(d\theta^2+\sin^2\theta\,d\varphi^2\right),
$$

the Fubini–Study line element of $\mathbb{P}^1(\mathbb{C})$, equal to one quarter of the round metric of the Bloch sphere. The factor $\tfrac14$ is the spinorial factor: it is the square of the ratio between the angle on the ray space and the angle on the Bloch sphere, that ratio being the half-angle $\tfrac12$ of the double cover $SU(2)\to SO(3)$.

Three further results complete the picture. The Fubini–Study metric is **Kähler**: its complex structure is the central scalar imaginary $i$ acting on the state module, and its symplectic form is, up to a factor, the trace of the algebra commutator,
$$
\omega \;=\; -\tfrac12\, i\,\mathrm{Tr}\!\left(\tilde{P}\,[\delta_1\tilde{P},\delta_2\tilde{P}]\right) \;=\; \tfrac14\,\hat{\mu}\cdot(\delta_1\hat{\mu}\times\delta_2\hat{\mu}).
$$
The **geodesic distance** is $d_{\mathrm{FS}}(\tilde{P},\tilde{Q}) = \arccos\lvert\langle\psi|\phi\rangle\rvert = \theta/2$, so that the trace distance of the companion article *Exercise: The Bloch Ball and the Geometry of Mixed States* is the sine of the Fubini–Study distance, $D = \sin d_{\mathrm{FS}}$. And on the interior the metric is the **Bures metric**, whose boundary restriction is the Fubini–Study metric; the flat quadratic form $-\tfrac14|d\mathbf{r}|^2$ that the norm form also supplies is *not* that interior metric, so the norm form gives the boundary exactly and the flat geometry everywhere, but not the metrically distinguished interior.

The article proceeds as follows. The state space and its two forms are recalled; the pure states are identified with the rays of the state module and with the points of $\mathbb{P}^1(\mathbb{C})$; the transition probability is computed from the trace pairing; the Fubini–Study line element is computed from the norm form in two independent ways, from the projector displacement and from the spinor, and the two agree; the complex structure and the Kähler form are exhibited; geodesics and distances are collected; and the Bures extension and the limits of the algebra's own contribution are stated. What the article does not do is the informational reading of the same geometry, which belongs to the informational articles, and the spin-specific readings, which belong to the spin articles.

**Conventions.** The notation is inherited unchanged from the read list. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$ and $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$, and central scalar imaginary $i$ with $i^2=-1$. The Hermitian and anti-Hermitian subspaces are
$$
\mathbb{M}_+=\{\tilde{Q}:\tilde{Q}^\dagger=\tilde{Q}\}=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\},
\qquad
\mathbb{M}_-=\{\tilde{Q}:\tilde{Q}^\dagger=-\tilde{Q}\}=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\},
$$
with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$. The trace is twice the scalar part, $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$, with $\mathrm{Tr}(e_0)=2$, and the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. The norm form is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$, so that on $\mathbb{M}_+$, with $\tilde{H}=h_0e_0+i\mathbf{h}$,
$$
N(\tilde{H})=\bigl(h_0^2-|\mathbf{h}|^2\bigr)e_0 .
$$
A state is $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ with $|\mathbf{r}|\leq1$; a pure state is the idempotent $\tilde{P}_\pm(\hat{\mu})=\tfrac12(e_0\pm i\hat{\mu})$ with $\hat{\mu}$ a unit pure real quaternion. The state module is the minimal left ideal $\mathbb{B}p$ with $p=\tfrac12(e_0+ie_3)$, with matrix units $x=\tfrac12(ie_1-e_2)$, $y=\tfrac12(ie_1+e_2)$ and basis $\{p,y\}$. The unit quaternions act on the Bloch sphere by rotations.

## The State Space and Its Two Forms

An element of the Hermitian subspace is $\tilde{H}=h_0e_0+i\mathbf{h}$ with $h_0\in\mathbb{R}$ and $\mathbf{h}\in\mathbb{R}^3$, and the state space is the trace-one slice of the future cone,
$$
\{\text{states}\}=\left\{\tilde{\rho}\in\mathbb{M}_+:\ \mathrm{Tr}(\tilde{\rho})=1,\ N(\tilde{\rho})\geq0\right\},
\qquad
\tilde{\rho}=\tfrac12(e_0+i\mathbf{r}),\quad |\mathbf{r}|\leq1 .
$$

Two symmetric forms live on the same four-dimensional real space, and the whole geometry of this article rests on keeping them apart.

**The trace pairing.**
$$
\mathrm{Tr}(\tilde{H}\tilde{K})=2\bigl(h_0k_0+\mathbf{h}\cdot\mathbf{k}\bigr)
$$
is positive definite, of signature $(4,0)$; it is the Euclidean pairing on $\mathbb{R}^4$ up to the normalization $\mathrm{Tr}(e_0)=2$, and it is the Hilbert–Schmidt pairing of the matrix model.

**The norm form and its polarization.**
$$
N(\tilde{H})=\tilde{H}\bar{\tilde{H}}=\bigl(h_0^2-|\mathbf{h}|^2\bigr)e_0,
\qquad
B(\tilde{H},\tilde{K})=\tfrac12\bigl(\tilde{H}\bar{\tilde{K}}+\tilde{K}\bar{\tilde{H}}\bigr)=\bigl(h_0k_0-\mathbf{h}\cdot\mathbf{k}\bigr)e_0,
$$
is indefinite, of signature $(1,3)$; its future cone is the positivity cone of the states, and its boundary is the pure states.

The two forms are the two ingredients of the geometry. The trace pairing is positive definite and therefore measures *overlap*; the norm form is indefinite, vanishes on the pure states, and therefore cannot measure *length* on them directly. The point of the article is that the norm form nevertheless determines the length, through its second variation on the null boundary. That is a standard feature of a quadratic form at a null direction — the first variation vanishes, and the second variation carries the geometry — and here it is the whole content of the Fubini–Study metric.

The reader should also keep in mind what these forms are *not*. Neither is the algebra's product; the norm form is the determinant of the matrix model, $N(\tilde{Q})\,e_0=\det M(\tilde{Q})\,e_0$, and the trace pairing is the matrix trace, $\mathrm{Tr}(\tilde{H}\tilde{K})=\mathrm{Tr}(M(\tilde{H})M(\tilde{K}))$. The geometry below is therefore a statement about the matrix model of the algebra, read through the two canonical matrix functionals.

## Pure States and the Projective Line

The boundary of the ball is the sphere $|\mathbf{r}|=1$. On it the norm form vanishes and the deviation from idempotency vanishes,
$$
N(\tilde{\rho})=0,\qquad \tilde{\rho}^2-\tilde{\rho}=\tfrac14\bigl(|\mathbf{r}|^2-1\bigr)e_0=0 ,
$$
so a boundary state is an idempotent of trace one and, in the matrix model, a rank-one projection. Writing it as
$$
\tilde{P}(\hat{\mu})=\tfrac12\bigl(e_0+i\hat{\mu}\bigr),\qquad |\hat{\mu}|=1 ,
$$
the map $\hat{\mu}\mapsto\tilde{P}(\hat{\mu})$ is a bijection from the unit sphere $S^2=\{\hat{\mu}\in\mathbb{R}^3\}$ to the pure states, and $\tilde{P}(\hat{\mu})$ and $\tilde{P}(-\hat{\mu})=e_0-\tilde{P}(\hat{\mu})$ are complementary orthogonal projections.

The pure states have a second, independent parametrization, and the agreement of the two is what makes the projective geometry available. The **state module** is the minimal left ideal
$$
\mathbb{B}p=\{\psi_1\,p+\psi_2\,y:\ \psi_1,\psi_2\in\mathbb{C}\}\cong\mathbb{C}^2,
\qquad
p=\tfrac12(e_0+ie_3),
$$
and its rays $[\psi]=\mathbb{C}\psi$ constitute the projective line $\mathbb{P}^1(\mathbb{C})$. To a nonzero spinor $\psi$ attach the rank-one element
$$
\tilde{P}_\psi=\frac{\psi\,\psi^\dagger}{\mathrm{Tr}(\psi^\dagger\psi)} .
$$
Since $\tilde{P}_\psi\psi=\psi$ and $\tilde{P}_\psi^\dagger=\tilde{P}_\psi$, this is a Hermitian idempotent of trace one; it depends only on the ray, and the map $[\psi]\mapsto\tilde{P}_\psi$ is a bijection from $\mathbb{P}^1(\mathbb{C})$ onto the pure states. Composing the two bijections,
$$
\mathbb{P}^1(\mathbb{C})\ \cong\ S^2\ \cong\ \{\text{pure states}\},
$$
is the standard identification of the projective line with the Bloch sphere. The corresponding spinor is the Bloch spinor of the ray,
$$
|\psi(\theta,\varphi)\rangle=\cos\tfrac{\theta}{2}\,|0\rangle+e^{i\varphi}\sin\tfrac{\theta}{2}\,|1\rangle ,
$$
and the physical equivalence of $\psi$ and $e^{i\alpha}\psi$ is the statement that the phase direction is the fiber of the Hopf map $S^3\to S^2$. The **central scalar imaginary** $i$ supplies that phase: it is central, so left multiplication by $i$ commutes with the left action of $\mathbb{B}$ on the module and gives the module its complex structure. The phase $U(1)$ is a central subgroup, and the quotient by it is the passage from spinors to rays.

Two remarks fix the roles. First, the complex structure used here lives on the **state module** $\mathbb{B}p$, not on $\mathbb{M}_+$: multiplication by $i$ exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, so it is not an operator on the state space. The projective structure is that of the module, and it descends to the boundary of the ball. Second, the pure states are the extreme points of the ball, so the boundary is not merely a convenient subset: it is the set on which the geometry is specified by the algebra's *quadratic* form rather than by the trace.

## The Transition Probability from the Trace Pairing

The trace pairing gives the overlap of two pure states. From the idempotent form and the quaternion product of pure real quaternions, which reads $\hat{\mu}\hat{\nu}=-\hat{\mu}\cdot\hat{\nu}+\hat{\mu}\times\hat{\nu}$,
$$
\tilde{P}(\hat{\mu})\tilde{P}(\hat{\nu})
=\tfrac14\bigl(e_0+i\hat{\mu}\bigr)\bigl(e_0+i\hat{\nu}\bigr)
=\tfrac14\Bigl(\bigl(1+\hat{\mu}\cdot\hat{\nu}\bigr)e_0+i(\hat{\mu}+\hat{\nu})-\hat{\mu}\times\hat{\nu}\Bigr).
$$
The trace keeps only the scalar part,
$$
\boxed{\ \mathrm{Tr}\bigl(\tilde{P}(\hat{\mu})\tilde{P}(\hat{\nu})\bigr)=\tfrac12\bigl(1+\hat{\mu}\cdot\hat{\nu}\bigr)=\cos^2\frac{\theta}{2},\ }
$$
where $\theta$ is the angle between the two Bloch vectors. This is the transition probability of the two pure states, the squared overlap $\lvert\langle\psi|\phi\rangle\rvert^2$, read as a trace of the algebra. On the matrix side it is $\lvert\langle\psi|\phi\rangle\rvert^2$ with the normalized spinors of the preceding section, and the identification is exact:
$$
\lvert\langle\psi(\hat{\mu})|\psi(\hat{\nu})\rangle\rvert^2=\mathrm{Tr}\bigl(\tilde{P}(\hat{\mu})\tilde{P}(\hat{\nu})\bigr).
$$

Two checks fix the normalization. For $\hat{\nu}=\hat{\mu}$ the trace is $1$, as it must be for a probability; for $\hat{\nu}=-\hat{\mu}$ it is $0$, the orthogonal case; for $\hat{\nu}\perp\hat{\mu}$ it is $\tfrac12$, the unbiased case. The quantity is invariant under the whole unitary group, because conjugation by a unitary preserves the trace, and it is the only non-constant unitary-invariant two-point function of the boundary that is bilinear in the two projectors. It is therefore the trace pairing's contribution to the geometry, and it is a *probability*, not a distance: the distance is the angle whose cosine-square it is.

The companion article *Exercise: The Bloch Ball and the Geometry of Mixed States* records the complementary boundary identity for the trace distance,
$$
D\bigl(\tilde{P}(\hat{\mu}),\tilde{P}(\hat{\nu})\bigr)=\tfrac12\bigl|\hat{\mu}-\hat{\nu}\bigr|=\sin\frac{\theta}{2},
\qquad
D^2+\mathrm{Tr}\bigl(\tilde{P}\tilde{Q}\bigr)=1 ,
$$
so that the trace distance and the transition probability carry the same information on the boundary. The Fubini–Study distance introduced in the next section is the remaining side of the same triangle of equivalent data,
$$
d_{\mathrm{FS}}=\frac{\theta}{2}=\arcsin D=\arccos\sqrt{\mathrm{Tr}\bigl(\tilde{P}\tilde{Q}\bigr)} .
$$

## The Fubini–Study Line Element from the Norm Form

The norm form vanishes on the pure states, so it assigns them a *length* zero. What a quadratic form does at a null direction is supply the metric as its second variation, and this section computes that second variation in two independent ways. The first uses the projector displacement, the second the spinor, and their agreement is the derivation of the line element.

### The projector variation

Differentiate the idempotent along the boundary. Since $\tilde{P}(\hat{\mu})=\tfrac12(e_0+i\hat{\mu})$,
$$
\delta\tilde{P}=\tfrac12\,i\,\delta\hat{\mu},\qquad \hat{\mu}\cdot\delta\hat{\mu}=0 ,
$$
the tangency condition being the differentiation of $|\hat{\mu}|^2=1$. The displacement is Hermitian, $\delta\tilde{P}\in\mathbb{M}_+$, with vanishing scalar part. Compute the norm form of the displacement, using that $\overline{\delta\hat{\mu}}=-\delta\hat{\mu}$ for a pure real quaternion and that $(\delta\hat{\mu})^2=-|\delta\hat{\mu}|^2e_0$:
$$
N(\delta\tilde{P})
=\Bigl(\tfrac12 i\,\delta\hat{\mu}\Bigr)\overline{\Bigl(\tfrac12 i\,\delta\hat{\mu}\Bigr)}
=\Bigl(\tfrac12 i\,\delta\hat{\mu}\Bigr)\Bigl(\tfrac12 i\,\overline{\delta\hat{\mu}}\Bigr)
=\Bigl(\tfrac12 i\,\delta\hat{\mu}\Bigr)\Bigl(-\tfrac12 i\,\delta\hat{\mu}\Bigr)
=-\tfrac14\,i^2\,(\delta\hat{\mu})^2
=\tfrac14\,(\delta\hat{\mu})^2
=-\tfrac14\,|\delta\hat{\mu}|^2\,e_0 .
$$

The scalar coefficient is **negative**, so the norm form is negative on tangential displacements; the metric is the negative of the form on those directions, and the Fubini–Study line element is
$$
ds^2_{\mathrm{FS}}=-\,N(\delta\tilde{P})\Big|_{\hat{\mu}\cdot\delta\hat{\mu}=0}
=\tfrac14\,|d\hat{\mu}|^2 .
$$
With $\hat{\mu}=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)$ this is
$$
\boxed{\ ds^2_{\mathrm{FS}}=\tfrac14\left(d\theta^2+\sin^2\theta\,d\varphi^2\right).\ }
$$
The round metric of the unit Bloch sphere is $d\Omega^2=d\theta^2+\sin^2\theta\,d\varphi^2$, so the Fubini–Study metric of the pure states is one quarter of the round metric of the sphere on which the states are drawn. Equivalently, the pure-state manifold is a round sphere of radius $\tfrac12$ with the Fubini–Study normalization, and its total area is $\pi$.

The sign convention in $-N$ deserves a word, because the norm form itself is indefinite and no sign choice can be avoided. On the tangential directions of the boundary the quadratic form is negative, $N(\delta\tilde{P})=-\tfrac14|\delta\hat{\mu}|^2e_0$, as the computation shows; the same displacement written in the $(1,3)$ coordinates of $\mathbb{M}_+$ has negative spatial norm, and the two statements agree. The minus sign in $ds^2_{\mathrm{FS}}=-N(\delta\tilde{P})$ converts the algebra's $(1,3)$ normalization to the positive normalization of a length. This is the precise sense in which the norm form, though indefinite, *does* contain the Fubini–Study metric: the metric is the negative of the form evaluated on the null boundary's tangential directions.

### The spinor computation

The second derivation uses the spinor directly and confirms the first. Let
$$
\psi(\theta,\varphi)=\cos\tfrac{\theta}{2}\,p+\sin\tfrac{\theta}{2}\,e^{i\varphi}\,y
$$
be a normalized spinor, $\mathrm{Tr}(\psi^\dagger\psi)=1$, with $\tilde{P}_\psi=\psi\psi^\dagger$. The Fubini–Study line element of the ray space is
$$
ds^2_{\mathrm{FS}}=\mathrm{Tr}\!\left(d\psi^\dagger\,d\psi\right)-\Bigl|\mathrm{Tr}\!\left(\psi^\dagger d\psi\right)\Bigr|^2 ,
$$
the second term removing the phase direction. With
$$
d\psi=\Bigl(-\tfrac12\sin\tfrac{\theta}{2}\,d\theta\Bigr)p+e^{i\varphi}\Bigl(\tfrac12\cos\tfrac{\theta}{2}\,d\theta+i\sin\tfrac{\theta}{2}\,d\varphi\Bigr)y ,
$$
from which $\partial_\varphi\psi=i\,e^{i\varphi}\sin\tfrac{\theta}{2}\,y$. Using the trace formula $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$, the normalization $\mathrm{Tr}(\psi^\dagger\psi)=1$, and the matrix-unit relations $p^2=p$, $y^2=x^2=0$, $xy=p$, $yx=e_0-p$ with $y^\dagger=x$, the four first derivatives are
$$
\mathrm{Tr}\!\left(\psi^\dagger\partial_\theta\psi\right)=0,
\qquad
\mathrm{Tr}\!\left(\psi^\dagger\partial_\varphi\psi\right)=i\,\sin^2\tfrac{\theta}{2},
\qquad
\mathrm{Tr}\!\left(\partial_\theta\psi^\dagger\partial_\theta\psi\right)=\tfrac14,
\qquad
\mathrm{Tr}\!\left(\partial_\varphi\psi^\dagger\partial_\varphi\psi\right)=\sin^2\tfrac{\theta}{2},
$$
the only mixed trace being $\mathrm{Tr}(\partial_\theta\psi^\dagger\partial_\varphi\psi)=\tfrac{i}{4}\sin\theta$ and its reverse, which is purely imaginary and cancels in the symmetrization $d\theta\,d\varphi=d\varphi\,d\theta$. Hence
$$
\mathrm{Tr}\!\left(\psi^\dagger d\psi\right)=i\,\sin^2\tfrac{\theta}{2}\,d\varphi,
\qquad
\Bigl|\mathrm{Tr}\!\left(\psi^\dagger d\psi\right)\Bigr|^2=\sin^4\tfrac{\theta}{2}\,d\varphi^2 ,
$$
and
$$
\mathrm{Tr}\!\left(d\psi^\dagger d\psi\right)=\tfrac14\,d\theta^2+\sin^2\tfrac{\theta}{2}\,d\varphi^2 .
$$
Subtracting,
$$
ds^2_{\mathrm{FS}}=\tfrac14\,d\theta^2+\sin^2\tfrac{\theta}{2}\Bigl(1-\sin^2\tfrac{\theta}{2}\Bigr)d\varphi^2
=\tfrac14\,d\theta^2+\tfrac14\sin^2\theta\,d\varphi^2 ,
$$
which is the result of the projector computation. The two derivations use different objects — the Hermitian projector in $\mathbb{M}_+$ and the spinor in the module — and meet in the same line element, as they must, since the projector is the bilinear companion $\psi\psi^\dagger$ of the spinor.

### The spinorial factor of four

The factor $\tfrac14$ is not an accident of normalization, and it is worth identifying. The unit spinors form the sphere $S^3$, the rays form $S^2$, and the map between them is the Hopf fibration, whose fibres are the central phase circles $U(1)$. The double cover in the background is that of the rotation group, $SU(2)\cong S^3\to SO(3)$: a rotation of the Bloch vector by $2\pi$ corresponds to the spinor $\psi\mapsto-\psi$, an operation that is trivial on rays. The angle between two rays is **half** the angle between the corresponding Bloch vectors, and squaring that ratio of angles gives the ratio of metrics, $\tfrac14$. The Fubini–Study metric is therefore the metric induced on the ray space by the unit spinor sphere through the Hopf fibration — the Riemannian submersion of $S^3$ onto the sphere of radius $\tfrac12$ — and the group behind it is the same $SU(2)\to SO(3)$ that the companion article *Angular Momentum and Spin in Biquaternionic Form* exhibits as the group of unit real quaternions.

The factor also shows why the trace normalization matters. The trace of the algebra is fixed to $\mathrm{Tr}(e_0)=2$ by the $2\times2$ matrix representation: $e_0$ is represented by the $2\times2$ unit matrix, whose trace is $2$. The metric above is normalized by that trace. A rescaling of the trace would rescale the metric and the factor $\tfrac14$; the invariant statement, independent of the normalization, is that the Fubini–Study metric is *a fixed multiple* of the round metric of the Bloch sphere, and the multiple is the square of the double-cover ratio. All distances, areas and curvatures below are stated in the normalization $\mathrm{Tr}(e_0)=2$.

## Complex Structure and the Kähler Form

The boundary is not only a Riemannian manifold; it is a complex manifold, and the complex structure is again supplied by the algebra. This section identifies it and its symplectic companion, so that the Fubini–Study metric can be exhibited as a Kähler metric with all three of its structures read from $\mathbb{B}$.

**The complex structure.** At a point $\hat{\mu}$ of the boundary, define a real-linear map on the tangent space by
$$
J_{\hat{\mu}}(v)=\hat{\mu}\times v,\qquad v\perp\hat{\mu}.
$$
Since $\hat{\mu}\times(\hat{\mu}\times v)=\hat{\mu}(\hat{\mu}\cdot v)-v|\hat{\mu}|^2=-v$ for a tangent $v$, this satisfies $J^2=-1$: it is an almost-complex structure on the sphere, and it is in fact integrable, the sphere being the projective line. The algebra supplies it as the antisymmetric part of the product of pure real quaternions,
$$
[\hat{\mu},v]=\hat{\mu}v-v\hat{\mu}=2\,\hat{\mu}\times v,
\qquad\text{so}\qquad
J_{\hat{\mu}}(v)=\tfrac12\,[\hat{\mu},v].
$$
The commutator is therefore the rotation by $\pi/2$ about the state axis, and the complex structure on the pure-state manifold is the algebra's own antisymmetric product. This is the same commutator that the companion article *Quantum Mechanics in Biquaternionic Form* records for two Hermitian observables, $[\tilde{H},\tilde{K}]=-2(\mathbf{h}\times\mathbf{k})$, restricted to the boundary.

**The Kähler compatibility.** The metric $g(\delta_1,\delta_2)=\tfrac14\,\delta_1\hat{\mu}\cdot\delta_2\hat{\mu}$ is invariant under $J$, because $J$ is a rotation:
$$
g(J\delta_1,J\delta_2)=\tfrac14(\hat{\mu}\times\delta_1\hat{\mu})\cdot(\hat{\mu}\times\delta_2\hat{\mu})=\tfrac14\,\delta_1\hat{\mu}\cdot\delta_2\hat{\mu}=g(\delta_1,\delta_2).
$$
The associated symplectic form is
$$
\omega(\delta_1,\delta_2)=g(J\delta_1,\delta_2)=\tfrac14\,\hat{\mu}\cdot(\delta_1\hat{\mu}\times\delta_2\hat{\mu}),
$$
which in the angles $(\theta,\varphi)$ is
$$
\omega=\tfrac14\sin\theta\,d\theta\wedge d\varphi .
$$
The pair $(g,\omega)$ is Kähler, and the complex structure is $J$; the sphere of radius $\tfrac12$ with its round metric has Gaussian curvature $4$, which is also the holomorphic sectional curvature of the Fubini–Study metric in this normalization. Its total symplectic area is
$$
\int_{S^2}\omega=\tfrac14\int_0^{2\pi}\!\!\int_0^{\pi}\sin\theta\,d\theta\,d\varphi=\pi ,
$$
the area of the sphere of radius $\tfrac12$, as stated above.

**The commutator expression.** The symplectic form can be written entirely inside the algebra, without the intermediate Bloch vector. For tangential displacements $\delta_1\tilde{P}=\tfrac12 i\,\delta_1\hat{\mu}$ and $\delta_2\tilde{P}=\tfrac12 i\,\delta_2\hat{\mu}$, the commutator of the displacements is a pure real quaternion, and the trace of the projector times that commutator is purely imaginary. One computes
$$
\mathrm{Tr}\!\left(\tilde{P}\,[\delta_1\tilde{P},\delta_2\tilde{P}]\right)
=\tfrac12\, i\;\hat{\mu}\cdot(\delta_1\hat{\mu}\times\delta_2\hat{\mu}),
$$
so that
$$
\boxed{\ \omega(\delta_1,\delta_2)=-\tfrac12\,i\,\mathrm{Tr}\!\left(\tilde{P}\,[\delta_1\tilde{P},\delta_2\tilde{P}]\right)=\tfrac14\,\hat{\mu}\cdot(\delta_1\hat{\mu}\times\delta_2\hat{\mu}).\ }
$$
This is the algebraic face of the Kähler form: it is built from the trace pairing, the product, and the Hermitian conjugation, with no metric input beyond the trace normalization. The imaginary unit $i$ appears because the commutator of two Hermitian displacements is anti-Hermitian, so its trace is imaginary; the factor $i$ converts it to the real two-form.

**The Kähler potential.** In the stereographic coordinate $w=\tan(\theta/2)\,e^{i\varphi}$ inherited from the spinor, the metric takes the standard Fubini–Study form
$$
ds^2_{\mathrm{FS}}=\frac{|dw|^2}{\bigl(1+|w|^2\bigr)^2},
\qquad
g_{w\bar{w}}=\partial_w\partial_{\bar{w}}\,K,
\qquad
K=\log\bigl(1+|w|^2\bigr),
$$
so the Kähler potential is the logarithm of the spinor norm, and the metric is the second derivative of that logarithm. The normalization is the one in which $|dw|^2=dw\,d\bar{w}$ and the line element is $g_{w\bar{w}}\,dw\,d\bar{w}$ with **no** factor of two, so that $g_{w\bar{w}}=1/(1+|w|^2)^2$, equivalently $\partial_w\partial_{\bar{w}}K=\tfrac14\Delta_0K$ with $\Delta_0=4\partial_w\partial_{\bar{w}}$ the flat Laplacian of the coordinate plane; a reader who uses the convention $ds^2=2g_{w\bar{w}}\,dw\,d\bar{w}$ must halve the $g_{w\bar{w}}$ written here, and with the normalization stated the display reproduces $\tfrac14(d\theta^2+\sin^2\theta\,d\varphi^2)$ exactly. The sphere is the projective line, the coordinate $w$ is the ratio of the two spinor components, and the central phase has been quotiented out by the passage to the ratio. The fibration is the Hopf fibration $S^3\to S^2$; its connection is what the companion article *The Berry Phase and Geometric Phases in Biquaternionic Form* integrates to give the Berry phase, and the curvature of that connection is proportional to $\omega$. The present article needs only the symplectic form, but it is worth recording that the two articles are reading the same structure: the Berry phase is the holonomy of the Hopf connection, and the Fubini–Study form is its curvature.

## Geodesics, Distance, and the Trace Distance

The metric determines distances, and the distances carry the same information as the transition probability and the trace distance already computed.

**The geodesic distance.** The geodesics of the round sphere of radius $\tfrac12$ are its great circles, so the Fubini–Study geodesic distance between two pure states is the arc length along the shorter great circle,
$$
d_{\mathrm{FS}}\bigl(\tilde{P}(\hat{\mu}),\tilde{P}(\hat{\nu})\bigr)=\tfrac12\,\theta=\arccos\lvert\langle\psi|\phi\rangle\rvert ,
$$
where $\theta$ is the angle between $\hat{\mu}$ and $\hat{\nu}$ and $\lvert\langle\psi|\phi\rangle\rvert=\cos(\theta/2)$ is the overlap of the normalized spinors of the two rays. Three checks: for coincident rays, $\theta=0$ and $d_{\mathrm{FS}}=0$; for orthogonal rays, $\theta=\pi$ and $d_{\mathrm{FS}}=\pi/2$, the **maximal** distance; and the diameter of the pure-state manifold is $\pi/2$, not $\pi$, because the antipodal point of $\hat{\mu}$ corresponds to the orthogonal complement of the ray, not to the same ray with reversed phase.

**The equivalent data on the boundary.** The three boundary quantities are monotone functions of one another, and the identities relating them are the content of the geometry:
$$
\mathrm{Tr}\bigl(\tilde{P}(\hat{\mu})\tilde{P}(\hat{\nu})\bigr)=\cos^2 d_{\mathrm{FS}},
\qquad
D\bigl(\tilde{P}(\hat{\mu}),\tilde{P}(\hat{\nu})\bigr)=\sin d_{\mathrm{FS}},
\qquad
d_{\mathrm{FS}}=\arccos\sqrt{\mathrm{Tr}\bigl(\tilde{P}\tilde{Q}\bigr)}=\arcsin D .
$$
The first is the trace pairing, the second the trace distance of the companion article *Exercise: The Bloch Ball and the Geometry of Mixed States*, and the third the Fubini–Study distance. They are not three independent geometries but one: the trace pairing gives the squared cosine, the trace distance gives the sine, and the Fubini–Study distance is the angle. The complementarity identity $D^2+\mathrm{Tr}(\tilde{P}\tilde{Q})=1$ of the exercise article is the Pythagorean identity of the same triangle.

**Uniqueness and invariance.** The unitary group $U(2)$ acts transitively on the rays, and its image $SO(3)$ acts transitively on the boundary sphere. Any metric on the boundary that is invariant under this action is a multiple of the round metric, so the algebra's own symmetry group fixes the Fubini–Study metric **up to scale**. The scale is then fixed by the trace pairing, through the identification of the transition probability with $\cos^2 d_{\mathrm{FS}}$; equivalently, by the requirement that the line element be $-N(\delta\tilde{P})$, whose normalization is the trace normalization. This is a two-step determination worth naming: the symmetry fixes the metric up to a constant, and the trace fixes the constant. Neither step imports a geometric posit beyond the algebra's two forms.

**Units.** The line element has been written so that $\hat{\mu}$ is a unit vector, i.e. the Bloch vector is measured in units in which the ball has radius one. If the physical Bloch vector is measured with a radius $r_0$ — for instance $r_0=\hbar/2$ for a spin — then the metric is multiplied by $r_0^2$ and the distance by $r_0$; the dimensionless statements above are the ones fixed by the algebra, and the physical conversion is a separate posit, like the identification of $\hat{\mu}$ with a direction in space.

## The Ball: the Bures Metric and What the Norm Form Does Not Give

The pure states are the boundary; the mixed states are the interior. The metric of the interior is not determined by the boundary metric alone, and the algebra's own favourite quadratic form does not supply it. This section states what the algebra supplies, what is standard, and where the two part company.

**What the norm form supplies in the interior.** For a state $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ and a displacement $\delta\tilde{\rho}=\tfrac12 i\,\delta\mathbf{r}$, the computation of the projector variation goes through unchanged,
$$
N(\delta\tilde{\rho})=-\tfrac14\,|\delta\mathbf{r}|^2\,e_0,
\qquad
-N(\delta\tilde{\rho})=\tfrac14\,|d\mathbf{r}|^2 ,
$$
but now for **all** displacements, radial as well as tangential. So the norm form supplies the flat Euclidean metric $\tfrac14|d\mathbf{r}|^2$ on the whole ball. On the boundary, where the radial component of a tangential displacement vanishes, this flat form restricted to the boundary is the Fubini–Study metric; in the interior it is the flat metric, not the Bures metric.

**What standard physics supplies.** The metrically and statistically distinguished metric of the mixed-state space is the **Bures metric**, equivalently the quantum Fisher information. In the convention in which the Bures distance of two pure states equals their Fubini–Study distance — so that the Uhlmann transition probability of two pure states is $\lvert\langle\psi|\phi\rangle\rvert^2$, as in the companion article *The Bloch Ball as the Trace-One Slice of the Future Light Cone* — the qubit Bures line element is
$$
ds^2_{\mathrm{Bures}}=\frac14\left(\frac{dr^2}{1-r^2}+r^2\,d\Omega^2\right)
=\frac14\left(|d\mathbf{r}|^2+\frac{(\mathbf{r}\cdot d\mathbf{r})^2}{1-r^2}\right),
\qquad r=|\mathbf{r}| .
$$
This is a standard result, not an algebraic one: it is the infinitesimal form of the Uhlmann transition probability, and it is the unique metric on the ball that is monotone under stochastic maps and reduces to the Fubini–Study metric on the boundary. Two checks fix it. On the boundary $r\to1$, the radial term diverges while the angular term tends to $\tfrac14 d\Omega^2$, which is exactly the Fubini–Study metric, so the Bures metric restricts to the Fubini–Study metric on the pure states. At the center $r=0$, the angular term vanishes and the line element is $\tfrac14|d\mathbf{r}|^2$, which agrees with the norm form's flat contribution there.

**Where the two part company.** The Bures metric and the norm form's flat metric agree at the center and agree (on tangential directions) on the boundary, but nowhere else in the interior. The difference is the radial term: Bures has $\tfrac14\,dr^2/(1-r^2)$, which blows up as the state approaches purity, while the norm form gives $\tfrac14\,dr^2$ there. The interpretation is the familiar one: the Bures/Fisher metric measures *distinguishability*, and two nearly pure states that differ slightly in purity can be distinguished with high confidence from many copies, so the radial cost diverges at the boundary; the flat metric measures only the Euclidean separation of Bloch vectors and is blind to this. The algebra's norm form therefore gives the correct geometry on the pure states and the correct geometry at the maximally mixed state, but it does not give the interpolating metric, and it cannot, because the interpolation is fixed by a statistical criterion (monotonicity under noisy maps) that is not an algebraic relation of $\mathbb{B}$.

It is worth recording the boundary of the claim. What the article derives from the algebra is: the transition probability from the trace pairing; the Fubini–Study metric from the norm form; their compatibility in the Kähler structure; and the uniqueness of the boundary metric up to a scale fixed by the trace. What it imports from standard quantum information is the Bures/Fisher metric of the interior, and it does so because the algebra supplies no interior metric other than the flat one, and the flat one is not the statistically distinguished one. This division is exactly the one the framework's own discipline requires: the algebra is credited with what it determines, and the standard theory with what it does not.

## What the Geometry Is and What It Is Not

Five statements summarize the result, and two of them are limitations that a reader should not blur.

1. **The Fubini–Study metric is the second variation of the norm form on the null boundary.** This is the central identity: the norm form vanishes on the pure states, and its negative on tangential displacements is the line element, $ds^2_{\mathrm{FS}}=-N(\delta\tilde{P})$. The norm form is therefore not idle on the state space even though it vanishes on the pure states; it is the metric generator.

2. **The trace pairing supplies the probability, not the distance.** The transition probability $\mathrm{Tr}(\tilde{P}\tilde{Q})$ is the trace pairing's two-point function, and the Fubini–Study distance is its arccosine-square-root. The two forms divide the geometry between them: the trace pairing gives the overlap, the norm form gives the length, and the Kähler structure relates them.

3. **The geometry is that of the state *module*, descended to the state space.** The complex structure, the Hopf fibration and the projective line belong to the module $\mathbb{B}p\cong\mathbb{C}^2$; the metric descends to the boundary of $\mathbb{M}_+$ through the bilinear map $\psi\mapsto\psi\psi^\dagger$. The complex structure does **not** live on $\mathbb{M}_+$, where multiplication by $i$ exchanges the two sectors; treating $\mathbb{M}_+$ itself as a complex vector space is the characteristic error that this separation avoids.

4. **The interior metric is imported.** The Bures metric of the mixed states is the standard monotone metric of quantum information theory. The algebra determines its boundary value and its value at the center, and it determines the flat alternative that it is not; it does not determine the interpolation. This is a limit on the algebra's reach, not a defect of the derivation, and it is stated to prevent an overclaim.

5. **All normalization statements are trace-relative.** The factor $\tfrac14$ and the area $\pi$ are stated in the trace normalization $\mathrm{Tr}(e_0)=2$; the invariant content is that the Fubini–Study metric is a fixed multiple of the round metric, with the multiple fixed by the double cover and the trace. A reader who changes the trace normalization changes these numbers and not the geometry.

## Summary

The state space of the biquaternion framework is the trace-one slice of the future cone of the norm form, and its geometry is determined by the framework's two forms. The trace pairing fixes the transition probability of two pure states, $\mathrm{Tr}(\tilde{P}(\hat{\mu})\tilde{P}(\hat{\nu}))=\cos^2(\theta/2)$. The norm form, though it vanishes on the pure states, fixes the metric through its second variation there, and the resulting line element is the Fubini–Study metric,

$$
ds^2_{\mathrm{FS}}=-N(\delta\tilde{P})\Big|_{\text{tangential}}=\tfrac14\left(d\theta^2+\sin^2\theta\,d\varphi^2\right),
$$

one quarter of the round metric of the Bloch sphere. The factor $\tfrac14$ is the square of the double-cover ratio $SU(2)\to SO(3)$. The metric is Kähler, with complex structure $J(v)=\hat{\mu}\times v$ supplied by the algebra commutator and symplectic form $\omega=-\tfrac12 i\,\mathrm{Tr}(\tilde{P}[\delta_1\tilde{P},\delta_2\tilde{P}])=\tfrac14\mu\cdot(\delta_1\mu\times\delta_2\mu)$; the Kähler potential is $\log(1+|w|^2)$ in the stereographic coordinate. The geodesic distance is $d_{\mathrm{FS}}=\theta/2=\arccos\lvert\langle\psi|\phi\rangle\rvert$, so that the transition probability is $\cos^2 d_{\mathrm{FS}}$ and the trace distance of the companion article *Exercise: The Bloch Ball and the Geometry of Mixed States* is $\sin d_{\mathrm{FS}}$.

The interior of the ball carries the standard Bures metric, whose boundary restriction is the Fubini–Study metric and whose value at the maximally mixed state agrees with the flat metric $-N(\delta\tilde{\rho})=\tfrac14|d\mathbf{r}|^2$ that the norm form supplies everywhere. The norm form therefore gives the pure-state geometry exactly, and the flat geometry everywhere, but not the interpolating mixed-state metric; that interpolation is a standard statistical import, and the article says so rather than claiming it. What the algebra determines — the probability, the metric on the boundary, the Kähler structure, and the boundary metric's uniqueness up to a trace-fixed scale — it determines completely; what it does not determine it leaves named.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\dagger$ | Hermitian conjugation, $\dagger=\bar{\cdot}\circ{}^{*}$ |
| $\mathbb{M}_+$ | Hermitian subspace, $\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, $\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ |
| $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$ | Trace, $\mathrm{Tr}(e_0)=2$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ | State, $|\mathbf{r}|\leq1$ |
| $\tilde{P}(\hat{\mu})=\tfrac12(e_0+i\hat{\mu})$ | Pure state (idempotent), $|\hat{\mu}|=1$ |
| $\mathbb{B}p$, $p=\tfrac12(e_0+ie_3)$ | State module, $\cong\mathbb{C}^2$ |
| $\psi$, $\lvert\psi\rangle$ | Spinor in the state module |
| $\mathrm{Tr}(\tilde{P}\tilde{Q})$ | Transition probability of two pure states |
| $\theta$ | Angle between $\hat{\mu}$ and $\hat{\nu}$ |
| $d_{\mathrm{FS}}=\theta/2$ | Fubini–Study distance |
| $ds^2_{\mathrm{FS}}=\tfrac14(d\theta^2+\sin^2\theta\,d\varphi^2)$ | Fubini–Study line element |
| $J(v)=\hat{\mu}\times v$ | Complex structure on the boundary |
| $\omega=\tfrac14\sin\theta\,d\theta\wedge d\varphi$ | Symplectic (Kähler) form |
| $w=\tan(\theta/2)e^{i\varphi}$ | Stereographic (affine) coordinate |
| $K=\log(1+|w|^2)$ | Kähler potential; $ds^2=g_{w\bar{w}}\,dw\,d\bar{w}$, $g_{w\bar{w}}=1/(1+|w|^2)^2$ |
| $D=\sin(\theta/2)$ | Trace distance of two pure states |
| $ds^2_{\mathrm{Bures}}$ | Bures metric of the ball (standard import) |

## Further Reading

- S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry, Vol. II* (Wiley, 1969), for the Fubini–Study metric on complex projective space, its Kähler structure, and its holomorphic sectional curvature.
- I. Bengtsson and K. Życzkowski, *Geometry of Quantum States: An Introduction to Quantum Entanglement* (Cambridge University Press, 2nd ed., 2017), for the Bloch ball, the Fubini–Study and Bures metrics, and their monotonicity properties.
- S. L. Braunstein and C. M. Caves, "Statistical distance and the geometry of quantum states", *Physical Review Letters* **72**, 3439 (1994), for the quantum Fisher information and the identification of the Bures metric with the statistically distinguished metric of the state space.
- A. Uhlmann, "The transition probability in the state space of a *-algebra", *Reports on Mathematical Physics* **9**, 273 (1976), for the transition probability of two states and the Bures metric it generates.
- D. Bures, "An extension of Kakutani's theorem on infinite product measures to the tensor product of semifinite *-algebras", *Transactions of the American Mathematical Society* **135**, 199 (1969), for the original construction of the metric.
- C. W. Helstrom, *Quantum Detection and Estimation Theory* (Academic Press, 1976), for the trace distance and its interpretation as a distinguishability probability.
- M. Nakahara, *Geometry, Topology and Physics* (Institute of Physics, 2nd ed., 2003), for the Hopf fibration, the complex projective line, and the Kähler geometry used in the section on the Kähler form.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000), for the Bloch sphere, the transition probability, and the fidelity of two states.
- H. Hopf, "Über die Abbildungen der dreidimensionalen Sphäre auf die Kugelfläche", *Mathematische Annalen* **104**, 637 (1931), for the fibration of the unit spinor sphere over the ray space and the phase fibre it supplies.
