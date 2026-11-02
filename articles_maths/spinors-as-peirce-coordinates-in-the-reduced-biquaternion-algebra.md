# __Spinors as Peirce Coordinates in the Reduced Biquaternion Algebra__

## Introduction

In the reduced biquaternion algebra the Peirce coordinates are the two idempotent coordinates $\breve Q_{+}$ and $\breve Q_{-}$. A column of the coordinate array has one nonzero entry, because the mixed Peirce lines vanish. A spinor is therefore a single complex scalar, and it carries no gauge, no chirality and no half-angle.

This article states the coordinates, the columns and the degenerate spinor. It assumes *The Peirce Decomposition of the Reduced Biquaternion Algebra* and *The Peirce Basis of the Reduced Biquaternion Algebra*.

## The Coordinates and the Columns

Every element is

$$
\breve Q=\breve Q_{+}\Pi_{+}+\breve Q_{-}\Pi_{-},\qquad \breve Q_{\pm}=u\pm v .
$$

The coordinate array is diagonal, and the two columns are

$$
\psi^{(+)}=(\breve Q_{+},0),\qquad \psi^{(-)}=(0,\breve Q_{-}).
$$

Each column has one nonzero entry. The vanishing of the other entry is not a choice: it is the vanishing of the mixed Peirce component $\mathbb{B}_{+-}=0$.

## The Spinor

**Definition.** A **spinor** is the tuple of the two coordinates of one column. In this algebra it is

$$
(\breve Q_{+},0)\quad\text{or}\quad(0,\breve Q_{-}),
$$

equivalently the single nonzero scalar $\breve Q_{+}$ or $\breve Q_{-}$.

**There is no gauge.** The basis $\{\Pi_{+},\Pi_{-}\}$ is canonical, so the coordinates are determined by the element and no rescaling is available. The overall factor of a column is not a gauge parameter here; it is the value of the scalar. The spinor is the coordinate itself, not a projective class.

**The two columns are the two factors.** The column of index $+$ is the coordinate on $\mathbb{C}\Pi_{+}$, and the column of index $-$ is the coordinate on $\mathbb{C}\Pi_{-}$. The pair $(\breve Q_{+},\breve Q_{-})$ is the element $\breve Q$; a column is one of its two coordinates.

## No Chirality

A chiral split of a column requires two columns of the same row, one for each sign of a grading. Here each row has only one nonzero entry, so there is nothing to split. The two rows belong to the two factors of $\mathbb{B}_{\mathrm r}\cong\mathbb{C}\times\mathbb{C}$; they are not two chiralities of one spinor.

**The element is not a two-component spinor.** The pair $(\breve Q_{+},\breve Q_{-})$ has two components, but it is the element of the algebra, not a column. Calling it a spinor would identify the element with one of its columns, which the decomposition does not do.

## No Half-Angle

The family is a single unordered pair, with no continuous parameter: the only nontrivial idempotents are $\Pi_{+}$ and $\Pi_{-}$, and the only symmetry is $j\mapsto-j$. There is no path of families, no torus of gauges and no lift to a double cover. A half-angle has no place in this layer.

## What a Spinor Is Not

A spinor is not an element of $\mathbb{B}_{\mathrm r}$; the element is the pair of the two coordinates. It is not a two-component object; it is a single scalar attached to one diagonal line. It is not a projective class, because there is no gauge. It is a coordinate in the canonical Peirce basis.

## Summary

The Peirce coordinates of the reduced biquaternion algebra are $\breve Q_{\pm}=u\pm v$, and the two columns are $(\breve Q_{+},0)$ and $(0,\breve Q_{-})$. A spinor is one of these columns, equivalently the single complex scalar $\breve Q_{+}$ or $\breve Q_{-}$. The basis is canonical, the gauge is trivial, there is no chiral split and no half-angle. The pair $(\breve Q_{+},\breve Q_{-})$ is the element, not a spinor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q_{\pm}=u\pm v$ | The Peirce coordinates |
| $\psi^{(\pm)}$ | The column of index $\pm$ |
| $\Pi_{\pm}$ | The idempotents, the basis units |

## Further Reading

- [The Peirce Decomposition of the Reduced Biquaternion Algebra](the-peirce-decomposition-of-the-reduced-biquaternion-algebra.html), for the lines and the root of $1$.
- [The Peirce Basis of the Reduced Biquaternion Algebra](the-peirce-basis-of-the-reduced-biquaternion-algebra.html), for the canonical basis.
- [Spinors as Peirce Coordinates in $n$ Dimensions](spinors-as-peirce-coordinates-in-n-dimensions.html), for the nondegenerate case.
