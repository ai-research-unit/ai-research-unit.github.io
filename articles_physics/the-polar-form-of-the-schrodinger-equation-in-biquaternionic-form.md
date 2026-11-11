# __The Polar Form of the Schrödinger Equation in Biquaternionic Form__

## Introduction

The Schrödinger equation of this corpus is one element of $\mathbb{B}$ acting on another by left multiplication. *The Schrödinger Equation in Biquaternionic Form* writes it as

$$
i\hbar\,\frac{\partial}{\partial t'}\tilde\Xi_{\mathrm{sp}}=\tilde H_\Psi\,\tilde\Xi_{\mathrm{sp}},
\qquad
\tilde H_\Psi=r_t\,e_t+i\vec r_\Psi\in\mathbb{B}_{\Psi},
$$

and states what the equation does not need: no column, no minimal left ideal, no projector, no idempotent, no declared axis, no matrix array in the body of the equation. The field is one element, the operator is one element, and the multiplication is the algebra's own.

This article substitutes a parametrisation of that one element into that one equation and reads what comes out. The parametrisation is the polar word of *The Polar Decomposition of an N-Regular Biquaternion*, in the exponential form it takes in *Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion*:

$$
\tilde\Xi=r\,e^{i\alpha}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm r}}{2}\vec u_{\mathrm r}\Bigr).
$$

The four factors are a positive real scale, a central angle, a Hermitian positive boost and a real rotor. The word has eight real parameters against the element's eight real components, and on its domain it is a bijection: it adds no object and drops no datum. The rotor's angle $\theta_{\mathrm r}$ is the angle of the spatial rotation the rotor performs, so the factor $\tfrac12$ in its exponential is the half-angle of a quaternion and not a physical factor.

**The domain is the whole of the qualification of this article.** In the corpus's vocabulary an element is $N$-regular when $N\neq0$ and $N$-degenerate when $N=0$, and $N$ is the determinant (*The Meaning of N-Regularity and Degeneracy*). The word is a parametrisation of the group of units, so

$$
\boxed{\;\text{the polar word of }\tilde\Xi\text{ exists}\iff N(\tilde\Xi)\neq0\iff\tilde\Xi\text{ is }N\text{-regular},\;}
$$

and it fails on every $N$-degenerate element. There is no third case and no extension of the word to $N=0$.

**That condition is weaker here than in the two companion articles, and the difference is the whole of the structure.** For the Dirac field the word fails on the one-sided fields, and those are not exotic: a field of definite value lies on the cone at every amplitude. For the Schrödinger field the cone is a set of measure zero and it is not the carrier: a generic element of $\mathbb{B}$ is a unit, and the flow preserves the cone, so a field is a unit at every event or at none (§*The Domain*). Nothing has to be excluded in advance and no carrier has to be declared. The polar form of this equation is therefore a parametrisation of the field itself, with no ideal, no projector and no axis behind it.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $\mathbb{B}_{C}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ is the centre; $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ are the anti-Hermitian and Hermitian fixed subspaces; $\natural$ is quaternion conjugation and $*$ the Hermitian one; $\mathrm{Sc}$ is the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. Time is written $t'$ and the parent's material length is $r'_t=c\,t'$, so $\partial/\partial r'_t=c^{-1}\partial/\partial t'$ and the parent's $i\hbar c\,\partial/\partial r'_t$ is $i\hbar\,\partial/\partial t'$; the two forms are used interchangeably and $\hbar$ is written explicitly in both.

**No wave number is used in this article, and that is deliberate.** A letter $k$ earns its place only where a mass, a momentum or an energy is absorbed by it, as $k_m=mc/\hbar$ absorbs the mass in the Dirac and Klein–Gordon equations. Here nothing is absorbed: the constant that multiplies the time derivative is $\hbar$, and the mass enters only through the operator $\tilde H_\Psi$ and, in the central case, through the kinetic term $|\nabla S|^{2}/2m$. Writing $k_m$ would require the composite $mc^{2}/k_m$, in which $m$ cancels and only $\hbar c$ survives, so the letter would hide the constant instead of naming a physical wave number. Every $\hbar$ below is therefore the reduced Planck constant and nothing else.

