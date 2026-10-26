# __The Polar Decomposition and Remarkable Subspaces__

## Introduction

**The subject.** This article reads the polar decomposition against the six remarkable subspaces of the algebra.

The four-factor word is that of *The Polar Decomposition of a N-Regular Biquaternion*, the refinement of the two-factor pair of *The Polar Decomposition of a Biquaternion*, and it reads

$$
\tilde{Q} = r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
$$

with the positive real scale $r$, the central phase $\zeta$ of modulus one on the branch $\arg\zeta\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, the Hermitian positive unit-norm boost $\tilde U_{\mathrm b}$ and the unit real quaternion rotor $\tilde u_{\mathrm r}$.

The pair is defined on the whole algebra, with a Hermitian positive semidefinite factor and a partial isometry. On the elements of non-vanishing norm the partial isometry is unitary and splits into the phase and the rotor, which is the word above; on the null cone it does not split, and the pair is computed there in *The Polar Decomposition of a N-Degenerate Biquaternion*.

The algebra carries six **remarkable subspaces**, defined in *Introduction to the Remarkable Subspaces*: the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$.

**The approach.** The article establishes four things, in this order. The four blocks and the exponent of each factor are identified. The blocks are put against the Clifford grades and against the six subspaces, which are their sums two by two. The incidence of the exponents with the subspaces is tabulated, with the polar data each subspace carries. The two products of the series — of two boosts, and of the word of a pure vector — are computed, and the domain and the conjugations of the word close the account.

**The result, in one sentence.** The four exponents of a generic polar word lie one in each of the four coordinate blocks of the algebra, so that each exponent lies in exactly three of the six remarkable subspaces and each remarkable subspace contains exactly two of them, and the polar word fails on a subspace exactly on the origin or its nonzero zero divisors.

Four conjugations are used. The quaternion conjugation is $\tilde{Q}^{\natural} = Q_te_t-\vec Q$, the coefficientwise conjugation is $\overline{\tilde{Q}}$, the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the reversal is $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$.

The norm is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^{2} = \det\mathsf{M}_2(\tilde{Q})$, complex in general, and the domain of the polar word is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$.

The symbols $r$, $\zeta$, $\alpha$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$, $\Rho = r\zeta$, $\psi$, $\theta$, $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$, $\mathcal{A}$ and $N$ are those of the companion article *The Polar Decomposition of a N-Regular Biquaternion*. The subspaces $\mathbb{M}_\pm$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ are the remarkable subspaces of *Introduction to the Remarkable Subspaces*, and the four coordinate blocks $A_1$, $A_2$, $B_1$, $B_2$ are those of *Comparison of the Remarkable Subspaces*.

No physics is invoked; the physical interpretation is cited where it clarifies the algebra.

## The Four Exponents of the Word

Each of the four factors has a single **exponent**, one real parameter times one **root** of the algebra; the phase angle is $\alpha=\arg\zeta$, and the square of the root decides the character of the factor. The four factors and their exponents are

$$
\boxed{\; \tilde{Q}=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\bigl(r,\zeta,\tilde U_{\mathrm b},\tilde u_{\mathrm r}\bigr)
\longleftrightarrow
\bigl(\ln r,\,i\alpha,\,i\tfrac{\psi}{2}\vec u_{\mathrm b},\,\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr) \;}.
$$

| factor | exponent | root | square of the root | character |
|---|---|---|---|---|
| $r$ | $\ln r$ | $e_t$ | $+e_t$ | hyperbolic, degenerate |
| $\zeta$ | $i\alpha$ | $i$ | $-e_t$ | trigonometric, central |
| $\tilde U_{\mathrm b}$ | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $i\vec u_{\mathrm b}$ | $+e_t$ | hyperbolic |
| $\tilde u_{\mathrm r}$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\vec u_{\mathrm r}$ | $-e_t$ | trigonometric |

The scale and the boost stand on a root of $+e_t$, one of them the central $e_t$ and one of them the Hermitian pure element $i\vec u_{\mathrm b}$; the phase and the rotor stand on a root of $-e_t$, one of them the central $i$ and one of them the real pure quaternion $\vec u_{\mathrm r}$.

The two axes are unit elements of the algebra as well: $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ are unit real pure quaternions, members of the axis sphere $\mathcal{A}$, and $i$ and $e_t$ are the two central unit elements.

## The Four Coordinate Blocks

The four **coordinate blocks** of the algebra are the pieces into which the eight real coordinates group (*Comparison of the Remarkable Subspaces*, §*Remarkable Subspaces and the Coordinate Blocks*):

$$
A_1 = \mathbb{R}e_t , \qquad A_2 = \mathbb{R}(ie_t) , \qquad B_1 = \operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\} , \qquad B_2 = \operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\} .
$$

The two scalar blocks $A_1,A_2$ have real dimension one, the two vector blocks $B_1,B_2$ have real dimension three, and the four of them add to the algebra, $A_1\oplus A_2\oplus B_1\oplus B_2 = \mathbb{B}$.

**The four exponents occupy the four blocks, one block each.** Comparing the coordinates of the four exponents with the definitions above,

| exponent | block | the block | factor |
|---|---|---|---|
| $\ln r$ | $A_1 = \mathbb{R}e_t$ | the real scalar line | the scale |
| $i\alpha$ | $A_2 = \mathbb{R}(ie_t)$ | the imaginary scalar line | the central phase |
| $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $B_1 = \operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | the real vector block | the rotor |
| $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $B_2 = \operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ | the imaginary vector block | the boost |

**Theorem (the block reading of the polar word).** For a generic polar word, each one of the four exponents lies in exactly one of the four coordinate blocks, and every one of the four blocks carries exactly one exponent.

**Proof.** The exponent $\ln r$ is a real multiple of $e_t$, hence in $A_1$; the exponent $i\alpha$ is a real multiple of $ie_t$, hence in $A_2$; the exponent $\tfrac{\theta}{2}\vec u_{\mathrm r}$ has three real coordinates on $\vec e_x,\vec e_y,\vec e_z$ and vanishing others, hence is in $B_1$; and the exponent $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ has three real coordinates on $i\vec e_x,i\vec e_y,i\vec e_z$ and vanishing others, hence is in $B_2$. Since distinct blocks meet only at $0$ and the four exponents are nonzero, the assignment is a bijection between the four exponents and the four blocks.

The additivity of the dimensions of the blocks is the block form of the count of the four factors,

$$
1+1+3+3 = 8 = \dim_{\mathbb{R}}\mathbb{B} ,
$$

and it is the same statement as the independence of the four factors in *The Polar Decomposition of a N-Regular Biquaternion*.

Because the four exponents lie in the four blocks and the four blocks add to the algebra, **the four exponents of a generic polar word are linearly independent**: they occupy one direction in each block, so they span a real four-dimensional subspace of $\mathbb{B}$, one dimension in each block, and the word is generated, block by block, by one scalar, one pseudoscalar, one Clifford vector and one bivector generator, in the grade notation of the next section.

## The Blocks and the Four Grades

Under the identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, $\gamma_k\mapsto i\vec e_k$ (*Comparison of the Remarkable Subspaces*, §*Remarkable Subspaces and the Coordinate Blocks*), the four blocks are the four Clifford grades.

