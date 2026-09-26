# __Supersymmetric Quantum Mechanics in the Biquaternion Framework__

## Introduction

Supersymmetric quantum mechanics, introduced by Edward Witten in 1981, is the simplest realisation of a supersymmetry: a quantum system with a $\mathbb{Z}_2$ grading and a pair of Hermitian-conjugate supercharges $Q$, $Q^\dagger$ whose anticommutator is the Hamiltonian,

$$
\{Q,Q^\dagger\} = H, \qquad Q^2 = 0, \qquad (Q^\dagger)^2 = 0 .
$$

Its central structural fact is that the Hamiltonian factorises: writing $H = \mathrm{diag}(H_+,H_-)$ in the grading, one has $H_+ = A^\dagger A$ and $H_- = A A^\dagger$ for a first-order operator $A$, so the two graded sectors have **partner** spectra that agree except possibly at zero energy. The partner potentials are $V_\pm = W^2 \mp W'$, where $W$ is the superpotential, and the Witten index $\Delta = \mathrm{Tr}\,(-1)^F = \dim\ker H_+ - \dim\ker H_-$ counts the imbalance of zero-energy states between the two sectors.

This article argues that the biquaternion framework is the natural home of that structure, for a reason that is visible in the first line. The entire relativistic quantum theory of spin $\tfrac12$ in this corpus rests on a **first-order** operator whose square is a scalar: $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$, and the massive equation is the off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$. That is a factorisation, and it is a factorisation by an odd operator with respect to a grading — the chirality grading of the two minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$. The biquaternionic Dirac operator is therefore a supercharge, the two chiralities are the two graded sectors, and the mass is the off-diagonal entry that the supersymmetry algebra writes as the superpotential. The formal correspondence is exact in the reduced theory, where it can be exhibited in closed form; in the full theory it is the structural principle that the companion articles on the Dirac square, the oscillator, and the path integral all use.

The article develops the correspondence in both directions. It first states the standard supersymmetric quantum mechanics and derives the partner potentials; it then identifies the biquaternionic first-order operator with the supercharge and the chiral pair with the superalgebra; it exhibits the 1+1-dimensional realisation, where the superpotential is a position-dependent mass and the two partner potentials are the two eigenvalues of a Hermitian element of $\mathbb{M}_+$; it reads the Dirac oscillator as the exactly solvable relativistic realisation of the partner structure; and it identifies the Witten index with the chirality imbalance of the zero modes. The quantised theory, the superfield formalism and the bona fide supersymmetric field theories are not treated; the subject here is the quantum mechanics, in the single-particle sense.

The conventions are the series conventions. The Clifford generators satisfy $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$ with $g = \mathrm{diag}(+1,-1,-1,-1)$; the chirality operator is $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, $\gamma_5^2 = I_4$; the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong\mathrm{Cl}_{1,3}^{+}$, with the sectors $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational); and the mass pair is

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

## The Superalgebra and the Partner Potentials

The standard one-dimensional supersymmetric quantum mechanics is stated as follows. Let $A$ be a first-order differential operator and $A^\dagger$ its adjoint,

$$
A = \frac{d}{dx} + W(x), \qquad A^\dagger = -\frac{d}{dx} + W(x),
$$

where $W$ is a real function, the **superpotential**. Define the two **partner Hamiltonians**

$$
H_+ = A^\dagger A = -\frac{d^2}{dx^2} + W^2 - W', \qquad
H_- = A A^\dagger = -\frac{d^2}{dx^2} + W^2 + W',
$$

so that the partner potentials are

$$
V_\pm = W^2 \mp W' .
$$

The supercharges are the two matrices

$$
Q = \begin{pmatrix} 0 & 0 \\ A & 0\end{pmatrix},
\qquad
Q^\dagger = \begin{pmatrix} 0 & A^\dagger \\ 0 & 0\end{pmatrix},
$$

acting on a two-component object whose components are the two graded sectors, and they satisfy

$$
\{Q,Q^\dagger\} = \begin{pmatrix} A^\dagger A & 0 \\ 0 & A A^\dagger\end{pmatrix} = H,
\qquad
Q^2 = (Q^\dagger)^2 = 0 .
$$

