# __The Polar Element Representation and Remarkable Subspaces__

## Introduction

A biquaternion with non-vanishing norm has the polar representation

$$
\tilde{Q} = r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
$$

of *The Polar Element Representation of Biquaternions*: the positive real scale $r$, the central phase $e^{i\alpha}$ on the branch $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, the Hermitian positive unit-norm boost $\tilde U_{\mathrm b}$ and the unit real quaternion rotor $\tilde u_{\mathrm r}$.

The algebra carries six **remarkable subspaces**, defined in *Introduction to the Remarkable Subspaces*: the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$.

This article reads the polar representation against those six subspaces, in the algebra. The per-sector reading of the same restriction is *The Polar Element Representation in Subspaces*, on the physics side; the restrictions are quoted here, not re-derived.

**The result, in one sentence.** The four exponents of the polar word lie one in each of the four coordinate blocks of the algebra, so that each exponent lies in exactly three of the six remarkable subspaces and each remarkable subspace contains exactly two of the exponents, and the representation fails on a subspace exactly on its zero divisors.

Four things are established, in this order. The four blocks and the exponent of each factor are identified. The blocks are put against the Clifford grades and against the six subspaces, which are their sums two by two. The incidence of the exponents with the subspaces is tabulated, with the polar data each subspace carries. The two products of the series — of two boosts, and of the word at a pure vector — are computed, and the domain and the conjugations of the word close the account.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has the basis $e_0,e_1,e_2,e_3$ with $e_1e_2 = e_3$ and the central scalar imaginary $i$, $i^2 = -1$. An element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$, with $Q_\mu\in\mathbb{C}$; the quaternion conjugation is $\tilde{Q}^{\natural} = Q_0e_0-\vec Q$, the coefficientwise conjugation is $\overline{\tilde{Q}}$, the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the reversal is $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$. The norm is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^{2} = \det\mathsf{M}_2(\tilde{Q})$, complex in general, and the domain of the representation is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. The symbols $r$, $e^{i\alpha}$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$, $\rho = re^{i\alpha}$, $\psi$, $\theta$, $\hat u_{\mathrm b}$, $\hat u_{\mathrm r}$, $\mathcal{A}$ and $N$ are those of the companion article, and the subspaces $\mathbb{M}_\pm$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ are the remarkable subspaces of *Introduction to the Remarkable Subspaces*. The four coordinate blocks $A_1$, $A_2$, $B_1$, $B_2$ are those of *Comparison of the Remarkable Subspaces*.

No physics is invoked; the physical reading is cited where it clarifies the algebra.

## The Four Exponents of the Word

Each of the four factors is the exponential of a single element of the algebra, which is the reading of *The Polar Element Representation of Biquaternions*, §*The Exponentials of the Factors*:

$$
\tilde{Q} = \exp(\ln r)\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\hat u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\hat u_{\mathrm r}\Bigr) .
$$

The four exponents are one real parameter times one **root** of the algebra, and the square of the root decides the character of the exponential.

| factor | exponent | root | square of the root | character |
|---|---|---|---|---|
| $r$ | $\ln r$ | $e_0$ | $+e_0$ | hyperbolic, degenerate |
| $e^{i\alpha}$ | $i\alpha$ | $i$ | $-e_0$ | trigonometric, central |
| $\tilde U_{\mathrm b}$ | $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ | $i\hat u_{\mathrm b}$ | $+e_0$ | hyperbolic |
| $\tilde u_{\mathrm r}$ | $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | $\hat u_{\mathrm r}$ | $-e_0$ | trigonometric |

The scale and the boost stand on a root of $+e_0$, one of them the central $e_0$ and one of them the Hermitian pure element $i\hat u_{\mathrm b}$; the phase and the rotor stand on a root of $-e_0$, one of them the central $i$ and one of them the real pure quaternion $\hat u_{\mathrm r}$.

The two axes are unit elements of the algebra as well: $\hat u_{\mathrm b}$ and $\hat u_{\mathrm r}$ are unit real pure quaternions, members of the axis sphere $\mathcal{A}$, and $i$ and $e_0$ are the two central unit elements.

## The Four Coordinate Blocks

The four **coordinate blocks** of the algebra are the pieces into which the eight real coordinates group (*Comparison of the Remarkable Subspaces*, §*Remarkable Subspaces and the Coordinate Blocks*):

$$
A_1 = \mathbb{R}e_0 , \qquad A_2 = \mathbb{R}(ie_0) , \qquad B_1 = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\} , \qquad B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\} .
$$

The two scalar blocks $A_1,A_2$ have real dimension one, the two vector blocks $B_1,B_2$ have real dimension three, and the four of them add to the algebra, $A_1\oplus A_2\oplus B_1\oplus B_2 = \mathbb{B}$.

**The four exponents occupy the four blocks, one block each.** Comparing the coordinates of the four exponents with the definitions above,