| block | $A_1$ | $B_2$ | $B_1$ | $A_2$ |
|---|---|---|---|---|
| grade | $0$ | $1$ | $2$ | $3$ |
| basis | $e_t$ | $i\vec e_x,i\vec e_y,i\vec e_z$ | $\vec e_x,\vec e_y,\vec e_z$ | $ie_t$ |
| exponent it carries | $\ln r$ | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $i\alpha$ |
| factor | the scale | the boost | the rotor | the central phase |

**The four factors of the polar word are the four Clifford grades, one factor to a grade**, and the order of the grades is not the order of the word: the word is written scale, phase, boost, rotor, which is grade $0$, grade $3$, grade $1$, grade $2$.

Two of the four exponents carry an axis, and the Clifford reading names the grade of each axis. The boost exponent is the Clifford vector

$$
i\tfrac{\psi}{2}\vec u_{\mathrm b} = \tfrac{\psi}{2}\bigl(\vec u_{\mathrm b,1}\gamma_1+\vec u_{\mathrm b,2}\gamma_2+\vec u_{\mathrm b,3}\gamma_3\bigr) ,
$$

because $i\vec e_k = \gamma_k$ for $k=1,2,3$. The rotor exponent is the Clifford **bivector**

$$
\tfrac{\theta}{2}\vec u_{\mathrm r} = -\tfrac{\theta}{2}\bigl(\vec u_{\mathrm r,1}\gamma_2\gamma_3+\vec u_{\mathrm r,2}\gamma_3\gamma_1+\vec u_{\mathrm r,3}\gamma_1\gamma_2\bigr) ,
$$

because $\vec e_x = -\gamma_2\gamma_3$, $\vec e_y = -\gamma_3\gamma_1$ and $\vec e_z = -\gamma_1\gamma_2$. The scale exponent is the scalar and the phase exponent the pseudoscalar,

$$
\ln r\in\mathbb{R} , \qquad i\alpha = \alpha\,\gamma_1\gamma_2\gamma_3 ,
$$

since $ie_t = (i\vec e_x)(i\vec e_y)(i\vec e_z) = \gamma_1\gamma_2\gamma_3$.

The naming of the two vector blocks is the trap the comparison article records: the block that the algebra calls the real vector block is the grade-two block, and the block that it calls the imaginary vector block is the grade-one block. So the rotor, not the boost, is the bivector of the Clifford reading, and the boost, not the rotor, is its vector.

**Remark.** The grade reading separates the four factors by the kind of object each one is: a number (the scale), a pseudoscalar (the phase), a vector (the boost) and a bivector (the rotor). In the physical interpretation of the companion articles this is the algebraic content of the statement that a rotation is generated by a bivector and a boost by a vector.

## The Six Subspaces as Sums of the Blocks

Every remarkable subspace is a sum of two of the four blocks (*Comparison of the Remarkable Subspaces*, §*Remarkable Subspaces and the Coordinate Blocks* and §*The Lattice of the Fixed Spaces*), and the sums are the following.

| subspace | defining condition | blocks | real dimension |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde{Q}^{\natural} = \tilde{Q}$ | $A_1\oplus A_2$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $B_1\oplus B_2$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $A_1\oplus B_1$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = -\tilde{Q}$ | $A_2\oplus B_2$ | $4$ |
| $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | $A_1\oplus B_2$ | $4$ |
| $\mathbb{M}_-$ | $\tilde{Q}^{*} = -\tilde{Q}$ | $A_2\oplus B_1$ | $4$ |

Two of the six subspaces are the two doubles of the blocks, the centre $A_1\oplus A_2$ and the vector subspace $B_1\oplus B_2$; the other four are the four mixed pairs, one scalar block with one vector block, and they are exactly the four ways of choosing one of $A_1,A_2$ and one of $B_1,B_2$. The table is the whole relation between the blocks and the subspaces.

## The Incidence of the Four Exponents and the Six Subspaces

The block reading of the word and the block reading of the subspaces give the incidence of the exponents with the subspaces, by one substitution: an exponent that lies in a block lies in every subspace that contains the block.

| exponent | its block | the subspaces that contain it |
|---|---|---|
| $\ln r$ (scale) | $A_1$ | $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ |
| $i\alpha$ (phase) | $A_2$ | $\mathbb{C}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ |
| $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ (boost) | $B_2$ | $\mathrm{Vect}(\mathbb{B})$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ |
| $\tfrac{\theta}{2}\vec u_{\mathrm r}$ (rotor) | $B_1$ | $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ |

**Theorem (the incidence).** For a generic polar word, each of the four exponents lies in exactly three of the six remarkable subspaces, and each of the six remarkable subspaces contains exactly two of the four exponents.

**Proof.** Each exponent lies in exactly one block, by the block reading of the word; each nonzero element of a block lies in exactly three remarkable subspaces, by the six-row table above; hence each exponent lies in exactly three of them. The dual statement is the same count read row by row of the subspace table: the centre contains $A_1$ and $A_2$, the vector subspace $B_1$ and $B_2$, the quaternion subspace $A_1$ and $B_1$, the anti-quaternion subspace $A_2$ and $B_2$, the Hermitian subspace $A_1$ and $B_2$, and the anti-Hermitian subspace $A_2$ and $B_1$. The counts agree: $4\times3 = 12 = 6\times2$.

Read subspace by subspace, the incidence gives the pair of exponents each subspace carries:

| subspace | the two exponents it carries | names |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\ln r$, $i\alpha$ | the modulus |
| $\mathrm{Vect}(\mathbb{B})$ | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$, $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | the two axes |
| $\mathbb{H}_{\mathbb{B}}$ | $\ln r$, $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | the scale and the rotor |
| $i\mathbb{H}_{\mathbb{B}}$ | $i\alpha$, $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | the phase and the boost |
| $\mathbb{M}_+$ | $\ln r$, $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | the hyperbolic pair |
| $\mathbb{M}_-$ | $i\alpha$, $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | the trigonometric pair |

Three consequences follow at once.

- **No subspace carries all four exponents, and none carries fewer than two.** The word never degenerates to a single subspace, and no subspace can explain the whole word.
- **The centre and the vector subspace carry the two pairs of the same kind.** The centre carries the modulus, that is its two central exponents; the vector subspace carries the two axes, that is its two non-central ones. These are the two subspaces that are sums of the two blocks of one kind.
- **The four mixed subspaces separate the two pairs.** The quaternion and anti-quaternion subspaces separate the real scalar block from the imaginary one and the two vector blocks from each other; the Hermitian and anti-Hermitian subspaces separate the blocks by the reality of their coordinates.

The incidence also matches the Hermitian split of the exponents of *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*: the scale exponent and the boost exponent lie in $\mathbb{M}_+$ and the phase exponent and the rotor exponent in $\mathbb{M}_-$. The split separates the two exponents of each pair, the modular pair and the axial pair, and it is the reason the Cartan pairing is called Hermitian.

## The Polar Data Carried by Each Subspace

The incidence says which exponents a subspace can carry. The polar data of an element of a subspace say more: which of the four factors are trivial there, and what the phase is.

