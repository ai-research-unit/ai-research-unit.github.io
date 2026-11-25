# __Helicity in Biquaternionic Form__

## Introduction

The angular momentum of a particle has a projection on its direction of motion, and the projection is the **helicity**. The corpus meets it on two levels, and the two are one object seen from two sides.

On the level of a carrier it is an **operator**: the spin of the carrier projected on the momentum axis. That statement needs a declared axis and nothing else, and it holds for a massive particle as readily as for a massless one. On the level of a null momentum it is a **weight**: the label a state carries under the one-parameter freedom that a null momentum leaves unfixed, which is the freedom of the factorisation of the momentum into two spinors. That statement needs the momentum to be null, and it is where helicity becomes a Lorentz-invariant label.

The passage between the two is the content of the article. The operator is defined once, for a carrier of any spin, and read on the carriers the algebra possesses: the fundamental one, the adjoint, the symmetric square. The weight is derived for a null momentum, from the rank-one factorisation that the zero-divisor cone forces. The two meet in the section that identifies the eigenvalues of the operator with the weights of the scaling, and they part again at $m\neq0$, where the operator survives and the weight does not.

The corpus divides a statement into what the algebra supplies and what it transcribes. Here a third head is needed, because several statements are neither: a statement is **standard** when it is the quantum mechanics of angular momentum, transcribed; **algebraic** when it follows from the biquaternion product; and **an input** when the algebra represents both alternatives and chooses neither. The article keeps the three apart.

## The Operator and the Declared Axis

Let a state carry the momentum $\vec p\neq0$, and let

$$
\vec u_p=\frac{\vec p}{\lvert\vec p\rvert}
$$

be the unit along it, a pure real quaternion of square $-e_t$. The axis is **declared**: it is a datum of the state and not a property of the algebra, and no statement below is about the algebra until an axis is named.

Let $\vec S$ be the rotation generator on the carrier of the state, read as one vector, so that its components are $\tilde S_{\Psi,k}=\frac{h}{4\pi}i\vec e_{\imath}$ on the fundamental carrier (*Angular Momentum and Spin in Biquaternionic Form*, §*The Spin Operators Under the Isomorphism*) and the corresponding generator on any other.

**Definition (helicity).** With the axis $\vec u_p$ declared, the **helicity operator** is the projection

$$
\digamma_{\mathrm{hlc}}=\vec u_p\cdot\vec S ,
$$

and the **helicity** of a state is its eigenvalue $\frac{h}{2\pi}\,h$, in units of $\frac{h}{2\pi}$. The operator is Hermitian and belongs to $\mathbb{B}_{\Psi}$; the number $h$ is real and labels the state, not the carrier.

**Proposition (the spectrum, and what the two words mean).** On a carrier of spin $s$ the spectrum of $\digamma_{\mathrm{hlc}}$ is $\frac{h}{2\pi}\,h$ with $h\in\{-s,-s+1,\dots,s\}$. The largest $h$ is the spin.

*Proof.* The spectrum of $\vec u\cdot\vec S$ is independent of the unit vector $\vec u$, and its maximum is the spin, which is the dimension of the carrier's representation space read on the generators (*From the Spin to the Carriers and the Closures*, §*The Spin Table*). The operator at the declared axis is that same operator, so it has that same string, ordered along $\vec u_p$ rather than along a fixed axis.

Two consequences are worth naming. **Spin is a property of the carrier; helicity is a property of the state.** The carrier fixes the list, the axis orders it, the state selects a member. **The list is the same at every axis**, so a rotation cannot change the values available, only which of them a given state carries; that is the content of the rotation law below.

$\digamma_{\mathrm{hlc}}$ is an observable and not a generator: its action on an element of the carrier is a left multiplication, and that is the sense in which the algebra supplies it as an element rather than as a matrix.

**Two collisions of the letter.**

- $\vec S$ is the spin vector of *Angular Momentum and Spin in Biquaternionic Form*. *The Photon in Biquaternionic Form* records that the same glyph is also the Poynting vector of its energy–momentum table. The two are distinguished by the carrier: the spin vector acts on a state, the Poynting vector is a density of the field.
- Two senses shared one glyph once, and this article keeps them apart. The operator is $\digamma_{\mathrm{hlc}}$, an element of the algebra carrying no index. The spinor is $\varpi_{\mathrm{twz}}$, one of the two factors of a null momentum, with a spinor index and a bar on its conjugate; the factorisation sections say which is in force.

**Two subscripts, one object.** The subscript names the element whose direction is taken, the third rule of the arrow in *Algebra and Element Conventions*, §*The Remarkable Subspaces of Biquaternions*: $\vec u_p$ for the momentum $\vec p$ and $\vec u_\Phi$ for the wave vector $\vec\nu_\Phi$. The two are the same element, since $\vec p=h\,\vec\nu_\Phi$; the subscript records which symbol the article in hand uses, the photon article writing $\vec u_\Phi$ and the Dirac articles $\vec u_p$.

## Why the Orbital Part Drops Out

The total angular momentum is $\vec J=\vec L+\vec S$, and its projection on the momentum is the helicity plus the projection of the orbital part. The orbital part contributes nothing:

$$
\vec L\cdot\vec p=(\vec r\times\vec p)\cdot\vec p=0 .
$$