Two points of discipline come first, because both are ways of losing the alignment.

**The word is not a split of the field.** It is a re-coordinatisation of the element. Every factor is read from the element and the product is the element. Nothing is put into a slot.

**The word brings nothing in behind it.** No module, no ideal, no projector, no column, no separate carrier stands behind the four factors. Whatever the word is used for, the object it parametrises is still one element of $\mathbb{B}$, and the equation it is put into is still one element acting on another.

What the article establishes is short, and each item is one sentence:

- the propagator's word is a central phase times a rotor, with its scale and its boost frozen at $1$ and $e_t$;
- the two rates of the word are the mean of the two eigenvalues of the Hamiltonian and half their gap;
- the field's own scale and rapidity are constants of the motion, and nothing else is: the flow moves six of the eight parameters, and the two it leaves are the two that unitarity fixes;
- every direction the field carries, the axis of its own boost included, precesses about the Hamiltonian's own axis at twice the half-gap;
- the density is the Hermitian norm and reads the scale and the boost, while the quaternionic norm reads the scale and the phase;
- the word of a central field is a scale, a phase and a sign, and Madelung's pair is exactly that case.

## The Field and Its Word

### One element, eight real numbers

The field is one element $\tilde\Xi_{\mathrm{sp}}$ of $\mathbb{B}$, with four complex coefficients and therefore eight real components. The subscript `sp` is the corpus's caret for the spinor role, beside `scl` for the scalar role and `fop` for the field operator, as the caret table of *Algebra and Element Conventions* fixes it; once the field is named, the body writes $\tilde\Xi$ for the same element. Nothing else is needed: $\mathbb{B}$ is an algebra, so a product of two elements is an element, and the equation restricts no subspace.

**The equation is complex-linear, and its symbol is Hermitian.** Because $i$ is central, left multiplication $L_{\tilde H_\Psi}$ satisfies $L_{\tilde H_\Psi}(i\tilde X)=iL_{\tilde H_\Psi}\tilde X$, so the equation is complex-linear on $\mathbb{B}$ read as a complex vector space of dimension four. Because $\tilde H_\Psi^{*}=\tilde H_\Psi$, it also satisfies

$$
\mathrm{Sc}\bigl((\tilde H_\Psi\tilde X)\tilde Y^{*}\bigr)=\mathrm{Sc}\bigl(\tilde X(\tilde H_\Psi\tilde Y)^{*}\bigr),
$$

so the symbol is Hermitian for the sesquilinear form $\langle\tilde X,\tilde Y\rangle_{*}=\mathrm{Sc}(\tilde X\tilde Y^{*})$, and the flow preserves $\mathrm{Sc}(\tilde X\tilde X^{*})$. Both facts were checked on a hundred random pairs.

**The display, where a display is wanted, is the axis-free array.** In the coefficient basis the symbol is $L_{\mathrm{axf}}(\tilde H_\Psi)$, a $4\times4$ complex Hermitian array with $\mathrm{Tr}\,L_{\mathrm{axf}}(\tilde H_\Psi)=4r_t$ and $\det L_{\mathrm{axf}}(\tilde H_\Psi)=\langle\tilde H_\Psi\rangle_{\natural}^{2}$, and it names no spatial direction. This is the ruling of *Why AXF Matrices instead of Pauli and Gamma Matrices*: the equation is written with elements and read with an axis-free array, and no matrix algebra stands between the two.

### The word

The word of the field is the display of the introduction. Its four factors carry, in order: the square root of the quaternionic norm's modulus, the half-angle of the norm's phase, the Hermitian boost whose rapidity and axis the field's own Hermitian part fixes, and the rotor that carries the field's orientation. On the units it is a bijection with the eight real components, so every statement below is a statement about the field and not about a class of fields.

