# __Peirce Decompositions of the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has complex dimension four. A complete orthogonal family of two nonzero idempotents, an element pair $\tilde\Pi_{\mathrm{id},+},\tilde\Pi_{\mathrm{id},-}$ with

$$
\tilde\Pi_{\mathrm{id},\pm}^{2}=\tilde\Pi_{\mathrm{id},\pm},\qquad
\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=\tilde\Pi_{\mathrm{id},-}\tilde\Pi_{\mathrm{id},+}=0,\qquad
\tilde\Pi_{\mathrm{id},+}+\tilde\Pi_{\mathrm{id},-}=e_{t},
$$

cuts $\mathbb{B}$ into four complex lines

$$
\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t},\qquad s,t\in\{+,-\}.
$$

The family is the only input. The signs are labels of the pair. No element of a mixed line is chosen, and no basis is chosen. Each such family gives its own Peirce decomposition, and the algebra carries as many as it carries families; the plural in the title records this, and the article keeps the family as the variable throughout.

The article defines the family and the four lines, proves that each line is one-dimensional and that the lines sum directly, computes their multiplication rule, reads the two indices that the family assigns to each line, identifies the two mixed components, records the parity of the cut, and says what the cut does not give. The choice of an element in each line and its frame group are *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*; the coordinates and the spinors are *The Polarized Module of the Biquaternion Algebra*. An example is given at the end.

## The Family

**Definition.** A family $\tilde\Pi_{\mathrm{id},+},\tilde\Pi_{\mathrm{id},-}$ is **complete, orthogonal and idempotent** when

$$
\tilde\Pi_{\mathrm{id},\pm}^{2}=\tilde\Pi_{\mathrm{id},\pm},\qquad
\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=\tilde\Pi_{\mathrm{id},-}\tilde\Pi_{\mathrm{id},+}=0,\qquad
\tilde\Pi_{\mathrm{id},+}+\tilde\Pi_{\mathrm{id},-}=e_{t}.
$$

It is **nondegenerate** when $\tilde\Pi_{\mathrm{id},\pm}\ne0$. The signs $+$ and $-$ are the two labels of the pair; exchanging them exchanges the two indices everywhere and leaves the unordered family unchanged.

**The family is not canonical.** The algebra carries no preferred family. Different families give different cuts of the same algebra.

## From One Idempotent to Its Complement

**Proposition.** Let $\tilde\Pi_{\mathrm{id}}\in\mathbb{B}$ be an idempotent with $\tilde\Pi_{\mathrm{id}}\ne0$ and $\tilde\Pi_{\mathrm{id}}\ne e_{t}$. Put $\tilde\Pi_{\mathrm{id}}'=e_{t}-\tilde\Pi_{\mathrm{id}}$. Then $\tilde\Pi_{\mathrm{id}}'$ is idempotent, nonzero, orthogonal to $\tilde\Pi_{\mathrm{id}}$, and $\tilde\Pi_{\mathrm{id}}+\tilde\Pi_{\mathrm{id}}'=e_{t}$. Conversely every nondegenerate complete family of two idempotents is obtained in this way from either of its members.

**Proof.** $(\tilde\Pi_{\mathrm{id}}')^{2}=e_{t}-2\tilde\Pi_{\mathrm{id}}+\tilde\Pi_{\mathrm{id}}^{2}=e_{t}-\tilde\Pi_{\mathrm{id}}=\tilde\Pi_{\mathrm{id}}'$, and $\tilde\Pi_{\mathrm{id}}\tilde\Pi_{\mathrm{id}}'=\tilde\Pi_{\mathrm{id}}-\tilde\Pi_{\mathrm{id}}^{2}=0=\tilde\Pi_{\mathrm{id}}'\tilde\Pi_{\mathrm{id}}$. The member $\tilde\Pi_{\mathrm{id}}'$ is nonzero because $\tilde\Pi_{\mathrm{id}}\ne e_{t}$, and $\tilde\Pi_{\mathrm{id}}$ is nonzero by hypothesis. The converse is the computation $e_{t}-\tilde\Pi_{\mathrm{id},+}=\tilde\Pi_{\mathrm{id},-}$ and $e_{t}-\tilde\Pi_{\mathrm{id},-}=\tilde\Pi_{\mathrm{id},+}$.

The proposition says that the family is the same data as a nontrivial idempotent, together with the choice of which member carries the label $+$. The Peirce corners of the pair are

$$
\mathbb{B}_{++}=\tilde\Pi_{\mathrm{id}}\mathbb{B}\tilde\Pi_{\mathrm{id}},\qquad
\mathbb{B}_{+-}=\tilde\Pi_{\mathrm{id}}\mathbb{B}\tilde\Pi_{\mathrm{id}}',\qquad
\mathbb{B}_{-+}=\tilde\Pi_{\mathrm{id}}'\mathbb{B}\tilde\Pi_{\mathrm{id}},\qquad
\mathbb{B}_{--}=\tilde\Pi_{\mathrm{id}}'\mathbb{B}\tilde\Pi_{\mathrm{id}}'.
$$

## The Peirce Decompositions

**Definition.** For $s,t\in\{+,-\}$ the **Peirce line** is $\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t}$.

