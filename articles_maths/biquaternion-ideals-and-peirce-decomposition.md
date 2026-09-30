# __Biquaternion Ideals and Peirce Decomposition__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, as established in the article on biquaternion algebra. This article studies the ideal structure of $\mathbb{B}$ and the decomposition of $\mathbb{B}$ relative to a family of idempotents.

Two facts organize the discussion. The algebra $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. Its ideal theory is therefore a theory of one-sided ideals: the main results are the classification of the left ideals — $0$, the minimal ones, and $\mathbb{B}$ — and the Peirce decomposition into four one-dimensional corners relative to a pair of orthogonal idempotents.

Because the biquaternions carry both a complex and a real structure, every statement is tagged with the field over which it is made. The sections before the last work over $\mathbb{C}$; §*The Real Structure* discusses the $\mathbb{R}$-view, where the ideal lattice itself is unchanged but the real structure leaves further traces. The notation follows the article on biquaternion algebra: $e_0$ is the unit, $e_1, e_2, e_3$ are the quaternion units with $e_1 e_2 = e_3$, $i$ is the central scalar imaginary, and a general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The definitions of the article on rings apply to the noncommutative algebra $\mathbb{B}$, where "left" and "right" must be distinguished.

## Ideals in an Algebra

Let $A$ be an associative unital algebra over a field $k$. An additive subgroup $I \subseteq A$ is a **left ideal** if $A I \subseteq I$, a **right ideal** if $I A \subseteq I$, and a **two-sided ideal** if it is both. The distinction matters only when $A$ is noncommutative; for $\mathbb{B}$ the three notions genuinely differ. The ideals $0$ and $A$ are called trivial.

A base-field remark will be used repeatedly. If $A I \subseteq I$, then $I$ is automatically a $k$-subspace, since $\lambda \tilde R = (\lambda 1) \tilde R \in I$ for $\lambda \in k$, $\tilde R \in I$, as $\lambda 1 \in A$. So the left ideals of a unital algebra do not depend on which field of scalars inside the center is used to view it; in particular the ideal lattice of $\mathbb{B}$ is the same in the $\mathbb{C}$-view and the $\mathbb{R}$-view (§*The Real Structure*).

For a two-sided ideal $I$, the **quotient algebra** $A/I$ is the set of cosets with the induced operations, well defined precisely because $I$ absorbs multiplication on both sides. Kernels of algebra homomorphisms are two-sided ideals, and the first isomorphism theorem gives $A/\ker\varphi \cong \operatorname{im}\varphi$. For a left ideal only, $A/I$ is still a left $A$-module but not in general an algebra. Thus the left ideals govern module theory and the two-sided ideals govern quotient algebras.

## The Two-Sided Ideals: Simplicity of $\mathbb{B}$

**Theorem.** Over $\mathbb{C}$, the only two-sided ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$. Equivalently, $\mathbb{B}$ is a **simple** $\mathbb{C}$-algebra.

**Proof.** Let $I \neq 0$ be a two-sided ideal. It is a $\mathbb{C}$-subspace, because multiplication by the central element $i$ is left multiplication by an element of $\mathbb{B}$. Fix $0 \neq \tilde{Q} = \sum_\mu Q_\mu e_\mu \in I$. For every unit $\tilde B \in \mathbb{B}$ the conjugate $\tilde B\tilde{Q}\tilde B^{-1}$ lies in $I$, since $I$ is two-sided.

Average the conjugates over the finite group $\{\pm e_0, \pm e_1, \pm e_2, \pm e_3\}$. Conjugation by $e_\mu$ fixes $e_0$ and $e_\mu$ and reverses $e_\nu$ for $\nu \neq \mu$, so the group elements of quaternion part $\pm e_\mu$ all give the same conjugate, and the average is twice

$$
Q_0 e_0 + \tfrac12\big(Q_0 e_0 + Q_1 e_1 - Q_2 e_2 - Q_3 e_3\big) + \tfrac12\big(Q_0 e_0 - Q_1 e_1 + Q_2 e_2 - Q_3 e_3\big) + \tfrac12\big(Q_0 e_0 - Q_1 e_1 - Q_2 e_2 + Q_3 e_3\big) = 4 Q_0 e_0,
$$

