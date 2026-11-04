# __Supersymmetric Quantum Physics in the Biquaternion Framework__

## Introduction

Supersymmetric quantum physics, introduced by Edward Witten in 1981, is the simplest realisation of a supersymmetry: a quantum system with a $\mathbb{Z}_2$ grading and a pair of conjugate supercharges $\mathcal{Q}$, $\mathcal{Q}^\dagger$ whose anticommutator is the Hamiltonian,

$$
\boxed{\;\{\mathcal{Q},\mathcal{Q}^\dagger\} = H, \qquad \mathcal{Q}^2 = 0, \qquad (\mathcal{Q}^\dagger)^2 = 0\;}.
$$

Its central structural fact is that the Hamiltonian factorises: writing $H = \mathrm{diag}(H_+,H_-)$ in the grading, one has $H_+ = A^\dagger A$ and $H_- = A A^\dagger$ for a first-order operator $A$, so the two graded sectors have **partner** spectra that agree except possibly at zero energy. The partner potentials are $V_\pm = W^2 \mp dW/dx$, where $W$ is the superpotential, and the Witten index counts the imbalance of zero-energy states between the two sectors.

This article argues that the biquaternion framework is the natural home of that structure, for a reason that is visible in the first line. The entire relativistic quantum theory of spin $\tfrac12$ in this corpus rests on a **first-order** operator whose square is a scalar: $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$, and the massive equation is the off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$. That is a factorisation, and it is a factorisation by an operator odd under a grading, since the gradient carries one chiral half into the other. The biquaternionic Dirac operator is therefore a supercharge, the two chiral halves are the two graded sectors, and the mass is the off-diagonal entry that the supersymmetry algebra reads as the superpotential. The correspondence is exact in the reduced theory, where it can be exhibited in closed form; in the full theory it is the structural principle that the companion articles on the Dirac square, the oscillator and the path integral all use.

**The grading is chirality, and chirality is the cell.** Two splittings of the algebra are in play and they are not the same. The Peirce components $\mathbb{B}\tilde\Pi_\pm$ are two copies of the spinor module; they are not the chiral pair. Chirality is the cell $\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, a pure right multiplication. On the Dirac module $\Delta = S\oplus\bar{S}$ it acts as the operator $\chi=\mathrm{diag}(-I_2,I_2)$, and its central form is the sign $\chi_{\mathrm{ad}} = i\tilde\Xi_{\mathrm{ad}}$ of the double, of square $\chi_{\mathrm{ad}}^2 = e_t$. The cell, its module representative and the central sign are one object in three representations, and it is the module operator $\chi$ that the parities below are written against. The distinction between the cell and the Peirce sign is the one drawn in *The Dirac Equation in Biquaternionic Form*, §*The Two Values of the Subscript*, where the value is a label and no cell is computed; the module operator and the central sign are that same label written in the double, and that extension is this article's own. The distinction is load-bearing below: the supercharge is odd under $\chi$, not under a Peirce sign, and a biquaternion carries no chirality label of its own.

**The two Dirac equations.** The corpus now carries two forms of the Dirac equation, and this article keeps them apart. The **one-sided** equation is the chiral pair written above: both gradients act from the left, and the mass is the off-diagonal pairing of the two chiral halves. It is the definition, and it is the form from which the supersymmetry is read. The **two-sided** equation is a single equation on an element $F\in\mathbb{B}$ in which the derivative acts from the left and the mass acts from the right through the chirality cell, $L_{\tilde\nabla^\natural}F = m\,\chi\bar{F}$; it is the form in which the two-sided operator algebra acts by cells, and its mass term is antilinear in $F$. §*The One-Sided and the Two-Sided Equation* below splits the two, and the rest of the article uses the one-sided pair.

The article develops the correspondence in both directions. It first states the standard supersymmetric quantum physics and derives the partner potentials; it then identifies the biquaternionic first-order operator with the supercharge and the chiral pair with the superalgebra; it exhibits the 1+1-dimensional realisation, where the superpotential is a position-dependent mass and the two partner potentials are the two eigenvalues of a Hermitian element of $\mathbb{M}_+$; it reads the Dirac oscillator as the exactly solvable relativistic realisation of the partner structure; and it identifies the Witten index with the chirality imbalance of the zero modes. The quantised theory, the superfield formalism and the bona fide supersymmetric field theories are not treated; the subject here is the quantum physics, in the single-particle sense. The general graded-algebra framework behind the supercharges, the graded commutator and the boundary of what the biquaternion algebra supplies rather than imports is *The Superalgebra Reading and the Odd Extension in Biquaternionic Form*; the interpretation of the parity as the grading of the ambient algebra is *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form*.

## The Conventions

The frame is the cell frame of the series. A cell is a two-sided multiplier, $L_{a}R_{b}\psi = a\psi b$, with $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ the identity and the composition rule $L_{a}R_{b}\,L_{c}R_{d}=L_{ac}R_{db}$; every operator display below is a sum of cells or a sum of element multipliers, and the side of an action is carried by position and never by a mark. The five generators of the reference frame are the cells $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, the three $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for $k=x,y,z$, and $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$. The first squares to $+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and the three spatial ones to $-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, so the four carry $\varepsilon=(1,-1,-1,-1)$ and distinct ones anticommute; the fifth anticommutes with all four and squares to $+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$. These five are named as gammas only in §*The Legacy Pauli Gamma Formulation*, and the name is not used before it.

The algebra, the sectors, the gradient, the d'Alembertian and the three conjugations are those of *Algebra and Element Conventions*, *Frame Conventions* and *Operator and Calculus Conventions*, and none is restated here. The chirality is the fifth frame cell of *Matrix Representations Conventions*, whose representative on $\Delta$ is written $\chi$ below and whose central form is the sign $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ of the complexified algebra, $\chi_{\mathrm{ad}}^2=e_t$. The mass pair is

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

and the pair operator that writes it once is $\mathbb{D}\Psi = (\tilde\nabla\tilde\Psi_R,\tilde\nabla^\natural\tilde\Psi_L)$ on $\Psi=(\tilde\Psi_L,\tilde\Psi_R)$, the operator of *Operator and Calculus Conventions*, §*The Gradient*.

## The Superalgebra and the Partner Potentials