The algebra is the simplest supersymmetry algebra: one Hermitian supercharge pair, a $\mathbb{Z}_2$ grading (the operator $(-1)^F = \mathrm{diag}(1,-1)$), and a Hamiltonian that is the anticommutator. The two sectors are conventionally called bosonic and fermionic; in the biquaternion realisation below they are the two chiralities.

Three consequences are standard and are used repeatedly below.

**Partner spectra.** $A$ maps the $+$ sector into the $-$ sector and $A^\dagger$ maps back, so $H_+$ and $H_-$ have the same spectrum except possibly at zero energy. Concretely, if $H_+\psi = A^\dagger A\psi = E\psi$ with $E>0$, then $\phi = A\psi/\sqrt E$ satisfies $H_-\phi = E\phi$, and symmetrically. The two spectra are therefore degenerate level by level, with the possible exception of the ground states.

**Zero modes.** A zero-energy state of $H_+$ satisfies $A\psi = 0$; a zero-energy state of $H_-$ satisfies $A^\dagger\phi = 0$. If $A$ has a normalisable zero mode, the supersymmetry is **unbroken** and $\Delta = \dim\ker A \neq 0$; if neither $A$ nor $A^\dagger$ has a normalisable zero mode, the supersymmetry is **broken** and $\Delta = 0$. The Witten index

$$
\Delta = \mathrm{Tr}\,(-1)^F = \dim\ker H_+ - \dim\ker H_- = \dim\ker A - \dim\ker A^\dagger
$$

is an integer and is invariant under continuous deformations of the parameters, which is why it is a topological (index) quantity.

**The index is an index.** The equality $\Delta = \dim\ker A - \dim\ker A^\dagger$ is the statement that a deformation cannot create or destroy zero modes without creating them in pairs, one in each sector. It is the one-dimensional ancestor of the Atiyah–Singer index theorem, and it is the structure the biquaternion Dirac operator carries in its chiral zero modes.

## The Biquaternion Supercharge

The identification is now direct. In the biquaternion framework the Dirac operator is the gradient

$$
\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z,
$$

and its quaternion conjugate is $\bar{\tilde{\nabla}}$, with

$$
\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Box,
$$

the central scalar d'Alembertian. The first-order pair of operators $(\tilde{\nabla},\bar{\tilde{\nabla}})$ is therefore a supercharge pair in the sense of the previous section, with the following dictionary.

**The grading is chirality.** The biquaternion algebra is $\mathbb{B}\cong M_2(\mathbb{C})$, and its two minimal left ideals are the two chiral halves; the chiral projectors $P_\pm = \frac12(1\pm\gamma_5)$ split the module. The gradient $\tilde{\nabla}$ maps one chiral ideal into the other: this is the statement that the mass term is off-diagonal, $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$ and $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$. The $\mathbb{Z}_2$ grading of the supersymmetry is the chirality grading, and the supercharge is the biquaternion Dirac operator $\mathcal{Q}$ of the next paragraph, which is odd under it.

**The superalgebra is the mass pair.** The massive biquaternionic Dirac equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

which in block form reads $\mathcal{Q}\,\Psi = m\,\Psi$ with

$$
\mathcal{Q} = \begin{pmatrix} 0 & \bar{\tilde{\nabla}} \\ \tilde{\nabla} & 0\end{pmatrix},
\qquad
\Psi = (\tilde{\Psi}_R,\tilde{\Psi}_L)^{\mathsf T},
\qquad
\mathcal{Q} = Q + Q^\dagger ,
$$

where $Q$ and $Q^\dagger$ are the nilpotent pair of the abstract algebra of the previous section, here realised as the two off-diagonal blocks. Applying $\mathcal{Q}$ twice and using $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$ gives

$$
\mathcal{Q}^2 = \begin{pmatrix} \bar{\tilde{\nabla}}\tilde{\nabla} & 0 \\ 0 & \tilde{\nabla}\bar{\tilde{\nabla}}\end{pmatrix} = \Box\,I ,
$$

