# __The Minimal Left Ideals__

## Introduction

The algebra has two minimal left ideals, and they are the two spinor spaces. This article constructs them from the idempotents of the frame, states their bases and their complex dimension, and reads the two chiralities.

The chain of the block ends here: the algebra is not a division algebra, it carries non-trivial idempotents, a non-trivial idempotent produces the minimal left ideal $\mathbb{B}\tilde\Pi$, and an element of that ideal is a spinor. The article assumes the Peirce frame and the regular module; it prepares the category of modules, where the same two ideals appear as the two simple objects.

Nothing here is a physical statement. The word spinor names an element of a minimal left ideal, and the two chiralities are the two ideals, not two states of a particle.

## The Decomposition into Minimal Left and Right Ideals

**The two idempotents generate the minimal left ideals and the minimal right ideals, and the two groupings of the four corners are the row and column readings of the Peirce table.**

A **minimal left ideal** is a nonzero left ideal containing no nonzero proper left ideal; equivalently, a simple submodule of the left regular module. A **minimal right ideal** is defined the same way on the right.

The two idempotents group the basis into one-sided ideals in a second way. The two **left ideals** $\mathbb{B}\tilde\Pi_+, \mathbb{B}\tilde\Pi_-$ and the two **right ideals** $\tilde\Pi_+\mathbb{B}, \tilde\Pi_-\mathbb{B}$ are one-sided, and

$$
\boxed{\;
\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_- = (\mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\vec\Upsilon_y) \oplus (\mathbb{C}\vec\Upsilon_x \oplus \mathbb{C}\tilde\Pi_-)
\;},
$$

$$
\mathbb{B} = \tilde\Pi_+\mathbb{B} \oplus \tilde\Pi_-\mathbb{B} = (\mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\vec\Upsilon_x) \oplus (\mathbb{C}\vec\Upsilon_y \oplus \mathbb{C}\tilde\Pi_-).
$$

The first exhibits $\mathbb{B}$ as a direct sum of the two minimal left ideals; the second exhibits it as a direct sum of the two minimal right ideals. The two groupings of the same four basis elements differ: the Peirce decomposition groups $\tilde\Pi_+$ with $\vec\Upsilon_x$ and $\tilde\Pi_-$ with $\vec\Upsilon_y$, whereas the left-ideal decomposition groups $\tilde\Pi_+$ with $\vec\Upsilon_y$ and $\tilde\Pi_-$ with $\vec\Upsilon_x$. Each left ideal is two-dimensional over $\mathbb{C}$; each right ideal is its dual. Since $\mathbb{B}$ is simple, a one-sided ideal is never two-sided; for instance $\mathbb{B}\tilde\Pi_+$ is not stable under right multiplication by $\vec\Upsilon_x$.

**Why the sum is direct, and the dimensions.** Every $\tilde Q_1 \in \mathbb{B}$ satisfies $\tilde Q_1 = \tilde Q_1(\tilde\Pi_+ + \tilde\Pi_-) = \tilde Q_1\tilde\Pi_+ + \tilde Q_1\tilde\Pi_-$, so the two left ideals span. Their intersection is zero: if $\tilde Q_1\tilde\Pi_+ = \tilde Q_2\tilde\Pi_-$, then multiplying on the right by $\tilde\Pi_+$ and using $\tilde\Pi_+^2 = \tilde\Pi_+$ and $\tilde\Pi_-\tilde\Pi_+ = 0$ gives $\tilde Q_1\tilde\Pi_+ = 0$. The basis above reads $\mathbb{B}\tilde\Pi_+ = \mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\vec\Upsilon_y$, of dimension $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$, with $\mathbb{B}\tilde\Pi_- = \mathbb{C}\vec\Upsilon_x \oplus \mathbb{C}\tilde\Pi_-$ for the second; together they account for $4 + 4 = 8 = \dim_{\mathbb{R}} \mathbb{B}$. Each is a minimal left ideal, by the primitivity of $\tilde\Pi_+$ and $\tilde\Pi_-$ (§*Idempotents and Orthogonal Idempotents*, §*The Decomposition into Minimal Left and Right Ideals*).

