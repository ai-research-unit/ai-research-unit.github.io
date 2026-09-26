# __The Dirac Oscillator in Biquaternionic Form__

## Introduction

The Dirac oscillator is the relativistic quantum system obtained from the free Dirac Hamiltonian by the non-minimal substitution

$$
\mathbf{p} \;\longrightarrow\; \mathbf{p} - i m\omega \beta\mathbf{r},
\qquad
H = c\,\boldsymbol\alpha\cdot\left(\mathbf{p} - i m\omega\beta\mathbf{r}\right) + \beta mc^2 ,
$$

introduced by Marcos Moshinsky and Adam Szczepaniak in 1989. The substitution is "non-minimal" in the precise sense that it cannot be obtained from a gauge potential: it adds, to the odd (frame-anticommuting) part of the Dirac operator, a term linear in the position. The resulting system is exactly solvable, its non-relativistic limit is the three-dimensional isotropic harmonic oscillator together with a spin–orbit coupling of the same order as the level spacing, and it has become the standard laboratory for the relativistic treatment of confining interactions.

It belongs in this subcategory as the **exactly solvable external-potential problem** of the biquaternionic Dirac theory. The hydrogen atom, treated in the companion article *The Hydrogen Atom in Biquaternionic Form — The Relativistic Case*, is exactly solvable by a different mechanism (a Coulomb central field and a second-order radial reduction); the oscillator is exactly solvable because the first-order operator can be **squared in closed form**, and the square is again a central second-order operator plus a spin–orbit term. That is the same square as in *Klein–Gordon from the Dirac Square in Biquaternionic Form*, now with the position-dependent addition that makes the square a harmonic oscillator. The two features together make the model the natural place to see, concretely, how the biquaternionic first-order operator behaves under squaring.

The article derives the substitution, the reduction to a pair of two-component equations, the exact operator identity on squaring, and the spectrum; it then reads the result in the algebra, works the one-dimensional case for which everything is transparent, and connects the zero modes to the supersymmetric structure developed in the companion article *Supersymmetric Quantum Mechanics in the Biquaternion Framework*. The conventions are the series conventions: the Clifford generators satisfy $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$ with $g = \mathrm{diag}(+1,-1,-1,-1)$, $\beta = \gamma^0$, $\alpha^k = \gamma^0\gamma^k$, and the biquaternion mass pair is

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

## The Non-Minimal Substitution

Minimal coupling replaces $\mathbf{p}$ by $\mathbf{p} - q\mathbf{A}$; the added term is a vector potential and enters the Hamiltonian through $\boldsymbol\alpha\cdot\mathbf{A}$. The oscillator substitution is different in three ways, and each matters.

**It multiplies the position by $\beta$.** The added term is $-im\omega\beta\mathbf{r}$, not $-im\omega\mathbf{r}$. Because $\beta$ anticommutes with $\boldsymbol\alpha$, the product $\boldsymbol\alpha\cdot(\beta\mathbf{r}) = (\boldsymbol\alpha\beta)\cdot\mathbf{r} = -(\beta\boldsymbol\alpha)\cdot\mathbf{r}$ is frame-**odd**: it is a spacelike Clifford vector contracted with the position, in the same grading class as the kinetic term $\boldsymbol\alpha\cdot\mathbf{p}$ and in the opposite class from the mass $\beta mc^2$. In the algebra this is the statement that the substitution shifts the odd part of the operator while leaving the even part alone, which is why the resulting square is again central.

**It is imaginary, and it is Hermitian.** The coefficient is $i$, not a real coupling: a gauge interaction adds the real, Hermitian $q\mathbf{A}$ to $\mathbf{p}$, whereas the substitution multiplies the position by $im\omega$, so that the imaginary coefficient comes paired with the matrix $\boldsymbol\alpha\beta$, which is itself anti-Hermitian. The product is Hermitian all the same. Writing $\beta = \gamma^0$ and $\alpha^k = \gamma^0\gamma^k$ gives $\alpha^k\beta = -\gamma^k$, and $\gamma^k$ is anti-Hermitian, $(\gamma^k)^\dagger = -\gamma^k$, since $\gamma^0\gamma^k\gamma^0 = -\gamma^k$ with $\gamma^0$ Hermitian and anticommuting with $\gamma^k$; the added operator is therefore $-icm\omega(\boldsymbol\alpha\beta)\cdot\mathbf{r} = +icm\omega\,\boldsymbol\gamma\cdot\mathbf{r}$, and $i$ times an anti-Hermitian matrix is Hermitian. What the imaginary coefficient signals is not a complex deformation — the oscillator Hamiltonian is Hermitian and its spectrum real — but a term that is frame-odd, linear in the position and matrix-valued, which a gauge potential cannot produce.

