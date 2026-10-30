# __The Determination of the Possible Spins in Biquaternionic Form__

## Introduction

The observed elementary particles carry spin $0$, $\tfrac12$ or $1$: the Higgs is a scalar, the quarks and leptons are spinors, and the photon, the $W^\pm$, the $Z$ and the gluons are vectors. No observed elementary particle carries another spin. This article asks what the biquaternion framework says about that list, and what it does not say.

The answer has two parts. The algebraic part is the companion article *The Four Uses of Spin in the Biquaternion Algebra*, which defines spin, separates the four uses of the word and proves the closure theorem. It states that $\mathbb{B}$ carries exactly three isomorphism classes of irreducible subcarriers, of complex dimensions $1$, $2$ and $3$, distributed over **two** module structures. The physical part is the interpretation of the three as the scalar, the spinor and the vector.

The distribution over two structures is already recorded in *Spin and the Three Elementary Carriers*: left multiplication sees the spinor twice, and the adjoint action sees the scalar and the vector. This article takes that distribution as its starting point and asks what it means physically. A single action cannot contain all three, because distinct irreducible submodules intersect trivially and $1+2+3=6$ would exceed $\dim_{\mathbb{C}}\mathbb{B}=4$.

The article fixes what spin is, gives the two lists, interprets each carrier physically, proves that there is no fourth, and then treats the relativistic label, the statistics sign and the classical limit. The carrier table and the particle assignments are developed at length in *Spin and the Three Elementary Carriers*; the present article owns the physical interpretation and the reason for the list.

## Spin Is the Casimir Label

**The label.** Spin is the highest weight $s$ of the rotation action on a carrier, defined by the Casimir:

$$
\tilde S^2=\hbar^2s(s+1)\,e_t .
$$

On an irreducible carrier the Casimir is a scalar, so $s$ is one number for the whole carrier. The number of states is $2s+1$. The spin is a real number, $s\in\tfrac12\mathbb{Z}_{\ge0}$; it is a scalar label, not a vector and not a complex number.

**The direction is a state label.** The component along an axis needs an axis: $\tilde S_3=\hbar s_z$ on the state $|s,s_z\rangle$. The axis is a measurement setting. At $s=0$ the axis labels nothing, so a direction cannot be the definition of spin.

**The classical picture.** A coherent state $|\vec u\rangle$ of maximal spin along $\vec u$ has

$$
\langle\vec S\rangle=\hbar s\,\vec u,\qquad
\langle\vec S^2\rangle=\hbar^2s(s+1).
$$

The expectation is a vector of length $\hbar s$; the Casimir length is $\hbar\sqrt{s(s+1)}$. The two agree only in the limit $s\gg1$. The vector is a shadow of the representation, not the representation.

**The boundary.** The direction is a continuous coordinate on the sphere of states. The spin is the discrete label of the carrier, and it does not vary with the direction.

## The Two Structures and the Two Lists

The product of $\mathbb{B}$ induces two actions of the rotation group, and they are of different kinds.

**Left multiplication** is an algebra homomorphism. It makes $\mathbb{B}$ a left module over itself and gives two copies of the defining action on the spinor module. This is the structure of a matter field: the defining representation is the simplest matter multiplet.

**Conjugation** is a group action, whose differential is the Lie bracket. It makes $\mathbb{B}$ a module over the rotation Lie algebra, not over the associative algebra. This is the structure of a vector field: a vector carries the adjoint representation of the rotation group.

The two structures give two lists:

| structure | carriers | dimensions | spins |
|---|---|---|---|
| left multiplication | $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | $2$ | $\tfrac12$ |
| conjugation | $Z=\mathbb{C}e_t$ | $1$ | $0$ |
| conjugation | $V=\ker\operatorname{tr}$ | $3$ | $1$ |

The spin-half carrier occurs twice, as the two Peirce planes; it is one isomorphism class. The three spin values are the union of the two lists.

**Why the union is forced.** Distinct irreducible submodules intersect trivially, so their dimensions add. A carrier of spin $s$ has $2s+1$ states, and a single structure on $\mathbb{B}$ would have to contain $1+2+3=6$ of them, but $\dim_{\mathbb{C}}\mathbb{B}=4$. So the three values are never the constituents of one action. This is arithmetic, and it is the reason the question has no single-list answer.

