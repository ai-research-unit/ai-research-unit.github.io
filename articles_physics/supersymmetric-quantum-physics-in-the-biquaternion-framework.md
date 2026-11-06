# __Supersymmetric Quantum Physics in the Biquaternion Framework__

## Introduction

Supersymmetric quantum physics, introduced by Edward Witten in 1981, is the simplest realisation of a supersymmetry: a quantum system with a $\mathbb{Z}_2$ grading and a pair of conjugate supercharges $\mathcal{Q}$, $\mathcal{Q}^\dagger$ whose anticommutator is the Hamiltonian,

$$
\boxed{\;\{\mathcal{Q},\mathcal{Q}^\dagger\} = H, \qquad \mathcal{Q}^2 = 0, \qquad (\mathcal{Q}^\dagger)^2 = 0\;}.
$$

Its central structural fact is that the Hamiltonian factorises: the grading separates the states into two sectors, the Hamiltonian reads on them as the pair of **partner** operators $H_+$ and $H_-$, and $H_+ = A^\dagger A$, $H_- = A A^\dagger$ for a first-order operator $A$. The two spectra agree except possibly at zero energy. The partner potentials are $V_\pm = W^2 \mp dW/dx$, where $W$ is the superpotential, and the Witten index counts the imbalance of zero-energy states between the two sectors.

This article argues that the biquaternion framework is the natural home of that structure, for a reason that is visible in the first line. The relativistic quantum theory of spin $\tfrac12$ in this corpus rests on a **first-order** operator whose square is a scalar: the square of the gradient is the central d'Alembertian $\Box$. The massive equation is the chiral pair of *Operator and Calculus Conventions*, §*The Dynamics*, one member per value of the subscript, and the mass is the only term of the pair that names the other value. A central operator written as a pair whose members carry no mass is exactly a supersymmetric factorisation. The biquaternionic Dirac operator is therefore a supercharge, the two values of the subscript are the two graded sectors, and the mass is the term that the supersymmetry algebra reads as the superpotential. The correspondence is exact in the reduced theory, where it can be exhibited in closed form; in the full theory it is the structural principle that the companion articles on the Dirac square, the oscillator and the path integral all use.

**The grading is the subscript, and the subscript takes two values.** Chirality here is the subscript on an element and nothing else: an element is written $\tilde{Ξ}_{\mathrm{sp},L}$ or $\tilde{Ξ}_{\mathrm{sp},R}$, the value $L$ is the minus one and the value $R$ the plus one, and only the zero element carries both. The field of this article is one element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$; its two parts are its two values, and no second carrier is added. The cell whose two values these are is the volume cell of the frame, $\mathsf{V}_{\mathrm{vol}}=-iR_{\vec e_z}$ of *Special Element Conventions*, §*The Chirality Convention*, named once here and not used as a notation below.

**The two Dirac equations.** The corpus carries two forms of the Dirac equation, and this article keeps them apart. The **one-sided** equation is the chiral pair: both gradients act from the left, and the mass pairs the two values. It is the definition, and it is the form from which the supersymmetry is read. The **two-sided** equation is a single equation on an element $F\in\mathbb{B}$ in which the derivative acts from the left and the mass from the right through the chirality cell; it is the form in which the two-sided operator algebra acts by cells, and its mass term is antilinear in $F$. §*The One-Sided and the Two-Sided Equation* below splits the two, and the rest of the article uses the one-sided pair.

The article develops the correspondence in both directions. It first states the standard supersymmetric quantum physics and derives the partner potentials; it then identifies the biquaternionic first-order operator with the supercharge and the pair with the superalgebra; it exhibits the 1+1-dimensional realisation, where the superpotential is a position-dependent mass and the two partner potentials are the two values of a Hermitian element of $\mathbb{B}_{\Psi}$; it reads the Dirac oscillator as the exactly solvable relativistic realisation of the partner structure; and it identifies the Witten index with the imbalance of the zero modes between the two values. The quantised theory, the superfield formalism and the bona fide supersymmetric field theories are not treated; the subject here is the quantum physics, in the single-particle sense. The general graded-algebra framework behind the supercharges, the graded commutator and the boundary of what the biquaternion algebra supplies rather than imports is *The Superalgebra Reading and the Odd Extension in Biquaternionic Form*; the interpretation of the parity as the grading of the ambient algebra is *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form*.

## The Frame, the Values and the Equation

The frame is the coefficient basis, declared once with $e_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$, and every display below is read in it. The algebra, the sectors, the two conjugations, the gradient $\tilde{\nabla}$, the d'Alembertian $\Box$, the pair operator $\mathbb{D}$ and the cell are those of *Algebra and Element Conventions*, *Frame and Metric Conventions*, *Operator and Calculus Conventions* and *Matrix Representations Conventions*, and none of them is restated here.