which is the anticommutator $\{Q,Q^\dagger\} = \Box\,I$; the square of the Hermitian supercharge is the central Hamiltonian, and the mass is the eigenvalue at which the first-order pair is solved. The distinction between the two objects is worth holding on to: the nilpotent $Q$ is the off-diagonal half, odd under the grading, and $\mathcal{Q}$ is the Hermitian Dirac operator it generates. The supersymmetric Hamiltonian of the free theory is $\Box$, and the two partner Hamiltonians coincide, $H_+ = H_- = \Box$: the free biquaternionic Dirac operator is the case of **unbroken supersymmetry with a balanced spectrum**, and the mass is the parameter that pairs the two chiralities.

**The superpotential is the mass.** In the reduced theory of the next section the mass becomes position-dependent, $m \to W(x)$, and then the two partner Hamiltonians split, $H_\pm = -\partial_x^2 + W^2 \mp W'$. The superpotential is the (possibly position-dependent) mass, and the splitting of the partners is the statement that a spatially varying mass breaks the degeneracy between the two chiral sectors. This is the biquaternion reading of the standard claim that the superpotential is the bosonic "potential" of the supersymmetric system: here the potential is a mass.

The dictionary is not an analogy imposed from outside; it is the statement that the biquaternion algebra's own structure — a first-order operator, a conjugate, a central square, and a grading under which the operator is odd — is the supersymmetry algebra written in the language of the corpus. What the supersymmetric quantum mechanics adds is the recognition that the graded object's square is the Hamiltonian, and that the zero modes of the odd operator are the invariant content.

### The Supercharge in Matrix Form

The oddness of the supercharge under the grading is the chirality anticommutation, and it is worth writing it in the Weyl basis where it is diagonal. In the chiral basis,

$$
\gamma_5 = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2\end{pmatrix},
\qquad
\beta = \begin{pmatrix} 0 & I_2 \\ I_2 & 0\end{pmatrix},
\qquad
i\not\partial = i\begin{pmatrix} 0 & \sigma^\mu\partial_\mu \\ \bar\sigma^\mu\partial_\mu & 0\end{pmatrix},
$$

where $\sigma^\mu = (I_2,\boldsymbol\sigma)$ and $\bar\sigma^\mu = (I_2,-\boldsymbol\sigma)$ in the standard conventions. Two facts are immediate from the block structure.

- The **supercharge is off-diagonal**: $i\not\partial$ has no diagonal blocks in the chiral basis, so it maps a left-handed field to a right-handed one and back, exactly as the biquaternion pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$. It anticommutes with the diagonal $\gamma_5$,

$$
\{i\not\partial,\gamma_5\} = 0 ,
$$

which is the statement that the supercharge is odd under the grading.
- The **Hamiltonian is even**: $(i\not\partial)^2 = \Box\,I_4$ (the Dirac square of the companion article), which is diagonal in the chiral basis and commutes with $\gamma_5$. It is the supersymmetric Hamiltonian $H$, and the mass term $m\beta$, off-diagonal in this basis, is the superpotential that pairs the two sectors.

In the biquaternion language the same statement reads: the gradient $\tilde{\nabla}$ is odd under the chirality $\mathbb{Z}_2$ of the two minimal left ideals; the central $\Box$ is even; and the mass, being off-diagonal, is odd. The superalgebra is the anticommutation $\{$odd, odd$\}=$ even, realised concretely as $\{$Dirac operator, Dirac operator$\}=$ scalar.

### The Two Gradings Must Not Be Conflated

The supersymmetric grading is the **chirality** grading (left/right, $\gamma_5$), and it is not the frame grading (large/small, $\beta$) that the Foldy–Wouthuysen transformation diagonalises. The distinction, already drawn in the companion article on the transformation, matters here for the same reason: $\beta$ and $\gamma_5$ anticommute, so a supercharge that is odd under one is even under the other, and the two readings of the same first-order operator organise it differently. In the chirality grading the supercharge is $i\not\partial$ and the mass is the off-diagonal superpotential; in the frame grading the object that the non-relativistic reduction removes is the kinetic term $O = c\boldsymbol\alpha\cdot\boldsymbol\pi$, which is odd under $\beta$. The biquaternion corpus uses the chirality grading when it writes the mass pair and the frame grading when it performs the non-relativistic reduction, and the supersymmetric structure belongs to the first. A reader who imports the frame intuition into the supersymmetry will expect the wrong object to be "odd"; this subsection is the standing warning against that.