**Why these two and not another pair.** These are the two actions the product supplies without a choice: left multiplication and conjugation. The right action is the mirror of the left and gives the same list. Other actions require extra data, such as a form or a grading, and are not carried by the product alone.

## The Scalar: Spin Zero

**The carrier.** The centre $Z=\mathbb{C}e_t$ is fixed by conjugation: $u(z e_t)u^{-1}=z e_t$. The Casimir vanishes, the spin is $0$, and the carrier has one state.

**The generator.** $\tilde S_k e_t=0$ for all $k$. There is no axis to choose and no ladder: the representation is trivial.

**The physical interpretation.** A scalar field. The carrier $Z=\mathbb{C}e_t$ is a complex line, two real dimensions; its real form $\mathbb{R}e_t$ is the real scalar of one degree of freedom. The Higgs is the observed spin-zero instance; its internal components are extra data, not a larger spin.

**What the carrier does not carry.** No direction, no polarization, no double-cover sign: a $2\pi$ rotation acts as the identity on $Z$.

## The Spinor: Spin One Half

**The carrier.** The Peirce plane $S_+=\mathbb{B}\tilde\Pi_+$ has complex dimension two, with basis $(\tilde\Pi_+,\vec\Upsilon_{-+})$. The second plane $S_-$ is a second copy, module-isomorphic and Hilbert-orthogonal.

**The operators.** With $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$,

$$
\tilde S^2=\tfrac34\hbar^2e_t,\qquad
\tilde S_3\tilde\Pi_+=\tfrac{\hbar}{2}\tilde\Pi_+,\qquad
\tilde S_3\vec\Upsilon_{-+}=-\tfrac{\hbar}{2}\vec\Upsilon_{-+}.
$$

The ladder operators are the nilpotent mixed units

$$
\vec\Upsilon_{+-}=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y),
$$

with $\tilde S_+=\hbar\vec\Upsilon_{+-}$, $\tilde S_-=\hbar\vec\Upsilon_{-+}$ and $\tilde S_\pm^2=0$. In *Spin and the Three Elementary Carriers* the same units are written $\vec\Upsilon_{+-}=\vec\Upsilon_x$ and $\vec\Upsilon_{-+}=\vec\Upsilon_y$.

**The copies at an axis.** For a unit real pure quaternion $\vec u$, the idempotents

$$
\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)
$$

generate the minimal left ideals $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$, each a copy of the carrier. The planes $S_\pm$ above are the case $\vec u=\vec e_z$.

**The states in a copy.** In the left action, $\tilde\Pi_+(\vec u)$ is the state of weight $+\tfrac{\hbar}{2}$ in $S_+(\vec u)$,

$$
(\vec u\cdot\tilde S)\,\tilde\Pi_+(\vec u)=+\tfrac{\hbar}{2}\,\tilde\Pi_+(\vec u),
$$

and $\tilde\Pi_-(\vec u)$ is the state of weight $-\tfrac{\hbar}{2}$ in $S_-(\vec u)$. The state of weight $-\tfrac{\hbar}{2}$ in $S_+$ is its nilpotent basis vector, not an idempotent.

**The two outcomes.** The two idempotents are the two outcomes of a measurement along $\vec u$: pure states of the algebra, not two vectors of one module. The axis is the measurement direction, and the two outcomes are its two signs.

