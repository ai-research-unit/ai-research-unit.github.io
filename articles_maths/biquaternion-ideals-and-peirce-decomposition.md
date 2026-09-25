# __Biquaternion Ideals and Peirce Decomposition__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, as established in the article on biquaternion algebra. This article studies the ideal structure of $\mathbb{B}$ and the decomposition of $\mathbb{B}$ relative to a family of idempotents.

Two facts organize the discussion. As a $\mathbb{C}$-algebra, $\mathbb{B}$ is isomorphic to the algebra of $2 \times 2$ complex matrices:

$$
\mathbb{B} \cong M_2(\mathbb{C}).
$$

And $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. Its ideal theory is therefore a theory of one-sided ideals, governed by the matrix structure: the main results are the classification of the left ideals — $0$, the minimal ones, and $\mathbb{B}$ — and the Peirce decomposition into four one-dimensional corners relative to a pair of orthogonal idempotents.

Because the biquaternions carry both a complex and a real structure, every statement is tagged with the field over which it is made. Sections 1 to 10 work over $\mathbb{C}$. Section 11 discusses the $\mathbb{R}$-view, where the ideal lattice itself is unchanged but the real structure leaves further traces. The notation follows the article on biquaternion algebra: $e_0$ is the unit, $e_1, e_2, e_3$ are the quaternion units with $e_1 e_2 = e_3$, $i$ is the central scalar imaginary, and a general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The definitions of the article on rings apply to the noncommutative algebra $\mathbb{B}$, where "left" and "right" must be distinguished.

# Part I: Ideals and Simplicity

## 1. Ideals in an Algebra

Let $A$ be an associative unital algebra over a field $k$. An additive subgroup $I \subseteq A$ is a **left ideal** if $A I \subseteq I$, a **right ideal** if $I A \subseteq I$, and a **two-sided ideal** if it is both. The distinction matters only when $A$ is noncommutative; for $\mathbb{B}$ the three notions genuinely differ. The ideals $0$ and $A$ are called trivial.

A base-field remark will be used repeatedly. If $A I \subseteq I$, then $I$ is automatically a $k$-subspace, since $\lambda x = (\lambda 1) x \in I$ for $\lambda \in k$, $x \in I$, as $\lambda 1 \in A$. So the left ideals of a unital algebra do not depend on which field of scalars inside the center is used to view it; in particular the ideal lattice of $\mathbb{B}$ is the same in the $\mathbb{C}$-view and the $\mathbb{R}$-view (Section 11).

For a two-sided ideal $I$, the **quotient algebra** $A/I$ is the set of cosets with the induced operations, well defined precisely because $I$ absorbs multiplication on both sides. Kernels of algebra homomorphisms are two-sided ideals, and the first isomorphism theorem gives $A/\ker\varphi \cong \operatorname{im}\varphi$. For a left ideal only, $A/I$ is still a left $A$-module but not in general an algebra. Thus the left ideals govern module theory and the two-sided ideals govern quotient algebras.

## 2. The Two-Sided Ideals: Simplicity of $\mathbb{B}$

**Theorem.** Over $\mathbb{C}$, the only two-sided ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$. Equivalently, $\mathbb{B}$ is a **simple** $\mathbb{C}$-algebra.

**Proof.** Transport along $\mathbb{B} \cong M_2(\mathbb{C})$. Let the matrix units satisfy

$$
E_{ij} E_{kl} = \delta_{jk} E_{il},
$$

from which $E_{ik} X E_{lj} = X_{kl} E_{ij}$ for any matrix $X = (X_{kl})$. If $I \neq 0$ is a two-sided ideal and $X \in I$ has $X_{kl} \neq 0$, then

$$
E_{ij} = X_{kl}^{-1} E_{ik} X E_{lj} \in I.
$$

Hence $I$ contains every matrix unit, so $I = M_2(\mathbb{C})$. Transporting back gives the claim. $\square$

Consequences over $\mathbb{C}$:

- The only quotient algebras of $\mathbb{B}$ are $\mathbb{B}$ and $0$.
- Every nonzero element generates $\mathbb{B}$ as a two-sided ideal.
- The center of $\mathbb{B}$ is the scalar copy of $\mathbb{C}$, so $\mathbb{B}$ is a **central simple** $\mathbb{C}$-algebra; in particular it is not a product $A_1 \times A_2$ of nonzero algebras, since each factor would give a nontrivial two-sided ideal.
- The many one-sided ideals of Sections 8 and 9 are all non-two-sided, so they do not contradict simplicity.