| exponent | block | the block | factor |
|---|---|---|---|
| $\ln r$ | $A_1 = \mathbb{R}e_0$ | the real scalar line | the scale |
| $i\alpha$ | $A_2 = \mathbb{R}(ie_0)$ | the imaginary scalar line | the central phase |
| $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | $B_1 = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | the real vector block | the rotor |
| $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ | $B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | the imaginary vector block | the boost |

**Theorem (the block reading of the polar word).** Each one of the four exponents of the polar word lies in exactly one of the four coordinate blocks, and every one of the four blocks carries exactly one exponent.

**Proof.** The exponent $\ln r$ is a real multiple of $e_0$, hence in $A_1$; the exponent $i\alpha$ is a real multiple of $ie_0$, hence in $A_2$; the exponent $\tfrac{\theta}{2}\hat u_{\mathrm r}$ has three real coordinates on $e_1,e_2,e_3$ and vanishing others, hence is in $B_1$; and the exponent $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ has three real coordinates on $ie_1,ie_2,ie_3$ and vanishing others, hence is in $B_2$. Since the blocks are disjoint, the assignment is a bijection between the four exponents and the four blocks. $\square$

The additivity of the dimensions of the blocks is the block form of the count of the four factors,

$$
1+1+3+3 = 8 = \dim_{\mathbb{R}}\mathbb{B} ,
$$

and it is the same statement as the independence of the four factors in *The Polar Element Representation of Biquaternions*.

Because the four exponents lie in the four blocks and the four blocks add to the algebra, **the four exponents of a generic polar word are linearly independent**: they occupy one direction in each block, so they span a real four-dimensional subspace of $\mathbb{B}$, one dimension in each block, and the word is generated, block by block, by one scalar, one pseudoscalar, one Clifford vector and one bivector generator, in the grade notation of the next section.

## The Blocks and the Four Grades

Under the identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, $\gamma_k\mapsto ie_k$ (*Comparison of the Remarkable Subspaces*, §*Remarkable Subspaces and the Coordinate Blocks*), the four blocks are the four Clifford grades.

| block | $A_1$ | $B_2$ | $B_1$ | $A_2$ |
|---|---|---|---|---|
| grade | $0$ | $1$ | $2$ | $3$ |
| basis | $e_0$ | $ie_1,ie_2,ie_3$ | $e_1,e_2,e_3$ | $ie_0$ |
| exponent it carries | $\ln r$ | $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ | $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | $i\alpha$ |
| factor | the scale | the boost | the rotor | the central phase |

**The four factors of the polar word are the four Clifford grades, one factor to a grade**, and the order of the grades is not the order of the word: the word is written scale, phase, boost, rotor, which is grade $0$, grade $3$, grade $1$, grade $2$.

Two of the four exponents are written as a Clifford element with no comment. The boost exponent is the Clifford vector

$$
i\tfrac{\psi}{2}\hat u_{\mathrm b} = \tfrac{\psi}{2}\bigl(\hat u_{\mathrm b,1}\gamma_1+\hat u_{\mathrm b,2}\gamma_2+\hat u_{\mathrm b,3}\gamma_3\bigr) ,
$$

because $ie_k = \gamma_k$ for $k=1,2,3$. The rotor exponent is the Clifford **bivector**

$$
\tfrac{\theta}{2}\hat u_{\mathrm r} = -\tfrac{\theta}{2}\bigl(\hat u_{\mathrm r,1}\gamma_2\gamma_3+\hat u_{\mathrm r,2}\gamma_3\gamma_1+\hat u_{\mathrm r,3}\gamma_1\gamma_2\bigr) ,
$$

because $e_1 = -\gamma_2\gamma_3$, $e_2 = -\gamma_3\gamma_1$ and $e_3 = -\gamma_1\gamma_2$. The scale exponent is the scalar and the phase exponent the pseudoscalar,

$$
\ln r\in\mathbb{R} , \qquad i\alpha = \alpha\,\gamma_1\gamma_2\gamma_3 ,
$$

since $ie_0 = (ie_1)(ie_2)(ie_3) = \gamma_1\gamma_2\gamma_3$.

The naming of the two vector blocks is the trap the comparison article records: the block that the algebra calls the real vector block is the grade-two block, and the block that it calls the imaginary vector block is the grade-one block. So the rotor, not the boost, is the bivector of the Clifford reading, and the boost, not the rotor, is its vector.

**Remark.** The grade reading separates the four factors by the kind of object each one is: a number (the scale), a pseudoscalar (the phase), a vector (the boost) and a bivector (the rotor). In the physical reading of the companion articles this is the algebraic content of the statement that a rotation is generated by a bivector and a boost by a vector.

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

Two of the six subspaces are the two doubles of the blocks, the centre $A_1\oplus A_2$ and the vector subspace $B_1\oplus B_2$; the other four are the four mixed pairs, one scalar block with one vector block, and the four mixed pairs are exactly the four ways of choosing one of $A_1,A_2$ and one of $B_1,B_2$.

The table is the whole relation between the blocks and the subspaces. It is a six-row table of two-block sums, and it is why the six subspaces are six and not eight: the eight sign patterns of the four blocks under a conjugation pair up into the six sums.

## The Incidence of the Four Exponents and the Six Subspaces

