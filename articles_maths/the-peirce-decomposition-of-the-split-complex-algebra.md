# __The Peirce Decomposition of the Split-Complex Algebra__

## Introduction

The split-complex algebra $\mathbb{D}=\mathbb{R}[j]$, with $j^{2}=+1$, carries the two idempotents $\Pi_{\pm}=\tfrac12(1\pm j)$. They are complete, orthogonal and central, and the Peirce decomposition relative to them is diagonal: the algebra is the sum of the two lines $\mathbb{R}\Pi_{+}$ and $\mathbb{R}\Pi_{-}$, and the two mixed components vanish.

This is the degenerate case of the Peirce construction. The general theory allows mixed components of dimension one or more; here they are zero, because the idempotents are central. The article states the decomposition for this algebra, gives the multiplication table and the root of $1$ that produces the family. The basis and the spinors are the subjects of *The Peirce Basis of the Split-Complex Algebra* and *Spinors as Peirce Coordinates in the Split-Complex Algebra*.

## The Algebra and the Family

**The algebra.** $\mathbb{D}=\mathbb{R}[j]$ with $j^{2}=+1$ is commutative, associative and unital, of real dimension $2$, with basis $1,j$. A general element is

$$
Q=q+jq',\qquad q,q'\in\mathbb{R}.
$$

The conjugation is $\bar Q=q-jq'$.

**The family.** Set

$$
\Pi_{+}=\frac{1+j}{2},\qquad \Pi_{-}=\frac{1-j}{2}.
$$

Then

$$
\Pi_{+}^{2}=\Pi_{+},\qquad \Pi_{-}^{2}=\Pi_{-},\qquad \Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}+\Pi_{-}=1 .
$$

The family is complete, orthogonal and idempotent. It is also central: $j\Pi_{\pm}=\Pi_{\pm}j$, so $\Pi_{\pm}$ commutes with every element.

**The coordinates in the family.** Every element has the unique expansion

$$
Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-},\qquad Q_{\pm}=q\pm q'.
$$

The map $Q\mapsto(Q_{+},Q_{-})$ is an isomorphism of $\mathbb{R}$-algebras from $\mathbb{D}$ to $\mathbb{R}\times\mathbb{R}$.

## The Peirce Lines

**Definition.** For $\sigma,\tau\in\{+,-\}$ the Peirce line is

$$
\mathbb{D}_{\sigma\tau}=\Pi_{\sigma}\mathbb{D}\Pi_{\tau}.
$$

**Proposition.** The two diagonal lines are one-dimensional, the two mixed lines are zero, and

$$
\mathbb{D}=\mathbb{D}_{++}\oplus\mathbb{D}_{--}.
$$

**Proof.** Since $\Pi_{\sigma}$ is central,

$$
\mathbb{D}_{\sigma\tau}=\Pi_{\sigma}\Pi_{\tau}\mathbb{D}=\delta_{\sigma\tau}\,\Pi_{\sigma}\mathbb{D}.
$$

So $\mathbb{D}_{+-}=\mathbb{D}_{-+}=0$, and

$$
\mathbb{D}_{++}=\Pi_{+}\mathbb{D}=\mathbb{R}\Pi_{+},\qquad \mathbb{D}_{--}=\Pi_{-}\mathbb{D}=\mathbb{R}\Pi_{-},
$$

each of real dimension one. The two lines sum to $\mathbb{D}$ because $\Pi_{+}+\Pi_{-}=1$, and their intersection is zero because $\Pi_{+}\Pi_{-}=0$.

**The diagonal is canonical.** Each diagonal line is spanned by its idempotent, and the idempotent is determined by the family. There is no off-diagonal line and therefore no off-diagonal element to choose.

## The Multiplication Rule

The general rule of the Peirce decomposition gives, for $\sigma,\tau,\mu,\nu\in\{+,-\}$,

$$
\mathbb{D}_{\sigma\tau}\mathbb{D}_{\mu\nu}\subseteq\delta_{\tau\mu}\mathbb{D}_{\sigma\nu}.
$$

In this algebra the only nonzero lines are the diagonal ones, so the table reduces to

$$
\mathbb{D}_{++}\mathbb{D}_{++}\subseteq\mathbb{D}_{++},\qquad
\mathbb{D}_{--}\mathbb{D}_{--}\subseteq\mathbb{D}_{--},\qquad
\mathbb{D}_{++}\mathbb{D}_{--}=0,\qquad
\mathbb{D}_{--}\mathbb{D}_{++}=0.
$$

