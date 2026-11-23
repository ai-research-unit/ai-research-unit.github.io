# __The Fourier Transform and the Dirac Equation in Biquaternionic Form__

## Introduction

The Dirac operator is mixed in position space and pure in momentum space, and the transform is the difference. *The Dirac Equation in Biquaternionic Form* writes the dynamics as the chiral pair $\tilde\nabla_\Phi\tilde\Xi_R=2\pi\nu_m\tilde\Xi_L$ and $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=2\pi\nu_m\tilde\Xi_R$. One term of the operator there is the anti-Hermitian gradient and the other is the Hermitian mass coefficient, so the two Hermiticity characters stand in the same equation with opposite signs of character. Nothing in position space separates them, because the operator there is differential and its character is a statement about its adjoint rather than about a multiplier.

Under the transform the separation is a multiplication by one central $i$. The symbol rule of *Derivatives, Fields and Transforms* sends $\partial/\partial R_{\imath}$ to $2\pi\rho\,\omega_{\imath}$ with $\rho=i$, so the gradient becomes $2\pi i\tilde\Upsilon_\Phi$ and its conjugate $2\pi i\tilde\Upsilon_\Phi^{\natural}$. Multiplication by the central $i$ carries an anti-Hermitian element to a Hermitian one. The momentum-space operator is therefore Hermitian-valued everywhere, and the mixed character of the position-space operator is gone.

Three statements organise the article. The light cone is exactly the locus of idempotent momenta, and the idempotent it produces is $\tfrac12(e_t-i\hat n\cdot\vec e)$ with $\hat n$ the momentum's direction; the two signs of $\hat n$ are the two massless ideals. The transform preserves the Hermitian form and breaks the quaternionic norm, so the indefinite quadratic structure survives on the symbol as a level set and not on fields as a norm. And the mechanism behind both is one coefficient: the sector change from $\mathbb{B}_\Phi$ to $\mathbb{B}_\Psi$ is the $i$ in the multiplier, never a change in the image of a function.

The denial is stated once, here. The transform acts on $\mathbb{B}$-valued functions and returns $\mathbb{B}$-valued functions. A $\mathbb{B}_\Phi$-valued field does not become $\mathbb{B}_\Psi$-valued. Every sector flip below is a statement about the coefficient of one multiplier, and none is a statement about a function.

Nothing here is a new prediction and nothing is a new solution. The equation, its solutions and the physics are the parent's. What the transform adds is where the light cone sits in the wave-number variables, and what the transform does to the two forms the algebra carries.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient and the d'Alembertian those of *Operator and Calculus Conventions*, the four products those of *Product and Form Conventions*, the two forms those of *Norm and Pairing Conventions*, the invertibles and the material time those of *Physics Units and Common Elements Conventions*. The transform is the one of *Derivatives, Fields and Transforms*, whose symbol rule is quoted once and not re-derived:

$$
\frac{\partial}{\partial R_{\imath}}\longmapsto 2\pi\rho\,\omega_{\imath} ,
\qquad
\rho\ \text{a root of }-1,\quad \rho=i\ \text{in the corpus}.
$$

On a plane wave the two identities used throughout are

$$
\tilde\nabla_\Phi e^{-i\theta_{\mathrm{pwp}}}=2\pi i\tilde\Upsilon_\Phi e^{-i\theta_{\mathrm{pwp}}},
\qquad
(\tilde\nabla_\Phi)^{\natural}e^{-i\theta_{\mathrm{pwp}}}=2\pi i\tilde\Upsilon_\Phi^{\natural}e^{-i\theta_{\mathrm{pwp}}},
\qquad
\theta_{\mathrm{pwp}}=\frac{p\cdot x}{h},
$$

with $\tilde\Upsilon_\Phi=\frac{\tilde P_\Phi}{h}=i\nu_t'e_t+\vec\nu_\Phi$ and $2\pi\nu_t'=\omega/c$. The four sector statements used below are $\tilde\Upsilon_\Phi\in\mathbb{B}_\Phi$ and anti-Hermitian, $2\pi i\tilde\Upsilon_\Phi\in\mathbb{B}_\Psi$ and Hermitian, $\nu_me_t\in\mathbb{B}_\Psi$ and Hermitian, and $\frac{2\pi iS}{h}\in\mathbb{B}_\Phi$ and anti-Hermitian. The transform's constant and the sign of its exponent depend on the convention, and no statement below depends on either.