divided by $8$, giving $Q_0 e_0 \in I$. If $Q_0 \neq 0$ then $e_0 = Q_0^{-1}(Q_0 e_0) \in I$ and $I = \mathbb{B}$. If $Q_0 = 0$ then $\tilde{Q}$ is a nonzero element of the vector subspace, and conjugating it by the real unit quaternions rotates it: the conjugates run over a sphere in $\mathrm{Vect}(\mathbb{B})$, whose real span is all of $\mathrm{Vect}(\mathbb{B})$, so $\mathrm{Vect}(\mathbb{B}) \subseteq I$. In particular $e_1 \in I$, hence $e_1^2 = -e_0 \in I$ and again $I = \mathbb{B}$.

Consequences over $\mathbb{C}$:

- The only quotient algebras of $\mathbb{B}$ are $\mathbb{B}$ and $0$.
- Every nonzero element generates $\mathbb{B}$ as a two-sided ideal.
- The center of $\mathbb{B}$ is the scalar copy of $\mathbb{C}$, so $\mathbb{B}$ is a **central simple** $\mathbb{C}$-algebra; in particular it is not a product $A_1 \times A_2$ of nonzero algebras, since each factor would give a nontrivial two-sided ideal.
- The many one-sided ideals of §*Minimal Left and Right Ideals* and §*The Lattice of Left Ideals* are all non-two-sided, so they do not contradict simplicity.

## Artinian, Semisimple, and Length Two

A nonzero module is **simple** if it has no submodules other than $0$ and itself. A **composition series** is a finite strictly increasing chain $0 = M_0 \subset M_1 \subset \cdots \subset M_r = M$ with simple successive quotients $M_i/M_{i-1}$; the number $r$ is the **length** of $M$. A ring is **left artinian** if every descending chain of left ideals stabilizes, and **semisimple** if its left regular module is a direct sum of simple modules.

Over $\mathbb{C}$, every descending chain of left ideals of $\mathbb{B}$ is a descending chain of $\mathbb{C}$-subspaces, so it stabilizes; thus $\mathbb{B}$ is artinian. By Wedderburn–Artin, a unital ring is semisimple if and only if it is artinian with zero Jacobson radical, and every simple artinian ring is semisimple. Hence $\mathbb{B}$ is **semisimple**, and every left ideal is a direct sum of minimal left ideals.

All simple left $\mathbb{B}$-modules are isomorphic, since a simple artinian ring has a unique simple module up to isomorphism. With the idempotents $\tilde\Pi_1, \tilde\Pi_2$ of §*Idempotents and Orthogonal Idempotents*, the algebra as a left module over itself reads $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$, with $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ both minimal left ideals. Hence $0 \subset \mathbb{B}\tilde\Pi_1 \subset \mathbb{B}$ is a composition series, and the **length of $\mathbb{B}$ as a left module over itself is $2$**, with both factors isomorphic. The right regular module has length $2$ as well. All of this is over $\mathbb{C}$.

## Idempotents and Orthogonal Idempotents

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$, and two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents, and for a semisimple algebra

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

Over $\mathbb{C}$, the idempotents

$$
\tilde\Pi_1 = \frac{e_0 + i e_3}{2}, \qquad \tilde\Pi_2 = \frac{e_0 - i e_3}{2}
$$

satisfy $\tilde\Pi_1^2 = \tilde\Pi_1$, $\tilde\Pi_2^2 = \tilde\Pi_2$, $\tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = 0$ and $\tilde\Pi_1 + \tilde\Pi_2 = e_0$. They are primitive, and they generate the off-diagonal elements of the next section.

The classification of the idempotents of $\mathbb{B}$ — the trivial idempotents, the bijection with the roots of $-1$, the Hermitian projections and the dimension of the idempotent set — is the subject of *Biquaternion Idempotents and Projections*.

## The Off-Diagonal Elements

The two off-diagonal corners are spanned by the elements

$$
\tilde R = \frac{i e_1 - e_2}{2}, \qquad \tilde T = \frac{i e_1 + e_2}{2}.
$$

