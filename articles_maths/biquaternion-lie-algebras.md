# __Biquaternion Lie Algebras__

## Introduction

A Lie algebra is not a property of a vector space; it is a property of a bracket on that space. The same space carries as many brackets as one gives it, and a bracket that is a Lie bracket on one subspace may fail the Jacobi identity on a larger one. The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four products — one bilinear and one sesquilinear, each in a complex and a quaternionic variant — and each product has an **antisymmetric part**, the half-difference of the product on the pair and on the pair with the two elements exchanged. The question *is $\mathbb{B}$ a Lie algebra* has no answer until the product, and hence the bracket, is named. This article answers the question product by product, and shows that the four brackets carry **one** Lie algebra and not four: on the whole space only the commutator works, and the other three do not give a second algebra but reduce to the commutator on the subspaces where their conjugations agree.

The four products are from *The Four Biquaternion Complex Products*, and the symmetric and the antisymmetric part of each are from *Decomposition of the Biquaternion Complex Products*. The **antisymmetric part** of a product $f$ is the bracket

$$
[\tilde{P},\tilde{Q}] = f(\tilde{P},\tilde{Q}) - f(\tilde{Q},\tilde{P}),
$$

always alternating. Whether it is a **Lie bracket** — bilinear over the right ring and satisfying the Jacobi identity — depends on the product and on the regime in which the product lives. Two regimes occur, and the distinction is the whole point:

- **Bilinear products.** If $f$ is bilinear over a commutative ring $R$, then the bracket is bilinear over $R$ as well, and it satisfies the Jacobi identity **as soon as $f$ is associative**; in that case it is the commutator of the algebra, the standard example of *Lie Algebras*, §*The Commutator Bracket*.
- **Sesquilinear products.** If $f$ is linear in one slot and conjugate-linear in the other, then the bracket is linear only over the fixed ring $R^{\varsigma}$, so it is at best a Lie bracket over $R^{\varsigma}$ and never a Lie bracket over the base ring; and for a product of full type the associativity of $f$ forces the twist to be invisible, so the genuinely sesquilinear case is exactly the case where the Jacobi identity fails. This is the criterion and the collapse theorem of *Lie Algebras of Sesquialgebras*, in the general framework of *Sesquialgebras*.

The four products of $\mathbb{B}$ fall into these regimes as follows.

- The **complex bilinear** product is associative, and its antisymmetric part is the commutator $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$, under which $\mathbb{B}$ is the complex Lie algebra $\mathrm{GL}(2,\mathbb{C})$; its centre is the scalar line, and the trace-free part is $\mathrm{SL}(2,\mathbb{C})$. This is the main algebra of the article.
- The **quaternionic bilinear** product is not associative, and its bracket fails Jacobi on the whole algebra; it is a Lie bracket on the vector subspace alone.
- The **complex sesquilinear** product is not associative, and its bracket fails Jacobi on the whole algebra; it is a Lie bracket on the anti-Hermitian subspace $\mathbb{M}_-$ alone.
- The **quaternionic sesquilinear** product is not associative, and its bracket fails Jacobi on the whole algebra; it is a Lie bracket on the quaternion subspace alone.

So the four brackets do not give four Lie algebras. They give **one** Lie algebra, the commutator $(\mathbb{B},[\cdot,\cdot])$, together with some of its subalgebras; wherever one of the other three brackets is a Lie bracket, it is $\pm$ the commutator, because on that subspace the two conjugations of the corresponding product agree:

| bracket | is a Lie bracket on | and there equals |
|---|---|---|
| $[\tilde{P},\tilde{Q}]_{\natural}=\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}$ | the vector subspace $\mathrm{Vect}(\mathbb{B})$ | $-\,[\tilde{P},\tilde{Q}]$ |
| $[\tilde{P},\tilde{Q}]_{*}=\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*}$ | the anti-Hermitian subspace $\mathbb{M}_-$ | $-\,[\tilde{P},\tilde{Q}]$ |
| $[\tilde{P},\tilde{Q}]_{\natural*}=\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*}$ | the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $+\,[\tilde{P},\tilde{Q}]$ |