In the algebra this is one line. The orbital operator is the vector part of the quaternionic product of position and momentum, $\vec L=\mathrm{Vect}(\vec r\,\tilde p)$ with $\tilde p=-i\,\frac{h}{2\pi}\vec\nabla_\Phi$ (*Angular Momentum and Spin in Biquaternionic Form*, §*The Orbital Angular Momentum Operator*), and the scalar triple product carrying $\vec p$ twice vanishes identically. The projection of $\vec J$ on $\vec u_p$ is therefore the projection of $\vec S$, which is why the quantity has a name of its own and is not called one component of the total angular momentum.

**The consequence for the slots.** The orbital part occupies the central scalar slot $e_t$ and the spin part the vector slots $i\vec e_{\imath}$, the asymmetry that article records. The vanishing above is what makes the asymmetry harmless for this one projection: the orbital slot contributes nothing to it, so the projection of $\vec J$ on $\vec u_p$ is the projection of $\vec S$ alone.

## The Fundamental Carrier

On the spin-$\tfrac12$ carrier the generator is $\tilde S_{\Psi,k}=\frac{h}{4\pi}i\vec e_{\imath}$, so the operator is the left multiplication by

$$
\digamma_{\mathrm{hlc}}=\frac{h}{4\pi}\,i\vec u_p\in\mathbb{B}_{\Psi} .
$$

The carrier is a minimal left ideal, and the two helicity values are its two weights. The vectors that carry them are named by the idempotents at the axis.

**Proposition (the two weights and their vectors).** In the carrier $S_+(\vec u_p)=\mathbb{B}\tilde\Pi_{\mathrm{id},+}(\vec u_p)$, with $\tilde\Pi_{\mathrm{id},\pm}(\vec u_p)=\tfrac12(e_t\pm i\vec u_p)$, the operator has the two values $\pm\frac{h}{4\pi}$, once each. The vector of the value $+\frac{h}{4\pi}$ is $\tilde\Pi_{\mathrm{id},+}(\vec u_p)$; the vector of $-\frac{h}{4\pi}$ is the companion corner $\tilde\Pi_{\mathrm{id},-}(\vec u_p)\,\mathbb{B}\,\tilde\Pi_{\mathrm{id},+}(\vec u_p)$, which is one-dimensional and nilpotent.

*Proof.* For the first, $i\vec u_p\,\tilde\Pi_{\mathrm{id},+}=\tfrac12\bigl(i\vec u_p+(i\vec u_p)^2\bigr)=\tfrac12\bigl(i\vec u_p+e_t\bigr)=\tilde\Pi_{\mathrm{id},+}$, using $(i\vec u_p)^2=e_t$ for a unit pure direction. For the second, every $\digamma_{\mathrm{spn}}$ of the companion corner satisfies $\digamma_{\mathrm{spn}}=\tilde\Pi_{\mathrm{id},-}(\vec u_p)\digamma_{\mathrm{spn}}$ and $\digamma_{\mathrm{spn}}=\digamma_{\mathrm{spn}}\tilde\Pi_{\mathrm{id},+}(\vec u_p)$; the first gives $i\vec u_p\digamma_{\mathrm{spn}}=-\digamma_{\mathrm{spn}}$, the second gives $\digamma_{\mathrm{spn}}^2=\digamma_{\mathrm{spn}}\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}\digamma_{\mathrm{spn}}=0$, and the corner is one-dimensional because two idempotents of rank one, one on each side, leave a single matrix entry. Two independent vectors exhaust a two-dimensional carrier.

This is the proposition of *Spinors and Dirac Spinors in the Biquaternion Algebra*, §*The Elementary Spinor*, read at the momentum axis, and the vocabulary there is the one to keep: the **elementary spinor** is an element of a minimal left ideal $S_\pm(\vec u_p)$, of complex dimension two, with the weights $\pm\tfrac12$, and the factor $\frac{h}{2\pi}$ is the only difference of units between the two statements. The idempotent $\tilde\Pi_{\mathrm{id},+}(\vec u_p)$ is the **pure state** of the carrier, its rank-one Hermitian projector (*Special Element Conventions*, §*The Idempotent Convention*); it is not the only element that carries the weight, since every element of $S_+(\vec u_p)$ does.

**One refinement, on the word eigenvector.** The operator is a left multiplication, and on the whole algebra its eigenspaces are not the left ideals but the right ideals $\tilde\Pi_{\mathrm{id},\pm}(\vec u_p)\mathbb{B}$, each of complex dimension two. The left ideals are the eigenspaces of the right multiplier $R(i\vec u_p)$, with the value $+1$ on $S_+(\vec u_p)$ and $-1$ on $S_-(\vec u_p)$ (*Spinors and Dirac Spinors in the Biquaternion Algebra*, §*The Pair Is a Multiplicity*). A state lives in a left ideal, so the statement above is the physical one: inside its own carrier the state's operator has the two values, and their vectors are the pure state and its companion nilpotent.

**The Dirac carrier.** A Dirac spinor is $\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R}$, an element of $\mathbb{B}$ with its two parts in the two left ideals at a declared axis (*Spinors and Dirac Spinors in the Biquaternion Algebra*, §*The Dirac Spinor*). Two things follow, and the second is the one usually got wrong.

- The two parts are two copies of one carrier, not two different carriers: the index that separates them is a copy index, and in adapted bases the same left multiplication has the same matrix on both.
- The two helicity values **cut each part into two lines**; they do not name the two parts. Inside $\tilde{Ξ}_{L}$, which is two-dimensional, the operator has the values $\pm\frac{h}{4\pi}$ once each, and the same inside $\tilde{Ξ}_{R}$. The parts are separated by the side of a multiplication, the right multiplier $R(i\vec u_p)$; the helicity by a left multiplier. **A helicity eigenstate is a line in a part, not a part.**