**The double cover.** A $2\pi$ rotation is multiplication by $-e_t$, which acts as $-\operatorname{id}$ on every copy $S_\pm(\vec u)$: a state returns to itself only up to sign. This is the spinor sign and the source of the half-integer class. The sign belongs to the module action, not to the idempotent: conjugation by the rotor carries $\tilde\Pi_+(\vec u)$ to $\tilde\Pi_+(\vec u')$ with no sign.

**The physical interpretation.** The electron, the quarks and the leptons. The same carrier, with the Hermitian form of the second slot, is the defining module of the relativistic qubit: two states, a Bloch sphere of axes, and the same double cover.

## The Vector: Spin One

**The carrier.** The traceless part $V=\ker\operatorname{tr}$ has complex dimension three, with the weight basis

$$
\varepsilon_\pm=\mp\tfrac{1}{\sqrt2}(\vec e_x\pm i\vec e_y),\qquad\varepsilon_0=\vec e_z ,
$$

the signs being the Condon–Shortley phase, chosen so that the ladder coefficients are positive.

**The operators.** With $\tilde S^{(\mathrm{adj})}_k=\tfrac{\hbar}{2}\mathrm{ad}_{i\vec e_k}$,

$$
\tilde S^{(\mathrm{adj})\,2}=2\hbar^2\operatorname{id}_V,\qquad
\tilde S^{(\mathrm{adj})}_3\varepsilon_\pm=\pm\hbar\,\varepsilon_\pm,\qquad
\tilde S^{(\mathrm{adj})}_3\varepsilon_0=0 .
$$

The Casimir follows from $C=(\tilde S^{(\mathrm{adj})}_3)^2+\tfrac12(\tilde S^{(\mathrm{adj})}_+\tilde S^{(\mathrm{adj})}_-+\tilde S^{(\mathrm{adj})}_-\tilde S^{(\mathrm{adj})}_+)$ and the ladder actions

$$
\tilde S^{(\mathrm{adj})}_+\varepsilon_-=\sqrt2\,\hbar\,\varepsilon_0,\qquad
\tilde S^{(\mathrm{adj})}_+\varepsilon_0=\sqrt2\,\hbar\,\varepsilon_+,\qquad
\tilde S^{(\mathrm{adj})}_-\varepsilon_+=\sqrt2\,\hbar\,\varepsilon_0,\qquad
\tilde S^{(\mathrm{adj})}_-\varepsilon_0=\sqrt2\,\hbar\,\varepsilon_-,
$$

which give $C=2\hbar^2$ on all three states. The value is $\hbar^2s(s+1)$ at $s=1$. There are three states.

**The physical interpretation.** A vector field. In the rest frame of a massive vector the three weights are the three polarizations. For a massless one the longitudinal state is removed and two helicities remain. The photon, the $W^\pm$, the $Z$ and the gluons are the observed instances.

**The massless count and the cone.** The two helicities are the self-dual and the anti-self-dual halves of the field strength, $\vec E+i c\vec B$ and $\vec E-i c\vec B$. The removed state is the longitudinal direction $\vec u_k$, the unit vector along the momentum, which is the helicity-zero eigenvector. The algebra exhibits the third eigenvector; it does not remove it. The removal is a gauge condition, and the gauge-fixing principle is imported.

**Masslessness, the cone and $N=0$.** The mass shell is the level set $N=-m^2c^2$ of the norm $N=\langle\tilde P\rangle_\natural$ of the four-momentum. The massless case is $N=0$, the zero-divisor cone. On that cone the little group is the double cover of $E(2)$. The algebra marks the cone: among the level sets of $N$ on the material sector, $N=0$ is the only one that is a cone, the only one on which the four-momentum is not invertible, and the only one invariant under rescaling. It does not choose $m=0$: the norm is homogeneous, so the algebra carries no preferred mass. The choice $m=0$ is an input.

## Why There Is No Fourth

**The counting.** An irreducible carrier of spin $s$ has $2s+1$ states. The irreducible subcarriers of $\mathbb{B}$ have dimensions $1$, $2$ and $3$. A fourth value would need an irreducible subcarrier of dimension $4$ or more.

**No such carrier exists.** Under the left action the invariant subspaces have dimensions $0$, $2$ and $4$; under conjugation they have dimensions $0$, $1$, $3$ and $4$. The only four-dimensional one is $\mathbb{B}$ itself, and it is reducible in both structures: $S_+\oplus S_-$ on the left, $Z\oplus V$ under conjugation. There is therefore no irreducible subcarrier above dimension $3$.

**What lies beyond.** Spin $\tfrac32$ would need dimension $4$, and spin $2$ would need dimension $5$. Neither is a subcarrier of $\mathbb{B}$. The graviton is spin $2$ and lives in the traceless symmetric square of $V$, the $\mathcal{V}_4$ summand of $V\odot V$, which is not a subspace of $\mathbb{B}$. The higher-spin hadrons are composites, not elementary states.

**What the match says.** The three values are the spins of all observed elementary particles. The match is a match of labels. The algebra does not say which particle carries which label, and it does not derive the particle content of the Standard Model.

## Mass, the Little Group and Helicity

**The little group.** For a particle of four-momentum $\tilde P$, the little group is the stabiliser

$$
G_{\tilde P}=\{\tilde U\in SL(2,\mathbb{C}):\tilde U\tilde P\tilde U^{*}=\tilde P\}.
$$

For a massive particle $\tilde P$ is timelike and $G_{\tilde P}\cong SU(2)$; its irreducible representations are the spin representations, labelled by $s$, and the rest-frame carrier has $2s+1$ states. For a massless particle $\tilde P$ is null and $G_{\tilde P}$ is the double cover of $E(2)$; each finite-dimensional irreducible unitary representation carries a single helicity $h$, and a massless particle of spin $s$ uses the two representations $h=\pm s$ (at $s=0$, only $h=0$). The reduction from $2s+1$ to two is the gauge condition, not the little group.

The passage from $SU(2)$ to the double cover of $E(2)$ is the reason the massless count is two and not three. It is a property of the momentum, not of the carrier.

**The covariant label.** The Pauli–Lubanski vector is

$$
W^\mu=\tfrac12\epsilon^{\mu\nu\rho\sigma}M_{\nu\rho}P_\sigma .
$$

In the rest frame $W^0=0$ and $\vec W=mc\vec S$, so $\vec W^2=m^2c^2\hbar^2s(s+1)$. With the corpus norm convention, in which the norm of the four-momentum is $N=-m^2c^2$, the invariant is $W^\mu W_\mu=-N\hbar^2s(s+1)=m^2c^2\hbar^2s(s+1)$. The rotation Casimir is the rest-frame shadow of the covariant invariant.

**The Lorentz label.** Under left multiplication by $SL(2,\mathbb{C})$ the algebra carries the chiral spinor $(\tfrac12,0)$ with multiplicity two; under conjugation it carries the four-vector $(\tfrac12,\tfrac12)$. The conjugate chirality $(0,\tfrac12)$ is the conjugate module $S^{\mathrm c}$, with a conjugate-linear action; it is not a complex $\mathbb{B}$-module. The rotation spin $s$ is the little-group label; it is not the full Lorentz label, and the split of the four-vector into $0\oplus1$ is the work of the compact subgroup.

## Spin and Statistics

**The sign.** The exchange sign of a spin-$s$ state is $(-1)^{2s}$: integer spin gives $+1$, half-integer spin gives $-1$.

**The algebraic split.** In the algebra the half-integer carrier is the left module $S_\pm$, on which $-e_t$ acts as $-1$. The integer carriers are $Z$ and $V$, on which the conjugation action of $-e_t$ is trivial. The module and the adjoint sector therefore track the two integrality classes.

**The boundary.** The algebraic split matches the two classes, but it does not prove the spin–statistics theorem. The theorem is a statement about quantum fields, locality and positivity, and it is imported from quantum field theory. The algebra respects it; it does not derive it. The spin–statistics article states the theorem and identifies exactly which of its ingredients the algebra supplies.

## The Classical Limit

**The coherent-state action.** The spin path integral is written on the sphere of coherent states. Its kinetic term is the Wess–Zumino term

$$
S_{WZ}=i\hbar\oint\langle z|\partial_{t'}|z\rangle\,dt'=-s\hbar\,\Omega,
$$

where $\Omega$ is the oriented solid angle of the loop, with the orientation fixed once and for all, and $|z\rangle$ is the spin-$s$ coherent state. For $s=\tfrac12$ the value is $-\hbar\Omega/2$, the spinor phase.

**The two quantities.** The direction is the loop on the sphere; the spin is the coefficient of the term. The Berry phase of the spin-$s$ coherent state carries the factor $s$, and the classical Hannay angle does not. The factor is the label; the trajectory is the direction.

**The boundary.** The vector picture is the classical limit. The spin vector $\langle\vec S\rangle=\hbar s\vec u$ is an expectation value, not the definition. The definition is the Casimir label.

## What the Framework Does Not Say

**No particle content.** The algebra lists the possible labels. It does not say which particle carries which, and it does not derive the spectrum.

**No mass and no dynamics.** The Casimir is kinematical. No mass, no Hamiltonian and no equation of motion follow from it.

**No masslessness.** The mass shell is the level set $N=-m^2c^2$; the null case $N=0$ is the zero-divisor cone. The cone marks the massless case but does not choose it. Masslessness is an input.

**No fourth elementary spin.** The closure is for $\mathbb{B}$ alone. Higher spin requires a tensor product, and a tensor product is not a subcarrier of $\mathbb{B}$.

**No derivation of statistics.** The spin–statistics theorem is imported.

**No single structure.** The three values are the union of the left-module list and the adjoint list. Any statement that presents them as the constituents of one action is false, and the arithmetic $1+2+3=6>4$ is the proof.

## Summary

The regular module of the biquaternion algebra contains exactly three irreducible subcarrier spins: $0$, $\tfrac12$ and $1$. They are distributed over two module structures. Left multiplication gives the spinor $S_\pm$, of dimension two, with Casimir $\tfrac34\hbar^2$ and spin $\tfrac12$. Conjugation gives the scalar $Z=\mathbb{C}e_t$, of dimension one, with spin $0$, and the vector $V=\ker\operatorname{tr}$, of dimension three, with Casimir $2\hbar^2$ and spin $1$.

There is no fourth: the irreducible subcarriers have dimensions $1$, $2$ and $3$, and the only four-dimensional invariant subspace is the whole algebra, which is reducible. The arithmetic $1+2+3=6>4$ shows that the three can never be the constituents of a single action.

The physical interpretation is the scalar, the spinor and the vector, and the observed elementary particles carry exactly these three spins. The match is a match of labels, not a prediction of the particle content. Spin is the Casimir label of a carrier, not a direction: the direction labels a state, and the spin labels the representation. The relativistic label is the little-group label, $SU(2)$ for a massive particle and the double cover of $E(2)$ with helicity for a massless one. The spin–statistics theorem is respected by the algebraic split but is not proved by it. Masslessness is not derived: the cone marks $N=0$, and the gauge condition that removes the longitudinal state is imported.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra |
| $Z=\mathbb{C}e_t$ | The centre, the spin-zero carrier |
| $V=\ker\operatorname{tr}$ | The traceless part, the spin-one carrier |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | The two Peirce planes, the spin-half carrier |
| $\tilde\Pi_\pm(\vec u)$ | The idempotents along the axis $\vec u$ |
| $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$ | The copy of the carrier at the axis $\vec u$ |
| $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ | The nilpotent mixed units |
| $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ | The spin-half operators |
| $\tilde S^{(\mathrm{adj})}_k=\tfrac{\hbar}{2}\mathrm{ad}_{i\vec e_k}$ | The spin-one generators |
| $C=\tilde S^{(\mathrm{adj})\,2}$ | The Casimir, $\sum_k(\tilde S^{(\mathrm{adj})}_k)^2$ |
| $s$ | The spin label |
| $\vec u$ | A unit real pure quaternion, an axis |
| $N=\langle\tilde P\rangle_\natural$ | The biquaternion norm of the four-momentum; $N=-m^2c^2$ |
| $W^\mu$ | The Pauli–Lubanski vector |

## Further Reading

- [The Four Uses of Spin in the Biquaternion Algebra](../articles_maths/the-four-uses-of-spin-in-the-biquaternion-algebra.html), for the definition, the two structures and the closure theorem.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the carrier table, the particle assignments and the Hilbert-orthogonality of the two Peirce planes.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html), for the angular-momentum algebra, the spin operators and the Casimir.
- [Integer Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the spin-one multiplet, its weight basis and the internal and orbital parts.
- [The Relativistic Qubit in Biquaternionic Form](the-relativistic-qubit-in-biquaternionic-form.html), for the defining module, the Lorentz action and the celestial sphere.
- [Spin Entropy and the Lorentz Group in Biquaternionic Form](spin-entropy-and-the-lorentz-group-in-biquaternionic-form.html), for the little group and the frame dependence.
- [The Spin-Half Path Integral in Biquaternionic Form](the-spin-half-path-integral-in-biquaternionic-form.html), for the coherent-state action, the saddle point and the topological term.
- [The Spin–Statistics Theorem in Biquaternionic Form](the-spin-statistics-theorem-in-biquaternionic-form.html), for the theorem, its ingredients and the algebra's own fermionic mode.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), for the module, the symplectic form and the Lorentz action.
- [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html), for the helicity operator, the self-dual split and the gauge reduction to two polarizations.
- [The Null Four-Momentum: What the Cone Derives and What It Does Not](the-null-four-momentum-what-the-cone-derives-and-what-it-does-not.html), for the mass shell as a norm level set, the $N=0$ cone, and the verdict that masslessness is an input.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the massless spectrum carried by the cone.