The block reading of the word and the block reading of the subspaces give the incidence of the exponents with the subspaces, by one substitution: an exponent that lies in a block lies in every subspace that contains the block.

| exponent | its block | the subspaces that contain it |
|---|---|---|
| $\ln r$ (scale) | $A_1$ | $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ |
| $i\alpha$ (phase) | $A_2$ | $\mathbb{C}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ |
| $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ (boost) | $B_2$ | $\mathrm{Vect}(\mathbb{B})$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ |
| $\tfrac{\theta}{2}\hat u_{\mathrm r}$ (rotor) | $B_1$ | $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ |

**Theorem (the incidence).** Each of the four exponents of the polar word lies in exactly three of the six remarkable subspaces, and each of the six remarkable subspaces contains exactly two of the four exponents.

**Proof.** Each exponent lies in exactly one block, by the block reading of the word; each block lies in exactly three remarkable subspaces, by the six-row table above; hence each exponent lies in exactly three of them. The dual statement is the same count read row by row of the subspace table: the centre contains $A_1$ and $A_2$, the vector subspace $B_1$ and $B_2$, the quaternion subspace $A_1$ and $B_1$, the anti-quaternion subspace $A_2$ and $B_2$, the Hermitian subspace $A_1$ and $B_2$, and the anti-Hermitian subspace $A_2$ and $B_1$. The counts agree: $4\times3 = 12 = 6\times2$. $\square$

Read subspace by subspace, the incidence gives the pair of exponents each subspace carries:

| subspace | the two exponents it carries | names |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\ln r$, $i\alpha$ | the modulus |
| $\mathrm{Vect}(\mathbb{B})$ | $i\tfrac{\psi}{2}\hat u_{\mathrm b}$, $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | the two axes |
| $\mathbb{H}_{\mathbb{B}}$ | $\ln r$, $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | the scale and the rotor |
| $i\mathbb{H}_{\mathbb{B}}$ | $i\alpha$, $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ | the phase and the boost |
| $\mathbb{M}_+$ | $\ln r$, $i\tfrac{\psi}{2}\hat u_{\mathrm b}$ | the hyperbolic pair |
| $\mathbb{M}_-$ | $i\alpha$, $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | the trigonometric pair |

Three consequences follow at once.

- **No subspace carries all four exponents, and none carries fewer than two.** The word never degenerates to a single subspace, and no subspace can explain the whole word.
- **The centre and the vector subspace carry the two pairs of the same kind.** The centre carries the modulus, that is its two central exponents; the vector subspace carries the two axes, that is its two non-central ones. These are the two subspaces that are sums of the two blocks of one kind.
- **The four mixed subspaces separate the two pairs.** The quaternion and anti-quaternion subspaces separate the real scalar block from the imaginary one and the two vector blocks from each other; the Hermitian and anti-Hermitian subspaces separate the blocks by the reality of their coordinates.

The incidence also matches the Hermitian split of the exponents of *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions*: the scale exponent and the boost exponent lie in $\mathbb{M}_+$ and the phase exponent and the rotor exponent in $\mathbb{M}_-$. The split separates the two exponents of each pair, the modular pair and the axial pair, and it is the reason the Cartan pairing is called Hermitian.

## The Polar Data Carried by Each Subspace

The incidence says which exponents a subspace can carry. The polar data of an element of a subspace say more: which of the four factors are trivial there, and what the phase is.

The behaviour of the phase is decided by the norm alone. The phase is $\alpha = \tfrac{1}{2}\arg N(\tilde{Q})$, so it is constant on a subspace exactly when the argument of the norm is constant there, and the six subspaces realise the possible behaviours.

| subspace | the norm $N(\tilde{Q})$ | the phase |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Q_0^{2}$, complex anisotropic | free, $\arg Q_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | $(\vec Q,\vec Q)$, complex indefinite | free |
| $\mathbb{H}_{\mathbb{B}}$ | a sum of four real squares, positive definite | $0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | minus a sum of four real squares, negative definite | $\pi/2$ |
| $\mathbb{M}_+$ | $\sigma^{2}-\lvert\vec w\rvert^{2}$, real indefinite | $0$ or $\pi/2$ |
| $\mathbb{M}_-$ | $\lvert\vec\rho\rvert^{2}-\tau^{2}$, real indefinite | $0$ or $\pi/2$ |

**The phase is a free coordinate on exactly the two subspaces whose norm is complex**, the centre and the vector subspace; it is frozen on the two halves, at $0$ and at $\pi/2$; and it is a two-valued label on the two sectors, where the norm is real indefinite. The norm is complex on exactly the two subspaces that are not real forms of the algebra, which is the same pair.

The two non-central factors behave as follows, on the same subspaces.

