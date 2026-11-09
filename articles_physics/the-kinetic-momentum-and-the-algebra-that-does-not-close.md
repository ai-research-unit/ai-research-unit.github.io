# __The Kinetic Momentum and the Algebra That Does Not Close__

## Introduction

Minimal coupling replaces the canonical momentum by the mechanical one, $\vec p\to\vec\pi=\vec p-ϙ\vec A$. The canonical commutation relation is written for the canonical momentum. The two statements sit side by side in every textbook, and the question this article answers is what the relation can and cannot see of the replacement.

The answer has two halves, and they do not agree. The first half of the relation, the bracket of position with momentum, is blind to the vector potential. It holds for the canonical momentum and for the mechanical one, and it holds for any shift of the momentum by a function of position. The second half, the bracket of two momenta with each other, is not blind. It vanishes for the canonical momentum and equals the field strength for the mechanical one.

A third statement follows, and it is the reason for the title. The angular momentum built from the mechanical momentum does not close on itself. Its bracket is the rotation bracket plus a term quadratic in position, and that term is a multiplication operator. The three components do not span a Lie algebra.

The article argues by contrast. It names the textbook objection in its own section and answers it. It then records what the failure costs: the angular momentum of the Landau problem that is conserved is the canonical one and not the mechanical one, which is why the companion article builds its conserved quantity from $\vec p$.

The framework enters in three places and nowhere else. It supplies the unit $\hbar=\frac{m\,c}{k_m}$, the centrality of the field strength, and the separation between the internal algebra and the envelope. It does not supply the bracket, which is ordinary operator algebra, and it does not predict the anomaly term, which is the standard magnetic torque.

The companion articles supply the pieces:
- Companion article *Landau Levels in Biquaternionic Form*, for the mechanical momentum, the central field-strength commutator and the guiding centre.
- Companion article *The Covariant Derivative and Gauge Connection in Biquaternionic Form*, for the connection, its curvature and the covariance law.
- Companion article *The Biquaternion Framework and the Canonical Commutation Relation: Independence, Not a Defect*, for the trace obstruction and the independence of the internal algebra.
- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the rotation bracket and the cross product as a commutator.
- Companion article *Gauge Transformations of the First and Second Kind in Biquaternionic Form*, for the central phase and its transformation law.

**Notation, once.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_t=1$ and $\vec e_j^2=-e_t$. The unit of action is $\hbar=\frac{m\,c}{k_m}$, so $i\hbar=\frac{m\,c\,i}{k_m}$. Position is $\vec r=(r_x,r_y,r_z)$. The canonical momentum is $p_\eta=-i\hbar\,\partial/\partial r_\eta$. The mechanical momentum is $\pi_\eta=p_\eta-ϙA_\eta$ and its algebra element is $\tilde\pi_\eta=\pi_\eta\,e_t$. The charge is $ϙ$ in coulomb. Units are SI throughout, as *Physics Units and Common Elements Conventions* fixes them.

## The Two Momenta

Minimal coupling is the replacement of one momentum by another.

$$
\pi_\eta=p_\eta-ϙA_\eta,\qquad \tilde\pi_\eta=\pi_\eta\,e_t .
$$

The two differ by a function of position. The canonical momentum differentiates and the vector potential multiplies. Nothing else separates them.

The distinction is not a choice of notation. The two momenta transform differently under a gauge transformation, and the difference is the whole content of the next section.

Under $\vec A\to\vec A+\nabla\lambda$ the canonical momentum is unchanged, the mechanical momentum shifts, and the field strength is unchanged.

| object | under $\vec A\to\vec A+\nabla\lambda$ |
|---|---|
| $\vec p$ | unchanged |
| $\vec\pi$ | $\vec\pi-ϙ\nabla\lambda$ |
| $\vec B$ | unchanged |
| $[\pi_j,\pi_\eta]$ | unchanged |

The state carries the compensating central phase. The companion article on gauge transformations of the first and second kinds fixes that phase, and the Aharonov–Bohm article records what it does around a closed path.

## What the Relation Fixes

The canonical commutation relation, in the framework's units, is

$$
[r_j,p_\eta]=i\hbar\,\delta_{j\eta},\qquad i\hbar=\frac{m\,c\,i}{k_m}.
$$

The mechanical momentum satisfies the same relation, and the reason is one line. The vector potential is a function of position, so it commutes with position:

