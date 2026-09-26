# __Biquaternion Ideals and Peirce Decomposition__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$. This article studies its ideal structure and the decomposition of $\mathbb{B}$ relative to a family of idempotents, and it reads both physically.

Two facts organise the discussion. As a $\mathbb{C}$-algebra, $\mathbb{B}\cong M_2(\mathbb{C})$; and $\mathbb{B}$ is **simple**, its only two-sided ideals being $0$ and $\mathbb{B}$. The ideal theory is therefore a theory of **one-sided** ideals, governed by the matrix structure: the left ideals are $0$, the minimal ones, and $\mathbb{B}$, and the Peirce decomposition splits the algebra into four one-dimensional corners relative to a pair of orthogonal idempotents.

Physically, this is the representation theory the whole framework runs on. The minimal left ideals are the **one-particle modules**: a left ideal of $\mathbb{B}$ is a two-complex-dimensional space on which the algebra acts, and that is what a state of the theory lives in. There is one such module up to isomorphism, so no intrinsic label distinguishes the different copies; the labels physics uses — spin, chirality, particle and antiparticle — come from extra structure laid on top, and Section 11 shows which structure: the **real structure** of coefficient conjugation, which pairs the defining module with its conjugate and therefore distinguishes $S$ from $\bar{S}$. The Peirce decomposition is the block structure of the matrix model, with the diagonal corners the two state projectors and the off-diagonal corners the transition (ladder) elements between them. And the simplicity of the algebra has a physical content of its own: the framework's two sectors, the material $\mathbb{M}_-$ and the informational $\mathbb{M}_+$, are **not** a decomposition into algebras, since a simple algebra has no nontrivial two-sided ideals; the sector split is a real-structure split and not an ideal-theoretic one.

Because the biquaternions carry both a complex and a real structure, every statement is tagged with the field over which it is made. Sections 1 to 10 work over $\mathbb{C}$; Section 11 discusses the $\mathbb{R}$-view, where the ideal lattice is unchanged but the real structure leaves further traces. Notation follows the algebra article: $e_0$ is the unit, $e_1,e_2,e_3$ the quaternion units with $e_1e_2 = e_3$, $i$ the central scalar imaginary, and $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. "Left" and "right" must be distinguished, the algebra being noncommutative.

# Part I: Ideals and Simplicity

## 1. Ideals in an Algebra

Let $A$ be an associative unital algebra over a field $k$. An additive subgroup $I\subseteq A$ is a **left ideal** if $AI\subseteq I$, a **right ideal** if $IA\subseteq I$, and a **two-sided ideal** if it is both. The distinction matters only when $A$ is noncommutative; for $\mathbb{B}$ the three notions genuinely differ. The ideals $0$ and $A$ are trivial.

A base-field remark used repeatedly: if $AI\subseteq I$ then $I$ is automatically a $k$-subspace, since $\lambda x = (\lambda e_0)x\in I$. So the left ideals do not depend on which field of scalars inside the centre is used to view the algebra; in particular the ideal lattice of $\mathbb{B}$ is the same in the $\mathbb{C}$-view and the $\mathbb{R}$-view (Section 11).

For a two-sided ideal $I$, the quotient algebra $A/I$ is defined and carries the induced operations; kernels of algebra homomorphisms are two-sided ideals, and $A/\ker\varphi\cong\operatorname{im}\varphi$. For a left ideal only, $A/I$ is a left $A$-module but not in general an algebra. Thus left ideals govern module theory and two-sided ideals govern quotient algebras.

## 2. The Two-Sided Ideals: Simplicity of $\mathbb{B}$

**Theorem.** Over $\mathbb{C}$, the only two-sided ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$: the algebra is **simple**.

**Proof.** Transport along $\mathbb{B}\cong M_2(\mathbb{C})$. With matrix units $E_{ij}E_{kl} = \delta_{jk}E_{il}$, one has $E_{ik}ME_{lj} = M_{kl}E_{ij}$ for $M = (M_{kl})$. If $I\neq0$ is two-sided and $M\in I$ has $M_{kl}\neq0$, then

