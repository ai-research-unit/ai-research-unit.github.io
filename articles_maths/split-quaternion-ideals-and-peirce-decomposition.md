
# __Split-Quaternion Ideals and Peirce Decomposition__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}} = \mathrm{Cl}_{1,1}$ is four-dimensional over $\mathbb{R}$ and isomorphic to the algebra of $2 \times 2$ real matrices, as established in *Split-Quaternion Algebra*. This article studies the ideal structure of $\mathbb{H}_{\mathrm{s}}$ and the decomposition of the algebra relative to its standard pair of idempotents.

One fact organizes the whole discussion. As a real algebra,

$$
\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R}),
$$

and $M_2(\mathbb{R})$ is **simple**: its only two-sided ideals are $0$ and the whole algebra. The algebra $\mathbb{H}_{\mathrm{s}}$ is therefore simple, and yet it is **not** a division algebra — it carries nonzero zero divisors, as *Split-Quaternion Zero Divisors* records. This combination is what makes its ideal theory interesting: the two-sided ideal lattice is trivial, while the one-sided ideal lattice is rich and governed by the matrix structure.

The article treats, in order, the definitions of ideals; the two-sided ideals and simplicity; the artinian and semisimple structure and the length of the algebra as a module over itself; the two idempotents and their orthogonal complementarity; the explicit matrix units; the Peirce decomposition into four one-dimensional corners; the grouping of the matrix units into minimal left and minimal right ideals; and the lattice of left ideals, which is a real projective line. It closes with the contrast with the quaternions $\mathbb{H}$, where there are no proper ideals at all, and with the biquaternions $\mathbb{B}$, whose ideal theory has the same shape over $\mathbb{C}$.

**Conventions.** The basis is $1, e_1, e_2, e_3$, with $e_1^2 = -1$, $e_2^2 = +1$, $e_3 = e_1 e_2$ and $e_1 e_2 = -e_2 e_1$; a general element is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$. The conjugation and the central product $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ are assumed from *Split-Quaternion Algebra*, the idempotents $\tilde\pi_\pm = \tfrac{1}{2}(1 \pm e_2)$ from *Split-Quaternion Idempotents and Projections*, and the metrical reading of $N$ from *Split-Quaternion Norm and Invertibility*. The definitions of rings and modules apply to the noncommutative algebra $\mathbb{H}_{\mathrm{s}}$, where "left" and "right" must be distinguished.

## Ideals in an Algebra

Let $A$ be an associative unital algebra over a field $k$. An additive subgroup $I \subseteq A$ is a **left ideal** if $A I \subseteq I$, a **right ideal** if $I A \subseteq I$, and a **two-sided ideal** if it is both. The distinction matters only when $A$ is noncommutative; for $\mathbb{H}_{\mathrm{s}}$ the three notions genuinely differ. The ideals $0$ and $A$ are called trivial.

A base-field remark will be used repeatedly. If $A I \subseteq I$, then $I$ is automatically a $k$-subspace, since $\lambda \tilde q = (\lambda 1)\tilde q \in I$ for $\lambda \in k$ and $\tilde q \in I$, as $\lambda 1 \in A$. So the left ideals do not depend on which field of scalars inside the centre is used to view the algebra.

For a two-sided ideal $I$, the **quotient algebra** $A/I$ is defined, and kernels of algebra homomorphisms are two-sided ideals; the first isomorphism theorem gives $A/\ker\varphi \cong \operatorname{im}\varphi$. For a left ideal only, $A/I$ is still a left $A$-module but not in general an algebra. Thus the left ideals govern module theory and the two-sided ideals govern quotient algebras.

## The Two-Sided Ideals: Simplicity of $\mathbb{H}_{\mathrm{s}}$

**Theorem.** The only two-sided ideals of $\mathbb{H}_{\mathrm{s}}$ are $0$ and $\mathbb{H}_{\mathrm{s}}$. Equivalently, $\mathbb{H}_{\mathrm{s}}$ is a **simple** $\mathbb{R}$-algebra.

**Proof.** Work in the matrix algebra $M_2(\mathbb{R})$ under the identification $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ (*Matrix Algebras*). Let the matrix units satisfy $E_{ij} E_{kl} = \delta_{jk} E_{il}$, from which $E_{ik} M E_{lj} = M_{kl} E_{ij}$ for any matrix $M = (M_{kl})$. If $I \neq 0$ is a two-sided ideal and $M \in I$ has $M_{kl} \neq 0$, then