Then $\{\tilde\Pi_1, \tilde R, \tilde T, \tilde\Pi_2\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$, and the multiplication is

$$
\tilde\Pi_1\tilde R = \tilde R = \tilde R\tilde\Pi_2, \qquad \tilde\Pi_2\tilde T = \tilde T = \tilde T\tilde\Pi_1, \qquad \tilde R\tilde T = \tilde\Pi_1, \qquad \tilde T\tilde R = \tilde\Pi_2,
$$

together with $\tilde R\tilde\Pi_1 = \tilde\Pi_2\tilde R = \tilde\Pi_1\tilde T = 0$, $\tilde T\tilde\Pi_2 = 0$, and $\tilde R^2 = \tilde T^2 = 0$.

## The Peirce Decomposition

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

**The biquaternion case.** Take $e_1 = \tilde\Pi_1$, $e_2 = \tilde\Pi_2$ from §*Idempotents and Orthogonal Idempotents*. The Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B} = \tilde\Pi_1\mathbb{B}\tilde\Pi_1 \oplus \tilde\Pi_1\mathbb{B}\tilde\Pi_2 \oplus \tilde\Pi_2\mathbb{B}\tilde\Pi_1 \oplus \tilde\Pi_2\mathbb{B}\tilde\Pi_2,
$$

and by the multiplication table of §*The Off-Diagonal Elements* each summand is one-dimensional over $\mathbb{C}$:

$$
\tilde\Pi_1\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde\Pi_1, \qquad \tilde\Pi_1\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde R, \qquad \tilde\Pi_2\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde T, \qquad \tilde\Pi_2\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde\Pi_2.
$$

So the Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B} = \mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde R \oplus \mathbb{C}\tilde T \oplus \mathbb{C}\tilde\Pi_2.
$$

The diagonal part $\tilde\Pi_1\mathbb{B}\tilde\Pi_1 \oplus \tilde\Pi_2\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde\Pi_2$ is a two-dimensional commutative subalgebra isomorphic to $\mathbb{C} \times \mathbb{C}$. Each diagonal corner is a division ring, namely $\mathbb{C}$, which is the primitivity criterion of §*Idempotents and Orthogonal Idempotents*.

A **null (light-cone) variant** of the same split is used in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. The idempotents there are the uniform nullquaternions $N = \tfrac12(1, \mathbf n)$ and $\bar N = \tfrac12(1, -\mathbf n)$, and the two Peirce components of a biquaternion are its **signed parts**, whose sign the source reads as the chirality of the Weyl spinor. The pair is orthogonal and complete in the article's own product — the **outer** product, for which $N \odot N = N$, $\bar N \odot \bar N = \bar N$, $N \odot \bar N = 0$ and $N + \bar N = e_0$ — and the article's matrix isomorphism carries the outer product to the ordinary matrix product and $N, \bar N$ to the two standard diagonal idempotents. It is the same orthogonal pair as above, transported to the light-cone coordinates with the product changed; these same elements are **not** idempotent under the Hamilton product of this article, so the chiral split is naturally stated in that paper's algebra rather than in this one.

## The Decomposition into Minimal Left and Right Ideals

The two idempotents group the basis into one-sided ideals in a second way. The two **left ideals** $\mathbb{B}\tilde\Pi_1, \mathbb{B}\tilde\Pi_2$ and the two **right ideals** $\tilde\Pi_1\mathbb{B}, \tilde\Pi_2\mathbb{B}$ are one-sided, and

$$
\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2 = (\mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde T) \oplus (\mathbb{C}\tilde R \oplus \mathbb{C}\tilde\Pi_2),
$$

$$
\mathbb{B} = \tilde\Pi_1\mathbb{B} \oplus \tilde\Pi_2\mathbb{B} = (\mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde R) \oplus (\mathbb{C}\tilde T \oplus \mathbb{C}\tilde\Pi_2).
$$

The first exhibits $\mathbb{B}$ as a direct sum of the two minimal left ideals; the second exhibits it as a direct sum of the two minimal right ideals. The two groupings of the same four basis elements differ: the Peirce decomposition groups $\tilde\Pi_1$ with $\tilde R$ and $\tilde\Pi_2$ with $\tilde T$, whereas the left-ideal decomposition groups $\tilde\Pi_1$ with $\tilde T$ and $\tilde\Pi_2$ with $\tilde R$. Each left ideal is two-dimensional over $\mathbb{C}$; each right ideal is its dual. Since $\mathbb{B}$ is simple, a one-sided ideal is never two-sided; for instance $\mathbb{B}\tilde\Pi_1$ is not stable under right multiplication by $\tilde R$.