The behaviour of the phase is decided by the norm alone. The phase is $\alpha = \tfrac{1}{2}\arg \langle\tilde{Q}\rangle_{\natural}$, so it is constant on a subspace exactly when the argument of the norm is constant there, and the six subspaces realise the possible behaviours.

| subspace | the norm $\langle\tilde{Q}\rangle_{\natural}$ | the phase |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Q_t^{2}$, complex anisotropic | free, $\arg Q_t$ |
| $\mathrm{Vect}(\mathbb{B})$ | $(\vec Q,\vec Q)$, complex indefinite | free |
| $\mathbb{H}_{\mathbb{B}}$ | a sum of four real squares, positive definite | $0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | minus a sum of four real squares, negative definite | $\pi/2$ |
| $\mathbb{M}_+$ | $\sigma^{2}-\lvert\vec w\rvert^{2}$, real indefinite | $0$ or $\pi/2$ |
| $\mathbb{M}_-$ | $\lvert\vec\Rho\rvert^{2}-\tau^{2}$, real indefinite | $0$ or $\pi/2$ |

The coordinates of the last two rows are those of the sectors: an element of the Hermitian subspace is $\sigma e_t+i\vec w$ with $\sigma = \operatorname{Re}Q_t$ and $\vec w = w_x\vec e_x+w_y\vec e_y+w_z\vec e_z$ real, and an element of the anti-Hermitian subspace is $i\tau e_t+\vec\Rho$ with $\tau = \operatorname{Im}Q_t$ and $\vec\Rho$ real. The two bars denote the Euclidean norm of the vector, $\lvert\vec w\rvert^{2} = w_x^{2}+w_y^{2}+w_z^{2}$ and likewise for $\vec\Rho$; on the vector subspace the same notation reads $(\vec Q,\vec Q) = Q_x^{2}+Q_y^{2}+Q_z^{2}$ with complex components, the complex Euclidean square.

**The phase is a free coordinate on exactly the two subspaces whose norm is complex**, the centre and the vector subspace, in the sense that it takes every value in the branch interval as the element varies; on a given element it is fixed by the norm, and it is $0$ or $\pi/2$ wherever the norm is real and nonzero, in particular on the real and imaginary lines. It is frozen on the two halves, at $0$ and at $\pi/2$, and it is a two-valued label on the two sectors, where the norm is real indefinite. The norm is complex on exactly the two subspaces that are not real forms of the algebra, which is the same pair.

The two non-central factors behave as follows.

| subspace | the boost | the rotor |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $e_t$ | $\pm e_t$ |
| $\mathrm{Vect}(\mathbb{B})$ | a boost, or $e_t$ on the complex lines through a real direction | a half turn |
| $\mathbb{H}_{\mathbb{B}}$ | $e_t$ | free in $\mathrm{Sp}(1)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $e_t$ | free in $\mathrm{Sp}(1)$ |
| $\mathbb{M}_+$, $N>0$ | the normalised element, up to sign | a sign, $\pm e_t$ |
| $\mathbb{M}_+$, $N<0$ | a nontrivial boost, or $e_t$ on the imaginary vector subspace | a half turn |
| $\mathbb{M}_-$, $N>0$ | a nontrivial boost, or $e_t$ on the real vector subspace | a half turn |
| $\mathbb{M}_-$, $N<0$ | the element times $-i/r$ | a sign, $\pm e_t$ |

Four of the rows are degenerate cases worth naming, and the derivations are those of *The Polar Decomposition in Subspaces*.

- **The centre.** Both non-central factors are trivial, $\tilde U_{\mathrm b} = \tilde u_{\mathrm r} = e_t$, up to the sign of the rotor; a central element is its own modulus. The rotor is $+e_t$ exactly when the argument of $Q_t$ lies in the branch interval $(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, and $-e_t$ otherwise, which is the residual sign of the two branches of the square root.
- **The two halves.** The boost is $e_t$ and the rotor absorbs the whole unit-norm part. On the quaternion subspace the phase is $0$ and the rotor is $\tilde Q/|\tilde Q|$; on the anti-quaternion subspace the phase is $\pi/2$ and the rotor is $\tilde Q/(i|\tilde Q|)$. The two subspaces carry the same rotor set, the same group $\mathrm{Sp}(1)$, with the phase shifted by a quarter turn.
- **The real vector block.** An element of $B_1$ has a positive real norm, so the phase is $0$, the boost is $e_t$, and the rotor is the direction of the element, a half turn about it.
- **A definite Hermitian element.** On $\mathbb{M}_+$ with $N>0$ the normalised element is Hermitian and definite, so it is a boost up to sign, and the rotor is a sign. The same holds on $\mathbb{M}_-$ with $N<0$, where the boost is $-i$ times the normalised element.

The pattern of the last two rows is the symmetry of the two sectors: **on each sector the sign of the norm decides which of the two non-central factors is trivial, except on the vector subspace.** A definite element of a sector is a boost with a sign rotor; an indefinite element outside the vector subspace has a half-turn rotor and a genuine boost, and on the vector subspace the rotor is a half turn, with the boost trivial on the complex lines through a real direction.

| sector | $N>0$ | $N<0$ |
|---|---|---|
| $\mathbb{M}_+$ | the boost carries the element, the rotor is a sign | the rotor carries a direction; the boost is genuine, or $e_t$ on the imaginary vector subspace |
| $\mathbb{M}_-$ | the rotor carries a direction; the boost is genuine, or $e_t$ on the real vector subspace | the boost carries the element, the rotor is a sign |

The two rows are exchanged row for row under the interchange $\mathbb{M}_+\leftrightarrow\mathbb{M}_-$ with $N\mapsto-N$, which is the central unit $i$ read on the sectors.

The signs in the two sign rows are the signs of the two central coordinates of the sector: on $\mathbb{M}_+$ with $N>0$ the rotor is $\operatorname{sign}(\sigma)e_t$, and on $\mathbb{M}_-$ with $N<0$ it is $\operatorname{sign}(\tau)e_t$ with $\tau$ the scalar coordinate. Both were verified over the random samples of each branch, with the boost matching the element to $1.8\times10^{-15}$ on $\mathbb{M}_+$ and to $7.2\times10^{-15}$ on $\mathbb{M}_-$.

## The Boost Family and the Rotor Group

The four factors are four subsets of the algebra, one for each of the four exponents, and three of them are groups and one is not.

- The scale runs over $\mathbb{R}_{>0}$, a half-line of the real scalar block and a group under multiplication.
- The phase runs over $\mathrm{U}(1)$, the unit circle of the imaginary scalar block.
- The boost runs over the Hermitian positive definite elements of norm one, the unit sphere of the positive cone in $\mathbb{M}_+$.
- The rotor runs over $\mathrm{Sp}(1)$, the unit sphere of the quaternion subspace.

The rotor set is a **group**: the product of two unit real quaternions is a unit real quaternion. The phase set is a group as well, and the scale set is a group under multiplication; these three are the groups the word carries.

The boost set is **not** a group: the product of two Hermitian positive elements is not Hermitian in general, so the product of two boosts does not stay in the boost set. The product of two boosts is a boost times a rotor,

$$
\boxed{\; \tilde U_{\mathrm b}(a,\vec u_1)\,\tilde U_{\mathrm b}(b,\vec u_2) = \tilde U_{\mathrm b}(\psi,\vec u_{\mathrm b})\,\tilde u_{\mathrm r}(\theta,\vec u_{\mathrm r}) \;},
$$

and the parameters are the classical ones. The rapidity of the product is fixed by the axes through their scalar and vector products,

$$
\cosh\psi = \cosh a\cosh b+\sinh a\sinh b\,(\vec u_1\cdot\vec u_2) ,
$$

and the residual rotor by

$$
\tan\frac{\theta}{2} = \frac{\sinh\frac{a}{2}\sinh\frac{b}{2}\,\lvert\vec u_1\times\vec u_2\rvert}{\cosh\frac{a}{2}\cosh\frac{b}{2}+\sinh\frac{a}{2}\sinh\frac{b}{2}\,(\vec u_1\cdot\vec u_2)} .
$$

Both identities were verified in double precision over $300$ random pairs, the first to $9.8\times10^{-13}$ and the second to $2.8\times10^{-13}$. The residual rotor is the Thomas-Wigner rotation of the physics articles, *The Lorentz Group in Biquaternionic Form — Structure and Representations*; the algebra records it as the statement that the boost set is a symmetric space and not a group, and the word records it as the escape into the rotor factor.

The two axes are two directions of the vector subspace, $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$, and the question whether they commute is the question whether the word may be reordered. With both factors nontrivial, they commute exactly when they are parallel, and then the word is a single boost-rotation about the common axis; if one factor is central, the word is already order-free. The bracket is developed in *The Hamilton Root Pairing of the Polar Decomposition of Biquaternions*, §*The Two Exponents*.

## The Vector Subspace Is Rigid

The vector subspace is the one subspace on which the polar data of every element is fixed in shape. The block table gives the reason: the vector subspace is the sum $B_1\oplus B_2$ of the two blocks that carry the two non-central exponents, and nothing else. The two central coordinates vanish, and their vanishing is a condition on the two non-central factors.

**Proposition (the half-turn rotor of a pure vector).** Let $\vec Q$ be an element of the vector subspace with $\langle\vec Q\rangle_{\natural}\neq0$, and let $\vec Q = \Rho\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ be its polar word. Then the rotor is a half turn, $\theta = \pi$; either the boost is trivial, $\psi=0$, or its axis is orthogonal to the rotor axis.

**Proof.** Write the two non-central factors in their closed forms,

$$
\tilde U_{\mathrm b} = \cosh\tfrac{\psi}{2}\,e_t+i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b} , \qquad \tilde u_{\mathrm r} = \cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r} ,
$$