The standard one-dimensional supersymmetric quantum physics is stated as follows. Let $A$ be a first-order differential operator and $A^\dagger$ its adjoint,

$$
A = \frac{d}{dx} + W(x), \qquad A^\dagger = -\frac{d}{dx} + W(x),
$$

where $W$ is a real function, the **superpotential**. Define the two **partner Hamiltonians**

$$
H_+ = A^\dagger A = -\frac{d^2}{dx^2} + W^2 - \frac{dW}{dx}, \qquad
H_- = A A^\dagger = -\frac{d^2}{dx^2} + W^2 + \frac{dW}{dx},
$$

so that the partner potentials are

$$
V_\pm = W^2 \mp \frac{dW}{dx} .
$$

The supercharges are the two matrices

$$
\mathcal{Q} = \begin{pmatrix} 0 & 0 \\ A & 0\end{pmatrix},
\qquad
\mathcal{Q}^\dagger = \begin{pmatrix} 0 & A^\dagger \\ 0 & 0\end{pmatrix},
$$

acting on a two-component object whose components are the two graded sectors, the first component being the $+$ sector. They satisfy

$$
\{\mathcal{Q},\mathcal{Q}^\dagger\} = \begin{pmatrix} A^\dagger A & 0 \\ 0 & A A^\dagger\end{pmatrix} = H,
\qquad
\mathcal{Q}^2 = (\mathcal{Q}^\dagger)^2 = 0 ,
$$

the two off-diagonal products vanishing term by term because each supercharge is strictly triangular. The algebra is the simplest supersymmetry algebra: one conjugate supercharge pair, a $\mathbb{Z}_2$ grading, the operator $(-1)^F = \mathrm{diag}(1,-1)$, and a Hamiltonian that is the anticommutator. Its two sectors are conventionally called bosonic and fermionic; in the biquaternion realisation below they are the two chiral halves, and neither is the bosonic sector in any other sense.

Three consequences are standard and are used repeatedly below.

**Partner spectra.** $A$ maps the $+$ sector into the $-$ sector and $A^\dagger$ maps back, so $H_+$ and $H_-$ have the same spectrum except possibly at zero energy. Concretely, if $H_+\psi = A^\dagger A\psi = E\psi$ with $E\neq0$, then $\phi = A\psi/\sqrt{|E|}$ satisfies $H_-\phi = E\phi$, and symmetrically. The two spectra are therefore degenerate level by level, with the possible exception of the ground states.

**Zero modes.** A zero-energy state of $H_+$ satisfies $A\psi = 0$; a zero-energy state of $H_-$ satisfies $A^\dagger\phi = 0$. If $A$ has a normalisable zero mode, the supersymmetry is **unbroken** and $\dim\ker A \neq 0$; if neither $A$ nor $A^\dagger$ has one, the supersymmetry is **broken** and the index vanishes. The Witten index

$$
\mathrm{Ind} = \mathrm{Tr}\,(-1)^F = \dim\ker H_+ - \dim\ker H_- = \dim\ker A - \dim\ker A^\dagger
$$

is an integer when both kernels are finite, and it is invariant under continuous deformations of the parameters, which is why it is a topological (index) quantity. The kernels need not be finite — the Dirac oscillator below has infinitely many zero modes in one chiral half and none in the other — and the difference is then still the invariant count, though no longer a finite integer, so the invariance argument is applied to a family with finite kernels and the infinite case is read as a limit. A vanishing index does not by itself mean that the supersymmetry is broken: it means that the two kernels balance, which is compatible with both.

**The index is an index.** The equality $\mathrm{Ind} = \dim\ker A - \dim\ker A^\dagger$ is the statement that a deformation cannot create or destroy zero modes without creating them in pairs, one in each sector. It is the one-dimensional ancestor of the Atiyah–Singer index theorem, and it is the structure the biquaternion Dirac operator carries in its chiral zero modes.

## The Biquaternion Supercharge

The identification is now direct. In the biquaternion framework the Dirac operator is the gradient

$$
\tilde{\nabla} = e_t\frac{\partial}{\partial Q_t} + \vec e_x\frac{\partial}{\partial Q_x} + \vec e_y\frac{\partial}{\partial Q_y} + \vec e_z\frac{\partial}{\partial Q_z},
$$

and its quaternion conjugate is $\tilde{\nabla}^{\natural}$, with

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \Box,
$$

the central scalar d'Alembertian. The first-order pair $(\tilde{\nabla},\tilde{\nabla}^{\natural})$ is therefore a supercharge pair in the sense of the previous section, with the following dictionary.

**The grading is chirality.** Chirality is the cell $\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, which on the Dirac module $\Delta = S\oplus\bar{S}$ its representative is written $\chi=\mathrm{diag}(-I_2,I_2)$ — the overall sign is a convention, and with this one the $+$ sector of the abstract section, the first component, is the left-handed half $S$, on which $\chi=-1$ — and in the cell algebra it is the chirality cell $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, which acts by $\psi\mapsto -i\,e_t\,\psi\,\vec e_z$ and squares to $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ because $(-i)^2=+1$ and $\vec e_z^2=-e_t$. The gradient carries one chiral half into the other: $\tilde\nabla$ maps $\bar{S}$ to $S$ and $\tilde\nabla^\natural$ maps $S$ to $\bar{S}$, which is exactly the off-diagonality that makes an operator odd under a diagonal grading. The $\mathbb{Z}_2$ grading of the supersymmetry is $\chi$, and the supercharge is the gradient read on $\Delta$, where it has no diagonal block.

**The superalgebra is the mass pair.** The massive biquaternionic Dirac equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

which in block form reads $\mathbb{D}\,\Psi = m\,\Psi$ with

$$
\mathbb{D} = \begin{pmatrix} 0 & \tilde{\nabla} \\ \tilde{\nabla}^{\natural} & 0\end{pmatrix},
\qquad
\Psi = (\tilde{\Psi}_L,\tilde{\Psi}_R)^{\mathsf T},
\qquad
\mathbb{D} = \mathcal{Q} + \mathcal{Q}^{\natural},
$$

where the two strictly triangular halves are

