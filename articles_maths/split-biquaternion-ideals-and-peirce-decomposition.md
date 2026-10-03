
# __Split-Biquaternion Ideals and Peirce Decomposition__

## Introduction

The algebra article defined the split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ and established the isomorphism $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$. This article treats the **ideals** of $\mathbb{H}_{\mathbb{D}}$, the decomposition of the algebra into its two quaternion halves, and the **Peirce decomposition** attached to the idempotents.

The treatment is purely mathematical. Every claim is either proved or stated as a definition. No physics is invoked. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ is assumed from the basic algebra article, its four conjugations and its idempotents $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$, $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$ are assumed from the article on split complex algebra and the basic algebra article, and the quaternion algebra $\mathbb{H}$ is assumed to be a division algebra.

Throughout, a split biquaternion is written $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu = q_\mu + j q'_\mu$, and the idempotent components are $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_\pm \in \mathbb{H}$. The four conjugations are $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger} = {}^{*}\circ\bar{\cdot}$ and ${}^{\flat} = -{}^{\dagger}$.

The classification and the structure of the *idempotents* themselves — their orthogonality, completeness and primitivity, their role as projections, and the four-point nature of the idempotent set — belong to *Split-Biquaternion Idempotents and Projections*. This article takes those facts as given and develops the objects that the idempotents generate: the ideals and the Peirce decomposition. The two articles share the idempotents $\tilde\Pi_\pm$ but not their ownership: the idempotents article owns the idempotents, this article owns the ideals and the splitting.

## Ideals in an Algebra

Let $A$ be an associative algebra. A **left ideal** is a subset $I \subseteq A$ closed under addition and under left multiplication by $A$: $AI \subseteq I$. A **right ideal** is closed under right multiplication, $IA \subseteq I$, and a **two-sided ideal** is both. An ideal is **proper** if it is neither $0$ nor $A$, and **minimal** (among nonzero left ideals) if it contains no nonzero proper left ideal. The algebra is **simple** if it has no proper nonzero two-sided ideal, and **semisimple** if it is a direct sum of simple algebras, equivalently if its Jacobson radical is zero.

The basic mechanism connecting ideals to idempotents is that an idempotent $e$ produces the decompositions

$$
A = Ae \oplus A(1 - e) \quad (\text{left}), \qquad A = eA \oplus (1 - e)A \quad (\text{right}),
$$

and that $Ae$ is a minimal left ideal exactly when $e$ is primitive.

## The Two-Sided Ideals: Simplicity Fails

**Theorem.** The proper nonzero two-sided ideals of $\mathbb{H}_{\mathbb{D}}$ are exactly $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$. Consequently $\mathbb{H}_{\mathbb{D}}$ is not simple.

**Proof.** Let $I$ be a two-sided ideal. In the idempotent basis $I = I_+ \tilde\Pi_+ \oplus I_- \tilde\Pi_-$ with $I_\pm \subseteq \mathbb{H}$. Because $\tilde\Pi_\pm$ is central, $I$ being an ideal is equivalent to each $I_\pm$ being an ideal of the quaternion algebra $\mathbb{H}$. But $\mathbb{H}$ is a division algebra and has no proper nonzero ideal: if $\tilde q \neq 0$ lies in an ideal $J$ of $\mathbb{H}$, then $1 = \tilde q^{-1} \tilde q \in J$, so $J = \mathbb{H}$. Hence for each sign either $I_\pm = 0$ or $I_\pm = \mathbb{H}$. The proper nonzero possibilities are therefore $I = \mathbb{H} \tilde\Pi_+$ and $I = \mathbb{H} \tilde\Pi_-$. Since these are proper and nonzero, $\mathbb{H}_{\mathbb{D}}$ is not simple.

**Corollary.** $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-$ is the unique decomposition of $\mathbb{H}_{\mathbb{D}}$ as a direct sum of two proper nonzero two-sided ideals, and the two summands are isomorphic to $\mathbb{H}$.

**Proof.** The decomposition follows from $\tilde\Pi_+ + \tilde\Pi_- = 1$; uniqueness from the theorem, since any decomposition into two nonzero two-sided ideals must consist of the two listed ideals. Each summand $\mathbb{H} \tilde\Pi_\pm$ is identified with $\mathbb{H}$ by the projection $\tilde{Q} \mapsto \tilde{Q}_\pm$.