$$
E_{ij} = M_{kl}^{-1}E_{ik}ME_{lj} \in I ,
$$

so $I$ contains every matrix unit and $I = M_2(\mathbb{C})$. $\square$

Consequences over $\mathbb{C}$:

- the only quotients of $\mathbb{B}$ are $\mathbb{B}$ and $0$;
- every nonzero element generates $\mathbb{B}$ as a two-sided ideal;
- the centre of $\mathbb{B}$ is the scalar copy of $\mathbb{C}$, so $\mathbb{B}$ is **central simple** over $\mathbb{C}$; in particular it is not a product $A_1\times A_2$ of nonzero algebras, since each factor would give a nontrivial two-sided ideal;
- the many one-sided ideals of Sections 8 and 9 are all non-two-sided, so they do not contradict simplicity.

**Physical reading: why the two sectors are not two algebras.** The framework's central structural split is the sector decomposition $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$ into the anti-Hermitian and Hermitian elements, and it is natural to read the two sectors as two worlds. The theorem forbids the strongest form of that reading: a decomposition of the algebra into two independent pieces would be a pair of complementary two-sided ideals, and there are none. The sector split is a split of the underlying real vector space by the involution $\dagger$, not an ideal decomposition, and $\mathbb{M}_\pm$ are not subalgebras (the product of two Hermitian elements is generally not Hermitian). The two sectors are two **readings** of one simple algebra, which is a stronger statement than a product of two algebras would be: no information is lost in passing from one to the other, since there is only one algebra.

## 3. Artinian, Semisimple, and Length Two

A nonzero module is **simple** if it has no submodules other than $0$ and itself. A **composition series** is a finite strictly increasing chain $0 = M_0\subset\cdots\subset M_r = M$ with simple successive quotients, and $r$ is the **length**. A ring is **left artinian** if every descending chain of left ideals stabilises, and **semisimple** if its left regular module is a direct sum of simple modules.

Over $\mathbb{C}$, every descending chain of left ideals of $\mathbb{B}$ is a descending chain of $\mathbb{C}$-subspaces, hence stabilises: $\mathbb{B}$ is artinian. By Wedderburn–Artin a unital ring is semisimple if and only if it is artinian with zero Jacobson radical, and every simple artinian ring is semisimple. Hence $\mathbb{B}$ is **semisimple**, and every left ideal is a direct sum of minimal left ideals.

All simple left $\mathbb{B}$-modules are isomorphic to the two-dimensional complex vector space $S = \mathbb{C}^2$, on which $\mathbb{B}\cong M_2(\mathbb{C}) = \operatorname{End}_{\mathbb{C}}(S)$ acts; this is the **defining module** of the framework. As a left module over itself,

$$
\mathbb{B}\cong S\oplus S ,
$$

which with the idempotents of Section 4 reads $\mathbb{B} = \mathbb{B}p\oplus\mathbb{B}q$ with $\mathbb{B}p\cong\mathbb{B}q\cong S$. Hence $0\subset\mathbb{B}p\subset\mathbb{B}$ is a composition series, and the **length of $\mathbb{B}$ as a left module over itself is $2$**, both factors isomorphic to $S$. The right regular module has length $2$ as well, with factors the dual module $S^{*}$. All of this is over $\mathbb{C}$.

**Physical reading.** The defining module is two-dimensional, and every module the framework builds is a direct sum of copies of it: that is the algebraic reason the theory is a two-state theory at bottom, and the reason a state space in this framework is a space of two-component objects. The length-2 statement is the algebraic form of the fact that the regular module contains two copies of the defining module and no more. The module's dual, its conjugate and the reality conditions on it are developed in *The Native Qubit and the Defining Module of the Biquaternion Algebra* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action*.

# Part II: Idempotents and the Peirce Decomposition

## 4. Idempotents and Orthogonal Idempotents

