# __The Matrix Images: Mixedness, Rapidity and the Phase Fibre__

## Introduction

A matrix representation is usually read as a computing device: it turns the multiplication of the algebra into the multiplication of arrays. Three physical interpretations become visible only there. The determinant of the matrix image of a state is its **mixedness**. The spectrum of the matrix image of the sandwich is the **doubled rapidity** of the frame change. The unit spinors of the module are a **circle bundle** over the Bloch sphere, and the fibre is the phase that the state loses. A fourth reading is a distinction rather than a number: the $2\times2$ image carries the data an element acts on, and the $4\times4$ image carries the element acting on the algebra itself.

The article states these four readings and their boundaries. The representations and their theorems are *The Element and Operator Representations* and the four representation articles it cites; this article owns no matrix identity. It reads invariants the matrices already carry, and it keeps apart the two things a matrix can be: a number and a map.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The element image $\mathsf{M}_2(\tilde Q)$, its determinant $\langle\tilde Q\rangle_{\natural}$ and its trace $2Q_t$ | [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](../articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html) |
| The regular image $\mathsf{M}_4^{L}(\tilde Q)$, $\det=\langle\tilde Q\rangle_{\natural}^{2}$, $\operatorname{Tr}=4Q_t$, and the block splitting $\mathsf{M}_4\cong\mathsf{M}_2\oplus\mathsf{M}_2$ | [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html) |
| The sandwich operator, its matrix $\operatorname{H}_{\tilde Q}=\mathsf{M}_4^{L}(\tilde Q)\mathsf{M}_4^{R}(\tilde Q^{*})$, its spectrum $\lambda_i\bar\lambda_j$, its determinant $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{4}$ and its trace $4\lvert Q_t\rvert^{2}$ | [Two-Sided Operator and the Polar Decomposition](../articles_maths/two-sided-operator-and-the-polar-decomposition.html), §*The Spectrum of the Sandwich*, for the spectrum, and [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the determinant and the trace |
| The eigenvalue decomposition, the eigenprojections and the degenerate case | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), [Spectral Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| The positive cone and the pure states as rank-one idempotents | [Jordan Algebras and the Positive Cone](../articles_maths/jordan-algebras-and-the-positive-cone.html) |
| The principal bundle, the connection, the curvature and the holonomy | [Fibre Bundles, Connections and Curvature](../articles_maths/fibre-bundles-connections-and-curvature.html) |

The physical sources are *The Element and Operator Representations* for the correspondence table, *The Bloch Ball as the Normalised Slice of the Future Light Cone* for the state geometry, *The Hopf Fibration and the Biquaternion Gauge Bundle* for the quaternion presentation of the bundle, and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form* for the half-solid-angle rule.

## Two Images of One Element

### The Element Image and the Map Image

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension four, and it is isomorphic to $M_2(\mathbb{C})$. Two matrix images follow from that isomorphism and from the regular representation:

$$
\mathsf{M}_2(\tilde Q)\in M_2(\mathbb{C}),
\qquad
\mathsf{M}_4^{L}(\tilde Q)\in M_4(\mathbb{C}).
$$

The first is the matrix of the element as it acts on the **spinor module** $S\cong\mathbb{C}^2$. The second is the matrix of the element as it acts on the **algebra**, taken as a module over itself, in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$.

The two are the same object seen through two kinds of data. $\mathsf{M}_2(\tilde Q)$ is the matrix of an element acting on *the data an object acts on*; $\mathsf{M}_4^{L}(\tilde Q)$ is the matrix of an element acting on *the objects themselves*. The corpus names the two pictures **element-data** and **map-data**. The reading is an interpretation, and its content is the doubling: the regular module is $S\oplus S$, split by the two minimal left ideals, which are the two column chiralities. In the column-adapted basis the regular image is block diagonal with two equal blocks,

$$
\mathsf{M}_4^{L}\;\cong\;\mathsf{M}_2\oplus\mathsf{M}_2 .
$$

That is the dictionary between the two kinds of data. The map-data image is the element-data image taken twice, one copy per chirality.

**The bookkeeping of the doubling.** The doubling is visible in every invariant. The trace doubles, from $2Q_t$ to $4Q_t$; the determinant squares, from $\langle\tilde Q\rangle_{\natural}$ to $\langle\tilde Q\rangle_{\natural}^{2}$; and the sandwich, which is the product of the two regular images, has determinant $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{4}$ and trace $4\lvert Q_t\rvert^{2}$. None of these factors is a physical quantity. They are the dimension of the module over which the trace is taken and the number of copies the regular module contains. The one invariant that does not move is the vanishing set: $\det\mathsf{M}_2(\tilde Q)=0$, $\det\mathsf{M}_4^{L}(\tilde Q)=0$ and $\det\operatorname{H}_{\tilde Q}=0$ exactly on the zero-divisor cone.

**The boundary.** The two pictures are one representation taken twice, not two theories. The names describe what the matrix acts on, and they do not assert two physical descriptions. A result proved in one picture must be translated before it is read in the other, and the determinant degree is where the translation is most often skipped.

The sandwich is a third matrix, $\operatorname{H}_{\tilde Q}=\mathsf{M}_4^{L}(\tilde Q)\mathsf{M}_4^{R}(\tilde Q^{*})$, quadratic in the parameter and a congruence rather than a similarity. Its spectrum is the subject of the rapidity reading below.

## The Determinant of a State Is Its Mixedness

### The Trace-One Slice

A state of the informational sector is an element

$$
\tilde{Ϛ}=\tfrac12\bigl(e_t+i\vec r\bigr),\qquad \vec r=(r_x,r_y,r_z)\in\mathbb{R}^3,
$$

with $\lvert\vec r\rvert\le1$. It is Hermitian, of trace one, and positive exactly on the closed ball. Its matrix image is the density matrix

$$
\mathsf{M}_2(\tilde{Ϛ})=\tfrac12\bigl(\mathrm{I}_2+r_k\,\mathsf{M}_2(i\vec e_k)\bigr),
$$

the standard Bloch form, with the three matrices $\mathsf{M}_2(i\vec e_k)$ Hermitian, traceless and of square $\mathrm{I}_2$.

The determinant of this matrix is

$$
\boxed{\;\det\mathsf{M}_2(\tilde{Ϛ})=\tfrac14\bigl(1-\lvert\vec r\rvert^{2}\bigr)\;}.
$$

It is the biquaternion norm $\langle\tilde{Ϛ}\rangle_{\natural}$ of the state, and it is real and non-negative on the ball. The two eigenvalues of the matrix are $\tfrac12(1\pm\lvert\vec r\rvert)$, so the determinant is their product, the two-dimensional volume the two eigen-directions span. On the Bloch ball it is the radial gap to the pure boundary: it vanishes on the sphere and is maximal at the centre.

### The Three Numbers

Three quantities read off the same determinant:

$$
\operatorname{Tr}(\tilde{Ϛ}^{2})=1-2\det\mathsf{M}_2(\tilde{Ϛ}),
\qquad
S_L=1-\operatorname{Tr}(\tilde{Ϛ}^{2})=2\det\mathsf{M}_2(\tilde{Ϛ}).
$$

The first is the **purity**; the second is the **linear entropy**. At the centre, $\vec r=0$, the determinant is $\tfrac14$, the purity is $\tfrac12$ and the linear entropy is $\tfrac12$, its maximum on the ball. On the sphere the determinant vanishes, the purity is one and the linear entropy is zero.

| position in the ball | $\det\mathsf{M}_2(\tilde{Ϛ})$ | purity | linear entropy | state |
| --- | --- | --- | --- | --- |
| centre, $\lvert\vec r\rvert=0$ | $\tfrac14$ | $\tfrac12$ | $\tfrac12$ | maximally mixed |
| interior, $0<\lvert\vec r\rvert<1$ | $\tfrac14(1-r^{2})$ | $\tfrac12(1+r^{2})$ | $\tfrac12(1-r^{2})$ | mixed |
| boundary, $\lvert\vec r\rvert=1$ | $0$ | $1$ | $0$ | pure |

**The matrix volume.** The determinant is not a probability and not an entropy; it is the product of the two eigenvalues of the state matrix. The purity and the linear entropy are affine functions of it, which is why the determinant is the one matrix invariant from which both are read. The von Neumann entropy is not such a function: it is $-\sum\lambda_\pm\log\lambda_\pm$, a nonlinear function of the same pair, and it is not a polynomial in the determinant.

### Purity Is the Zero Divisor

The vanishing of the determinant is the vanishing of the norm, and the norm is the invertibility criterion. Hence:

- inside the ball the state is a **unit**, invertible as an element and as a map;
- on the sphere the state is a **zero divisor**, of rank one, and its matrix image is the rank-one projector onto a ray.

The pure states are therefore exactly the states on the wall of the algebra. This is the matrix form of the statement of *The Unit Group, the Cone and the Orders*: the cone meets the positive cone in the cone over the pure states, and its trace-one slice is the Bloch sphere. The determinant is a measure of the distance to that wall, vanishing on it and maximal at the centre.

**The boundary.** The identity $\operatorname{Tr}(\tilde{Ϛ}^{2})=1-2\det$ holds in the trace-one normalisation and for a positive element. For a general element of $\mathbb{B}$ the determinant is the complex norm, and it is not a mixedness; the reading requires the state conditions, not the matrix alone. The linear entropy is one monotone among many, and the determinant supplies no entropy argument beyond it.

### The Singular Values of the Amplitude

For a general element the matrix image has a polar decomposition and two singular values. The amplitude is

$$
\mathsf{M}_2(\tilde H)=\sqrt{\mathsf{M}_2(\tilde Q)\,\mathsf{M}_2(\tilde Q)^{\dagger}},
$$

so $\tilde H$ is Hermitian positive semidefinite and its eigenvalues $\sigma_1\ge\sigma_2\ge0$ are the singular values of $\tilde Q$. On the amplitude the determinant changes character:

$$
\langle\tilde H\rangle_{\natural}=\det\mathsf{M}_2(\tilde H)=\sigma_1\sigma_2=\lvert\det\mathsf{M}_2(\tilde Q)\rvert=\lvert\langle\tilde Q\rangle_{\natural}\rvert .
$$

**The norm of an amplitude is real and non-negative**, even when the norm of the element is complex. For a Hermitian element the norm is $\langle\tilde H\rangle_{\natural}=h_t^{2}-\lvert\vec h\rvert^{2}$, the determinant of a Hermitian matrix; positivity makes it $\sigma_1\sigma_2$. The element and its amplitude have norms of the same modulus and differ in phase.

The state inherits the singular values and loses the phase. With $\hat H=\tilde H/\sqrt{\sigma_1^{2}+\sigma_2^{2}}$, the state is $\hat H^{2}$, its eigenvalues are $p_i=\sigma_i^{2}/(\sigma_1^{2}+\sigma_2^{2})$, and its determinant is

$$
\det\mathsf{M}_2(\tilde{Ϛ}_Q)=\frac{\sigma_1^{2}\sigma_2^{2}}{(\sigma_1^{2}+\sigma_2^{2})^{2}}\in\left[0,\tfrac14\right].
$$

The two ends are the pure state, $\sigma_2=0$, and the maximally mixed state, $\sigma_1=\sigma_2$. The mixedness of the state is therefore the spread of the singular values, read on the same determinant that the first part of this article reads as a volume.

**The boundary.** The singular values are invariants of the matrix and do not depend on the polar frame, but the amplitude is not the element: for a non-normal element the singular values are not the moduli of its eigenvalues, and the eigen-decomposition of $\tilde Q$ does not give them. Only for a normal element do the two coincide.

## The Spectrum Is the Doubled Rapidity

### The Eigenvalues of the Element

The element matrix satisfies its characteristic equation

$$
\lambda^{2}-2Q_t\,\lambda+\langle\tilde Q\rangle_{\natural}=0,
$$

so its two eigenvalues are

$$
\boxed{\;\lambda_\pm=Q_t\pm\sqrt{Q_t^{2}-\langle\tilde Q\rangle_{\natural}}
=Q_t\pm\sqrt{-\bigl(Q_x^{2}+Q_y^{2}+Q_z^{2}\bigr)}\;}.
$$

The pair is the eigenvalue map of the element. It is not a homomorphism: the eigenvalues of a product are not a function of the two pairs, because the factors need not commute. Its product is multiplicative,

$$
\lambda_+\lambda_-=\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural},
$$