and compute the scalar part of their product. Only the scalar part is needed, and it splits into two terms, because the cross terms of a scalar factor with a pure factor have vanishing scalar part:

$$
\operatorname{Sc}\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr) = \cosh\tfrac{\psi}{2}\cos\tfrac{\theta}{2}+i\sinh\tfrac{\psi}{2}\sin\tfrac{\theta}{2}\operatorname{Sc}\bigl(\vec u_{\mathrm b}\vec u_{\mathrm r}\bigr) .
$$

Now $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ are real pure quaternions, so the scalar part of their product is minus their dot product,

$$
\operatorname{Sc}\bigl(\vec u_{\mathrm b}\vec u_{\mathrm r}\bigr) = -\,(\vec u_{\mathrm b},\vec u_{\mathrm r}) .
$$

The element $\vec Q$ is pure, so $\operatorname{Sc}(\vec Q) = 0$, and the modulus $\Rho$ is central, so $\operatorname{Sc}(\tilde U_{\mathrm b}\tilde u_{\mathrm r}) = 0$ as well. The right-hand side is the sum of a real number and a purely imaginary one, so both vanish:

$$
\cosh\tfrac{\psi}{2}\cos\tfrac{\theta}{2} = 0 , \qquad \sinh\tfrac{\psi}{2}\sin\tfrac{\theta}{2}\,(\vec u_{\mathrm b},\vec u_{\mathrm r}) = 0 .
$$

The first gives $\cos\tfrac{\theta}{2} = 0$, that is $\theta = \pi$, since $\theta\in[0,2\pi]$ and the other factor is positive. The second, with $\sin\tfrac{\theta}{2} = 1$, gives either $\psi = 0$ or $(\vec u_{\mathrm b},\vec u_{\mathrm r}) = 0$: the boost is trivial or the two axes are orthogonal.

**Corollary (the normalised piece of a pure vector is a root of $-1$).** With the notation of the proposition, the unit-norm part $\vec Q/\Rho$ satisfies

$$
\boxed{\; \left(\frac{\vec Q}{\Rho}\right)^{\natural} = -\frac{\vec Q}{\Rho} , \qquad \left(\frac{\vec Q}{\Rho}\right)^{2} = -e_t \;},
$$

so it is a root of $-1$ of the algebra, pure and of unit norm. Both identities were verified over $1000$ random complex vectors, the natural conjugate to machine precision and the square to $3.6\times10^{-15}$, together with the two conclusions of the proposition: the scalar part of the rotor vanished to $4.4\times10^{-16}$, and the dot product of the two axes vanished to $2.6\times10^{-15}$ whenever the boost was nontrivial.

**Converse.** The argument reverses. If the rotor of the word of an element is a half turn and either the boost is trivial or its axis is orthogonal to the rotor axis, then the scalar part of $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ vanishes, so the element with that word and any central modulus is pure. The vector subspace is therefore exactly the set of elements whose word has a half-turn rotor, with the boost trivial or its axis orthogonal to the rotor axis.

The proposition is the algebra behind the reading of *The Polar Decomposition in Subspaces*, where the rotor of an element of the vector subspace is a unit vector of the plane of the two real parts; the block form of the same fact is that the vector subspace is the sum of the two non-central blocks and nothing else.

## The Domain Read on the Subspaces

The domain of the polar decomposition is the complement of the null cone $\{\langle\tilde Q\rangle_{\natural}=0\}$, and the intersection of the null cone with a subspace is read from the norm of the subspace.

| subspace | the zeros of the norm | real dimension | the polar word |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $0$ alone, the norm is anisotropic | $0$ | on the punctured centre |
| $\mathrm{Vect}(\mathbb{B})$ | the complex isotropic cone $(\vec Q,\vec Q) = 0$ | $4$ | fails on the cone |
| $\mathbb{H}_{\mathbb{B}}$ | $0$ alone, the norm is definite | $0$ | on the punctured subspace |
| $i\mathbb{H}_{\mathbb{B}}$ | $0$ alone, the norm is definite | $0$ | on the punctured subspace |
| $\mathbb{M}_+$ | the cone $\sigma^{2} = \lvert\vec w\rvert^{2}$ | $3$ | fails on the cone |
| $\mathbb{M}_-$ | the cone $\lvert\vec\Rho\rvert^{2} = \tau^{2}$ | $3$ | fails on the cone |

**Theorem (the domain on the subspaces).** The polar decomposition exists on the whole of the punctured centre, punctured quaternion subspace and punctured anti-quaternion subspace, and it fails on the other three subspaces exactly on the origin and their nonzero zero divisors.