| subspace | the boost | the rotor |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $e_0$ | $\pm e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | a boost, or $e_0$ on the lines of a single direction | a half turn |
| $\mathbb{H}_{\mathbb{B}}$ | $e_0$ | free in $\mathrm{Sp}(1)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $e_0$ | free in $\mathrm{Sp}(1)$ |
| $\mathbb{M}_+$, $N>0$ | the normalised element, up to sign | a sign, $\pm e_0$ |
| $\mathbb{M}_+$, $N<0$ | a nontrivial boost | a half turn |
| $\mathbb{M}_-$, $N>0$ | a nontrivial boost | a half turn |
| $\mathbb{M}_-$, $N<0$ | the element times $-i/r$ | a sign, $\pm e_0$ |

Four of the rows are degenerate cases worth naming, and the derivations are those of the per-sector article.

- **The centre.** Both non-central factors are trivial, $\tilde U_{\mathrm b} = \tilde u_{\mathrm r} = e_0$, up to the sign of the rotor; a central element is its own modulus. The rotor is $+e_0$ exactly when the argument of $Q_0$ lies in the branch interval $(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, and $-e_0$ otherwise, which is the residual sign of the two branches of the square root.
- **The two halves.** The boost is $e_0$ and the rotor absorbs the whole unit-norm part. On the quaternion subspace the phase is $0$ and the rotor is $\tilde Q/|\tilde Q|$; on the anti-quaternion subspace the phase is $\pi/2$ and the rotor is $\tilde Q/(i|\tilde Q|)$. The two subspaces carry the same rotor set, the same group $\mathrm{Sp}(1)$, with the phase shifted by a quarter turn.
- **The real vector block.** An element of $B_1$ has a positive real norm, so the phase is $0$, the boost is $e_0$, and the rotor is the direction of the element, a half turn about it.
- **A definite Hermitian element.** On $\mathbb{M}_+$ with $N>0$ the normalised element is Hermitian and definite, so it is a boost up to sign, and the rotor is a sign. The same holds on $\mathbb{M}_-$ with $N<0$, where the normalised element is $i$ times a boost.

The pattern of the last two rows is the symmetry of the two sectors: **on each sector the sign of the norm decides which of the two non-central factors is trivial.** A definite element of a sector is a boost with a sign rotor; an indefinite one has a half-turn rotor and a genuine boost.

| sector | $N>0$ | $N<0$ |
|---|---|---|
| $\mathbb{M}_+$ | the boost carries the element, the rotor is a sign | the rotor carries a direction, the boost is genuine |
| $\mathbb{M}_-$ | the rotor carries a direction, the boost is genuine | the boost carries the element, the rotor is a sign |

The two rows are exchanged row for row under the interchange $\mathbb{M}_+\leftrightarrow\mathbb{M}_-$ with $N\mapsto-N$, which is the central unit $i$ read on the sectors.

The signs in the two sign rows are the signs of the two central coordinates of the sector: on $\mathbb{M}_+$ with $N>0$ the rotor is $\operatorname{sign}(\sigma)e_0$, where $\sigma = \operatorname{Re}Q_0$, and on $\mathbb{M}_-$ with $N<0$ it is $\operatorname{sign}(\tau)e_0$, where $\tau = \operatorname{Im}Q_0$ is the time coordinate. Both were verified over the random samples of each branch, with the boost matching the element to $1.8\times10^{-15}$ on $\mathbb{M}_+$ and to $7.2\times10^{-15}$ on $\mathbb{M}_-$.

## The Boost Family and the Rotor Group

The four factors are four subsets of the algebra, one per block, and two of them are groups and two are not.

- The scale runs over $\mathbb{R}_{>0}$, a half-line of the real scalar block.
- The phase runs over $U(1)$, the unit circle of the imaginary scalar block.
- The boost runs over the Hermitian positive definite elements of norm one, the unit sphere of the positive cone in $\mathbb{M}_+$.
- The rotor runs over $\mathrm{Sp}(1)$, the unit sphere of the quaternion subspace.

The rotor set is a **group**: the product of two unit real quaternions is a unit real quaternion. The phase set is a group as well, and the two of them are the groups the word carries.

The boost set is **not** a group: the product of two Hermitian positive elements is not Hermitian in general, and it is not positive definite when it is, so the product of two boosts leaves the boost set. The product of two boosts is a boost times a rotor,

$$
\tilde U_{\mathrm b}(a,\hat a)\,\tilde U_{\mathrm b}(b,\hat b) = \tilde U_{\mathrm b}(\psi,\hat u)\,\tilde u_{\mathrm r}(\theta,\hat n) ,
$$

and the parameters are the classical ones. Writing $\phi$ for the angle between the two axes $\hat a,\hat b$, the rapidity of the product is fixed by

$$
\cosh\psi = \cosh a\cosh b+\sinh a\sinh b\cos\phi ,
$$

and the residual rotor by

$$
\tan\frac{\theta}{2} = \frac{\sinh\frac{a}{2}\sinh\frac{b}{2}\sin\phi}{\cosh\frac{a}{2}\cosh\frac{b}{2}+\sinh\frac{a}{2}\sinh\frac{b}{2}\cos\phi} .
$$

Both identities were verified in double precision over $300$ random pairs, the first to $9.8\times10^{-13}$ and the second to $2.8\times10^{-13}$. The residual rotor is the Thomas-Wigner rotation of the physics articles, *The Lorentz Group in Biquaternionic Form — Structure and Representations*; the algebra records it as the statement that the boost set is a symmetric space and not a group, and the word records it as the escape into the rotor factor.

The two axes are two directions of the vector subspace, $\hat u_{\mathrm b}$ and $\hat u_{\mathrm r}$, and the question whether they commute is the question whether the word may be reordered. They commute exactly when they are parallel, and then the word is a single boost-rotation about the common axis; the bracket is developed in *The Polar Element Representation of Biquaternions*, §*The Order of the Factors*.

## The Vector Subspace Is Rigid

The vector subspace is the one subspace on which the polar data of every element is fixed in shape. The block table gives the reason: the vector subspace is the sum $B_1\oplus B_2$ of the two blocks that carry the two non-central exponents, and nothing else. The two central coordinates vanish, and their vanishing is a condition on the two non-central factors.

**Proposition (the half-turn rotor of a pure vector).** Let $\vec Q$ be an element of the vector subspace with $N(\vec Q)\neq0$, and let $\vec Q = \rho\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ be its polar word. Then the rotor is a half turn, $\theta = \pi$, and the rotor axis is orthogonal to the boost axis.

**Proof.** Write the two non-central factors in their closed forms,

$$
\tilde U_{\mathrm b} = \cosh\tfrac{\psi}{2}\,e_0+i\sinh\tfrac{\psi}{2}\,\hat u_{\mathrm b} , \qquad \tilde u_{\mathrm r} = \cos\tfrac{\theta}{2}\,e_0+\sin\tfrac{\theta}{2}\,\hat u_{\mathrm r} ,
$$

and compute the scalar part of their product. Only the scalar part is needed, and the two scalar parts contribute additively, because the scalar part of the product of a real scalar and an element is the product of the scalars:

$$
\operatorname{Sc}\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr) = \cosh\tfrac{\psi}{2}\cos\tfrac{\theta}{2}+i\sinh\tfrac{\psi}{2}\sin\tfrac{\theta}{2}\operatorname{Sc}\bigl(\hat u_{\mathrm b}\hat u_{\mathrm r}\bigr) .
$$