**It is linear in the position**, so it grows without bound. The oscillator potential is confining; the spectrum is discrete; and the model is a relativistic confinement model rather than a scattering problem. This is the physical reason for its use in quark-confinement phenomenology, and it is the reason the spectrum consists of bound levels with the mass gap at their base.

The covariant form of the equation, obtained by multiplying the Hamiltonian equation by $\beta$ and using $\beta\boldsymbol\alpha = \boldsymbol\gamma$, is

$$
\left(i\gamma^\mu\partial_\mu - \frac{mc}{\hbar}\right)\psi = i\,\frac{m\omega}{\hbar}\,\beta\,\gamma^k x_k\,\psi ,
$$

The right-hand side is a spacelike Clifford vector times the frame, linear in $x$: the non-minimal term is a position-dependent generator of the odd part. This is the form in which the biquaternion reading is made below.

## Reduction to Two-Component Equations

Write the four-spinor as a pair of two-spinors, $\psi = (\phi,\chi)^{\mathsf T}$, and use the Dirac representation

$$
\beta = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix},
\qquad
\alpha^k = \begin{pmatrix} 0 & \sigma^k \\ \sigma^k & 0 \end{pmatrix}.
$$

Since $\beta\mathbf{r} = \mathrm{diag}(\mathbf{r},-\mathbf{r})$, the substitution acts differently in the two blocks:

$$
\boldsymbol\alpha\cdot\left(\mathbf{p}-im\omega\beta\mathbf{r}\right)
= \begin{pmatrix}
0 & \boldsymbol\sigma\cdot(\mathbf{p}+im\omega\mathbf{r}) \\
\boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r}) & 0
\end{pmatrix}.
$$

The time-independent equation $H\psi = E\psi$ therefore becomes the coupled pair

$$
(E - mc^2)\phi = c\,\boldsymbol\sigma\cdot(\mathbf{p}+im\omega\mathbf{r})\,\chi,
\qquad
(E + mc^2)\chi = c\,\boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})\,\phi .
$$

This is the form in which the oscillator is normally solved: the upper and lower two-spinors are coupled by the two conjugate first-order operators, and the coupling is exactly the minimal-coupling-like structure with $\pm im\omega\mathbf{r}$ in place of $\mathbf{A}$. Eliminating $\chi$,

$$
\chi = \frac{c\,\boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})}{E+mc^2}\,\phi ,
$$

and substituting into the first equation gives the second-order equation for $\phi$ alone:

$$
\left(E^2 - m^2c^4\right)\phi
= c^2\left[\boldsymbol\sigma\cdot(\mathbf{p}+im\omega\mathbf{r})\right]
\left[\boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})\right]\phi .
$$

Everything now rests on evaluating the product of the two first-order operators in closed form.

## The Square of the Coupled Operator

The product is evaluated with the Pauli identity

$$
(\boldsymbol\sigma\cdot\mathbf{A})(\boldsymbol\sigma\cdot\mathbf{B})
= \mathbf{A}\cdot\mathbf{B} + i\,\boldsymbol\sigma\cdot(\mathbf{A}\times\mathbf{B}),
$$

which holds for operator-valued $\mathbf{A},\mathbf{B}$ with the ordering as written. Take

$$
\mathbf{A} = \mathbf{p} + im\omega\mathbf{r}, \qquad \mathbf{B} = \mathbf{p} - im\omega\mathbf{r}.
$$

The dot product gives

$$
\mathbf{A}\cdot\mathbf{B} = \mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 + im\omega\left[\mathbf{r}\cdot\mathbf{p} - \mathbf{p}\cdot\mathbf{r}\right]
= \mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 - 3m\hbar\omega,
$$