The commutator is the infinitesimal counterpart of the group. The group of units, the exponential and its parametrisation are in *Biquaternion Lie Group and Exponential Structure*; the topology of the group is in *The Biquaternion Unit Group as a Topological Group*; and the motions the bracket generates are in *Biquaternion Rotations and Lorentz Transformations*. The algebra, its basis and its six subspaces are from *Biquaternions as a Vector Space over $\mathbb{C}$*, the two parts of the complex bilinear product are *Decomposition of the Biquaternion Complex Products*, and the behaviour of the product and the bracket on each subspace is tabulated in *Biquaternion Relations Between Subspaces*, cited below. The symmetrisation on the other side is *Biquaternion Jordan Algebras*, the companion of this article.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$. The three involutions are the natural conjugation ${}^{\natural}$, the coefficientwise conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

---

## The Four Brackets

The antisymmetric part of each of the four products is read in *Decomposition of the Biquaternion Complex Products*, where the four are tabulated. For a product $f$ write $[\tilde{P},\tilde{Q}]_f=f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P})$; the four brackets, the regime, and the ring of scalars are as follows.

| product $f$ | bracket $[\tilde{P},\tilde{Q}]_f$ | regime | scalars |
|---|---|---|---|
| $\tilde{P}\tilde{Q}$ (complex bilinear) | $\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$, the commutator | bilinear | $\mathbb{C}$ |
| $\tilde{P}^{\natural}\tilde{Q}$ (quaternionic bilinear) | $\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}$, values in $\mathrm{Vect}(\mathbb{B})$ | bilinear | $\mathbb{C}$ |
| $\tilde{P}\tilde{Q}^{*}$ (complex sesquilinear) | $\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*}$, values in $\mathbb{M}_-$ | sesquilinear | $\mathbb{R}$ |
| $\tilde{P}^{\natural}\tilde{Q}^{*}$ (quaternionic sesquilinear) | $\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*}$, values in neither $\mathbb{M}_+$ nor $\mathbb{M}_-$ | sesquilinear | $\mathbb{R}$ |

### The Failure of the Jacobi Identity

**Theorem.** Among the four brackets exactly the commutator $[\cdot,\cdot]$ satisfies the Jacobi identity on all of $\mathbb{B}$.

**Proof.** The commutator of an associative algebra satisfies the Jacobi identity, and the skew-symmetry was noted. For each of the other three a single triple witnesses the failure; the two sesquilinear brackets being only $\mathbb{R}$-bilinear, the identity is tested over $\mathbb{R}$ for them. For a bracket $[\cdot,\cdot]$ write the Jacobi sum

$$
J(\tilde{P},\tilde{Q},\tilde{R}) := \bigl[[\tilde{P},\tilde{Q}],\tilde{R}\bigr] + \bigl[[\tilde{Q},\tilde{R}],\tilde{P}\bigr] + \bigl[[\tilde{R},\tilde{P}],\tilde{Q}\bigr] ,
$$

read for each bracket in turn; it takes the following values.

| bracket | $\tilde{P},\tilde{Q},\tilde{R}$ | $J$ |
|---|---|---|
| $[\cdot,\cdot]_{\natural}$ | $e_0,\ e_1,\ e_2$ | $-4e_3$ |
| $[\cdot,\cdot]_{*}$ | $e_0,\ e_1,\ e_2$ | $4e_3$ |
| $[\cdot,\cdot]_{\natural*}$ | $e_1,\ e_2,\ ie_3$ | $4ie_0$ |

### The Lie Algebras Found

The failure on the whole algebra does not remove the structures carried by the subspaces. The commutator is a Lie bracket on every subspace where it closes, and each of the other three brackets is a Lie bracket on the subspace where its two conjugations agree, where it equals $\pm$ the commutator by the proposition below. Each product is taken in turn. The centre is a one-dimensional abelian Lie algebra for every one of the four brackets.

