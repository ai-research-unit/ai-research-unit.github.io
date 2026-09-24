# __The Qutrit Problem: Three-Level Systems Outside the Biquaternion Algebra__

## Introduction

The biquaternion algebra is the algebra of a two-state system. Its defining module is two-dimensional, its observables are the Hermitian elements of $\mathbb{B}$, its states are the positive trace-one elements of $\mathbb{M}_+$, and its state space is the Bloch ball, the trace-one slice of the future light cone of the norm form. Every one of these statements rests on the same number: the module has two levels.

Three-level systems are the next step, and they are physically unavoidable: a spin-one atom, a qutrit, a three-level ladder, the internal states of a nitrogen-vacancy centre. The question this article addresses is whether the biquaternion algebra can describe them, and if not, exactly where the obstruction lies. The answer has two halves, and both are useful.

The obstruction is structural and can be located precisely. The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, so every unital finite-dimensional module is a direct sum of copies of the two-dimensional defining module, and a three-dimensional unital module does not exist. Three further ceilings point at the same place: a nilpotent element of $\mathbb{B}$ has square zero, so the algebra's own raising operator cannot climb more than one step; the identity of $\mathbb{B}$ splits into at most two orthogonal idempotents, so the algebra cannot host a three-outcome projective measurement; and the three-dimensional space of the adjoint representation carries an action of the *Lie algebra* $\mathfrak{su}(2)$ but not of the algebra $\mathbb{B}$, because the adjoint action is a derivation, not a multiplication. Each of these is a different face of the same fact: **the algebra has two levels, and the third is not inside it.**

What is available is the tensor square. Two fundamental systems carry four levels, and the four split into three plus one, the symmetric square and the antisymmetric square. The symmetric part is exactly the qutrit: it is the spin-one multiplet of the total angular momentum of the two fundamental systems, its operators are the symmetric combinations of the two one-particle operators, and it is the sector in which the coupling of two fundamental systems is expressed. The price is explicit: one extra level, which must be *projected out*, and a doubling of the algebra. The qutrit is therefore not outside the framework; it is outside the algebra, and inside its tensor square.

The article is organised as follows. The defining module and its classification are recalled. The three obstructions are then stated and proved: the level count, the nilpotency ceiling, and the idempotent ceiling. The adjoint representation is then examined, and the sense in which the three-dimensional space of the algebra is a Lie-algebra module but not an algebra module is made precise. The construction of the qutrit in the tensor square follows, with its cost. A short section gives the general counting for higher spin, and a closing section states what happens to the algebra's specific virtues — the quadratic norm form, the Lorentzian positive cone, the zero divisors — when the level count is raised.

## The Defining Module: Two Levels

The classification is stated in the companion article *Biquaternion Representation Theory* and is used here as given.

**Theorem.** *Let $V=\mathbb{C}^2$ be the space of column vectors with the natural action of $\mathbb{B}\cong M_2(\mathbb{C})$. Every finite-dimensional $\mathbb{B}$-module is isomorphic to a direct sum of copies of $V$,*

$$
M\;\cong\;V^{\oplus k},\qquad \dim_{\mathbb{C}}M=2k ,
$$

*and $V$ is the only simple module. Over $\mathbb{R}$ the same conclusion holds with $S=\mathrm{Res}_{\mathbb{C}/\mathbb{R}}V$, of real dimension $4$.*

Two consequences are used constantly. First, the dimension of every module is even. Second, every module is completely reducible and the multiplicity $k$ determines it up to isomorphism. The algebra is simple and its centre acts by scalars, so on any unital module the identity of $\mathbb{B}$ acts as the identity and the dimension is twice the multiplicity.

The element that makes the qubit work is not the dimension of the module by itself but the coincidence of three structures on the same two-dimensional space: $V$ is at once a module over the algebra $\mathbb{B}$, a module over the Lie algebra of its anti-Hermitian elements, and the space on which the Lorentz group acts through $SL(2,\mathbb{C})$. For the qubit all three actions are the same action, and this is why a single algebra element both generates a rotation and carries a probability amplitude.