and that product is the reason the determinant is the one invariant of the pair. The map is a similarity invariant and not a complete one: a scalar $Q_te_t$ and a non-scalar element with $(\vec Q,\vec Q)=0$ share the pair $\{Q_t,Q_t\}$ and are not similar. The eigenprojections, not the pair, carry the remaining information, and they are the subject of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*.

The sandwich has the four eigenvalues $\lambda_i\bar\lambda_j$, so the nontrivial pair of the operator is the **square** of the pair of the element. The element stores half of the frame change; the congruence stores the whole of it.

### The Boost

Take the boost rotor of rapidity $\eta$ along $\vec e_z$,

$$
\tilde B_\eta=\cosh\tfrac{\eta}{2}\,e_t+\sinh\tfrac{\eta}{2}\,i\vec e_z .
$$

Its norm is one, and its matrix is diagonal in the eigenbasis of $\mathsf{M}_2(i\vec e_z)$:

$$
\mathsf{M}_2(\tilde B_\eta)=\operatorname{diag}\bigl(e^{\eta/2},e^{-\eta/2}\bigr).
$$

The sandwich therefore has the eigenvalues

$$
e^{\eta},\;1,\;1,\;e^{-\eta}.
$$

The two middle eigenvalues are the transverse directions, which the boost fixes. The longitudinal pair is squared: the element carries $e^{\pm\eta/2}$ and the congruence carries $e^{\pm\eta}$. The corpus's worked rotor $\tilde Q=\tfrac53e_t+\tfrac43i\vec e_z$ has matrix $\operatorname{diag}(3,\tfrac13)$ and operator eigenvalues $9,1,1,\tfrac19$. In the convention of this article its frame rapidity is $\eta=2\ln3$, while the operand stores $\eta/2=\ln3$; the source names the stored value the rapidity and the four-vector value twice that.