**The complex bilinear product $\tilde{P}\tilde{Q}$.** Bilinear over $\mathbb{C}$ and associative. Its antisymmetric part is the commutator

$$
[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P},
$$

which lands in the trace-free part $\mathrm{Vect}(\mathbb{B})$ and satisfies the Jacobi identity on all of $\mathbb{B}$. It is the commutator of the associative algebra $\mathbb{B}$ of *Lie Algebras*, §*The Commutator Bracket*.

**The quaternionic bilinear product $\tilde{P}^{\natural}\tilde{Q}$.** Bilinear over $\mathbb{C}$ and not associative. Its antisymmetric part is

$$
[\tilde{P},\tilde{Q}]_{\natural}=\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}=2\bigl(P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}\bigr),
$$

with values in $\mathrm{Vect}(\mathbb{B})$. The Jacobi identity fails at $e_0,e_1,e_2$, where the sum is $-4e_3$; on $\mathrm{Vect}(\mathbb{B})$ it holds and $[\tilde{P},\tilde{Q}]_{\natural}=-[\tilde{P},\tilde{Q}]$.

**The complex sesquilinear product $\tilde{P}\tilde{Q}^{*}$.** Linear over $\mathbb{R}$ and not associative. Its antisymmetric part $[\tilde{P},\tilde{Q}]_{*}=\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*}$ has values in $\mathbb{M}_-$. The Jacobi identity fails at $e_0,e_1,e_2$, where the sum is $4e_3$; on $\mathbb{M}_-$ it holds and $[\tilde{P},\tilde{Q}]_{*}=-[\tilde{P},\tilde{Q}]$.

**The quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$.** Linear over $\mathbb{R}$ and not associative. Its antisymmetric part $[\tilde{P},\tilde{Q}]_{\natural*}=\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*}$ has values in none of the six distinguished subspaces. The Jacobi identity fails at $e_1,e_2,ie_3$, where the sum is $4ie_0$; on $\mathbb{H}_{\mathbb{B}}$, where the two conjugations agree, it holds and $[\tilde{P},\tilde{Q}]_{\natural*}=[\tilde{P},\tilde{Q}]$.

| the product | regime and scalars | where it is a Lie bracket | the Lie algebra it gives |
|---|---|---|---|
| $\tilde{P}\tilde{Q}$ | bilinear, $\mathbb{C}$, associative | all of $\mathbb{B}$ | the commutator $(\mathbb{B},[\cdot,\cdot])\cong\mathrm{GL}(2,\mathbb{C})$ |
| $\tilde{P}^{\natural}\tilde{Q}$ | bilinear, $\mathbb{C}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathfrak{sl}(2,\mathbb{C})$, as $-$ the commutator |
| $\tilde{P}\tilde{Q}^{*}$ | sesquilinear, $\mathbb{R}$ | $\mathbb{M}_-$ | $\mathfrak{u}(2)$, as $-$ the commutator |
| $\tilde{P}^{\natural}\tilde{Q}^{*}$ | sesquilinear, $\mathbb{R}$ | $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{R}e_0\oplus\mathfrak{su}(2)$, as $+$ the commutator |

So the four brackets give one Lie algebra and not four: the first row is the algebra, and the other three rows are a second reading of three of its subalgebras and never a new one. The rest of the article keeps the two apart. §*The Lie Algebra $(\mathbb{B},[\cdot,\cdot])$*, immediately below, develops the one algebra of the table in full. §*The Three Subalgebras the Other Products Reproduce*, after that, develops the three subalgebras that the other products reach: the vector subalgebra $\mathrm{Vect}(\mathbb{B})$, reproduced by product 2; the anti-Hermitian subalgebra $\mathbb{M}_-$, reproduced by product 3; and the quaternion subalgebra $\mathbb{H}_{\mathbb{B}}$, reproduced by product 4.