$$
E_{ij} = M_{kl}^{-1} E_{ik} M E_{lj} \in I .
$$

Hence $I$ contains every matrix unit, so $I = M_2(\mathbb{R})$. Transporting back gives the claim.

Consequences:

- The only quotient algebras of $\mathbb{H}_{\mathrm{s}}$ are $\mathbb{H}_{\mathrm{s}}$ and $0$.
- Every nonzero element generates $\mathbb{H}_{\mathrm{s}}$ as a two-sided ideal.
- The centre of $\mathbb{H}_{\mathrm{s}}$ is the scalar copy $\mathbb{R}\cdot 1$ of $\mathbb{R}$, so $\mathbb{H}_{\mathrm{s}}$ is a **central simple** $\mathbb{R}$-algebra; in particular it is not a product $A_1 \times A_2$ of nonzero algebras.
- The many one-sided ideals constructed below are all non-two-sided, so they do not contradict simplicity.

Simplicity does not imply that every nonzero element is invertible: the element $1 + e_2$ is a nonzero zero divisor, since $(1+e_2)(1-e_2) = 0$, yet it generates $\mathbb{H}_{\mathrm{s}}$ as a two-sided ideal. Simplicity and the division property are independent, and $\mathbb{H}_{\mathrm{s}}$ is the standard example distinguishing them.

## Artinian, Semisimple, and Length Two

A nonzero module is **simple** if it has no submodules other than $0$ and itself. A **composition series** is a finite strictly increasing chain $0 = M_0 \subset M_1 \subset \cdots \subset M_r = M$ with simple successive quotients; the number $r$ is the **length** of $M$. A ring is **left artinian** if every descending chain of left ideals stabilizes, and **semisimple** if its left regular module is a direct sum of simple modules.

Every descending chain of left ideals of $\mathbb{H}_{\mathrm{s}}$ is a descending chain of real subspaces of the finite-dimensional space $\mathbb{H}_{\mathrm{s}}$, so it stabilizes; thus $\mathbb{H}_{\mathrm{s}}$ is artinian. By the Wedderburn–Artin theorem, a unital ring is semisimple if and only if it is artinian with zero Jacobson radical, and every simple artinian ring is semisimple. Hence $\mathbb{H}_{\mathrm{s}}$ is **semisimple**, and every left ideal is a direct sum of minimal left ideals.

Every simple left $\mathbb{H}_{\mathrm{s}}$-module is two-dimensional over $\mathbb{R}$, and all simple left modules are isomorphic. As a left module over itself,

$$
\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^2 \oplus \mathbb{R}^2 .
$$

With the idempotents $\tilde\pi_+, \tilde\pi_-$ below this reads $\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_-$ with $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm \cong \mathbb{R}^2$. Hence $0 \subset \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \subset \mathbb{H}_{\mathrm{s}}$ is a composition series, and the **length of $\mathbb{H}_{\mathrm{s}}$ as a left module over itself is $2$**, with both factors isomorphic to $\mathbb{R}^2$. The right regular module has length $2$ as well, with factors the dual module $(\mathbb{R}^2)^{*}$.

## Idempotents and Orthogonal Idempotents

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$, and two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents, and for a semisimple algebra

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

The idempotents

$$
\tilde\pi_+ = \tfrac{1}{2}(1 + e_2), \qquad \tilde\pi_- = \tfrac{1}{2}(1 - e_2)
$$

satisfy $\tilde\pi_+^2 = \tilde\pi_+$, $\tilde\pi_-^2 = \tilde\pi_-$, $\tilde\pi_+ \tilde\pi_- = \tilde\pi_- \tilde\pi_+ = 0$ and $\tilde\pi_+ + \tilde\pi_- = 1$, ; they are primitive. Their classification — the bijection with the roots of $+1$ in the vector subspace — is the subject of *Split-Quaternion Idempotents and Projections*, and is quoted here only for the pair used below.

## Matrix Units in the Split-Quaternion Algebra

The off-diagonal matrix units can be written explicitly. Put