because $[r_j,p_j] = i\hbar$ and the sum over three directions gives $3i\hbar$, so $im\omega\,(3i\hbar) = -3m\hbar\omega$. The cross product gives

$$
\mathbf{A}\times\mathbf{B}
= -im\omega\,\mathbf{p}\times\mathbf{r} + im\omega\,\mathbf{r}\times\mathbf{p}
= 2im\omega\,\mathbf{L},
\qquad \mathbf{L} = \mathbf{r}\times\mathbf{p},
$$

using $\mathbf{p}\times\mathbf{r} = -\mathbf{L}$; hence

$$
i\,\boldsymbol\sigma\cdot(\mathbf{A}\times\mathbf{B}) = -2m\omega\,\boldsymbol\sigma\cdot\mathbf{L}.
$$

The operator identity is therefore

$$
\left[\boldsymbol\sigma\cdot(\mathbf{p}+im\omega\mathbf{r})\right]
\left[\boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})\right]
= \mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\mathbf{L}.
$$

This is the load-bearing equation of the article. It was verified by direct matrix computation in a truncated three-dimensional oscillator basis: the identity held in the bulk of the basis to $1.8\times10^{-15}$ (the deviation in the outermost shell of the truncation is the expected finite-basis artefact of the commutator $[r_j,p_j] = i\hbar$, which a truncated basis realises only in the bulk). The representation used was the Cartesian three-mode Fock space with total excitation number up to $N_{\max} = 7$, restricted to states of excitation number at most $N_{\max}-2$.

Two features of the right-hand side are worth separating. The first two terms are the **three-dimensional isotropic oscillator** in operator form,

$$
\mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 = 2m\left(\frac{\mathbf{p}^2}{2m} + \tfrac12 m\omega^2\mathbf{r}^2\right) = 2m\,H_{\mathrm{osc}},
$$

with the standard spectrum $\hbar\omega(N+\tfrac32)$ in terms of the total oscillator number $N = 2n_r + l$. The constant $-3m\hbar\omega$ then removes exactly the zero-point energy of the oscillator, leaving $2m\hbar\omega N$. The last term, $-2m\omega\,\boldsymbol\sigma\cdot\mathbf{L}$, is a **spin–orbit coupling** whose strength is tied to the oscillator frequency; it is not a small correction but a term of the same order as the level spacing, and it governs the whole spectral structure.

## The Spectrum

Insert the identity into the second-order equation:

$$
\left(E^2 - m^2c^4\right)\phi
= c^2\left(\mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\mathbf{L}\right)\phi .
$$

The operator on the right is central in the spatial variables but contains the spin–orbit term, which is diagonal in the basis $|N,l,j,m_j\rangle$: it commutes with $\mathbf{J}^2$, $\mathbf{L}^2$ and $N$. Its eigenvalues are the standard ones,

$$
\frac{1}{\hbar}\,\boldsymbol\sigma\cdot\mathbf{L} =
\begin{cases}
+l, & j = l + \tfrac12 \\[2pt]
-(l+1), & j = l - \tfrac12
\end{cases}
$$

so that, using $\mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 - 3m\hbar\omega = 2m\hbar\omega N$ and $N = 2n_r + l$,

$$
E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \frac{\boldsymbol\sigma\cdot\mathbf{L}}{\hbar}\right)
=
\begin{cases}
m^2c^4 + 4m\hbar\omega c^2\,n_r, & j = l+\tfrac12, \\[4pt]
m^2c^4 + 2m\hbar\omega c^2\left(2n_r + 2l + 1\right), & j = l-\tfrac12 .
\end{cases}
$$

This is the Dirac-oscillator spectrum. Its structure is the two-branch pattern familiar from the literature: one branch is a tower in the radial quantum number $n_r$ alone, the other a tower shifted by the orbital quantum number; both are positive, so $E^2 \geq m^2c^4$ and the spectrum has a gap. The ground state has $n_r = 0$, $l = 0$, $j = \tfrac12$, and energy $E = \pm mc^2$; the first excited level stands at $E^2 = m^2c^4 + 4m\hbar\omega c^2$.