Now $\hat u_{\mathrm b}$ and $\hat u_{\mathrm r}$ are real pure quaternions, so the scalar part of their product is minus their dot product,

$$
\operatorname{Sc}\bigl(\hat u_{\mathrm b}\hat u_{\mathrm r}\bigr) = -\,(\hat u_{\mathrm b},\hat u_{\mathrm r}) .
$$

The element $\vec Q$ is pure, so $\operatorname{Sc}(\vec Q) = 0$, and the modulus $\rho$ is central, so $\operatorname{Sc}(\tilde U_{\mathrm b}\tilde u_{\mathrm r}) = 0$ as well. The right-hand side is the sum of a real number and a purely imaginary one, so both vanish:

$$
\cosh\tfrac{\psi}{2}\cos\tfrac{\theta}{2} = 0 , \qquad \sinh\tfrac{\psi}{2}\sin\tfrac{\theta}{2}\,(\hat u_{\mathrm b},\hat u_{\mathrm r}) = 0 .
$$

The first gives $\cos\tfrac{\theta}{2} = 0$, that is $\theta = \pi$, since $\theta\in[0,2\pi]$ and the other factor is positive. The second, with $\sin\tfrac{\theta}{2} = 1$, gives either $\psi = 0$ or $(\hat u_{\mathrm b},\hat u_{\mathrm r}) = 0$: the boost is trivial or the two axes are orthogonal. $\square$

**Corollary (the normalised piece of a pure vector is a root of $-1$).** With the notation of the proposition, the unit-norm part $\vec Q/\rho$ satisfies

$$
\left(\frac{\vec Q}{\rho}\right)^{\natural} = -\frac{\vec Q}{\rho} , \qquad \left(\frac{\vec Q}{\rho}\right)^{2} = -e_0 ,
$$

so it is a root of $-1$ of the algebra, pure and of unit norm. Both identities were verified to $2.6\times10^{-15}$ over $500$ random complex vectors, together with the two conclusions of the proposition: the scalar part of the rotor vanished to $7.8\times10^{-16}$ and the dot product of the two axes to $7.5\times10^{-16}$.

**Converse.** The argument reverses. If the rotor of the word of an element is a half turn about an axis orthogonal to the boost axis, then the scalar part of $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ vanishes, so the element with that word and any central modulus is pure. The vector subspace is therefore exactly the set of elements whose word has a half-turn rotor orthogonal to the boost axis.

The proposition is the algebra behind the reading of the per-sector article, where the rotor of an element of the vector subspace is a unit vector of the plane of the two real parts; the block form of the same fact is that the vector subspace is the sum of the two non-central blocks and nothing else.

## The Domain Read on the Subspaces

The domain of the polar representation is the complement of the null cone $\{N = 0\}$, and the intersection of the null cone with a subspace is read from the norm of the subspace.

