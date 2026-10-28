# __The Peirce Decomposition of the Reduced Biquaternion Algebra__

## Introduction

The reduced biquaternion algebra $\mathbb{B}_{\mathrm r}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is commutative, associative and unital, of complex dimension $2$, with basis $1,j$ and $j^{2}=+1$. Its two idempotents $\Pi_{\pm}=\tfrac12(1\pm j)$ are complete, orthogonal and central, and the Peirce decomposition relative to them is diagonal: the algebra is the sum of the two lines $\mathbb{C}\Pi_{+}$ and $\mathbb{C}\Pi_{-}$, and the two mixed components vanish.

This is the degenerate case of the Peirce construction. The mixed components vanish because the idempotents are central, exactly as in the split-complex algebra. The article states the decomposition, the multiplication table and the root of $1$ that produces the family. The basis and the spinors are *The Peirce Basis of the Reduced Biquaternion Algebra* and *Spinors as Peirce Coordinates in the Reduced Biquaternion Algebra*.

## The Algebra and the Family

**The algebra.** Over $\mathbb{C}$,

$$
\mathbb{B}_{\mathrm r}=\mathbb{C}[j]/(j^{2}-1),\qquad j^{2}=1,
$$

with basis $1,j$ and product determined by $j^{2}=1$. A general element is

$$
\breve Q=u+jv,\qquad u,v\in\mathbb{C}.
$$

The algebra is commutative, associative and unital, with unit $1$. Over $\mathbb{R}$ it has dimension $4$; over $\mathbb{C}$ it has dimension $2$. The scalar field of the Peirce decomposition is $\mathbb{C}$.

**The family.** Set

$$
\Pi_{+}=\frac{1+j}{2},\qquad \Pi_{-}=\frac{1-j}{2}.
$$

Then

$$
\Pi_{+}^{2}=\Pi_{+},\qquad \Pi_{-}^{2}=\Pi_{-},\qquad \Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}+\Pi_{-}=1 .
$$

The family is complete, orthogonal and idempotent. It is central, because $j$ commutes with $i$ and with every element.

**The coordinates in the family.** Every element has the unique expansion

$$
\breve Q=\breve Q_{+}\Pi_{+}+\breve Q_{-}\Pi_{-},\qquad \breve Q_{\pm}=u\pm v .
$$

The map $\breve Q\mapsto(\breve Q_{+},\breve Q_{-})$ is an isomorphism of $\mathbb{C}$-algebras from $\mathbb{B}_{\mathrm r}$ to $\mathbb{C}\times\mathbb{C}$.

## The Peirce Lines

**Definition.** For $\sigma,\tau\in\{+,-\}$ the Peirce line is

$$
\mathbb{B}_{\sigma\tau}=\Pi_{\sigma}\mathbb{B}_{\mathrm r}\Pi_{\tau}.
$$

**Proposition.** The two diagonal lines are one-dimensional over $\mathbb{C}$, the two mixed lines are zero, and

$$
\mathbb{B}_{\mathrm r}=\mathbb{B}_{++}\oplus\mathbb{B}_{--}.
$$

**Proof.** Since $\Pi_{\sigma}$ is central,

$$
\mathbb{B}_{\sigma\tau}=\Pi_{\sigma}\Pi_{\tau}\mathbb{B}_{\mathrm r}=\delta_{\sigma\tau}\,\Pi_{\sigma}\mathbb{B}_{\mathrm r}.
$$

So $\mathbb{B}_{+-}=\mathbb{B}_{-+}=0$, and

$$
\mathbb{B}_{++}=\mathbb{C}\Pi_{+},\qquad \mathbb{B}_{--}=\mathbb{C}\Pi_{-},
$$

each of complex dimension one. The two lines sum to the algebra because $\Pi_{+}+\Pi_{-}=1$, and their intersection is zero because $\Pi_{+}\Pi_{-}=0$.

**The diagonal is canonical.** Each diagonal line is spanned by its idempotent, and the idempotent is determined by the family. There is no off-diagonal line and no off-diagonal element to choose.

## The Multiplication Rule

The general rule gives, for $\sigma,\tau,\mu,\nu\in\{+,-\}$,

$$
\mathbb{B}_{\sigma\tau}\mathbb{B}_{\mu\nu}\subseteq\delta_{\tau\mu}\mathbb{B}_{\sigma\nu}.
$$

In this algebra the only nonzero lines are the diagonal ones, so the table reduces to

$$
\mathbb{B}_{++}\mathbb{B}_{++}\subseteq\mathbb{B}_{++},\qquad
\mathbb{B}_{--}\mathbb{B}_{--}\subseteq\mathbb{B}_{--},\qquad
\mathbb{B}_{++}\mathbb{B}_{--}=0,\qquad
\mathbb{B}_{--}\mathbb{B}_{++}=0.
$$