---

## The Lie Algebra $(\mathbb{B},[\cdot,\cdot])$

The one algebra of the table of *The Lie Algebras Found* is the biquaternion algebra under the commutator, and this section develops it in full: the bracket and the centre, the trace-free part, the outer and the cross product, and the derived subalgebra. The subalgebras that the other three products reproduce are developed separately, after the table.

### The Commutator Bracket

The trace functional is

$$
\mathrm{Tr}(\tilde{Q}) = 2Q_0 .
$$

**Dimension.** As a complex vector space, $\mathbb{B} \cong \mathbb{C}^4$ has complex dimension $4$; as a real vector space it has real dimension $8$. The trace-free part has complex dimension $3$ and real dimension $6$.

The set $\mathbb{B}$ carries the **commutator bracket**

$$
[\tilde{P}, \tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P},
$$

under which it is a complex Lie algebra, written $\mathrm{G}$, of dimension $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$. Its center is the scalar line

$$
\mathrm{Z}(\mathrm{G}) = \mathbb{C}e_0,
$$

of complex dimension $1$ and real dimension $2$; every scalar multiple of $e_0$ commutes with all of $\mathbb{B}$. Removing the center gives the decomposition

$$
\mathrm{G} = \mathrm{B}_0 \oplus \mathbb{C}e_0,
$$

with complex dimensions $4 = 3 + 1$ and real dimensions $8 = 6 + 2$. Here $\mathrm{B}_0=\{\tilde{Q}:Q_0=0\}$ is the **trace-free subalgebra**, the complex pure-vector part, developed next.

### The Trace-Free Subalgebra

The Lie algebra of $\mathbb{B}^\times_1$ is the trace-free subalgebra

$$
\mathrm{B}_0 = \{\tilde{Q} \in \mathbb{B} : Q_0 = 0\} = \mathrm{span}_\mathbb{C}\{e_1, e_2, e_3\},
$$

of complex dimension $3$ and real dimension $6$, closed under the bracket,

$$
[e_j,e_k] = 2\sum_l \epsilon_{jkl} e_l .
$$

Over the reals it splits into two three-dimensional real subspaces,

$$
\mathrm{B}_0 = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\} \;\oplus\; \mathrm{span}_\mathbb{R}\{ie_1, ie_2, ie_3\},
$$

with real dimensions $6 = 3 + 3$. The first summand,

$$
\mathrm{K} = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\},
$$

is a Lie subalgebra, the **compact real form**, on which the bracket is twice the cross product; the second, $\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$, is not a subalgebra, since the bracket of two of its elements lands in $\mathrm{K}$. The pair is the $\mathbb{Z}/2$-grading of $\mathrm{B}_0$ by the star-involution: the elements of $\mathrm{K}$ are anti-Hermitian and those of $\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$ Hermitian, so the bracket is internal on the even part and exchanges the two on the mixed pairs.

In the fixed-point subspaces of the basic algebra article the first summand is generated by $e_k \in \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and the second by $ie_k \in \mathbb{M}_+$. These are exactly the two real three-dimensional pieces into which $\mathrm{B}_0$ splits, and the central direction $\mathbb{C}e_0$ completes the picture, $\mathrm{G} = \mathrm{B}_0 \oplus \mathbb{C}e_0$.

### The Outer Product and the Cross Product

The product of two biquaternions splits into a symmetric and an antisymmetric part, as in *Decomposition of the Biquaternion Complex Products*,

$$
\tilde{P}\tilde{Q} = \tilde{P}\bullet\tilde{Q} + \tilde{P}\wedge\tilde{Q},
$$

the **symmetrised product** $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ and the **outer product** $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$. The commutator is twice the outer product,

$$
[\tilde{P},\tilde{Q}] = \tilde{P}\tilde{Q}-\tilde{Q}\tilde{P} = 2\,\tilde{P}\wedge\tilde{Q},
$$