| subspace | the zeros of the norm | real dimension | the representation |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $0$ alone, the norm is anisotropic | $0$ | on the punctured centre |
| $\mathrm{Vect}(\mathbb{B})$ | the complex isotropic cone $(\vec Q,\vec Q) = 0$ | $4$ | fails on the cone |
| $\mathbb{H}_{\mathbb{B}}$ | $0$ alone, the norm is definite | $0$ | on the punctured subspace |
| $i\mathbb{H}_{\mathbb{B}}$ | $0$ alone, the norm is definite | $0$ | on the punctured subspace |
| $\mathbb{M}_+$ | the cone $\sigma^{2} = \lvert\vec w\rvert^{2}$ | $3$ | fails on the cone |
| $\mathbb{M}_-$ | the cone $\lvert\vec\rho\rvert^{2} = \tau^{2}$ | $3$ | fails on the cone |

**Theorem (the domain on the subspaces).** The polar representation exists on the whole of the punctured centre, punctured quaternion subspace and punctured anti-quaternion subspace, and it fails on the other three subspaces exactly on their nonzero zero divisors.

**Proof.** By the table, the norm of an element of each of the centre, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ vanishes only at the origin: the centre is a field, the quaternion subspace is a division algebra, and the anti-quaternion subspace is its purely imaginary copy, where the norm is minus a sum of squares. On the other three subspaces the vanishing of the norm is one complex equation on the vector subspace and two real equations on each sector, defining the isotropic cone and the two light cones, and $N = 0$ with $\tilde Q\neq0$ is exactly the zero-divisor condition. $\square$

The three subspaces on which the representation never fails are exactly the three that carry no nonzero zero divisor, which is the statement of *Introduction to the Remarkable Subspaces* read through the polar representation. The intersection of the domain with the algebra is thus the complement of a single cone, and the trace of that cone on the subspaces is a single point on each of the centre, the quaternion subspace and the anti-quaternion subspace, the four-dimensional complex isotropic cone on the vector subspace, and a three-dimensional light cone on each sector.

The behaviour of the word at the boundary is the statement of *The Polar Element Representation of Biquaternions*, §*The Boundary of the Family*: along a path to the cone of $\mathbb{M}_+$ the scale collapses and the word tends to the minimal idempotent $\tfrac{1}{2}(e_0+\hat\Xi i)$ with $\hat\Xi$ a unit real vector, Hermitian, of norm zero and idempotent. The boundary of the family of boosts is the family of minimal idempotents of the Hermitian subspace, and the two objects — the boundary of the domain and the set of minimal idempotents — are one cone.

## The Four Conjugations on the Polar Data

The domain is invariant under the four conjugations, since each of them carries the norm to the norm or to its conjugate,

$$
N(\tilde{Q}^{\natural}) = N(\tilde{Q}) , \qquad N(\overline{\tilde{Q}}) = \overline{N(\tilde{Q})} , \qquad N(\tilde{Q}^{*}) = \overline{N(\tilde{Q})} , \qquad N(\tilde{Q}^{\flat}) = \overline{N(\tilde{Q})} ,
$$

so a vanishing norm stays vanishing and a non-vanishing one stays non-vanishing. The factors themselves transform as follows.

| conjugation | the scale $r$ | the phase angle $\alpha$ | the boost | the rotor |
|---|---|---|---|---|
| $\overline{\tilde{Q}}$ | unchanged | $-\alpha$ | $\tilde U_{\mathrm b}^{\natural}$ | $\tilde u_{\mathrm r}$ |
| $\tilde{Q}^{\natural}$ | unchanged | unchanged | $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}^{\natural}\tilde u_{\mathrm r}$ | $\tilde u_{\mathrm r}^{-1}$ |
| $\tilde{Q}^{*}$ | unchanged | $-\alpha$ | the reversed word | the reversed word |
| $\tilde{Q}^{\flat}$ | unchanged | $-\alpha$ | the reversed word | the reversed word |

The complex conjugation is the one that preserves the shape of the word. Its effect is the coefficientwise conjugation of each factor, and since the rotor is a real quaternion and the boost has one real and three purely imaginary coefficients,

$$
\overline{\tilde{Q}} = r\,e^{-i\alpha}\,\tilde U_{\mathrm b}^{\natural}\,\tilde u_{\mathrm r} ,
$$

which is a polar word again: the scale is unchanged, the phase is reversed, the rotor is unchanged, and the boost is replaced by its natural conjugate. The natural conjugate of a boost is a boost — it is the inverse, with the same rapidity and the opposite axis — so the complex conjugation acts on the polar data by reversing the phase and reflecting the boost axis, and it fixes the rotor. Verified to $8.9\times10^{-16}$ over $300$ elements, together with the positivity of $\tilde U_{\mathrm b}^{\natural}$.

The quaternion conjugation is the one that reverses the order of the two non-central factors. It keeps the modulus, since $N$ is invariant, and it gives

$$
\tilde{Q}^{\natural} = r\,e^{i\alpha}\,\tilde u_{\mathrm r}^{-1}\,\tilde U_{\mathrm b}^{-1} ,
$$