## 3. Artinian, Semisimple, and Length Two

A nonzero module is **simple** if it has no submodules other than $0$ and itself. A **composition series** is a finite strictly increasing chain $0 = M_0 \subset M_1 \subset \cdots \subset M_r = M$ with simple successive quotients $M_i/M_{i-1}$; the number $r$ is the **length** of $M$. A ring is **left artinian** if every descending chain of left ideals stabilizes, and **semisimple** if its left regular module is a direct sum of simple modules.

Over $\mathbb{C}$, every descending chain of left ideals of $\mathbb{B}$ is a descending chain of $\mathbb{C}$-subspaces, so it stabilizes; thus $\mathbb{B}$ is artinian. By Wedderburn–Artin, a unital ring is semisimple if and only if it is artinian with zero Jacobson radical, and every simple artinian ring is semisimple. Hence $\mathbb{B}$ is **semisimple**, and every left ideal is a direct sum of minimal left ideals.

All simple left $\mathbb{B}$-modules are isomorphic to the two-dimensional complex vector space $S = \mathbb{C}^2$, the **spinor module**, on which $\mathbb{B} \cong M_2(\mathbb{C}) = \operatorname{End}_{\mathbb{C}}(S)$ acts. As a left module over itself,

$$
\mathbb{B} \cong S \oplus S.
$$

With the idempotents $p, q$ of Section 4 this reads $\mathbb{B} = \mathbb{B}p \oplus \mathbb{B}q$ with $\mathbb{B}p \cong \mathbb{B}q \cong S$. Hence $0 \subset \mathbb{B}p \subset \mathbb{B}$ is a composition series, and the **length of $\mathbb{B}$ as a left module over itself is $2$**, with both factors isomorphic to $S$. The right regular module has length $2$ as well, with factors the dual module $S^{*}$. All of this is over $\mathbb{C}$.

# Part II: Idempotents and the Peirce Decomposition

## 4. Idempotents and Orthogonal Idempotents

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$. Idempotents encode direct summands: for idempotent $e$,

$$
A = Ae \oplus A(1-e) \quad (\text{left}), \qquad A = eA \oplus (1-e)A \quad (\text{right}),
$$

and every such decomposition of the regular module arises from an idempotent. Two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$; then $e+f$ is again idempotent. A family $\{e_1, \dots, e_n\}$ is pairwise orthogonal if $e_i e_j = 0$ for $i \neq j$, and **complete** if in addition $\sum_i e_i = 1$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents. The criterion used below, for a semisimple algebra $A$, is

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

**Explicit idempotents in $\mathbb{B}$.** Over $\mathbb{C}$, put

$$
p = \frac{e_0 + i e_3}{2}, \qquad q = \frac{e_0 - i e_3}{2}.
$$

Since $(i e_3)^2 = i^2 e_3^2 = (-1)(-1) = 1$, one has $p^2 = p$, $q^2 = q$ and

$$
pq = qp = \frac{e_0 - (i e_3)^2}{4} = 0, \qquad p + q = e_0.
$$

So $p$ and $q$ are orthogonal idempotents summing to the unit. They are not central: $e_1$ anticommutes with $i e_3$, hence does not commute with $p$ or $q$. Under $\mathbb{B} \cong M_2(\mathbb{C})$ they correspond to the diagonal matrix units, and each is primitive.

## 5. Matrix Units in the Biquaternion Algebra

The off-diagonal matrix units can also be written explicitly. Put

$$
x = \frac{i e_1 - e_2}{2}, \qquad y = \frac{i e_1 + e_2}{2}.
$$