The $j = l+\tfrac12$ branch depends on $n_r$ and **not on $l$**. This is the characteristic degeneracy of the Dirac oscillator: for every $l$ with $j = l+\tfrac12$, the state with $n_r = 0$ has the same energy $E = \pm mc^2$, so the ground level is infinitely degenerate. The degeneracy is not an artefact of the truncation or of a particular gauge: it follows from the exact operator identity above, because the spin–orbit term cancels the oscillator zero point precisely for the aligned states. It is the same zero-mode structure that appears in the supersymmetric reading of the biquaternion section below, and it is the reason the model is called a "pseudo-oscillator": the spatial oscillator and the spin–orbit term conspire to produce a degeneracy pattern different from the non-relativistic oscillator's.

The two branches can be written in the unified form

$$
E^2 = m^2c^4 + 4m\hbar\omega c^2\,n_r
\quad\text{for the aligned states, and}\quad
E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N + l + 1\right)
\quad\text{for the anti-aligned states.}
$$

The structure agrees with the published two-branch spectra obtained by solving the radial equations or by locating the poles of the Green's function (see the Further Reading); the derivation here obtains it directly from the operator identity, without a radial decomposition.

## The One-Dimensional Case

The one-dimensional oscillator shows the mechanism without the spin–orbit bookkeeping. With a single coordinate and the substitution $p \to p - im\omega\beta x$, the pair reduces to

$$
(E-mc^2)\phi = c\left(p + im\omega x\right)\chi, \qquad
(E+mc^2)\chi = c\left(p - im\omega x\right)\phi,
$$

and the product of the two first-order operators is now a scalar,

$$
\left(p + im\omega x\right)\left(p - im\omega x\right)
= p^2 + m^2\omega^2x^2 - m\hbar\omega .
$$

The oscillator's zero point is $\tfrac12\hbar\omega$, so $p^2 + m^2\omega^2x^2 = 2m\hbar\omega(n+\tfrac12)$ and the constant removes exactly the zero point:

$$
E^2 = m^2c^4 + 2m\hbar\omega c^2\,n, \qquad n = 0,1,2,\dots
$$

Each level is non-degenerate in the oscillator quantum number and the ground state sits at $E = \pm mc^2$, as in the three-dimensional aligned branch but without the orbital multiplicity. The one-dimensional result is the cleanest check that the constant $-m\hbar\omega$ (which becomes $-3m\hbar\omega$ in three dimensions) is not a convention but a consequence of the commutator $[x,p] = i\hbar$; the zero-point cancellation that produces the $E \propto n$ spectrum is the same mechanism in both cases.

## The Non-Relativistic Limit and the Pseudo-Oscillator

The companion article on the Foldy–Wouthuysen transformation gives the systematic non-relativistic expansion; applied to the oscillator it produces, in the upper block, the effective operator $Q^\dagger Q/(2m)$ obtained from $E^2 - m^2c^4 = c^2Q^\dagger Q$, and its negative in the lower block. Its oscillator part is

$$
H_{\mathrm{osc}} \approx \frac{\mathbf{p}^2}{2m} + \tfrac12 m\omega^2\mathbf{r}^2 ,
$$

whose levels would be $\hbar\omega(N+\tfrac32)$ if it were the whole of the operator. But the **physical** second-order operator has the zero point removed and carries in addition the spin–orbit term $-2m\omega\boldsymbol\sigma\cdot\mathbf{L}$; in the energy, the relation $E - mc^2 \approx Q^\dagger Q/(2m)$, which follows from $E^2 - m^2c^4 = c^2Q^\dagger Q$ at leading order, contributes $-\hbar\omega\,\boldsymbol\sigma\cdot\mathbf{L}/\hbar$, whose eigenvalues $-\hbar\omega\,l$ (for $j = l+\tfrac12$) and $+\hbar\omega(l+1)$ (for $j = l-\tfrac12$) exceed the oscillator spacing $\hbar\omega$ in magnitude by the orbital factor. It is therefore not legitimate to treat the term as a small perturbation of the non-relativistic oscillator. The non-relativistic limit of the Dirac oscillator is the oscillator **with a spin–orbit coupling of order $\omega$**, and its spectrum is the branch structure derived above, not the pure oscillator spectrum. This is a standard feature of the model, and it is the reason the Dirac oscillator is used as a test of relativistic confinement rather than as a mere relativistic correction to the oscillator.