## Three Obstructions

### No three-dimensional module

A three-level system requires three independent states, hence a three-dimensional complex vector space. The classification says that no unital $\mathbb{B}$-module of dimension three exists: the dimension is $2k$.

If the requirement of unitarity of the action is dropped, a three-dimensional action exists, and it is unique up to isomorphism. Take $\mathbb{C}^3=\mathbb{C}^2\oplus\mathbb{C}$ and let the algebra act as

$$
x\cdot(u\oplus w)=xu\oplus 0 ,
$$

that is, by an arbitrary $2\times2$ block and by zero on the third level; in matrices, the image of $\mathbb{B}$ in $M_3(\mathbb{C})$ is the block-diagonal subalgebra $M_2(\mathbb{C})\oplus 0$,

$$
x\;\longmapsto\;\begin{pmatrix} x & 0\\ 0 & 0\end{pmatrix}.
$$

The embedding is a homomorphism, but the third level is inert: every algebra element annihilates it. The operator that the physically interesting quantities require, the shift connecting the third level to the others,

$$
\begin{pmatrix}0&0&0\\0&0&0\\1&0&0\end{pmatrix}\quad\text{or}\quad \begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},
$$

is not in the image, as the block form shows. The image is an eight-real-dimensional subalgebra of the eighteen-real-dimensional $M_3(\mathbb{C})$, and the ten real dimensions outside it are precisely the operators that involve the third level: eight that connect it to the other two, and two — one complex direction — that act within it.

This is the sharp form of the obstruction: **$\mathbb{B}$ can act on a three-level space only as a qubit plus a spectator, and the spectator is invisible to the algebra.** A qutrit, in which all three levels are connected by the operators of the theory, is not a module of $\mathbb{B}$.

The embedding is also unique up to conjugation, which rules out a cleverer three-dimensional action.

**Proposition.** *Let $\phi:\mathbb{B}\to M_3(\mathbb{C})$ be an algebra homomorphism with nonzero image. Then the image is isomorphic to $M_2(\mathbb{C})$, and up to conjugation in $M_3(\mathbb{C})$ it is the block $M_2(\mathbb{C})\oplus0$. Consequently the operators of $M_3(\mathbb{C})$ that annihilate the third level and preserve the two-level subspace $\mathbb{C}^2\oplus0$ are exactly the image, and the ten-real-dimensional complement lies outside it: eight real directions that connect the third level to the other two, and two that act within the third level.*