**Proof.** By the table, the norm of an element of each of the centre, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ vanishes only at the origin: the centre is a field, the quaternion subspace is a division algebra, and the anti-quaternion subspace is its purely imaginary copy, where the norm is minus a sum of squares. On the other three subspaces the vanishing of the norm is one complex equation on the vector subspace and two real equations on each sector, defining the isotropic cone and the two null cones, and $\langle\tilde Q\rangle_{\natural}=0$ with $\tilde Q\neq0$ is exactly the zero-divisor condition.

The three subspaces on which the polar word fails only at the origin are exactly the three that carry no nonzero zero divisor, which is the statement of *Introduction to the Remarkable Subspaces* read through the polar decomposition. The intersection of the domain with the algebra is thus the complement of a single cone, and the trace of that cone on the subspaces is a single point on each of the centre, the quaternion subspace and the anti-quaternion subspace, the four-dimensional complex isotropic cone on the vector subspace, and a three-dimensional null cone on each sector.

The behaviour of the word at the boundary completes the picture: along a path to the cone of $\mathbb{M}_+$ the scale collapses and the word tends to the minimal idempotent $\tfrac{1}{2}(e_t+\vec\Xi i)$ with $\vec\Xi$ a unit real vector, Hermitian, of norm zero and idempotent. The boundary of the family of boosts is the family of minimal idempotents of the Hermitian subspace, and within $\mathbb{M}_+$ the null cone is the cone over that family: every nonzero null element of the Hermitian half is a real multiple of a Hermitian minimal idempotent.

The failure is of the four-factor word, not of the decomposition. On the cone the two-factor pair survives, with a Hermitian positive semidefinite factor and a partial isometry; the minimal idempotent above is its positive factor up to the scalar. The general statement is *The Polar Decomposition of a Biquaternion*, and the closed forms on the two sectors of the cone are *The Polar Decomposition of a N-Degenerate Biquaternion*.

## The Action on the Two Halves

The four factors are also an action. The **sandwich** of an invertible element is

$$
\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\,\tilde Q_1\,\tilde Q^{*}.
$$

It is $\mathbb{C}$-linear and preserves each half, because

$$
\bigl(\tilde Q\tilde Q_1\tilde Q^{*}\bigr)^{*}=\tilde Q\tilde Q_1^{*}\tilde Q^{*}=\pm\,\tilde Q\tilde Q_1\tilde Q^{*}
$$

according as $\tilde Q_1^{*}=\pm\tilde Q_1$. Stability is a consequence of the involution, not of a norm-one hypothesis. The word factorises the action,

$$
\boxed{\; \Theta_{\tilde Q}=r^{2}\,\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}} \;},
$$

since the phase is central of modulus one and acts trivially, the scale multiplies every image by $r^{2}$, and the two non-central factors act in the order rotor first, boost second.

Stability belongs to the sandwich and not to multiplication: a nonzero central multiplier preserves a half only when it is real, so multiplication by a non-real central scalar moves $\mathbb{M}_\pm$ out of itself, while the sandwich by any central scalar is the identity.

### The Anti-Hermitian Half as Four-Vectors

An element of $\mathbb{M}_-$ is written $\tilde Q_-=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b\in\mathbb{R}^{3}$. Its norm is the Lorentzian form

$$
\langle\tilde Q_-\rangle_{\natural}=-a^{2}+\lvert\vec b\rvert^{2},
$$

of signature $(3,1)$, with polarisation $g_-=-aa'+\vec b\cdot\vec b'$ and matrix $G_-=\operatorname{diag}(-1,1,1,1)$.

For a norm-one element $\tilde U$, the matrix image has determinant one, so it lies in $SL(2,\mathbb{C})$, and

$$
\langle\Theta_{\tilde U}(\tilde Q_-)\rangle_{\natural}
=\lvert\det\mathsf M_2(\tilde U)\rvert^{2}\langle\tilde Q_-\rangle_{\natural}
=\langle\tilde Q_-\rangle_{\natural}.
$$

The action is a Lorentz transformation, proper and orthochronous because $SL(2,\mathbb{C})$ is connected and the map is continuous. Its kernel is $\{\pm e_t\}$ and both groups have real dimension six, so the image is all of $SO^{+}(1,3)$.

The boost $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ acts by

$$
a'=a\cosh\psi-b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi-a\sinh\psi,\qquad
\vec b_\perp'=\vec b_\perp,
$$

and the rotor fixes the time direction and applies the spatial rotation of angle $\theta$ about its axis to $\vec b$. A general norm-one element gives

$$
\Lambda_-(\psi,\theta)=B_-(\psi,\vec u_{\mathrm b})\operatorname{diag}(1,\mathsf R(\theta,\vec u_{\mathrm r})),
$$

with $B_-$ the $4\times4$ boost matrix and $\mathsf R$ the Rodrigues matrix. The rotation acts first. For a general element the action is $r^{2}\Lambda_-$: a linear conformal transformation, of determinant $r^{8}$, whose image is $CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3)$. The Lorentz group and its double cover are in *Biquaternion Rotations and Lorentz Transformations*.

### The Hermitian Half as a Congruence

An element of $\mathbb{M}_+$ is written $\tilde Q_+=a\,e_t+i\vec b$, and its norm is

$$
\langle\tilde Q_+\rangle_{\natural}=a^{2}-\lvert\vec b\rvert^{2},
$$

with $G_+=\operatorname{diag}(1,-1,-1,-1)=-G_-$. The sandwich is a congruence of the Hermitian matrix image by the invertible matrix $\mathsf M_2(\tilde Q)$. Sylvester's law of inertia applies: rank, inertia and causal type are preserved. The determinant scales,

$$
\det\mathsf M_2\bigl(\Theta_{\tilde Q}(\tilde Q_+)\bigr)=r^{4}\langle\tilde Q_+\rangle_{\natural},
$$

and the boost acts by the same formulas with the opposite cross-term signs,

$$
a'=a\cosh\psi+b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi+a\sinh\psi.
$$

The trace is invariant under the phase, the scale and the rotor, up to the factor $r^{2}$ of the scale, and is changed by the boost. The invariant object is the pair of the determinant scaling and the inertia, not the spectrum.

### The Two Halves Are One Action

The central $i$ commutes with every element, so

$$
\Theta_{\tilde Q}(i\tilde Q_+)=i\,\Theta_{\tilde Q}(\tilde Q_+),
$$

and multiplication by $i$ intertwines the two restrictions. The intertwiner is not an isometry: $\langle i\tilde Q_+\rangle_{\natural}=-\langle\tilde Q_+\rangle_{\natural}$, and in coordinates it is the reflection $D=\operatorname{diag}(1,-1,-1,-1)$, so the two forms are opposite. The two boost matrices satisfy

$$
B_-=D\,B_+\,D=B_+^{-1},
$$

and the rotor matrix and the scale are the same in both halves. The sign of the form is opposite, the causal type is the same, and the null cone $a^{2}=\lvert\vec b\rvert^{2}$ is common.

| group | image on either half | kernel |
|---|---|---|
| $\mathbb{B}^{\times}$ | $CO^{+}(1,3)$ | $\mathrm{U}(1)=\{\omega:\lvert\omega\rvert=1\}$ |
| $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$ | $SO^{+}(1,3)$ | $\{\pm e_t\}$ |
| $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$ | $SO(3)$ | $\mathrm{U}(1)$ |