In coordinates the product is componentwise:

$$
(Q_{+}\Pi_{+}+Q_{-}\Pi_{-})(R_{+}\Pi_{+}+R_{-}\Pi_{-})=(Q_{+}R_{+})\Pi_{+}+(Q_{-}R_{-})\Pi_{-}.
$$

## The Root of $1$

**Proposition.** The roots of $x^{2}=1$ in $\mathbb{D}$ are $1,-1,j,-j$.

**Proof.** Write $x=a+bj$. Then $x^{2}=a^{2}+b^{2}+2abj$, so $x^{2}=1$ is equivalent to

$$
a^{2}+b^{2}=1,\qquad 2ab=0.
$$

If $b=0$ then $a=\pm1$; if $a=0$ then $b=\pm1$. These are the four elements listed.

**The family from the root.** The nontrivial roots are $\pm j$, and

$$
\Pi_{\pm}=\frac{1\pm j}{2},\qquad \Pi_{\mp}=\frac{1\mp j}{2}.
$$

The two roots give the same unordered family: the root $j$ attaches $\Pi_{+}$ to $+1$ and $\Pi_{-}$ to $-1$, and the root $-j$ exchanges the two labels. The family is the spectral family of $j$.

**The root is not needed.** The pair $\{\Pi_{+},\Pi_{-}\}$ is the only nontrivial complete orthogonal pair of $\mathbb{D}$: the idempotents of $\mathbb{R}\times\mathbb{R}$ are $(0,0)$, $(1,0)$, $(0,1)$ and $(1,1)$. So the family is unique as an unordered pair, and every root of $1$ different from $\pm1$ produces it.

## Central Idempotents and the Product Decomposition

Because $\Pi_{\pm}$ is central, the decomposition $\mathbb{D}=\mathbb{D}_{++}\oplus\mathbb{D}_{--}$ is a decomposition into two algebras, each with unit $\Pi_{\pm}$, and the algebra is the direct product of them:

$$
\mathbb{D}\cong\mathbb{R}\Pi_{+}\times\mathbb{R}\Pi_{-},\qquad Q\longmapsto(Q_{+},Q_{-}).
$$

This is the structural reason for the vanishing of the mixed lines. In a general Peirce decomposition the mixed line $\mathbb{D}_{+-}$ need not vanish; it vanishes exactly when $\Pi_{+}$ is central, because then $\Pi_{+}\mathbb{D}\Pi_{-}=\Pi_{+}\Pi_{-}\mathbb{D}=0$.

The scalar $j$ is the difference of the two idempotents:

$$
j=\Pi_{+}-\Pi_{-},\qquad \Pi_{\pm}=\frac{1\pm j}{2}.
$$

## What the Decomposition Does Not Give

The decomposition gives two lines, each spanned by its idempotent, and no mixed line. It gives no off-diagonal element to choose, no gauge, no coordinate mixing and no two-component spinor. The basis is canonical and the spinor is a single scalar; these are the degenerate forms of the two constructions, and they are treated in the next two articles.

## Summary

The split-complex algebra $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=1$, has the complete orthogonal family $\Pi_{\pm}=\tfrac12(1\pm j)$. The idempotents are central, so the Peirce decomposition is diagonal, $\mathbb{D}=\mathbb{R}\Pi_{+}\oplus\mathbb{R}\Pi_{-}$, with the two mixed components zero. The multiplication is componentwise, the algebra is $\mathbb{R}\times\mathbb{R}$, and the nontrivial roots of $1$ are $\pm j$, both giving the same unordered family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=1$ | The split-complex algebra |
| $Q=q+jq'$ | A general element |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The two idempotents |
| $Q_{\pm}=q\pm q'$ | The idempotent coordinates |
| $\mathbb{D}_{\sigma\tau}=\Pi_{\sigma}\mathbb{D}\Pi_{\tau}$ | A Peirce component |

## Further Reading

- [The Split-Complex Algebra](split-complex-algebra.html), for the algebra, its conjugation and its geometry.
- [Square Roots of One and the Idempotents of the Split-Complex Algebra](square-roots-of-one-and-the-idempotents-of-the-split-complex-algebra.html), for the idempotents and the halving map.
- [The Peirce Basis of the Split-Complex Algebra](the-peirce-basis-of-the-split-complex-algebra.html), for the canonical basis.
- [Spinors as Peirce Coordinates in the Split-Complex Algebra](spinors-as-peirce-coordinates-in-the-split-complex-algebra.html), for the degenerate spinor.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the nondegenerate case.