**The module structure.** With the basis $\{\tilde\Pi_+, \vec\Upsilon_y\}$ the left $\mathbb{B}$-module $\mathbb{B}\tilde\Pi_+$ is $\mathbb{C}^2$, and the central element $i$ acts on it as the scalar $i$:
$$
i\,(\alpha \tilde\Pi_+ + \beta \vec\Upsilon_y) = (i\alpha)\tilde\Pi_+ + (i\beta)\vec\Upsilon_y .
$$
So the simple module underlying each minimal left ideal is the standard two-dimensional one, with $i$ acting by the identity matrix.

**Every left ideal is a direct sum of minimal left ideals, every minimal left ideal is $\mathbb{B}\tilde\Pi$ for a primitive idempotent $\tilde\Pi$, and all are isomorphic; the right ideals are dual.**

Over $\mathbb{C}$, since $\mathbb{B}$ is semisimple, every left ideal of $\mathbb{B}$ is a direct sum of minimal left ideals, and every minimal left ideal is of the form $\mathbb{B}\tilde\Pi$ for a primitive idempotent $\tilde\Pi$. The examples are the left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ of §*The Decomposition into Minimal Left and Right Ideals*, and all minimal left ideals are isomorphic as left $\mathbb{B}$-modules: a general one is obtained from $\mathbb{B}\tilde\Pi_+$ by an algebra automorphism, so it has the same shape in a suitable basis. Dually, every minimal right ideal is isomorphic to $\tilde\Pi_+\mathbb{B}$. Thus there is one isomorphism class of simple left modules and one of simple right modules. Being nonzero proper one-sided ideals, none of them is two-sided — which is exactly why their abundance is compatible with §*The Two-Sided Ideals*.

## Spinors and the Two Couples

**The four Peirce vectors split into two couples of two spinors, one couple per minimal left ideal. Left multiplication acts on each couple by the same Peirce matrix; chirality labels the couple, not a scalar of left multiplication.**

### The Two Spinor Spaces

**Definition (spinor space).** A **spinor space** of $\mathbb{B}$ is a minimal non-zero left ideal. Relative to the pair $\tilde\Pi_+,\tilde\Pi_-$ the two spinor spaces are

$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{B}_{++}\oplus\mathbb{B}_{-+}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{B}_{+-}\oplus\mathbb{B}_{--}=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$

with $\vec\Upsilon_-\in\mathbb{B}_{+-}$ and $\vec\Upsilon_+\in\mathbb{B}_{-+}$. A **spinor of first chirality** is an element of $S_+$, and a **spinor of second chirality** is an element of $S_-$. Each space has complex dimension two, and

$$
\mathbb{B}=S_+\oplus S_-.
$$

**The two couples.** The four Peirce vectors form the two **couples**

$$
\mathcal{C}_+=(\tilde\Pi_+,\ \vec\Upsilon_+),
\qquad
\mathcal{C}_-=(\vec\Upsilon_-,\ \tilde\Pi_-),
$$

each made of one idempotent and one nilpotent, each a basis of its spinor space. They are the two halves of the Peirce basis $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. For the standard pair $\vec\Upsilon_-=\vec\Upsilon_x$ and $\vec\Upsilon_+=\vec\Upsilon_y$, so the two couples are $(\tilde\Pi_+,\vec\Upsilon_y)$ and $(\vec\Upsilon_x,\tilde\Pi_-)$.

**Every element is a pair of spinors.** The splitting gives

$$
\tilde X=\tilde X\tilde\Pi_++\tilde X\tilde\Pi_-,
\qquad
\tilde X\tilde\Pi_+\in S_+,\quad\tilde X\tilde\Pi_-\in S_-.
$$

In the matrix model of §*The Peirce Coordinates and the Matrix Model* the two summands are the two columns.

**The two spaces are isomorphic as left modules.** Right multiplication by $\vec\Upsilon_-$ carries $S_+$ to $S_-$, and right multiplication by $\vec\Upsilon_+$ carries $S_-$ back:

$$
S_+\longrightarrow S_-,\quad\xi\longmapsto\xi\vec\Upsilon_-,
\qquad
S_-\longrightarrow S_+,\quad\eta\longmapsto\eta\vec\Upsilon_+.
$$

The two maps are inverse because $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$. The spaces are distinct subspaces of $\mathbb{B}$ even though they are isomorphic as left modules, so the chirality label records the embedding of the module in the algebra, not the module itself.

### The Left Action on Each Couple

**Proposition (one matrix, two couples).** In the basis $\mathcal{C}_+$ of $S_+$ and in the basis $\mathcal{C}_-$ of $S_-$, left multiplication by $\tilde P$ has the same matrix,

$$
L_{\tilde P}|_{S_+}=\mathsf M_{\tilde\Pi}(\tilde P),
\qquad
L_{\tilde P}|_{S_-}=\mathsf M_{\tilde\Pi}(\tilde P).
$$

*Proof.* From the Peirce table, in $S_+$,

$$
\tilde P\tilde\Pi_+=p_{11}\tilde\Pi_++p_{21}\vec\Upsilon_+,
\qquad
\tilde P\vec\Upsilon_+=p_{12}\tilde\Pi_++p_{22}\vec\Upsilon_+,
$$

and in $S_-$,

$$
\tilde P\vec\Upsilon_-=p_{11}\vec\Upsilon_-+p_{21}\tilde\Pi_-,
\qquad
\tilde P\tilde\Pi_-=p_{12}\vec\Upsilon_-+p_{22}\tilde\Pi_-.
$$

In each couple the first basis vector has the column $(p_{11},p_{21})$ and the second the column $(p_{12},p_{22})$, which are the two columns of $\mathsf M_{\tilde\Pi}(\tilde P)$. ∎

**Remark (chirality is not a scalar of left multiplication).** Left multiplication never mixes the two couples, because $S_\pm$ are left ideals, but inside a couple it mixes the idempotent and the nilpotent whenever $p_{12}$ or $p_{21}$ is nonzero. A basis spinor is carried to a multiple of itself exactly when the coefficient that couples it to the other member of its couple vanishes; both are carried to multiples exactly when the Peirce matrix is diagonal. In the regular case it is diagonal, and each basis spinor is carried to a multiple of itself. The degenerate case is treated in *The Spectrally Degenerate Sector*.

**Remark (the right action).** Right multiplication by $\tilde P$ sends

$$
\tilde\Pi_+\mapsto p_{11}\tilde\Pi_++p_{12}\vec\Upsilon_-,
\qquad
\vec\Upsilon_+\mapsto p_{11}\vec\Upsilon_++p_{12}\tilde\Pi_-,
$$

so it preserves $S_+$ exactly when $p_{12}=0$; it sends

$$
\vec\Upsilon_-\mapsto p_{21}\tilde\Pi_++p_{22}\vec\Upsilon_-,
\qquad
\tilde\Pi_-\mapsto p_{21}\vec\Upsilon_++p_{22}\tilde\Pi_-,
$$

so it preserves $S_-$ exactly when $p_{21}=0$. When both entries vanish, $\tilde P$ is diagonal and right multiplication is the scalar $p_{11}$ on $S_+$ and $p_{22}$ on $S_-$; the chirality of a spinor is then the scalar by which $R_{\tilde P}$ acts on it. In general the right action mixes the two chiralities, whereas the left action never does.

**Remark (the matrix picture).** In the matrix model of §*The Peirce Coordinates and the Matrix Model*, left multiplication multiplies both columns by $\mathsf M_{\tilde\Pi}(\tilde P)$, and right multiplication multiplies the whole matrix by $\mathsf M_{\tilde\Pi}(\tilde P)$ on the right and mixes the columns. This is the concrete form of the two statements above: the left action is chirality-diagonal, the right action is not.

### The Adjoint

The star sends a left ideal to a right ideal,

$$
S_+^*=(\mathbb{B}\tilde\Pi_+)^*=\tilde\Pi_+^*\mathbb{B}.
$$