$$
[r_j,\pi_\eta]=[r_j,p_\eta]-ϙ\,[r_j,A_\eta]=i\hbar\,\delta_{j\eta}.
$$

The relation therefore does not separate the two momenta. Both satisfy it. A relation that both objects satisfy cannot be the statement that decides between them.

The blindness is wider than the two examples. Any shift of the momentum by a function of position leaves the relation untouched:

$$
[r_j,\,p_\eta+f_\eta(\vec r)]=i\hbar\,\delta_{j\eta}.
$$

The converse runs in the same direction. If two momenta give the same bracket with position, their difference commutes with position, and on the Schrödinger carrier the commutant of the position operators is the algebra of functions of position. The difference is then a function of position, and nothing else.

The relation fixes the momentum **only up to a function of position**. That is the exact statement of what it does and does not determine. It fixes the generator of translations, and it leaves free everything that multiplies.

**What follows.** The canonical commutation relation cannot tell a relabelling from a physical field. A shift that is a gradient is a change of description. A shift that is not a gradient is a change of physics. The relation accepts both without comment, because both leave its left-hand side unchanged.

## The Half That Breaks

The relation has a second half, and the second half is not blind.

For the canonical momentum the components commute:

$$
[p_j,p_\eta]=0 .
$$

The same shift by a function of position gives

$$
[p_j+f_j,\,p_\eta+f_k]=i\hbar\left(\partial_k f_j-\partial_j f_k\right).
$$

The right-hand side is the antisymmetrised derivative of the shift. It vanishes exactly when the shift is a gradient.

Minimal coupling takes $f_k=-ϙA_\eta$ and the right-hand side becomes the field strength:

$$
[\pi_j,\pi_\eta]=i\hbar\,ϙ\,\varepsilon_{j\eta l}B_l=\frac{m\,c\,i\,ϙ}{k_m}\,\varepsilon_{j\eta l}B_l .
$$

This is the commutator the companion article on Landau levels builds the whole problem on. Here it carries a different reading: it is the exact measure of how far minimal coupling is from a relabelling.

The two halves of the relation therefore behave differently under one and the same shift.

| shift | $[r_j,P_\eta]$ | $[P_j,P_\eta]$ | implemented by a unitary |
|---|---|---|---|
| $f_\eta=\partial_k\lambda$ | $i\hbar\,\delta_{j\eta}$ | $0$ | yes |
| $f_\eta=-ϙA_\eta$, $\vec B\neq0$ | $i\hbar\,\delta_{j\eta}$ | $i\hbar\,ϙ\,\varepsilon_{j\eta l}B_l$ | no |

The last column is the physical content. A gradient shift is implemented on the states by the central phase, so it is a relabelling and no observable changes. On a simply-connected region where $\vec B\neq0$ no single-valued $\lambda$ exists, no such phase implements the shift, and the second half of the relation records the failure.

**The asymmetry, stated once.** The first half of the relation is invariant under every shift by a function of position. The second half is invariant only under the gradient ones. The field lives in the difference between the two invariance groups.

## The Two Angular Momenta

Two angular momenta are built from the two momenta, and they are different operators.

$$
\tilde L_{\mathrm{orb},i}=\varepsilon_{ij\eta}\,r_j\,p_\eta\,e_t ,\qquad \tilde L_{\mathrm{kin},i}=\varepsilon_{ij\eta}\,r_j\,\pi_\eta\,e_t .
$$

The second is the physical one. It is the moment of the mechanical momentum, and it is the quantity a torque acts on. The first is the generator of rotations of the wave function.

The two differ by the vector potential:

$$
\vec L_{\mathrm{kin}}=\vec L_{\mathrm{orb}}-ϙ\,\vec r\times\vec A .
$$

In the symmetric gauge $\vec A=\tfrac12\vec B\times\vec r$ with $\vec B=B\vec u_z$ the difference is explicit:

$$
\tilde L_{\mathrm{kin},z}=\tilde L_{\mathrm{orb},z}-\frac{ϙB}{2}\left(r_x^2+r_y^2\right)e_t .
$$

The correction is quadratic in position and grows with the orbit. It is not a small term at large radius, and it is not removable by a gauge choice because $\vec B$ is gauge invariant.