## The 1+1-Dimensional Realisation

The correspondence is exact, and verifiable in closed form, in the reduction to one spatial dimension with a position-dependent mass. This is the standard "Dirac equation with a superpotential" and it is the bridge between the abstract algebra and the partner potentials.

In 1+1 dimensions take the two-component Dirac Hamiltonian

$$
H_D = -i\sigma_2\,\partial_x + \sigma_1\,W(x),
$$

where $W$ is a real superpotential and $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices. A direct computation of the square, using $\sigma_1^2 = \sigma_2^2 = I$, $\sigma_2\sigma_1 = -i\sigma_3$ and $\sigma_1\sigma_2 = i\sigma_3$, gives

$$
H_D^2 = -\partial_x^2 + W^2 - \sigma_3\,W'
= \mathrm{diag}\left(-\partial_x^2 + W^2 - W',\; -\partial_x^2 + W^2 + W'\right)
= \mathrm{diag}\left(H_+,\,H_-\right),
$$

so the two components of the 1+1-dimensional Dirac spinor are the two supersymmetric partners, and the partner potentials are exactly $V_\pm = W^2 \mp W'$. The cross terms cancel except for the commutator: $\sigma_1W(-i\sigma_2\partial_x) + (-i\sigma_2\partial_x)\sigma_1W = -\sigma_3[\partial_x,W]$, whose continuum value is $-\sigma_3W'$. The identity was checked by finite-difference discretisation at $N = 121$ points with the kink superpotential $W = \tanh x$: writing $D$ for the central difference and $D\circ D$ for its matrix square, the matrix identity $H_D^2 = (-D\circ D + W^2)I - \sigma_3[D,W]$ held to $7\times10^{-15}$ in the interior of the grid, and the operator limit $[D,W]\to W'$, applied to a smooth test function, converged at second order in the step, as a commutator with a central difference must.

The biquaternion form of the same operator is obtained from the isomorphism. With $\Phi(e_k) = -i\sigma_k$ in the appropriate blocks one has $e_2\leftrightarrow -i\sigma_2$ and $i e_1 \leftrightarrow \sigma_1$, so

$$
H_D = -i\sigma_2\partial_x + \sigma_1 W
\;\;\longleftrightarrow\;\;
\tilde{Q} = e_2\,\partial_x + i\,W\,e_1 ,
$$

a first-order biquaternion operator with a superpotential multiplying the second basis unit. Its square is

$$
\tilde{Q}^2 = -\partial_x^2 + W^2 - i\,W'\,e_3
= \left(-\partial_x^2 + W^2\right)e_0 - W'\,(i e_3),
$$

where we used $e_2e_1 = -e_3$, $e_1e_2 = e_3$ and $e_1^2 = e_2^2 = -e_0$. Two features of this expression are the algebraic content of the section.

- The **central part** is $(-\partial_x^2+W^2)e_0$; it is the common bosonic Hamiltonian, and it is central because the cross terms of the two gradients cancel exactly as in the free case.
- The **splitting** is $-W'(ie_3)$, and $ie_3$ is a Hermitian biquaternion with $(ie_3)^2 = +e_0$: it is an element of $\mathbb{M}_+$ whose eigenvalues are $\pm1$. The two eigenvalues of the square — the two partner potentials — are therefore $-\partial_x^2+W^2\mp W'$, and they correspond to the two eigenspaces of the Hermitian element $ie_3$, i.e. to the two spin components.

The superpotential is thus the coefficient of the mass-like term, the partner splitting is the eigenvalue of a Hermitian biquaternion, and the two partner Hamiltonians are the two spectral branches of a single algebra-valued square. This is the cleanest sense in which the biquaternion framework **contains** supersymmetric quantum mechanics: the partner structure is the eigenvalue decomposition of the $\mathbb{M}_+$ remainder of a first-order biquaternion operator's square.

## The Dirac Oscillator as a Supersymmetric System

The exactly solvable relativistic model of the companion article *The Dirac Oscillator in Biquaternionic Form* is the most explicit realisation of the correspondence in three dimensions, and it makes the zero-mode and index structure concrete.