## The Algebra Is Semisimple

**Proposition.** The Jacobson radical of $\mathbb{H}_{\mathbb{D}}$ is zero, so $\mathbb{H}_{\mathbb{D}}$ is semisimple.

**Proof.** By the theorem, the only proper nonzero two-sided ideals are $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$; their intersection is $\mathbb{H} \tilde\Pi_+ \cap \mathbb{H} \tilde\Pi_- = 0$, so the radical, being the intersection of the maximal two-sided ideals, is zero.

The algebra is thus semisimple but not simple, and its two simple components are both the same division algebra $\mathbb{H}$. This is the algebraic content of the isomorphism $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$: the right-hand side is a product of two division algebras.

## The Idempotents Revisited

The four idempotents of $\mathbb{H}_{\mathbb{D}}$ are $0$, $\tilde\Pi_+$, $\tilde\Pi_-$ and $1$, and all of them are central; this is proved in *Split-Biquaternion Idempotents and Projections*. Here only the following facts are used: $\{\tilde\Pi_+, \tilde\Pi_-\}$ is a **complete** family of **orthogonal**, **primitive**, **central** idempotents, with

$$
\tilde\Pi_+^2 = \tilde\Pi_+, \qquad \tilde\Pi_-^2 = \tilde\Pi_-, \qquad \tilde\Pi_+ \tilde\Pi_- = \tilde\Pi_- \tilde\Pi_+ = 0, \qquad \tilde\Pi_+ + \tilde\Pi_- = 1.
$$

Because they are central, the left, right and two-sided ideals they generate coincide, and the primitivity criterion gives that each of $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ is a minimal ideal.

## The Peirce Decomposition

Let $e$ be an idempotent of an algebra $A$. Relative to $e$ and its complement $1 - e$, the algebra decomposes as a direct sum of four **Peirce spaces**:

$$
A = eAe \oplus eA(1 - e) \oplus (1 - e)Ae \oplus (1 - e)A(1 - e).
$$

**Theorem.** For $e = \tilde\Pi_+$ in $\mathbb{H}_{\mathbb{D}}$ the Peirce decomposition is

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus 0 \oplus 0 \oplus \mathbb{H} \tilde\Pi_-,
$$

the two **off-diagonal** Peirce spaces $\tilde\Pi_+ \mathbb{H}_{\mathbb{D}} \tilde\Pi_-$ and $\tilde\Pi_- \mathbb{H}_{\mathbb{D}} \tilde\Pi_+$ both vanishing.

**Proof.** Since $\tilde\Pi_+$ is central,

$$
\tilde\Pi_+ \mathbb{H}_{\mathbb{D}} \tilde\Pi_+ = \mathbb{H}_{\mathbb{D}} \tilde\Pi_+ = \mathbb{H} \tilde\Pi_+, \qquad \tilde\Pi_+ \mathbb{H}_{\mathbb{D}} \tilde\Pi_- = \mathbb{H}_{\mathbb{D}} \tilde\Pi_+ \tilde\Pi_- = 0,
$$

and similarly $(1 - \tilde\Pi_+) \mathbb{H}_{\mathbb{D}} (1 - \tilde\Pi_+) = \mathbb{H} \tilde\Pi_-$ and the other off-diagonal space vanishes. The direct sum is the whole algebra because $\tilde\Pi_+ + \tilde\Pi_- = 1$.

The vanishing of the off-diagonal Peirce spaces is the algebraic statement that the two halves of $\mathbb{H}_{\mathbb{D}}$ do not mix: no element of one half acts on the other. This is the sharpest contrast with the biquaternion algebra, where the Peirce spaces relative to a noncentral primitive idempotent have nonzero off-diagonal parts and carry off-diagonal elements $E_{12}$, $E_{21}$.

## The Decomposition into Minimal Ideals

The Peirce decomposition can be read as the sum of the two minimal ideals. For the complete family $\{\tilde\Pi_+, \tilde\Pi_-\}$,

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-,
$$

and each summand is a **minimal** two-sided ideal, equivalently a minimal left ideal and a minimal right ideal, isomorphic to $\mathbb{H}$. Summing over the family, the algebra is the direct sum of its minimal ideals, one for each idempotent of the complete family:

**Proposition.** $\mathbb{H}_{\mathbb{D}}$ is the direct sum of its two minimal ideals $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$, and every minimal left ideal of $\mathbb{H}_{\mathbb{D}}$ is one of these two.

**Proof.** The direct-sum statement is the corollary above. For the second statement, let $L$ be a minimal left ideal. If $L$ contains an element with a nonzero $\tilde\Pi_+$-component, then that component lies in $L \cap \mathbb{H} \tilde\Pi_+$, a nonzero left ideal contained in the minimal ideal $\mathbb{H} \tilde\Pi_+$, hence equal to it; otherwise $L \subseteq \mathbb{H} \tilde\Pi_-$. Minimality then forces $L$ to equal $\mathbb{H} \tilde\Pi_+$ or $\mathbb{H} \tilde\Pi_-$.

## Minimal Left and Right Ideals

Because the idempotents are central, the left ideal, the right ideal and the two-sided ideal generated by an idempotent coincide. Hence the minimal left ideals, the minimal right ideals and the minimal two-sided ideals of $\mathbb{H}_{\mathbb{D}}$ are the **same two objects**, $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$, each isomorphic to the division algebra $\mathbb{H}$.

$$
\mathbb{H}_{\mathbb{D}} \tilde\Pi_+ = \tilde\Pi_+ \mathbb{H}_{\mathbb{D}} = \tilde\Pi_+ \mathbb{H}_{\mathbb{D}} \tilde\Pi_+ = \mathbb{H} \tilde\Pi_+ \cong \mathbb{H},
$$

and likewise for $\tilde\Pi_-$. Each summand is annihilated by the complementary idempotent — $\mathbb{H} \tilde\Pi_+$ by $\tilde\Pi_-$ and $\mathbb{H} \tilde\Pi_-$ by $\tilde\Pi_+$ — so the two ideals are disjoint, and together they fill the algebra: $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_- \cong \mathbb{H} \oplus \mathbb{H}$, both summands isomorphic to the division algebra $\mathbb{H}$ as rings.

In the biquaternion algebra the corresponding statement is different in every respect: the minimal left ideals $\mathbb{B}p$ and $\mathbb{B}q$ are not two-sided, are not right ideals, and are isomorphic to $\mathbb{C}^2$ rather than to a division algebra.

## The Lattice of Left Ideals

**Proposition.** The left ideals of $\mathbb{H}_{\mathbb{D}}$ are exactly

$$
0, \qquad \mathbb{H} \tilde\Pi_+, \qquad \mathbb{H} \tilde\Pi_-, \qquad \mathbb{H}_{\mathbb{D}}.
$$

They form a lattice that is the diamond: $0$ is contained in $\mathbb{H} \tilde\Pi_\pm$, each of these is contained in $\mathbb{H}_{\mathbb{D}}$, and $\mathbb{H} \tilde\Pi_+$, $\mathbb{H} \tilde\Pi_-$ are incomparable. The same description holds for the right ideals and for the two-sided ideals.

**Proof.** A left ideal $L$ is contained in $\mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-$. Its intersections $L \cap \mathbb{H} \tilde\Pi_+$ and $L \cap \mathbb{H} \tilde\Pi_-$ are each either $0$ or the whole summand, since each summand is minimal. The four combinations give the four listed ideals, and no second idempotent pair occurs, so there are no further left ideals.

**Corollary.** Every left ideal of $\mathbb{H}_{\mathbb{D}}$ is two-sided, and $\mathbb{H}_{\mathbb{D}}$ has exactly two maximal left ideals, $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$.

The contrast with $\mathbb{B}$ is extreme. In $\mathbb{B} \cong M_2(\mathbb{C})$ the left ideals form a lattice isomorphic to the projective line $\mathbb{P}^1$, with infinitely many maximal left ideals; in $\mathbb{H}_{\mathbb{D}}$ the lattice has four elements and the two maximal left ideals are the two halves. The reduction is a direct consequence of the vanishing of the off-diagonal Peirce spaces.

## The Radical

The **Jacobson radical** $J(A)$ of a finite-dimensional algebra $A$ is the intersection of its maximal left ideals, equivalently of its maximal right ideals, equivalently the largest nilpotent two-sided ideal; in particular $J(A) = 0$ if and only if $A$ is semisimple.