$$
\tilde q = \tfrac{1}{2}(e_3 - e_1), \qquad \tilde p = \tfrac{1}{2}(e_1 + e_3).
$$

Then $\{\tilde\pi_+, \tilde q, \tilde p, \tilde\pi_-\}$ is an $\mathbb{R}$-basis of $\mathbb{H}_{\mathrm{s}}$, and it satisfies the matrix-unit relations with

$$
E_{11} = \tilde\pi_+, \qquad E_{12} = \tilde q, \qquad E_{21} = \tilde p, \qquad E_{22} = \tilde\pi_- .
$$

Explicitly, $\tilde\pi_+^2 = \tilde\pi_+$, $\tilde\pi_-^2 = \tilde\pi_-$, $\tilde\pi_+ \tilde\pi_- = \tilde\pi_- \tilde\pi_+ = 0$, $\tilde\pi_+ + \tilde\pi_- = 1$, and

$$
\tilde\pi_+ \tilde q = \tilde q = \tilde q \tilde\pi_-, \qquad \tilde\pi_- \tilde p = \tilde p = \tilde p \tilde\pi_+, \qquad \tilde q \tilde p = \tilde\pi_+, \qquad \tilde p \tilde q = \tilde\pi_-,
$$

together with $\tilde q \tilde\pi_+ = \tilde\pi_- \tilde q = 0$, $\tilde\pi_+ \tilde p = \tilde p \tilde\pi_- = 0$, and $\tilde q^2 = \tilde p^2 = 0$. Both $\tilde q$ and $\tilde p$ are square zero, so $\{\tilde\pi_+, \tilde q, \tilde p, \tilde\pi_-\}$ is a system of matrix units of $\mathbb{H}_{\mathrm{s}}$, with $E_{11} = \tilde\pi_+$, $E_{22} = \tilde\pi_-$, $E_{12} = \tilde q$ and $E_{21} = \tilde p$. The names $E_{ij}$ refer to this abstract multiplication table.

## The Peirce Decomposition

The **Peirce decomposition** is the decomposition of an algebra relative to a family of orthogonal idempotents; it is the algebraic form of a block decomposition of a matrix.

**One idempotent.** Let $e \in A$ be idempotent and $f = 1 - e$. Every $q_0 \in A$ expands as $q_0 = eae + eaf + fae + faf$, giving the direct sum

$$
A = eAe \oplus eAf \oplus fAe \oplus fAf,
$$

whose summands are the **Peirce spaces**. The corner $eAe$ is a subalgebra with identity $e$; the other corners are only one-sided pieces. The expansion and the directness are proved in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, where the case of a **central** idempotent is also separated: for a central $e$ the off-diagonal corners vanish and the sum is a product of algebras. That special case does not arise here, since the idempotents lie in a simple algebra.

**A complete orthogonal family.** If $\{e_1, \dots, e_n\}$ is complete and pairwise orthogonal, the same expansion gives

$$
A = \bigoplus_{i,j=1}^{n} e_i A e_j, \qquad (e_i A e_j)(e_k A e_l) \subseteq \delta_{jk}\, e_i A e_l .
$$

Each diagonal corner $e_i A e_i$ is an algebra with identity $e_i$, and each off-diagonal piece is a bimodule over the corresponding corners.

**The split-quaternion case.** Take $e_1 = \tilde\pi_+$ and $e_2 = \tilde\pi_-$. The Peirce decomposition of $\mathbb{H}_{\mathrm{s}}$ is

$$
\mathbb{H}_{\mathrm{s}} = \tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_- \oplus \tilde\pi_- \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \tilde\pi_- \mathbb{H}_{\mathrm{s}} \tilde\pi_-,
$$

and by the table above each summand is one-dimensional over $\mathbb{R}$:

$$
\tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_+ = \mathbb{R} \tilde\pi_+, \qquad \tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_- = \mathbb{R} \tilde q, \qquad \tilde\pi_- \mathbb{H}_{\mathrm{s}} \tilde\pi_+ = \mathbb{R} \tilde p, \qquad \tilde\pi_- \mathbb{H}_{\mathrm{s}} \tilde\pi_- = \mathbb{R} \tilde\pi_- .
$$