**Lemma.** Let $A$ be a simple unital algebra, and let $e,f\in A$ be nonzero idempotents. Then $eAf\ne0$.

**Proof.** Suppose $eAf=0$. Then $e(AfA)=0$. The set $AfA$ is stable under multiplication on the left and on the right by $A$ and contains $f=f^{2}$, hence it is nonzero; by simplicity $AfA=A$. So $eA=0$, and then $e=e^{2}=0$, against the hypothesis.

**Theorem.** Each $\mathbb{B}_{st}$ is a complex line, and

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}.
$$

**Proof.** The sum is direct: if $\sum_{s,t}Q_{st}=0$ with $Q_{st}\in\mathbb{B}_{st}$, then multiplying on the left by $\tilde\Pi_{\mathrm{id},s}$ and on the right by $\tilde\Pi_{\mathrm{id},t}$ gives $Q_{st}=0$. It is all of $\mathbb{B}$ because

$$
\tilde Q=(\tilde\Pi_{\mathrm{id},+}+\tilde\Pi_{\mathrm{id},-})\tilde Q(\tilde\Pi_{\mathrm{id},+}+\tilde\Pi_{\mathrm{id},-})
=\sum_{s,t}\tilde\Pi_{\mathrm{id},s}\tilde Q\tilde\Pi_{\mathrm{id},t}
$$

for every $\tilde Q\in\mathbb{B}$. Each corner is nonzero: the diagonal corner contains $\tilde\Pi_{\mathrm{id},s}$, and the mixed corners are nonzero by the lemma, since $\mathbb{B}$ is simple (*Introduction to the Algebra of Biquaternions*). The algebra has complex dimension four, the sum is direct, and it has four nonzero summands; hence each summand is one-dimensional.

### The Biquaternion Case

The four lines are the whole content of the cut. The diagonal lines are

$$
\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_{\mathrm{id},+},\qquad
\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_{\mathrm{id},-},
$$

and the two mixed lines are nilpotent lines: every element of $\mathbb{B}_{+-}$ or of $\mathbb{B}_{-+}$ squares to zero. The idempotents $\tilde\Pi_{\mathrm{id},\pm}$ are primitive, because their corners are lines. The coarse split by the single idempotent $\tilde\Pi_{\mathrm{id},+}$ and the fine split by the pair have the same four corners.

**The family has four real parameters.** Under the matrix model $\mathbb{B}\cong M_{2}(\mathbb{C})$, a nontrivial idempotent is a rank-one projection: its image is a line in $\mathbb{C}^{2}$ and its kernel is a complementary line. The image is a point of $\mathbb{P}^{1}$, of one complex parameter, and the kernel is a point of $\mathbb{P}^{1}$ different from the image, of one complex parameter. The family therefore has complex dimension two, that is real dimension four. The labels $+$ and $-$ are discrete and do not change the dimension.

## The Multiplication Rule

**Theorem.** For $s,t,u,v\in\{+,-\}$,

$$
\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}.
$$

**Proof.** For $\tilde Q,\tilde Q'\in\mathbb{B}$,