The equation under study is the chiral pair that the corpus states as its dynamics (*Operator and Calculus Conventions*, §*The Dynamics*), printed once because the whole article is a reading of it:

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R} .
$$

Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The pair operator that writes it once is $\mathbb{D}$, of the same article, with $\mathbb{D}^2=\Box$, and the article uses the pair and the operator as that article fixes them. At $m=0$ the pair decouples into one equation per value, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=0$.

Two objects are this article's own, and each is defined where it is used: the reduced supercharge $\tilde{Q}$ of §*The 1+1-Dimensional Realisation* and the oscillator pair of §*The Dirac Oscillator*.

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

The supercharges are two operators of the graded space, and the rule is one clause each: $\mathcal{Q}$ carries a state of the $+$ sector to $A$ times it and annihilates the $-$ sector, and $\mathcal{Q}^\dagger$ carries a state of the $-$ sector to $A^\dagger$ times it and annihilates the $+$ sector. So

$$
\{\mathcal{Q},\mathcal{Q}^\dagger\} = H,
\qquad H = H_+ \text{ on the } + \text{ sector}, \quad H = H_- \text{ on the } - \text{ sector},
\qquad \mathcal{Q}^2 = (\mathcal{Q}^\dagger)^2 = 0 ,
$$

the squares vanishing because each supercharge annihilates the sector it lands in. The algebra is the simplest supersymmetry algebra: one conjugate supercharge pair, a $\mathbb{Z}_2$ grading $(-1)^F$ that is $+1$ on the $+$ sector and $-1$ on the $-$, and a Hamiltonian that is the anticommutator. Its two sectors are conventionally called bosonic and fermionic; in the biquaternion realisation below they are the two values of the subscript, and neither is the bosonic sector in any other sense.

Three consequences are standard and are used repeatedly below.

**Partner spectra.** $A$ carries the $+$ sector into the $-$ sector and $A^\dagger$ carries it back, so $H_+$ and $H_-$ have the same spectrum except possibly at zero energy. Concretely, if $H_+\tilde{Ξ}_{\mathrm{sp}} = A^\dagger A\tilde{Ξ}_{\mathrm{sp}} = E\tilde{Ξ}_{\mathrm{sp}}$ with $E\neq0$, then $\xi_{\mathrm{scl}} = A\tilde{Ξ}_{\mathrm{sp}}/\sqrt{|E|}$ satisfies $H_-\xi_{\mathrm{scl}} = E\xi_{\mathrm{scl}}$, and symmetrically. The two spectra are therefore degenerate level by level, with the possible exception of the ground states.

**Zero modes.** A zero-energy state of $H_+$ satisfies $A\tilde{Ξ}_{\mathrm{sp}} = 0$; a zero-energy state of $H_-$ satisfies $A^\dagger\xi_{\mathrm{scl}} = 0$. If $A$ has a normalisable zero mode, the supersymmetry is **unbroken** and $\dim\ker A \neq 0$; if neither $A$ nor $A^\dagger$ has one, the supersymmetry is **broken** and the index vanishes. The Witten index

$$
\mathrm{Ind} = \mathrm{Tr}\,(-1)^F = \dim\ker H_+ - \dim\ker H_- = \dim\ker A - \dim\ker A^\dagger
$$

is an integer when both kernels are finite, and it is invariant under continuous deformations of the parameters, which is why it is a topological (index) quantity. The kernels need not be finite — the Dirac oscillator below has infinitely many zero modes on one value of the subscript and none on the other — and the difference is then still the invariant count, though no longer a finite integer, so the invariance argument is applied to a family with finite kernels and the infinite case is read as a limit. A vanishing index does not by itself mean that the supersymmetry is broken: it means that the two kernels balance, which is compatible with both.

**The index is an index.** The equality $\mathrm{Ind} = \dim\ker A - \dim\ker A^\dagger$ is the statement that a deformation cannot create or destroy zero modes without creating them in pairs, one on each sector. It is the one-dimensional ancestor of the Atiyah–Singer index theorem, and it is the structure that the biquaternion Dirac operator carries in its zero modes on the two values.

## The Biquaternion Supercharge

The identification is now direct. The gradient is the first-order operator of the corpus and its square is the central d'Alembertian, so the pair $(\tilde{\nabla},\tilde{\nabla}^{\natural})$ is a supercharge pair in the sense of the previous section, and the dictionary has three entries.

**The grading is the subscript.** The value of the subscript is $L$ or $R$, one for each part of the field. The abstract $+$ sector of the previous section is read on one value and the $-$ sector on the other, and the assignment is the one the corpus records: $L$ is the minus value and $R$ the plus value (*Matrix Representations Conventions*, §*The Legacy Pauli Gamma Formulation*). The two values are exactly two, and only the zero element is both.

**The mass pair is the superalgebra.** The pair of the conventions is the massive equation, and each of its members multiplies the part with one value and equals a multiple of the part with the other, so the two sides of one member name the two values. The mass is the only term of the pair that names the other value. Read as one operator the same content is the pair operator $\mathbb{D}$, with $\mathbb{D}\tilde{Ξ}_{\mathrm{sp}}=k_m\tilde{Ξ}_{\mathrm{sp}}$ and $\mathbb{D}^2=\Box$; read as two equations it is the pair printed above. The square of the supercharge is the central Hamiltonian, and the mass is the number at which the pair is solved.