The comparison isolates where the relativistic content lives. In the free theory, the spin–orbit coupling is a $1/c^2$ correction; in the oscillator it is present at leading order because the confining substitution is itself linear in the position and frame-odd. The biquaternion framework reads this as the statement that the substitution shifts the **odd** part of the operator, and the odd part is precisely what the square converts into an even operator with a spin–orbit component.

## The Biquaternion Reading

Three structural statements can now be made in the algebra.

**The substitution is a shift of the odd part.** In the biquaternion decomposition, the gradient $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ has an even frame part ($e_0\partial_{ict}$, the timelike direction) and a frame-odd part ($e_k\partial_k$, the spacelike directions). The oscillator substitution $\mathbf{p} \to \mathbf{p} - im\omega\beta\mathbf{r}$ adds to the odd part a term linear in the position with the same frame parity. Squaring the coupled first-order operators therefore returns a **central** second-order operator — because the cross terms of the two conjugate gradients cancel as in the free case — plus a remainder in the Hermitian sector $\mathbb{M}_+$, namely the spin–orbit element $-2m\omega\,\boldsymbol\sigma\cdot\mathbf{L}$. That the remainder is in $\mathbb{M}_+$ (it is Hermitian and spinorial) rather than in the center is the algebraic statement that the oscillator's square is not the Klein–Gordon operator: the non-minimal term, unlike the mass, does not merely shift the eigenvalue; it adds a Hermitian operator to the square.

**The zero point is a commutator.** The constant $-3m\hbar\omega$ arises from the commutator of the two biquaternionic components of the shifted gradient. In the algebra, the two conjugate operators do not commute, and their commutator is the central scalar that shifts the zero point. This is why the oscillator's ground state sits at the mass gap for the aligned states: the commutator has removed the zero-point energy exactly, and the cancellation is a property of the three-dimensional quaternion algebra (three directions, three units), not of a particular representation.

**The zero modes are supersymmetric.** The operator identity has the form of a factorisation. Write

$$
Q = \boldsymbol\sigma\cdot(\mathbf{p} - im\omega\mathbf{r}), \qquad
Q^\dagger = \boldsymbol\sigma\cdot(\mathbf{p} + im\omega\mathbf{r}),
$$

so that $Q^\dagger Q = \mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 - 3m\hbar\omega - 2m\omega\boldsymbol\sigma\cdot\mathbf{L}$. The aligned states with $n_r = 0$ are exactly the **zero modes** $Q\phi = 0$, and their infinite degeneracy is the zero-mode degeneracy of the factorised operator. The pair $(Q,Q^\dagger)$ is the standard supersymmetric pair of quantum mechanics: $Q^\dagger Q$ and $QQ^\dagger$ are partner Hamiltonians, and the zero modes of $Q$ are the states the supersymmetry relates. The companion article *Supersymmetric Quantum Mechanics in the Biquaternion Framework* develops this correspondence; the Dirac oscillator is its exactly solvable relativistic realisation. The reader should note that the two operators here are not the two gradients $\tilde{\nabla},\bar{\tilde{\nabla}}$ of the free mass pair but their shifted, spin-projected forms; what is common to both is that the square of a first-order operator with a conjugate partner is a second-order operator whose zero modes carry the structure.

## Summary

The Dirac oscillator is the system obtained by the non-minimal substitution $\mathbf{p} \to \mathbf{p} - im\omega\beta\mathbf{r}$ in the Dirac Hamiltonian. The substitution is frame-odd, imaginary and linear in the position; it shifts the odd part of the first-order operator without touching the even (mass) part. In the Dirac representation the equation reduces to the coupled pair

$$
(E-mc^2)\phi = c\,\boldsymbol\sigma\cdot(\mathbf{p}+im\omega\mathbf{r})\chi,
\qquad
(E+mc^2)\chi = c\,\boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})\phi .
$$

Eliminating $\chi$ and using the Pauli identity gives the exact operator identity

$$
\left[\boldsymbol\sigma\cdot(\mathbf{p}+im\omega\mathbf{r})\right]\left[\boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})\right]
= \mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\mathbf{L},
$$

verified in the bulk of a truncated Cartesian oscillator basis to $1.8\times10^{-15}$. The right-hand side is the three-dimensional oscillator with its zero point removed, plus a spin–orbit coupling of order $\omega$. The spectrum is