So the Peirce decomposition is exactly the matrix-unit decomposition

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R} \tilde\pi_+ \oplus \mathbb{R} \tilde q \oplus \mathbb{R} \tilde p \oplus \mathbb{R} \tilde\pi_- = \bigoplus_{i,j=1}^{2} \mathbb{R} E_{ij}.
$$

The diagonal part $\tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \tilde\pi_- \mathbb{H}_{\mathrm{s}} \tilde\pi_- = \mathbb{R} \tilde\pi_+ \oplus \mathbb{R} \tilde\pi_-$ is the two-dimensional commutative subalgebra isomorphic to $\mathbb{R} \times \mathbb{R}$, the diagonal subalgebra of the matrix picture. Each diagonal corner is a division ring, namely $\mathbb{R}$, which is the primitivity criterion. The off-diagonal corner $\tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_- = \mathbb{R} \tilde q$ is nonzero, and it is the reason the decomposition of $\mathbb{H}_{\mathrm{s}}$ by the non-central idempotent $\tilde\pi_+$ is a module decomposition and not an algebra decomposition; the element $\tilde\pi_+ e_3 \tilde\pi_- = \tilde q$ detects it.

## The Matrix-Unit Decomposition as a Sum of Minimal Ideals

The matrix units group into one-sided ideals in a second way. With $E_{11} = \tilde\pi_+$ and $E_{22} = \tilde\pi_-$, the two **columns** $\mathbb{H}_{\mathrm{s}} \tilde\pi_+, \mathbb{H}_{\mathrm{s}} \tilde\pi_-$ and the two **rows** $\tilde\pi_+ \mathbb{H}_{\mathrm{s}}, \tilde\pi_- \mathbb{H}_{\mathrm{s}}$ are one-sided ideals, and

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_- = (\mathbb{R} \tilde\pi_+ \oplus \mathbb{R} \tilde p) \oplus (\mathbb{R} \tilde q \oplus \mathbb{R} \tilde\pi_-),
$$

$$
\mathbb{H}_{\mathrm{s}} = \tilde\pi_+ \mathbb{H}_{\mathrm{s}} \oplus \tilde\pi_- \mathbb{H}_{\mathrm{s}} = (\mathbb{R} \tilde\pi_+ \oplus \mathbb{R} \tilde q) \oplus (\mathbb{R} \tilde p \oplus \mathbb{R} \tilde\pi_-).
$$

The first exhibits $\mathbb{H}_{\mathrm{s}}$ as a direct sum of the two minimal left ideals (the columns); the second exhibits it as a direct sum of the two minimal right ideals (the rows). The two groupings of the same four basis elements differ: the Peirce decomposition groups $\tilde\pi_+$ with $\tilde q$ and $\tilde\pi_-$ with $\tilde p$, whereas the column decomposition groups $\tilde\pi_+$ with $\tilde p$ and $\tilde\pi_-$ with $\tilde q$. Each column is two-dimensional and isomorphic, as a left $\mathbb{H}_{\mathrm{s}}$-module, to $\mathbb{R}^2$; each row is isomorphic to the dual $(\mathbb{R}^2)^{*}$. Since $\mathbb{H}_{\mathrm{s}}$ is simple, a column or a row is never a two-sided ideal; for instance $\mathbb{H}_{\mathrm{s}} \tilde\pi_+$ is not stable under right multiplication by $\tilde p$.

## Minimal Left and Right Ideals

A **minimal left ideal** is a nonzero left ideal containing no nonzero proper left ideal; equivalently, a simple submodule of the left regular module. A **minimal right ideal** is defined the same way on the right.

Since $\mathbb{H}_{\mathrm{s}}$ is semisimple, every left ideal is a direct sum of minimal left ideals, and every minimal left ideal is of the form $\mathbb{H}_{\mathrm{s}} e$ for a primitive idempotent $e$. The coordinate examples are the columns $\mathbb{H}_{\mathrm{s}} \tilde\pi_+$ and $\mathbb{H}_{\mathrm{s}} \tilde\pi_-$, and all minimal left ideals are isomorphic as left $\mathbb{H}_{\mathrm{s}}$-modules to the simple module $\mathbb{R}^2$: a general one is obtained from a column by an algebra automorphism, so it is again a column in a suitable basis. Dually, every minimal right ideal is a row and is isomorphic to $(\mathbb{R}^2)^{*}$, the coordinate examples being $\tilde\pi_+ \mathbb{H}_{\mathrm{s}}$ and $\tilde\pi_- \mathbb{H}_{\mathrm{s}}$. Thus there is one isomorphism class of simple left modules and one of simple right modules. Being nonzero proper one-sided ideals, none of them is two-sided — which is exactly why their abundance is compatible with the simplicity theorem.