**Why the mass does not undo the cut.** The mass term is the only term of the Dirac equation that names the other part, and it does so on the right, while the helicity element multiplies on the left (*Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation*, §*The Gradient and the Two Parts*). Left and right multiplications commute, so the mass couples the two parts and leaves the helicity split of each intact. At $m=0$ the parts decouple altogether into two Weyl equations, one per part, and the helicity is then locked to the part.

**The spinor form.** The same element is written in that exercise with the root $\tilde{Ζ}=i\vec u_p$ of the central value $+1$, and the two are proportional,

$$
\digamma_{\mathrm{hlc}}=\frac{h}{4\pi}\,\tilde{Ζ} .
$$

The values $\pm1$ of $\tilde{Ζ}$ are therefore the helicity values in units of $\frac{h}{4\pi}$, and the exercise quotes them under the name of the helicity. The pair is the same pair; the factor is invertible.

## The Higher Carriers

The fundamental carrier is a minimal left ideal. The integer carriers are not: spin one is the adjoint action on the imaginary quaternions, and spin two is the symmetric traceless square of that space. The rule for the operator is the same on each, and only the carrier changes.

**Spin one.** In the adjoint action, with $\vec u_p$ the axis,

$$
\digamma_{\mathrm{hlc}}=\frac{i\,h}{4\pi}\,\mathrm{ad}_{\vec u_p},
$$

whose representative is the Hermitian element $i\,\frac{h}{2\pi}\,\vec u_{p}\in\mathbb{B}_{\Psi}$, with the spectrum $\{+\frac{h}{2\pi},0,-\frac{h}{2\pi}\}$ on the complexified vector part. The corpus states this spectrum in units of $\frac{h}{2\pi}$, as $\{+1,0,-1\}$, and writes the dimensionless $\tfrac{i}{2}\mathrm{ad}_{\vec u_\Phi}$ (*The Photon in Biquaternionic Form*, §*Helicity as an Observable in the Informational Sector*) or $\tilde S_{\Psi,\mathrm{adj},3}$ (*Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*); the two are the same operator in different units, and the $\frac{h}{2\pi}$ above restores the invertibles of the spin-$\tfrac12$ case. The $\pm \frac{h}{2\pi}$ eigenvectors are the two circular polarizations, and the $0$ eigenvector is the direction $\vec u_p$ itself, since $\mathrm{ad}_{\vec u_p}(\vec u_p)=0$. The one qualification is a matter of sides: the observable is an element of $\mathbb{B}_{\Psi}$ and the carrier is the vector part, so the operator is a left multiplication on the algebra of which the carrier is a subspace, and it is not itself a state.

**The massive field.** The same carrier carries the Proca field, and there all three states are physical. Along the momentum the two transverse states carry $\pm1$ and the longitudinal one carries $0$, and a boost rotates a transverse polarization into the longitudinal one. The label is therefore not invariant at $m\neq0$, which is the massive case of the boost law below (*The Proca Equation: Massive Spin 1 in Biquaternionic Form*, §*The Massive Field Strength and the Self-Dual Split*). The algebra represents both cases on the same carrier, and the value of $m$ decides which states are physical.

**The self-dual split.** For the massless field the two nonzero labels are the two self-dual halves of the field strength. With $\vec N=\vec E+ic\vec B$ the self-dual half and $\vec N^*$ its conjugate, Faraday's law gives $\vec B=\vec u_\Phi\times\vec E$ and $\vec u_\Phi\times\varepsilon_{\mathrm{fop},\pm}=\mp i\varepsilon_{\mathrm{fop},\pm}$, so each half carries one sign of $\digamma_{\mathrm{hlc}}$ (*The Photon in Biquaternionic Form*, §*Helicity and the Self-Dual Split of the Field Strength*). That is the field-theoretic face of the same operator: the weight of the little group is the label of one of the two complex three-dimensional representations of the Lorentz group.

**Spin two.** On the symmetric traceless square the spectrum is $\{-2,-1,0,1,2\}$ in units of $\frac{h}{2\pi}$, and the gauge and trace removals leave the two of $\pm2$ (*Canonical Quantization of the Biquaternion Graviton Field*, §*Helicity and the Massless Little Group*). The algebra supplies the five-dimensional carrier and the projector; it does not supply the removal.

**General $s$.** On any carrier the spectrum is the weight string $\frac{h}{2\pi}\,h$ with $h\in\{-s,\dots,s\}$, and the largest $h$ is the spin. Nothing in the operator depends on the carrier: it is the same projection, on a different module.

## Reversal, Rotation and Boost

Three laws hold on every carrier. The first two cost no computation; the third is where the label stops being invariant.

**Reversal.** The unit along $-\vec p$ is $-\vec u_p$, so

$$
\digamma_{\mathrm{hlc}}(-\vec p)=-\digamma_{\mathrm{hlc}}(\vec p).
$$

This is also the statement $\tilde\Pi_{\mathrm{id},+}(\vec u_p)=\tilde\Pi_{\mathrm{id},-}(-\vec u_p)$: the set of values is the same at the reversed axis, and what reverses is the attribution of a value to a given momentum. The two helicities of a state are therefore not exchanged by the reversal of the momentum alone; the state is a different state in the reversed frame.