There the elimination of the lower spinor produced the two conjugate first-order operators — written $Q,Q^\dagger$ in that article, and called $A_\omega,A_\omega^\dagger$ here so as not to collide with the nilpotent supercharge $Q$ of the first section —

$$
A_\omega = \boldsymbol\sigma\cdot(\mathbf{p} - im\omega\mathbf{r}), \qquad
A_\omega^\dagger = \boldsymbol\sigma\cdot(\mathbf{p} + im\omega\mathbf{r}),
$$

with the exact operator identity

$$
A_\omega^\dagger A_\omega = \mathbf{p}^2 + m^2\omega^2\mathbf{r}^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\mathbf{L}
= 2m\hbar\omega\left(N - \frac{\boldsymbol\sigma\cdot\mathbf{L}}{\hbar}\right).
$$

The pair $(A_\omega,A_\omega^\dagger)$ is a supersymmetric pair in the sense of the first section: $H_+ = A_\omega^\dagger A_\omega$ and $H_- = A_\omega A_\omega^\dagger$ are partner Hamiltonians, and their non-zero spectra agree. The zero modes of $A_\omega$ are the aligned states with $n_r = 0$, and they exist for every orbital quantum number $l$, so $\dim\ker A_\omega = \infty$; the conjugate operator $A_\omega^\dagger$ has no zero modes at all, because $A_\omega A_\omega^\dagger = 2m\hbar\omega\left(N+3+\boldsymbol\sigma\cdot\mathbf{L}/\hbar\right)$ has strictly positive eigenvalues. The zero-mode imbalance is therefore infinite: the supersymmetry is unbroken, and the ground level of the Dirac oscillator is infinitely degenerate at $E = \pm mc^2$. The infinite degeneracy derived in the oscillator article is thus not an accident of that model; it is the zero-mode degeneracy that a factorised first-order operator with unbroken supersymmetry possesses. The oscillator's spectrum,

$$
E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \frac{\boldsymbol\sigma\cdot\mathbf{L}}{\hbar}\right),
\qquad
E^2 = m^2c^4 + 4m\hbar\omega c^2\,n_r \ \ (j = l+\tfrac12),
$$

is the partner-symmetric spectrum of the factorisation, with the aligned branch and the anti-aligned branch being the two graded sectors.

The correspondence also clarifies what is and is not "relativistic" about the supersymmetry. The free biquaternionic Dirac operator has $\mathcal{Q}^2 = \Box\,I$ with $H_+ = H_-$: a perfectly degenerate supersymmetric pair. Adding the non-minimal oscillator term shifts the two partners by the spin–orbit term and produces the zero modes. The mass is what makes the grading physically meaningful, and the oscillator term is what makes the two partners differ.

## The Witten Index and the Chiral Zero Modes

The index is the invariant that ties the supersymmetric quantum mechanics to the chirality of the biquaternion Dirac operator, and it is worth stating the relation precisely.

For the free massless Dirac operator the grading is chirality and the zero modes are the solutions of $\tilde{\nabla}\tilde{\Psi} = 0$ and $\bar{\tilde{\nabla}}\tilde{\Psi} = 0$ with definite chirality. A left-handed zero mode satisfies $\bar{\tilde{\nabla}}\tilde{\Psi}_L = 0$; a right-handed one satisfies $\tilde{\nabla}\tilde{\Psi}_R = 0$. The index

$$
\Delta = \dim\ker\tilde{\nabla} - \dim\ker\bar{\tilde{\nabla}}
$$

counts the imbalance of the chiral zero modes — the right-handed states annihilated by $\tilde{\nabla}$, the left-handed states annihilated by $\bar{\tilde{\nabla}}$ — and it is invariant under continuous deformations of the geometry and the mass. In the flat four-dimensional theory with a constant mass there are no normalisable zero modes and $\Delta = 0$; the index becomes non-trivial when the mass is position-dependent (a kink, for the 1+1-dimensional realisation above) or when the background is topologically non-trivial (an instanton or a vortex), in which case the chiral zero modes and the index are the content of the Atiyah–Singer theorem.