For a Hermitian pair $\tilde\Pi_+^*=\tilde\Pi_+$, so the image is the first row $\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-$, a minimal right ideal and not one of the two chiralities, which are left ideals. Chirality therefore belongs to the left-ideal decomposition and not to the Hermitian structure. The spinor adjoints and the reality conditions are treated in *Spinors as Minimal Left Ideals with Inner Conjugation*.

### The Nilpotents and the Ideals

**For a nonzero nilpotent the one-sided ideal it generates equals its one-sided annihilator on each side, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$; each is a minimal one-sided ideal of real dimension four, and the ideal and the annihilator coincide exactly for the nilpotents.**

The nilpotents are the elements on which the ideal theory of the algebra is simplest, because the ideal they generate and the annihilator they determine coincide.

**Theorem.** Let $\tilde\Upsilon\neq0$ be a nilpotent and let $I_{\tilde\Upsilon}=\{\tilde Q_2:\tilde Q_2\tilde\Upsilon=0\}$ and $J_{\tilde\Upsilon}=\{\tilde Q_2:\tilde\Upsilon\tilde Q_2=0\}$ be its left and right annihilators. Then $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$; each is a minimal one-sided ideal of real dimension four, and the two coincide exactly for the nilpotents.

**Proof.** If $\tilde\Upsilon^2=0$ then $(\tilde Q_2\tilde\Upsilon)\tilde\Upsilon=\tilde Q_2\tilde\Upsilon^2=0$ for every $\tilde Q_2$, so $\mathbb{B}\tilde\Upsilon\subseteq I_{\tilde\Upsilon}$; both are nonzero proper left ideals and both are minimal of real dimension four, hence equal. The right statement is the mirror image. The converse, that coincidence forces nilpotency, is the statement for the other class in *The Six Subspaces*.

The deeper ideal theory, the Peirce decomposition, the minimal left and right ideals $\mathbb{B}\tilde\Pi_+,\mathbb{B}\tilde\Pi_-$ and the module structure of the algebra over itself, is *The Peirce Decomposition* and *The Category of Modules*; the nilpotents enter it as the off-diagonal units $\vec\Upsilon_x,\vec\Upsilon_y$.


### The Standard Idempotents and the Minimal Ideals

**The standard idempotents generate the two minimal left ideals, and the algebra is their direct sum.**

The principal left ideals $\mathbb{B}\tilde\Pi_{+}$ and $\mathbb{B}\tilde\Pi_{-}$ are the two minimal left ideals of the standard pair, and the completeness and orthogonality of the pair give the direct sum

$$
\mathbb{B}=\mathbb{B}\tilde\Pi_{+}\oplus\mathbb{B}\tilde\Pi_{-}.
$$

The two ideals are collected in the table.

| Ideal | Generator | Form | Minimality |
|---|---|---|---|
| Left | $\tilde\Pi_{+}$ | $\mathbb{B}\tilde\Pi_{+}$ | yes |
| Left | $\tilde\Pi_{-}$ | $\mathbb{B}\tilde\Pi_{-}$ | yes |
| Right | $\tilde\Pi_{+}$ | $\tilde\Pi_{+}\mathbb{B}$ | yes |
| Right | $\tilde\Pi_{-}$ | $\tilde\Pi_{-}\mathbb{B}$ | yes |

The minimality is the primitive character of the pair: the only idempotents of $\tilde\Pi_{+}\mathbb{B}\tilde\Pi_{+}$ and $\tilde\Pi_{-}\mathbb{B}\tilde\Pi_{-}$ are $0$ and the identity of the corner, so neither ideal contains a proper nonzero ideal of its own. The Peirce decomposition, the corner algebras and the matrix units of the two ideals are *The Peirce Decomposition*.


## The Idempotents and the Ideals in the Remarkable Subspaces

An element of $\mathbb{B}$ is an **idempotent** if $\tilde\Pi^2 = \tilde\Pi$, a **left ideal** is a $\mathbb{C}$-subspace $I$ with $\mathbb{B}I \subseteq I$, a **right ideal** a subspace $J$ with $J\mathbb{B} \subseteq J$, and a **two-sided ideal** one that is both. An idempotent splits the algebra as