Let $A$ be an associative unital algebra. An element $e$ is an **idempotent** if $e^2 = e$, and two idempotents are **orthogonal** if $ef = fe = 0$. A nonzero idempotent is **primitive** if it is not a sum of two nonzero orthogonal idempotents, and for a semisimple algebra

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring} .
$$

Over $\mathbb{C}$, the idempotents

$$
p = \frac{e_0+ie_3}{2}, \qquad q = \frac{e_0-ie_3}{2}
$$

satisfy $p^2 = p$, $q^2 = q$, $pq = qp = 0$ and $p+q = e_0$, and correspond to the diagonal matrix units $E_{11}$ and $E_{22}$. They are primitive and they generate the matrix units of the next section.

The classification of the idempotents — the trivial ones, the bijection with the roots of $-1$, the Hermitian projections and the dimension of the idempotent set — is the subject of *Biquaternion Idempotents and Projections*. In the physical reading of that article, $p$ and $q$ are the two rank-one projectors of a single mode, and the only idempotents that are orthogonal projections are the Hermitian ones.

## 5. Matrix Units in the Biquaternion Algebra

The off-diagonal matrix units can be written explicitly. Put

$$
x = \frac{ie_1-e_2}{2}, \qquad y = \frac{ie_1+e_2}{2} .
$$

Then $\{p,x,y,q\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$ satisfying the matrix-unit relations with

$$
E_{11} = p, \qquad E_{12} = x, \qquad E_{21} = y, \qquad E_{22} = q .
$$

Explicitly, $p^2 = p$, $q^2 = q$, $pq = qp = 0$, $p+q = e_0$, and

$$
px = x = xq, \qquad qy = y = yp, \qquad xy = p, \qquad yx = q,
$$

together with $xp = qx = py = yq = 0$ and $x^2 = y^2 = 0$. This is the multiplication table of $M_2(\mathbb{C})$ in biquaternion coordinates.

**Physical reading: the transition elements.** The off-diagonal elements $x$ and $y$ are the **ladder operators** of the algebra. They are not states and cannot be: each has vanishing norm form, $N(x) = N(y) = 0$, so each is a zero divisor and not invertible; neither is Hermitian; and each is nilpotent, $x^2 = y^2 = 0$, so neither is an idempotent and neither can be a projector. What they do is move between the two diagonal corners: $xy = p$ and $yx = q$, so the products of a raising and a lowering element are the two state projectors. A transition in the framework is therefore a **product of two off-diagonal Peirce elements**, which is the algebraic form of the statement that an observable's off-diagonal part is what makes two states interfere.

## 6. The Peirce Decomposition

The **Peirce decomposition** is the decomposition of an algebra relative to a family of orthogonal idempotents; it is the algebraic form of a block decomposition of a matrix.

**One idempotent.** Let $e\in A$ be idempotent and $f = e_0-e$. Every $a\in A$ expands as

$$
a = eae + eaf + fae + faf ,
$$

giving the direct sum $A = eAe\oplus eAf\oplus fAe\oplus fAf$ into the **Peirce spaces**. The corner $eAe$ is a subalgebra with identity $e$; the other corners are only one-sided pieces. For a **central** idempotent the off-diagonal corners vanish and the sum is a product of algebras; that case does not arise here, since no nontrivial idempotent of $\mathbb{B}$ is central (the algebra is simple and the idempotents are non-central).

**A complete orthogonal family.** For $\{e_1,\dots,e_n\}$ complete and pairwise orthogonal,

$$
A = \bigoplus_{i,j=1}^{n}e_iAe_j, \qquad (e_iAe_j)(e_kAe_l)\subseteq\delta_{jk}\,e_iAe_l .
$$

**The biquaternion case.** Take $e_1 = p$, $e_2 = q$. The Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B} = p\mathbb{B}p\oplus p\mathbb{B}q\oplus q\mathbb{B}p\oplus q\mathbb{B}q ,
$$