The identity was checked numerically in the symmetric gauge on a spectral grid: the two sides of $\tilde L_{\mathrm{kin},z}=\tilde L_{\mathrm{orb},z}-\frac{ϙB}{2}(r_x^2+r_y^2)e_t$ agree to a relative residual of $2.8\times10^{-16}$, which is machine precision.

## The Bracket of the Kinetic Angular Momentum

With $\vec B$ uniform, the bracket of the kinetic angular momentum is

$$
\boxed{\;[\tilde L_{\mathrm{kin},i},\tilde L_{\mathrm{kin},j}]=\frac{m\,c\,i}{k_m}\,\varepsilon_{ij\eta}\Bigl(\tilde L_{\mathrm{kin},\eta}+ϙ\,r_\eta\,(\vec r\cdot\vec B)\Bigr)\;}
$$

The bracket is the rotation bracket plus one term. The extra term carries no derivative, is quadratic in position, and vanishes with the field.

**The reduction.** Two contraction rules generate everything:

$$
[r_j,\pi_\eta]=i\hbar\,\delta_{j\eta},\qquad [\pi_j,\pi_\eta]=i\hbar\,ϙ\,\varepsilon_{j\eta l}B_l .
$$

Write $\tilde L_{\mathrm{kin},i}=\varepsilon_{iab}r_a\pi_b e_t$ and use $[AB,C]=A[B,C]+[A,C]B$ on the four contractions. The two rules above, with $\vec B$ taken uniform so that it commutes with $\vec r$, reduce the contractions to the boxed form. The uniform-field hypothesis is what makes the statement exact; a position-dependent field adds gradient terms that the bracket above does not carry.

**The check.** The reduction was verified symbolically on the word algebra generated by $\vec r$ and $\vec\pi$ with the two contraction rules, with $\hbar$, $ϙ$ and $\vec B$ kept symbolic. The free case $ϙ\to0$ returns $[\tilde L_{\mathrm{orb},i},\tilde L_{\mathrm{orb},j}]=\frac{m\,c\,i}{k_m}\varepsilon_{ij\eta}\tilde L_{\mathrm{orb},\eta}$ exactly, which validates the engine before it is used. The boxed form then returns a residual of zero on all three cyclic pairs.

The same statement was verified numerically in the symmetric gauge, on a $64^3$ spectral grid with $\hbar$, $c$ and $ϙ$ at their SI values and $B=1$ T. The residual of $[\tilde L_{\mathrm{kin},x},\tilde L_{\mathrm{kin},y}]$ against $\frac{m\,c\,i}{k_m}(\tilde L_{\mathrm{kin},z}+ϙ\,r_z(\vec r\cdot\vec B))$ is $6.4\times10^{-9}$ relative, at the discretisation floor of the grid, which the elementary commutator $[r_x,p_x]=i\hbar$ reproduces to $1.2\times10^{-8}$ on the same grid. Dropping the extra term fails the same comparison by $173$ per cent.

## Why It Does Not Close

The bracket above is not a Lie bracket on the span of the generators, and the reason is visible in the shape of the extra term.

**Different kinds of object.** The generators $\tilde L_{\mathrm{kin},\eta}$ contain a derivative. The extra term $ϙ\,r_\eta(\vec r\cdot\vec B)$ does not; it is a function of position times $e_t$, hence a multiplication operator. A linear combination of the $\tilde L_{\mathrm{kin},\eta}$ is a first-order differential operator. The right-hand side is one of those plus a multiplication operator. The two are not the same kind of thing, and no coefficients turn one into the other.

**What fails is closure, not consistency.** The Jacobi identity holds for the bracket, because the bracket is a commutator of operators and commutators always satisfy it. The failure is narrower and sharper: the commutator of two members of the triple is not a member of the span of the triple. A reader who expects the Jacobi identity to be the test will look in the wrong place.

**Nothing repairs it.** Three repairs suggest themselves and all fail. A rescaling of the generators rescales the anomaly with them. A linear redefinition mixes the generators among themselves and leaves the anomaly outside the span, because the anomaly is independent of the generators. A gauge choice cannot remove it, because the anomaly is built from $\vec B$ and $\vec B$ is gauge invariant.

**The free case is the control.** At $ϙ=0$ the anomaly vanishes and the bracket closes exactly on the rotation algebra. The failure is therefore not a property of the cross product or of the biquaternion notation. It is a property of the field, and it appears exactly when the second half of the canonical relation stops vanishing.