**Rotation.** For the rotor $\tilde u$ of a rotation carrying $\vec u_p$ to $\vec u_{p'}$ (*Angular Momentum and Spin in Biquaternionic Form*, §*The Rotor Realisation of Rotations*), the operator is conjugated,

$$
\digamma_{\mathrm{hlc}}(\vec p')=\tilde u\,\digamma_{\mathrm{hlc}}(\vec p)\,\tilde u^{*},
$$

so a rotation relabels the axis and leaves the spectrum alone. Helicity is a scalar under rotations by construction, and no rotation can spoil the label.

**Boost.** A boost along $\vec p$ leaves $\vec u_p$ alone and rescales $\lvert\vec p\rvert$, so $\digamma_{\mathrm{hlc}}$ is unchanged. A boost transverse to $\vec p$ is a different matter. The momentum turns in the boost, and the spin turns with it by the Wigner rotation the boost induces, which is not in general the rotation carrying the old axis to the new one; the state then ceases to be an eigenstate of the new $\digamma_{\mathrm{hlc}}$. The extreme case is a boost that overtakes the particle, which reverses the momentum in the new frame while the spin does not reverse with it, so $\digamma_{\mathrm{hlc}}$ changes sign. Overtaking is possible only for a particle slower than light, and that is the whole of the massive case: **helicity is not Lorentz invariant at $m\neq0$.** The rest frame is the limit of the same fact: at $\vec p=0$ the axis is undefined, so the operator is undefined, and helicity is a property of a state in motion.

## The Little Group and the Invariance

At $m=0$ the label becomes invariant, and the reason is that a null direction cannot be reversed. The group-theoretic statement — the stabiliser of a null momentum, its $ISO(2)$, the compact $U(1)$, the removal of the continuous label by locality — is treated in *The Determination of the Possible Spins in Biquaternionic Form*, §*Mass, the Little Group and Helicity*, and in *Canonical Quantization of the Biquaternion Graviton Field*, §*Helicity and the Massless Little Group*; it is not repeated here. What the operator adds is the invariance itself, which it proves without the group.

**The invariance.** A boost cannot reverse a null direction. With $\vec p$ null and $\beta<1$ the boosted energy $E'=\gamma(E-\beta p_\parallel)=\gamma E(1-\beta\cos\theta)$ is positive for every boost, so the momentum stays in the forward light cone and $\vec u_p$ tilts with it instead of turning over. Nothing overtakes a massless particle, so the mechanism of the massive case is unavailable.

**The reduction from $2s+1$ to two is not the little group.** The little group supplies the weight; it does not cut the carrier. The algebra exhibits all $2s+1$ values of $\digamma_{\mathrm{hlc}}$ and removes none, and the passage to the two states of $\pm s$ is the gauge condition (*The Determination of the Possible Spins in Biquaternionic Form*, §*Mass, the Little Group and Helicity*; *The Photon in Biquaternionic Form*, §*Helicity as an Observable in the Informational Sector*). For the vector field the zero eigenvector is $\vec u_p$ itself, and the gauge structure is what deletes it. A massless scalar keeps $h=0$, so the zero weight is excluded only when the spin is nonzero and the field is a gauge field.

**The doubling.** That a massless particle of definite helicity $h$ carries the one-dimensional representation of weight $h$ is the little group's statement. Whether the field carries both signs is a property of the field: for the photon and the graviton the field is real, and a real field is the sum of a mode and its conjugate, so both signs occur; for a Weyl fermion the field is one handed spinor, and the other sign belongs to its antiparticle and not to the particle.

## The Massless Momentum as a Zero Divisor

The rest of the article is the second level, where helicity is a weight. It begins with the algebra of the null momentum, and that algebra is the zero-divisor structure of $\mathbb{B}$.

A nonzero biquaternion is a zero divisor if and only if its biquaternion norm vanishes, $\langle\tilde Q\rangle_{\natural}=0$ (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*); since the norm is the determinant of the matrix realisation, the nonzero zero divisors are exactly the rank-one elements of $\mathsf{M}_2(\mathbb{C})$. The four-momentum is

$$
\tilde P_{\Phi}=\frac{iE}{c}\,e_t+\vec p\in\mathbb{B}_{\Phi},\qquad
\langle\tilde P_{\Phi}\rangle_{\natural}=-\frac{E^2}{c^2}+\vec p^{\,2}=-m^2c^2 .
$$

**At $m=0$ it is a zero divisor.** Then $E=c\lvert\vec p\rvert$, the norm vanishes, and $\tilde P_{\Phi}\neq0$ whenever $E\neq0$. The light cone of $\mathbb{B}_{\Phi}$ *is* the zero-divisor cone (*Four-Vectors and the Interval*). The divisor is of the **non-pure** kind, its scalar part $iE/c$ being nonzero, so it obeys $\tilde P_{\Phi}^2=2P_t\tilde P_{\Phi}$, the square relation of the non-pure family.

**At $m\neq0$ it is not.** Then $\langle\tilde P_{\Phi}\rangle_{\natural}=-m^2c^2\neq0$, the element is invertible, and the matrix has rank two. That asymmetry is the whole of the singular limit treated below.

**Rank one.** At $m=0$, $\det\mathsf{M}_2(\tilde P_{\Phi})=0$ and $\mathsf{M}_2(\tilde P_{\Phi})\neq0$, hence

$$
\mathsf{M}_2(\tilde P_{\Phi})=i\left(\frac{E}{c}I_2-\vec p\cdot\boldsymbol\sigma\right),
$$

of rank exactly one. The matrix in parentheses, $p_{\alpha\bar\beta}=\frac{E}{c}\delta_{\alpha\bar\beta}-(\vec p\cdot\boldsymbol\sigma)_{\alpha\bar\beta}$, is the standard spinor-helicity bispinor, Hermitian, of determinant $E^2/c^2-\vec p^{\,2}=m^2c^2$, and rank one exactly at $m=0$. The factor $i$ is the framework's $i r'_t$ convention; with $\tilde H_\Psi=-i\tilde P_{\Phi}\in\mathbb{B}_{\Psi}$ one has $\mathsf{M}_2(\tilde H_\Psi)=p_{\alpha\bar\beta}$ exactly.

## Rank One Is Factorisability

The passage from rank one to a product of two spinors is a lemma of linear algebra, and it is the reason the algebra needs no separate spinor-helicity postulate.

**Lemma.** A nonzero $2\times2$ matrix $M$ has rank one if and only if there are nonzero columns $\varpi_{\mathrm{twz}},\bar\varpi_{\mathrm{twz}}\in\mathbb{C}^2$ with $M=\varpi_{\mathrm{twz}}\bar\varpi_{\mathrm{twz}}^{T}$. The pair is determined up to the scaling $(\varpi_{\mathrm{twz}},\bar\varpi_{\mathrm{twz}})\mapsto(r'_t\varpi_{\mathrm{twz}},{r'_{t}}^{-1}\bar\varpi_{\mathrm{twz}})$, $r'_t\in\mathbb{C}^\times$.

*Proof.* If $M=\varpi_{\mathrm{twz}}\bar\varpi_{\mathrm{twz}}^{T}$ with both factors nonzero, every column is a multiple of $\varpi_{\mathrm{twz}}$, so the column space is one-dimensional and the rank is one. Conversely, if the rank is one, take a nonzero column $\varpi_{\mathrm{twz}}$; every other column is a multiple of it, and every row is a multiple of the row $\bar\varpi_{\mathrm{twz}}^{T}$ read off any nonzero row; then $M=\varpi_{\mathrm{twz}}\bar\varpi_{\mathrm{twz}}^{T}$. The scaling is the elementary ambiguity, $(r'_t\varpi_{\mathrm{twz}})({r'_{t}}^{-1}\bar\varpi_{\mathrm{twz}})^{T}=\varpi_{\mathrm{twz}}\bar\varpi_{\mathrm{twz}}^{T}$.