Three objects are held apart here. The nilpotent half is one member of the pair: applied where it lands, it annihilates, because the other member carries the field back. The operator $\mathbb{D}$ is the pair written once, and its square is central. And $m$ is a number: it multiplies the field in $\mathbb{D}\tilde{Ξ}_{\mathrm{sp}}=k_m\tilde{Ξ}_{\mathrm{sp}}$, and it becomes a term of the operator only when the same equation is written as a Schrödinger problem, where it multiplies the time cell of the frame. The two readings are one statement, that the mass is the term which pairs the two values.

**One sign, recorded once.** With respect to the sesquilinear form of the algebra the adjoint of the gradient is minus its quaternion conjugate, $(\tilde{\nabla})^{\dagger} = -\tilde{\nabla}^{\natural}$: the derivative contributes a minus, and the units contribute $e_t^{*}=e_t$ and $\vec e_k^{*}=-\vec e_k$, so the two minus signs cancel on the spatial part and the timelike term keeps its own. The pair operator is therefore anti-Hermitian, $\mathbb{D}^{\dagger} = -\mathbb{D}$, and $i\mathbb{D}$ is the Hermitian representative: the operator of the series is anti-Hermitian exactly as its first derivative is, and the factor of $i$ that repairs it is the one that also appears in the momentum of the coordinate form. The algebra is unaffected. Multiplying an anti-Hermitian operator by $i$ multiplies its square by $-1$, so the anticommutator of the repaired pair is $-\Box$ while the algebra's pairing is $+\Box$. The two differ by that one sign, which is the price of Hermiticity. The sign that does move is the one inside the d'Alembertian: on the material sector, where $Q_t=i c r'_t$, the d'Alembertian changes by the one sign of $i^2=-1$.

**The superpotential is the mass.** For a constant mass the parameter is an eigenvalue and the two partners coincide. For a position-dependent mass, $m\to W(Q_x)$, the mass is no longer an eigenvalue but a term of the operator, and the two partner Hamiltonians split, $H_\pm = -\partial^2/\partial R_x^2 + W^2 \mp dW/dx$. The superpotential is thus the possibly position-dependent mass, and the splitting of the partners is the statement that a spatially varying mass breaks the degeneracy between the two values of the subscript. This is the biquaternion form of the standard claim that the superpotential is the "potential" of the supersymmetric system: here the potential is a mass.

The dictionary is not an analogy imposed from outside; it is the statement that the biquaternion algebra's own structure — a first-order operator, a conjugate, a central square, and a pair whose members carry no mass — is the supersymmetry algebra written in the language of the corpus. What the supersymmetric quantum physics adds is the recognition that the graded object's square is the Hamiltonian, and that the zero modes of the graded operator are the invariant content.

### The One-Sided and the Two-Sided Equation

Two formulations carry the name *Dirac equation*, and the supersymmetry above is read from the first. The **one-sided** form is the chiral pair written with both gradients on the left,

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}
\qquad\text{(one-sided)},
$$

and the **two-sided** form is a single equation on an element, in which the derivative multiplies from the left and the mass from the right through the chirality cell. Written as the action it is, with no operator symbol, it is

$$
\tilde{\nabla}^{\natural}F = -i\,m\,\bar{F}\,\vec e_z
\qquad\text{(two-sided)} ,
$$

the right multiplier $\vec e_z$ carrying the cell of the two values and the conjugate $\bar F$ supplying the antilinearity. The second is the first restated on the algebra rather than on a pair: one equation instead of two, at the price of the coefficient conjugate.

| | One-sided equation | Two-sided equation |
|---|---|---|
| Equation | $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$ | $\tilde{\nabla}^{\natural}F = -i\,m\,\bar{F}\,\vec e_z$ |
| Multiplication | left, by $\tilde\nabla$ and $\tilde\nabla^\natural$ | left by the gradient, right by $\vec e_z$ |
| Field | $\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R} \in \mathbb{B}$ | $F\in\mathbb{B}$ |
| Mass | the pairing of the two values | the right multiplication by $\vec e_z$, applied to the conjugate field |
| Linearity | linear in the field | antilinear in the mass term |
| Use | the definition, and the supersymmetry of this article | the two-sided operator algebra |

The two-sided equation is a single equation on the algebra, and it exhibits the structure that the one-sided form states as a pair. Its derivative multiplies on the left and its mass on the right, so the two commute as actions, and the mass term is the chirality cell itself, applied to the conjugate field. That is the operator-algebra form of the same fact: the derivative is the one that carries no mass, and the mass is the term that carries the value. The price of the single equation is the coefficient conjugation $\bar{F}$, which supplies the antilinear part; the one-sided pair needs no conjugation and is the definition.

