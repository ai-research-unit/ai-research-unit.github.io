# __The Fourier Transform and the Schrödinger Equation in Biquaternionic Form__

## Introduction

**The parent writes the equation and solves it. The transform is the lens that is missing.** *The Schrödinger Equation in Biquaternionic Form* writes $i\hbar\,c\,\partial_{r'_t}\tilde\Xi=\tilde H_\Psi\tilde\Xi$ and gives the flow $\tilde Q(r'_t)=\exp(\tilde H_\Phi r'_t/(\hbar\,c))$. This article takes the transform of that equation and reads what the transform returns: one element of $\mathbb{B}$ in place of one differential operator.

**The replacement is exact and it costs nothing.** Differentiation in $t'$ becomes multiplication by $-i\omega$, so the operator $i\hbar\,\partial_{t'}-\tilde H_\Psi$ becomes the element $\hbar\omega\,e_t-\tilde H_\Psi$. That element is the symbol. Every statement below is a statement about it, and none of them is a new prediction: the symbol is the parent's equation read at one frequency.

**The first finding is that the symbol is not a number.** In the scalar theory the symbol is a scalar function of $\omega$ and $\vec k$. Here it is an element of $\mathbb{B}$ that acts by left multiplication on a four-dimensional complex space, and its determinant is a perfect square. **The square is the carrier's dimension speaking**, and it is the first structural difference from the scalar case.

**The second finding is that centrality is the statement that the zero set is real.** Left multiplication by $\tilde H_\Psi$ is a Hermitian operator exactly when $\tilde H_\Psi$ is Hermitian, and a Hermitian operator has real eigenvalues. That is one line, and it is the whole content of the parent's uniqueness theorem read in momentum space. The parent proves the uniqueness of $i$ by a commutant argument in position space; here the same fact appears as a reality statement about two points of the real line.

**The third finding is what a first-order equation cannot have.** The Klein–Gordon and Dirac symbols are even in $\omega$; the Schrödinger symbol is even about $h_t$ and not about zero. A solution at frequency $\omega$ has a partner at $-\omega$ in the second-order theories and a partner at $2h_t/\hbar-\omega$ here. **That asymmetry is the absence of the antiparticle, read on the zero set**, and it follows from the order of the equation and not from the algebra.

**The other three readings are companions.** *The Fourier Transform and the Schrödinger Equation in Biquaternionic Polar Variables* reads the same symbol in the word. *The Fourier Transform, the Variational Principle and the Schrödinger Equation in Biquaternionic Form* asks what the action's quadratic form becomes at fixed frequency. The coupled pair repeats both questions with a connection. This article is the free element-form case, and it cites its parents rather than repeating them.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient and the symbol rule those of *Operator and Calculus Conventions*, the two forms those of *Norm and Pairing Conventions*, the units and the material time those of *Physics Units and Common Elements Conventions*, and the sector bookkeeping those of *Mirror Biquaternions and the Phy–Psy Switch*.

**The bookkeeping is quoted once.** With $t'$ the time and $r'_t=c\,t'$ the material time, a positive-frequency plane wave is $\tilde\Xi=\tilde\Xi_0\exp(-i\omega t'+i\vec k_\Phi\cdot\vec r)$, so