**The reading.** The rapidity is the logarithm of the eigenvalue ratio. The element matrix stores **half** the rapidity, because it acts on the spinor, and the spinor is the half-spin representation of the Lorentz group. The congruence acts on the Hermitian matrix, which is the four-vector, and stores the full rapidity. The factor two is the same factor that makes a rotation through $2\pi$ return the spinor with a minus sign and the vector to itself.

### The Rotation, and the Double Cover

Take the rotation rotor of angle $\theta$ about $\vec e_z$,

$$
\tilde R_\theta=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec e_z .
$$

Its matrix has the eigenvalues $e^{\pm i\theta/2}$, and the sandwich has $e^{\pm i\theta}$ beside the two transverse eigenvalues $1$. At $\theta=2\pi$ the element eigenvalues are $e^{\pm i\pi}=-1$, while the operator eigenvalues are $e^{\pm2\pi i}=1$. The spectrum is the double cover: the spinor returns with a sign, the four-vector returns unchanged. The logarithm of the modulus of the eigenvalue is half the rapidity, its argument the half-angle, and the congruence doubles both.

### Where the Reading Stops

The eigenvalue reading requires the element matrix to be diagonalisable. Off the cone it is, except on a set of measure zero. On the cone $\langle\tilde Q\rangle_{\natural}=0$, the characteristic equation is $\lambda(\lambda-2Q_t)=0$, and the eigenvalues are $0$ and $2Q_t$: they collide at zero only on the trace-zero part of the cone, where the matrix is nilpotent. There the four operator eigenvalues vanish while its rank is one, the operator is not diagonalisable, and no rapidity is defined. The four eigenvalues vanish because the rank has dropped to one, not because a pair of nonzero eigenvalues has met.