$$
\mathcal{Q} = \begin{pmatrix} 0 & \tilde{\nabla} \\ 0 & 0\end{pmatrix},
\qquad
\mathcal{Q}^{\natural} = \begin{pmatrix} 0 & 0 \\ \tilde{\nabla}^{\natural} & 0\end{pmatrix},
\qquad
\mathcal{Q}^2 = (\mathcal{Q}^{\natural})^2 = 0 .
$$

Here the name $\mathcal{Q}$ follows the natural half rather than the adjoint: with $A = \tilde\nabla^\natural$, so that $A^\dagger = \tilde\nabla$, this is the supercharge pair of the previous section with the two names exchanged, and $H_+ = A^\dagger A = \tilde\nabla\tilde\nabla^\natural$ is the same operator either way. Applying $\mathbb{D}$ twice and using $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$ gives

$$
\boxed{\;\mathbb{D}^2 = \begin{pmatrix} \tilde{\nabla}\tilde{\nabla}^{\natural} & 0 \\ 0 & \tilde{\nabla}^{\natural}\tilde{\nabla}\end{pmatrix} = \Box\,I\;},
$$

which is the anticommutator $\{\mathcal{Q},\mathcal{Q}^{\natural}\} = \Box\,I$: the square of the supercharge is the central Hamiltonian, and the mass is the eigenvalue at which the first-order pair is solved. Three objects are distinguished here and are worth holding apart. The nilpotent $\mathcal{Q}$ is one off-diagonal half, odd under $\chi$. The operator $\mathbb{D}$, its sum with the conjugate half, is the Dirac operator, odd under $\chi$ and with diagonal square. And $m$ is a number: in $\mathbb{D}\Psi=m\Psi$ it multiplies the identity, and it is only when the same equation is read as a Schrödinger problem, $i\partial \psi/\partial t = H_D\psi$ with $H_D = c\boldsymbol\alpha\cdot\vec p + \beta mc^2$, that the mass becomes the operator $m\beta$, off-diagonal in the chiral basis and odd under $\chi$. The off-diagonality of the one-sided mass pair and the oddness of $m\beta$ are one statement in two languages.

**One sign, recorded once.** With respect to the module's sesquilinear form the adjoint of the gradient is minus its quaternion conjugate, $(\tilde\nabla)^{\dagger} = -\tilde\nabla^{\natural}$: the derivative contributes $(\partial/\partial Q_\mu)^{\dagger} = -\partial/\partial Q_\mu$, and the units satisfy $e_t^{*}=e_t$ and $\vec e_k^{*}=-\vec e_k$, so the two minus signs cancel on the spatial part and the timelike term keeps its own. The two blocks therefore satisfy $\mathcal{Q}^{\dagger} = -\mathcal{Q}^{\natural}$ and $\mathbb{D}^{\dagger} = -\mathbb{D}$, so $\mathbb{D}$ is anti-Hermitian and $i\mathbb{D}$ is the Hermitian representative: the operator of the series is anti-Hermitian exactly as its first derivative is, and the factor of $i$ that repairs it is the one that also appears in the momentum of the coordinate form. The algebra is unaffected. Since $\mathcal{Q}^{\dagger} = -\mathcal{Q}^{\natural}$, the repaired half is $(i\mathcal{Q})^{\dagger} = i\mathcal{Q}^{\natural}$ and the product $(i\mathcal{Q})(i\mathcal{Q})^{\dagger} = \mathcal{Q}\mathcal{Q}^{\natural}$ carries $i\cdot i = -1$, so $\{i\mathcal{Q},(i\mathcal{Q})^{\dagger}\} = -\Box\,I$ while the algebra's pairing is $\{\mathcal{Q},\mathcal{Q}^{\natural}\} = \Box\,I$. The two differ by that one sign, which is the price of Hermiticity: multiplying an anti-Hermitian operator by $i$ multiplies its square by $-1$. The sign that does move is the one inside the d'Alembertian: on the material sector, where $Q_t=ict'$ and $\partial/\partial Q_t = -(i/c)\partial/\partial t'$, one has $\Box = -\partial^2/\partial t'^2/c^2+\Delta_Q$, the minus being $i^2=-1$ again.

**The superpotential is the mass.** For a constant mass the parameter is an eigenvalue and the two partners coincide. For a position-dependent mass, $m\to W(x)$, the mass is no longer an eigenvalue but a term of the operator, and the two partner Hamiltonians split, $H_\pm = -\partial^2/\partial Q_x^2 + W^2 \mp dW/dx$. The superpotential is thus the possibly position-dependent mass, and the splitting of the partners is the statement that a spatially varying mass breaks the degeneracy between the two chiral sectors. This is the biquaternion form of the standard claim that the superpotential is the "potential" of the supersymmetric system: here the potential is a mass.

The dictionary is not an analogy imposed from outside; it is the statement that the biquaternion algebra's own structure — a first-order operator, a conjugate, a central square, and a grading under which the operator is odd — is the supersymmetry algebra written in the language of the corpus. What the supersymmetric quantum physics adds is the recognition that the graded object's square is the Hamiltonian, and that the zero modes of the odd operator are the invariant content.

### The One-Sided and the Two-Sided Equation

Two formulations carry the name *Dirac equation*, and the supersymmetry above is read from the first. The **one-sided** form is the chiral pair written with both gradients on the left,

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R
\qquad\text{(one-sided)},
$$

and the **two-sided** form is a single equation on an element, in which the derivative multiplies from the left and the mass from the right through the chirality cell,

$$
L_{\tilde\nabla^\natural}F = m\,\chi\bar{F}
\qquad\text{(two-sided)} .
$$

The second is the first restated on the algebra rather than on the module: one equation instead of a pair, at the price of the coefficient conjugate.

| | One-sided equation | Two-sided equation |
|---|---|---|
| Equation | $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | $L_{\tilde\nabla^\natural}F = m\,\chi\bar{F}$ |
| Multiplication | left, by $\tilde\nabla$ and $\tilde\nabla^\natural$ | left by the gradient, right by the chirality cell |
| Field | $\tilde{\Psi} = \tilde{\Psi}_L+\tilde{\Psi}_R \in \Delta = S\oplus\bar{S}$ | $F\in\mathbb{B}$ |
| Mass | the off-diagonal pairing of the two chiral halves | the cell that defines $\chi$, applied to the conjugate field |
| Linearity | linear in the field | antilinear in the mass term |
| Use | the definition, and the supersymmetry of this article | the two-sided operator algebra |