$$
\partial_{t'}\longmapsto-i\omega,
\qquad
\partial_\eta\longmapsto ik_\eta,
\qquad
i\hbar\,\partial_{t'}\longmapsto\hbar\omega,
\qquad
r'_t\longmapsto\hbar\omega/c\ \text{as a wave number}.
$$

**The constant setting is the licence.** The Hamiltonian is a constant element $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ with $h_t$ and $\vec h_\Psi$ real. A symbol exists only for constant coefficients. The operator setting replaces the symbol by a convolution, and §*Limits* states that boundary.

## The Symbol of the Transform

**The transform of the equation.** Write $\hat{\tilde\Xi}(\omega)=\int\mathrm{d}t'\,e^{i\omega t'}\tilde\Xi(t')$. The transform of $i\hbar\,\partial_{t'}\tilde\Xi=\tilde H_\Psi\tilde\Xi$ is

$$
\big(\hbar\omega\,e_t-\tilde H_\Psi\big)\hat{\tilde\Xi}(\omega)=0,
$$

because $i\hbar\times(-i\omega)=\hbar\omega$ and $\tilde H_\Psi$ is constant. **The operator has become an element.** The element is the symbol, and it depends on one real number.

**Multiplication is the operator.** Left multiplication $L_{\tilde H_\Psi}$ carries $\mathbb{B}$ to itself. In the coefficient basis it is the axis-free array $L_{\mathrm{axf}}(\tilde H_\Psi)$, whose trace is $4h_t$ and whose determinant is $\langle\tilde H_\Psi\rangle_\natural^{2}$, the square of the quaternionic norm. The symbol is therefore the array

$$
\sigma(\omega)=L_{\mathrm{axf}}\big(\hbar\omega\,e_t-\tilde H_\Psi\big)
=\hbar\omega\,I_4-L_{\mathrm{axf}}(\tilde H_\Psi).
$$

**The determinant is the object whose zeros are the spectrum.** Its two invariants are the trace and the determinant, so

$$
\operatorname{tr}\sigma(\omega)=4\big(\hbar\omega-h_t\big),
\qquad
\det\sigma(\omega)=\Big(\big(\hbar\omega-h_t\big)^{2}-\lvert\vec h_\Psi\rvert^{2}\Big)^{2}.
$$

The square is exact. It has one reason: the array is $L_{\mathrm{axf}}(\tilde H_\Psi)\otimes I_2$ in a suitable ordering, so every eigenvalue of the two-dimensional factor occurs twice.

**The eigenvalues are two real numbers, each twice.** The array $L_{\mathrm{axf}}(\tilde H_\Psi)$ has eigenvalues $h_t+\lvert\vec h_\Psi\rvert$ and $h_t-\lvert\vec h_\Psi\rvert$, each with multiplicity two. Over one hundred draws of $(h_t,\vec h_\Psi)$ uniform in $[-1,1]^{4}$ the largest imaginary part of an eigenvalue was $3.1\times10^{-16}$, and the sorted list agreed with the closed form to $1.8\times10^{-15}$. **The zero set is the pair, taken twice, and nothing else.**

**The frequency-space propagator is the inverse symbol.** The parent's flow $\tilde Q(t')$ has the transform $R(\omega)=\sigma(\omega)^{-1}$ read as left multiplication, so the two poles of $R$ are the two eigenvalues and the residues are the two spectral projectors. **In frequency space the propagator is one rational element**, and the pole structure is the whole of its content.

## The Symbol Is an Element and Not a Number

**The scalar symbol is scalar because the scalar equation is one equation.** Four complex coefficients obey four copies of the same equation with the same scalar symbol, so one function of $\omega$ describes all of them. Here the symbol multiplies on the left, so it acts on the four coefficients as one array, and the array is not diagonal in the coefficient basis.

**Diagonalising the array is not an operation of the algebra.** The array is Hermitian and can be diagonalised by a unitary change of basis. That change of basis is a complex-linear map mixing $e_t$ with $\vec e_\mu$, and it is not multiplication by an element. **The diagonal form is available for calculation and unavailable for interpretation**, which is why the article keeps the element and reads its two invariants instead.

**Two invariants, and they are the whole spectrum.** A change of basis preserves the trace and the determinant, so those are the canonical scalars of the symbol. The trace fixes the mean $(\hbar\omega-h_t)$ and the determinant fixes the gap $\lvert\vec h_\Psi\rvert$. **The symbol's spectrum is a mean and a gap**, and every display below is a statement about those two numbers.

**The position-space reading is the same statement.** The parent's solution is a central phase times a real rotor: the phase runs at the mean and the rotor at the gap. The frequency-space symbol has the same two parameters, and the coincidence is not a coincidence: a symbol with two parameters produces a flow with two rates.

## Centrality Is What Makes the Zero Set Real