### The Supercharge Carries No Mass

The pair carries no mass term. Each member of the pair multiplies the part with one value and equals a multiple of the part with the other, so the two sides of one member name the two values, and no member of the pair names one value twice. The central $\Box$, by contrast, names no value at all, being a scalar. That is the graded-pair, even-Hamiltonian pattern of the abstract section, and the mass is what the pattern is read against.

Two consequences follow, and both are used below.

- The **supercharge is graded**: each member of the pair carries one value on its left and names the other value on its right, and the operator $\mathbb{D}$, which is the pair written once, is read with both members. Its square, being central, carries no value.
- The **Hamiltonian is even**: the square of the gradient is the central scalar, $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$, which carries each value to itself because it carries no label at all. It is the supersymmetric Hamiltonian $H$. The mass, in turn, is a number in the eigenvalue equation and the time cell of the frame in the Schrödinger form; as a term of the operator it is the one that pairs the two values.

In the biquaternion language the same statement reads: the pair names the two values of the subscript, the central $\Box$ names neither, and the mass is the pairing term. The superalgebra is the rule that a pair of graded objects multiplies to one that is not, realised concretely as $\tilde{\nabla}\tilde{\nabla}^{\natural}=\Box$, a scalar.

### The Two Gradings Must Not Be Conflated

The supersymmetric grading is the **value of the subscript**, and it is not the frame grading, the large/small grading of the time cell $iR_{\vec e_x}$ that the Foldy–Wouthuysen transformation diagonalises. The two cells anticommute:

$$
(iR_{\vec e_x})(-iR_{\vec e_z}) = R_{\vec e_z\vec e_x} = -R_{\vec e_x\vec e_z} = -(-iR_{\vec e_z})(iR_{\vec e_x}).
$$

A cell that commutes with the chirality cell carries each of the two values to itself, and a cell that anticommutes with it exchanges them. That is the whole content of the anticommutator, and it is why the two gradings sort every operator differently.

They sort the same Hamiltonian differently, and the sorting is complementary. Write the free Hamiltonian in the cells of the frame: its mass term is $mc^2$ times the time cell $iR_{\vec e_x}$, and its kinetic term is the sum $c\sum_k p_k\,(L_{\vec e_k}R_{\vec e_z})$ of the three velocity cells. The time cell anticommutes with the chirality cell, so the mass term exchanges the two values; the velocity cells commute with it, because a left multiplier commutes with a right one, and the kinetic term therefore carries each value to itself. Each grading therefore splits the Hamiltonian into one preserved and one exchanged piece, and the two gradings swap the pieces. Neither grading makes the whole of $H$ exchange the values, and that is not a defect of the notation but the reason the two are distinguished. The non-relativistic reduction removes the term that the frame grading exchanges, and the supersymmetry pairs the two values that the subscript separates.

The supercharge carries no mass. The operator $\mathbb{D}$ of the previous sections has no mass term, its square is the scalar $\Box$, and the mass enters only as the eigenvalue in $\mathbb{D}\tilde{Ξ}_{\mathrm{sp}} = k_m\tilde{Ξ}_{\mathrm{sp}}$, where it is the pairing of the two values. The pair (an operator whose two members name the two values, a central square) is exactly what the supersymmetry needs, and the label it needs is the subscript and not the frame grading. A reader who imports the frame intuition into the supersymmetry will expect the kinetic term to be the graded object and the mass the ungraded one, and will then read the supercharge as the wrong operator.

## The 1+1-Dimensional Realisation

The correspondence is exact, and verifiable in closed form, in the reduction to one spatial dimension with a position-dependent mass. This is the Dirac equation with a superpotential, and it is the bridge between the abstract algebra and the partner potentials.

Take the first-order element operator

$$
\tilde{Q} = \vec e_y\frac{\partial}{\partial R_x} + i\,W\,\vec e_x ,
$$

where $W$ is a real superpotential, a function of the coordinate alone. The second basis unit is the mass-like term and $\vec e_y$ is the derivative term. The square follows from the multiplication of the basis, $\vec e_y\vec e_x = -\vec e_z$, $\vec e_x\vec e_y = \vec e_z$ and $\vec e_x^2 = \vec e_y^2 = -e_t$, with the derivative acting on everything to its right, so that the only surviving term of its action on $W$ is the derivative of $W$:

$$
\tilde{Q}^2 = \left(-\frac{\partial^2}{\partial R_x^2} + W^2\right)e_t - i\,\frac{dW}{dx}\,\vec e_z
= \left(-\frac{\partial^2}{\partial R_x^2} + W^2\right)e_t - \frac{dW}{dx}\,(i \vec e_z).
$$

Both terms of $\tilde Q$ are Hermitian: the derivative and $\vec e_y$ each contribute a minus, and $i\vec e_x$ is Hermitian because $(i\vec e_x)^{*} = i^{*}\vec e_x^{*} = (-i)(-\vec e_x) = i\vec e_x$.