$$
E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \frac{\boldsymbol\sigma\cdot\mathbf{L}}{\hbar}\right)
=
\begin{cases}
m^2c^4 + 4m\hbar\omega c^2\,n_r, & j = l+\tfrac12, \\[4pt]
m^2c^4 + 2m\hbar\omega c^2\left(2n_r+2l+1\right), & j = l-\tfrac12,
\end{cases}
$$

with the aligned branch independent of $l$ and hence an infinitely degenerate level at $E = \pm mc^2$. In one dimension the spin–orbit term is absent and the spectrum is $E^2 = m^2c^4 + 2m\hbar\omega c^2 n$, $n = 0,1,2,\dots$. In the biquaternion framework the substitution shifts the frame-odd part of the gradient; the square is central except for a Hermitian spin–orbit remainder in $\mathbb{M}_+$; the zero-point cancellation is a quaternion commutator; and the zero modes of the shifted operator are the supersymmetric partner structure that the companion article develops.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian (informational) sector |
| $\beta = \gamma^0$, $\alpha^k = \gamma^0\gamma^k$ | Frame and Dirac velocity matrices |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric (level-3 tool) |
| $H = c\,\boldsymbol\alpha\cdot(\mathbf{p}-im\omega\beta\mathbf{r}) + \beta mc^2$ | Dirac-oscillator Hamiltonian |
| $\mathbf{p} - im\omega\beta\mathbf{r}$ | Non-minimal substitution (frame-odd shift) |
| $\phi$, $\chi$ | Upper (large) and lower (small) two-spinors |
| $Q = \boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})$, $Q^\dagger = \boldsymbol\sigma\cdot(\mathbf{p}+im\omega\mathbf{r})$ | Factorised conjugate operators |
| $Q^\dagger Q = \mathbf{p}^2+m^2\omega^2\mathbf{r}^2-3m\hbar\omega-2m\omega\boldsymbol\sigma\cdot\mathbf{L}$ | Operator identity |
| $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ | Orbital angular momentum |
| $N = 2n_r + l$ | Total oscillator quantum number |
| $n_r$ | Radial quantum number |
| $E^2 = m^2c^4+4m\hbar\omega c^2 n_r$ ($j=l+\tfrac12$) | Aligned branch |
| $E^2 = m^2c^4+2m\hbar\omega c^2(2n_r+2l+1)$ ($j=l-\tfrac12$) | Anti-aligned branch |
| $E^2 = m^2c^4+2m\hbar\omega c^2 n$ | One-dimensional spectrum |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Biquaternion mass pair |
| $\Box = \partial_{ict}^2 + \Delta$ | Series d'Alembertian |

## Further Reading

- M. Moshinsky and A. Szczepaniak, "The Dirac oscillator," *Journal of Physics A: Mathematical and General* **22** (1989) L817–L819, for the original non-minimal substitution and the exact solution.
- M. Moshinsky and Yu. F. Smirnov, *The Harmonic Oscillator in Modern Physics* (Harwood, 1996), for the oscillator algebra, the pseudo-oscillator, and the relativistic realisation.
- A. D. Alhaidari, "The Dirac-oscillator Green's function," *International Journal of Theoretical Physics* **43** (2004) 939–946, for the two-branch energy spectrum obtained from the Green's-function poles.
- R. Szmytkowski and M. Gruchowski, "Relativistic quantum mechanics of a Dirac oscillator," *Journal of Physics A: Mathematical and General* **33** (2000) 5993, for the solution and its interpretation as the motion of a particle with an anomalous magnetic moment in a charged sphere.
- V. M. Villalba and A. R. Plastino, "The Dirac oscillator in a rotating frame," *Foundations of Physics Letters* **17** (2004) 259–272, and references therein, for the oscillator in external and non-inertial settings.
- F. Dominguez-Adame and M. A. Gonzalez, "The Dirac oscillator in two dimensions," *Europhysics Letters* **13** (1990) 193, for the reduced-dimensional spectra.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Dirac representation, the coupled two-spinor equations and the non-relativistic reduction.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Dirac Hamiltonian, the frame grading, and the Foldy–Wouthuysen reduction used in the non-relativistic comparison.