**The statement.** $L_{\tilde H}$ is self-adjoint for the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$ exactly when $\tilde H^{*}=\tilde H$. The proof is one line,
$$
\big\langle L_{\tilde H}X,Y\big\rangle=\mathrm{Sc}\big((\tilde H X)^{*}Y\big)=\mathrm{Sc}\big(X^{*}\tilde H^{*}Y\big)=\big\langle X,L_{\tilde H}Y\big\rangle,
$$
and the middle equality uses the hypothesis and nothing else.

**The consequence.** A self-adjoint array has real eigenvalues. So for every Hermitian Hamiltonian the two numbers are real and the zero set is two points of the real axis. **The reality of the spectrum is the centrality of the unit, stated as an operator fact.**

**The verification.** One hundred draws, the element written $h_t\,e_t+i\vec h_\Psi$ with real coefficients, the array built from the coefficient basis. Every eigenvalue was real to $3.1\times10^{-16}$, and every sorted list matched $\{h_t-\lvert\vec h_\Psi\rvert,h_t-\lvert\vec h_\Psi\rvert,h_t+\lvert\vec h_\Psi\rvert,h_t+\lvert\vec h_\Psi\rvert\}$ to $1.8\times10^{-15}$.

**The parent's theorem is the same theorem.** The parent shows that only $\pm i$ keeps the generator anti-Hermitian for every Hermitian $\tilde H_\Psi$, and that a quaternion root fails for Hamiltonians that do not commute with it. In frequency space the same failure is a loss of reality: the zeros of the determinant leave the real axis. **Both statements are statements about self-adjointness**, one about the generator and one about the symbol.

**What centrality does not do.** It does not make the symbol scalar. The vector part $\vec h_\Psi$ survives as the gap, so a Hermitian Hamiltonian with $\vec h_\Psi\neq0$ has two distinct frequencies. The parent's two writings and the polar companion's two rates are the two numbers of this section.

**A word about the wrong root.** The counterexample of the parent, $\tilde Z=\vec e_z$ with $\tilde H_\Psi=i\vec e_x$, is a symbol whose determinant is not real on the real axis. §*The Non-Central Roots and the Pencil* computes it and shows that the failure is generic and quantified.

## The Non-Central Roots and the Pencil