A general Lorentz element need not be either a pure boost or a pure rotation, and its eigenvalues are then neither real and reciprocal nor conjugate of unit modulus. The pair (rapidity, angle) is not read off a single eigenvalue; the polar decomposition is what separates the two factors. The "doubled rapidity" is a reading of the pure cases and of the polar factors, not a formula for a general element.

## The Unit Spinors Are a Phase Fibre

### The Hopf Map

The spinor module is $S\cong\mathbb{C}^2$. Its unit vectors form the three-sphere

$$
S^{3}=\bigl\{\varsigma\in\mathbb{C}^{2}:\lVert\varsigma\rVert=1\bigr\}.
$$

The map

$$
\pi(\varsigma)=\varsigma\varsigma^{\dagger}
$$

sends a unit spinor to a rank-one Hermitian matrix of trace one, which is a pure state of the informational sector. In the algebra it is the idempotent $\tfrac12(e_t+i\vec u)$ with $\vec u$ the Bloch vector of $\varsigma$. The map is surjective onto the Bloch sphere $S^{2}$, and its fibre over a state is the set of spinors that differ by a phase:

$$
\bigl\{e^{i\alpha}\varsigma:\alpha\in\mathbb{R}\bigr\}.
$$

That phase is the **central phase**: the element $e^{i\alpha}e_t$ acts on the spinor as the scalar matrix $e^{i\alpha}\mathrm{I}_2$. The bundle

$$
\boxed{\;\mathrm{U}(1)\hookrightarrow S^{3}\longrightarrow S^{2}\;}
$$

is the Hopf bundle, of first Chern number one. The state carries the axis and no phase; the phase is the fibre.

