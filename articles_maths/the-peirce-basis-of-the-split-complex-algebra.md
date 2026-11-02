# __The Peirce Basis of the Split-Complex Algebra__

## Introduction

The Peirce decomposition of the split-complex algebra has two diagonal lines and no mixed line. A Peirce basis is therefore the pair of the two idempotents, $\Pi_{+}$ and $\Pi_{-}$, and it is canonical: there is no element to choose, no gauge and no freedom. This article states the basis, proves its uniqueness, gives the coordinates and records the degenerate dimension count.

It assumes *The Peirce Decomposition of the Split-Complex Algebra*. The spinors are *Spinors as Peirce Coordinates in the Split-Complex Algebra*.

## The Definition

**Definition.** A **Peirce basis** of $\mathbb{D}$ relative to the family $\Pi_{+},\Pi_{-}$ is a family $E_{\sigma\tau}\in\mathbb{D}_{\sigma\tau}$, one element for each pair, with

$$
E_{\sigma\tau}E_{\mu\nu}=\delta_{\tau\mu}E_{\sigma\nu},\qquad E_{\sigma\sigma}=\Pi_{\sigma}.
$$

**The off-diagonal elements do not exist.** Since $\mathbb{D}_{+-}=\mathbb{D}_{-+}=0$, the only possible elements are $E_{++}$ and $E_{--}$, and the definition forces

$$
E_{++}=\Pi_{+},\qquad E_{--}=\Pi_{-}.
$$

So the Peirce basis is the pair $\{\Pi_{+},\Pi_{-}\}$.

## Existence and Uniqueness

**Theorem.** The Peirce basis exists and is unique.

**Proof.** The diagonal line $\mathbb{D}_{++}=\mathbb{R}\Pi_{+}$ contains the two idempotents $0$ and $\Pi_{+}$; a basis element is nonzero, so it is $\Pi_{+}$. The same argument gives $E_{--}=\Pi_{-}$. The product rule is satisfied because $\Pi_{+}\Pi_{-}=0$ and $\Pi_{\pm}^{2}=\Pi_{\pm}$. There is no other choice, because there is no other line.

**There is no gauge.** In the general theory two bases of the same family differ by $E_{\sigma\tau}\mapsto t_{\sigma}t_{\tau}^{-1}E_{\sigma\tau}$. Here the only entries are diagonal, and the replacement reads

$$
E_{\sigma\sigma}\longmapsto t_{\sigma}t_{\sigma}^{-1}E_{\sigma\sigma}=E_{\sigma\sigma}.
$$

The formula is defined but acts trivially. The effective gauge is the trivial group.

## The Coordinates

Every element is

$$
Q=Q_{+}E_{++}+Q_{-}E_{--},\qquad Q_{\pm}=q\pm q'.
$$

The coordinate array is diagonal:

$$
\begin{pmatrix}Q_{+}&0\\0&Q_{-}\end{pmatrix}.
$$

The product is the componentwise product,

$$
(Q_{+},Q_{-})(R_{+},R_{-})=(Q_{+}R_{+},Q_{-}R_{-}),
$$

which is the matrix product of the diagonal arrays. The coordinates are the idempotent coordinates of the algebra, and no choice entered their definition.

## The Dimension Count

**The family.** The idempotents of $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ are $(0,0)$, $(1,0)$, $(0,1)$ and $(1,1)$. The nontrivial complete orthogonal pairs are $(\Pi_{+},\Pi_{-})$ and $(\Pi_{-},\Pi_{+})$, which are the same unordered family, with the two labelings exchanged by $j\mapsto-j$. The unordered family space is a single point.

**The frame.** The Peirce basis is unique, so the frame space is a single point.

**The gauge.** The gauge is trivial, of dimension $0$.

**The count.** The orbit–stabiliser count degenerates:

$$
0=0+0 .
$$

The automorphism group of $\mathbb{D}$ is $\{1,\varsigma\}$ with $\varsigma(j)=-j$; it has order $2$ and swaps the two lines. It fixes the unordered family and acts on the two labelings. There is no continuous parameter, no torus and no projective family.

## What the Basis Is Not

The basis is not a choice. In the nondegenerate case the word *basis* names a selection inside each line, and the selection carries a gauge; here the selection is forced, and the gauge is trivial. The word is still correct, because the two units satisfy the product rule and span the algebra, but it carries no freedom.

The basis is not a second decomposition. The lines are the decomposition; the two idempotents are the only nonzero elements available.

## Summary

The Peirce basis of the split-complex algebra is the pair $\{\Pi_{+},\Pi_{-}\}$, and it is unique. Every element is $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ with $Q_{\pm}=q\pm q'$, the coordinate array is diagonal, and the product is componentwise. The gauge is trivial, the dimension count is $0=0+0$, and the only symmetry is $j\mapsto-j$, which swaps the two lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The two idempotents |
| $E_{++}=\Pi_{+}$, $E_{--}=\Pi_{-}$ | The Peirce basis |
| $Q_{\pm}=q\pm q'$ | The coordinates |
| $\varsigma(j)=-j$ | The nontrivial automorphism |

## Further Reading

- [The Peirce Decomposition of the Split-Complex Algebra](the-peirce-decomposition-of-the-split-complex-algebra.html), for the lines and their multiplication.
- [Spinors as Peirce Coordinates in the Split-Complex Algebra](spinors-as-peirce-coordinates-in-the-split-complex-algebra.html), for the degenerate spinor.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the nondegenerate case and the gauge.