**Why the sum is direct, and the dimensions.** Every $\tilde{Q} \in \mathbb{B}$ satisfies $\tilde{Q} = \tilde{Q}(\tilde\Pi_1 + \tilde\Pi_2) = \tilde{Q}\tilde\Pi_1 + \tilde{Q}\tilde\Pi_2$, so the two left ideals span. Their intersection is zero: if $\tilde{Q}\tilde\Pi_1 = \tilde{P}\tilde\Pi_2$, then multiplying on the right by $\tilde\Pi_1$ and using $\tilde\Pi_1^2 = \tilde\Pi_1$ and $\tilde\Pi_2\tilde\Pi_1 = 0$ gives $\tilde{Q}\tilde\Pi_1 = 0$. The basis above reads $\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde T$, of dimension $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$, with $\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde R \oplus \mathbb{C}\tilde\Pi_2$ for the second; together they account for $4 + 4 = 8 = \dim_{\mathbb{R}} \mathbb{B}$. Each is a minimal left ideal, by the primitivity of $\tilde\Pi_1$ and $\tilde\Pi_2$ (§*Idempotents and Orthogonal Idempotents*, §*Minimal Left and Right Ideals*).

**The module structure.** With the basis $\{\tilde\Pi_1, \tilde T\}$ the left $\mathbb{B}$-module $\mathbb{B}\tilde\Pi_1$ is $\mathbb{C}^2$, and the central element $i$ acts on it as the scalar $i$:
$$
i\,(\alpha \tilde\Pi_1 + \beta \tilde T) = (i\alpha)\tilde\Pi_1 + (i\beta)\tilde T .
$$
So the simple module underlying each minimal left ideal is the standard two-dimensional one, with $i$ acting by the identity matrix.

## Minimal Left and Right Ideals

A **minimal left ideal** is a nonzero left ideal containing no nonzero proper left ideal; equivalently, a simple submodule of the left regular module. A **minimal right ideal** is defined the same way on the right.

Over $\mathbb{C}$, since $\mathbb{B}$ is semisimple, every left ideal of $\mathbb{B}$ is a direct sum of minimal left ideals, and every minimal left ideal is of the form $\mathbb{B}e$ for a primitive idempotent $e$. The examples are the left ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ of §*The Decomposition into Minimal Left and Right Ideals*, and all minimal left ideals are isomorphic as left $\mathbb{B}$-modules: a general one is obtained from $\mathbb{B}\tilde\Pi_1$ by an algebra automorphism, so it has the same shape in a suitable basis. Dually, every minimal right ideal is isomorphic to $\tilde\Pi_1\mathbb{B}$. Thus there is one isomorphism class of simple left modules and one of simple right modules. Being nonzero proper one-sided ideals, none of them is two-sided — which is exactly why their abundance is compatible with §*The Two-Sided Ideals: Simplicity of $\mathbb{B}$*.

## The Lattice of Left Ideals

Over $\mathbb{C}$, every left ideal of the simple artinian algebra $\mathbb{B}$ is a direct sum of minimal left ideals, so the left ideals are exactly $0$, the minimal ones, and $\mathbb{B}$. The minimal left ideals form the middle layer of the lattice,

$$
0 \;\subset\; \{\, L : L \text{ a minimal left ideal} \,\} \;\subset\; \mathbb{B},
$$

the elements of the middle layer being pairwise incomparable, each covering $0$ and covered by $\mathbb{B}$. Because the length of $\mathbb{B}$ as a left module over itself is $2$, every minimal left ideal is also a **maximal** left ideal, nothing lying strictly between it and $\mathbb{B}$. The minimal left ideals are parametrized by the projective line $\mathbb{P}^1(\mathbb{C})$. Right ideals admit the same description, with the dual parametrization.