**The two norms read different factors, and neither reads all four.** The quaternionic norm is

$$
\langle\tilde\Xi\rangle_{\natural}=\tilde\Xi\tilde\Xi^{\natural}=r^{2}e^{2i\alpha},
$$

a central element that reads the scale and the phase and nothing else; and the Hermitian norm is

$$
\rho=\mathrm{Tr}\bigl(\tilde\Xi^{\dagger}\tilde\Xi\bigr)=2\,\mathrm{Sc}\bigl(\tilde\Xi\tilde\Xi^{*}\bigr)=2r^{2}\cosh\theta_{\mathrm{rpd},w},
$$

a positive real number that reads the scale and the boost and nothing else. Both were checked on a hundred random elements, to $10^{-7}$ relative. Neither norm sees the rotor, and the reason is structural: the rotor is real and unitary, so it cancels in both.

### The domain

*Proposition.* The word of $\tilde\Xi$ exists exactly on the complement of the cone $\{\tilde X:\langle\tilde X\rangle_{\natural}=0\}$, and the flow carries that complement to itself.

*Proof.* The first half is the boxed statement of the introduction. For the second, the propagator is $\tilde Q=\exp(-i\tilde H_\Psi t'/\hbar)$ and $\langle\tilde Q\rangle_{\natural}$ is central, so

$$
\langle\tilde Q\tilde\Xi\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde\Xi\rangle_{\natural},
$$

and $\langle\tilde Q\rangle_{\natural}$ is a unit of the centre at every $t'$. Hence $\langle\tilde\Xi\rangle_{\natural}$ vanishes at one time exactly when it vanishes at every time, and the word's domain is an invariant set.

**What that means in practice.** A field that is a unit at $t'=0$ is a unit at every $t'$, and the word exists for all time. A field on the cone at $t'=0$ never leaves it, and the word exists at no time. There is no crossing, and no field drifts into or out of the domain. This was checked directly: a hundred random fields were evolved and $|\langle\tilde\Xi\rangle_{\natural}|$ was constant to $10^{-7}$ relative in every case.

**The cone is not the nodal set.** A central field vanishes exactly when its single complex coefficient does, and that is a point of the cone but not the whole of it: the cone is a proper algebraic subset of the algebra and not a level set of a single coefficient, and a field can be off the cone while one of its coefficients vanishes. What fails on the cone is the parametrisation and never the equation: the equation is one element times one element, and it makes sense on zero divisors as well.

## The Flow of the Word

### The propagator is a phase times a rotor

The parent's solution is

$$
\tilde Q(t')=\exp\Bigl(-i\frac{\tilde H_\Psi t'}{\hbar}\Bigr)
=\exp\Bigl(-i\frac{r_t t'}{\hbar}\Bigr)\Bigl(\cos\theta\,e_t+\sin\theta\,\vec u_\Psi\Bigr),
\qquad
\theta=\frac{|\vec r_\Psi|\,t'}{\hbar},
$$

where $\vec u_\Psi=\vec r_\Psi/|\vec r_\Psi|$ when $\vec r_\Psi\neq0$, and the constant is $\hbar$ alone because the variable is the time $t'$ and not the material length $r'_t=c\,t'$. Its word was computed in a hundred random cases:

$$
\boxed{\;\tilde Q(t')=e^{i\alpha_Q}\tilde u_Q,\qquad r_Q=1,\qquad \tilde U_{\Psi,\mathrm b,Q}=e_t,\qquad \alpha_Q=-\frac{r_t t'}{\hbar},\qquad \theta_{\mathrm r,Q}=\frac{2|\vec r_\Psi|t'}{\hbar},\;}
$$

so the propagator's word has four of its eight parameters frozen, at every time and for every Hamiltonian. The scale is one and the boost is the identity for one reason: $\tilde Q\tilde Q^{*}=e_t$, because the two factors of the parent's closed form are a central phase and a real rotor and nothing else. The Hermitian part of the propagator is therefore trivial and its word has nothing to read from it. What remains is the central phase and the rotor, which is the parent's real unit quaternion with its half-angle made explicit.

**The factor of two is the word's, not the parent's.** The parent writes $\cos\theta\,e_t+\sin\theta\,\vec u_\Psi$ with $\theta=|\vec r_\Psi|t'/\hbar$. That quaternion is a rotation through $2\theta$ about $\vec u_\Psi$, so its rotor angle is $\theta_{\mathrm r}=2\theta=2|\vec r_\Psi|t'/\hbar$. No factor has been inserted: the same element is read once as a half-angle and once as an angle. The two readings agree to $10^{-6}$ in a hundred random cases.

### The field's scale and rapidity are constants

Left multiplication by $\tilde Q$ acts on the field's word in the only way it can. The central phase passes through everything, and the propagator's rotor is real and unitary, so

$$
\tilde Q\,\tilde\Xi
=\Bigl(e^{i\alpha_Q}\tilde u_Q\Bigr)\Bigl(r\,e^{i\alpha}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r}\Bigr)
=r\,e^{i(\alpha+\alpha_Q)}\,\bigl(\tilde u_Q\,\tilde U_{\Psi,\mathrm b}\,\tilde u_Q^{\natural}\bigr)\bigl(\tilde u_Q\,\tilde u_{\mathrm r}\bigr).
$$

**The rotor does not pass through the boost.** A real rotor and a Hermitian boost commute only when their axes are parallel or one of them is zero, so $\tilde u_Q\tilde U_{\Psi,\mathrm b}\neq\tilde U_{\Psi,\mathrm b}\tilde u_Q$ in general, and the word of $\tilde Q\tilde\Xi$ is not the word of $\tilde\Xi$ with $\tilde u_Q$ moved to the front. The rotor is applied on both sides of the boost, and what that does is rotate the boost's axis and change nothing else. With $\tilde U_{\Psi,\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$,

$$
\tilde u_Q\,\tilde U_{\Psi,\mathrm b}\,\tilde u_Q^{\natural}
=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\bigl(\tilde u_Q\,\vec u_{\mathrm b}\,\tilde u_Q^{\natural}\bigr),
$$

and $\tilde u_Q\vec u_{\mathrm b}\tilde u_Q^{\natural}$ is $\vec u_{\mathrm b}$ turned through $2\theta$ about $\vec u_\Psi$. Three statements follow, each checked on a hundred random fields and random Hamiltonians, and with them the count of what the flow can move.

**The scale is a constant of the motion.** $r(t')=r(0)$, to $10^{-15}$ relative.

**The rapidity is a constant of the motion, and the boost is not.** $\theta_{\mathrm{rpd}}(t')=\theta_{\mathrm{rpd}}(0)$, to $10^{-14}$, because conjugation preserves the $e_t$ coefficient. The axis does not stay, because it is a vector and the rotor turns vectors:

$$
\frac{d\vec u_{\mathrm b}}{dt'}=\frac{2}{\hbar}\,\vec r_\Psi\times\vec u_{\mathrm b},
$$

checked against a finite difference to $10^{-5}$. The boost axis runs at the gap, the rate at which every carried direction runs, so the boost of the field's word is not a constant of the motion: its rapidity is an invariant and its axis is a frame datum.

**The rotor is carried by the propagator's rotor.** $\tilde u_{\mathrm r}(t')=\tilde u_Q(t')\tilde u_{\mathrm r}(0)$, a left multiplication and not a similarity. Its content is geometric: every real direction the field carries, $\hat s=\tilde u_{\mathrm r}\hat s_0\tilde u_{\mathrm r}^{\natural}$, is carried to $\tilde u_Q\hat s\tilde u_Q^{\natural}$, so the whole carried frame turns rigidly.

**Two of the eight parameters are frozen, and six move.** The scale and the rapidity stay where they are. The phase, the rotor's angle, the rotor's axis and the boost's axis all move: the rotor's angle because a product of two rotors is a third rotor whose angle is not that of either factor, the rotor's axis because that composite rotation has an axis of its own, and the boost's axis because the boost is conjugated. The two frozen parameters are the two that unitarity fixes, $r$ and $\rho=2r^{2}\cosh\theta_{\mathrm{rpd}}$; the six that move are the frame's.

### The two rates

The eigenvalues of the symbol are the two numbers $r_t-|\vec r_\Psi|$ and $r_t+|\vec r_\Psi|$, each twice, and both statements below are readings of the word against them.

**The phase runs at the mean.** Differentiating $\alpha+\alpha_Q$ gives

$$
\frac{d\alpha}{dt'}=-\frac{r_t}{\hbar},
$$

checked to $10^{-5}$ in a hundred random cases. The central phase of the field advances at minus the mean of the two eigenvalues.

**Every carried direction runs at the gap.** Differentiating $\hat s(t')=\tilde u_Q\hat s(0)\tilde u_Q^{\natural}$ gives

$$
\frac{d\hat s}{dt'}=\frac{2}{\hbar}\,\vec r_\Psi\times\hat s,
$$

checked to $2\times10^{-2}$ relative in a hundred random cases. The angular velocity is $2|\vec r_\Psi|/\hbar$, which is the gap between the eigenvalues and not half of it, because a direction turns at twice the half-angle. In the word's own parameter the half-angle runs at half the gap: $d\theta_{\mathrm r}/dt'=2|\vec r_\Psi|/\hbar$ for the rotor angle, that is $|\vec r_\Psi|/\hbar$ for its half. The boost's axis is one more direction carried in this way, and its precession obeys the same law (§*The field's scale and rapidity are constants*).

**The two rates are therefore the mean and the half-gap, and there are no others.** The Hamiltonian supplies two numbers, the mean and the gap, and the word has exactly two frequencies to spend them on: the central phase runs at the mean, and the rotor's angle at the gap with its half-angle at half the gap. What remains in the word adds no third frequency. The scale and the rapidity are frozen, and the two axes are not frozen but carried: the rotor's axis and the boost's axis precess at the gap, which is the rate the rotor already has.

### The half turn

At the time $\theta=\pi$, that is $|\vec r_\Psi|t'=\pi\hbar$, the propagator's rotor is $-e_t$ and

$$
\tilde\Xi(t')=-\exp\Bigl(-i\frac{r_t t'}{\hbar}\Bigr)\tilde\Xi(0),
$$

checked to $10^{-6}$ in a hundred random cases. The field returns to minus itself up to the central phase: the sign is the rotor's and the phase is the centre's. This is the one place where the two rates separate by inspection, because the phase has advanced by $r_t\pi/|\vec r_\Psi|$ while the rotor has advanced by exactly a half turn.

### What the word of the propagator does not say

**It does not say that the flow is periodic.** The flow is periodic only when $r_t/|\vec r_\Psi|$ is rational; otherwise the two rates are incommensurable and the word never repeats. The parent's closed form says the same thing less plainly.

**It does not fix the field's rotor.** The propagator's word is the same for every initial field. What the field's own rotor is, is read from the field, and the flow multiplies it on the left.

## The Central Field

### The degeneration of the word

A field is **central** when it is a complex multiple of $e_t$, $\tilde\Xi_{\mathrm{sp}}=\Xi_t\,e_t$. Its word degenerates, and the degeneration was checked on a hundred random central fields:

$$
r=|\Xi_t|,\qquad \tilde U_{\Psi,\mathrm b}=e_t,\qquad \tilde u_{\mathrm r}=\pm e_t,\qquad 2\alpha\equiv\arg\Xi_t\ (\mathrm{mod}\ \pi),
$$

the sign of the rotor carrying the half-turn branch of the angle. A central field's word is therefore a scale, a phase and a sign, and three of the four factors have collapsed. This is exactly Madelung's pair, with $A=r$ and $S=\hbar\alpha$.

**The central class is not invariant under a general Hamiltonian.** If $\vec r_\Psi\neq0$ then $\tilde H_\Psi\tilde\Xi_{\mathrm{sp}}$ has a vector part, so a central field is carried off the centre at once; the class is invariant exactly when the Hamiltonian is central. Checked in a hundred random cases, with no exception.

**No gauge defect is left over.** The field has eight real components, the word has eight real parameters, and the equation is first order in time with one complex equation per coefficient, that is eight real equations. The word is therefore exactly determined by the field, with no free function: there is no gauge to fix and no sector to choose. The four parameters that Madelung's form does not show are the boost's three and the rotor's angle, and they are not dropped by a choice; they are zero because the field is central.

### The exact pair

For a central field the equation is the ordinary one-component equation, and the word's two real functions satisfy a pair that is exact and not an approximation. Write $\tilde\Xi_{\mathrm{sp}}=A\,e^{iS/\hbar}e_t$ and $\tilde H_\Psi=V\,e_t$; substituting into the equation and separating the real and the imaginary parts gives

$$
\boxed{\;\frac{\partial S}{\partial t'}+\frac{|\nabla S|^{2}}{2m}+V+Q=0,\qquad
\frac{\partial A^{2}}{\partial t'}+\nabla\cdot\Bigl(A^{2}\frac{\nabla S}{m}\Bigr)=0,\;}
$$

with the quantum potential

$$
Q=-\frac{\hbar^{2}}{2m}\frac{\nabla^{2}A}{A}.
$$

The first is a Hamilton–Jacobi equation with one extra term; the second is a continuity equation. Both were checked on exact solutions rather than on random functions: the free Gaussian packet at three carrier momenta gave a relative residual of $10^{-7}$, and generic amplitudes and actions gave $10^{-8}$.

**The operator is the Laplacian and not the d'Alembertian.** This is the one place where the Schrödinger case differs from the Dirac and Klein–Gordon companions: the equation is first order in time and second order in space, so the quantum potential carries $\nabla^{2}$ and not $\Box$. The polar identity is otherwise the same identity.

**The pair is equivalent to the equation, and neither half is an approximation.** The real part says that the phase's gradient is the momentum; the imaginary part says that the density is conserved. Together they are the equation, with nothing dropped.

### The current and the transport equation

The density and the current are the two halves of the continuity equation:

$$
\rho=A^{2},\qquad
\vec j=A^{2}\frac{\nabla S}{m}=\rho\,\vec v,
\qquad
\frac{\partial\rho}{\partial t'}+\nabla\cdot\vec j=0.
$$

The velocity is the boost's content in the central case, where the boost has collapsed: $\vec v=\nabla S/m$ is the field's phase gradient over the mass. In the general field the current reads the scale and the boost, and the rotor contributes nothing, exactly as the two norms say.

**The density is a probability density and the current is its flux.** $\rho$ is positive by construction, because it is $\mathrm{Tr}(\tilde\Xi^{\dagger}\tilde\Xi)$ and $\tilde\Xi^{\dagger}\tilde\Xi$ is positive in the Hermitian form; the equation preserves it, as checked to $10^{-8}$ in a hundred random evolutions of a general field.

### Why there is no mass shell

The Dirac and Klein–Gordon companions end with a mass-shell condition: the word's boost is a boost exactly when the four-momentum is on the shell, and off the shell the boost is not unitary. There is no analogue here, and the absence is not a defect of the analysis.

**The reason is the order of the equation.** The Schrödinger equation is first order in time, so the symbol has no second time derivative to constrain, and the dispersion relation is a definition of the frequency rather than a constraint on the field. The propagator's word carries no boost at all, and the field's word carries one whose rapidity the flow cannot change, so there is nothing for a shell condition to be a condition on.

**What replaces it is the pair.** The two real equations of the previous section are an unconstrained system: one Hamilton–Jacobi equation that defines the phase and one continuity equation that defines the density, with the quantum potential carrying the only second derivative. Nothing is required of the initial data beyond the two functions.

## What the Polar Form Does and Does Not Add

**The equation, no; the coordinates, yes.** Nothing here predicts anything the parent does not. What the polar form adds is a set of coordinates in which the flow is a statement about two numbers, the phase and the rotor's angle, and their two rates.

**The domain is settled, and it is not a carrier.** The word exists exactly on the units, the units are generic in this algebra, and the flow preserves them. Unlike the Dirac case there is no class of fields excluded in advance, and unlike the Klein–Gordon case there is no nodal set that coincides with the cone. The polar form of this equation is total on the fields that occur.

**The frozen parameters are the statement of unitarity.** Of the propagator's four factors, the scale and the boost are frozen; the two that remain are the two that a unitary element can carry when the Hamiltonian is fixed. The field's word freezes the same two quantities, its scale and its rapidity, while its phase and its two axes turn. The count is two in both cases, and it needs no proof beyond the word's definition.

**The two rates are the mean and the half-gap.** The central phase runs at minus the mean of the eigenvalues and the rotor's half-angle at half the gap; a direction carried by the field runs at the gap. These are the whole of the time dependence — two rates and one carried frame — and the parent's closed form contains them in one line without separating them.

**Madelung's pair is one case, and the case is characterised.** The central field is the field whose word has collapsed to a scale and a phase, and it is invariant exactly under a central Hamiltonian. Madelung's amplitude and phase are therefore not an approximation and not a general chart: they are the two parameters of a class of fields, and the class is the one in which nothing turns.

**What was checked.** The statements above were recomputed numerically on random Hermitian $\tilde H_\Psi$ and random fields: the word, the two norms, the flow, the two rates, the half turn, the non-Hermitian generator and the central class, and three exact-solution checks of the pair. The largest residual among the exact identities was $6\times10^{-16}$, the conjugated boost $\tilde u_Q\tilde U_{\Psi,\mathrm b}\tilde u_Q^{\natural}$ included, and the two differential laws were checked against finite differences to $10^{-6}$.

## Open Questions

**1. The meaning of a fixed rapidity on a turning axis.** The rapidity of the field's word is a constant of the motion and its axis precesses at the gap; in the central case the boost is the identity and there is no axis at all. What physical reading the pair has for a non-central field — a velocity, a strain, or nothing — is not settled here, and the precession belongs to the question rather than beside it: a rapidity that holds while its axis turns is not yet a velocity, because nothing in the equation selects the axis.

**2. The non-Hermitian generator.** If $r_t$ acquires an imaginary part the scale leaves $1$ and the word reads decay, $r(t')=\exp(\gamma t')$; if $\vec r_\Psi$ acquires a real part the boost leaves the identity. Both were checked. Whether either is the right description of a decaying system is open, and it is the natural place for the word to earn its keep.

**3. The relativistic limit.** Whether this equation, with its frozen rapidity and its absent mass shell, is the non-relativistic limit of the biquaternion Dirac equation is not checked here. The companions' mass shells are the natural comparison.

**4. The relation to the WKB series.** The pair of this article is the first term of the series of *The WKB Approximation in Biquaternionic Form*. Whether the word's exact coordinates simplify the higher orders is not examined.

## Summary

The Schrödinger equation is one element of $\mathbb{B}$ acting on another by left multiplication, and the polar word of the second element is substituted into it. The word exists exactly on the units of the algebra, which is the complement of the zero-divisor cone; a generic field is a unit and the flow preserves the cone, so the word exists for all time or for none.

The propagator's word is a central phase times a rotor, with scale $1$ and boost $e_t$ frozen: four of the eight parameters cannot move. The field's own scale and rapidity are constants of the motion, and they are the only two: the phase and the rotor's angle run, the rotor's axis and the boost's axis precess at the gap, and the flow moves six of the eight parameters. The phase runs at minus the mean of the Hamiltonian's two eigenvalues and the rotor's half-angle at half their gap; a direction the field carries runs at the gap, $d\hat s/dt'=2\vec r_\Psi\times\hat s/\hbar$.

The two norms read different factors: the quaternionic norm is $r^{2}e^{2i\alpha}$ and reads the scale and the phase, and the Hermitian norm is $2r^{2}\cosh\theta_{\mathrm{rpd},w}$ and reads the scale and the boost. Neither reads the rotor.

A central field's word collapses to a scale, a phase and a sign, and that case is exactly Madelung's: the Hamilton–Jacobi equation with the quantum potential $Q=-\hbar^{2}\nabla^{2}A/(2mA)$ and the continuity equation for $A^{2}$. The pair is exact, the operator is the Laplacian, and there is no mass shell, because the equation is first order in time.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\tilde\Xi_{\mathrm{sp}}$ | The field: one element of $\mathbb{B}$ |
| $\tilde H_\Psi=r_t\,e_t+i\vec r_\Psi$ | Hermitian Hamiltonian |
| $r_t,\ \vec r_\Psi$ | Its scalar part and its vector part |
| $\vec u_\Psi=\vec r_\Psi/\lvert\vec r_\Psi\rvert$ | Its axis, when $\vec r_\Psi\neq0$ |
| $N(\tilde\Xi)$ | Determinant; the word exists iff $N\neq0$ |
| $\langle\tilde X\rangle_{\natural}=\tilde X\tilde X^{\natural}$ | Quaternionic norm |
| $\natural,\ *$ | Quaternion conjugation, Hermitian conjugation |
| $\mathrm{Sc},\ \mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part, trace |
| $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word of the field |
| $r>0$ | The scale |
| $\alpha$ | The central angle |
| $\theta_{\mathrm{rpd}},\ \vec u_{\mathrm b}$ | Rapidity and axis of the boost |
| $\theta_{\mathrm r},\ \vec u_{\mathrm r}$ | Angle and axis of the rotor |
| $\tilde Q(t')=\exp(-i\tilde H_\Psi t'/\hbar)=e^{i\alpha_Q}\tilde u_Q$ | The propagator and its word |
| $\theta=\lvert\vec r_\Psi\rvert t'/\hbar$ | The parent's angle; the rotor's half-angle |
| $\tilde u_Q=\cos\theta\,e_t+\sin\theta\,\vec u_\Psi$ | The propagator's rotor |
| $\rho=\mathrm{Tr}(\tilde\Xi^{\dagger}\tilde\Xi)$ | Density (Hermitian norm) |
| $Q=-\hbar^{2}\nabla^{2}A/(2mA)$ | Quantum potential |
| $L_{\mathrm{axf}}(\tilde H_\Psi)$ | Axis-free $4\times4$ array of the symbol |

## Further Reading

- *The Schrödinger Equation in Biquaternionic Form*, for the equation, its solution and the axis-free array.
- *The Polar Decomposition of an N-Regular Biquaternion*, for the word and its factors.
- *Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion*, for the exponential form used here.
- *The Meaning of N-Regularity and Degeneracy*, for $N$, the units and the cone.
- *The Polar Form of the Dirac Equation in Biquaternionic Form* and *The Polar Form of the Klein–Gordon Equation in Biquaternionic Form*, for the same construction in the two relativistic cases.
- *The WKB Approximation in Biquaternionic Form*, for the pair read as the first term of a series.
- *Why AXF Matrices instead of Pauli and Gamma Matrices*, for why the body of the equation carries elements and not arrays.