## The Operator's Symbol

### The Mixed Operator in Position Space

The gradient's character and the mass's are opposite, and the operator of the pair holds both. The gradient is anti-Hermitian for the pairing, $(\tilde\nabla_\Phi)^{*}=-(\tilde\nabla_\Phi)^{\natural}$, so left multiplication by $\tilde\nabla_\Phi$ is anti-self-adjoint and multiplication by $(\tilde\nabla_\Phi)^{\natural}$ is self-adjoint. The mass coefficient $\nu_m$ is a real central number, hence Hermitian, and it multiplies the field without differentiating it.

So the position-space operator has no single Hermiticity character. A symbol is a multiplier, and a multiplier's character is decided by its sector. The position-space operator is not a multiplier at all: it is a differential operator, and its character is a statement about its adjoint. That is why the mixed character is invisible there. It is not hidden; it has no place to live.

### The Pure Symbol in Momentum Space

In momentum space the operator is a multiplier, and every entry of it is Hermitian.

$$
\mathcal{D}(\tilde\Upsilon_\Phi)=
\begin{pmatrix}
-2\pi\nu_m & 2\pi i\tilde\Upsilon_\Phi\\[2pt]
2\pi i\tilde\Upsilon_\Phi^{\natural} & -2\pi\nu_m
\end{pmatrix},
$$

acting on the column of the two parts. The diagonal entries are the real central number $-\nu_m$, Hermitian. The off-diagonal entries are $2\pi i\tilde\Upsilon_\Phi$ and its $\natural$-conjugate. The first is $-\nu_t'e_t+i\vec\nu_\Phi$: its temporal coefficient is real and its spatial ones are imaginary. The coefficient conjugation reverses the imaginary ones and the quaternion conjugation reverses the spatial sign, so the two together return every coefficient to itself, $(2\pi i\tilde\Upsilon_\Phi)^{*}=2\pi i\tilde\Upsilon_\Phi$, and the entry equals its own star. The second entry, $-\nu_t'e_t-i\vec\nu_\Phi$, is the same case with the signs of the spatial coefficients exchanged. The check is exact rather than numerical, and it was also run: over four random momenta with $2\pi\nu_m=0.7$, $\lvert(2\pi i\tilde\Upsilon_\Phi-\nu_m)^{*}-(2\pi i\tilde\Upsilon_\Phi-\nu_m)\rvert$ came out $0.0$ at every one.

That is what "pure $\mathbb{B}_\Psi$" means. It is not that the operator is a single element of the Hermitian sector; it is that each of its entries is. The Hermitian sector is a real subspace, not an algebra, so a matrix of its elements is the only object that could be called a pure symbol, and this one is.

### The One Central Factor

The sector change is one element, used in one place. The parent's variational companion records that the $i$ inside the material time is what makes the temporal kinetic term self-adjoint without disturbing the spatial ones. Here the same central $i$ appears as the root of the transform and multiplies the whole wave-number element. In position space it sits in the coordinate, $R_t=ir_t'$, and splits the four directions into one anti-Hermitian and three Hermitian. In momentum space it sits in front of the symbol and makes all four directions Hermitian at once. **One element, two appearances, and the transform is what moves it from the coordinate to the multiplier.**

This is the mechanism the denial requires. A reader who expects the transform to carry a material field into an informational one has the wrong object in view. The field's image is a $\mathbb{B}$-valued function either way, and its eight components at each wave number are the same eight components at each position, resummed. What changes sector is the multiplier's coefficient, and the coefficient that changes is the $i$.

## The Massless Shell as the Idempotent Variety

### The Identity

On the light cone the wave-number element squares to twice its own temporal part times itself.