## The Objection from Textbook Practice

The strongest objection is that none of this is new. The mechanical momentum is not the generator of translations, its angular momentum is not conserved, and every textbook on the quantised charged particle says both. The objection is correct about the physics.

It is not correct about what the corpus records. The corpus states the commutator of the mechanical momenta and uses it. It does not state that the two halves of the canonical relation have different invariance groups under a shift of the momentum. It does not state the bracket of the kinetic angular momentum. Both are exact operator identities, and both are needed to say what minimal coupling does to an algebra rather than to a Hamiltonian.

The second part of the answer is structural, and it is the reason the result belongs in this corpus rather than in a footnote.

**The anomaly has the corpus's own shape.** In the companion article on the covariant derivative, the commutator of two covariant derivatives is not a third covariant derivative. It is multiplication by the curvature. That article reads the curvature exactly as the object that the commutator produces and the operators do not contain.

The bracket derived here has the same shape one rank up. The commutator of two kinetic angular momenta is not a third kinetic angular momentum. It is a third one plus multiplication by a field quantity. The commutator leaves the span of the operators and lands on multiplication, exactly as the curvature does.

The parallel is not decorative. Minimal coupling turns a derivative into a connection, and a connection's commutator is its curvature. The mechanical momentum is the spatial part of that connection, the field strength is its curvature, and the kinetic angular momentum is the cross product of position with the connection. The anomaly is what a cross product of position with a connection produces when the curvature does not vanish.

## What Is Conserved

The bracket says what does not close. The Hamiltonian says what does not survive.

In the symmetric gauge with $\vec B=B\vec u_z$, the Hamiltonian is $H=\frac{1}{2m}(\pi_x^2+\pi_y^2)$ and the two angular momenta behave differently under it.

The canonical one is conserved:

$$
[\tilde L_{\mathrm{orb},z},H]=0 .
$$

The kinetic one is not:

$$
[\tilde L_{\mathrm{kin},z},H]=-\frac{ϙB}{2}\left[\left(r_x^2+r_y^2\right),H\right],
$$

and the inner commutator does not vanish. With $\vec r_\perp\cdot\vec\pi_\perp=r_x\pi_x+r_y\pi_y$,

$$
\left[\left(r_x^2+r_y^2\right),H\right]=\frac{2\,i\,\hbar}{m}\,\vec r_\perp\cdot\vec\pi_\perp+\frac{2\,\hbar^{2}}{m}.
$$

Both statements were checked on the same spectral grid. The canonical commutator returns a residual of $3.1\times10^{-42}$ relative to the energy scale, which is zero to machine precision. The kinetic one does not vanish: it matches the closed form above to a relative residual of $4.9\times10^{-8}$, at the grid's floor of $1.2\times10^{-8}$ as calibrated by $[r_x,p_x]=i\hbar$.

**The consequence for the companion article.** The angular momentum that is conserved in the Landau problem is the canonical one. This is why the companion article on Landau levels builds $\tilde L_{\mathrm{orb},z}=(\vec r\times p)_z\,e_t$ from the canonical momentum and not from the mechanical one. That choice is not a convenience. The other operator does not commute with the Hamiltonian, and its bracket does not close.

The physical statement is the classical one. A charged particle in a uniform magnetic field feels a torque $\vec r\times(ϙ\vec v\times\vec B)$, whose $z$ component is $-\frac{ϙB}{2}\,d(r_x^2+r_y^2)/dt$. The kinetic angular momentum changes at exactly that rate. The canonical one does not, because it is not the quantity the torque acts on. Quantum mechanically the same two facts appear as the two commutators above.

**The linear version is already in the corpus.** The companion article *The Relativistic Particle in an External Field in Biquaternionic Form* records the same fact one rank down: the conserved components of the momentum are the canonical ones and the kinetic momentum rotates. That article states it for the four-momentum and describes the rotating vector classically; the statement here is its rank-two counterpart, where the conserved generator is the orbital angular momentum and the rotating one is the kinetic angular momentum. Neither statement is new to physics and the two are mutually consistent, which is the check that matters: a corpus that said the kinetic four-momentum is the physical one and the kinetic angular momentum the conserved one would contradict itself.