**The equation with a root.** Replace $i$ by $\tilde Z$ with $\tilde Z^{2}=-e_t$ and write the equation in the parent's form, $\hbar\,\tilde Z\,\partial_{t'}\tilde\Xi=\tilde H_\Psi\tilde\Xi$. The substitution sends $\hbar\tilde Z\partial_{t'}$ to $-i\hbar\omega\tilde Z$, so the symbol is

$$
\sigma_{\tilde Z}(\omega)=\hbar\omega\,\big(-i\tilde Z\big)-\tilde H_\Psi .
$$

The factor $-i\tilde Z$ is what the root becomes in frequency space, and it is Hermitian exactly when $\tilde Z$ is anti-Hermitian. Every root of $-e_t$ is anti-Hermitian, so the symbol is a **Hermitian pencil** for every root: two Hermitian arrays, one of them carrying the frequency.

**A Hermitian pencil with an indefinite mass term has complex zeros.** That is the general fact behind the counts below, and it is the frequency-space form of the parent's caveat. Self-adjointness of each term does not make the zeros real; definiteness would, and $\tilde E=-i\tilde Z$ is indefinite for every non-central root.

**The case $\tilde Z=\vec e_z$ is exactly solvable.** There $\tilde E=-i\vec e_z$ has the eigenvalues $\pm1$, and the determinant is

$$
\det\sigma_{\vec e_z}(\omega)=\Big(h_t^{2}-\big(\hbar\omega+h_z\big)^{2}-h_\perp^{2}\Big)^{2},
\qquad
h_\perp^{2}=h_x^{2}+h_y^{2},
$$

verified over one hundred draws to $1.4\times10^{-14}$. **The zeros are $\hbar\omega=-h_z\pm\sqrt{h_t^{2}-h_\perp^{2}}$**, and they are real exactly on the cone $h_t^{2}\ge h_x^{2}+h_y^{2}$. On that cone the closed form matched the computed roots to $2.0\times10^{-15}$, over the $32$ draws.

**The count.** Over one hundred draws: all four roots real in $32$ draws for $\vec e_z$, $30$ for $\vec e_x$ and $37$ for $(\vec e_x+\vec e_z)/\sqrt2$. For $\tilde Z=\vec e_z$ the cone condition held in exactly the same $32$ draws, which is the whole explanation of the number.

**So reality is a cone and not a theorem.** For a central unit the cone is everything, because the pencil is definite on the whole carrier. For a quaternion root the cone is a proper subset of the Hamiltonians, and the subset depends on the root's axis. **A unit that works on one cone is not a unit for the equation**, which is the parent's uniformity argument in its momentum-space form.

## The Zero Set Is Two Points

**A first-order equation has no dispersion surface.** The symbol depends on $\omega$ alone, because the constant setting carries no spatial derivative. Its zero set is therefore a subset of the real line, not a hypersurface in $(\omega,\vec k_\Phi)$.

**The contrast is with the second-order case.** The Klein–Gordon symbol is $k_t'^{2}-k_\Phi^{2}-k_m^{2}$ with $k_t'=\omega/c$, and its zero set is a two-sheeted hyperboloid in four variables. The Dirac symbol's determinant is a power of the same quadric. **Those equations have a mass shell; this one has two frequencies**, and the polar companion draws the same conclusion from the absence of a second time derivative.

**What replaces the shell is a definition.** The dispersion relation of a first-order equation defines the frequency rather than constraining the field. Given $\vec k_\Phi$, the equation returns $\omega$; nothing is required of the initial data beyond the field's value at one time.

**The dimension count says the same.** The symbol is one element times one number: four complex conditions on four complex unknowns. A shell condition would be a fifth condition; the equation has none to spare.

## The Frequency Symmetry Is Evenness About $h_t$

**What the determinant is even in.** $\det\sigma(\omega)$ is a quadratic in $(\hbar\omega-h_t)^{2}$, so it is even about $\omega=h_t/\hbar$ and not about zero. A change of the sign of the frequency is not a symmetry of the symbol unless $h_t=0$.

**The numbers.** With $h_t=0.4$, $\lvert\vec h_\Psi\rvert=0.616441$ and $\hbar=1$ the zeros are at $\omega=-0.2164$ and $\omega=1.0164$. At $\omega=1.2$ the elementary determinant is $0.2600$ and at $\omega=-1.2$ it is $2.1800$; the symbol's determinant, being its square, is $0.0676$ at the first and $4.7524$ at the second, a ratio of $70.3$. **The two frequencies are not images of one another**, and the asymmetry is the mass term's.

**The second-order equations are even.** The Klein–Gordon and Dirac determinants are functions of $p^{2}$, so their zero sets are invariant under $\omega\mapsto-\omega$. That invariance is what makes a negative-frequency mode a solution of the same equation with the same $|p|$, and it is the kinematic half of the antiparticle statement.

| Equation | Order in time | Symbol's $\omega$-dependence | Symmetry of the zero set | Partner of a mode at $\omega$ |
| --- | --- | --- | --- | --- |
| Schrödinger | first | affine | $\omega\mapsto 2h_t/\hbar-\omega$ | $2h_t/\hbar-\omega$ |
| Klein–Gordon | second | quadratic | $\omega\mapsto-\omega$ | $-\omega$ |
| Dirac | second | quadratic through $p^{2}$ | $\omega\mapsto-\omega$ | $-\omega$ |

**What the table is not.** It is not a statement that the negative-frequency solutions of the second-order equations are particles. It is a statement about the zero sets, and the interpretation of a negative-frequency mode belongs to the field theory and not to the transform.

**What the table explains.** The Schrödinger equation has no pair creation, and the reason is visible here in one line: the mirror image of a solution is another solution of the same equation, but the mirror is $\omega\mapsto2h_t/\hbar-\omega$ and it is not the complex conjugate of the frequency. **The equation has no charge-conjugation symmetry because it has no second time derivative to supply one.**

**The symmetry is exact and it is a statement about the symbol.** $\det\sigma(2h_t/\hbar-\omega)=\det\sigma(\omega)$ for every Hermitian $\tilde H_\Psi$, because the determinant is a function of $(\hbar\omega-h_t)^{2}$ alone, and the statement survives the coupling, where the shift of $h_t$ is the potential's, as the coupled companion records.

**A degenerate case.** When $h_t=0$ the symmetry is $\omega\mapsto-\omega$, and the free equation with a purely vector Hamiltonian has a symmetric zero set. That is the closest the first-order equation comes to the second-order symmetry, and it is a property of one Hamiltonian and not of the equation.

## The Count of Poles

**The resolvent's poles, not the determinant's multiplicity.** The determinant's zero is double because the carrier is four-dimensional and each eigenvalue is doubly degenerate. The resolvent $\sigma^{-1}$ has simple poles, and the count of distinct poles is the count of distinct eigenvalues.

| Hamiltonian | Distinct zeros | Multiplicity in $\det\sigma$ | Rank of $\sigma$ at a zero | Rank of $\sigma$ off the zeros |
| --- | --- | --- | --- | --- |
| scalar, $\vec h_\Psi=0$ | $1$ | $4$ | $0$ | $4$ |
| general Hermitian | $2$ | $2$ each | $2$ | $4$ |

**The ranks are computed and they are exact.** For $\vec h_\Psi=0$ the symbol at $\omega=h_t/\hbar$ is the zero array, so its rank is $0$; the null space is the whole carrier. For $\vec h_\Psi\neq0$ the symbol at a zero has rank $2$, and the null space is the eigenspace of the other eigenvalue. Both were checked numerically on the example above.

**The off-shell rank is four.** The symbol is invertible at every frequency that is not an eigenvalue, which is the statement that the free propagator exists. **One is the degenerate count and two is the generic count**, and the second-order equations give two surfaces rather than two points.

## The Denial That Survives

**The transform does not leave the algebra, and it does not leave the sector.** Every transform here acts on a $\mathbb{B}$-valued function and returns one. No step carries a field out of $\mathbb{B}$, and no step pairs a material-sector element with an informational one. The sector statements of §*Conventions* are statements about one constant Hamiltonian.

**The symbol is not the spectrum of the operator setting.** A symbol exists where the coefficients are constant. With $\tilde H_\Psi=\hat H\,e_t$ and $\hat H=-\hbar^{2}\Delta_\Phi/(2m)+V$, the frequency-space object is a convolution whose kernel is the transform of $V$, and there is no array to read. **The constant setting is a licence and not a convenience.**

**The article does not re-derive the solution.** The flow, its $*$-unitarity and the two rates are the parent's and the polar companion's. What is added here is the shape of the zero set and the rank of the symbol, and nothing else.

## Limits

**Constant coefficients are the boundary.** Every display above is a statement about a constant Hamiltonian. §*The Denial That Survives* states the reason, and the coupled companions show how far the boundary moves when a constant connection is added: not at all.

**The carrier is four-dimensional and the square is its signature.** The determinant's perfect square is not an accident of the example. It is the statement that the array is a tensor product, and it would be a different power on a carrier of another dimension.

**The reality theorem is a theorem about Hermitian elements.** It says nothing about a non-Hermitian coefficient. A complex $h_t$ or a complex $\vec h_\Psi$ makes the symbol non-self-adjoint, and the zeros move off the real axis for the same reason the non-central roots do.

## Open Questions

**The first question is the operator setting.** What replaces the two-point zero set when the Hamiltonian contains $\nabla$? The polar companion's answer is that the frequency becomes a function of position, a local frequency; whether that function has a zero set with a geometric meaning is not settled here.

**The second is the sign of the imaginary part.** For a non-central root the zeros are complex, and the sign of their imaginary part decides growth or decay. Which sign a given Hamiltonian produces, and whether the two signs are separated by the cone, is not computed here.

**The third is the relation to the spectral theorem.** The symbol's two eigenvalues are the spectrum of a self-adjoint array. The operator setting's spectrum is a set of real numbers with accumulation points, and the passage from one to the other is the spectral theorem for $L^{2}$ sections of a bundle, which this article does not construct.

**The fourth is the physical status of the second writing.** The symbol uses $i\hbar\partial_{t'}-\tilde H_\Psi$, and the parent's second writing divides by $i\hbar c$. The two give symbols that differ by the real factor $c$ in the frequency; that factor is a unit and not a structure, and no statement here depends on it.

## Summary

The transform of the free Schrödinger equation is one element, $\hbar\omega\,e_t-\tilde H_\Psi$, acting by left multiplication on a four-dimensional complex space. Its determinant is $\big((\hbar\omega-h_t)^{2}-\lvert\vec h_\Psi\rvert^{2}\big)^{2}$, so the zero set is two real points, each of multiplicity two, and the multiplicity is the carrier's dimension. Verified over one hundred draws to $3.1\times10^{-16}$ on the eigenvalues and to $1.4\times10^{-14}$ on the determinant.

The reality of the zero set is exactly the Hermiticity of $\tilde H_\Psi$ and hence the centrality of $i$. Replacing $i$ by a quaternion root turns the symbol into a Hermitian pencil with an indefinite mass term, whose zeros are real only on a cone: $32$ of one hundred draws for $\vec e_z$, $30$ for $\vec e_x$, $37$ for $(\vec e_x+\vec e_z)/\sqrt2$, and for $\vec e_z$ the cone $h_t^{2}\ge h_x^{2}+h_y^{2}$ accounts for the number exactly.

The symbol's zero set is two points and not a surface, because a first-order equation has no second time derivative to constrain. Its symmetry is evenness about $h_t$ and not about zero, and the numbers $0.2600$ and $2.1800$ at $\omega=\pm1.2$ measure the asymmetry. **That is the absence of the antiparticle read on the symbol**, and it is the structural difference from the Klein–Gordon and Dirac cases that the companion articles take up.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\sigma(\omega)=\hbar\omega\,e_t-\tilde H_\Psi$ | The free symbol; an element acting by left multiplication |
| $\sigma_{\tilde Z}(\omega)=\hbar\omega\,(-i\tilde Z)-\tilde H_\Psi$ | The symbol of the equation with a root $\tilde Z$; a Hermitian pencil |
| $\det\sigma=\big((\hbar\omega-h_t)^{2}-\lvert\vec h_\Psi\rvert^{2}\big)^{2}$ | The determinant; its zeros are the spectrum, twice |
| $h_t\pm\lvert\vec h_\Psi\rvert$ | The two eigenvalues of $L_{\tilde H_\Psi}$; the mean and the gap |
| $\operatorname{tr}\sigma=4(\hbar\omega-h_t)$ | The trace; fixes the mean and nothing else |
| $2h_t/\hbar-\omega$ | The mirror frequency; the first-order partner of a mode |
| $\det\sigma_{\vec e_z}=\big(h_t^{2}-(\hbar\omega+h_z)^{2}-h_\perp^{2}\big)^{2}$ | The pencil for $\tilde Z=\vec e_z$; real zeros on the cone $h_t^{2}\ge h_\perp^{2}$ |
| $\tilde E=-i\tilde Z$ | The root as it enters the symbol; Hermitian for every anti-Hermitian root |
| $R(\omega)=\sigma(\omega)^{-1}$ | The frequency-space propagator; its simple poles are the two eigenvalues |

## Further Reading

- *The Schrödinger Equation in Biquaternionic Form*, for the equation, its solution, and the uniqueness of the central unit this article reads in momentum space.
- *The Schrödinger Equation in Biquaternionic Polar Variables*, for the two rates, which are the mean and the gap of this article's symbol.
- *The Fourier Transform and the Schrödinger Equation in Biquaternionic Polar Variables*, for the same symbol read in the word.
- *The Fourier Transform, the Variational Principle and the Schrödinger Equation in Biquaternionic Form*, for the action's quadratic form at fixed frequency.
- *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form*, for the second-order comparison: the rank of a quadric and the two-sheeted shell.
- *Algebra and Element Conventions*, for the coefficient basis, the axis-free array, and the two norms.