$$
\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}(e_t - \tilde\Pi) ,
$$

its complement $e_t - \tilde\Pi$ is the complementary idempotent, and when the idempotent is primitive the two summands are minimal one-sided ideals. The classifications themselves are the business of *Idempotents* and *The Peirce Decomposition*; what is recorded here is their restriction to the remarkable subspaces.

**The ideals.** $\mathbb{B}$ is **simple**, its only two-sided ideals being $0$ and $\mathbb{B}$, and it has **length two** as a left module over itself, so that every nonzero proper left ideal is **minimal**, of real dimension $4$, and dually every nonzero proper right ideal is a minimal right ideal of real dimension $4$. Two consequences are immediate. Since the only two-sided ideals are $0$ and $\mathbb{B}$, **no subspace of the remarkable subspaces is a two-sided ideal**. And each of the remarkable subspaces **generates the whole algebra on both sides**,

$$
\boxed{\;\mathbb{B}\mathbb{S} = \mathbb{S}\mathbb{B} = \mathbb{B} \qquad \text{for each of the remarkable subspaces } \mathbb{S}\;},
$$

because a left ideal containing a unit is everything, and each of the remarkable subspaces contains a unit: $e_t$ is in the centre, in the quaternion subspace and in $\mathbb{M}_+$, the element $\vec e_x$ is in the vector subspace and in $\mathbb{M}_-$, and $ie_t$ is in the anti-quaternion subspace.

**Theorem (the annihilators of the zero divisors).** Let $\tilde Q_1 \neq 0$ be a zero divisor of $\mathbb{B}$, so that $Q_{1t}^2+Q_{1x}^2+Q_{1y}^2+Q_{1z}^2 = 0$. Write $I_{\tilde Q_1}$ for the set of $\tilde Q_2$ with $\tilde Q_2\tilde Q_1 = 0$ and $J_{\tilde Q_1}$ for the set of $\tilde Q_2$ with $\tilde Q_1\tilde Q_2 = 0$. Then $I_{\tilde Q_1}$ is a minimal left ideal, $J_{\tilde Q_1}$ is a minimal right ideal, and each has real dimension $4$.

**Theorem (the ideal generated against the annihilator).** For a nonzero **nilpotent** of the vector subspace, $\vec P^2 = 0$, the ideal generated and the annihilator coincide, $\mathbb{B}\vec P = I_{\vec P}$ and $\vec P\mathbb{B} = J_{\vec P}$; for every other zero divisor $\tilde Q$ the two are distinct and therefore complementary,

$$
\boxed{\;\mathbb{B} = \mathbb{B}\tilde Q \oplus I_{\tilde Q} = \tilde Q\mathbb{B} \oplus J_{\tilde Q}\;}.
$$

**Proof of the nilpotent case.** If $\vec P^2 = 0$ then $(\tilde Q_3\vec P)\vec P = \tilde Q_3\vec P^2 = 0$ for every $\tilde Q_3$, so $\mathbb{B}\vec P \subseteq I_{\vec P}$, and $\mathbb{B}\vec P$ contains $\vec P \neq 0$ while $I_{\vec P}$ is proper, so both are nonzero proper left ideals; by the length-two statement they are both minimal of real dimension $4$, hence equal. The right-hand statement is the mirror image, using $(\vec P\tilde Q_3)\vec P = 0$ on the left instead.

The subspaces of the remarkable subspaces that carry a zero divisor are the vector subspace, $\mathbb{M}_+$ and $\mathbb{M}_-$, by the sections above; the other three — the centre, the quaternion subspace and the anti-quaternion subspace — consist of $0$ and units, and determine no minimal ideal at all. So the ideal content of the remarkable subspaces is carried by three of them:

| subspace | left ideal generated | units in it | minimal one-sided ideals determined |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{B}$ | all $Ae_t$ with $A \neq 0$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $\vec e_x$ | $\mathbb{B}\vec P = I_{\vec P}$ and $\vec P\mathbb{B} = J_{\vec P}$, $\vec P$ a nonzero nilpotent |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $e_t$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $ie_t$ | none |
| $\mathbb{M}_+$ | $\mathbb{B}$ | $e_t$ | $\mathbb{B}\tilde\Pi$, $I_{\tilde\Pi} = \mathbb{B}(e_t-\tilde\Pi)$ and their right-hand twins, $\tilde\Pi$ a Hermitian idempotent |
| $\mathbb{M}_-$ | $\mathbb{B}$ | $\vec e_x$ | the same four, unchanged |

Every one of the minimal ideals determined by the remarkable subspaces meets the remarkable subspaces in the same way, two real dimensions in the vector subspace, one in $\mathbb{M}_+$ and one in $\mathbb{M}_-$:

| minimal ideal | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| each $\mathbb{B}\vec P$, $\vec P\mathbb{B}$, $\mathbb{B}\tilde\Pi$, $\mathbb{B}\tilde\Pi'$, $\tilde\Pi\mathbb{B}$, $\tilde\Pi'\mathbb{B}$ | $0$ | $2$ | $0$ | $0$ | $1$ | $1$ |

the entries being real dimensions; so the minimal ideals meet exactly the three subspaces that carry zero divisors, and avoid the other three entirely.

## The Matrix Model

**The roots of $+1$.** A matrix $X$ with $X^2=\mathrm I_2$ is conjugate to a diagonal matrix with entries $\pm1$: it is a scalar involution $\pm\mathrm I_2$ when the two entries agree, and a traceless involution when they differ. The six subspaces carry the following roots.

| Subspace | Roots of $+1$ |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\pm\mathrm I_2$ |
| $\mathrm{Vect}(\mathbb{B})$ | the traceless involutions, $\operatorname{Tr}X=0$, $X^2=\mathrm I_2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\pm\mathrm I_2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the Hermitian traceless involutions $\vec u\cdot\vec\sigma$, $\lvert\vec u\rvert=1$ |
| $\mathbb{M}_+$ | $\pm\mathrm I_2$ and $\vec u\cdot\vec\sigma$, $\lvert\vec u\rvert=1$ |
| $\mathbb{M}_-$ | none |

The last row is immediate: an anti-Hermitian matrix is conjugate to a diagonal matrix with purely imaginary entries, so it cannot be conjugate to $\operatorname{diag}(\pm1)$. The table is the matrix form of the root table of §*The Idempotents in the Six Subspaces* above.

**The idempotents.** A matrix $\Pi$ with $\Pi^2=\Pi$ is a projector; if it is not $0$ or $\mathrm I_2$, its rank is one. In the six subspaces the only nontrivial idempotents are

$$
\Pi(\vec u)=\tfrac12\bigl(\mathrm I_2+\vec u\cdot\vec\sigma\bigr),
\qquad \vec u\in\mathbb{R}^3,\quad\lvert\vec u\rvert=1,
$$

and they all lie in the Hermitian subspace $\mathbb{M}_+$. The centre and the quaternion subspace contain only $0$ and $\mathrm I_2$; the vector subspace, the anti-quaternion subspace and $\mathbb{M}_-$ contain only $0$. The family is the matrix form of the Hermitian idempotents $\tfrac12(e_t+i\vec u)$ of §*The Idempotents in the Six Subspaces* above.

**The nilpotents.** The roots of $0$ are the nilpotents, and a nonzero nilpotent has trace zero and rank one. It lies in the vector subspace and on the null cone, and it lies in none of the other five subspaces except through the common origin. The idempotent and the nilpotent are the two ends of the rank-one variety: $\Pi^2=\Pi$ and $X^2=0$.



### Idempotents and Their Projectors

**Every idempotent is the member attached to $+1$ of the pair of a root, and its complement the member attached to $-1$; the standard pair carries the two projections that resolve the identity, and a Hermitian idempotent satisfies $\tilde\Pi^{*}=\tilde\Pi$ and lies in $\mathbb{M}_+$.**