*Proof.* The algebra $M_2(\mathbb{C})$ is simple, so a nonzero homomorphism has zero kernel and its image is isomorphic to $M_2(\mathbb{C})$; the image is therefore a simple subalgebra of $M_3(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$. By the double centraliser theorem, a subalgebra of $M_n(\mathbb{C})$ isomorphic to $M_k(\mathbb{C})$ with $k<n$ is conjugate to $M_k(\mathbb{C})\oplus0$. The dimension count is $\dim_{\mathbb{R}}M_3(\mathbb{C})-\dim_{\mathbb{R}}M_2(\mathbb{C})=18-8=10$. $\square$

The ten missing dimensions are the operators that involve the third level, and the count is the quantitative form of the spectator statement.

### No cubic nilpotent: the ladder stops at two levels

The obstruction also has a nilpotency form, which is the most concrete way to see it.

A two-level ladder is built from a raising operator $S_+$ with

$$
S_+^2=0 ,
$$

so that two applications annihilate every state: the ladder has one rung. In the algebra this is not an accident of the matrix realisation but follows from the Cayley–Hamilton identity. For any $2\times2$ matrix $n$ with $\mathrm{Tr}(n)=0$ and $\det(n)=0$,

$$
n^2-\mathrm{Tr}(n)\,n+\det(n)\,I=0\quad\Longrightarrow\quad n^2=0 ,
$$

so every nilpotent element of $\mathbb{B}$ has square zero. In the algebra itself the same identity reads $(ie_1-e_2)^2=0$ for the raising element of the fundamental module, and $(\tilde S_+)^2=0$ for the spin operator.

A three-level ladder, by contrast, has two rungs and is nilpotent of index three: the spin-one raising operator satisfies

$$
J_+\neq0,\qquad J_+^2\neq0,\qquad J_+^3=0 ,
$$

which was verified explicitly, and the shift matrix above has the same property. In the Jordan picture a ladder over $d$ levels is generated by a single block of size $d$, and the powers $S,S^2,\dots,S^{d-1}$ are $d-1$ linearly independent raising directions; $\mathbb{B}$ has blocks of size at most two, so its chain is $S\neq0$, $S^2=0$, one rung. The index of nilpotency of the ladder equals the number of levels minus one, and since $\mathbb{B}$ contains no element of nilpotency index three, no chain of three levels can be generated inside the algebra: the third level would require a second, independent step.

### At most two orthogonal idempotents

A projective measurement with three outcomes is a resolution of the identity into three mutually orthogonal idempotents,

$$
P_1+P_2+P_3=e_0,\qquad P_iP_j=\delta_{ij}P_i .
$$

In $\mathbb{B}\cong M_2(\mathbb{C})$ this is impossible: idempotents have ranks $1$ or $2$, orthogonal idempotents have additive ranks, and $\mathrm{rank}(e_0)=2$, so at most two nonzero terms can occur. A three-outcome projective measurement is a three-level structure, and the algebra has room only for two.

The statement is about *projective* measurements and should not be overstated. A three-outcome POVM — three positive elements $E_1+E_2+E_3=e_0$ without orthogonality — does exist in $\mathbb{B}$; the trine measurement of the qubit is the standard example. What does not exist is the sharp, repeatable three-outcome measurement that a qutrit's standard basis measurement represents. Three orthogonal idempotents summing to the identity exist in $M_3(\mathbb{C})$, as one checks immediately, and they are the minimal form of the obstruction.

## The Adjoint Representation Is a Lie-Algebra Module

There is a three-dimensional space in the framework that carries spin one: the traceless part $W=\operatorname{span}_\mathbb{C}\{ie_1,ie_2,ie_3\}$ of $\mathbb{B}$, on which the adjoint action

$$
\mathrm{ad}_{\tilde S_k}(ie_l)=[\tilde S_k,ie_l]=i\hbar\,\epsilon_{klm}\,(ie_m)
$$

is a spin-one angular momentum. Since a three-dimensional module of $\mathbb{B}$ does not exist, something must distinguish this action from a module action, and the difference is exactly the multiplicativity of the map $x\mapsto\mathrm{ad}_x$.

A representation of the *algebra* requires $\mathrm{ad}_{xy}=\mathrm{ad}_x\mathrm{ad}_y$. The adjoint action is a derivation instead,

$$
\mathrm{ad}_x(yz)=\mathrm{ad}_x(y)\,z+y\,\mathrm{ad}_x(z),
$$

and derivations are not multiplications. The failure is explicit. In the matrix realisation, with $ie_1=\sigma_1$ and $ie_2=\sigma_2$,

$$
\mathrm{ad}_{ie_1}\bigl(\mathrm{ad}_{ie_1}(ie_2)\bigr)=[ie_1,[ie_1,ie_2]]=+4\,ie_2\neq0,\qquad
\mathrm{ad}_{(ie_1)^2}(ie_2)=[e_0,ie_2]=0 .
$$

So $\mathrm{ad}_{ie_1}^2\neq\mathrm{ad}_{(ie_1)^2}$, and the map $x\mapsto\mathrm{ad}_x$ is not an algebra homomorphism. It is a **Lie-algebra** homomorphism: the linear span of the $ie_k$ with the commutator is $\mathfrak{su}(2)$, and the adjoint action makes $W$ a module over $\mathfrak{su}(2)$, equivalently over its universal enveloping algebra $\mathcal{U}(\mathfrak{su}(2))$ and over the group $SU(2)$.

That is the precise location of the three-level structure. The qutrit is a module of $\mathfrak{su}(2)$ — or of $SU(2)$, whose three-dimensional irreducible representation is the adjoint — and not a module of the associative algebra $\mathbb{B}$. The companion article *Biquaternion Representation Theory* records the same fact from the other side: all derivations of $\mathbb{B}$ are inner and $\mathrm{Der}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$, so the adjoint action sees only the six-real-dimensional Lie algebra, not the eight-real-dimensional associative algebra. For the qubit the distinction is invisible, because the defining module is a module of both.

The three-dimensional representation is therefore available in the framework's *kinematics*: angular momenta, rotations, Clebsch–Gordan coefficients, tensor operators, and the state-space geometry of a spin-one system all make sense. What is not available is a qutrit *algebra of observables* sitting inside $\mathbb{B}$ itself, because that would be a three-dimensional module of $M_2(\mathbb{C})$.

## The Absent Dynamical Algebra

A second way to see the obstruction is to count the operations available on the three levels.

The observables of the algebra are the Hermitian elements of $\mathbb{M}_+$, a real vector space of dimension four; their unitary exponentials form $U(2)$, of real dimension four, which is the full group of unitary operations on two levels. A three-level system admits $U(3)$, of real dimension nine, and its traceless part $\mathfrak{su}(3)$ has dimension eight. The comparison is decisive at every level of structure:

$$
\dim_{\mathbb{R}}\mathbb{M}_+=4<9=\dim_{\mathbb{R}}\mathfrak{u}(3),\qquad
\dim_{\mathbb{R}}\mathbb{B}=8<9,\qquad
\dim_{\mathbb{R}}\mathrm{Der}(\mathbb{B})=6<8=\dim_{\mathbb{R}}\mathfrak{su}(3) .
$$

Even the whole algebra, regarded as a real Lie algebra of dimension eight, is too small to contain $\mathfrak{u}(3)$, of dimension nine, and its Lie algebra of derivations, of dimension six, is smaller than $\mathfrak{su}(3)$, of dimension eight. No copy of the qutrit's dynamical algebra fits inside $\mathbb{B}$. What $\mathbb{B}$ supplies on the qutrit sector is the spin subgroup: the rotations generated by the adjoint action form $SU(2)$, of dimension three, acting transitively on the coherent states. That is the group of classical rotations of a spin-one system, and it is exactly the group that the framework's adjoint action can reach.

The remaining operations of $U(3)$ — those that change the alignment of a state without changing its spin direction, and those that mix the two transition frequencies independently — are not in $\mathbb{B}$. They are available in the tensor square, because the qutrit observables there generate $M_3(\mathbb{C})$, and exponentiating its anti-Hermitian elements gives all of $U(3)$. The pattern is by now familiar: a symmetry of the framework's own algebra on the left, a larger symmetry available only through the tensor square on the right.

This also identifies what a three-level system is *for* in the framework. A spin-one system's physically classical content — its polarization, its rotation, its coherent states — is described by $\mathbb{B}$ through the adjoint action. Its genuinely three-level content — the alignment (nematic) degrees of freedom, the two independent transition frequencies, the interference between the extreme and middle levels — requires the tensor square. A spin-one condensate is a physical system in which both are present at once, and the split between them is visible in its order parameter.

## What Is Available: Three Levels in the Tensor Square

### The symmetric square

The three-dimensional representation exists as an irreducible summand of the tensor square of the defining module. The Clebsch–Gordan rule of the companion article gives

$$
V\otimes V\;\cong\;\mathrm{Sym}^2V\;\oplus\;\Lambda^2V,\qquad 4=3+1 ,
$$

the three-dimensional symmetric square being the adjoint representation of $\mathfrak{su}(2)$ and the one-dimensional alternating square the scalar, spanned by the invariant alternating form. The qutrit is $\mathrm{Sym}^2V$, realised in the framework by the triplet of the two-spin problem.

In the framework the tensor square is $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$, the module is $V\otimes V$ with the four basis states of the companion problem on two spin-$\tfrac12$ particles, and the two summands are the triplet and the singlet. The projector onto the qutrit sector is

$$
P_{\mathrm{sym}}=\tfrac{1}{4}\left(3\,e_0\otimes e_0-\sum_ke_k\otimes e_k\right),
$$

and the spin-one operators are the symmetric combinations

$$
\tilde F_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}=\tfrac{\hbar}{2}\left(ie_k\otimes e_0+e_0\otimes ie_k\right),
$$