The parameter space deserves a caution. In the Wedderburn–Artin decomposition $M_n(D)$ of a simple artinian algebra, the minimal one-sided ideals are parametrized by the projective space $\mathbb{P}^{n-1}(D)$ over the **division ring** $D$, not over an arbitrary base field. Here $D = \mathbb{C}$ and $n = 2$, so the parameter space is $\mathbb{P}^1(\mathbb{C})$. In particular, regarding $\mathbb{B}$ as an $\mathbb{R}$-algebra does not replace this by $\mathbb{P}^1(\mathbb{R})$: the one-sided ideals are still parametrized by $\mathbb{P}^1(\mathbb{C})$. The real projective line appears only as the subfamily that the real structure preserves, not as a set of fixed minimal left ideals: §*The Real Structure* shows that no minimal left ideal is stable under coefficient conjugation.

## The Radical

The **Jacobson radical** $J(A)$ is the intersection of all maximal left ideals of $A$, equivalently of all maximal right ideals; it is a two-sided ideal. For an artinian ring, $J(A)$ is the largest nilpotent ideal and $A/J(A)$ is semisimple; an artinian ring is semisimple if and only if its radical is zero.

Over $\mathbb{C}$, the radical of $\mathbb{B}$ vanishes:

$$
J(\mathbb{B}) = 0.
$$

Indeed $J(\mathbb{B})$ is a two-sided ideal, hence by simplicity is $0$ or $\mathbb{B}$; it cannot be $\mathbb{B}$, since in a unital algebra the radical is proper. This restates the semisimplicity of §*Artinian, Semisimple, and Length Two* in terms of the radical. Consequences over $\mathbb{C}$:

- $\mathbb{B}$ has no nonzero **nilpotent two-sided ideals**; the nilradical is zero.
- It has no nonzero nilpotent left or right ideals either, since such an ideal generates a nonzero nilpotent two-sided ideal.
- The absence of a radical is not the absence of nilpotent **elements**: $\tilde R^2 = \tilde T^2 = 0$ (§*The Off-Diagonal Elements*), yet the left ideal generated by $\tilde R$ is not nilpotent.
- Every left $\mathbb{B}$-module is semisimple.

## The Real Structure

Everything so far was stated over $\mathbb{C}$. We now regard the same set $\mathbb{B}$ as an eight-dimensional algebra over $\mathbb{R}$ and record what changes.

**(a) The ideal lattice does not change.** By the base-field remark of §*Ideals in an Algebra*, an additive subgroup closed under left multiplication by $\mathbb{B}$ is automatically a complex subspace, because multiplication by $i$ is left multiplication by the central element $i e_0$. So an $\mathbb{R}$-left ideal is the same thing as a $\mathbb{C}$-left ideal, and the same holds on the right and for two-sided ideals. In particular, over $\mathbb{R}$: $\mathbb{B}$ is still simple, with two-sided ideals only $0$ and $\mathbb{B}$; the minimal left ideals are the same subsets, parametrized by $\mathbb{P}^1(\mathbb{C})$; the radical is still zero; and the length as a module over itself is still $2$.

**(b) The algebra is not central over $\mathbb{R}$.** The center of $\mathbb{B}$ is the copy of $\mathbb{C}$ spanned by $e_0$ and $i e_0$ — the **complex subspace** $\mathbb{C}_{\mathbb{B}}$ — a proper field extension of $\mathbb{R}$ of degree $2$. Thus $\mathbb{B}$ is a simple $\mathbb{R}$-algebra but not a **central simple** one. In the Wedderburn–Artin description $\mathbb{B} \cong M_n(D)$ over $\mathbb{R}$, one has $n = 2$ and $D = \mathbb{C}$.

**(c) The enrichment appears after extension of scalars.** The complexification of the real algebra $\mathbb{B}$ is