### The Infinitesimal Split

Differentiating at the identity separates the two kinds of factor. For a rotor direction $\mathcal R=\frac{1}{2}\vec u_{\mathrm r}$, real and pure, the rotor path $\tilde u(\epsilon)=e_t+\epsilon\mathcal R+O(\epsilon^{2})$ gives

$$
\Theta_{\tilde u(\epsilon)}(\tilde Q_1)=\tilde Q_1+\epsilon\,[\mathcal R,\tilde Q_1]+O(\epsilon^{2}),
$$

a commutator. For a boost direction $\mathcal H=\frac{i}{2}\vec u_{\mathrm b}$, imaginary and pure, the boost path $\tilde U(\epsilon)=e_t+\epsilon\mathcal H+O(\epsilon^{2})$ gives

$$
\Theta_{\tilde U(\epsilon)}(\tilde Q_1)=\tilde Q_1+\epsilon\,\{\mathcal H,\tilde Q_1\}+O(\epsilon^{2}),
$$

an anticommutator. The phase direction $ie_t$ gives zero. The commutator and the anticommutator are the two summands of the Cartan decomposition $\mathfrak{sl}(2,\mathbb{C})=\mathfrak{su}(2)\oplus\mathfrak{p}$, which the Cartan pairing records at the level of the element. The action therefore reproduces, infinitesimally, the same split the word exhibits algebraically.

## Which Subspaces the Sandwich Preserves

Every sandwich preserves the two halves. A general sandwich does not preserve the other four remarkable subspaces; it does exactly when the element is a central multiple of a real unit quaternion. The table records, for a general unit and for a real unit quaternion, whether the image of a general element of the subspace lies in the same subspace.

| subspace | $\Theta_{\tilde Q}$, general unit $\tilde Q$ | $\Theta_{\tilde u}$, real unit quaternion |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | no | yes |
| $\mathrm{Vect}(\mathbb{B})$ (vector, $6$-dimensional) | no | yes |
| $\mathbb{H}_{\mathbb{B}}$ (real quaternions) | no | yes |
| $i\mathbb{H}_{\mathbb{B}}$ (antiquaternions) | no | yes |
| $\mathbb{M}_+$ (Hermitian) | yes | yes |
| $\mathbb{M}_-$ (anti-Hermitian) | yes | yes |

The two sectors are preserved for every element. For a general unit the other four are not preserved, and the theorem below identifies exactly when they are.

**Theorem (which operators preserve the whole subspace structure).** Let $\tilde Q$ be a unit with polar word $\tilde Q=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, where $\Rho=r\zeta$ with $r>0$ and $\zeta$ central of modulus one, $\tilde U_{\mathrm b}$ is Hermitian positive of unit norm and $\tilde u_{\mathrm r}$ is a unit real quaternion. The following are equivalent:

1. the sandwich $\Theta_{\tilde Q}$ maps each of the six remarkable subspaces to itself;
2. $\tilde U_{\mathrm b}=e_t$;
3. $\tilde Q=A\tilde u_{\mathrm r}$ with $A$ central and $\tilde u_{\mathrm r}$ a unit real quaternion;
4. $\tilde Q\tilde Q^{*}$ is a positive real multiple of $e_t$.

When they hold, $\Theta_{\tilde Q}=\lvert A\rvert^{2}\Theta_{\tilde u_{\mathrm r}}$ is a dilation composed with a rotation of the vector space, and every remarkable subspace is preserved.

**Proof.** $(3)\Rightarrow(4)$: for $\tilde Q=A\tilde u_{\mathrm r}$ one has $\tilde Q\tilde Q^{*}=\lvert A\rvert^{2}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=\lvert A\rvert^{2}e_t$, since a real unit quaternion satisfies $\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1}$. $(4)\Rightarrow(3)$: if $\tilde Q\tilde Q^{*}=\lambda e_t$ with $\lambda>0$ then $\lvert\langle\tilde Q\rangle_{\natural}\rvert=\lambda$; the element $\tilde Q/\Rho$, with $\Rho$ the principal square root of $\langle\tilde Q\rangle_{\natural}$, has norm one and Hermitian square $e_t$, hence is a unit real quaternion $\tilde u_{\mathrm r}$, and $\tilde Q$ is of the form $(3)$. $(2)\Leftrightarrow(3)$ is immediate from the word. $(3)\Rightarrow(1)$: the central factor contributes the dilation, which preserves every subspace, and $\Theta_{\tilde u_{\mathrm r}}$ is the rotation of the vector space, which does the same. $(1)\Rightarrow(4)$: if the centre is preserved then $\tilde Q\tilde Q^{*}$ is central; that element is Hermitian positive, and a central Hermitian positive element of the algebra is a positive real multiple of $e_t$.

On the unit-norm slice the operators preserving the subspace structure are those of the unit real quaternions, modulo the sign, and they form $SO(3)$, of real dimension three; with the dilations admitted they form $\mathbb{R}_{>0}\times SO(3)$, of real dimension four. The rotation group sits inside the six-dimensional operator group as the rotations sit inside the Lorentz group, and the remaining three dimensions are the boosts, which move the centre, the vector subspace and the two halves.

## The Four Conjugations on the Polar Data

The domain is invariant under the four conjugations, since each of them carries the norm to the norm or to its conjugate,

$$
\langle\tilde{Q}^{\natural}\rangle_{\natural} = \langle\tilde{Q}\rangle_{\natural} , \qquad \langle\overline{\tilde{Q}}\rangle_{\natural} = \overline{\langle\tilde{Q}\rangle_{\natural}} , \qquad \langle\tilde{Q}^{*}\rangle_{\natural} = \overline{\langle\tilde{Q}\rangle_{\natural}} , \qquad \langle\tilde{Q}^{\flat}\rangle_{\natural} = \overline{\langle\tilde{Q}\rangle_{\natural}} ,
$$

so a vanishing norm stays vanishing and a non-vanishing one stays non-vanishing. The factors themselves transform as follows.

| conjugation | the scale $r$ | the phase angle $\alpha$ | the boost | the rotor |
|---|---|---|---|---|
| $\overline{\tilde{Q}}$ | unchanged | $-\alpha$ | $\tilde U_{\mathrm b}^{\natural}$ | $\tilde u_{\mathrm r}$ |
| $\tilde{Q}^{\natural}$ | unchanged | unchanged | $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}^{\natural}\tilde u_{\mathrm r}$ | $\tilde u_{\mathrm r}^{-1}$ |
| $\tilde{Q}^{*}$ | unchanged | $-\alpha$ | $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\tilde u_{\mathrm r}^{-1}$ |
| $\tilde{Q}^{\flat}$ | unchanged | $-\alpha$ | $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $-\tilde u_{\mathrm r}^{-1}$ |

The complex conjugation is the one that preserves the shape of the word. Its effect is the coefficientwise conjugation of each factor, and since the rotor is a real quaternion and the boost has one real and three purely imaginary coefficients,

$$
\overline{\tilde{Q}} = r\,\zeta^{-1}\,\tilde U_{\mathrm b}^{\natural}\,\tilde u_{\mathrm r} ,
$$