which act on $\mathrm{Sym}^2V$ irreducibly and annihilate $\Lambda^2V$. The ladder behaves as a three-level ladder should: the raising operator restricted to the symmetric sector is the spin-one raising operator,

$$
\left(\tilde S_+^{(1)}+\tilde S_+^{(2)}\right)\Big|_{\mathrm{Sym}^2V}=\hbar\, J_+
$$

with the standard matrix elements $J_+|1,0\rangle=\sqrt2\hbar\,|1,1\rangle$ and $J_+|1,-1\rangle=\sqrt2\hbar\,|1,0\rangle$; this was verified by restricting the four-dimensional operator to the symmetric basis. The first obstruction is thus bypassed at the cost of one factor: the two-level algebra, applied twice.

The observables of the qutrit are equally available. The spin-one operators generate the full matrix algebra: the real span of the products of $I_3,F_1,F_2,F_3$ of length up to three has real dimension $18$, which is $\dim_{\mathbb{R}}M_3(\mathbb{C})$, as required by the density theorem for an irreducible representation. Every operator connecting the three levels — including the shifts whose absence was the obstruction — is therefore a polynomial in the spin-one operators of the tensor square.

### The cost

Three prices are paid for this construction, and they are worth stating plainly.

- **One extra level.** The tensor square has four levels; the qutrit has three. The singlet must be projected out, either by the projector $P_{\mathrm{sym}}$ or, equivalently, by imposing exchange symmetry as a superselection rule. Physically this is the statement that a spin-one system built from two spin-$\tfrac12$ parts carries an antisymmetric partner that must be discarded.
- **A larger algebra.** The algebra grows from $\mathbb{B}\cong M_2(\mathbb{C})$ to $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$: complex dimension $4$ to $16$. The qutrit's ten-real-dimensional block of operators involving the third level exists, but in $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$, not in $\mathbb{B}$.
- **A changed notion of elementary.** In $\mathbb{B}$ the observable algebra, the state space and the norm form are all properties of one algebra element. In the tensor square the qutrit's observables are elements of a sector selected by a projector, and the sector is not closed under multiplication by the whole algebra — $P_{\mathrm{sym}}xP_{\mathrm{sym}}$ is a qutrit operator for every $x$, but the intermediate objects are four-dimensional.