with $\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{\natural}$, so the word of $\tilde Q^{\natural}$ is the word of the inverse of the unit-norm part. Read in the standard order, it has the same scale and the same phase, the boost $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}^{\natural}\tilde u_{\mathrm r}$ and the rotor $\tilde u_{\mathrm r}^{-1}$: the rapidity is unchanged, the boost axis is rotated by the rotor and reversed, and the rotation angle is reversed. Verified to $4.5\times10^{-16}$ over $300$ elements.

The Hermitian conjugation and the reversal reverse the order of the two factors and negate the phase. The Hermitian conjugate of the word is

$$
\tilde{Q}^{*} = r\,e^{-i\alpha}\,\tilde u_{\mathrm r}^{-1}\,\tilde U_{\mathrm b} ,
$$

verified to $6.3\times10^{-15}$ over $300$ elements: the scale is unchanged, the phase is reversed, and the two non-central factors appear in the reversed order, with the boost on the right. The reversal differs from it by the central sign, $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$, and the two of them therefore have the same polar data.

## Worked Examples

**The centre.** For $\tilde{Q} = 1.2-0.5i$, the norm is $1.19-1.2i$, the modulus is $\rho = 1.2-0.5i$, so $r = 1.3$ and $\alpha = -0.394791120$, and the two non-central factors are $\tilde U_{\mathrm b} = \tilde u_{\mathrm r} = e_0$. The argument of $Q_0$ lies in the branch interval, which is the rotor $+e_0$ rather than $-e_0$. The reconstruction error is $2.5\times10^{-16}$.

**The quaternion subspace.** For $h = 0.7+1.1e_1-0.4e_2+0.9e_3$ the norm is the positive real $2.67$, so $\alpha = 0$, the boost is $e_0$, and the rotor is the normalised element,

$$
\tilde u_{\mathrm r} = 0.428393043\,e_0+0.673189067\,e_1-0.244796025\,e_2+0.550791055\,e_3 ,
$$

of angle $\theta = 2.256165420$ about the axis $(0.745014008,-0.270914185,0.609556915)$, with $r = 1.634013464$.

**The anti-quaternion subspace.** The same element multiplied by $i$ has norm $-2.67$, so $\alpha = \pi/2$, the boost is again $e_0$, and the rotor is the same unit real quaternion; only the phase has moved, by the quarter turn.

**The real vector block.** For $\vec\rho = 0.6e_1-0.8e_3$ the norm is $+1$, so $r = 1$, $\alpha = 0$, the boost is $e_0$, and the rotor is the direction $\vec\rho$ itself, of angle $\pi$ about the axis $(0.6,0,-0.8)$: the half turn of the proposition, with a trivial boost. The same direction multiplied by $i$ has norm $-1$, hence $\alpha = \pi/2$, the same boost and the same rotor.

**A generic complex vector.** For $\vec Q = (0.9+0.4i)e_1+(0.2-0.7i)e_2+0.5e_3$ the norm is complex, $0.45+0.44i$, and the phase is free: $r = 0.793325128$, $\alpha = 0.387081341$. The boost has rapidity $\psi = 1.681781019$ about the axis $(0.428682140,0.244961223,-0.869612340)$, the rotor has angle $\theta = \pi$ about the axis $(0.902525976,-0.072463835,0.424494823)$, and the two axes are orthogonal, their dot product being $1.6\times10^{-16}$. The reconstruction error is $1.2\times10^{-16}$.

**A definite Hermitian element.** For $\tilde U_{\mathrm b} = \cosh0.9\,e_0+i\sinh0.9\,\hat u$ with $\hat u = (1,1,1)/\sqrt3$, of norm one and rapidity $1.8$, the polar data are $r = 1$, $\alpha = 0$, the boost equal to the element and the rotor $e_0$: the element is its own boost, which is the row $N>0$ of the Hermitian subspace. The negated element has the same boost and the rotor $-e_0$.

**The product of two boosts.** For the boost of rapidity $0.7$ about $e_1$ and the boost of rapidity $0.5$ about $e_2$, the product has norm one, so $r = 1$ and $\alpha = 0$, and its polar data are a boost of rapidity $0.882520256$ about the axis $(0.854013219,0.520251306,0)$ and a rotor of angle $0.164398032$ about $-e_3$. The rapidity satisfies $\cosh\psi = \cosh0.7\cosh0.5$ to $9.8\times10^{-13}$, the two axes being orthogonal, and the rotor angle satisfies $\tan\tfrac{\theta}{2} = \sinh0.35\sinh0.25/(\cosh0.35\cosh0.25)$ to $2.8\times10^{-13}$.

## Summary

The polar representation of a biquaternion of non-vanishing norm is read against the six remarkable subspaces by its four exponents. The four exponents lie one in each of the four coordinate blocks — the scale in the real scalar block, the phase in the imaginary scalar block, the rotor in the real vector block, the boost in the imaginary vector block — and the four blocks are the four Clifford grades, of which the word uses the scalar, the pseudoscalar, the vector and the bivector. Under the identification $\gamma_k\mapsto ie_k$ the scale is the scalar, the phase the pseudoscalar, the boost the Clifford vector and the rotor the bivector, and the order of the word is not the order of the grades.