In coordinates the product is componentwise:

$$
(\breve Q_{+}\Pi_{+}+\breve Q_{-}\Pi_{-})(\breve R_{+}\Pi_{+}+\breve R_{-}\Pi_{-})=(\breve Q_{+}\breve R_{+})\Pi_{+}+(\breve Q_{-}\breve R_{-})\Pi_{-}.
$$

## The Root of $1$

**Proposition.** The roots of $x^{2}=1$ in $\mathbb{B}_{\mathrm r}$ are $1,-1,j,-j$.

**Proof.** Write $x=u+jv$ with $u,v\in\mathbb{C}$. Then $x^{2}=u^{2}+v^{2}+2uvj$, so $x^{2}=1$ is equivalent to

$$
u^{2}+v^{2}=1,\qquad 2uv=0.
$$

If $v=0$ then $u=\pm1$; if $u=0$ then $v=\pm1$. These are the four elements listed.

**The family from the root.** The nontrivial roots are $\pm j$, and

$$
\Pi_{\pm}=\frac{1\pm j}{2}.
$$

The root $j$ attaches $\Pi_{+}$ to $+1$ and $\Pi_{-}$ to $-1$; the root $-j$ exchanges the labels and gives the same unordered family. The family is the spectral family of $j$.

**The root is not needed.** The idempotents of $\mathbb{C}\times\mathbb{C}$ are $(0,0)$, $(1,0)$, $(0,1)$ and $(1,1)$, so the nontrivial complete orthogonal pairs are $(\Pi_{+},\Pi_{-})$ and $(\Pi_{-},\Pi_{+})$, the same unordered family. Every nontrivial root of $1$ produces it.

## Central Idempotents and the Product Decomposition

Because $\Pi_{\pm}$ is central, the decomposition is a decomposition into two algebras, each with unit $\Pi_{\pm}$, and the algebra is the direct product

$$
\mathbb{B}_{\mathrm r}\cong\mathbb{C}\Pi_{+}\times\mathbb{C}\Pi_{-},\qquad \breve Q\longmapsto(\breve Q_{+},\breve Q_{-}).
$$

This is the structural reason for the vanishing of the mixed lines: for central $\Pi_{+}$,

$$
\Pi_{+}\mathbb{B}_{\mathrm r}\Pi_{-}=\Pi_{+}\Pi_{-}\mathbb{B}_{\mathrm r}=0.
$$

The generator $j$ is the difference of the two idempotents:

$$
j=\Pi_{+}-\Pi_{-},\qquad \Pi_{\pm}=\frac{1\pm j}{2}.
$$

## What the Decomposition Does Not Give

The decomposition gives two lines, each spanned by its idempotent, and no mixed line. It gives no off-diagonal element to choose, no gauge, no coordinate mixing and no two-component spinor. The basis is canonical and the spinor is a single complex scalar; these are the degenerate forms of the two constructions, treated in the next two articles.

## Summary

The reduced biquaternion algebra $\mathbb{B}_{\mathrm r}=\mathbb{C}[j]/(j^{2}-1)$, of complex dimension $2$, has the complete orthogonal family $\Pi_{\pm}=\tfrac12(1\pm j)$. The idempotents are central, so the Peirce decomposition is diagonal, $\mathbb{B}_{\mathrm r}=\mathbb{C}\Pi_{+}\oplus\mathbb{C}\Pi_{-}$, with the mixed components zero. The multiplication is componentwise, the algebra is $\mathbb{C}\times\mathbb{C}$, and the nontrivial roots of $1$ are $\pm j$, both giving the same unordered family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm r}=\mathbb{C}[j]/(j^{2}-1)$ | The reduced biquaternion algebra |
| $\breve Q=u+jv$ | A general element |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The two idempotents |
| $\breve Q_{\pm}=u\pm v$ | The idempotent coordinates |
| $\mathbb{B}_{\sigma\tau}=\Pi_{\sigma}\mathbb{B}_{\mathrm r}\Pi_{\tau}$ | A Peirce component |

## Further Reading

- [Introduction to the Algebra of the Reduced Biquaternions](introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the algebra and its product.
- [The Peirce Basis of the Reduced Biquaternion Algebra](the-peirce-basis-of-the-reduced-biquaternion-algebra.html), for the canonical basis.
- [Spinors as Peirce Coordinates in the Reduced Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-reduced-biquaternion-algebra.html), for the degenerate spinor.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the nondegenerate case.