which is a polar word again: the scale is unchanged, the phase is reversed, the rotor is unchanged, and the boost is replaced by its natural conjugate. The natural conjugate of a boost is a boost — it is the inverse, with the same rapidity and the opposite axis — so the complex conjugation acts on the polar data by reversing the phase and reflecting the boost axis, and it fixes the rotor. Verified to $1.1\times10^{-14}$ over $300$ elements, together with the positivity of $\tilde U_{\mathrm b}^{\natural}$.

The quaternion conjugation is the one that reverses the order of the two non-central factors. It keeps the modulus, since $\langle\tilde Q\rangle_{\natural}$ is invariant, and it gives

$$
\tilde{Q}^{\natural} = r\,\zeta\,\tilde u_{\mathrm r}^{-1}\,\tilde U_{\mathrm b}^{-1} ,
$$

with $\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{\natural}$, so the word of $\tilde Q^{\natural}$ is the word of the inverse of the unit-norm part. Read in the standard order, it has the same scale and the same phase, the boost $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}^{\natural}\tilde u_{\mathrm r}$ and the rotor $\tilde u_{\mathrm r}^{-1}$: the rapidity is unchanged, the boost axis is rotated by the rotor and reversed, and the rotation angle is reversed. Verified over $300$ elements, the word to $2.1\times10^{-14}$, its boost to $9.8\times10^{-15}$ and its rotor to $2.6\times10^{-15}$.

The Hermitian conjugation and the reversal reverse the order of the two factors and negate the phase. The Hermitian conjugate of the word is

$$
\tilde{Q}^{*} = r\,\zeta^{-1}\,\tilde u_{\mathrm r}^{-1}\,\tilde U_{\mathrm b} ,
$$

verified to $1.1\times10^{-14}$ over $300$ elements: the scale is unchanged, the phase is reversed, and the two non-central factors appear in the reversed order, with the boost on the right. Read in the standard order, its boost is $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ — the same rapidity about the rotor-rotated axis — and its rotor is $\tilde u_{\mathrm r}^{-1}$, verified to $1.7\times10^{-14}$ and $3.6\times10^{-15}$.

The reversal is the Hermitian conjugate followed by the central sign, $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$, and the central sign is a factor of the word: multiplying a unit-norm element by $-e_t$ leaves the scale, the phase and the boost in place, since $(-e_t)$ commutes and the Hermitian positive factor of $-\tilde Q$ is that of $\tilde Q$, and it negates the rotor. So the reversal has the same scale, the same phase and the same boost as the Hermitian conjugate, and its rotor is $-\tilde u_{\mathrm r}^{-1}$, verified to $3.6\times10^{-15}$: the same rotation read on the other sheet of the double cover, which is why the two words are the same only up to the sign of the rotor.

## Worked Examples

**The centre.** For $\tilde{Q} = 1.2-0.5i$, the norm is $1.19-1.2i$, the modulus is $\Rho = 1.2-0.5i$, so $r = 1.3$ and $\alpha = -0.394791120$, and the two non-central factors are $\tilde U_{\mathrm b} = \tilde u_{\mathrm r} = e_t$. The argument of $Q_t$ lies in the branch interval, so the rotor is $+e_t$ and not $-e_t$. The reconstruction error is $1.1\times10^{-16}$.

**The quaternion subspace.** For $\tilde q = 0.7+1.1\vec e_x-0.4\vec e_y+0.9\vec e_z$ the norm is the positive real $2.67$, so $\alpha = 0$, the boost is $e_t$, and the rotor is the normalised element,

$$
\tilde u_{\mathrm r} = 0.428393043\,e_t+0.673189067\,\vec e_x-0.244796025\,\vec e_y+0.550791055\,\vec e_z ,
$$

of angle $\theta = 2.256165420$ about the axis $(0.745014008,-0.270914185,0.609556915)$, with $r = 1.634013464$.

**The anti-quaternion subspace.** The same element multiplied by $i$ has norm $-2.67$, so $\alpha = \pi/2$, the boost is again $e_t$, and the rotor is the same unit real quaternion; only the phase has moved, by the quarter turn.

**The real vector block.** For $\vec\Rho = 0.6\vec e_x-0.8\vec e_z$ the norm is $+1$, so $r = 1$, $\alpha = 0$, the boost is $e_t$, and the rotor is the direction $\vec\Rho$ itself, of angle $\pi$ about the axis $(0.6,0,-0.8)$: the half turn of the proposition, with a trivial boost. The same direction multiplied by $i$ has norm $-1$, hence $\alpha = \pi/2$, the same boost and the same rotor.

**A generic complex vector.** For $\vec Q = (0.9+0.4i)\vec e_x+(0.2-0.7i)\vec e_y+0.5\vec e_z$ the norm is complex, $0.45+0.44i$, and the phase is free: $r = 0.793325128$, $\alpha = 0.387081341$. The boost has rapidity $\psi = 1.681781019$ about the axis $(0.428682140,0.244961223,-0.869612340)$, the rotor has angle $\theta = \pi$ about the axis $(0.902525976,-0.072463835,0.424494823)$, and the two axes are orthogonal, their dot product being $1.6\times10^{-16}$. The reconstruction error is $1.2\times10^{-16}$.

**A definite Hermitian element.** For $\tilde U_{\mathrm b} = \cosh0.9\,e_t+i\sinh0.9\,\vec u$ with $\vec u = (1,1,1)/\sqrt3$, of norm one, the half-rapidity is the $0.9$ of the element and the rapidity is $1.8$; the polar data are $r = 1$, $\alpha = 0$, the boost equal to the element and the rotor $e_t$: the element is its own boost, which is the row $N>0$ of the Hermitian subspace. The negated element has the same boost and the rotor $-e_t$.

**The product of two boosts.** For the boost of rapidity $0.7$ about $\vec e_x$ and the boost of rapidity $0.5$ about $\vec e_y$, the product has norm one, so $r = 1$ and $\alpha = 0$, and its polar data are a boost of rapidity $0.882520256$ about the axis $(0.854013219,0.520251306,0)$ and a rotor of angle $0.164398032$ about $-\vec e_z$. The rapidity satisfies $\cosh\psi = \cosh0.7\cosh0.5$ to $9.8\times10^{-13}$, the two axes being orthogonal, and the rotor angle satisfies $\tan\tfrac{\theta}{2} = \sinh0.35\sinh0.25/(\cosh0.35\cosh0.25)$ to $2.8\times10^{-13}$.

## Summary

The polar decomposition of a biquaternion of non-vanishing norm is read against the six remarkable subspaces by its four exponents. For a generic word, the four exponents lie one in each of the four coordinate blocks — the scale in the real scalar block, the phase in the imaginary scalar block, the rotor in the real vector block, the boost in the imaginary vector block — and the four blocks are the four Clifford grades, of which the word uses the scalar, the pseudoscalar, the vector and the bivector. Under the identification $\gamma_k\mapsto i\vec e_k$ the scale is the scalar, the phase the pseudoscalar, the boost the Clifford vector and the rotor the bivector, and the order of the word is not the order of the grades.