The two-sided equation is a single equation on the algebra, and it exhibits the structure that the module form states in blocks. Its derivative is a left multiplier and its mass is a right multiplier, so the two commute as operators, and the mass term is the chirality cell itself, $\chi = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} = -iR_{\vec e_z}^{\mathrm{axf}}$. That is the operator-algebra form of the same fact: the derivative is chirality-blind, and the mass is the chirality-carrying term. The price of the single equation is the coefficient conjugation $\bar{F}$, which supplies the antilinear part; the one-sided pair needs no conjugation and is the definition.

### The Supercharge in Block Form

In the chiral basis, the basis in which $\chi$ is diagonal, the three operators are read at sight:

$$
\chi = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2\end{pmatrix},
\qquad
\beta = \begin{pmatrix} 0 & I_2 \\ I_2 & 0\end{pmatrix},
\qquad
\mathbb{D} = \begin{pmatrix} 0 & \tilde\nabla \\ \tilde\nabla^{\natural} & 0\end{pmatrix},
$$

with $\mathbb{D}^2=\Box\,I$, $[\mathbb{D}^2,\beta]=0$ and $\{\chi,\beta\}=0$. Two facts follow from the block structure.

- The **supercharge is off-diagonal**: $\mathbb{D}$ has no diagonal block in the chiral basis, so it maps a left-handed field to a right-handed one and back, exactly as the pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ does. It is odd under $\chi$, which is the statement that the supercharge carries the odd grade, $\{\mathbb{D},\chi\}=0$.
- The **Hamiltonian is even**: the square of the gradient is the central scalar, $\tilde{\nabla}^{\natural}\tilde{\nabla} = \Box$, which is diagonal in every basis and commutes with $\chi$. It is the supersymmetric Hamiltonian $H$. The mass, in turn, is a number in the eigenvalue equation and the operator $m\beta$ in the Schrödinger form; $m\beta$ is off-diagonal here and satisfies $\{\chi,m\beta\}=0$, so the mass insertion is the chirality-odd object that pairs the two sectors.

In the biquaternion language the same statement reads: the gradient is odd under the chirality $\mathbb{Z}_2$ of the two chiral halves; the central $\Box$ is even; and the mass, being the off-diagonal pairing, is odd. The superalgebra is the rule that a pair of odd objects multiplies to an even one, realised concretely as $\{\tilde\nabla,\tilde\nabla^\natural\}=\Box$, a scalar.

### The Two Gradings Must Not Be Conflated

The supersymmetric grading is the **chirality** $\chi$ (left/right), and it is not the frame grading (large/small) $\beta$ that the Foldy–Wouthuysen transformation diagonalises. The two anticommute, $\{\chi,\beta\}=0$, so $\chi$ is itself odd under the frame grading.

They sort the same Hamiltonian differently, and the sorting is complementary. Write the coordinate form $H = \beta mc^2 + c\boldsymbol\alpha\cdot\vec p$, with $\alpha_k$ the velocity matrices satisfying $\{\alpha_j,\alpha_k\}=2\delta_{jk}$ and $\{\alpha_k,\beta\}=0$. Chirality commutes with every $\alpha_k$ and anticommutes with $\beta$; the frame grading commutes with $\beta$ and anticommutes with every $\alpha_k$. Each grading therefore splits $H$ into one even and one odd piece, and the two gradings swap the pieces: the mass term is odd under $\chi$ and even under $\beta$, the kinetic term even under $\chi$ and odd under $\beta$. Neither grading makes the whole of $H$ odd, and that is not a defect of the notation but the reason the two are distinguished. The non-relativistic reduction removes the term that is odd under $\beta$, and the supersymmetry pairs the halves that $\chi$ separates.

The supercharge carries no mass. The operator $\mathbb{D} = \mathcal{Q}+\mathcal{Q}^{\natural}$ of the previous sections has no diagonal block in the chiral basis, so $\{\mathbb{D},\chi\}=0$ and its square is the scalar $\Box$; the mass enters only as the eigenvalue in $\mathbb{D}\Psi = m\Psi$, where it is the pairing of the two chiral halves. The pair (operator odd under $\chi$, central square) is exactly what the supersymmetry needs, and it exists in the chirality grading and in no other. A reader who imports the frame intuition into the supersymmetry will expect the kinetic term to be the odd object and the mass the even one, and will then read the supercharge as the wrong operator.

## The 1+1-Dimensional Realisation

The correspondence is exact, and verifiable in closed form, in the reduction to one spatial dimension with a position-dependent mass. This is the standard Dirac equation with a superpotential, and it is the bridge between the abstract algebra and the partner potentials.

Take the two-component Dirac Hamiltonian

$$
H_D = -i\sigma_2\frac{\partial}{\partial Q_x} + \sigma_1\,W,
$$

where $W$ is a real superpotential, a function of the coordinate alone, and $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices. Since $\sigma_1^2 = \sigma_2^2 = I$ with $\sigma_2\sigma_1 = -i\sigma_3$ and $\sigma_1\sigma_2 = i\sigma_3$, the two cross terms combine into one commutator, and

$$
H_D^2 = -\frac{\partial^2}{\partial Q_x^2} + W^2 - \sigma_3\Bigl[\frac{\partial}{\partial Q_x},W\Bigr].
$$

The commutator is multiplication by the derivative of $W$, because the derivative acts on everything to its right and the only term that survives is its action on $W$. Writing $x$ for the coordinate $Q_x$, so that $\partial W/\partial Q_x = dW/dx$, this gives

$$
H_D^2 = \mathrm{diag}\left(-\frac{\partial^2}{\partial Q_x^2} + W^2 - \frac{dW}{dx},\; -\frac{\partial^2}{\partial Q_x^2} + W^2 + \frac{dW}{dx}\right)
= \mathrm{diag}\left(H_+,\,H_-\right),
$$

so the two components of the 1+1-dimensional Dirac spinor are the two supersymmetric partners, and the partner potentials are exactly $V_\pm = W^2 \mp dW/dx$.