$$
(\tilde\Pi_{\mathrm{id},s}\tilde Q\tilde\Pi_{\mathrm{id},t})(\tilde\Pi_{\mathrm{id},u}\tilde Q'\tilde\Pi_{\mathrm{id},v})
=\tilde\Pi_{\mathrm{id},s}\tilde Q(\tilde\Pi_{\mathrm{id},t}\tilde\Pi_{\mathrm{id},u})\tilde Q'\tilde\Pi_{\mathrm{id},v}
=\delta_{tu}\,\tilde\Pi_{\mathrm{id},s}\tilde Q\tilde Q'\tilde\Pi_{\mathrm{id},v},
$$

which lies in $\mathbb{B}_{sv}$ when $t=u$ and is zero otherwise.

The right index of the first factor must equal the left index of the second; the product runs from the left index of the first to the right index of the second. The mixed lines are square-zero, and the diagonal lines are the two idempotent lines.

## The Two Indices

**The left and right indices are the two idempotents that act as the identity.** For $\tilde Q\in\mathbb{B}_{st}$,

$$
\tilde\Pi_{\mathrm{id},s}\tilde Q=\tilde Q,\qquad \tilde Q\tilde\Pi_{\mathrm{id},t}=\tilde Q.
$$

Conversely, if both equations hold, then

$$
\tilde Q=\tilde\Pi_{\mathrm{id},s}\tilde Q\tilde\Pi_{\mathrm{id},t}\in\mathbb{B}_{st}.
$$

| Corner | Left index | Right index |
|---|---|---|
| $\mathbb{B}_{++}$ | $\tilde\Pi_{\mathrm{id},+}$ | $\tilde\Pi_{\mathrm{id},+}$ |
| $\mathbb{B}_{+-}$ | $\tilde\Pi_{\mathrm{id},+}$ | $\tilde\Pi_{\mathrm{id},-}$ |
| $\mathbb{B}_{-+}$ | $\tilde\Pi_{\mathrm{id},-}$ | $\tilde\Pi_{\mathrm{id},+}$ |
| $\mathbb{B}_{--}$ | $\tilde\Pi_{\mathrm{id},-}$ | $\tilde\Pi_{\mathrm{id},-}$ |

The diagonal lines have equal indices and the mixed lines have different indices. The two indices are the Peirce indices.

## The Two Mixed Components

**Proposition.** Let $u\in\mathbb{B}_{+-}$ be nonzero. Left multiplication by $u$ is an isomorphism from $\mathbb{B}_{-+}$ onto $\mathbb{B}_{++}$, maps $\mathbb{B}_{--}$ onto $\mathbb{B}_{+-}$, and kills $\mathbb{B}_{++}$ and $\mathbb{B}_{+-}$. Let $v\in\mathbb{B}_{-+}$ be nonzero. Left multiplication by $v$ is an isomorphism from $\mathbb{B}_{++}$ onto $\mathbb{B}_{-+}$, maps $\mathbb{B}_{+-}$ onto $\mathbb{B}_{--}$, and kills $\mathbb{B}_{-+}$ and $\mathbb{B}_{--}$.

**Proof.** The corner rule gives $u\mathbb{B}_{-+}\subseteq\mathbb{B}_{++}$, $u\mathbb{B}_{++}=0$, $u\mathbb{B}_{--}\subseteq\mathbb{B}_{+-}$ with $u\tilde\Pi_{\mathrm{id},-}=u\ne0$, and $u\mathbb{B}_{+-}=0$. The product $\mathbb{B}_{+-}\mathbb{B}_{-+}$ is nonzero by the lemma of §*The Peirce Decompositions*, and $\mathbb{B}_{-+}$ is a line, so $u\mathbb{B}_{-+}\ne0$ for every nonzero $u$. A nonzero linear map between two lines is an isomorphism. The same argument with the signs exchanged gives the statement for $v$, and $v\tilde\Pi_{\mathrm{id},+}=v\ne0$ is the direct witness.

The two isomorphisms are inverse up to the normalization of the pair. If $\vec\Pi_{\mathrm{nil},+-}\in\mathbb{B}_{+-}$ and $\vec\Pi_{\mathrm{nil},-+}\in\mathbb{B}_{-+}$ satisfy

$$
\vec\Pi_{\mathrm{nil},+-}\vec\Pi_{\mathrm{nil},-+}=\tilde\Pi_{\mathrm{id},+},\qquad
\vec\Pi_{\mathrm{nil},-+}\vec\Pi_{\mathrm{nil},+-}=\tilde\Pi_{\mathrm{id},-},
$$

then left multiplication by $\vec\Pi_{\mathrm{nil},-+}$ is the inverse of left multiplication by $\vec\Pi_{\mathrm{nil},+-}$ on $\mathbb{B}_{-+}$, and the two maps are inverse isomorphisms between $\mathbb{B}_{-+}$ and $\mathbb{B}_{++}$. Without the normalization, the pair is defined only up to reciprocal scale, and that scale is the frame group treated in *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*. No basis of either line is fixed by the family.

## The Decomposition as a Grading

**The diagonal lines form a subalgebra, and the mixed part is stable under it on both sides.** Put

$$
A_{0}=\mathbb{B}_{++}\oplus\mathbb{B}_{--},\qquad
A_{1}=\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}.
$$

The product rule reads

$$
A_{0}A_{0}\subseteq A_{0},\qquad
A_{0}A_{1}\subseteq A_{1},\qquad
A_{1}A_{0}\subseteq A_{1},\qquad
A_{1}A_{1}\subseteq A_{0}.
$$