and by the table of Section 5 each summand is one-dimensional over $\mathbb{C}$:

$$
p\mathbb{B}p = \mathbb{C}p, \qquad p\mathbb{B}q = \mathbb{C}x, \qquad q\mathbb{B}p = \mathbb{C}y, \qquad q\mathbb{B}q = \mathbb{C}q .
$$

So the Peirce decomposition is exactly the matrix-unit decomposition

$$
\mathbb{B} = \mathbb{C}p\oplus\mathbb{C}x\oplus\mathbb{C}y\oplus\mathbb{C}q = \bigoplus_{i,j=1}^{2}\mathbb{C}E_{ij} .
$$

The diagonal part $\mathbb{C}p\oplus\mathbb{C}q$ is a two-dimensional commutative subalgebra isomorphic to $\mathbb{C}\times\mathbb{C}$, the diagonal subalgebra of the matrix picture. Each diagonal corner is a division ring, namely $\mathbb{C}$, which is the primitivity criterion of Section 4.

**Physical reading: the block structure of an observable.** The four corners are the four blocks: two diagonal blocks, each the complex line spanned by a state projector, and two off-diagonal blocks, each the complex line spanned by a transition element. Expanding an element of $\mathbb{B}$ in this decomposition is writing it as a $2\times2$ matrix with respect to the pair of states, and that is what the quantum-mechanical articles do when they write an observable or a density element in the two-state basis. The diagonal commutativity — $\mathbb{C}p\oplus\mathbb{C}q\cong\mathbb{C}\times\mathbb{C}$ — is the algebraic form of the fact that two orthogonal projectors can be read simultaneously.

## 7. The Matrix-Unit Decomposition as a Sum of Minimal Ideals

The matrix units group into one-sided ideals in a second way. With $E_{11} = p$ and $E_{22} = q$, the two **columns** $\mathbb{B}p,\mathbb{B}q$ and the two **rows** $p\mathbb{B},q\mathbb{B}$ are one-sided ideals, and

$$
\mathbb{B} = \mathbb{B}p\oplus\mathbb{B}q = (\mathbb{C}p\oplus\mathbb{C}y)\oplus(\mathbb{C}x\oplus\mathbb{C}q),
$$

$$
\mathbb{B} = p\mathbb{B}\oplus q\mathbb{B} = (\mathbb{C}p\oplus\mathbb{C}x)\oplus(\mathbb{C}y\oplus\mathbb{C}q).
$$

The first exhibits $\mathbb{B}$ as a direct sum of the two minimal left ideals (the columns); the second as a direct sum of the two minimal right ideals (the rows). The two groupings of the same four basis elements differ: the Peirce decomposition groups $p$ with $x$ and $q$ with $y$, whereas the column decomposition groups $p$ with $y$ and $q$ with $x$. Each column is two-dimensional over $\mathbb{C}$ and isomorphic as a left $\mathbb{B}$-module to $S = \mathbb{C}^2$; each row is isomorphic to the dual $S^{*}$. Since $\mathbb{B}$ is simple, a column or a row is never two-sided; for instance $\mathbb{B}p$ is not stable under right multiplication by $x$.

**Physical reading: modules and dual modules.** The columns are the **one-particle modules**: each is a copy of $S$, and a state is an element of one. The rows are their duals, the spaces of linear functionals, which is where the conjugate (antiparticle) side is reached — not by transposing but through the real structure of Section 11. The two groupings are the reason a statement about the algebra can be read either by states or by functionals, and the reason a reader must say which grouping is meant: the Peirce blocks are not the columns, even though both are built from the same four elements.

# Part III: One-Sided Ideals, the Radical, and the Real Structure

## 8. Minimal Left and Right Ideals