The last point is the one that controls the geometry. The state space of the qutrit is the positive unit-trace part of the projected sector, and it is not the trace-one slice of a cone in $\mathbb{M}_+$; its boundary is cut by the cubic $\det\rho=0$, and the largest ball it contains has half the radius of the pure-state sphere. The cone picture, which was exact for the qubit, is what the third level costs.

### Comparison with the standard qutrit formalism

The ledger between the algebra and the tensor square can be drawn item by item. The first column lists what a three-level system is usually taken to be; the second records where, in the framework, it is found.

| Qutrit ingredient | Where it lives |
|---|---|
| Three orthonormal levels | the triplet sector $\mathrm{Sym}^2V\subset V\otimes V$ |
| The three spectral projectors $E_{mm}$ | symmetric elements of $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$, selected by $P_{\mathrm{sym}}$ |
| Raising and lowering $J_\pm$ ($J_+^3=0$) | $\tilde S_\pm^{(1)}+\tilde S_\pm^{(2)}$ restricted to the sector |
| The spin vector $\langle\mathbf F\rangle$ | the adjoint action of $\mathbb{B}$ on the traceless part |
| Coherent states | symmetrised products $P_{\mathrm{sym}}(P_+\otimes P_+)P_{\mathrm{sym}}$ |
| Gell-Mann basis, structure constants | not in $\mathbb{B}$; reachable as polynomials in $I_3,F_1,F_2,F_3$ |
| The dynamical group $U(3)$, the two Cartan directions | not in $\mathbb{B}$; $M_3(\mathbb{C})$ generated by the $F$'s in $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$ |
| Quadratic invariant of a state | the purity $\mathrm{Tr}(\rho^2)=\tfrac13(1+2\lvert\mathbf n\rvert^2)$, quadratic in the Bloch vector |
| Cubic invariant | $\det\rho$, with $\det\rho\ge0$ the boundary condition for positivity |
| State space as a cone slice | not available; the boundary is cubic, not the null cone of a quadratic form |