Every idempotent is the member attached to $+1$ of the pair of a root: for $\tilde\Pi$ idempotent the element $\tilde\Xi=2\tilde\Pi-e_t$ is a root of $+1$, and $\tilde\Pi_{+}(\tilde\Xi)=\tilde\Pi$ while $\tilde\Pi_{-}(\tilde\Xi)=e_t-\tilde\Pi$. The **complement** $e_t-\tilde\Pi$ is therefore the member attached to $-1$ of the same pair, an idempotent orthogonal to $\tilde\Pi$ by §*The Arithmetic of the Pair*, and the direct sum decomposition of the underlying $\mathbb{C}$-module,

$$
\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_t-\tilde\Pi)\mathbb{B},\qquad \mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_t-\tilde\Pi),
$$

is the one read there at a single root. This is the algebraic content of the statement that idempotents correspond to projectors under multiplication: multiplication by the idempotent is the projector, its complement gives the complementary projector, and the algebra splits into the image of one and the image of the other.

For the standard pair, left multiplication gives the two projections

$$
P_{+}:\tilde Q\longmapsto\tilde\Pi_{+}\tilde Q,\qquad
P_{-}:\tilde Q\longmapsto\tilde\Pi_{-}\tilde Q,
$$

with

$$
P_{+}^{2}=P_{+},\qquad P_{-}^{2}=P_{-},\qquad P_{+}P_{-}=P_{-}P_{+}=0,\qquad P_{+}+P_{-}=\mathrm{id}.
$$

The identity $P_{+}+P_{-}=\mathrm{id}$ is the **resolution of the identity**; the images are the two minimal right ideals $\tilde\Pi_{+}\mathbb{B}$ and $\tilde\Pi_{-}\mathbb{B}$. Right multiplication gives the two projections onto the minimal left ideals $\mathbb{B}\tilde\Pi_{+}$ and $\mathbb{B}\tilde\Pi_{-}$, with the same identities. The two left projectors are collected in the table.

| Projector | Formula | Image | Kernel |
|---|---|---|---|
| $P_{+}$ | $\tilde Q\mapsto\tilde\Pi_{+}\tilde Q$ | $\tilde\Pi_{+}\mathbb{B}$ | $\tilde\Pi_{-}\mathbb{B}$ |
| $P_{-}$ | $\tilde Q\mapsto\tilde\Pi_{-}\tilde Q$ | $\tilde\Pi_{-}\mathbb{B}$ | $\tilde\Pi_{+}\mathbb{B}$ |

A **Hermitian idempotent** is one fixed by ${}^{*}$, $\tilde\Pi^{*}=\tilde\Pi$; it is the kind carried by the Hermitian subspace. Since $\tilde\Pi^{*}=\overline{\tilde\Pi^{\natural}}$, the non-trivial Hermitian idempotents are the members of the second family of §*The Families of Idempotents*, and they lie in $\mathbb{M}_+$.


## Summary

- A non-trivial idempotent $\tilde\Pi$ gives the minimal left ideal $\mathbb{B}\tilde\Pi$, of complex dimension two and isomorphic to $\mathbb{C}^2$.
- The two ideals $\mathbb{B}\tilde\Pi$ and $\mathbb{B}\tilde\Pi'$ are the two chiralities, and the algebra is their direct sum as a left module.
- A spinor is an element of a minimal left ideal; the two couples $\mathcal{C}_\pm=(\tilde\Pi_\pm,\vec\Upsilon_\pm)$ are the bases adapted to the element.
- The left action is the same on the two chiralities; the right action mixes them.
- The two sector articles that follow are the spectral and the degenerate specialisations of this construction.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}\tilde\Pi$ | the minimal left ideal of $\tilde\Pi$ |
| $\mathcal{C}_\pm=(\tilde\Pi_\pm,\vec\Upsilon_\pm)$ | the two spinor couples |
| $\mathsf M_{\tilde\Pi}$ | the Peirce matrix acting on both |

## Further Reading

- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the corners.
- [The Regular Module](the-regular-module.html), for the ideals as submodules.
- [The Category of Modules](modules-over-the-biquaternion-algebra.html), for the classification.
- [$M_2(\mathbb{C})$ Model : Columns, Rows and the Spinor Module](m2c-representation-the-columns-the-rows-and-the-spinor-module.html), for the matrix picture.