Applying it to the null momentum,

$$
\mathsf{M}_2(\tilde P_{\Phi})=\varpi_{\mathrm{twz}}\,\bar\varpi_{\mathrm{twz}}^{T},
\qquad \varpi_{\mathrm{twz}}\in S,\ \bar\varpi_{\mathrm{twz}}\in\bar S,
$$

with $\varpi_{\mathrm{twz}}$ in the spinor module and $\bar\varpi_{\mathrm{twz}}$ in its conjugate. This is the spinor-helicity factorisation $p_{\alpha\bar\beta}=\varpi_{\mathrm{twz},\alpha}\bar\varpi_{\mathrm{twz},\bar\beta}$, and it is not an analogy: it is the rank-one condition of the zero-divisor cone written in coordinates. The two factors are the two rulings of the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$ (*The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$*, §*The Factorisation*).

**Here $\varpi_{\mathrm{twz}}$ is a spinor.** In this section and the next two, $\varpi_{\mathrm{twz}}$ and $\bar\varpi_{\mathrm{twz}}$ are the two factors, elements of $S$ and of $\bar S$, one of them barred. Everywhere else in the article the helicity operator is $\digamma_{\mathrm{hlc}}$, an element of $\mathbb{B}_{\Psi}$ with no index.

**Reality.** For a real momentum $\tilde P_{\Phi}\in\mathbb{B}_{\Phi}$ is anti-Hermitian, so $\mathsf{M}_2(\tilde P_{\Phi})$ is anti-Hermitian and of the form $i\,uu^{\dagger}$; the two factors are then conjugate up to a phase,

$$
\bar\varpi_{\mathrm{twz}}\sim\varpi_{\mathrm{twz}}^{*},
$$

which is the reality condition of the real slice. For a complexified momentum the components are complex and the two factors become independent, which is an extension off $\mathbb{B}_{\Phi}$ and is flagged as such.

## The Brackets as the Invariant Pairing

The spinor module carries the invariant symplectic form $\varepsilon(\tilde{Ξ},\xi_{\mathrm{alt}})=\tilde{Ξ}^T\epsilon\,\xi_{\mathrm{alt}}$ (*The Spinor Module in Biquaternionic Form and Its Lorentz Action*), and the two brackets of the formalism are that form applied to the factors of two different momenta:

$$
\langle ij\rangle=\varpi_{\mathrm{twz},i}^{T}\epsilon\,\varpi_{\mathrm{twz},j}=-\langle ji\rangle,
\qquad
[ij]=\bar\varpi_{\mathrm{twz},i}^{T}\epsilon\,\bar\varpi_{\mathrm{twz},j}=-[ji].
$$

The antisymmetry is the antisymmetry of $\epsilon$ and nothing else; the brackets are not a new structure. In the corpus convention $\varepsilon_{12}=+1$, each bracket is the $2\times2$ determinant of the two spinors, and the identity $\langle ij\rangle[ij]=\det\bigl(\mathsf{M}_2(\tilde P_{\Phi,i})+\mathsf{M}_2(\tilde P_{\Phi,j})\bigr)$ expresses the pairing of two null momenta as a product of brackets.