Two entries deserve comment. The projectors and the shifts are genuinely available, and they are elements of the two-qubit algebra, so the framework does contain the qutrit's standard formalism — in the tensor square. The Gell-Mann basis and the dynamical group are available too, but only as polynomials; they are not *elementary*, in the sense that no single algebra element of $\mathbb{B}$ represents a Gell-Mann generator. That distinction — elementary versus generated — is what the level count really controls.

The physical reading of the spectator statement is worth stating once. If one insists on a three-level system inside $\mathbb{B}$, the only possibility is a qubit plus a decoupled level, and the decoupled level is a superselection sector: no observable of the theory connects it to the other two. Such a system is a qubit with a label, not a qutrit; and the label carries no information, because nothing acts on it. The framework's own three-level structures are therefore always composite, in the sense of the tensor square.

## Higher Spin: The General Counting

The pattern is general. The irreducible representation of highest weight $n$ is the symmetric power

$$
\mathrm{Sym}^nV,\qquad \dim_{\mathbb{C}}\mathrm{Sym}^nV=n+1 ,
$$

that is, the spin-$j$ multiplet $V_j$ with $j=n/2$, as recorded in the companion article *Biquaternion Representation Theory*, and it appears as a summand of the $n$-fold tensor power, with multiplicities given by the ballot numbers. Since a single factor of the algebra carries only two levels, the counting is:

| Spin | Multiplet $\dim=2s+1$ | Sector of | Factors needed |
|---|---|---|---|
| $0$ | $1$ | $\Lambda^2V$ (singlet) | $2$ |
| $\tfrac12$ | $2$ | $V$ (the defining module) | $1$ |
| $1$ | $3$ | $\mathrm{Sym}^2V$ (qutrit) | $2$ |
| $\tfrac32$ | $4$ | the highest summand of $V^{\otimes3}$ | $3$ |
| $s$ | $2s+1$ | $\mathrm{Sym}^{2s}V$ | $2s$ |

The cost is linear in the number of levels minus one. The $\tfrac32$ case requires three factors and is instructive: $V^{\otimes3}\cong\mathrm{Sym}^3V\oplus 2V$, so the four-dimensional multiplet appears together with two unwanted doublets, and the projection is onto a sector of a sector. For a spin-one system the projection is clean — one singlet out — and for that reason spin one is the first case in which the framework's higher-spin construction is genuinely useful, and the last in which it is uncomplicated.

## What the Algebra's Virtues Become

The qubit's most characteristic results are properties of $M_2$ rather than of quantum theory in general, and each of them degrades in a way that can be stated exactly.