and the outer product of any two biquaternions is a pure vector, so the bracket depends on the vector parts alone.

**Theorem.** For two pure vectors the outer product is the cross product, and the bracket is twice either of them,

$$
\mathbf{P}\wedge\mathbf{Q} = \mathbf{P}\times\mathbf{Q}, \qquad [\mathbf{P},\mathbf{Q}] = 2\,\mathbf{P}\wedge\mathbf{Q} = 2\,\mathbf{P}\times\mathbf{Q},
$$

with the cross product taken in $\mathbb{C}^3$ under the identification $\mathrm{Vect}(\mathbb{B})\cong\mathbb{C}^3$.

**Proof.** For pure vectors the product splits as $\mathbf{P}\mathbf{Q}=-(\textstyle\sum_k P_kQ_k)e_0+\mathbf{P}\times\mathbf{Q}$ and $\mathbf{Q}\mathbf{P}=-(\textstyle\sum_k P_kQ_k)e_0-\mathbf{P}\times\mathbf{Q}$; the difference is $\mathbf{P}\mathbf{Q}-\mathbf{Q}\mathbf{P}=2\,\mathbf{P}\times\mathbf{Q}$, and the outer product is half of that difference.

The map $\mathbf{P}\mapsto\mathrm{ad}_{\mathbf{P}}|_{\mathrm{B}_0}$ is then the cross-product operator, and for a real vector part the operator so defined is antisymmetric.

### The Derived Subalgebra

The commutator of two biquaternions has vanishing scalar part, since the scalar part commutes with everything:
$$
[\tilde{P},\tilde{Q}] = [\mathbf{P},\mathbf{Q}].
$$
Hence the **derived subalgebra** is the complex span of the vector units,
$$
[\mathrm{G},\mathrm{G}] = \mathrm{B}_0 = \mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\} = \mathrm{Vect}(\mathbb{B}),
$$
of complex dimension $3$ and real dimension $6$: the derived subalgebra is exactly the vector subspace of *Biquaternions as a Vector Space over $\mathbb{C}$*, and the quotient $\mathrm{G}/[\mathrm{G},\mathrm{G}]$ is the centre $\mathbb{C}e_0$ of dimension $1$ over $\mathbb{C}$.

The action of the bracket on each of the six distinguished subspaces — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ — is the commutator row of the tables of *Biquaternion Relations Between Subspaces*, read there along with the product and the symmetrised product. In brief, the centre is central, $\mathrm{Vect}(\mathbb{B})$ is closed and the bracket on it is the cross product above, $\mathbb{H}_{\mathbb{B}}$ is closed with the bracket of the imaginary quaternions, the bracket carries $\mathbb{M}_+$ to $\mathbb{M}_-$ and $\mathbb{M}_-$ to itself, and the bracket of $\mathbb{M}_+$ with $\mathbb{M}_-$ carries the second back to the first; the exact signs are those tables'.

---

## The Three Subalgebras the Other Products Reproduce

Product 2 of the table above reproduces the vector subspace, product 3 the anti-Hermitian one and product 4 the quaternion one, so the three subspaces that follow are the subalgebras of the one algebra $(\mathbb{B},[\cdot,\cdot])$ that the other products reach, and not algebras of their own. The proposition first explains why each of them carries the commutator up to a sign.

### The Subspace Brackets Are the Commutator

The three non-commutator brackets are Lie brackets exactly on the subspace where their two conjugations agree, and there each remembers only a sign.

**Proposition.** Let $f(\tilde{P},\tilde{Q})=\tilde{P}^{\alpha}\tilde{Q}^{\beta}$ be one of the three products obtained from the complex bilinear product by a conjugation $\alpha$ in the first slot and $\beta$ in the second, and let $V$ be a subspace on which $\alpha$ acts as the scalar $\varepsilon=\pm1$ and $\beta$ as the scalar $\delta=\pm1$. Then on $V$