The calculus built on these objects — the momentum-conservation constraints, the explicit spinor parametrisations, the Parke–Taylor formula — is standard and transcribed; the algebra supplies the factorisation and the pairing, and it does not supply the calculus built on them.

## Helicity as the Weight of the Scaling

The scaling freedom of the factorisation is the kinematic little group, and the helicity is its weight. This is where the two levels of the article meet.

**The scaling leaves the momentum invariant.** If $\mathsf{M}_2(\tilde P_{\Phi})=\varpi_{\mathrm{twz}}\bar\varpi_{\mathrm{twz}}^{T}$ and one sends $\varpi_{\mathrm{twz}}\mapsto r'_t\varpi_{\mathrm{twz}}$, $\bar\varpi_{\mathrm{twz}}\mapsto{r'_{t}}^{-1}\bar\varpi_{\mathrm{twz}}$ with $r'_t\in\mathbb{C}^\times$, the product is unchanged, so $\tilde P_{\Phi}$ is unchanged. The scaling is exactly the ambiguity of the lemma.

**From $\mathbb{C}^\times$ to $U(1)$.** For a real momentum the reality condition fixes the modulus of $r'_t$ and leaves its phase, so the freedom is a $U(1)$. That $U(1)$ is realized inside the algebra as the rotation about $\vec p$: the rotor $\tilde u_{\mathrm r}=\cos(\theta_{\mathrm{rat}}/2)+\sin(\theta_{\mathrm{rat}}/2)\vec u_p$ commutes with $\tilde P_{\Phi}$, since $iE/c$ is central and $\vec u_p$ commutes with $\vec p$, and it acts on the spinor module by the phase $e^{\pm i\theta_{\mathrm{rat}}/2}$, with $\theta_{\mathrm{rat}}$ the rotation angle about $\vec p$, real. The little-group scaling is therefore not an abstract relabelling; it is the rotation about the momentum axis acting on the two factors.