Then $\{p, x, y, q\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$, and it satisfies the matrix-unit relations with

$$
E_{11} = p, \qquad E_{12} = x, \qquad E_{21} = y, \qquad E_{22} = q.
$$

Explicitly, $p^2 = p$, $q^2 = q$, $pq = qp = 0$, $p+q = e_0$, and

$$
px = x = xq, \qquad qy = y = yp, \qquad xy = p, \qquad yx = q,
$$

together with $xp = qx = py = 0$, $yq = 0$, and $x^2 = y^2 = 0$. These are the multiplication table of $M_2(\mathbb{C})$ written in biquaternion coordinates.

## 6. The Peirce Decomposition

The **Peirce decomposition** is the decomposition of an algebra relative to a family of orthogonal idempotents; it is the algebraic form of a block decomposition of a matrix.

**One idempotent.** Let $e \in A$ be idempotent and $f = 1-e$. Every $a \in A$ expands as $a = eae + eaf + fae + faf$, giving the direct sum

$$
A = eAe \oplus eAf \oplus fAe \oplus fAf,
$$

whose summands are the **Peirce spaces**. The corner $eAe$ is a subalgebra with identity $e$; the other corners are only one-sided pieces. The expansion, the directness of the four terms and the product rule below are proved in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, where the case of a **central** idempotent is also separated: for a central $e$ the off-diagonal corners vanish and the sum is a product of algebras. That special case does not arise here, since the idempotents of this article lie in a simple algebra and no nontrivial idempotent of $\mathbb{B}$ is central.

**A complete orthogonal family.** If $\{e_1, \dots, e_n\}$ is complete and pairwise orthogonal, the same expansion gives

$$
A = \bigoplus_{i,j=1}^{n} e_i A e_j, \qquad (e_i A e_j)(e_k A e_l) \subseteq \delta_{jk}\, e_i A e_l.
$$

Each diagonal corner $e_i A e_i$ is an algebra with identity $e_i$, and each off-diagonal piece is a bimodule over the corresponding corners.

**The biquaternion case.** Take $e_1 = p$, $e_2 = q$ from Section 4. The Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B} = p\mathbb{B}p \oplus p\mathbb{B}q \oplus q\mathbb{B}p \oplus q\mathbb{B}q,
$$

and by the table of Section 5 each summand is one-dimensional over $\mathbb{C}$:

$$
p\mathbb{B}p = \mathbb{C}p, \qquad p\mathbb{B}q = \mathbb{C}x, \qquad q\mathbb{B}p = \mathbb{C}y, \qquad q\mathbb{B}q = \mathbb{C}q.
$$

So the Peirce decomposition is exactly the matrix-unit decomposition

$$
\mathbb{B} = \mathbb{C}p \oplus \mathbb{C}x \oplus \mathbb{C}y \oplus \mathbb{C}q = \bigoplus_{i,j=1}^{2} \mathbb{C}E_{ij}.
$$

The diagonal part $p\mathbb{B}p \oplus q\mathbb{B}q = \mathbb{C}p \oplus \mathbb{C}q$ is a two-dimensional commutative subalgebra isomorphic to $\mathbb{C} \times \mathbb{C}$, the diagonal subalgebra of the matrix picture. Each diagonal corner is a division ring, namely $\mathbb{C}$, which is the primitivity criterion of Section 4.

## 7. The Matrix-Unit Decomposition as a Sum of Minimal Ideals

The matrix units group into one-sided ideals in a second way. With $E_{11} = p$ and $E_{22} = q$, the two **columns** $\mathbb{B}p, \mathbb{B}q$ and the two **rows** $p\mathbb{B}, q\mathbb{B}$ are one-sided ideals, and

$$
\mathbb{B} = \mathbb{B}p \oplus \mathbb{B}q = (\mathbb{C}p \oplus \mathbb{C}y) \oplus (\mathbb{C}x \oplus \mathbb{C}q),
$$

$$
\mathbb{B} = p\mathbb{B} \oplus q\mathbb{B} = (\mathbb{C}p \oplus \mathbb{C}x) \oplus (\mathbb{C}y \oplus \mathbb{C}q).
$$

The first exhibits $\mathbb{B}$ as a direct sum of the two minimal left ideals (the columns); the second exhibits it as a direct sum of the two minimal right ideals (the rows). The two groupings of the same four basis elements differ: the Peirce decomposition groups $p$ with $x$ and $q$ with $y$, whereas the column decomposition groups $p$ with $y$ and $q$ with $x$. Each column is two-dimensional over $\mathbb{C}$ and isomorphic, as a left $\mathbb{B}$-module, to $S = \mathbb{C}^2$; each row is isomorphic to the dual $S^{*}$. Since $\mathbb{B}$ is simple, a column or a row is never a two-sided ideal; for instance $\mathbb{B}p$ is not stable under right multiplication by $x$.

# Part III: One-Sided Ideals, the Radical, and the Real Structure

## 8. Minimal Left and Right Ideals

A **minimal left ideal** is a nonzero left ideal containing no nonzero proper left ideal; equivalently, a simple submodule of the left regular module. A **minimal right ideal** is defined the same way on the right.