$$
\tilde\Upsilon_\Phi^{2}-2i\nu_t'\,\tilde\Upsilon_\Phi
=\bigl(-\nu_t'^{2}e_t+2i\nu_t'\vec\nu_\Phi-\nu_{\Phi}^{2}e_t\bigr)-\bigl(-2\nu_t'^{2}e_t+2i\nu_t'\vec\nu_\Phi\bigr)
=\bigl(\nu_t'^{2}-\nu_{\Phi}^{2}\bigr)e_t .
$$

The right side is the interval: it vanishes exactly where the norm $\tilde\Upsilon_\Phi\tilde\Upsilon_\Phi^{\natural}=-\nu_t'^{2}+\nu_{\Phi}^{2}$ vanishes, which is the light cone. So the identity $\tilde\Upsilon_\Phi^{2}=2i\nu_t'\tilde\Upsilon_\Phi$ holds on the cone and only there.

### The Projector

Divide by the temporal part and the wave-number element becomes a projector. Put

$$
\tilde\Pi_{\mathrm{id}}=\frac{\tilde\Upsilon_\Phi}{2i2\pi\nu_t'}=\tfrac12\bigl(e_t-i\hat n\cdot\vec e\bigr),
\qquad
\hat n=\frac{2\pi\vec\nu_\Phi}{2\pi\nu_t'},
$$

where $\hat n$ is a real unit vector on the cone. The defect of idempotency is the interval, in closed form:

$$
\tilde\Pi_{\mathrm{id}}^{2}-\tilde\Pi_{\mathrm{id}}=-\frac{\nu_t'^{2}-\nu_{\Phi}^{2}}{4\nu_t'^{2}}\,e_t .
$$

The computation is one line from the identity above, and the check covered five random null momenta: $\lvert\tilde\Pi_{\mathrm{id}}^{2}-\tilde\Pi_{\mathrm{id}}\rvert$ came out at most $5.6\times10^{-17}$, $\lvert2\,\mathrm{Sc}\,\tilde\Pi_{\mathrm{id}}-1\rvert$ at most $1.1\times10^{-16}$, and the same defect formula held off the cone to $2.8\times10^{-17}$ at five further momenta. One off-cone instance, $2\pi\nu_t'=1$ and $2\pi\nu_{\Phi}=0.7$, gives a defect of $0.1275$.

**A defect that is a central multiple of $e_t$ is the sharpest form the statement can take.** Off the cone the object is not a projector by an amount that is exactly the interval over four times the frequency squared. On the cone it is a projector of trace one, hence of rank one: a single surviving direction, and no more.

### The Two Signs of the Direction

The other sign of $\hat n$ is the other projector, and the two are orthogonal.

$$
\tilde\Pi_{\mathrm{id},\pm}=\tfrac12\bigl(e_t\pm i\hat n\cdot\vec e\bigr),
\qquad
\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=0,
\qquad
\tilde\Pi_{\mathrm{id},++}\tilde\Pi_{\mathrm{id},-}=e_t ,
$$

with the product checked at $5.6\times10^{-17}$ over the same five momenta. The pair is complete: two rank-one projectors, orthogonal, summing to the identity. **The sign of the momentum's direction is the only discrete data the cone carries**, and this is the form in which the massless equation's two sides appear.

### The Generalisation of a Corpus Display

*Degenerate Solutions of the Biquaternionic Dirac Equation* writes a null four-vector of the material sector as $i\kappa e_t+\kappa\vec n=2i\kappa\,\tilde\Pi_{\mathrm{id}}(-\vec n)$, for a real unit $\vec n$ and a real $\kappa$, where $\tilde\Pi_{\mathrm{id}}(\pm\vec n)=\tfrac12(e_t\pm i\vec n)$ is that article's name for the two projectors written $\tilde\Pi_{\mathrm{id},\pm}$ here. That display is the case $\kappa=\nu_t'$ of the projector above. What the present section adds is the converse: the light cone is not merely a locus where such a display can be written, it is exactly the locus where the divided wave-number element is idempotent, and the defect off the cone is the interval.

### The Two Massless Ideals

The two members of the pair annihilate the two complementary ideals. With $\hat n$ the direction of $\vec\nu_\Phi$,

$$
\tilde\Upsilon_\Phi=2i\nu_t'\,\tilde\Pi_{\mathrm{id},-},
\qquad
\tilde\Upsilon_\Phi^{\natural}=2i\nu_t'\,\tilde\Pi_{\mathrm{id},+} ,
$$

so the massless member $2\pi i\tilde\Upsilon_\Phi\,w=0$ is $\tilde\Pi_{\mathrm{id},-w}=0$, whose solutions are $w=\tilde\Pi_{\mathrm{id},+}\,u$ for arbitrary $u$; and the conjugate member has the mirror statement. The check covered four null momenta: $\lvert 2\pi i\tilde\Upsilon_\Phi\,(\tilde\Pi_{\mathrm{id},+u})\rvert$ came out at most $1.2\times10^{-16}$ and $\lvert 2\pi i\tilde\Upsilon_\Phi^{\natural}(\tilde\Pi_{\mathrm{id},-u})\rvert$ at most $2.5\times10^{-16}$, while the control $\lvert 2\pi i\tilde\Upsilon_\Phi(\tilde\Pi_{\mathrm{id},-u})\rvert$ was $2.01$.

The two solution spaces are the two complementary minimal left ideals of the algebra, and the sign of the momentum's direction selects which member gets which. The parent's warning about values is not in play here: a value is a right ideal, and the kernel of a left multiplication by a projector is a left ideal. These are different objects, and the article states the ideal that the kernel actually is.

## What the Transform Preserves and What It Breaks

### The Hermitian Form Survives

The kernel is central, so the transform acts on each coefficient separately, and a unitary transform on coefficients preserves the modulus-squared sum. For two fields $f$ and $g$ the Hermitian pairing $\int\mathrm{Sc}(f^{*}g)$, read coefficientwise as $\sum_\alpha\int\bar c_{\alpha}g_{\alpha}$, is carried to itself. The check used 64 samples, two independent fields with generic complex coefficients, and a unitary discrete transform: the pairing differed by $2.8\times10^{-13}$ and the norm $\int\mathrm{Sc}(f^{*}f)$ by $4.6\times10^{-13}$, both at the level of the transform's own round-off.

This is Plancherel, and it is the reason the corpus's Hermitian form is the one the wave-number notation rests on. Every amplitude the corpus computes in momentum space is a Hermitian-pairing amplitude, and the transform would be useless without this exactness.

### The Quaternionic Norm Does Not

The other form is not preserved, and its failure is not a normalization. The scalar part of the quaternionic norm of a field is $\mathrm{Sc}(ff^{\natural})=\sum_\alpha c_\alpha^{2}$ — a holomorphic quadratic form in the complex coefficients, with no conjugate anywhere. A unitary transform on coefficients preserves $\sum\bar c_\alpha c_\alpha$ and not $\sum c_\alpha^{2}$, because it mixes $c$ with $\bar c$.

The numbers are unambiguous. On the same 64 samples the summed scalar part of the quaternionic norm went from $-16.861768-42.722374\,i$ in position space to $-15.112387-17.526486\,i$ in momentum space: the real part moved by a tenth and the imaginary part changed by more than a factor of two. For a field with real coefficients the failure is starkest, because the quaternionic norm is then real and the transform's value is not. One 64-sample real field gave $56.651597$ before the transform and $-6.686526$ after, and the exact identity behind the number is

$$
\sum_k\hat c_k^{2}=\sum_n c_nc_{-n},
$$

which held to $1.6\times10^{-13}$. **The transform of the norm is the reflected overlap of the field with itself**, not the norm, and the two agree only for a field symmetric under reflection.

### Why They Differ

One form is holomorphic and the other is not, and that is the whole of it. The Hermitian form pairs a coefficient with the conjugate of another. The quaternionic norm pairs a coefficient with itself. A unitary change of basis respects the first and cannot respect the second, because a complex-unitary matrix is orthogonal on the real and imaginary parts separately and quadratic in neither.

The consequence for the algebra is exact. The quaternionic norm is indefinite — it is negative on the centre — so it could not have been a norm on a space even if it had survived. What it can be is a quadratic form evaluated on a single element, and the single element it is evaluated on is the symbol.

## The Interval as a Level Set

On the symbol both forms are evaluable, and they disagree. For a wave-number element,

$$
\langle\tilde\Upsilon_\Phi\rangle_\natural=-\nu_t'^{2}+\nu_{\Phi}^{2},
\qquad
\mathrm{Sc}\bigl(\tilde\Upsilon_\Phi^{*}\tilde\Upsilon_\Phi\bigr)=\nu_t'^{2}+\nu_{\Phi}^{2}.
$$

The first is indefinite and its level sets are hyperboloids; the second is positive and its level sets are spheres. On the mode $2\pi\nu_{\Phi}=3$, $2\pi\nu_t'=5$ the first is $-16$ and the second is $34$; the first takes the value $-\nu_m^{2}$ at $2\pi\nu_m=4$, so that mode lies on the shell of a particle of wave-number mass $4$, and the second form knows nothing about it. Only the hyperboloid terminates on the mass shell. *Wave–Particle Duality and the Fourier Transform* states this comparison for the general equation; the Dirac case adds the value of the level and the structure at its degenerate point.

The Dirac addition is the value and the degeneration. The level is $-\nu_m^{2}$, so the shell the solutions live on is the level set of the symbol's own quaternionic norm at minus the mass squared. At $\nu_m=0$ the level is $0$, and the level set is the cone of the previous section, where the symbol divides into the two idempotents. **The mass shell of the Dirac equation is therefore a level set at nonzero mass and the idempotent variety at zero mass**, and the two descriptions are one description at two values of one number.

This is why the corpus says the interval is the symbol. A quadratic form that cannot survive as a norm on fields survives as a level set on the multiplier, and the transform is what makes the multiplier the only object it can be evaluated on.

## Limits

Constant coefficients. The symbol is a constant element of $\mathbb{B}$ only where the operator's coefficients are constant. The mass is constant, so the free Dirac equation transforms exactly, and every display above is exact. With a potential the symbol depends on the position, the transform of the equation is a convolution, and the algebraic reading stops. *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* and *The Coupled Dirac Equation in Biquaternionic Form* are where that case is treated, and nothing here anticipates them.

The transform's image is $\mathbb{B}$-valued, and the sector statements are about coefficients. This is the denial of the introduction, repeated where it is used: the projector $\tilde\Pi_{\mathrm{id}}$ is an element of $\mathbb{B}$ built from the symbol's coefficients, and it is not a statement that the field's values have moved to another sector.

The transform's existence. Plancherel holds for a root with $\rho^{*}=-\rho$, which the central imaginary satisfies; the constant and the sign of the exponent are convention, as *Derivatives, Fields and Transforms* records. No display above depends on either choice, because every one of them is an identity of elements.

## Open Questions

The article closes; it leaves no question of its own. Its findings are algebraic identities and exact checks, and none of them has an unresolved case.

Two adjacent questions belong to other articles. A symbol that depends on position is the coupled article's subject, and the measure-theoretic reading of a level set is the subject of *Wave–Particle Duality and the Weight of a Level Set*. Neither is claimed or attempted here.

## Summary

In position space the Dirac operator is mixed: the gradient is anti-Hermitian and the mass coefficient is Hermitian, and the two stand in one pair with opposite characters. Under the transform each derivative becomes multiplication by the central $i$ times the wave-number element, and multiplication by $i$ carries the anti-Hermitian symbol to a Hermitian one. The momentum-space operator is therefore Hermitian in every entry, and that is what a pure $\mathbb{B}_\Psi$ symbol means.

The light cone is exactly the locus where $\tilde\Upsilon_\Phi/(2i\nu_t')$ is idempotent. The defect of idempotency is $-\frac{\nu_t'^{2}-\nu_{\Phi}^{2}}{4\nu_t'^{2}}e_t$, a central multiple of the interval, and on the cone the projector is $\tfrac12(e_t-i\hat n\cdot\vec e)$ of trace one, with the other sign of $\hat n$ giving the orthogonal partner. The two members of the massless pair have the two complementary minimal left ideals for their solution spaces, and the sign of the momentum's direction selects which is which.

The transform preserves the Hermitian form, by Plancherel, and breaks the quaternionic norm, whose scalar part is a holomorphic quadratic form: the summed scalar part of the norm of a real 64-sample field went from $56.651597$ to $-6.686526$, with the exact identity $\sum_k\hat c_k^{2}=\sum_nc_nc_{-n}$ holding to $1.6\times10^{-13}$. So the indefinite quadratic structure lives on the symbol, where it is a level set: the Dirac shell is the level $-\nu_m^{2}$, and at $\nu_m=0$ that level set is the idempotent variety.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Upsilon_\Phi=i\nu_t'e_t+\vec\nu_\Phi$ | The wave-number element; anti-Hermitian, in $\mathbb{B}_\Phi$ |
| $2\pi i\tilde\Upsilon_\Phi$ | The symbol of the gradient; Hermitian, in $\mathbb{B}_\Psi$ |
| $\mathcal{D}(\tilde\Upsilon_\Phi)$ | The pair's symbol; every entry Hermitian |
| $\tilde\Upsilon_\Phi^{2}-2i\nu_t'\tilde\Upsilon_\Phi=(\nu_t'^{2}-\nu_{\Phi}^{2})e_t$ | The identity that holds on the light cone only |
| $\tilde\Pi_{\mathrm{id}}=\tilde\Upsilon_\Phi/(2i2\pi\nu_t')=\tfrac12(e_t-i\hat n\cdot\vec e)$ | The idempotent of a null momentum; rank one |
| $\tilde\Pi_{\mathrm{id}}^{2}-\tilde\Pi_{\mathrm{id}}=-\frac{\nu_t'^{2}-\nu_{\Phi}^{2}}{4\nu_t'^{2}}e_t$ | The defect off the cone; the interval |
| $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm i\hat n\cdot\vec e)$ | The two orthogonal projectors; $\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=0$ |
| $\tilde\Upsilon_\Phi=2i\nu_t'\tilde\Pi_{\mathrm{id},-}$, $\tilde\Upsilon_\Phi^{\natural}=2i\nu_t'\tilde\Pi_{\mathrm{id},+}$ | The two massless members |
| $\int\mathrm{Sc}(f^{*}g)$ | The Hermitian form; preserved by the transform |
| $\mathrm{Sc}(ff^{\natural})=\sum_\alpha c_\alpha^{2}$ | The quaternionic norm's scalar part; not preserved |
| $\sum_k\hat c_k^{2}=\sum_nc_nc_{-n}$ | What the transform makes of it; the reflected overlap |
| $\langle\tilde\Upsilon_\Phi\rangle_\natural=-\nu_t'^{2}+\nu_{\Phi}^{2}$ | The indefinite form on the symbol; level sets are shells |
| $\mathrm{Sc}(\tilde\Upsilon_\Phi^{*}\tilde\Upsilon_\Phi)=\nu_t'^{2}+\nu_{\Phi}^{2}$ | The positive form on the symbol; level sets are spheres |

## Further Reading

- *The Dirac Equation in Biquaternionic Form*, for the chiral pair, the gradient and the mass coefficient.
- *The Dirac Equation in Biquaternionic Polar Variables*, for the word and the phase gradient.
- *The Lagrangian and the Dirac Equation*, for the action, its self-adjointness and the sentence about the $i$ inside the material time.
- *Degenerate Solutions of the Biquaternionic Dirac Equation*, for the null four-vector as twice an idempotent.
- *Derivatives, Fields and Transforms*, for the transform, its kernel and its symbol rule.
- *Wave–Particle Duality and the Fourier Transform*, for the two forms on one element and the interval as a symbol.
- *Biquaternion Continuous Harmonic Analysis*, for Plancherel's condition on the root and the support on the cone.
- *Canonical Quantization of the Biquaternion Dirac Field*, for the plane-wave amplitudes the transform produces.
- M. Plancherel, "Contribution à l'étude de la représentation d'une fonction arbitraire par des intégrales définies," *Rendiconti del Circolo Matematico di Palermo* **30** (1910) 289–335, for the isometry of the transform.
- R. Penrose and W. Rindler, *Spinors and Space-Time I* (Cambridge, 1984), for the two ideals of a null momentum and the flag it carries.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the null-momentum projector written on the algebra's units.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the idempotents of the algebra and their ranks.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Heldermann, 2003), for the quaternionic Dirac operator in the wave-number variables.