**Why the degeneracy is not counted by the kinetic generator.** In the companion article on Landau levels the degeneracy ladder within a level is built from the guiding-centre coordinates, which commute with the Hamiltonian and move the orbit from one degenerate state to another at fixed energy. That is the same fact read from the other side. A generator that does not commute with $H$ cannot label the states of a level, so the ladder has to be built from operators that do, and the kinetic angular momentum is not one of them.

## The Reading in the Algebra

The cross product is the vector part of a quaternion product. With $\vec r$ and $\vec\pi$ read as pure vector quaternions, their product is $-\vec r\cdot\vec\pi+\vec r\times\vec\pi$, and the three components $\tilde L_{\mathrm{kin},\eta}$ are the components of the vector part multiplied by $e_t$.

The anomaly sits in the same place as the field strength. It is a real function of position times $e_t$, so it is central in the quaternion factor and labelled by position. The companion article on Landau levels makes the same point about $\vec B$: the field strength there is central, and that centrality is what makes the spin-0 problem a scalar oscillator problem.

The two statements are one statement seen twice. The field strength is central because it carries no quaternion direction. The anomaly is central because it carries no derivative and no quaternion direction either. Both are elements of the centre of the operator algebra, and neither can be written as a combination of the derivative-carrying generators.

**What the algebra itself cannot hold.** Inside $\mathbb{B}$ the anomaly has no home. Every commutator of two elements of $\mathbb{B}$ has zero scalar part, by the trace theorem of the companion article on the canonical relation, so no pair of algebra elements produces a non-zero central multiple of $e_t$. The anomaly is a central multiple of $e_t$ multiplied by a function of position, and position is not an element of $\mathbb{B}$. The failure therefore lives in the envelope algebra and not in the internal algebra, which is the same separation the companion article draws between $\mathcal{A}$ and $\mathcal{M}$.

## What the Framework Supplies

**Supplies.** The unit $\hbar=\frac{m\,c}{k_m}$, so that every bracket is measured in one unit and no scale is fixed by the algebra. The centrality of the field strength, which is what makes $[\pi_j,\pi_\eta]$ a central multiple of $e_t$; the anomaly is central for a different reason, being a real function of position times $e_t$ with no quaternion direction. The separation between the internal algebra and the envelope, without which the failure would be read as a failure of $\mathbb{B}$.

**Transcribes.** The two momenta, the two angular momenta, the bracket, the non-closure, the conservation statements. All of it is ordinary operator algebra in the notation of the corpus.

**Does not supply.** Any bracket that differs from the standard one. Any prediction that distinguishes the reformulation from the quantised charged particle. Any repair of the non-closure: the anomaly is the magnetic torque and it is not a defect of the algebra.

**Open.** Whether the anomaly has a finite shadow. The companion article on the canonical relation builds its finite shadow from the Weyl pair, and the anomaly is quadratic in position, so the question is whether a finite module carries a representation of the deformed triple. This article does not settle it.

## Summary

Minimal coupling replaces $\vec p$ by $\vec\pi=\vec p-ϙ\vec A$, and the canonical commutation relation accepts the replacement without noticing it. The bracket of position with momentum is unchanged, because the vector potential is a function of position and commutes with position; more generally, any shift of the momentum by a function of position leaves that bracket untouched, so the relation fixes the momentum only up to a function of position. The bracket of two momenta is not blind: it vanishes for the canonical momentum, is the antisymmetrised derivative of the shift for a general one, and equals $\frac{m\,c\,i\,ϙ}{k_m}\varepsilon_{j\eta l}B_l$ for minimal coupling.

The kinetic angular momentum $\tilde L_{\mathrm{kin},i}=\varepsilon_{ij\eta}r_j\pi_\eta e_t$ inherits the difference. With uniform $\vec B$,

$$
[\tilde L_{\mathrm{kin},i},\tilde L_{\mathrm{kin},j}]=\frac{m\,c\,i}{k_m}\,\varepsilon_{ij\eta}\Bigl(\tilde L_{\mathrm{kin},\eta}+ϙ\,r_\eta\,(\vec r\cdot\vec B)\Bigr),
$$

a rotation bracket plus a multiplication operator quadratic in position. The three components do not span a Lie algebra, because the extra term is not a first-order differential operator. Jacobi holds; closure fails. No rescaling, redefinition or gauge choice repairs it, and the failure vanishes exactly with the field.