$$
\mathbb{B} \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}) \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong (\mathbb{C} \oplus \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong \mathbb{B} \oplus \mathbb{B},
$$

using $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$ and the associativity and commutativity of $\otimes_{\mathbb{R}}$. The algebra on the right is **not simple**: its two-sided ideals are $0$, the two summands, and the whole ring. So the real biquaternion algebra is **not absolutely simple**: simple over $\mathbb{R}$, but with a complexification that splits as a product of two simple algebras. This is the precise sense in which the real structure carries a richer two-sided ideal theory — not in the lattice of $\mathbb{B}$ itself, which is $\{0, \mathbb{B}\}$ in both views, but in the lattice produced by base change. In contrast, $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{B}$ is simple: it is the real biquaternion algebra, not $\mathbb{H}$, whose complexification splits.

**(d) The action of complex conjugation on the lattice.** Complex conjugation $\tilde{Q} \mapsto \tilde{Q}^{*} = \sum_\mu \bar{Q}_\mu e_\mu$ is an $\mathbb{R}$-algebra automorphism of $\mathbb{B}$ (it is $\mathbb{C}$-antilinear), so it permutes the left ideals, $\sigma(\mathbb{B}\tilde{\chi}) = \mathbb{B}\sigma(\tilde{\chi})$. Since $\sigma(\tilde\Pi_1) = \tilde\Pi_2$ and $\sigma(\tilde\Pi_2) = \tilde\Pi_1$, it **interchanges the two standard left ideals**:

$$
\sigma(\mathbb{B}\tilde\Pi_1) = \mathbb{B}\tilde\Pi_2, \qquad \sigma(\mathbb{B}\tilde\Pi_2) = \mathbb{B}\tilde\Pi_1.
$$

On the parametrizing projective line the induced map $t \mapsto -1/\bar{t}$ has no fixed point, so **no minimal left ideal is stable under complex conjugation**. The **real lines** still form the real projective line $\mathbb{P}^1(\mathbb{R}) \subset \mathbb{P}^1(\mathbb{C})$, which $\sigma$ preserves and acts on as the antipodal map. So although the lattice of left ideals is unchanged from $\mathbb{C}$ to $\mathbb{R}$, the real structure does not mark out conjugation-stable minimal left ideals; what it marks out is the subfamily $\mathbb{P}^1(\mathbb{R})$ that it preserves.

## Summary

| Statement | Over $\mathbb{C}$ | Over $\mathbb{R}$ |
|---|---|---|
| Dimension | $4$ | $8$ |
| Algebra type | simple $\mathbb{C}$-algebra, $\dim 4$ | simple $\mathbb{R}$-algebra, $\dim 8$ |
| Two-sided ideals | $0$, $\mathbb{B}$ (simple) | $0$, $\mathbb{B}$ (simple) |
| Central simple? | yes, center $\mathbb{C}$ | no, center $\mathbb{C} \neq \mathbb{R}$ |
| Left ideals | $0$, the $\mathbb{P}^1(\mathbb{C})$ of minimal ones, $\mathbb{B}$ | same lattice |
| Minimal left ideals | all isomorphic | same; $\sigma$ pairs them, none stable |
| Minimal right ideals | all isomorphic | same |
| Jacobson radical | $0$ | $0$ |
| Length as module over itself | $2$ | $2$ |
| Base change $\otimes_{\mathbb{R}}\mathbb{C}$ | — | not simple; splits into two simple factors |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; dimension $4$ over $\mathbb{C}$, $8$ over $\mathbb{R}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary; $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center |
| $\tilde\Pi_1, \tilde\Pi_2$ | Orthogonal idempotents, $\tilde\Pi_1+\tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = 0$ |
| $\tilde R, \tilde T$ | Nilpotent off-diagonal elements, $\tilde R = \tfrac{i e_1 - e_2}{2}$, $\tilde T = \tfrac{i e_1 + e_2}{2}$, $\tilde R^2 = \tilde T^2 = 0$ |
| $\mathbb{B}\tilde\Pi_1 \cong \mathbb{C}^2$ | The minimal left ideal, a simple left $\mathbb{B}$-module, $i$ acting as the scalar $i$ |
| $\mathbb{P}^1(\mathbb{C})$ | The projective line parameterising the minimal left ideals |
| $\sigma$ | The real structure, pairing the two standard minimal left ideals |
| $\mathcal{J}$ | Jacobson radical; it is $0$ for $\mathbb{B}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982). The standard reference for the Peirce decomposition and the structure theory of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001). Simplicity, semisimplicity, the Jacobson radical, and matrix rings.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009). Wedderburn–Artin theory and the radical.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002). Ring and module theory, central simple algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001). The algebraic structure of the biquaternion algebra.