**The check.** The identity was verified on $121$ points of $[-6,6]$ (step $h=0.1$) with the kink superpotential $W = \tanh x$. Writing $D$ for the central difference and $D\circ D$ for its matrix square, the matrix identity $H_D^2 = (-D\circ D + W^2)I - \sigma_3[D,W]$ held to $7\times10^{-15}$ on the whole grid, and the operator limit $[D,W]\to dW/dx$, applied to a smooth test function, converged at second order: the errors at successive halvings of the step, from $121$ to $241$ to $481$ points, stood in the ratios $3.97$ and $3.99$, as a commutator with a central difference must.

**The biquaternion form.** With $\mathsf{M}_2(\vec e_k) = -i\sigma_k$ one has $\vec e_y\leftrightarrow -i\sigma_2$ and $i\vec e_x\leftrightarrow\sigma_1$, so the operator of the same equation is

$$
H_D = -i\sigma_2\frac{\partial}{\partial Q_x} + \sigma_1 W
\;\;\longleftrightarrow\;\;
\tilde{Q} = \vec e_y\frac{\partial}{\partial Q_x} + i\,W\,\vec e_x ,
$$

a first-order biquaternion operator with the superpotential multiplying the second basis unit. Its square follows from $\vec e_y\vec e_x = -\vec e_z$, $\vec e_x\vec e_y = \vec e_z$ and $\vec e_x^2 = \vec e_y^2 = -e_t$:

$$
\tilde{Q}^2 = \left(-\frac{\partial^2}{\partial Q_x^2} + W^2\right)e_t - i\,\frac{dW}{dx}\,\vec e_z
= \left(-\frac{\partial^2}{\partial Q_x^2} + W^2\right)e_t - \frac{dW}{dx}\,(i \vec e_z).
$$

Both terms of $\tilde Q$ are Hermitian: the derivative and $\vec e_y$ each contribute a minus, and $i\vec e_x$ is Hermitian because $(i\vec e_x)^{*} = i^{*}\vec e_x^{*} = (-i)(-\vec e_x) = i\vec e_x$. So $\tilde Q$ is the element-level analogue of the Hermitian $H_D$. The same identity, read in the same discretisation, held to $7\times10^{-15}$.

Two features of this square are the algebraic content of the section.

- The **central part** is $(-\partial^2/\partial Q_x^2+W^2)e_t$; it is the common bosonic Hamiltonian, and it is central because the cross terms of the two factors cancel exactly as in the free case.
- The **splitting** is $-\frac{dW}{dx}(i\vec e_z)$, and $i\vec e_z$ is a Hermitian biquaternion with $(i\vec e_z)^2 = i^2\vec e_z^2 = +e_t$: an element of $\mathbb{M}_+$ with eigenvalues $\pm1$. The two eigenvalues of the square — the two partner potentials — are therefore $-\partial^2/\partial Q_x^2+W^2\mp dW/dx$, and they correspond to the two eigenspaces of the Hermitian element $i\vec e_z$, that is, to the two spin components.

The superpotential is thus the coefficient of the mass-like term, the partner splitting is the eigenvalue of a Hermitian biquaternion, and the two partner Hamiltonians are the two spectral branches of a single algebra-valued square. This is the cleanest sense in which the biquaternion framework **contains** supersymmetric quantum physics: the partner structure is the eigenvalue decomposition of the $\mathbb{M}_+$ remainder of a first-order biquaternion operator's square.

## The Dirac Oscillator as a Supersymmetric System

The exactly solvable relativistic model of the companion article *The Dirac Oscillator in Biquaternionic Form* is the most explicit three-dimensional realisation of the correspondence, and it makes the zero-mode and index structure concrete.

Eliminating the lower spinor there produced the two conjugate first-order operators — written $\mathcal{Q},\mathcal{Q}^\dagger$ in that article, and called $A_\omega,A_\omega^\dagger$ here so as not to collide with the nilpotent supercharge —

$$
A_\omega = \boldsymbol\sigma\cdot(\vec p - im\omega\vec r), \qquad
A_\omega^\dagger = \boldsymbol\sigma\cdot(\vec p + im\omega\vec r),
$$

with the exact operator identity

$$
A_\omega^\dagger A_\omega = \vec p^2 + m^2\omega^2\vec r^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\vec L
= 2m\hbar\omega\left(N - \frac{\boldsymbol\sigma\cdot\vec L}{\hbar}\right),
$$

and its partner

$$
A_\omega A_\omega^\dagger = 2m\hbar\omega\left(N + 3 + \frac{\boldsymbol\sigma\cdot\vec L}{\hbar}\right),
$$

where $N$ is the oscillator number operator. The constant terms differ, $-3m\hbar\omega$ against $+3m\hbar\omega$, and the two products differ by their commutator, which carries the constant and twice the spin–orbit term, $[A_\omega^\dagger,A_\omega] = -6m\hbar\omega - 4m\omega\,\boldsymbol\sigma\cdot\vec L$. The commutator is not a multiple of the identity, and the two operators are nevertheless isospectral away from zero, because $A_\omega$ intertwines them: $A_\omega(A_\omega^\dagger A_\omega) = (A_\omega A_\omega^\dagger)A_\omega$. Both identities were checked on the truncated oscillator space of the states with $N\le4$ (thirty-five bosonic states, seventy with the spin), where they held to $10^{-15}$ in the bulk of the basis, that is for every state with $N\le2$; the deviation in the outermost shell is the expected artefact of a truncation that realises $[a_k,a_k^\dagger]=1$ only below its ceiling. $A_\omega$ annihilates the vacuum exactly.

The pair $(A_\omega,A_\omega^\dagger)$ is a supersymmetric pair in the sense of the first section: $H_+ = A_\omega^\dagger A_\omega$ and $H_- = A_\omega A_\omega^\dagger$ are partner Hamiltonians, and their non-zero spectra agree. The zero modes of $A_\omega$ are the aligned states with $n_r = 0$, and they exist for every orbital quantum number $l$, so $\dim\ker A_\omega = \infty$; the conjugate operator has no zero modes at all, because $A_\omega A_\omega^\dagger$ has strictly positive eigenvalues. The zero-mode imbalance is therefore infinite: the supersymmetry is unbroken, and the ground level of the Dirac oscillator is infinitely degenerate at $E = \pm mc^2$. The infinite degeneracy derived in the oscillator article is thus not an accident of that model; it is the zero-mode degeneracy that a factorised first-order operator with unbroken supersymmetry possesses. The oscillator's spectrum,

