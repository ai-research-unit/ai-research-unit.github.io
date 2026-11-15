# __The Involutions, the Subspaces and the Idempotent Lines of the Split-Complex Space__

## Introduction

The split-complex ring $\mathbb{C}_{\mathrm{spl}}=\mathbb{R}[j]$, $j^2=1$, carries exactly two involutions: the identity and the conjugation $\bar\cdot$, $j\mapsto-j$. The two form the group $V_2$ of order two. This article computes what the two involutions cut: the four subspaces, fixed and anti-fixed, the two decompositions of the plane they give, the finer decomposition into the two idempotent lines, and the two lines on which the Hermitian form vanishes.

The count is the point. The ring offers two marks, the identity and the bar, and no third: the bar is an automorphism of order two and the intrinsic conjugation has nothing to reverse. The shortness of the list is not an accident of notation: it is the commutativity of the ring together with the absence of a vector part.

The article assumes the algebra of *Split-Complex Algebra* and the idempotents of *Square Roots of One and the Idempotents of the Split-Complex Algebra*. The forms used in the last section are *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, and the ideals the idempotent lines define are *Ideals and Peirce Decomposition of the Split-Complex Algebra*.

## The Two Involutions

**Definition.** An **involution** of $\mathbb{C}_{\mathrm{spl}}$ is an $\mathbb{R}$-linear map $\sigma$ with $\sigma(AC)=\sigma(A)\sigma(C)$ for all $A,C$ and $\sigma^2=\mathrm{id}$.

The ring is commutative, so an anti-automorphism is an automorphism and the two words name one notion. This is the first place where the split case is simpler than the non-commutative one, where the intrinsic conjugation reverses the order of a product.

**Theorem (the involution group).** The involutions of $\mathbb{C}_{\mathrm{spl}}$ are the identity and the conjugation

$$
\mathrm{id}:q+jq'\mapsto q+jq', \qquad \bar\cdot:q+jq'\mapsto q-jq' ,
$$

and they form the group $V_2=\{\mathrm{id},\bar\cdot\}$ of order two.

**Proof.** An involution fixes $1$ and preserves sums, so it is determined by the image of $j$. That image satisfies $\xi^2=\sigma(j)^2=\sigma(j^2)=\sigma(1)=1$, hence $\xi=\pm1$ over $\mathbb{R}$, and the two choices give the two maps displayed; each is $\mathbb{R}$-linear, multiplicative and of square one. It remains to see that $\sigma$ fixes $\mathbb{R}$. It fixes $\mathbb{Q}$, and it maps a square to a square, so it maps a positive real to a positive real, hence preserves the order of $\mathbb{R}$; an order-preserving field automorphism of $\mathbb{R}$ is the identity.

The proof uses only that $\mathbb{R}$ is an ordered field, so the same computation over any ordered field gives the same $V_2$. Over a field containing a square root of $1$ other than $\pm1$ the count would be larger; there is none in an ordered field.

### The Identity

The identity has the whole algebra as its fixed space and $\{0\}$ as its anti-fixed space. The eigenspace decomposition it gives is the degenerate one,

$$
\mathbb{C}_{\mathrm{spl}}=\mathbb{C}_{\mathrm{spl}}\oplus\{0\} ,
$$

and it carries no information: a direct sum with a zero summand. The identity is in the group for the same reason that the unit is in a group, and it contributes the two trivial subspaces and nothing else.

### The Conjugation

The conjugation has the real line as its fixed space and the split imaginary line as its anti-fixed space,

$$
\mathbb{C}_{\mathrm{spl}}^{\bar\cdot}=\{Q:\bar Q=Q\}=\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}, \qquad
\mathbb{C}_{\mathrm{spl}}^{-\bar\cdot}=\{Q:\bar Q=-Q\}=j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}} .
$$