**The check.** The identity was verified on $121$ points of $[-6,6]$ (step $h=0.1$) with the kink superpotential $W = \tanh x$. Writing $D$ for the central difference and $D\circ D$ for its square, the discretised form of $\tilde Q^2$ agreed with $(-D\circ D + W^2)e_t - \frac{dW}{dx}(i\vec e_z)$ to $7\times10^{-15}$ on the whole grid, and the operator limit $[D,W]\to dW/dx$, applied to a smooth test function, converged at second order: the errors at successive halvings of the step, from $121$ to $241$ to $481$ points, stood in the ratios $3.97$ and $3.99$, as a commutator with a central difference must.

Two features of this square are the algebraic content of the section.

- The **central part** is $(-\partial^2/\partial R_x^2+W^2)e_t$: it is the common Hamiltonian of the two values, and it is central because the cross terms of the two factors cancel exactly as in the free case.
- The **splitting** is $-\frac{dW}{dx}(i\vec e_z)$, and $i\vec e_z$ is a Hermitian biquaternion with $(i\vec e_z)^2 = i^2\vec e_z^2 = +e_t$, an element of $\mathbb{B}_{\Psi}$ with the two values $\pm1$. The two values of the square — the two partner potentials — are therefore $-\partial^2/\partial R_x^2+W^2\mp dW/dx$, and each belongs to one of the two values of the subscript.

The superpotential is thus the coefficient of the mass-like term, the partner splitting is the value of a Hermitian element, and the two partner Hamiltonians are the two values of a single algebra-valued square. This is the cleanest sense in which the biquaternion framework **contains** supersymmetric quantum physics: the partner structure is the two values of the $\mathbb{B}_{\Psi}$ remainder of a first-order operator's square.

## The Dirac Oscillator as a Supersymmetric System

The exactly solvable relativistic model of the companion article *The Dirac Oscillator in Biquaternionic Form* is the most explicit three-dimensional realisation of the correspondence, and it makes the zero-mode and index structure concrete.

That article eliminated the second value of the field and produced two conjugate first-order actions, written there $\mathcal{Q}_\pm$ and called $A_\omega,A_\omega^\dagger$ here so as not to collide with the supercharge:

$$
A_\omega: Q\longmapsto\sum_k\vec e_k\,\bigl(p_k-im\omega Q_k\bigr)\,Q\,\vec e_z,
\qquad
A_\omega^\dagger: Q\longmapsto\sum_k\vec e_k\,\bigl(p_k+im\omega Q_k\bigr)\,Q\,\vec e_z .
$$

Their products are the exact operator identities of that article,

$$
A_\omega^\dagger A_\omega = \vec p^2 + m^2\omega^2\vec r^2 - \dfrac{3\hbar^2\omega\,k_m}{c} - 2m\omega\,S
= \dfrac{2\hbar^2\omega\,k_m}{c}\left(N - \frac{S}{\hbar}\right),
$$

and

$$
A_\omega A_\omega^\dagger = \dfrac{2\hbar^2\omega\,k_m}{c}\left(N + 3 + \frac{S}{\hbar}\right),
\qquad
S=\sum_k L_{\mathrm{orb},k}\,\tilde S_k ,
$$

where $N$ is the oscillator number operator and $S$ is the spin–orbit element. The constant terms differ, $-\dfrac{3\hbar^2\omega\,k_m}{c}$ against $+\dfrac{3\hbar^2\omega\,k_m}{c}$, and the two products differ by their commutator, which carries the constant and twice the spin–orbit term. The commutator is not central, and the two operators are nevertheless isospectral away from zero, because $A_\omega$ intertwines them: $A_\omega(A_\omega^\dagger A_\omega) = (A_\omega A_\omega^\dagger)A_\omega$. Both identities were checked on the truncated oscillator space of the states with $N\le4$ (thirty-five bosonic states, seventy with the spin), where they held to $10^{-15}$ in the bulk of the basis, that is for every state with $N\le2$; the deviation in the outermost shell is the expected artefact of a truncation that realises the commutator of the ladder only below its ceiling. $A_\omega$ annihilates the vacuum exactly.

The pair $(A_\omega,A_\omega^\dagger)$ is a supersymmetric pair in the sense of the first section: $H_+ = A_\omega^\dagger A_\omega$ and $H_- = A_\omega A_\omega^\dagger$ are partner Hamiltonians, and their non-zero spectra agree. The zero modes of $A_\omega$ are the aligned states with $n_r = 0$, and they exist for every orbital quantum number $l$, so $\dim\ker A_\omega = \infty$; the conjugate operator has no zero modes at all, because $A_\omega A_\omega^\dagger$ has strictly positive eigenvalues. The imbalance of zero modes is therefore infinite: the supersymmetry is unbroken, and the ground level of the Dirac oscillator is infinitely degenerate at $E = \pm mc^2$. The infinite degeneracy derived in the oscillator article is thus not an accident of that model; it is the zero-mode degeneracy that a factorised first-order operator with unbroken supersymmetry possesses.