$$
E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \frac{\boldsymbol\sigma\cdot\vec L}{\hbar}\right),
\qquad
E^2 = m^2c^4 + 4m\hbar\omega c^2\,n_r \ \ (s_{\mathrm{tot}} = l+\tfrac12),
$$

is the spectrum of $H_+ = A_\omega^\dagger A_\omega$. The first line is the general form, and the second is its aligned branch, $\boldsymbol\sigma\cdot\vec L/\hbar = l$, rewritten with $N = 2n_r+l$; that branch vanishes at $n_r = 0$, which is the infinitely degenerate level at $E = \pm mc^2$. The anti-aligned branch, $\boldsymbol\sigma\cdot\vec L/\hbar = -(l+1)$, gives $E^2 = m^2c^4 + 2m\hbar\omega c^2(2n_r+2l+1)$. The two branches are the two eigenvalues of the spin–orbit term, not the two graded sectors. The partner $H_- = A_\omega A_\omega^\dagger$ has two towers as well, $2m\hbar\omega(2n_r+2l+3)$ aligned and $4m\hbar\omega(n_r+1)$ anti-aligned; these are the two towers of $H_+$ with the branches exchanged and $n_r$ advanced by one. At fixed excitation the statement is exact: $\mathrm{spec}\,H_-$ on the states of $N$ excitations is $\mathrm{spec}\,H_+$ on the states of $N+1$ excitations with the zero modes removed. The exchange of branches is forced by the intertwiner, since $A_\omega$ commutes with $\vec J$, lowers $N$ by one and is odd under parity, so it changes $l$ by one unit and cannot keep the branch label.

The correspondence also clarifies what is and is not supersymmetric about the free theory. The free biquaternionic Dirac operator has $\mathbb{D}^2 = \Box\,I$ with $H_+ = H_-$: the pair is degenerate, the index vanishes, and what remains of the supersymmetry is the exact degeneracy, not a protected zero mode. Adding the non-minimal oscillator term shifts the two partners by opposite constants and opposite spin–orbit terms, and produces the zero modes. The mass is what makes the grading physically meaningful, and the oscillator term is what makes the two partners differ.

## The Witten Index and the Chiral Zero Modes

The index is the invariant that ties the supersymmetric quantum physics to the chirality of the biquaternion Dirac operator, and the relation is worth stating precisely.

For the free massless Dirac operator the grading is chirality, and a chiral zero mode is a chiral half annihilated by its own gradient: a left-handed one satisfies $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = 0$ and a right-handed one satisfies $\tilde{\nabla}\tilde{\Psi}_R = 0$. The index

$$
\mathrm{Ind} = \dim\ker H_+ - \dim\ker H_- = \dim\ker\tilde{\nabla}^{\natural} - \dim\ker\tilde{\nabla}
$$

counts the imbalance of the chiral zero modes — the left-handed states annihilated by $\tilde{\nabla}^{\natural}$, which are the kernel of the $(1,1)$ block $H_+=\tilde\nabla\tilde\nabla^\natural$, minus the right-handed states annihilated by $\tilde{\nabla}$, the kernel of $H_-=\tilde\nabla^\natural\tilde\nabla$ — and it is invariant under continuous deformations of the geometry and of the mass. In the flat four-dimensional theory with a constant mass there are no normalisable zero modes and the index vanishes; it becomes non-trivial when the mass is position-dependent, as the kink of the 1+1-dimensional realisation is, or when the background is topologically non-trivial, as an instanton or a vortex is, in which case the chiral zero modes and the index are the content of the Atiyah–Singer theorem.

In the biquaternion framework the index has a simple interpretation. The chirality grading is the $\mathbb{Z}_2$ of the two chiral halves of $\Delta = S\oplus\bar{S}$; the supercharge is the gradient read on $\Delta$, which is odd under it; and the index is the imbalance in the dimensions of the two kernels. The mass is the off-diagonal entry that pairs the sectors, and the index is what survives when the mass is allowed to vary: an invariant of the graded algebra that no continuous deformation removes. That is the precise sense in which the biquaternion Dirac operator is a supersymmetric quantum-mechanical system whose index is a topological invariant of the chirality grading.

Two caveats keep the statement in scope. First, the index discussed here is the index of the **single-particle** Dirac operator; the quantised-field index and its anomalies belong to *Biquaternion Quantum Fields*. Second, the correspondence developed here is between the biquaternion Dirac theory and **quantum physics**, not between biquaternions and four-dimensional supersymmetric field theory; the superalgebra $\{\mathcal{Q},\mathcal{Q}^\dagger\}=H$ with a single supercharge pair is the quantum-mechanical $\mathcal{N}=1$ algebra, and it is the one the corpus's first-order structure realises.

## Shape Invariance and Exactly Solvable Partners

A final standard thread connects the factorisation to solvability, and the biquaternion realisation explains its algebraic origin. A pair of partner potentials is **shape invariant** when the two differ only by a change of parameters plus a constant,

$$
V_-(x;a_1) = V_+(x;a_2) + R(a_1),
$$

with $a_2$ a function of $a_1$ and $R$ a constant for each step. When this holds, the partner Hamiltonians are isospectral except for the ground state, and the spectrum can be generated algebraically. The oscillator, the Coulomb problem and the Morse potential are the standard examples; the Dirac oscillator is a relativistic one.

In the biquaternion framework shape invariance has a direct interpretation. The superpotential is the mass, or the mass profile, and a change of the parameter $a$ is a change of that profile; the constant $R$ is the shift produced by the central part of the squared operator. The partner Hamiltonians are the two eigenvalue branches of the squared operator, whose splitting is the Hermitian remainder $-\frac{dW}{dx}(i\vec e_z)$, and shape invariance is the statement that a one-parameter change of $W$ maps one branch into the other up to a shift. The exactly solvable problems of the corpus — the oscillator of the companion article and [The Hydrogen Atom in Biquaternionic Form: The Non-Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-non-relativistic-case.html), together with their non-relativistic limits — are the cases where this change of parameters closes on itself, which is why they are exactly solvable. The algebraic origin of solvability, in this interpretation, is that the square of the first-order operator is central plus a single Hermitian element whose eigenvalues are the partners.