**Proof.** $\bar Q=Q$ reads $q-jq'=q+jq'$, hence $q'=0$; $\bar Q=-Q$ reads $q-jq'=-q-jq'$, hence $q=0$.

Both spaces are one-dimensional, and the algebra is their direct sum. The conjugation is also the exchange of the idempotent coordinates, $\overline{Q_+}=Q_-$ and $\overline{Q_-}=Q_+$, and it exchanges the two idempotents, $\overline{\Pi_+}=\Pi_-$ and $\overline{\Pi_-}=\Pi_+$. The exchange of coordinates is the reason the bar can be read on the spectrum as the transposition of the two points, which is *The Spectrum and the Two-Point Structure of $\mathbb{C}^{\mathrm{spl}}$ over $\mathbb{R}$*.

### The Conjugation and the Two Other Marks

Three descriptions of the involution occur in the corpus, and on $\mathbb{C}_{\mathrm{spl}}$ two of them coincide while the third is the identity.

- The **conjugation** of the ring, $j\mapsto-j$, is the involution above.
- The **exchange of the idempotent coordinates**, $Q_+\leftrightarrow Q_-$, is the same map, since $\overline{q\pm q'}=q\mp q'$.
- The **intrinsic conjugation** ${}^{\natural}$, which reverses the sign of the vector part, is the identity here: there is no vector part to reverse.

A non-commutative algebra with a vector part carries more marks than this one; here the marks act as two maps, the identity and the bar, and the group is $V_2$. The short list has two causes and no third: the ring is commutative, so no involution can be an anti-automorphism without being an automorphism, and the element has no vector part, so the intrinsic conjugation has no carrier.

## The Three Decompositions of the Plane

The plane carries three decompositions into two subspaces, and it matters which one is finer than which.

| Decomposition | The two summands | Dimensions | What it is |
|---|---|---|---|
| the identity | $\mathbb{C}_{\mathrm{spl}}$, $\{0\}$ | $2+0$ | degenerate |
| the conjugation | $\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$, $j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$ | $1+1$ | the eigenspaces of $\bar\cdot$ |
| the idempotents | $\mathbb{R}\Pi_+$, $\mathbb{R}\Pi_-$ | $1+1$ | the minimal ideals |

### The Degenerate Decomposition of the Identity

It is the eigenspace decomposition of the identity and it separates nothing. Its only use is to fix the pattern: to each involution belong the two eigenspaces with eigenvalues $+1$ and $-1$, and for the identity the second is zero.

### The Eigenspace Decomposition of the Conjugation

It separates the scalar from the hyperbolic part. The fixed line is the line of the elements the involution cannot see, and the anti-fixed line is the line it negates; every element is a sum of one from each, and the sum is unique.

### The Idempotent Split

The idempotent split is the decomposition

$$
\mathbb{C}_{\mathrm{spl}}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_- , \qquad \Pi_\pm=\tfrac12(1\pm j) ,
$$

and it is the finest decomposition of the algebra into ideals: the two lines are the two minimal ideals and the only proper non-zero ones (*Ideals and Peirce Decomposition of the Split-Complex Algebra*). No line inside $\mathbb{R}\Pi_+$ is an ideal.

**The objection.** The idempotent split is not a refinement of the bar split: the fixed line $\mathbb{R}$ contains the element $\Pi_++\Pi_-=1$ and is not a sum of idempotent lines, and the idempotent line $\mathbb{R}\Pi_+$ meets the fixed line in $\{0\}$. So "finer" needs a meaning.

**The answer.** Fineness is a property of a decomposition into ideals, and there the order is exact: the idempotent split refines every decomposition of the algebra into ideals, and the bar split is not one of those, its summands being the eigenspaces of a map and not ideals. The two splits answer different questions, and the idempotent one is the finest answer to the algebraic question.

The bar permutes the two idempotent lines and preserves the two bar lines, so the two splits are exchanged by the group and not nested. This is *The Peirce Basis of the Split-Complex Algebra* read on the involution, and the same relation holds in a larger algebra, where the bar permutes a family the intrinsic conjugation preserves.

## The Four Subspaces and Their Intersections

To the two involutions belong four subspaces, and their intersections state how much the two involutions share.

| The intersection | The subspace | Dimension |
|---|---|---|
| fixed of $\mathrm{id}$ with fixed of $\bar\cdot$ | $\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$ | $1$ |
| fixed of $\mathrm{id}$ with anti-fixed of $\bar\cdot$ | $j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$ | $1$ |
| anti-fixed of $\mathrm{id}$ with fixed of $\bar\cdot$ | $\{0\}$ | $0$ |
| anti-fixed of $\mathrm{id}$ with anti-fixed of $\bar\cdot$ | $\{0\}$ | $0$ |

### The Fixed Spaces Meet in the Real Line

The fixed space of the identity is the whole algebra and the fixed space of the conjugation is the real line, so their intersection is the real line. It is the one non-zero subspace fixed by both involutions. In a larger algebra with four distinct marks the same computation gives many more non-zero intersections, because four marks give four fixed and four anti-fixed spaces; here two marks give four spaces in all, and only the two displayed carry a line.

### The Anti-Fixed Spaces Meet in Zero

The identity has no anti-fixed vector and the conjugation negates the split imaginary line, so the two anti-fixed spaces meet in $\{0\}$. An element negated by both involutions is negated by the identity, hence is zero. The asymmetry between the two rows is the whole content of the group being $V_2$: the identity has one non-trivial space and the conjugation two.

## The Closure of the Real Line and the Failure of Closure of the Split Imaginary Line

The real line is closed under the product and the split imaginary line is not.

**Proposition.** $\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}\cdot\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}\subseteq\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$ and $j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}\cdot j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}=\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}\not\subseteq j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$.