A **minimal left ideal** is a nonzero left ideal containing no nonzero proper left ideal, equivalently a simple submodule of the left regular module. Over $\mathbb{C}$, since $\mathbb{B}$ is semisimple, every left ideal is a direct sum of minimal left ideals, and every minimal left ideal is $\mathbb{B}e$ for a primitive idempotent $e$. The coordinate examples are the columns $\mathbb{B}p$ and $\mathbb{B}q$, and **all minimal left ideals are isomorphic** as left $\mathbb{B}$-modules to $S = \mathbb{C}^2$: a general one is obtained from a column by an algebra automorphism. Dually every minimal right ideal is a row, isomorphic to $S^{*}$, with coordinate examples $p\mathbb{B}$ and $q\mathbb{B}$. There is one isomorphism class of simple left modules and one of simple right modules; being nonzero proper one-sided ideals, none of them is two-sided, which is why their abundance is compatible with Section 2.

**Physical reading.** Since all one-particle modules are isomorphic, the algebra alone cannot tell two of them apart. Any distinction between one copy and another — between two spin states, between a particle and an antiparticle, between two chiralities — must come from structure **outside** the left module structure: from a chosen idempotent, from an involution, or from the real structure. This is exactly the shape the framework's physical identifications take, and the reason the corpus is careful to say which structure supplies which label.

## 9. The Lattice of Left Ideals as a Projective Line

The one-sided ideals can be listed explicitly. Over $\mathbb{C}$, for each $\mathbb{C}$-subspace $W\subseteq\mathbb{C}^2$ define

$$
L_W = \{\,M\in M_2(\mathbb{C}) : M|_W = 0\,\},
$$

the matrices annihilating $W$. This is a left ideal, since $\ker(AM)\supseteq\ker M$. The assignment $W\mapsto L_W$ reverses inclusions, and

$$
L_0 = \mathbb{B}, \qquad L_{\mathbb{C}^2} = 0, \qquad L_W \text{ minimal} \iff \dim_{\mathbb{C}}W = 1 .
$$

Conversely every left ideal is of this form: a left ideal is a submodule of the left regular module $\mathbb{B}\cong S\oplus S$, and since $S$ is simple and $\mathbb{B}$ has length 2, the only submodules of $S\oplus S$ are $0$, a copy of $S$, and the whole module. A minimal left ideal $L$ is determined by the line $W = \bigcap_{M\in L}\ker M$.

**Theorem (over $\mathbb{C}$).** The left ideals of $\mathbb{B}$ are exactly $0$, $\mathbb{B}$, and the minimal left ideals $L_W$ with $W$ a line in $\mathbb{C}^2$. The minimal left ideals are indexed by the projective line

$$
\mathbb{P}^1(\mathbb{C}) = \{W\subseteq\mathbb{C}^2 : W \text{ a one-dimensional } \mathbb{C}\text{-subspace}\},
$$

and they form the middle layer of the lattice:

$$
0 \subset \{L_W : W\in\mathbb{P}^1(\mathbb{C})\} \subset \mathbb{B}.
$$

The middle elements are pairwise incomparable; each covers $0$ and is covered by $\mathbb{B}$. Because the length of $\mathbb{B}$ as a left module over itself is 2, every minimal left ideal is also **maximal**: nothing lies strictly between it and $\mathbb{B}$. Right ideals admit the same description, with lines in the dual space and the rows as coordinate members.

The parameter space deserves a caution. The projective space classifying the minimal one-sided ideals of $M_n(D)$ is $\mathbb{P}^{n-1}(D)$, over the **division ring** $D$ in the Wedderburn–Artin decomposition — not over an arbitrary base field. Here $D = \mathbb{C}$ and $n = 2$, so the parameter space is $\mathbb{P}^1(\mathbb{C})$. In particular, regarding $\mathbb{B}$ as an $\mathbb{R}$-algebra does not replace this by $\mathbb{P}^1(\mathbb{R})$: the one-sided ideals are still parametrised by $\mathbb{P}^1(\mathbb{C})$. The real projective line appears only as the subfamily of kernels the real structure preserves, not as a set of fixed minimal left ideals; Section 11 shows that no minimal left ideal is stable under coefficient conjugation.