The oscillator's spectrum,

$$
E^2 = m^2c^4 + \dfrac{2\hbar^2\omega\,k_m}{c} c^2\left(N - \frac{S}{\hbar}\right),
\qquad
E^2 = m^2c^4 + 4m\hbar\omega c^2\,n_r \ \ (s_{\mathrm{tot}} = l+\tfrac12),
$$

is the spectrum of $H_+ = A_\omega^\dagger A_\omega$. The first line is the general form, and the second is its aligned branch, $S/\hbar = l$, rewritten with $N = 2n_r+l$; that branch vanishes at $n_r = 0$, which is the infinitely degenerate level at $E = \pm mc^2$. The anti-aligned branch, $S/\hbar = -(l+1)$, gives $E^2 = m^2c^4 + \dfrac{2\hbar^2\omega\,k_m}{c} c^2(2n_r+2l+1)$.

The two branches are the two values of the spin–orbit element, not the two graded sectors. The partner $H_- = A_\omega A_\omega^\dagger$ has two towers as well, $\dfrac{2\hbar^2\omega\,k_m}{c}(2n_r+2l+3)$ aligned and $4m\hbar\omega(n_r+1)$ anti-aligned; these are the two towers of $H_+$ with the branches exchanged and $n_r$ advanced by one. At fixed excitation the statement is exact: the spectrum of $H_-$ on the states of $N$ excitations is the spectrum of $H_+$ on the states of $N+1$ excitations with the zero modes removed. The exchange of branches is forced by the intertwiner, since $A_\omega$ commutes with the total angular momentum, lowers $N$ by one and is graded, so it changes $l$ by one unit and cannot keep the branch label.

The correspondence also clarifies what is and is not supersymmetric about the free theory. The free biquaternionic Dirac operator has $\mathbb{D}^2 = \Box$ with $H_+ = H_-$: the pair is degenerate, the index vanishes, and what remains of the supersymmetry is the exact degeneracy, not a protected zero mode. Adding the non-minimal oscillator term shifts the two partners by opposite constants and opposite spin–orbit terms, and produces the zero modes. The mass is what makes the grading physically meaningful, and the oscillator term is what makes the two partners differ.

## The Witten Index and the Zero Modes

The index is the invariant that ties the supersymmetric quantum physics to the value of the subscript on the biquaternion Dirac operator, and the relation is worth stating precisely.

For the free massless Dirac operator the grading is the value of the subscript, and a zero mode is annihilated by its own member of the pair: the part with one value satisfies $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = 0$ and the part with the other satisfies $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = 0$. The index

$$
\mathrm{Ind} = \dim\ker H_+ - \dim\ker H_- = \dim\ker\tilde{\nabla}^{\natural} - \dim\ker\tilde{\nabla}
$$

counts the imbalance of the zero modes between the two values — the states annihilated by $\tilde{\nabla}^{\natural}$, which are the kernel of $H_+=\tilde\nabla\tilde\nabla^\natural$, minus the states annihilated by $\tilde{\nabla}$, the kernel of $H_-=\tilde\nabla^\natural\tilde\nabla$ — and it is invariant under continuous deformations of the geometry and of the mass. In the flat four-dimensional theory with a constant mass there are no normalisable zero modes and the index vanishes; it becomes non-trivial when the mass is position-dependent, as the kink of the 1+1-dimensional realisation is, or when the background is topologically non-trivial, as an instanton or a vortex is, in which case the zero modes and the index are the content of the Atiyah–Singer theorem.

In the biquaternion framework the index has a simple interpretation. The grading is the value of the subscript, taking two values and no more; the supercharge is the pair of the gradient, whose two members name the two values; and the index is the imbalance in the dimensions of the two kernels. The mass is the term that pairs the two values, and the index is what survives when the mass is allowed to vary: an invariant of the graded object that no continuous deformation removes. That is the precise sense in which the biquaternion Dirac operator is a supersymmetric quantum-mechanical system whose index is a topological invariant of the value of the subscript.

Two caveats keep the statement in scope. First, the index discussed here is the index of the **single-particle** Dirac operator; the quantised-field index and its anomalies belong to *Biquaternion Quantum Fields*. Second, the correspondence developed here is between the biquaternion Dirac theory and **quantum physics**, not between biquaternions and four-dimensional supersymmetric field theory; the superalgebra $\{\mathcal{Q},\mathcal{Q}^\dagger\}=H$ with a single supercharge pair is the quantum-mechanical $\mathcal{N}=1$ algebra, and it is the one the corpus's first-order structure realises.

## Shape Invariance and Exactly Solvable Partners

A final standard thread connects the factorisation to solvability, and the biquaternion realisation explains its algebraic origin. A pair of partner potentials is **shape invariant** when the two differ only by a change of parameters plus a constant,

$$
V_-(x;a_1) = V_+(x;a_2) + R(a_1),
$$