**Proposition.** $J(\mathbb{H}_{\mathbb{D}}) = 0$. Moreover $J(\mathbb{H}_{\mathbb{D}}) = \mathbb{H} \tilde\Pi_+ \cap \mathbb{H} \tilde\Pi_-$.

**Proof.** The maximal left ideals are $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ by the corollary above, and their intersection is $0$ because $\tilde\Pi_+ \tilde\Pi_- = 0$ and the two ideals are complementary summands.

So $\mathbb{H}_{\mathbb{D}}$ is semisimple in the strongest sense: its radical vanishes. This is one of the senses in which $\mathbb{H}_{\mathbb{D}}$ is *smaller* and better behaved than a general associative algebra — it is a product of two division algebras, and products of division algebras have vanishing radical and only finitely many ideals.

## The Real Structure

The algebra $\mathbb{H}_{\mathbb{D}}$ is an eight-dimensional real algebra and a four-dimensional algebra over $\mathbb{D}$. The ideals $\mathbb{H} \tilde\Pi_\pm$ are real vector subspaces of dimension $4$ and are closed under multiplication by $\mathbb{D}$; neither is a free $\mathbb{D}$-span, since $j - 1$ annihilates $\mathbb{H} \tilde\Pi_+$ and $j + 1$ annihilates $\mathbb{H} \tilde\Pi_-$, whereas a free $\mathbb{D}$-span has no such annihilator. The whole algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-$ has $\mathbb{D}$-basis $e_0, e_1, e_2, e_3$.

The $\mathbb{R}$-automorphisms and $\mathbb{R}$-derivations of $\mathbb{H}_{\mathbb{D}}$ act on this two-term decomposition. Because the two simple factors are isomorphic, the automorphism group contains the exchange of the factors, and the derivations contain the corresponding off-diagonal maps; the precise statements, together with the comparison with the biquaternion case, are the subject of *Split-Biquaternion Automorphisms and Derivations*. The splitting $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-$ established here is the object on which those automorphisms act.

## Summary

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ has exactly two proper nonzero two-sided ideals, $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$; it is therefore not simple, but it is semisimple, with vanishing radical. The two ideals are the two quaternion halves of the decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_- \cong \mathbb{H} \oplus \mathbb{H}$, each isomorphic to the division algebra $\mathbb{H}$.

The minimal left ideals, the minimal right ideals and the minimal two-sided ideals coincide and are exactly $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$, because the underlying idempotents are central. The Peirce decomposition relative to $\tilde\Pi_+$ has vanishing off-diagonal spaces,

$$
\mathbb{H}_{\mathbb{D}} = \tilde\Pi_+ \mathbb{H}_{\mathbb{D}} \tilde\Pi_+ \oplus (1 - \tilde\Pi_+) \mathbb{H}_{\mathbb{D}} (1 - \tilde\Pi_+) = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-,
$$

so the two halves do not mix. The left ideals are exactly $0$, $\mathbb{H} \tilde\Pi_+$, $\mathbb{H} \tilde\Pi_-$, $\mathbb{H}_{\mathbb{D}}$, forming a diamond lattice with two maximal ideals, in contrast with the projective line of left ideals of the simple biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$. The idempotents themselves, their classification, their role as projections and their relation to the roots of $-1$, are the subject of *Split-Biquaternion Idempotents and Projections*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, $\cong \mathbb{H} \oplus \mathbb{H}$ |
| $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ | The complete family of primitive central idempotents |
| $\mathbb{H} \tilde\Pi_+, \mathbb{H} \tilde\Pi_-$ | The two minimal (left, right and two-sided) ideals, each $\cong \mathbb{H}$ |
| $\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_-$ | Idempotent decomposition, $\tilde{Q}_\pm \in \mathbb{H}$ |
| $eAe$, $eA(1-e)$, $(1-e)Ae$, $(1-e)A(1-e)$ | Peirce spaces relative to an idempotent $e$ |
| $J(\mathbb{H}_{\mathbb{D}})$ | Jacobson radical, equal to $0$ |
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$, simple |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for ideals, minimal left ideals and the Peirce decomposition in semisimple algebras.
- Irving Kaplansky, *Fields and Rings* (Chicago, 1972), for the structure theory of semisimple algebras and the radical.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the ideal structure of Clifford algebras and their relatives.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the algebraic structure of split biquaternions and their direct-sum decomposition.