The anomaly has the shape of the curvature in the covariant derivative article: a commutator that leaves the span of the operators and lands on multiplication. The mechanical momentum is the spatial part of the connection, the field strength is its curvature, and the kinetic angular momentum is the cross product of position with the connection.

The conserved angular momentum of the Landau problem is the canonical one. The kinetic one does not commute with the Hamiltonian, and its rate of change is the magnetic torque. This is why the companion article on Landau levels builds its conserved quantity from $\vec p$. The framework supplies the unit, the centrality of the field strength, and the separation between the internal algebra and the envelope. It supplies no new prediction, and the anomaly is not a defect to be repaired.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_j^2=-e_t$ |
| $\hbar=\frac{m\,c}{k_m}$ | Unit of action; $i\hbar=\frac{m\,c\,i}{k_m}$ |
| $ϙ$ | Electric charge, in coulomb |
| $\vec r=(r_x,r_y,r_z)$ | Position |
| $p_\eta=-i\hbar\,\partial/\partial r_\eta$ | Canonical momentum |
| $\pi_\eta=p_\eta-ϙA_\eta$ | Mechanical momentum |
| $\tilde\pi_\eta=\pi_\eta\,e_t$ | Mechanical momentum as an algebra element |
| $\vec A$ | Vector potential; $\vec B=\nabla\times\vec A$ |
| $[r_j,\pi_\eta]=i\hbar\,\delta_{j\eta}$ | Position–momentum bracket; holds for both momenta |
| $[\pi_j,\pi_\eta]=\frac{m\,c\,i\,ϙ}{k_m}\varepsilon_{j\eta l}B_l$ | Field-strength commutator; central |
| $\tilde L_{\mathrm{orb},i}=\varepsilon_{ij\eta}r_jp_\eta e_t$ | Canonical angular momentum |
| $\tilde L_{\mathrm{kin},i}=\varepsilon_{ij\eta}r_j\pi_\eta e_t$ | Kinetic angular momentum |
| $\vec L_{\mathrm{kin}}=\vec L_{\mathrm{orb}}-ϙ\,\vec r\times\vec A$ | The two angular momenta |
| $[\tilde L_{\mathrm{kin},i},\tilde L_{\mathrm{kin},j}]=\frac{m\,c\,i}{k_m}\varepsilon_{ij\eta}\bigl(\tilde L_{\mathrm{kin},\eta}+ϙ\,r_\eta(\vec r\cdot\vec B)\bigr)$ | The bracket that does not close |
| $\frac{ϙB}{2}(r_x^2+r_y^2)e_t$ | Anomaly in the symmetric gauge, per component |
| $H=\frac{1}{2m}\sum_\eta\pi_\eta^2$ | Hamiltonian of a charge in a magnetic field |
| $[\tilde L_{\mathrm{orb},z},H]=0$ | Canonical angular momentum is conserved |
| $[\tilde L_{\mathrm{kin},z},H]=-\frac{ϙB}{2}[(r_x^2+r_y^2),H]$ | Kinetic angular momentum is not |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for minimal coupling, the mechanical momentum and the symmetric-gauge angular momentum.
- J. J. Sakurai, *Modern Quantum Mechanics* (Addison-Wesley, 1994), for the distinction between the canonical and the kinetic momentum in a magnetic field.
- C. Cohen-Tannoudji, B. Diu, and F. Laloë, *Quantum Mechanics* (Wiley, 1977), for the two angular momenta of the symmetric gauge and the guiding centre.
- R. Peierls, "Zur Theorie des Diamagnetismus von Leitungselektronen," *Zeitschrift für Physik* **80** (1933) 763–791, for the lattice version of the same replacement.
- M. V. Berry, "Quantal phase factors accompanying adiabatic changes," *Proceedings of the Royal Society A* **392** (1984) 45–57, for the phase that distinguishes a gauge shift from a physical change.
- Y. Aharonov and D. Bohm, "Significance of electromagnetic potentials in the quantum theory," *Physical Review* **115** (1959) 485–491, for a non-gradient potential having an observable effect.
- T. T. Wu and C. N. Yang, "Concept of nonintegrable phase factors and global formulation of gauge fields," *Physical Review D* **12** (1975) 3845–3857, for the obstruction to a single-valued gauge function on a region of non-zero field.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the vector product as the vector part of a quaternion product.