**Physical reading: the two spheres.** The projective line $\mathbb{P}^1(\mathbb{C})$ is a two-sphere, and so is the family of pure states: the Hermitian idempotents are parametrised by the unit directions $\hat{\boldsymbol\mu}\in S^2$ through $P_+(\hat{\boldsymbol\mu}) = \tfrac12(e_0+i\hat{\boldsymbol\mu})$, as *Biquaternion Idempotents and Projections* records. The two parametrisations match: the assignment

$$
\hat{\boldsymbol\mu} \longmapsto \mathbb{B}\,P_+(\hat{\boldsymbol\mu})
$$

sends a state direction to its one-particle module, and it is **injective** — distinct directions give distinct minimal left ideals, verified on random directions — so the sphere of state directions embeds in the projective line; both are compact connected surfaces, so the embedding is a bijection. The state space and the lattice of one-particle modules are therefore the same two-sphere seen twice, once as projectors and once as modules. This is the algebraic reason the Bloch sphere appears both in the state language and in the ideal language of the framework.

## 10. The Radical

The **Jacobson radical** $J(A)$ is the intersection of all maximal left ideals, equivalently of all maximal right ideals; it is a two-sided ideal. For an artinian ring, $J(A)$ is the largest nilpotent ideal and $A/J(A)$ is semisimple; an artinian ring is semisimple if and only if its radical is zero.

Over $\mathbb{C}$, the radical of $\mathbb{B}$ vanishes: $J(\mathbb{B}) = 0$, since it is a two-sided ideal, hence $0$ or $\mathbb{B}$ by simplicity, and it cannot be $\mathbb{B}$ in a unital algebra. Consequences:

- $\mathbb{B}$ has no nonzero nilpotent two-sided ideals: the nilradical is zero;
- it has no nonzero nilpotent left or right ideals either, since such an ideal generates a nonzero nilpotent two-sided ideal;
- the absence of a radical is not the absence of nilpotent **elements**: $x^2 = y^2 = 0$, yet the left ideal generated by $x$ is not nilpotent;
- every left $\mathbb{B}$-module is semisimple, i.e. a direct sum of copies of $S = \mathbb{C}^2$.

**Physical reading.** Complete reducibility is what lets the framework build its many-particle spaces by taking direct sums and tensor powers of the defining module without any obstruction from the algebra: a module over $\mathbb{B}$ never has a non-split extension, so Fock space and the multi-qubit algebras are assembled from copies of $S$ and nothing else. The nilpotent elements are not an obstruction either: they are not in any nilpotent ideal, which is why an off-diagonal transition element can appear in a well-defined expression without generating a degenerate subspace.

## 11. The Real Structure

Everything so far was stated over $\mathbb{C}$. Regarding the same set $\mathbb{B}$ as an eight-dimensional algebra over $\mathbb{R}$, what changes is the following.

**(a) The ideal lattice does not change.** By the base-field remark of Section 1, an additive subgroup closed under left multiplication is automatically a complex subspace, because multiplication by $i$ is left multiplication by the central element $ie_0$. So an $\mathbb{R}$-left ideal is the same thing as a $\mathbb{C}$-left ideal, and likewise on the right and two-sidedly. Over $\mathbb{R}$: $\mathbb{B}$ is still simple with two-sided ideals $0$ and $\mathbb{B}$; the minimal left ideals are the same subsets, parametrised by $\mathbb{P}^1(\mathbb{C})$; the radical is still zero; the length is still 2.

**(b) The algebra is not central over $\mathbb{R}$.** The centre of $\mathbb{B}$ is the copy of $\mathbb{C}$ spanned by $e_0$ and $ie_0$ — the complex subspace $\mathbb{C}_{\mathbb{B}}$ — a proper field extension of $\mathbb{R}$ of degree 2. So $\mathbb{B}$ is simple over $\mathbb{R}$ but not central simple; in $M_n(D)$ over $\mathbb{R}$ one has $n = 2$ and $D = \mathbb{C}$.