| Structure | Qubit, from $\mathbb{B}=M_2(\mathbb{C})$ | Qutrit, in $\mathrm{Sym}^2V$ |
|---|---|---|
| Number of levels | $2$, the module dimension | $3$, a summand of the tensor square |
| Norm form | $N(\tilde H)=\det\tilde H$, a quadratic form of signature $(1,3)$ | the determinant of a $3\times3$ matrix, a cubic |
| Positive cone | the future light cone of $N$; positivity $=$ causality | not a cone of a quadratic form; positivity is $|\mathbf n|\le1$ with $\det\rho\ge0$ |
| Pure states | the zero divisors at trace one; the boundary of the ball | rank-one states; a four-real-dimensional manifold, not a sphere |
| State space | the Bloch ball, a slice of the cone | an eight-dimensional convex body; the inscribed ball has radius $\tfrac12$ |
| Ladder | one rung, $S_+^2=0$ | two rungs, $J_+^3=0$, $J_+^2\neq0$ |
| Sharp measurements | up to two outcomes | up to three outcomes, in $M_3(\mathbb{C})$ |
| Algebra | $M_2(\mathbb{C})$, real dimension $8$ | $M_3(\mathbb{C})$, real dimension $18$, reached only in $\mathbb{B}\otimes\mathbb{B}$ |

The pattern is uniform: each entry in the right-hand column loses a property that followed, in the left-hand column, from the coincidence of "two levels", "determinant of a $2\times2$ matrix", and "the module of the algebra". The determinant becomes a cubic, the cone becomes a body cut by a cubic and a quadratic, the zero divisors cease to be the boundary of the state space, and the level count is no longer the dimension of a module of the algebra.

None of this argues that the framework is inapplicable to spin one. The operators, the multiplets, the coupling coefficients, the coherent states and the geometry are all constructible, and the companion articles carry out the construction. What it argues is that the third level is not a feature of the algebra: **the qutrit is a sector of the tensor square of two fundamental systems, and its description is imported through a projector rather than read off from a single algebra element.** That is the sense, and the only precise sense, in which three-level systems lie outside the biquaternion algebra.

## Summary

Three-level systems are outside the biquaternion algebra as modules, and inside its tensor square as a sector. The article established the following.