Because each block lies in exactly three of the six subspaces and each subspace is the sum of two blocks, each exponent lies in exactly three subspaces and each subspace carries exactly two exponents. The centre carries the two central exponents, the vector subspace the two axial ones, and the four mixed subspaces separate the pairs: the quaternion subspace carries the scale and the rotor, the anti-quaternion subspace the phase and the boost, the Hermitian subspace the scale and the boost, the anti-Hermitian subspace the phase and the rotor. The Hermitian split of the incidence reproduces the Hermitian split of the Cartan pairing.

The polar data of an element of a subspace follow from its norm. The phase is free on exactly the two subspaces whose norm is complex, the centre and the vector subspace, frozen at $0$ and $\pi/2$ on the two halves and two-valued on the two sectors. The boost is trivial on the centre and on the two halves; the rotor is a sign on the centre and on the definite branch of each sector; and the vector subspace is rigid, every one of its non-null elements having a half-turn rotor about an axis orthogonal to the boost axis.

The two products of the series are the product of two boosts, which is a boost times a rotor with the classical rapidity and the Thomas-Wigner angle, and the word at a pure vector, whose unit-norm part is a root of $-1$ with a half-turn rotor about an axis orthogonal to the boost axis. The domain is the complement of the null cone, and its trace on the subspaces is a single point on each of the centre, the quaternion subspace and the anti-quaternion subspace, the complex isotropic cone on the vector subspace, and the two light cones on the sectors; the representation fails on a subspace exactly on its zero divisors. The four conjugations preserve the domain, and the complex conjugation preserves the shape of the word, reversing the phase and reflecting the boost axis while fixing the rotor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar representation, four factors |
| $r$, $e^{i\alpha}$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$ | scale, central phase, Hermitian positive boost, unit real quaternion rotor |
| $\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}$ | the complex modulus, $N$ the biquaternion norm |
| $\ln r$, $i\alpha$, $i\tfrac{\psi}{2}\hat u_{\mathrm b}$, $\tfrac{\theta}{2}\hat u_{\mathrm r}$ | the four exponents of the word |
| $A_1 = \mathbb{R}e_0$ | the real scalar block, home of the scale exponent |
| $A_2 = \mathbb{R}(ie_0)$ | the imaginary scalar block, home of the phase exponent |
| $B_1 = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | the real vector block, home of the rotor exponent |
| $B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | the imaginary vector block, home of the boost exponent |
| $\gamma_k = ie_k$ | the Clifford generators, $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ |
| grade $0$, $1$, $2$, $3$ | the scalar, the Clifford vector, the bivector, the pseudoscalar |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre $A_1\oplus A_2$ and the vector subspace $B_1\oplus B_2$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion subspace $A_1\oplus B_1$ and the anti-quaternion subspace $A_2\oplus B_2$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian subspace $A_1\oplus B_2$ and the anti-Hermitian subspace $A_2\oplus B_1$ |
| $\mathrm{Sp}(1)$ | the group of unit real quaternions, the rotor set |
| $\mathcal{A}$ | the axis sphere, the unit vectors of $\mathbb{R}^3$ |
| $\psi$, $\hat u_{\mathrm b}$ | rapidity and unit axis of the boost |
| $\theta$, $\hat u_{\mathrm r}$ | rotation angle and unit axis of the rotor |
| $\phi$ | the angle between the two axes of a pair of boosts |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$, ${}^{\flat}$ | quaternion, coefficientwise, Hermitian conjugation and reversal |
| $\mathsf{M}_2$ | the matrix model $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$, with $N(\tilde{Q}) = \det\mathsf{M}_2(\tilde{Q})$ |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the four factors, their exponentials, the count $1+1+3+3$, the order of the factors and the boundary of the family on the null cone.
- *The Polar Element Representation in Subspaces* (`articles_physics/the-polar-element-representation-in-subspaces.md`), for the same restriction read sector by sector on the physics side: the norm of each subspace, the criteria for a trivial boost and a trivial rotor, and the worked examples of every sector. Its boost is written $\exp(-i\psi\hat u_{\mathrm b})$ where the maths series writes $\exp(i\tfrac{\psi}{2}\hat u_{\mathrm b})$, so its rapidity parameter is the double of the present one for the same element.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the Hermitian positive and unitary factors, and for the split of the exponents into $\mathbb{M}_+$ and $\mathbb{M}_-$ that the incidence of this article reproduces.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`) and *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the two partial pairings of the same four factors and their domains, which are the two regroupings the incidence of this article does not see.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the six subspaces one by one, their bases, their dimensions, their elements and their ideals.
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the four coordinate blocks, the intersections, the lattice of the fixed spaces and the action of the conjugations on the subspaces.
- *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces.md`), for the three eigenspace decompositions the conjugations cut out.
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations and the norm.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the Thomas-Wigner rotation of the product of two boosts and the double cover read on the rotor.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the symbols, the root convention and the unitary convention.