### The Two Circles

The corpus's Hopf article writes the same geometry on the unit real quaternions, where the map is $\tilde U\mapsto\tilde U\vec e_z\bar{\tilde U}$ and the fibre is the **stabiliser** of the axis, the circle of rotations about $\vec e_z$. That circle and the central phase circle are different subgroups of $\mathrm{U}(2)$: the stabiliser is the diagonal torus $\{\operatorname{diag}(e^{i\alpha},e^{-i\alpha})\}$, the central phase is the scalar circle $\{\operatorname{diag}(e^{i\alpha},e^{i\alpha})\}$, and they meet only in $\{\pm\mathrm{I}_2\}$.

The two descriptions are two presentations of the Hopf bundle, and they must not be identified fibre by fibre. In the spinor-ray description the fibre is the overall phase; in the quaternion-conjugation description the fibre is the stabiliser, and the central imaginary $i$ is the coefficient of the abelian connection. Both statements are correct, and neither is the other. The distinction matters as soon as a phase is called a gauge transformation: the overall phase moves no state, while the stabiliser is a rotation about the axis, trivial on that state and non-trivial on the others.

### The Holonomy

The natural connection on the Hopf bundle has curvature $-\tfrac12$ times the area form of the sphere. Its holonomy over a loop is therefore

$$
\gamma=-\tfrac12\,\Omega,
$$

minus one half of the enclosed solid angle. This is the Pancharatnam phase, and the Berry phase of a spin in a slowly varying field is the same holonomy. The factor $\tfrac12$ is the factor of the double cover again: a rotation of the vector by $\theta$ is a phase of $\theta/2$ on the spinor.

**The boundary.** The bundle, its Chern number, the connection and the phase are owned by *The Hopf Fibration and the Biquaternion Gauge Bundle* and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*. The article records the matrix image of the fibre and adds no topology. The unit spinor is not a unit-norm biquaternion: the unit spinors form $S^{3}$, the unit-norm biquaternions form $SL(2,\mathbb{C})$, of real dimension six, and the unit real quaternions, read as spinors, are the common three-sphere.

## What the Three Readings Share

A $2\times2$ matrix has two scalar invariants, its determinant and its trace, and the three readings divide them.

| matrix | determinant | eigenvalue pair | reading |
| --- | --- | --- | --- |
| $\mathsf{M}_2(\tilde{Ϛ})$ | $\tfrac14(1-r^{2})$ | $\tfrac12(1\pm r)$ | mixedness; the purity is affine in the determinant |
| $\mathsf{M}_2(\tilde B_\eta)$ | $1$ | $e^{\pm\eta/2}$ | half the rapidity |
| $\mathsf{M}_2(\tilde R_\theta)$ | $1$ | $e^{\pm i\theta/2}$ | half the angle |
| $\varsigma\varsigma^{\dagger}$ | $0$ | $1,0$ | a pure state; the fibre over it is the phase |

The determinant is a **scale**, the eigenvalue ratio a **shape**, and the phase the one datum the map to the ray forgets. The three are independent. A state matrix has a determinant and a real eigenvalue ratio; the ratio is a population ratio and not a rapidity, because the state is Hermitian and is not a Lorentz frame element. A boost matrix has a rapidity and determinant one, because it is a unit. A unit spinor has a phase and a pure-state image of determinant zero, because the map to the ray is rank one.

Read together, the three readings say what a matrix image can carry: a norm, a frame and a volume. It cannot carry the phase of the element, which the sandwich loses and the state ray forgets, and it cannot carry a dynamics.

## Limits

The article reads invariants. It derives no equation of motion, no Lorentz action and no measurement update.

The mixedness reading requires a trace-one positive element. For a general element the determinant is the complex norm, and it is not a mixedness; the purity formula is a statement about the Bloch ball and not about $\mathbb{B}$.

The rapidity reading requires a diagonalisable element matrix and a pure boost or rotation. On the cone one eigenvalue vanishes; on its trace-zero part the two collide at zero and the reading stops. For a general Lorentz element no single rapidity exists.

The phase-fibre reading is the Hopf bundle, not a gauge field. The connection, its curvature and its Chern number are cited; no gauge dynamics and no charge quantisation are derived.

The element-data and map-data distinction is an interpretation of the doubling $\mathsf{M}_4\cong\mathsf{M}_2\oplus\mathsf{M}_2$, not an identification of two theories.

## Summary