## The Lattice of Left Ideals as a Projective Line

The one-sided ideals can be listed explicitly. For each real subspace $W \subseteq \mathbb{R}^2$ define

$$
L_W = \{\, M \in M_2(\mathbb{R}) : M|_W = 0 \,\},
$$

the matrices annihilating $W$. This is a left ideal, since $\ker(AM) \supseteq \ker M$ for every $A$. The assignment $W \mapsto L_W$ reverses inclusions, and

$$
L_0 = \mathbb{H}_{\mathrm{s}}, \qquad L_{\mathbb{R}^2} = 0, \qquad L_W \text{ is minimal when } \dim_{\mathbb{R}} W = 1 .
$$

Conversely every left ideal is of this form: a left ideal is a submodule of the left regular module $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^2 \oplus \mathbb{R}^2$, and since $\mathbb{R}^2$ is simple and $\mathbb{H}_{\mathrm{s}}$ has length $2$, the only submodules of $\mathbb{R}^2 \oplus \mathbb{R}^2$ are $0$, a copy of $\mathbb{R}^2$, and the whole module. A minimal left ideal $L$ is thus a copy of $\mathbb{R}^2$, determined by the line $W = \bigcap_{M \in L} \ker M$.

**Theorem.** The left ideals of $\mathbb{H}_{\mathrm{s}}$ are exactly $0$, the whole algebra, and the minimal left ideals $L_W$ with $W$ a line in $\mathbb{R}^2$. The minimal left ideals are indexed by the real projective line

$$
\mathbb{P}^1(\mathbb{R}) = \{\, W \subseteq \mathbb{R}^2 : W \text{ a one-dimensional } \mathbb{R}\text{-subspace} \,\},
$$

which is a circle, and they form the middle layer of the lattice:

$$
0 \;\subset\; \{\, L_W : W \in \mathbb{P}^1(\mathbb{R}) \,\} \;\subset\; \mathbb{H}_{\mathrm{s}} .
$$

The middle elements are pairwise incomparable; each covers $0$ and is covered by $\mathbb{H}_{\mathrm{s}}$. Because the length of $\mathbb{H}_{\mathrm{s}}$ as a left module over itself is $2$, every minimal left ideal is also a **maximal** left ideal: nothing lies strictly between it and $\mathbb{H}_{\mathrm{s}}$. Right ideals admit the same description, with lines in the dual space and the rows as coordinate members.

**Remark.** The parameter space classifying the minimal one-sided ideals of $M_n(D)$ is $\mathbb{P}^{n-1}(D)$, over the **division ring** $D$ in the Wedderburn–Artin decomposition $M_n(D)$, not over an arbitrary base field. Here $D = \mathbb{R}$ and $n = 2$, so the parameter space is $\mathbb{P}^1(\mathbb{R})$. The field over which the algebra is viewed does not change the ideal lattice, because the base-field remark of *Ideals in an Algebra* shows that the left ideals are automatically subspaces over any subfield of the centre.

## The Contrast with $\mathbb{H}$ and with $\mathbb{B}$

**The quaternions.** The algebra $\mathbb{H}$ is a division algebra, so every nonzero element is invertible and the only left ideal is $0$ or $\mathbb{H}$ itself; there are no proper one-sided ideals and no nontrivial idempotents. The absence of proper ideals is a consequence of the division property: if $I \neq 0$ is a left ideal and $0 \neq \tilde q \in I$, then $1 = \tilde q^{-1} \tilde q \in I$, so $I = \mathbb{H}$. The split-quaternion algebra has the same two-sided ideal lattice as $\mathbb{H}$ — just $0$ and the whole algebra — but its one-sided ideal lattice is as large as a circle, and the difference is entirely due to the zero divisors.