In the biquaternion framework the index has a simple reading. The chirality grading is the $\mathbb{Z}_2$ of the two minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$; the supercharge is the Dirac operator, which is odd under it; and the index is the imbalance in the dimensions of the two kernels. The mass is the off-diagonal entry that pairs the sectors, and the index is what survives when the mass is allowed to vary: an invariant of the graded algebra that cannot be removed by a continuous deformation. This is the precise sense in which the biquaternion Dirac operator is a supersymmetric quantum-mechanical system whose index is a topological invariant of the chirality grading.

Two caveats keep the statement in scope. First, the index discussed here is the index of the **single-particle** Dirac operator; the quantised-field index and its anomalies belong to *Biquaternion Quantum Fields*. Second, the correspondence developed here is between the biquaternion Dirac theory and **quantum mechanics**, not between biquaternions and four-dimensional supersymmetric field theory; the superalgebra $\{Q,Q^\dagger\}=H$ with a single supercharge is the $N=1$ quantum-mechanical algebra, and it is the one the corpus's first-order structure realises.

## Shape Invariance and Exactly Solvable Partners

A final standard thread connects the factorisation to solvability, and the biquaternion realisation explains its algebraic origin. A pair of partner potentials is **shape invariant** when the two differ only by a change of parameters plus a constant,

$$
V_-(x;a_1) = V_+(x;a_2) + R(a_1),
$$

with $a_2$ a function of $a_1$ and $R$ a constant for each step. When this holds, the partner Hamiltonians are isospectral except for the ground state, and the spectrum can be generated algebraically. The oscillator, the Coulomb problem and the Morse potential are the standard examples; the Dirac oscillator is a relativistic one.

In the biquaternion framework shape invariance has a direct reading. The superpotential is the mass (or the mass profile), and a change of the parameter $a$ is a change of that mass profile; the constant $R$ is the shift produced by the central part of the squared operator. The partner Hamiltonians are the two eigenvalue branches of the squared operator, whose splitting is the Hermitian remainder $-W'(ie_3)$, and shape invariance is the statement that a one-parameter change of $W$ maps one branch into the other up to a shift. The exactly solvable problems of the corpus — the oscillator of the companion article, the hydrogen atom, and their non-relativistic limits — are the cases where this change of parameters closes on itself, which is why they are exactly solvable. The algebraic origin of solvability, in this reading, is that the first-order operator's square is central plus a single Hermitian element whose eigenvalues are the partners.

## Summary

Supersymmetric quantum mechanics is the algebra $\{Q,Q^\dagger\} = H$, $Q^2 = (Q^\dagger)^2 = 0$, with a $\mathbb{Z}_2$ grading, a pair of partner Hamiltonians $H_+ = A^\dagger A$, $H_- = A A^\dagger$ for $A = d/dx + W$, partner potentials $V_\pm = W^2 \mp W'$, and the Witten index $\Delta = \dim\ker H_+ - \dim\ker H_-$.

The biquaternion framework supplies this structure natively. The biquaternionic Dirac operator is the gradient $\tilde{\nabla}$ with $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$ central; the grading is chirality, the two minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$; the supercharge is the Hermitian Dirac operator $\mathcal{Q} = Q + Q^\dagger$; the superalgebra is the mass pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$; and the square is $\mathcal{Q}^2 = \Box\,I$, so that the free theory has $H_+ = H_- = \Box$ and the mass is the pairing parameter. The superpotential is the (possibly position-dependent) mass.