**(c) The enrichment appears after extension of scalars.** The complexification is

$$
\mathbb{B}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C})\cong M_2(\mathbb{C}\oplus\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$

using $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$. The algebra on the right is **not** simple: its two-sided ideals are $0$, the two summands, and the whole ring. So the real biquaternion algebra is **not absolutely simple**: simple over $\mathbb{R}$, but with a complexification that splits as a product of two simple algebras. This is the precise sense in which the real structure carries a richer two-sided ideal theory — not in the lattice of $\mathbb{B}$ itself, which is $\{0,\mathbb{B}\}$ in both views, but in the lattice produced by base change. In contrast, $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{B}$ is simple: it is the real biquaternion algebra, not $\mathbb{H}$, whose complexification splits.

**(d) The action of complex conjugation on the lattice.** Coefficient conjugation $\tilde{Q}\mapsto\tilde{Q}^{*} = \sum_\mu\bar{Q}_\mu e_\mu$ is an $\mathbb{R}$-algebra automorphism (it is $\mathbb{C}$-antilinear), so it permutes the left ideals, $\sigma(\mathbb{B}\tilde{\chi}) = \mathbb{B}\sigma(\tilde{\chi})$. Since $\sigma(p) = q$ and $\sigma(q) = p$, it **interchanges the two columns**:

$$
\sigma(\mathbb{B}p) = \mathbb{B}q, \qquad \sigma(\mathbb{B}q) = \mathbb{B}p .
$$

It does **not** act as entrywise conjugation of the matrix. With $\varphi(\tilde{Q}) = M$ under the isomorphism of Section 5, coefficient conjugation is

$$
\varphi(\tilde{Q}^{*}) = \begin{pmatrix}\bar{d} & -\bar{c}\\ -\bar{b} & \bar{a}\end{pmatrix} = J\,\overline{M}\,J^{-1}, \qquad J = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix} = \varphi(-e_2),
$$

whereas entrywise conjugation fixes $E_{11} = p$ and would leave $\mathbb{B}p$ invariant. The two differ already on $e_1$: $\varphi(e_1) = -i\sigma_1$ is fixed by $\sigma$, but entrywise conjugation would carry it to $+i\sigma_1$.

On a minimal left ideal $L_W$ the action is $\sigma(L_W) = L_{W^{\perp}}$, where $W^{\perp}$ is the Hermitian-orthogonal complement of $W$ in $\mathbb{C}^2$: if $W = \operatorname{span}(w_1,w_2)$ then $W^{\perp} = \operatorname{span}(\bar{w}_2,-\bar{w}_1)$. In the affine coordinate $t = w_2/w_1$ the induced map on $\mathbb{P}^1(\mathbb{C})$ is $t\mapsto-1/\bar{t}$, whose fixed-point equation $t = -1/\bar{t}$ reads $|t|^2 = -1$ and has no solution. So **no minimal left ideal is stable under complex conjugation**: the involution is fixed-point-free and pairs the two columns. This is the algebraic form of the statement, used elsewhere in the series, that coefficient conjugation exchanges the defining module $S$ and its conjugate $\bar{S}$.

The **real lines** $W = \overline{W}$ still form the real projective line $\mathbb{P}^1(\mathbb{R})\subset\mathbb{P}^1(\mathbb{C})$, and $\sigma$ preserves this subfamily — the Hermitian orthogonal of a real line is again real — acting on it as the antipodal map. So although the lattice of left ideals is unchanged from $\mathbb{C}$ to $\mathbb{R}$, the real structure does not mark out conjugation-stable minimal left ideals; what it marks out is the subfamily $\mathbb{P}^1(\mathbb{R})$ of kernels it preserves, on which it acts without fixed points.