**The biquaternions.** Over $\mathbb{C}$, $\mathbb{B} \cong M_2(\mathbb{C})$ is simple in the same way, its length as a left module over itself is $2$, its idempotents $p, q$ play the role of $\tilde\pi_\pm$, and its matrix units satisfy the same relations; the only change is that the minimal left ideals are indexed by the **complex** projective line $\mathbb{P}^1(\mathbb{C})$, a two-dimensional real surface, rather than the circle $\mathbb{P}^1(\mathbb{R})$. The ideal theory over the base field $\mathbb{R}$ is developed in *Biquaternion Ideals and Peirce Decomposition*; the passage from $\mathbb{C}$ to $\mathbb{R}$ restricts the parameter space of minimal left ideals to a real circle but leaves the shape of the lattice unchanged.

## Summary

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ is simple: its only two-sided ideals are $0$ and $\mathbb{H}_{\mathrm{s}}$. It is semisimple, artinian, and of length $2$ as a left module over itself, with $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^2 \oplus \mathbb{R}^2$ and $\mathbb{R}^2$ the defining module. Simplicity does not force the division property: $1 + e_2$ is a nonzero zero divisor that nonetheless generates the algebra as a two-sided ideal.

The standard idempotents $\tilde\pi_\pm = \tfrac{1}{2}(1 \pm e_2)$ are orthogonal, complete and primitive. With the explicit matrix units $\tilde q = \tfrac{1}{2}(e_3 - e_1)$ and $\tilde p = \tfrac{1}{2}(e_1 + e_3)$, the set $\{\tilde\pi_+, \tilde q, \tilde p, \tilde\pi_-\}$ is a set of matrix units and the Peirce decomposition is the four-corner decomposition

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R} \tilde\pi_+ \oplus \mathbb{R} \tilde q \oplus \mathbb{R} \tilde p \oplus \mathbb{R} \tilde\pi_- .
$$

The two columns $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$ are the minimal left ideals, each isomorphic to $\mathbb{R}^2$; the two rows $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ are the minimal right ideals, each isomorphic to the dual $(\mathbb{R}^2)^{*}$. Every left ideal is $0$, the whole algebra, or a minimal left ideal $L_W$ indexed by a line $W$ in $\mathbb{R}^2$; the minimal left ideals form the middle layer of the lattice and are parametrised by the real projective line $\mathbb{P}^1(\mathbb{R})$. The quaternion algebra, being a division algebra, has no proper ideal at all, while the biquaternion algebra has the same ideal lattice with the complex projective line $\mathbb{P}^1(\mathbb{C})$ in place of the real one.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ | *Split-Quaternion Algebra* |
| $I$ | an ideal (left, right or two-sided) | this article |
| $M_2(\mathbb{R})$, $E_{ij}$ | the matrix algebra and its matrix units, $E_{ij}E_{kl}=\delta_{jk}E_{il}$ | *Matrix Algebras* |
| $\tilde\pi_+ = \tfrac{1}{2}(1+e_2)$, $\tilde\pi_- = \tfrac{1}{2}(1-e_2)$ | the standard orthogonal idempotents | *Split-Quaternion Idempotents and Projections* |
| $\tilde q = \tfrac{1}{2}(e_3-e_1)$, $\tilde p = \tfrac{1}{2}(e_1+e_3)$ | the off-diagonal matrix units $E_{12}$, $E_{21}$ | this article |
| $\mathbb{R}^2$ | the simple (defining) left module, $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^2 \oplus \mathbb{R}^2$ | this article |
| $(\mathbb{R}^2)^{*}$ | the dual (right) module | this article |
| $eAe$, $eAf$, … | the Peirce spaces of an idempotent $e$ | this article |
| $L_W$ | the minimal left ideal annihilating the line $W$ | this article |
| $\mathbb{P}^1(\mathbb{R})$ | the real projective line, parametrising the minimal left ideals | this article |
| $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ | the central product, formed and evaluated algebraically | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the module-theoretic description of the ideal lattice.
- T. Y. Lam, *A First Course in Noncommutative Rings*, 2nd ed. (Springer, 2001), for the Wedderburn–Artin theorem, simplicity, semisimplicity and the length of a module.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification $M_2(\mathbb{R}) \cong \mathrm{Cl}_{1,1}$ and its matrix units.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for idempotents, minimal ideals and the matrix models of the low-dimensional Clifford algebras.