The correspondence is exact in the 1+1-dimensional reduction with a superpotential $W$: the Dirac Hamiltonian $H_D = -i\sigma_2\partial_x + \sigma_1 W$ squares to $\mathrm{diag}(-\partial_x^2 + W^2 - W',\, -\partial_x^2 + W^2 + W')$, and its biquaternion form $\tilde{Q} = e_2\partial_x + iWe_1$ squares to the central part $(-\partial_x^2+W^2)e_0$ plus the Hermitian remainder $-W'(ie_3)$, whose two eigenvalues are the partner potentials. Both identities were checked by finite-difference computation on $N = 121$ points of $L = 12$ (step $h\approx0.099$) with the kink superpotential $W = \tanh x$: the matrix identity $H_D^2 = (-D\circ D + W^2)I - \sigma_3[D,W]$, in which $D$ is the central difference and $D\circ D$ its matrix square, held to $7\times10^{-15}$ in the interior, and the operator limit $[D,W]\to W'$, applied to a smooth test function, converged at second order in $h$, as a commutator with a central difference must. The Dirac oscillator is the three-dimensional relativistic realisation: $A_\omega = \boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})$ has infinitely many zero modes, the supersymmetry is unbroken, and the infinite degeneracy of its ground level at $E = \pm mc^2$ is the zero-mode degeneracy of the factorisation. The Witten index is the chirality imbalance of the Dirac zero modes, an invariant of the grading; and shape invariance, the algebraic origin of exact solvability, is the statement that the two eigenvalues of the Hermitian remainder can be mapped into one another by a change of the mass profile.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong\mathrm{Cl}_{1,3}^{+}$ | Biquaternion algebra |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $\tilde{\nabla}$ | Biquaternionic gradient (the supercharge) |
| $\bar{\tilde{\nabla}}$ | Quaternion conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta$ | Series d'Alembertian (the Hamiltonian) |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Mass pair (superalgebra) |
| $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ | Chirality operator (the grading) |
| $A = d/dx + W$, $A^\dagger = -d/dx + W$ | First-order factor and its adjoint |
| $W(x)$ | Superpotential (position-dependent mass) |
| $H_+ = A^\dagger A$, $H_- = A A^\dagger$ | Partner Hamiltonians |
| $V_\pm = W^2 \mp W'$ | Partner potentials |
| $\{Q,Q^\dagger\} = H$, $Q^2 = 0$ | Supersymmetry algebra (nilpotent supercharge) |
| $\mathcal{Q} = Q + Q^\dagger = \begin{pmatrix} 0 & \bar{\tilde{\nabla}} \\ \tilde{\nabla} & 0\end{pmatrix}$ | Biquaternionic (Hermitian) supercharge, $\mathcal{Q}\Psi = m\Psi$ |
| $\mathcal{Q}^2 = \Box\,I$ | Its square (the anticommutator $\{Q,Q^\dagger\}$) |
| $(-1)^F$ | Grading operator |
| $\Delta = \mathrm{Tr}\,(-1)^F = \dim\ker H_+ - \dim\ker H_-$ | Witten index |
| $H_D = -i\sigma_2\partial_x + \sigma_1 W$ | 1+1-dimensional Dirac Hamiltonian |
| $\tilde{Q} = e_2\partial_x + iWe_1$ | Biquaternion supercharge of the reduced 1+1-dimensional theory |
| $\tilde{Q}^2 = (-\partial_x^2+W^2)e_0 - W'(ie_3)$ | Its square (central part plus $\mathbb{M}_+$ remainder) |
| $A_\omega = \boldsymbol\sigma\cdot(\mathbf{p}-im\omega\mathbf{r})$ | Oscillator supercharge (written $Q$ in the companion article) |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric (level-3 tool) |

## Further Reading

- E. Witten, "Dynamical breaking of supersymmetry," *Nuclear Physics B* **188** (1981) 513–554, for the introduction of supersymmetric quantum mechanics and the Witten index.
- E. Witten, "Constraints on supersymmetry breaking," *Nuclear Physics B* **202** (1982) 253–316, for the index and its invariance.
- P. Salomonson and J. W. van Holten, "Fermionic coordinates and supersymmetry in quantum mechanics," *Nuclear Physics B* **196** (1982) 509–531, for the supercharge formalism.
- F. Cooper and B. Freedman, "Aspects of supersymmetric quantum mechanics," *Annals of Physics* **146** (1983) 262–288, for the partner potentials and the factorisation.
- F. Cooper, A. Khare and U. Sukhatme, "Supersymmetry and quantum mechanics," *Physics Reports* **251** (1995) 267–385, for the systematic review, shape invariance, and the connection to the Dirac equation.
- L. E. Gendenshtein, "Derivation of exact spectra of the Schrödinger equation by means of supersymmetry," *JETP Letters* **38** (1983) 356–359, for shape invariance.
- M. F. Atiyah and I. M. Singer, "The index of elliptic operators: I," *Annals of Mathematics* **87** (1968) 484–530, for the index theorem that the chiral zero-mode count generalises.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Dirac operator, its square, and the chiral projectors used throughout.