$$
[\tilde{P},\tilde{Q}]_f = \varepsilon\delta\,[\tilde{P},\tilde{Q}],
$$

so $f$ is a Lie bracket on $V$ and the Lie algebra is $V$ with the commutator or its opposite.

**Proof.** On $V$ one has $f(\tilde{P},\tilde{Q})=\varepsilon\delta\,\tilde{P}\tilde{Q}$ and $f(\tilde{Q},\tilde{P})=\varepsilon\delta\,\tilde{Q}\tilde{P}$, so the bracket is $\varepsilon\delta\,(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$. $\square$

The proposition applies to the two bilinear-conjugation products. For the $\natural$-product the involution ${}^{\natural}$ acts as $-1$ on the vector subspace, so the $\natural$-bracket is $-$ the commutator on $\mathrm{Vect}(\mathbb{B})$:

$$
[\tilde{P},\tilde{Q}]_{\natural} = 2\,\mathrm{Vec}\bigl(\tilde{P}^{\natural}\tilde{Q}\bigr)
= 2\bigl(P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}\bigr),
\qquad
[\mathbf{P},\mathbf{Q}]_{\natural} = -2\,\mathbf{P}\times\mathbf{Q} = -\,[\mathbf{P},\mathbf{Q}] ,
$$

the mixed terms dropping on the vector subspace. For the star-product the involution ${}^{*}$ acts as $-1$ on the anti-Hermitian subspace, so the star-bracket is $-$ the commutator on $\mathbb{M}_-$:

$$
[\tilde{P},\tilde{Q}]_{*} = \tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*} \in \mathbb{M}_- ,
\qquad
[s,t]_{*} = -\,[s,t] \quad (s,t\in\mathbb{M}_-).
$$

For the $\natural*$-product the two involutions do not act as a single scalar on either subspace, but on the quaternion subspace they agree and the same collapse occurs: for $\tilde{P},\tilde{Q}\in\mathbb{H}_{\mathbb{B}}$ the natural conjugation and the Hermitian conjugation coincide, $\tilde{P}^{\natural}=\tilde{P}^{*}$, so $f(\tilde{P},\tilde{Q})=\tilde{P}^{*}\tilde{Q}^{*}=(\tilde{Q}\tilde{P})^{*}$ and

$$
[\tilde{P},\tilde{Q}]_{\natural*} = (\tilde{Q}\tilde{P})^{*}-(\tilde{P}\tilde{Q})^{*} = -\,\bigl([\tilde{P},\tilde{Q}]\bigr)^{*} = [\tilde{P},\tilde{Q}] ,
$$

because the commutator of two quaternions is imaginary and the star-involution negates the imaginary part. So the $\natural*$-bracket is $+$ the commutator on $\mathbb{H}_{\mathbb{B}}$.

Each of the three identities says the same thing: the bracket of the product is not a new Lie algebra, it is the commutator of the associative product read on a subspace. This is the general dichotomy of *Lie Algebras of Sesquialgebras*, where the antisymmetrisation of a sesquilinear product fails on the whole algebra and the Lie structure migrates to the commutator on the half whose range is closed; the biquaternion case is the worked example, and it shows the migration on both the bilinear and the sesquilinear sides.

### The Vector Subalgebra $\mathrm{Vect}(\mathbb{B})$

The vector subspace $\mathrm{Vect}(\mathbb{B})$ is the trace-free part $\mathrm{B}_0$ of *The Trace-Free Subalgebra*, of complex dimension $3$ and real dimension $6$. With the commutator it is the special linear Lie algebra $\mathfrak{sl}(2,\mathbb{C})$, and over the reals its compact real form is $\mathrm{K}=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, on which the bracket is twice the cross product. It is the subalgebra that **product 2** reproduces, where the $\natural$-bracket is minus the commutator.

### The Anti-Hermitian Subalgebra $\mathbb{M}_-$

