# __The Peirce Basis of the Reduced Biquaternion Algebra__

## Introduction

The Peirce decomposition of the reduced biquaternion algebra has two diagonal lines and no mixed line. A Peirce basis is the pair of the two idempotents, $\Pi_{+}$ and $\Pi_{-}$, and it is canonical: there is no element to choose, no gauge and no freedom.

This article states the basis, proves its uniqueness, gives the coordinates and records the degenerate dimension count. It assumes *The Peirce Decomposition of the Reduced Biquaternion Algebra*.

## The Definition

**Definition.** A **Peirce basis** of $\mathbb{B}_{\mathrm r}$ relative to the family $\Pi_{+},\Pi_{-}$ is a family $E_{\sigma\tau}\in\mathbb{B}_{\sigma\tau}$, one element for each pair, with

$$
E_{\sigma\tau}E_{\mu\nu}=\delta_{\tau\mu}E_{\sigma\nu},\qquad E_{\sigma\sigma}=\Pi_{\sigma}.
$$

**The off-diagonal elements do not exist.** Since $\mathbb{B}_{+-}=\mathbb{B}_{-+}=0$, the only possible elements are $E_{++}$ and $E_{--}$, and the definition forces

$$
E_{++}=\Pi_{+},\qquad E_{--}=\Pi_{-}.
$$

So the Peirce basis is the pair $\{\Pi_{+},\Pi_{-}\}$.

## Existence and Uniqueness

**Theorem.** The Peirce basis exists and is unique.

**Proof.** The diagonal line $\mathbb{B}_{++}=\mathbb{C}\Pi_{+}$ contains the two idempotents $0$ and $\Pi_{+}$; a basis element is nonzero, so it is $\Pi_{+}$. The same argument gives $E_{--}=\Pi_{-}$. The product rule holds because $\Pi_{+}\Pi_{-}=0$ and $\Pi_{\pm}^{2}=\Pi_{\pm}$. There is no other choice, because there is no other line.

**There is no gauge.** In the general theory two bases differ by $E_{\sigma\tau}\mapsto t_{\sigma}t_{\tau}^{-1}E_{\sigma\tau}$. Here the only entries are diagonal, and the replacement reads

$$
E_{\sigma\sigma}\longmapsto t_{\sigma}t_{\sigma}^{-1}E_{\sigma\sigma}=E_{\sigma\sigma}.
$$

The formula is defined but acts trivially. The effective gauge is the trivial group.

## The Coordinates

Every element is

$$
\breve Q=\breve Q_{+}E_{++}+\breve Q_{-}E_{--},\qquad \breve Q_{\pm}=u\pm v.
$$

The coordinate array is diagonal:

$$
\begin{pmatrix}\breve Q_{+}&0\\0&\breve Q_{-}\end{pmatrix}.
$$

The product is the componentwise product,

$$
(\breve Q_{+},\breve Q_{-})(\breve R_{+},\breve R_{-})=(\breve Q_{+}\breve R_{+},\breve Q_{-}\breve R_{-}),
$$

which is the matrix product of the diagonal arrays. The coordinates are the idempotent coordinates of the algebra, and no choice entered their definition.

## The Dimension Count

**The family.** The idempotents of $\mathbb{B}_{\mathrm r}\cong\mathbb{C}\times\mathbb{C}$ are $(0,0)$, $(1,0)$, $(0,1)$ and $(1,1)$. The nontrivial complete orthogonal pairs are $(\Pi_{+},\Pi_{-})$ and $(\Pi_{-},\Pi_{+})$, the same unordered family, with the two labelings exchanged by $j\mapsto-j$. The unordered family space is a single point.

**The frame.** The Peirce basis is unique, so the frame space is a single point.

**The gauge.** The gauge is trivial, of dimension $0$.

**The count.**

$$
0=0+0 .
$$

The automorphism group of $\mathbb{B}_{\mathrm r}$ is $\{1,\varsigma\}$ with $\varsigma(j)=-j$; it has order $2$ and swaps the two lines. It fixes the unordered family and acts on the two labelings. There is no continuous parameter, no torus and no projective family.

## What the Basis Is Not

The basis is not a choice. In the nondegenerate case the word *basis* names a selection inside each line, and the selection carries a gauge; here the selection is forced and the gauge is trivial. The word remains correct, because the two units satisfy the product rule and span the algebra, but it carries no freedom.

The basis is not a second decomposition. The lines are the decomposition; the two idempotents are the only nonzero elements available.

## Summary

The Peirce basis of the reduced biquaternion algebra is the pair $\{\Pi_{+},\Pi_{-}\}$, and it is unique. Every element is $\breve Q=\breve Q_{+}\Pi_{+}+\breve Q_{-}\Pi_{-}$ with $\breve Q_{\pm}=u\pm v$, the coordinate array is diagonal, and the product is componentwise. The gauge is trivial, the dimension count is $0=0+0$, and the only symmetry is $j\mapsto-j$, which swaps the two lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The two idempotents |
| $E_{++}=\Pi_{+}$, $E_{--}=\Pi_{-}$ | The Peirce basis |
| $\breve Q_{\pm}=u\pm v$ | The coordinates |
| $\varsigma(j)=-j$ | The nontrivial automorphism |

## Further Reading

- [The Peirce Decomposition of the Reduced Biquaternion Algebra](the-peirce-decomposition-of-the-reduced-biquaternion-algebra.html), for the lines and their multiplication.
- [Spinors as Peirce Coordinates in the Reduced Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-reduced-biquaternion-algebra.html), for the degenerate spinor.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the nondegenerate case and the gauge.