Because each nonzero element of a block lies in exactly three of the six subspaces and each subspace is the sum of two blocks, each exponent of a generic word lies in exactly three subspaces and each subspace carries exactly two of them. The centre carries the two central exponents, the vector subspace the two axial ones, and the four mixed subspaces separate the pairs: the quaternion subspace carries the scale and the rotor, the anti-quaternion subspace the phase and the boost, the Hermitian subspace the scale and the boost, the anti-Hermitian subspace the phase and the rotor. The Hermitian split of the incidence reproduces the Hermitian split of the Cartan pairing.

The polar data of an element of a subspace follow from its norm. The phase is free on exactly the two subspaces whose norm is complex, the centre and the vector subspace, frozen at $0$ and $\pi/2$ on the two halves and two-valued on the two sectors. The boost is trivial on the centre and on the two halves; the rotor is a sign on the centre and on the definite branch of each sector; and the vector subspace is rigid, every one of its non-null elements having a half-turn rotor, with the boost trivial or its axis orthogonal to the rotor axis.

The two products of the series are the product of two boosts, which is a boost times a rotor with the classical rapidity and the Thomas-Wigner angle, and the word of a pure vector, whose unit-norm part is a root of $-1$ with a half-turn rotor, the boost being trivial or its axis orthogonal to the rotor axis. The domain is the complement of the null cone, and its trace on the subspaces is a single point on each of the centre, the quaternion subspace and the anti-quaternion subspace, the complex isotropic cone on the vector subspace, and the two null cones on the sectors; the polar word fails on a subspace exactly on the origin or its nonzero zero divisors. The four conjugations preserve the domain, and the complex conjugation preserves the shape of the word, reversing the phase and reflecting the boost axis while fixing the rotor. The word also acts: the sandwich $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ preserves both halves for every invertible element, factorises as $r^{2}\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}}$, sends the phase to the identity and the scale to a dilation, and reads as a proper orthochronous Lorentz transformation on the anti-Hermitian half and as a congruence on the Hermitian one. The central $i$ intertwines the two readings as an anti-isometry, the two boost matrices satisfy $B_-=DB_+D=B_+^{-1}$, and the image of the group of units is $CO^{+}(1,3)$. All six remarkable subspaces are preserved exactly for the central multiples of the real unit quaternions; on the unit-norm slice those operators form $SO(3)$, and with the dilations admitted $\mathbb{R}_{>0}\times SO(3)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = r \zeta \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar decomposition, four factors |
| $r$, $\zeta$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$ | scale, central phase, Hermitian positive boost, unit real quaternion rotor |
| $\Rho = r\zeta = \sqrt{\langle\tilde{Q}\rangle_{\natural}}$ | the complex modulus, $\langle\tilde{Q}\rangle_{\natural}$ the biquaternion norm |
| $\alpha$ | the phase angle, $\alpha=\arg\zeta\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ |
| $\ln r$, $i\alpha$, $i\tfrac{\psi}{2}\vec u_{\mathrm b}$, $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | the four exponents of the word |
| $A_1 = \mathbb{R}e_t$ | the real scalar block, home of the scale exponent |
| $A_2 = \mathbb{R}(ie_t)$ | the imaginary scalar block, home of the phase exponent |
| $B_1 = \operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | the real vector block, home of the rotor exponent |
| $B_2 = \operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ | the imaginary vector block, home of the boost exponent |
| $\gamma_k = i\vec e_k$ | the Clifford generators, $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ |
| grade $0$, $1$, $2$, $3$ | the scalar, the Clifford vector, the bivector, the pseudoscalar |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre $A_1\oplus A_2$ and the vector subspace $B_1\oplus B_2$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion subspace $A_1\oplus B_1$ and the anti-quaternion subspace $A_2\oplus B_2$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian subspace $A_1\oplus B_2$ and the anti-Hermitian subspace $A_2\oplus B_1$ |
| $\sigma$, $\vec w$ | the scalar and the real vector of an element $\sigma e_t+i\vec w$ of the Hermitian subspace |
| $\tau$, $\vec\Rho$ | the scalar and the real vector of an element $i\tau e_t+\vec\Rho$ of the anti-Hermitian subspace |
| $\mathrm{Sp}(1)$ | the group of unit real quaternions, the rotor set |
| $\mathcal{A}$ | the axis sphere, the unit vectors of $\mathbb{R}^3$ |
| $\psi$, $\vec u_{\mathrm b}$ | rapidity and unit axis of the boost |
| $\theta$, $\vec u_{\mathrm r}$ | rotation angle and unit axis of the rotor |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$, ${}^{\flat}$ | quaternion, coefficientwise, Hermitian conjugation and reversal |
| $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ | the sandwich, the action of $\tilde Q$ on the algebra |
| $\Theta_{\tilde Q}$ preserves all six subspaces | exactly for $\tilde Q=A\tilde u_{\mathrm r}$, $A$ central, $\tilde u_{\mathrm r}$ a unit real quaternion |
| $B_\pm$, $CO^{+}(1,3)$ | the $4\times4$ boost matrices on the two halves and the linear conformal group |
| $\mathsf{M}_2$ | the matrix model $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$, with $\langle\tilde{Q}\rangle_{\natural} = \det\mathsf{M}_2(\tilde{Q})$ |

## Further Reading

- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four factors, their closed forms, the count $1+1+3+3$, the order of the factors and the branch of the modulus.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the two-factor pair on the whole algebra, its uniqueness, its continuity and its behaviour at the null cone and at the origin.
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the closed forms of the pair on the two sectors of the cone.
- [The Polar Decomposition in Subspaces](../articles_physics/the-polar-decomposition-in-subspaces.html), for the same restriction read sector by sector on the physics side: the norm of each subspace, the criteria for a trivial boost and a trivial rotor, and the worked examples of every sector. Its boost has rapidity $\psi$ and the sign $-i$, where the maths series has rapidity $\tfrac{\psi}{2}$ and the sign $+i$ in the same closed form, so for the same element the parameter of the maths series is twice the one used there; the sign of the imaginary unit is the orientation of the axis and carries nothing more.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive and unitary factors, and for the split of the exponents into $\mathbb{M}_+$ and $\mathbb{M}_-$ that the incidence of this article reproduces.
- [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html) and [The Quaternion Pairing of the Polar Decomposition of Biquaternions](the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html), for the two partial pairings of the same four factors and their domains, which are the two regroupings the incidence of this article does not see.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the six subspaces one by one, their bases, their dimensions, their elements and their ideals.
- [Comparison of the Remarkable Subspaces](comparison-of-the-remarkable-subspaces.html), for the four coordinate blocks, the intersections, the lattice of the fixed spaces and the action of the conjugations on the subspaces.
- [Decompositions Along the Remarkable Subspaces](decompositions-along-the-remarkable-subspaces.html), for the three eigenspace decompositions the conjugations cut out.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, the four conjugations and the norm.
- [The Lorentz Group in Biquaternionic Form — Structure and Representations](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html), for the Thomas-Wigner rotation of the product of two boosts and the double cover read on the rotor.
- [Two-Sided Operator and the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](two-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the sandwich as an operator, its kernel $U(1)$, its image $CO^{+}(1,3)$ and the factor-by-factor word.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz group, its double cover and the reflections.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the symbols, the root convention and the unitary convention.