with $a_2$ a function of $a_1$ and $R$ a constant for each step. When this holds, the partner Hamiltonians are isospectral except for the ground state, and the spectrum can be generated algebraically. The oscillator, the Coulomb problem and the Morse potential are the standard examples; the Dirac oscillator of the previous section is a relativistic one.

In the biquaternion framework shape invariance has a direct interpretation. The superpotential is the mass, or the mass profile, and a change of the parameter $a$ is a change of that profile; the constant $R$ is the shift produced by the central part of the squared operator. The partner Hamiltonians are the two values of the squared operator, whose splitting is the Hermitian remainder $-\frac{dW}{dx}(i\vec e_z)$, and shape invariance is the statement that a one-parameter change of $W$ maps one value into the other up to a shift. The exactly solvable problems of the corpus — the oscillator of the companion article and [The Hydrogen Atom in Biquaternionic Form: The Non-Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-non-relativistic-case.html), together with their non-relativistic limits — are the cases where this change of parameters closes on itself, which is why they are exactly solvable. The algebraic origin of solvability, in this interpretation, is that the square of the first-order operator is central plus a single Hermitian element whose two values are the partners.

**The isospectral family.** The partner pair is the corpus's simplest isospectral family: $H_+=A^{\dagger}A$ and $H_-=AA^{\dagger}$ agree away from zero, differ at zero where the Witten index counts the imbalance, and are carried into one another by the change of the mass profile that shape invariance describes. The element-level version of the same statement, with the mass as a root of a general element, is [The Roots of a General Element: Mass, Frames and the Mass Shell](the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html).
## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and a cell is $L_{a}R_{b}$.

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}, &\gamma_1 &= iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}, &\gamma_3 &= iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}, &\gamma_1 &= iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}, &\gamma_3 &= iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}.
\end{aligned}
$$

The squares follow from $(L_{a}R_{b})^2=L_{a^2}R_{b^2}$ and $\vec e_k^2=-e_t$: $\gamma_0^2=+L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}$ and $\gamma_k^2=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}$, so the four carry $\varepsilon=(1,-1,-1,-1)$, and $\{L_{a}R_{b},L_{c}R_{d}\}=L_{ac}R_{db}+L_{ca}R_{bd}$. A cell is a pure tensor in $\mathrm{End}(\mathbb{B})\cong\mathbb{B}\otimes\mathbb{B}_{\mathrm{opp}}$, and the cells span the whole operator algebra over $\mathbb{C}$, so every operator on the module is a finite sum of cells. A single cell is not a projection: $L_{a}R_{b}$ is invertible whenever $a$ and $b$ are invertible, so it has rank four, and the operators of this article are written as short sums of cells rather than as one.

$\gamma_5$ is the reference-frame cell of the chirality and $\gamma_0$ the reference-frame time cell, and two identifications close the article. The chirality sign of the previous sections, $\xi=\mathrm{diag}(-I_2,I_2)$ on $\Delta$, has $\gamma_5$ as its cell: the cell and the array are the same operator in the two representations, while the central sign $\xi_{\mathrm{ad}}=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\xi_{\mathrm{ad}}^2=e_t$ — is the algebra's definition of it. And $\gamma_0$ is off-diagonal on the Dirac module, so the frame grading $\beta$ of §*The Two Gradings Must Not Be Conflated* is $\gamma_0$. The anticommutation that separates the two gradings is then a one-line computation on the cells,

$$
\gamma_0\gamma_5 = (iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x})(-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}) = (-i^2)\,L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z\vec e_x} = L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z\vec e_x} = -L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x\vec e_z} = -\gamma_5\gamma_0,
$$

In the axis-free display:

$$
\gamma_0\gamma_5 = (iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x})(-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}) = (-i^2)\,L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z\vec e_x} = L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z\vec e_x} = -L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x\vec e_z} = -\gamma_5\gamma_0,
$$

the two coefficients multiplying to $(-i)(i) = -i^2 = +1$, and the minus coming from the right multipliers, whose order the composition rule reverses: $R_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_z} = R_{\mathrm{pau},\vec e_z\vec e_x} = -R_{\mathrm{pau},\vec e_x\vec e_z}$, since $\vec e_z\vec e_x = -\vec e_x\vec e_z$.

The dictionary is complex-linear; over $\mathbb{R}$ the products of the gammas span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Supersymmetric quantum physics is the algebra $\{\mathcal{Q},\mathcal{Q}^\dagger\} = H$, $\mathcal{Q}^2 = (\mathcal{Q}^\dagger)^2 = 0$, with a $\mathbb{Z}_2$ grading, a pair of partner Hamiltonians $H_+ = A^\dagger A$, $H_- = A A^\dagger$ for $A = d/dx + W$, partner potentials $V_\pm = W^2 \mp dW/dx$, and the Witten index $\mathrm{Ind} = \dim\ker H_+ - \dim\ker H_-$.