- **Level count.** $\mathbb{B}\cong M_2(\mathbb{C})$ has $V=\mathbb{C}^2$ as its only simple module, and every unital finite-dimensional module is $V^{\oplus k}$ of even dimension $2k$. A unital three-dimensional module does not exist; the only three-dimensional action is the block embedding into $M_2(\mathbb{C})\oplus0\subset M_3(\mathbb{C})$, in which the third level is annihilated by every algebra element, and the ten operators that involve it are absent.
- **Nilpotency ceiling.** By Cayley–Hamilton every nilpotent element of $\mathbb{B}$ has square zero, $n^2=0$, and the algebra's raising element satisfies $(\tilde S_+)^2=0$ and $(ie_1-e_2)^2=0$. A three-level ladder has nilpotency index three, $J_+^3=0$ with $J_+^2\neq0$; no such element exists in $\mathbb{B}$. The index of nilpotency equals the number of levels minus one.
- **Idempotent ceiling.** At most two orthogonal idempotents of $\mathbb{B}$ can sum to the identity, so a three-outcome projective measurement is impossible in the algebra; three-outcome POVMs exist, but they are not sharp.
- **The adjoint representation.** The traceless part $W$ carries spin one under the adjoint action, but $\mathrm{ad}_{xy}\neq\mathrm{ad}_x\mathrm{ad}_y$: explicitly $\mathrm{ad}_{ie_1}^2(ie_2)=+4ie_2\neq0=\mathrm{ad}_{(ie_1)^2}(ie_2)$. The three-dimensional space is a module of the Lie algebra $\mathfrak{su}(2)$ and of the group $SU(2)$, not of the algebra $\mathbb{B}$; all derivations are inner and $\mathrm{Der}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$.
- **The absent dynamical algebra.** $\dim_{\mathbb{R}}\mathbb{M}_+=4$, $\dim_{\mathbb{R}}\mathbb{B}=8$ and $\dim_{\mathbb{R}}\mathrm{Der}(\mathbb{B})=6$ are all smaller than $\dim_{\mathbb{R}}\mathfrak{u}(3)=9$ and $\dim_{\mathbb{R}}\mathfrak{su}(3)=8$; the framework supplies the spin subgroup $SU(2)$ of dimension three, and the rest of $U(3)$ only through the tensor square.
- **The construction.** $V\otimes V\cong\mathrm{Sym}^2V\oplus\Lambda^2V$, $4=3+1$; the qutrit is $\mathrm{Sym}^2V$, selected by $P_{\mathrm{sym}}$, on which $\tilde F_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}$ acts irreducibly with $(\tilde S_+^{(1)}+\tilde S_+^{(2)})|_{\mathrm{Sym}^2V}=\hbar J_+$; the products of $I_3,F_1,F_2,F_3$ generate $M_3(\mathbb{C})$, of real dimension $18$.
- **The cost.** One extra level that must be projected out, an algebra that grows from $M_2(\mathbb{C})$ to $M_4(\mathbb{C})$, and a state space whose positivity is no longer a quadratic cone condition.
- **General counting.** $\mathrm{Sym}^nV$ has dimension $n+1$; spin $s$ requires $2s$ factors, so the cost in factors is linear in the number of levels minus one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $V=\mathbb{C}^2$ | Defining module, the only simple module |
| $V^{\oplus k}$ | General unital module, dimension $2k$ |
| $S=\mathrm{Res}_{\mathbb{C}/\mathbb{R}}V$ | Simple real module, real dimension $4$ |
| $W=\operatorname{span}_\mathbb{C}\{ie_1,ie_2,ie_3\}$ | Traceless part, carries the adjoint (spin-one) action |
| $\mathrm{ad}_x(y)=[x,y]$ | Adjoint action, a derivation |
| $S_+$, $\tilde S_+$ | Raising operator; $S_+^2=0$ |
| $J_+$ | Spin-one raising operator; $J_+^3=0$, $J_+^2\neq0$ |
| $P_{\mathrm{sym}},P_{\mathrm{asym}}$ | Triplet and singlet projectors of $\mathbb{B}\otimes\mathbb{B}$ |
| $\mathrm{Sym}^2V$, $\Lambda^2V$ | Symmetric and antisymmetric squares; dimensions $3$ and $1$ |
| $\mathrm{Sym}^nV$ | Symmetric $n$-th power of the defining module, dimension $n+1$ |
| $\tilde F_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}$ | Spin-one operators of the tensor square |
| $M_3(\mathbb{C})$ | Qutrit observable algebra, real dimension $18$ |

## Further Reading

- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the classification of modules over a full matrix algebra, Schur's lemma, and the density theorem.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras* (Academic Press, 1983), for the density theorem, irreducible representations, and the structure of finite-dimensional operator algebras.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for the Jordan form, the nilpotency index, and the idempotent decompositions used here.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Van Nostrand, 1958), for the spectral theorem and the rank additivity of orthogonal projections.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for three-level systems, their ladder operators and their standard projective measurements.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for POVMs, the trine measurement, and the comparison between projective and non-projective resolutions of the identity.
- Alexander Holevo, *Probabilistic and Statistical Aspects of Quantum Theory* (North-Holland, 1982), for the general theory of quantum measurements on finite-level systems.
- Ingemar Bengtsson and Karol Życzkowski, *Geometry of Quantum States* (Cambridge University Press, 2006), for state spaces of three-level systems and how they differ from the Bloch ball.