The anti-Hermitian subspace $\mathbb{M}_-$ is the unitary Lie algebra $\mathfrak{u}(2)$ over $\mathbb{R}$, with centre the line $\mathbb{R}\,ie_0$ and derived subalgebra $\mathfrak{su}(2)=\mathrm{K}$; it is the object that *The Unitary Lie Algebra* develops for its own sake. It is the subalgebra that **product 3** reproduces, where the star-bracket is minus the commutator.

### The Quaternion Subalgebra $\mathbb{H}_{\mathbb{B}}$

The quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is closed under the commutator, and the bracket vanishes on its real line $\mathbb{R}e_0$ and is the cross product on its imaginary part, so $(\mathbb{H}_{\mathbb{B}},[\cdot,\cdot])\cong\mathbb{R}e_0\oplus\mathfrak{su}(2)$, with derived subalgebra the imaginary quaternions. It is the subalgebra that **product 4** reproduces, where the $\natural*$-bracket is plus the commutator.

---

## The Real Structure and the Adjoint Maps

Over $\mathbb{R}$ the algebra is the Lie algebra of the real Lie group $\mathbb{B}^\times$, and the trace-free part $\mathrm{B}_0$, of real dimension $6$, is its real form, with $[\mathrm{G},\mathrm{G}]=\mathrm{B}_0$ as over $\mathbb{C}$.

The **adjoint maps** are
$$
\operatorname{ad}_{\tilde{Q}} : \tilde{P}\mapsto[\tilde{Q},\tilde{P}],
$$
and the map $\tilde{Q}\mapsto\operatorname{ad}_{\tilde{Q}}$ is a Lie algebra homomorphism whose kernel is the centre $\mathbb{C}e_0$.

## Summary

A Lie algebra is relative to a bracket, and the four brackets of the biquaternion algebra give one Lie algebra and not four. Under the commutator $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$, the antisymmetric part of the complex bilinear product, the biquaternion algebra is a complex Lie algebra of complex dimension $4$ and real dimension $8$, isomorphic to $\mathrm{GL}(2,\mathbb{C})$; its centre is the scalar line $\mathbb{C}e_0$, of complex dimension $1$. The trace functional is $\mathrm{Tr}(\tilde{Q})=2Q_0$, and the trace-free part $\mathrm{B}_0=\{\tilde{Q}:Q_0=0\}=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ has complex dimension $3$ and real dimension $6$, isomorphic to $\mathrm{SL}(2,\mathbb{C})$; the algebra splits as $\mathrm{G}=\mathrm{B}_0\oplus\mathbb{C}e_0$. The derived subalgebra is the vector subspace itself, $[\mathrm{G},\mathrm{G}]=\mathrm{Vect}(\mathbb{B})$, so the algebra is not solvable; the bracket of two pure vectors is twice their outer product, equivalently twice their cross product, $[\mathbf{P},\mathbf{Q}]=2\,\mathbf{P}\wedge\mathbf{Q}=2\,\mathbf{P}\times\mathbf{Q}$. Over $\mathbb{R}$ the trace-free part is the sum of the two three-dimensional real subspaces $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$, the first a compact subalgebra on which the bracket is twice the cross product and the second not a subalgebra.