The biquaternion framework supplies this structure natively. The biquaternionic Dirac operator is the gradient $\tilde{\nabla}$, whose square is the central $\Box$; the grading is the value of the subscript, which is $L$ or $R$ and nothing else, with $L$ the minus value; the supercharge is the pair operator $\mathbb{D}$ with $\mathbb{D}^2=\Box$; the superalgebra is the chiral pair, one member per value, in which the mass is the only term that names the other value; and the free theory has $H_+ = H_- = \Box$, a balanced spectrum with a vanishing index. The two-sided form of the same equation, $\tilde{\nabla}^{\natural}F = -i\,m\,\bar{F}\,\vec e_z$, multiplies the derivative on the left and $\vec e_z$ on the right, and exhibits the mass as the term that carries the cell of the two values.

The correspondence is exact in the 1+1-dimensional reduction with a superpotential $W$: the operator $\tilde{Q} = \vec e_y\partial/\partial R_x + iW\vec e_x$ squares to the central part $(-\partial^2/\partial R_x^2+W^2)e_t$ plus the Hermitian remainder $-\frac{dW}{dx}(i\vec e_z)$, whose two values are the partner potentials. The identity was checked by finite-difference computation on $121$ points of $[-6,6]$ (step $h=0.1$) with the kink superpotential $W = \tanh x$: it held to $7\times10^{-15}$ on the whole grid, and the operator limit $[D,W]\to dW/dx$ converged at second order in $h$, the error falling by a factor close to four at each halving of the step.

The Dirac oscillator is the three-dimensional relativistic realisation: the pair $A_\omega$, $A_\omega^\dagger$ of the companion article has infinitely many zero modes on one side and none on the other, $A_\omega A_\omega^\dagger = \dfrac{2\hbar^2\omega\,k_m}{c}(N+3+S/\hbar)$ has no zero mode, the supersymmetry is unbroken, and the infinite degeneracy of the ground level at $E = \pm mc^2$ is the zero-mode degeneracy of the factorisation. The Witten index is the imbalance of the zero modes between the two values, an invariant of the grading; and shape invariance, the algebraic origin of exact solvability, is the statement that the two values of the Hermitian remainder can be mapped into one another by a change of the mass profile.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $e_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, with $i^2=-1$ |
| $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The two values of the subscript; $L$ is the minus value, $R$ the plus value |
| $\mathsf{V}_{\mathrm{vol}}=-iR_{\vec e_z}$ | The chirality cell of the frame, whose two values the subscript takes |
| $iR_{\vec e_x}$ | The time cell of the frame, the frame grading |
| $\tilde{\nabla}$ | Biquaternionic gradient (the supercharge) |
| $\tilde{\nabla}^{\natural}$ | Quaternion conjugate gradient; $(\tilde\nabla)^{\dagger}=-\tilde\nabla^{\natural}$ |
| $\Box$ | The d'Alembertian of the series (the Hamiltonian), the square of the gradient |
| $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$ | The chiral pair (one-sided equation, superalgebra) |
| $\tilde{\nabla}^{\natural}F = -i\,m\,\bar{F}\,\vec e_z$ | Two-sided equation |
| $A = d/dx + W$, $A^\dagger = -d/dx + W$ | First-order factor and its adjoint |
| $W(x)$ | Superpotential (position-dependent mass) |
| $H_+ = A^\dagger A$, $H_- = A A^\dagger$ | Partner Hamiltonians |
| $V_\pm = W^2 \mp dW/dx$ | Partner potentials |
| $\{\mathcal{Q},\mathcal{Q}^\dagger\} = H$, $\mathcal{Q}^2 = 0$ | Supersymmetry algebra (nilpotent supercharge) |
| $\mathbb{D}$ | The pair operator, $\mathbb{D}\tilde{Ξ}_{\mathrm{sp}} = k_m\tilde{Ξ}_{\mathrm{sp}}$ with $\mathbb{D}^2=\Box$ |
| $a^{*}$, $a^{\natural}$, $\bar a$ | Conjugate for the adjoint ($i^{*}=-i$, $\vec e_k^{*}=-\vec e_k$), order-reversing conjugate, coefficient conjugate |
| $(-1)^F$ | Grading operator |
| $\mathrm{Ind} = \mathrm{Tr}\,(-1)^F = \dim\ker H_+ - \dim\ker H_-$ | Witten index |
| $\tilde{Q} = \vec e_y\partial/\partial R_x + iW\vec e_x$ | Reduced supercharge (1+1 dimensions) |
| $\tilde{Q}^2 = (-\partial^2/\partial R_x^2+W^2)e_t - \frac{dW}{dx}(i\vec e_z)$ | Its square (central part plus $\mathbb{B}_{\Psi}$ remainder) |
| $A_\omega$, $A_\omega^\dagger$ | Oscillator pair (written $\mathcal{Q}_\pm$ in the companion article) |
| $S=\sum_k L_{\mathrm{orb},k}\tilde S_k$ | Spin–orbit element of the oscillator, with the two values $\hbar l$ and $-\hbar(l+1)$ |
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