**The weight is the helicity.** An object of helicity $h$ scales as ${r'_{t}}^{-2h}$, so a monomial of $\varpi_{\mathrm{twz}}$-degree $d_{\imath}$ and $\bar\varpi_{\mathrm{twz}}$-degree $d_{\bar k}$ in a particle of definite helicity has

$$
h=\tfrac12\bigl(d_{\bar k}-d_{\imath}\bigr).
$$

The spinor $\digamma_{\mathrm{hlc}}$ has $d_{\imath}=+1$ and therefore $h=-\tfrac12$; its conjugate has $h=+\tfrac12$. The fundamental carrier is the object of weight $\pm\tfrac12$, which is the operator's own statement at the momentum axis, $\digamma_{\mathrm{hlc}}=\pm\frac{h}{4\pi}$ on the two lines of the carrier. **The two levels agree because both are the projection on $\vec u_p$, read in the two descriptions of the same spinor: as an element of a left ideal, and as a factor of a null momentum.**

Two qualifications are kept explicit. The full little group of a massless particle is $ISO(2)$ and not $U(1)$; the compact part is what acts nontrivially on finite-helicity states, and it is the part the factorisation exhibits. And the identification of helicity with the $U(1)$ weight is standard representation theory: the algebra supplies the $U(1)$ action through its rotation rotors, and it does not select which weight is physical.

## The Massless Limit Is Singular

It is tempting to say that the massive case follows from the massless one by continuity. It does not, and the algebra shows why in one line.

For $m\neq0$ the matrix $\mathsf{M}_2(\tilde P_{\Phi})$ is invertible and of rank two, so there is no one-term factorisation; the massive bispinor needs two,

$$
p_{\alpha\bar\beta}=\varpi_{\mathrm{twz},\alpha}\bar\varpi_{\mathrm{twz},\bar\beta}+\mu_\alpha\bar\mu_{\bar\beta},
$$

one term per physical polarization, and the little group is $SU(2)$ rather than $U(1)$. The algebraic defect measures the discontinuity:

$$
\tilde P_{\Phi}^2=2\,\frac{iE}{c}\,\tilde P_{\Phi}+m^2c^2e_t,
$$

so the zero-divisor relation $\tilde P_{\Phi}^2=2P_t\tilde P_{\Phi}$ holds only at $m=0$, and the departure is additive of order $m^2$. Three things fail to be continuous: the **rank** drops from two to one, the **factorisation** from two terms to one, and the **little group** from $SU(2)$ to $ISO(2)$.

The operator, by contrast, is continuous through the limit: it never divides by the mass, and $\digamma_{\mathrm{hlc}}=\vec u_p\cdot\vec S$ is defined at every $m$. What fails is not the operator but the identification of its values with a little-group weight, which is why the article keeps the two levels apart instead of deriving one from the other.

## Chirality and Helicity

The two words name different things and coincide at one mass.

**Chirality** is the eigenvalue of the chirality basis operator $\xi=-iR_{\mathrm{axf},\vec e_z}$, a pure right multiplier that carries one chiral half to minus itself and the other to plus itself. It is not a central sign but a slot: it acts on the right, a product takes the value of its right factor, and a left multiplication keeps the value. It is Lorentz invariant with or without a mass, because it commutes with the six Lorentz basis operators (*Chiral Fermions in the Biquaternion Framework*).

**Helicity** is the eigenvalue of $\digamma_{\mathrm{hlc}}$, a projection on the momentum, fixed by the little group and dependent on it.

So the two differ in kind. Chirality is a fixed side, the same in every frame and for every momentum. Helicity is a projection, and it needs a momentum to exist. At $m=0$ the two labels agree on a positive-energy state, because the little group is then all that remains of the Lorentz action and both reduce to the same weight; on a negative-energy state they are opposite, which is the same statement read on the antiparticle.

**Why helicity is conserved and chirality is not.** Helicity is $\vec J\cdot\vec u_p$, since the orbital part contributes nothing, and both factors are conserved by a free motion: $\vec J$ generates the rotations the free Hamiltonian respects, and $\vec p$ is conserved, so $\vec u_p$ is conserved with it. Hence $[\digamma_{\mathrm{hlc}},\tilde H_\Psi]=0$ for a free particle, at any mass. Chirality has no such argument, because what breaks it is the mass and not the motion. One is a symmetry of the free motion, the other a symmetry of the massless Lagrangian.

In the algebra the mass is the off-diagonal pair that exchanges the two chiral parts, central in coefficient and odd under the basis operator (*The Hydrogen Atom in Biquaternionic Form — The Relativistic Case*). At $m=0$ the pair decouples into two Weyl equations, one per part, and that decoupling is why the two labels agree there.

**The basis operator at an axis.** The chirality basis operator is the frame's version of the grading that separates the two parts: the right multiplier $R(i\vec u_p)$ at the momentum axis, up to the sign that decides which part is called positive. The two parts of a Dirac spinor are the two left ideals at a declared axis, the right multiplier separates them, and the basis operator is that multiplier at the frame's own axis $\vec e_z$ (*Operator Chirality on the Biquaternion Algebra*; *Spinors and Dirac Spinors in the Biquaternion Algebra*, §*The Pair Is a Multiplicity*).

## What the Algebra Supplies and What It Does Not

**Supplied by the algebra.**

- The operator $\digamma_{\mathrm{hlc}}=\vec u_p\cdot\vec S$ as a Hermitian element of $\mathbb{B}_{\Psi}$ on every carrier, and its action as a left multiplication.
- Its spectrum, the weight string $\frac{h}{2\pi}\,h$ of the carrier, and the two carrier vectors of the fundamental case: the pure state at the axis and its companion nilpotent.
- The reversal law and the rotation law, as statements about the idempotents at an axis.
- The identification of the null momentum with a zero divisor, of the zero divisor with a rank-one matrix, and of the rank-one matrix with the factorisation into two spinors.
- The brackets as the invariant symplectic pairing, and their antisymmetry as the antisymmetry of that pairing.
- The little-group scaling as the ambiguity of the factorisation, and its compact part as the rotation about the momentum axis.

**Not supplied.**

- **The momentum.** The algebra has no state and no momentum; $\vec p$ is a datum the state carries, and without it there is no axis and no operator.
- **The mass.** Whether $m=0$ is an input. The framework represents the Proca field as readily as the Maxwell one, and the two differ in whether the label is invariant and whether the third value is physical.
- **The gauge removal.** The deletion of the zero value of a massless vector field is a property of the gauge orbit and not of the spectrum.
- **The doubling.** Whether both helicities are present is a property of the field.
- **The choice of carrier.** Which particle uses which carrier — the electron the fundamental module, the photon the adjoint — is physics and not algebra.
- **The amplitude calculus.** The Parke–Taylor formula, the colour structure and the momentum-conservation constraints are transcribed, not derived.
- **A massive spinor-helicity extension.** The two-term bispinor and its $SU(2)$ little group are not developed.

## Summary

Helicity is the projection of the spin on the direction of motion, $\digamma_{\mathrm{hlc}}=\vec u_p\cdot\vec S$, a Hermitian element of $\mathbb{B}_{\Psi}$ acting by left multiplication on every carrier of the algebra. On a carrier of spin $s$ its spectrum is the weight string $\frac{h}{2\pi}\,h$, $h\in\{-s,\dots,s\}$, and the largest value is the spin: the carrier fixes the list, the axis orders it, the state selects a member. The orbital part drops out identically, $\vec L\cdot\vec p=0$, which is why the projection is a name and not a component of $\vec J$. On the fundamental carrier the two values are $\pm\frac{h}{4\pi}$, carried by the pure state $\tilde\Pi_{\mathrm{id},+}(\vec u_p)$ and its companion nilpotent; on the adjoint the spectrum is $\{+1,0,-1\}$ in units of $\frac{h}{2\pi}$, with the propagation direction at zero; on the symmetric square it is $\{-2,-1,0,1,2\}$. The reversal law is exact and the rotation law is a conjugation by the rotor; a boost is what breaks the label, and only for a particle slower than light.

At $m=0$ a second description opens. The null momentum is a zero divisor, hence a rank-one matrix, hence a product of two spinors, and the ambiguity of that product is the little-group scaling, a $U(1)$ for real momenta, realized as the rotation about $\vec p$. Helicity is the weight of that scaling, $h=\tfrac12(d_{\bar k}-d_{\imath})$, and the factors $\varpi_{\mathrm{twz}}$ and $\bar\varpi_{\mathrm{twz}}$ carry $\mp\tfrac12$: the two levels of the article agree. The limit $m\to0$ is singular in the factorisation — rank, number of terms and little group all change — while the operator passes through it untouched, so the weight is not derived from the operator but identified with it where both exist. Chirality is a different object: a right multiplier, a slot, invariant at every mass, coinciding with helicity only in the massless case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec u_p=\vec p/\lvert\vec p\rvert$ | The unit along the momentum, declared; a pure real quaternion, $\vec u_p^2=-e_t$ |
| $\vec u_\Phi=2\pi\vec\nu_\Phi/\lvert2\pi\vec\nu_\Phi\rvert$ | The unit along the wave vector; the same element as $\vec u_p$, since $\vec p=h\,\vec\nu_\Phi$ |
| $\digamma_{\mathrm{hlc}}=\vec u_p\cdot\vec S$ | The helicity operator, $\in\mathbb{B}_{\Psi}$, acting by left multiplication; $\frac{h}{2\pi}$ times the dimensionless $\tfrac{i}{2}\mathrm{ad}_{\vec u_p}$ on the adjoint |
| $\vec S$ | The rotation generator read as one vector, $\tilde S_{\Psi,k}=\frac{h}{4\pi}i\vec e_{\imath}$ on the fundamental carrier |
| $\tilde\Pi_{\mathrm{id},\pm}(\vec u_p)=\tfrac12(e_t\pm i\vec u_p)$ | The idempotents at the momentum axis; $\tilde\Pi_{\mathrm{id},+}$ is the vector of the value $+\frac{h}{4\pi}$ in $S_+(\vec u_p)$ |
| $S_\pm(\vec u_p)=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u_p)$ | The minimal left ideals at the axis; an elementary spinor is an element of one of them |
| $\tilde{Ζ}=i\vec u_p$ | The root of $+1$ on the fundamental carrier; $\digamma_{\mathrm{hlc}}=\frac{h}{4\pi}\tilde{Ζ}$ |
| $\tilde P_{\Phi}=\frac{iE}{c}e_t+\vec p$ | The four-momentum, null when $\langle\tilde P_{\Phi}\rangle_{\natural}=0$ |
| $\varpi_{\mathrm{twz}},\ \bar\varpi_{\mathrm{twz}}$ | In the factorisation sections only: the two spinors with $\mathsf{M}_2(\tilde P_{\Phi})=\varpi_{\mathrm{twz}}\bar\varpi_{\mathrm{twz}}^{T}$; not the operator |
| $\langle ij\rangle,\ [ij]$ | The brackets, the symplectic pairing on $S$ and on $\bar S$ |
| $r'_t$ | The little-group scaling, $\varpi_{\mathrm{twz}}\mapsto r'_t\varpi_{\mathrm{twz}}$, $\bar\varpi_{\mathrm{twz}}\mapsto {r'_{t}}^{-1}\bar\varpi_{\mathrm{twz}}$; $\lvert r'_t\rvert=1$ for a real momentum |
| $h$ | The helicity, the weight; the operator's eigenvalue is $\frac{h}{2\pi}\,h$ |
| $\xi=-iR_{\mathrm{axf},\vec e_z}$ | The chirality basis operator, a pure right multiplier; not the helicity |

## Further Reading

- [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html), for the spin-one helicity operator, its three values and the gauge removal of the longitudinal state.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the little group and the adjoint-action reading of $\digamma_{\mathrm{hlc}}$.
- [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html), for the helicity element $\tilde{Ζ}$, the two helicity lines and the mass that leaves them intact.
- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the massive case, where the label is not invariant.
- [Canonical Quantization of the Biquaternion Graviton Field](canonical-quantization-of-the-biquaternion-graviton-field.html), for the spin-two spectrum and the two physical states.
- [The Determination of the Possible Spins in Biquaternionic Form](the-determination-of-the-possible-spins-in-biquaternionic-form.html), for the little-group classification and the statement that the reduction from $2s+1$ to two is the gauge condition.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html), for the spin operator whose projection this is.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html), for the chirality basis operator and its invariance.
- [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html), for the non-conservation of chirality at nonzero mass.
- [Spinors and Dirac Spinors in the Biquaternion Algebra](../articles_maths/spinors-and-dirac-spinors-in-the-biquaternion-algebra.html), for the elementary spinor, the weights $\pm\tfrac12$, and the two parts of a Dirac spinor as two copies.
- [From the Spin to the Carriers and the Closures](../articles_maths/the-carriers-the-representation-the-spin-and-the-closure.html), for the definition of spin as a maximal weight and the classification of the carriers.
- [Operator Chirality on the Biquaternion Algebra](../articles_maths/operator-chirality-on-the-biquaternion-algebra.html), for the chirality basis operator as a right multiplier and the two parts it separates.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the zero-divisor criterion and the pure and non-pure families.
- [The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$](../articles_maths/the-forms-the-norms-and-the-singular-set-of-m4c.html), for the rank-one statement and the spinor factorisation.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), for the module $S$, the conjugate module and the symplectic form.
- Zvi Bern, Lance J. Dixon and David A. Kosower, "On-shell methods in perturbative QCD," *Annals of Physics* **322** (2007) 1587–1634, for helicity amplitudes in practical calculations.
- Henriette Elvang and Yu-tin Huang, *Scattering Amplitudes in Gauge Theory and Gravity* (Cambridge University Press, 2015), for the spinor-helicity formalism and the little-group weights.
- Stephen J. Parke and T. R. Taylor, "An amplitude for $n$ gluon scattering," *Physical Review Letters* **56** (1986) 2459–2460, for the Parke–Taylor formula.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge University Press, 1984), for the two-component spinor calculus and the reality condition.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge University Press, 1995), §2.5, for the massless little group and helicity as its weight.
- E. Wigner, "On unitary representations of the inhomogeneous Lorentz group," *Annals of Mathematics* **40** (1939) 149–204, for the classification of the little groups.