Over $\mathbb{C}$, since $\mathbb{B}$ is semisimple, every left ideal of $\mathbb{B}$ is a direct sum of minimal left ideals, and every minimal left ideal is of the form $\mathbb{B}e$ for a primitive idempotent $e$. The coordinate examples are the columns $\mathbb{B}p$ and $\mathbb{B}q$ of Section 7, and all minimal left ideals are isomorphic as left $\mathbb{B}$-modules to the simple module $S = \mathbb{C}^2$: a general one is obtained from a column by an algebra automorphism, so it is again a column in a suitable basis. Dually, every minimal right ideal is a row and is isomorphic to $S^{*}$, the coordinate examples being $p\mathbb{B}$ and $q\mathbb{B}$. Thus there is one isomorphism class of simple left modules and one of simple right modules. Being nonzero proper one-sided ideals, none of them is two-sided — which is exactly why their abundance is compatible with Section 2.

## 9. The Lattice of Left Ideals as a Projective Line

The one-sided ideals can be listed explicitly. Over $\mathbb{C}$, for each $\mathbb{C}$-subspace $W \subseteq \mathbb{C}^2$ define

$$
L_W = \{\, M \in M_2(\mathbb{C}) : M|_W = 0 \,\},
$$

the matrices annihilating $W$. This is a left ideal, since $\ker(AM) \supseteq \ker M$ for every $A$. The assignment $W \mapsto L_W$ reverses inclusions, and

$$
L_0 = \mathbb{B}, \qquad L_{\mathbb{C}^2} = 0, \qquad L_W \text{ is minimal when } \dim_{\mathbb{C}} W = 1.
$$

Conversely every left ideal is of this form: a left ideal is a submodule of the left regular module $\mathbb{B} \cong S \oplus S$, and since $S$ is simple and $\mathbb{B}$ has length $2$, the only submodules of $S \oplus S$ are $0$, a copy of $S$, and the whole module. A minimal left ideal $L$ is thus a copy of $S$, determined by the line $W = \bigcap_{M \in L} \ker M$.

**Theorem (over $\mathbb{C}$).** The left ideals of $\mathbb{B}$ are exactly $0$, the whole algebra $\mathbb{B}$, and the minimal left ideals $L_W$ with $W$ a line in $\mathbb{C}^2$. The minimal left ideals are indexed by the projective line

$$
\mathbb{P}^1(\mathbb{C}) = \{\, W \subseteq \mathbb{C}^2 : W \text{ a one-dimensional } \mathbb{C}\text{-subspace} \,\},
$$

and they form the middle layer of the lattice:

$$
0 \;\subset\; \{\, L_W : W \in \mathbb{P}^1(\mathbb{C}) \,\} \;\subset\; \mathbb{B}.
$$

The middle elements are pairwise incomparable; each covers $0$ and is covered by $\mathbb{B}$. Because the length of $\mathbb{B}$ as a left module over itself is $2$, every minimal left ideal is also a **maximal** left ideal: nothing lies strictly between it and $\mathbb{B}$. Right ideals admit the same description, with lines in the dual space and the rows as coordinate members.

The parameter space deserves a caution. The projective space classifying the minimal one-sided ideals of $M_n(D)$ is $\mathbb{P}^{n-1}(D)$, over the **division ring** $D$ in the Wedderburn–Artin decomposition $M_n(D)$ — not over an arbitrary base field. Here $D = \mathbb{C}$ and $n = 2$, so the parameter space is $\mathbb{P}^1(\mathbb{C})$. In particular, regarding $\mathbb{B}$ as an $\mathbb{R}$-algebra does not replace this by $\mathbb{P}^1(\mathbb{R})$: the one-sided ideals are still parametrized by $\mathbb{P}^1(\mathbb{C})$. The real projective line appears only as the subfamily of kernels that the real structure preserves, not as a set of fixed minimal left ideals: Section 11 shows that no minimal left ideal is stable under coefficient conjugation.

## 10. The Radical

The **Jacobson radical** $J(A)$ is the intersection of all maximal left ideals of $A$, equivalently of all maximal right ideals; it is a two-sided ideal. For an artinian ring, $J(A)$ is the largest nilpotent ideal and $A/J(A)$ is semisimple; an artinian ring is semisimple if and only if its radical is zero.

Over $\mathbb{C}$, the radical of $\mathbb{B}$ vanishes:

$$
J(\mathbb{B}) = 0.
$$

Indeed $J(\mathbb{B})$ is a two-sided ideal, hence by simplicity is $0$ or $\mathbb{B}$; it cannot be $\mathbb{B}$, since in a unital algebra the radical is proper. This restates the semisimplicity of Section 3 in terms of the radical. Consequences over $\mathbb{C}$:

- $\mathbb{B}$ has no nonzero **nilpotent two-sided ideals**; the nilradical is zero.
- It has no nonzero nilpotent left or right ideals either, since such an ideal generates a nonzero nilpotent two-sided ideal.
- The absence of a radical is not the absence of nilpotent **elements**: $x^2 = y^2 = 0$ (Section 5), yet the left ideal generated by $x$ is not nilpotent.
- Every left $\mathbb{B}$-module is semisimple, i.e., a direct sum of copies of $S = \mathbb{C}^2$.

## 11. The Real Structure

Everything so far was stated over $\mathbb{C}$. We now regard the same set $\mathbb{B}$ as an eight-dimensional algebra over $\mathbb{R}$ and record what changes.

**(a) The ideal lattice does not change.** By the base-field remark of Section 1, an additive subgroup closed under left multiplication by $\mathbb{B}$ is automatically a complex subspace, because multiplication by $i$ is left multiplication by the central element $i e_0$. So an $\mathbb{R}$-left ideal is the same thing as a $\mathbb{C}$-left ideal, and the same holds on the right and for two-sided ideals. In particular, over $\mathbb{R}$: $\mathbb{B}$ is still simple, with two-sided ideals only $0$ and $\mathbb{B}$; the minimal left ideals are the same subsets, parametrized by $\mathbb{P}^1(\mathbb{C})$; the radical is still zero; and the length as a module over itself is still $2$.

**(b) The algebra is not central over $\mathbb{R}$.** The center of $\mathbb{B}$ is the copy of $\mathbb{C}$ spanned by $e_0$ and $i e_0$ — the **complex subspace** $\mathbb{C}_{\mathbb{B}}$ — a proper field extension of $\mathbb{R}$ of degree $2$. Thus $\mathbb{B}$ is a simple $\mathbb{R}$-algebra but not a **central simple** one. In the Wedderburn–Artin description $\mathbb{B} \cong M_n(D)$ over $\mathbb{R}$, one has $n = 2$ and $D = \mathbb{C}$.

**(c) The enrichment appears after extension of scalars.** The complexification of the real algebra $\mathbb{B}$ is

$$
\mathbb{B} \otimes_{\mathbb{R}} \mathbb{C} \cong M_2(\mathbb{C}) \otimes_{\mathbb{R}} \mathbb{C} \cong M_2(\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C}) \cong M_2(\mathbb{C} \oplus \mathbb{C}) \cong M_2(\mathbb{C}) \oplus M_2(\mathbb{C}),
$$

using $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$. The algebra on the right is **not simple**: its two-sided ideals are $0$, the two summands, and the whole ring. So the real biquaternion algebra is **not absolutely simple**: simple over $\mathbb{R}$, but with a complexification that splits as a product of two simple algebras. This is the precise sense in which the real structure carries a richer two-sided ideal theory — not in the lattice of $\mathbb{B}$ itself, which is $\{0, \mathbb{B}\}$ in both views, but in the lattice produced by base change. In contrast, $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{B}$ is simple: it is the real biquaternion algebra, not $\mathbb{H}$, whose complexification splits.

**(d) The action of complex conjugation on the lattice.** Complex conjugation $\tilde{Q} \mapsto \tilde{Q}^{*} = \sum_\mu \bar{Q}_\mu e_\mu$ is an $\mathbb{R}$-algebra automorphism of $\mathbb{B}$ (it is $\mathbb{C}$-antilinear), so it permutes the left ideals, $\sigma(\mathbb{B}\tilde{\chi}) = \mathbb{B}\sigma(\tilde{\chi})$. Since $\sigma(p) = q$ and $\sigma(q) = p$, it **interchanges the two columns**:

$$
\sigma(\mathbb{B}p) = \mathbb{B}q, \qquad \sigma(\mathbb{B}q) = \mathbb{B}p.
$$

It does **not** act as entrywise conjugation of the matrix. With $\varphi(\tilde{Q}) = M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ under the isomorphism of Section 5, coefficient conjugation is

$$
\varphi(\tilde{Q}^{*}) = \begin{pmatrix} \bar{d} & -\bar{c} \\ -\bar{b} & \bar{a} \end{pmatrix} = J\,\overline{M}\,J^{-1}, \qquad J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \varphi(-e_2),
$$