**Proof.** $(a)(c)=ac$ is real, and $(aj)(cj)=ac\,j^2=ac$ is real and non-zero for $ac\neq0$.

So the real line is a subalgebra, in fact the smallest one, and the split imaginary line is not: it is closed under addition and under multiplication by reals, and the product of two of its elements falls out of it. The consequence is structural. The fixed part of the involution is a ring and the anti-fixed part is only a module over that ring. The failure is the split sign itself: with $j^2=-1$ the anti-fixed line of the complex conjugation would be closed, and the complex field would have two subrings where the split ring has one.

The two lines together generate the algebra. The unital subalgebras are therefore $\mathbb{R}$ and $\mathbb{C}_{\mathrm{spl}}$ alone, since a unital subalgebra containing an element off the real line is two-dimensional. The non-unital ones are $\{0\}$ and the two idempotent lines $\mathbb{R}\Pi_\pm$, which are closed because $\Pi_\pm^2=\Pi_\pm$; the split imaginary line is not among them. The classification of the subalgebras is the split instance of the general theory of *Commutative Algebras with an Involution*.

## The Two Isotropic Idempotent Lines

The two idempotent lines are isotropic for the Hermitian form and for the split norm, and this is the property the complex field cannot reproduce.

**Proposition.** $H(\lambda\Pi_+,\mu\Pi_+)=0$ and $H(\lambda\Pi_-,\mu\Pi_-)=0$ for all real $\lambda,\mu$, where $H(A,C)=A\bar C$, and $\langle\lambda\Pi_\pm\rangle_*=\lambda^2\Pi_\pm\bar\Pi_\pm=0$.

**Proof.** $\overline{\Pi_+}=\Pi_-$ and $\Pi_+\Pi_-=0$, so $H(\lambda\Pi_+,\mu\Pi_+)=\lambda\mu\Pi_+\overline{\Pi_+}=\lambda\mu\Pi_+\Pi_-=0$; the computation for $\Pi_-$ is the same with the two labels exchanged. The split norm $\langle Q\rangle_*=Q\bar Q$ agrees with $H(Q,Q)$, so it vanishes on the same lines.