**The isospectral example.** The partner pair is the corpus's simplest isospectral family: $H_+=A^{\dagger}A$ and $H_-=AA^{\dagger}$ agree away from zero, differ at zero where the Witten index counts the imbalance, and are carried into one another by the change of the mass profile that shape invariance describes. The element-level version of the same statement is §*The Isospectral Family* of [The Roots of a General Element: Mass, Frames and the Mass Shell](the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html).

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and a cell is $L_{a}R_{b}$.

$$
\begin{aligned}
\gamma_0[\mathbb{M}_-] &= iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}, &\gamma_1[\mathbb{M}_-] &= iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_2[\mathbb{M}_-] &= iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}, &\gamma_3[\mathbb{M}_-] &= iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_5 &= -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0[\mathbb{M}_-] &= iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}, &\gamma_1[\mathbb{M}_-] &= iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\\[2pt]
\gamma_2[\mathbb{M}_-] &= iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}, &\gamma_3[\mathbb{M}_-] &= iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\\[2pt]
\gamma_5 &= -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
\end{aligned}
$$

The squares follow from $(L_{a}R_{b})^2=L_{a^2}R_{b^2}$ and $\vec e_k^2=-e_t$: $\gamma_0[\mathbb{M}_-]^2=+L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and $\gamma_k[\mathbb{M}_-]^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, so the four carry $\varepsilon=(1,-1,-1,-1)$, and $\{L_{a}R_{b},L_{c}R_{d}\}=L_{ac}R_{db}+L_{ca}R_{bd}$. A cell is a pure tensor in $\mathrm{End}(\mathbb{B})\cong\mathbb{B}\otimes\mathbb{B}^{\mathrm{op}}$, and the cells span the whole operator algebra over $\mathbb{C}$, so every operator on the module is a finite sum of cells. A single cell is not a projection: $L_{a}R_{b}$ is invertible whenever $a$ and $b$ are invertible, so it has rank four, and the operators of this article are written as short sums of cells rather than as one.

$\gamma_5$ is the reference-frame cell of the chirality and $\gamma_0[\mathbb{M}_-]$ the reference-frame time cell, and two identifications close the article. The chirality sign of the previous sections, $\chi=\mathrm{diag}(-I_2,I_2)$ on $\Delta$, has $\gamma_5$ as its cell: the cell and the array are the same operator in the two representations, while the central sign $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is the algebra's definition of it. And $\gamma_0[\mathbb{M}_-]$ is off-diagonal on the Dirac module, so the frame grading $\beta$ of §*The Two Gradings Must Not Be Conflated* is $\gamma_0[\mathbb{M}_-]$. The anticommutation that separates the two gradings is then a one-line computation on the cells,

$$
\gamma_0[\mathbb{M}_-]\gamma_5 = (iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})(-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}) = (-i^2)\,L_{e_t}^{\mathrm{pau}}R_{\vec e_z\vec e_x}^{\mathrm{pau}} = L_{e_t}^{\mathrm{pau}}R_{\vec e_z\vec e_x}^{\mathrm{pau}} = -L_{e_t}^{\mathrm{pau}}R_{\vec e_x\vec e_z}^{\mathrm{pau}} = -\gamma_5\gamma_0[\mathbb{M}_-],
$$

In the axis-free display:

$$
\gamma_0[\mathbb{M}_-]\gamma_5 = (iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}})(-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}) = (-i^2)\,L_{e_t}^{\mathrm{axf}}R_{\vec e_z\vec e_x}^{\mathrm{axf}} = L_{e_t}^{\mathrm{axf}}R_{\vec e_z\vec e_x}^{\mathrm{axf}} = -L_{e_t}^{\mathrm{axf}}R_{\vec e_x\vec e_z}^{\mathrm{axf}} = -\gamma_5\gamma_0[\mathbb{M}_-],
$$

the two coefficients multiplying to $(-i)(i) = -i^2 = +1$, and the minus coming from the right multipliers, whose order the composition rule reverses: $R_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} = R_{\vec e_z\vec e_x}^{\mathrm{pau}} = -R_{\vec e_x\vec e_z}^{\mathrm{pau}}$, since $\vec e_z\vec e_x = -\vec e_x\vec e_z$.

The dictionary is complex-linear; over $\mathbb{R}$ the products of the gammas span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Supersymmetric quantum physics is the algebra $\{\mathcal{Q},\mathcal{Q}^\dagger\} = H$, $\mathcal{Q}^2 = (\mathcal{Q}^\dagger)^2 = 0$, with a $\mathbb{Z}_2$ grading, a pair of partner Hamiltonians $H_+ = A^\dagger A$, $H_- = A A^\dagger$ for $A = d/dx + W$, partner potentials $V_\pm = W^2 \mp dW/dx$, and the Witten index $\mathrm{Ind} = \dim\ker H_+ - \dim\ker H_-$.

The biquaternion framework supplies this structure natively. The biquaternionic Dirac operator is the gradient $\tilde{\nabla}$ with $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$ central; the grading is the chirality cell $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ on $\Delta=S\oplus\bar{S}$, whose central form is the sign $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$; the supercharge is the operator $\mathbb{D} = \mathcal{Q}+\mathcal{Q}^{\natural}$ with $\mathbb{D}^2=\Box\,I$; the superalgebra is the mass pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$, in which the mass is an off-diagonal eigenvalue; and the free theory has $H_+ = H_- = \Box$, a balanced spectrum with a vanishing index. The two-sided form of the same equation, $L_{\tilde\nabla^\natural}F = m\,\chi\bar{F}$, puts the derivative on the left and the chirality cell on the right, and exhibits the mass as the chirality-carrying term.

The correspondence is exact in the 1+1-dimensional reduction with a superpotential $W$: the Dirac Hamiltonian $H_D = -i\sigma_2\partial/\partial Q_x + \sigma_1 W$ squares to $\mathrm{diag}(-\partial^2/\partial Q_x^2 + W^2 - dW/dx,\, -\partial^2/\partial Q_x^2 + W^2 + dW/dx)$, and its biquaternion form $\tilde{Q} = \vec e_y\partial/\partial Q_x + iW\vec e_x$ squares to the central part $(-\partial^2/\partial Q_x^2+W^2)e_t$ plus the Hermitian remainder $-\frac{dW}{dx}(i\vec e_z)$, whose two eigenvalues are the partner potentials. Both identities were checked by finite-difference computation on $121$ points of $[-6,6]$ (step $h=0.1$) with the kink superpotential $W = \tanh x$: the first held to $7\times10^{-15}$ on the whole grid, and the operator limit $[D,W]\to dW/dx$ converged at second order in $h$, the error falling by a factor close to four at each halving of the step.