whereas entrywise conjugation fixes $E_{11} = p$ and would leave $\mathbb{B}p$ invariant. The two differ already on $e_1$: $\varphi(e_1) = -i\sigma_1$ is fixed by $\sigma$, but entrywise conjugation carries it to $+i\sigma_1$.

On a minimal left ideal $L_W$ the action is

$$
\sigma(L_W) = L_{W^{\perp}},
$$

where $W^{\perp}$ is the **Hermitian-orthogonal complement** of $W$ in $\mathbb{C}^2$: if $W = \operatorname{span}(w_1, w_2)$, then $W^{\perp} = \operatorname{span}(\bar{w}_2, -\bar{w}_1)$. In the affine coordinate $t = w_2/w_1$ the induced map on $\mathbb{P}^1(\mathbb{C})$ is $t \mapsto -1/\bar{t}$, whose fixed-point equation $t = -1/\bar{t}$ reads $|t|^2 = -1$ and has no solution. So **no minimal left ideal is stable under complex conjugation**: the involution $W \mapsto W^{\perp}$ is fixed-point-free and pairs the two columns, which is the algebraic form of the statement, used elsewhere in the series, that coefficient conjugation exchanges the defining module $S$ and its conjugate $\bar{S}$.

The **real lines** $W = \overline{W}$ still form the real projective line

$$
\mathbb{P}^1(\mathbb{R}) \subset \mathbb{P}^1(\mathbb{C}),
$$

and $\sigma$ preserves this subfamily — the Hermitian orthogonal of a real line is again real — acting on it as the antipodal map $W \mapsto W^{\perp}$. So although the lattice of left ideals is unchanged from $\mathbb{C}$ to $\mathbb{R}$, the real structure does not mark out conjugation-stable minimal left ideals; what it marks out is the subfamily $\mathbb{P}^1(\mathbb{R})$ of kernels that it preserves, on which it acts without fixed points.

## Summary

| Statement | Over $\mathbb{C}$ | Over $\mathbb{R}$ |
|---|---|---|
| Dimension | $4$ | $8$ |
| Algebra type | $M_2(\mathbb{C})$ | $M_2(\mathbb{C})$ |
| Two-sided ideals | $0$, $\mathbb{B}$ (simple) | $0$, $\mathbb{B}$ (simple) |
| Central simple? | yes, center $\mathbb{C}$ | no, center $\mathbb{C} \neq \mathbb{R}$ |
| Left ideals | $0$, the $\mathbb{P}^1(\mathbb{C})$ of minimal ones, $\mathbb{B}$ | same lattice |
| Minimal left ideals | columns, all $\cong \mathbb{C}^2$ | same; $\sigma$ pairs $L_W \leftrightarrow L_{W^{\perp}}$, none stable |
| Minimal right ideals | rows, all $\cong (\mathbb{C}^2)^{*}$ | same |
| Jacobson radical | $0$ | $0$ |
| Length as module over itself | $2$ | $2$ |
| Base change $\otimes_{\mathbb{R}}\mathbb{C}$ | — | $M_2(\mathbb{C}) \oplus M_2(\mathbb{C})$, not simple |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; $M_2(\mathbb{C})$ over $\mathbb{C}$, real dimension $8$ over $\mathbb{R}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary; $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center |
| $p, q$ | Orthogonal idempotents, $p+q = e_0$, $pq = qp = 0$; the diagonal matrix units |
| $x, y$ | Nilpotent off-diagonal elements, $x = \tfrac{i e_1 - e_2}{2}$, $y = \tfrac{i e_1 + e_2}{2}$, $x^2 = y^2 = 0$ |
| $E_{ij}$ | Matrix units, $E_{11} = p$, $E_{12} = x$, $E_{21} = y$, $E_{22} = q$ |
| $L_W$ | Minimal left ideal defined by a line $W \subset \mathbb{C}^2$; $L_W \perp L_{W'}$ in the Hermitian sense |
| $\mathbb{P}^1(\mathbb{C})$ | The projective line parameterising the minimal left ideals |
| $\sigma$ | The real structure, pairing $L_W \leftrightarrow L_{W^{\perp}}$ |
| $\mathcal{J}$ | Jacobson radical; it is $0$ for $\mathbb{B}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982). The standard reference for the Peirce decomposition and the structure theory of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001). Simplicity, semisimplicity, the Jacobson radical, and matrix rings.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009). Wedderburn–Artin theory and the radical.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002). Ring and module theory, central simple algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001). The biquaternion algebra as $M_2(\mathbb{C})$ and its matrix and spinor models.