Here $A_{0}=\mathbb{C}\tilde\Pi_{\mathrm{id},+}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},-}$ is the commutative algebra $\mathbb{C}\times\mathbb{C}$ with unit $e_{t}$, and $A_{1}$ is the sum of the two mixed lines. The parity of a corner $\mathbb{B}_{st}$ is the product $st$, which is $+1$ on the diagonal and $-1$ on the mixed lines. The parity is a consequence of the two-term family; it is not an extra input.

## What the Decomposition Does Not Give

The family gives the four lines and their multiplication. It gives no element of a mixed line, no basis, no frame freedom and no spinor. The diagonal lines have canonical vectors, the idempotents. The mixed lines do not: each is a complex line with its zero element removed, and the choice of a point in it is an extra datum. That datum, and the freedom that remains after it, are *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*.

## Example: The Standard Family

The standard family is

$$
\tilde\Pi_{\mathrm{id},+}=\frac{e_{t}+i\vec e_{z}}{2},\qquad
\tilde\Pi_{\mathrm{id},-}=\frac{e_{t}-i\vec e_{z}}{2}.
$$

It is complete, orthogonal and idempotent: the two squares are the two idempotents, the product is zero, and the sum is $e_{t}$. The four lines are spanned by

$$
\tilde\Pi_{\mathrm{id},+},\qquad
\vec\Pi_{\mathrm{nil},1}=\frac{i\vec e_{x}-\vec e_{y}}{2},\qquad
\vec\Pi_{\mathrm{nil},2}=\frac{i\vec e_{x}+\vec e_{y}}{2},\qquad
\tilde\Pi_{\mathrm{id},-},
$$

with $\vec\Pi_{\mathrm{nil},1}\in\mathbb{B}_{+-}$ and $\vec\Pi_{\mathrm{nil},2}\in\mathbb{B}_{-+}$. The products are

$$
\tilde\Pi_{\mathrm{id},+}\vec\Pi_{\mathrm{nil},1}=\vec\Pi_{\mathrm{nil},1}=\vec\Pi_{\mathrm{nil},1}\tilde\Pi_{\mathrm{id},-},\qquad
\tilde\Pi_{\mathrm{id},-}\vec\Pi_{\mathrm{nil},2}=\vec\Pi_{\mathrm{nil},2}=\vec\Pi_{\mathrm{nil},2}\tilde\Pi_{\mathrm{id},+},
$$

$$
\vec\Pi_{\mathrm{nil},1}\vec\Pi_{\mathrm{nil},2}=\tilde\Pi_{\mathrm{id},+},\qquad
\vec\Pi_{\mathrm{nil},2}\vec\Pi_{\mathrm{nil},1}=\tilde\Pi_{\mathrm{id},-},\qquad
\vec\Pi_{\mathrm{nil},1}^{2}=\vec\Pi_{\mathrm{nil},2}^{2}=0,
$$

and the other four products vanish. The standard family is Hermitian; it is one family among the four-real-parameter family of nontrivial idempotents, not a preferred one.

## Summary

A nondegenerate complete family $\tilde\Pi_{\mathrm{id},+},\tilde\Pi_{\mathrm{id},-}$ of two idempotents gives the four complex lines $\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t}$, each of dimension one, with the product rule $\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}$. The diagonal lines are spanned by the idempotents and the mixed lines are nilpotent lines. The left and right Peirce indices are the two idempotents acting as the identity, and the mixed lines have different indices. The diagonal part is the subalgebra $\mathbb{C}\times\mathbb{C}$ and the two mixed lines are stable under multiplication by it on both sides; the cut carries a parity. The family has four real parameters and is not canonical. It fixes the four lines but no element inside a mixed line, no basis and no frame freedom. One family gives one Peirce decomposition, and the algebra carries one for each family it carries.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra |
| $e_{t},\vec e_{x},\vec e_{y},\vec e_{z}$ | The quaternion units |
| $\tilde\Pi_{\mathrm{id},\pm}$ | The two idempotents of the family |
| $\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t}$ | A Peirce line |
| $\vec\Pi_{\mathrm{nil},+-},\vec\Pi_{\mathrm{nil},-+}$ | Nonzero elements of the mixed lines |
| $A_{0},A_{1}$ | The diagonal and mixed parts |

## Further Reading

- [The Biquaternion Algebra](introduction-to-the-algebra-of-biquaternions.html), for the units, the product table, the centre and simplicity.
- [Idempotents](the-square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the classification of the idempotents and the standard pair.
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the choice of an element in each line and the frame group.
- [The Polarized Module of the Biquaternion Algebra](the-polarized-module-of-the-biquaternion-algebra.html), for the elements of the two spinor spaces; the matrix form of the cut.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the general family.
- [Complementary Idempotents and the Peirce Decomposition](complementary-idempotents-and-the-peirce-decomposition.html), for the complement and the general corner rule.