**Physical reading: the real structure and the conjugate module.** The pairing of $\mathbb{B}p$ with $\mathbb{B}q$ by $\sigma$ is what the physical articles use when they pass from the regular module $S\oplus S$, whose two columns both carry the defining representation, to the Dirac module $S\oplus\bar{S}$, whose second factor carries the conjugate action; the passage between the two is the real structure, and it is an $\mathbb{R}$-antilinear map, not a change of basis. This is the structure the mass articles use: a mass term that pairs a field with a conjugate defined on the same space is a real-structure term, while a term that couples the two halves of a Dirac field is linear. See *Chiral Fermions in the Biquaternion Framework* for the comparison of the two module pictures, and *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* for the two kinds of mass term. The fixed-point-freeness is the algebraic fact behind the statement that the framework's real structure is an involution without conjugacy-stable one-particle modules.

## Summary

| Statement | Over $\mathbb{C}$ | Over $\mathbb{R}$ |
|---|---|---|
| Dimension | 4 | 8 |
| Algebra type | $M_2(\mathbb{C})$ | $M_2(\mathbb{C})$ |
| Two-sided ideals | $0$, $\mathbb{B}$ (simple) | $0$, $\mathbb{B}$ (simple) |
| Central simple? | yes, centre $\mathbb{C}$ | no, centre $\mathbb{C}\neq\mathbb{R}$ |
| Left ideals | $0$, the $\mathbb{P}^1(\mathbb{C})$ of minimal ones, $\mathbb{B}$ | same lattice |
| Minimal left ideals | columns, all $\cong\mathbb{C}^2$ | same; $\sigma$ pairs $L_W\leftrightarrow L_{W^{\perp}}$, none stable |
| Minimal right ideals | rows, all $\cong(\mathbb{C}^2)^{*}$ | same |
| Jacobson radical | 0 | 0 |
| Length as module over itself | 2 | 2 |
| Base change $\otimes_{\mathbb{R}}\mathbb{C}$ | — | $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, not simple |

Physically: the two-sided triviality of the ideal lattice is the statement that the sector split of the framework is not a decomposition into algebras; the minimal left ideals are the one-particle modules, all isomorphic, so every physical label on them comes from extra structure; the lattice of one-particle modules and the sphere of pure states are the same two-sphere; complete reducibility is why the multi-particle spaces are built freely from copies of the defining module; and the real structure is coefficient conjugation, which pairs the defining module with its conjugate and leaves no minimal left ideal stable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra; $M_2(\mathbb{C})$ over $\mathbb{C}$, real dimension 8 |
| $e_0,e_1,e_2,e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary; $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ is the centre |
| $p,q$ | Orthogonal idempotents, $p+q = e_0$, $pq = 0$; the diagonal matrix units; the state projectors |
| $x,y$ | Nilpotent off-diagonal elements, $x = \tfrac{ie_1-e_2}{2}$, $y = \tfrac{ie_1+e_2}{2}$, $x^2 = y^2 = 0$; the transition elements |
| $E_{ij}$ | Matrix units, $E_{11} = p$, $E_{12} = x$, $E_{21} = y$, $E_{22} = q$ |
| $S = \mathbb{C}^2$ | The defining module; all simple left modules are isomorphic to it |
| $L_W$ | Minimal left ideal defined by a line $W\subset\mathbb{C}^2$ |
| $\mathbb{P}^1(\mathbb{C})$ | The projective line parametrising the minimal left ideals; a two-sphere |
| $P_+(\hat{\boldsymbol\mu}) = \tfrac12(e_0+i\hat{\boldsymbol\mu})$ | Pure state; Hermitian idempotent; $\hat{\boldsymbol\mu}\in S^2$ |
| $\sigma$ | Coefficient conjugation, the real structure; pairs $L_W\leftrightarrow L_{W^{\perp}}$ |
| $J(\mathbb{B})$ | Jacobson radical; it is 0 |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the Peirce decomposition and the structure theory of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001), for simplicity, semisimplicity, the Jacobson radical and matrix rings.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009), for Wedderburn–Artin theory and the radical.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for ring and module theory and central simple algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the biquaternion algebra as $M_2(\mathbb{C})$ and its matrix and spinor models.