The Dirac oscillator is the three-dimensional relativistic realisation: $A_\omega = \boldsymbol\sigma\cdot(\vec p-im\omega\vec r)$ has infinitely many zero modes, $A_\omega A_\omega^\dagger = 2m\hbar\omega(N+3+\boldsymbol\sigma\cdot\vec L/\hbar)$ has none, the supersymmetry is unbroken, and the infinite degeneracy of the ground level at $E = \pm mc^2$ is the zero-mode degeneracy of the factorisation. The Witten index is the chirality imbalance of the Dirac zero modes, an invariant of the grading; and shape invariance, the algebraic origin of exact solvability, is the statement that the two eigenvalues of the Hermitian remainder can be mapped into one another by a change of the mass profile.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong\mathrm{Cl}_{1,3}^{+}$ | Biquaternion algebra |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $e_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, with $i^2=-1$ |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi = a\psi b$ | The cell: multiply on the left by $a$, on the right by $b$ |
| $\Delta = S\oplus\bar{S}$ | Dirac module, the two chiral halves |
| $\chi_{\mathrm{ad}} = i\tilde\Xi_{\mathrm{ad}}$, $\chi_{\mathrm{ad}}^2 = e_t$ | Central sign of the complexified algebra, the abstract chirality |
| $\chi = \mathrm{diag}(-I_2,I_2)$ on $\Delta$ | Its representative, the chirality operator of the grading |
| $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, the fifth reference-frame cell; its matrix image is $\chi$ |
| $\beta$ | Frame grading (large/small); $\{\chi,\beta\}=0$ |
| $\tilde{\nabla}$ | Biquaternionic gradient (the supercharge) |
| $\tilde{\nabla}^{\natural}$ | Quaternion conjugate gradient; $(\tilde\nabla)^{\dagger}=-\tilde\nabla^{\natural}$ |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta_Q$ | Series d'Alembertian (the Hamiltonian) |
| $\Delta_Q = \sum_k\partial^2/\partial Q_k^2$ | Spatial Laplacian |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Mass pair (one-sided equation, superalgebra) |
| $L_{\tilde\nabla^\natural}F = m\,\chi\bar{F}$ | Two-sided equation |
| $A = d/dx + W$, $A^\dagger = -d/dx + W$ | First-order factor and its adjoint |
| $W(x)$ | Superpotential (position-dependent mass) |
| $H_+ = A^\dagger A$, $H_- = A A^\dagger$ | Partner Hamiltonians |
| $V_\pm = W^2 \mp dW/dx$ | Partner potentials |
| $\{\mathcal{Q},\mathcal{Q}^\dagger\} = H$, $\mathcal{Q}^2 = 0$ | Supersymmetry algebra (nilpotent supercharge) |
| $\mathbb{D} = \mathcal{Q}+\mathcal{Q}^{\natural}$ | Dirac operator (the pair operator), $\mathbb{D}\Psi = m\Psi$, off-diagonal in the chiral basis |
| $\mathcal{Q}^{\natural}$ | Conjugate off-diagonal half; $\mathcal{Q}^{\dagger}=-\mathcal{Q}^{\natural}$, so $\mathbb{D}^{\dagger}=-\mathbb{D}$ |
| $a^{*}$, $a^{\natural}$, $\bar a$ | Conjugate for the adjoint ($i^{*}=-i$, $\vec e_k^{*}=-\vec e_k$), order-reversing conjugate, coefficient conjugate |
| $\mathbb{D}^2 = \Box\,I$ | Its square (the anticommutator) |
| $(-1)^F$ | Grading operator |
| $\mathrm{Ind} = \mathrm{Tr}\,(-1)^F = \dim\ker H_+ - \dim\ker H_-$ | Witten index |
| $H_D = -i\sigma_2\partial/\partial Q_x + \sigma_1 W$ | 1+1-dimensional Dirac Hamiltonian |
| $\tilde{Q} = \vec e_y\partial/\partial Q_x + iW\vec e_x$ | Biquaternion form of the reduced supercharge |
| $\tilde{Q}^2 = (-\partial^2/\partial Q_x^2+W^2)e_t - \frac{dW}{dx}(i\vec e_z)$ | Its square (central part plus $\mathbb{M}_+$ remainder) |
| $A_\omega = \boldsymbol\sigma\cdot(\vec p-im\omega\vec r)$ | Oscillator supercharge (written $\mathcal{Q}$ in the companion article) |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector of the four frame cells |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- E. Witten, "Dynamical breaking of supersymmetry," *Nuclear Physics B* **188** (1981) 513–554, for the introduction of supersymmetric quantum physics and the Witten index.
- E. Witten, "Constraints on supersymmetry breaking," *Nuclear Physics B* **202** (1982) 253–316, for the index and its invariance.
- P. Salomonson and J. W. van Holten, "Fermionic coordinates and supersymmetry in quantum mechanics," *Nuclear Physics B* **196** (1982) 509–531, for the supercharge formalism.
- F. Cooper and B. Freedman, "Aspects of supersymmetric quantum mechanics," *Annals of Physics* **146** (1983) 262–288, for the partner potentials and the factorisation.
- F. Cooper, A. Khare and U. Sukhatme, "Supersymmetry and quantum mechanics," *Physics Reports* **251** (1995) 267–385, for the systematic review, shape invariance, and the connection to the Dirac equation.
- L. E. Gendenshtein, "Derivation of exact spectra of the Schrödinger equation by means of supersymmetry," *JETP Letters* **38** (1983) 356–359, for shape invariance.
- M. F. Atiyah and I. M. Singer, "The index of elliptic operators: I," *Annals of Mathematics* **87** (1968) 484–530, for the index theorem that the chiral zero-mode count generalises.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Dirac operator, its square, and the chiral projectors used throughout.