The other three brackets are not Lie brackets on the whole algebra, and the doubled antisymmetric parts of the three other products of *The Four Biquaternion Complex Products* fail the Jacobi identity at $(e_0,e_1,e_2)$ with $-4e_3$ for the $\natural$-product, at $(e_0,e_1,e_2)$ with $4e_3$ for the star-product, and at $(e_1,e_2,ie_3)$ with $4ie_0$ for the quaternionic sesquilinear product. Each becomes a Lie bracket on the subspace where its two conjugations agree, and there it is the commutator up to sign: the $\natural$-bracket on the vector subspace, the star-bracket on the anti-Hermitian subspace, and the $\natural*$-bracket on the quaternion subspace. The Lie algebras so obtained — $\mathrm{SL}(2,\mathbb{C})$ on the vector subspace, $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ on the quaternion subspace, and $\mathfrak{u}(2)$ on the anti-Hermitian subspace — are subalgebras of the one Lie algebra $\mathrm{G}$, and the companion article *Biquaternion Jordan Algebras* reads the symmetric halves of the same four products.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$ | Commutator bracket; $\mathbb{B}$ is a complex Lie algebra under it |
| $[\tilde{P},\tilde{Q}]_{\natural}=\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}$ | the antisymmetric part of the $\natural$-product, a Lie bracket on $\mathrm{Vect}(\mathbb{B})$ only |
| $[\tilde{P},\tilde{Q}]_{*}=\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*}$ | the antisymmetric part of the star-product, a Lie bracket on $\mathbb{M}_-$ only |
| $[\tilde{P},\tilde{Q}]_{\natural*}=\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*}$ | the antisymmetric part of the quaternionic sesquilinear product, a Lie bracket on $\mathbb{H}_{\mathbb{B}}$ only |
| $[\mathbf{P},\mathbf{Q}]_{\natural}=-[\mathbf{P},\mathbf{Q}]$ | the $\natural$-bracket equals minus the commutator on the vector subspace |
| $[s,t]_{*}=-[s,t]$ | the star-bracket equals minus the commutator on $\mathbb{M}_-$ |
| $[\tilde{P},\tilde{Q}]_{\natural*}=[\tilde{P},\tilde{Q}]$ | the $\natural*$-bracket equals the commutator on $\mathbb{H}_{\mathbb{B}}$ |
| $\mathrm{G}=\mathbb{B}$ | The algebra as a Lie algebra; complex dimension $4$, real dimension $8$ |
| $\mathrm{Tr}(\tilde{Q})=2Q_0$ | Trace functional |
| $\mathrm{B}_0=\{Q_0=0\}$ | Trace-free subalgebra; $\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$; $\mathrm{SL}(2,\mathbb{C})$ |
| $\mathrm{Z}(\mathrm{G})=\mathbb{C}e_0$ | Centre; complex dimension $1$, real dimension $2$ |
| $[\mathrm{G},\mathrm{G}]=\mathrm{Vect}(\mathbb{B})$ | Derived subalgebra, the vector subspace |
| $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | Outer product; the commutator is twice it, $[\tilde{P},\tilde{Q}]=2\,\tilde{P}\wedge\tilde{Q}$ |
| $[\mathbf{P},\mathbf{Q}]=2\,\mathbf{P}\wedge\mathbf{Q}=2\,\mathbf{P}\times\mathbf{Q}$ | Bracket of pure vectors as twice the outer product and twice the cross product |
| $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Compact real form; the bracket on it is twice the cross product |
| $\mathbb{H}_{\mathbb{B}}$ with $[\cdot,\cdot]$ | $\mathbb{R}e_0\oplus\mathfrak{su}(2)$, derived subalgebra $\mathrm{Im}\,\mathbb{H}$ |
| $\mathbb{M}_-$ with $[\cdot,\cdot]$ | $\mathfrak{u}(2)$, the unitary Lie algebra |
| $\operatorname{ad}_{\tilde{Q}}(\tilde{P})=[\tilde{Q},\tilde{P}]$ | Adjoint map |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- The companion articles of this series: *The Four Biquaternion Complex Products*, *Decomposition of the Biquaternion Complex Products*, *Biquaternion Jordan Algebras*, and *Biquaternion Relations Between Subspaces*, for the four products, the four antisymmetric parts, the symmetrisation on the other side, and the subspace table.
- *Sesquialgebras* and *Lie Algebras of Sesquialgebras* (`articles_maths/`), for the general antisymmetrisation of a sesquilinear product, the failure of the Jacobi identity and the commutator Lie algebra of a sesquialgebra; the biquaternion case is the worked example of that article.