### The Isotropic Lines

A line is **isotropic** for $H$ when the form vanishes on its square. The two idempotent lines are isotropic, and they are the only ones: $H(Q,Q)=q^2-q'^2$ vanishes exactly when $q^2=q'^2$, which is $Q\in\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$ (*Zero Divisors of the Split-Complex Algebra*). The isotropic set is therefore a pair of lines and not a point, and it is exactly the set of non-units with the origin adjoined.

The lines are also the two Peirce components, so the isotropic set is the union of the two minimal ideals. This coincidence is special to dimension two: in a higher-dimensional algebra the null set is larger than the union of the minimal ideals.

### The Comparison with the Complex Field

Over $\mathbb{C}$ with the conjugation $i\mapsto-i$ the group is again $V_2$, the fixed space is the real line and the anti-fixed space the imaginary line, and the Hermitian form $A\bar C$ is positive definite. Its isotropic set is therefore the origin alone, and neither of the two eigenspaces is isotropic: the whole phenomenon of the last proposition is absent. What the split ring adds is not a second involution but a second isotropic line, and the two come from one fact, the sign $j^2=+1$, which makes the anti-fixed line fall out of the subring of fixed elements.

## Summary

The split-complex ring has exactly two involutions, the identity and the conjugation $j\mapsto-j$, and they form $V_2=\{\mathrm{id},\bar\cdot\}$: an involution is determined by the image of $j$, which satisfies $\xi^2=1$, and the bar is the exchange of the idempotent coordinates. The four marks of the general theory act here as two maps because the ring is commutative and has no vector part.

The identity gives the degenerate decomposition $\mathbb{C}_{\mathrm{spl}}\oplus\{0\}$, the conjugation the eigenspace decomposition $\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}\oplus j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$, and the idempotents the split $\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ into the two minimal ideals, which is the finest decomposition into ideals and is neither finer nor coarser than the bar split.

The only non-zero subspace fixed by both involutions is the real line, and the two anti-fixed spaces meet in $\{0\}$. The real line is closed under the product and the split imaginary line is not, because $j^2=1$, so the fixed part of the involution is a subring and the anti-fixed part is only a module. The two idempotent lines are isotropic for the Hermitian form and for the split norm, and they are the only isotropic lines; over the complex field the fixed and anti-fixed lines are the real and imaginary axes and neither is isotropic, since the Hermitian form is definite there.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{id}$, $\bar\cdot$ | The two involutions, $j\mapsto j$ and $j\mapsto-j$ |
| $V_2=\{\mathrm{id},\bar\cdot\}$ | The involution group, of order two |
| $\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$ | The fixed line of the conjugation, the real line |
| $j\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}$ | The anti-fixed line, the split imaginary line |
| $\Pi_\pm=\tfrac12(1\pm j)$ | The two idempotents; $\mathbb{R}\Pi_\pm$ the two idempotent lines |
| $\mathbb{C}_{\mathrm{spl}}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ | The idempotent split, the finest decomposition into ideals |
| $H(A,C)=A\bar C$ | The Hermitian form, vanishing on both idempotent lines |
| $\langle Q\rangle_*=Q\bar Q=q^2-q'^2$ | The split norm, with the same two null lines |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for involutions of an algebra, the exchange involution of a product ring and the Peirce decomposition.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, Colloquium Publications 44, 1998), for algebras with involution, the first and the second kind, and the split case.
- Nathan Jacobson, *Basic Algebra I* (Freeman, 2nd ed. 1985), for the automorphisms of a polynomial quotient and the ordered-field argument that fixes the base.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for $\mathbb{C}_{\mathrm{spl}}$ as the Clifford algebra $\mathrm{Cl}_{1,0}$ and its involutions read as grade signs.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the isotropic lines of the split plane and their role in the hyperbolic geometry.