- The $2\times2$ image is the element acting on the spinor data; the $4\times4$ regular image is the element acting on the algebra, and it is the $2\times2$ image taken twice, $\mathsf{M}_4\cong\mathsf{M}_2\oplus\mathsf{M}_2$.
- The trace doubles, $2Q_t$ to $4Q_t$; the determinant squares, $\langle\tilde Q\rangle_{\natural}$ to $\langle\tilde Q\rangle_{\natural}^{2}$; the sandwich determinant is $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{4}$. Only the vanishing set is common to the three.
- The eigenvalues of the element are $Q_t\pm iB$ with $B^2=Q_x^2+Q_y^2+Q_z^2$; their product is the determinant $\langle\tilde Q\rangle_{\natural}$, and the eigenvalue map is a similarity invariant and not a complete one.
- The determinant of a trace-one state is $\tfrac14(1-\lvert\vec r\rvert^{2})$, the product of its two eigenvalues; the purity is $1-2\det$ and the linear entropy is $2\det$.
- The determinant vanishes exactly on the pure states, so the pure states are the zero divisors of the state slice and the mixed states are its units.
- For a pure boost or rotation, the element matrix stores half the rapidity or half the angle; the sandwich stores the full one, because the congruence acts on the four-vector and the element on the spinor.
- The spectrum is the double cover: a rotation through $2\pi$ gives $-1$ on the element and $1$ on the congruence.
- The unit spinors form $S^{3}$ over the Bloch sphere $S^{2}$ with fibre the central phase; the bundle is the Hopf bundle and its holonomy is minus one half the solid angle.
- The Hopf fibre of the spinor-ray description is the central phase; the Hopf fibre of the quaternion-conjugation description is the stabiliser torus. The two circles meet only in $\{\pm\mathrm{I}_2\}$.
- The determinant is a scale, the eigenvalue ratio a shape, and the phase what the ray forgets. No invariant of a single matrix supplies a dynamics.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathsf{M}_2(\tilde Q)$ | the element image in $M_2(\mathbb{C})$; $\det=\langle\tilde Q\rangle_{\natural}$, $\operatorname{Tr}=2Q_t$ |
| $\mathsf{M}_4^{L}(\tilde Q)$ | the left regular image in $M_4(\mathbb{C})$; $\det=\langle\tilde Q\rangle_{\natural}^{2}$, $\operatorname{Tr}=4Q_t$ |
| $\operatorname{H}_{\tilde Q}$ | the sandwich operator; $\det=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{4}$, $\operatorname{Tr}=4\lvert Q_t\rvert^{2}$ |
| $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ | a trace-one state of the Bloch ball |
| $\det\mathsf{M}_2(\tilde{Ϛ})$ | the mixedness, $\tfrac14(1-\lvert\vec r\rvert^{2})$ |
| $S_L=2\det\mathsf{M}_2(\tilde{Ϛ})$ | the linear entropy |
| $\tilde B_\eta$ | the boost rotor of rapidity $\eta$, of eigenvalues $e^{\pm\eta/2}$ |
| $\tilde R_\theta$ | the rotation rotor of angle $\theta$, of eigenvalues $e^{\pm i\theta/2}$ |
| $\varsigma$ | a unit spinor of $S\cong\mathbb{C}^{2}$ |
| $\pi(\varsigma)=\varsigma\varsigma^{\dagger}$ | the Hopf map to the Bloch sphere |
| $\gamma=-\tfrac12\Omega$ | the Pancharatnam phase, the holonomy of the Hopf connection |

## Further Reading

- [The Element and Operator Representations](the-element-and-operator-representations.html), for the correspondence table this article extends.
- [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), for the spectrum and the eigenprojections, and [Spectral Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html) for the point where the pair stops being a complete invariant.
- [The Bloch Ball as the Normalised Slice of the Future Light Cone](the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html), for the ball, its centre and its boundary.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the state conditions and the Born pairing.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone as the boundary of the state space.
- [The Unit Group, the Cone and the Orders](the-unit-group-the-cone-and-the-orders.html), for the partition into units and zero divisors.
- [The Hopf Fibration and the Biquaternion Gauge Bundle](the-hopf-fibration-and-the-biquaternion-gauge-bundle.html), for the bundle, its fibre and its Chern number.
- [Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html), for the half-solid-angle rule.
- [Exercise: The Bloch Ball and the Geometry of Mixed States](exercise-the-bloch-ball-and-the-geometry-of-mixed-states.html), for the determinant, purity and linear entropy.
