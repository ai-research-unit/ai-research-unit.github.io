# __Spinors as Peirce Coordinates in $n$ Dimensions__

## Introduction

A Peirce basis turns an element of $M_{n}(\mathbb{C})$ into an $n\times n$ array of coordinates. A column of that array is an $n$-tuple of scalars, and this tuple is what the corpus calls a **spinor** of the family in the basis. The definition is a definition of coordinates: the spinor is not an element of the algebra, not a line of the decomposition and not an invariant object. It depends on the family, on the basis, and on the gauge.

The article defines the Peirce coordinates and the spinor, computes the action of the gauge on a spinor, gives the projective reading, the Hermitian norm and the condition under which a column splits into two chiralities, and states where a half-angle can enter. It assumes the two preceding articles, *The Peirce Decomposition in $n$ Dimensions* and *The Peirce Basis in $n$ Dimensions*.

## The Coordinates

Let $P_{1},\dots,P_{n}$ be a complete family, $A_{kl}$ its Peirce lines, and $E_{kl}$ a Peirce basis. Every element has a unique expansion

$$
X=\sum_{k,l=1}^{n}X_{kl}E_{kl},\qquad X_{kl}\in\mathbb{C}.
$$

The numbers $X_{kl}$ are the **Peirce coordinates** of $X$. The first index is the row and the second the column. The coordinate $X_{kl}$ lies on the line $A_{kl}$: it is the coefficient of the chosen element of that line.

## The Column and the Spinor

**Definition.** For fixed $l$, the **column** of $X$ is the $n$-tuple

$$
\psi^{(l)}=(X_{1l},\dots,X_{nl}).
$$

A **spinor** of the family, in the basis, is a column of the coordinate array, taken up to a common nonzero factor.

The common factor is not a physical parameter. Multiplying the whole column by $\lambda$ multiplies each coordinate by $\lambda$, and this is the same kind of redundancy as the overall scale of a vector: the column describes the component of $X$ on the lines $A_{1l},\dots,A_{nl}$, and only the ratios of its entries are meaningful once the basis is fixed.

**Why a column and not a row.** Left multiplication by $A$ acts on $X$ by

$$
(AX)_{rl}=\sum_{s=1}^{n}A_{rs}X_{sl},
$$

so the column $(X_{1l},\dots,X_{nl})$ is multiplied by the matrix $A$. The column is the space on which the left action acts, that is, the coordinate form of the space $M_{n}P_{l}\cong\mathbb{C}^{n}$. Right multiplication acts on the rows instead. The corpus attaches the spinor to the left action, so its coordinate form is a column.

**The spinor is not an element of the algebra.** The element is the full array $X$, which is the sum of $n$ columns. A column alone is not closed under multiplication: the product of two elements sums over the inner index, so a column of $X$ and a row of $Y$ meet in a single coordinate. The spinor is one column of the description, not a subalgebra and not a subspace of $M_{n}(\mathbb{C})$.

**The column is attached to the right index.** The index $l$ names the right idempotent $P_{l}$, that is, the line on the right of every entry of the column. The entries $X_{1l},\dots,X_{nl}$ lie on the lines $A_{1l},\dots,A_{nl}$, one per left idempotent.

## The Gauge Action

**Proposition.** Under the gauge $E'_{kl}=t_{k}t_{l}^{-1}E_{kl}$, the coordinates transform by

$$
X'_{kl}=t_{k}^{-1}t_{l}X_{kl},
$$

so, after multiplying the column by the common factor $t_{l}^{-1}$, the entries transform by

$$
\psi_{k}\longmapsto t_{k}^{-1}\psi_{k}.
$$

**Proof.** The coordinate law was proved in *The Peirce Basis in $n$ Dimensions*: $X'_{kl}=t_{k}^{-1}t_{l}X_{kl}$. Multiplying the column by $t_{l}$ removes the factor $t_{l}$ and leaves the factor $t_{k}^{-1}$ on the $k$-th entry.

**The effective gauge on a spinor is $(n-1)$-dimensional.** The scalars $t_{1},\dots,t_{n}$ act on the entries by independent rescalings, and a common rescaling of all entries is the overall factor of the column, which is not part of the spinor. The effective group is therefore $(\mathbb{C}^{\times})^{n}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{n-1}$.

## The Projective Reading

Because the overall factor is removed, a spinor is a point of the projective space $\mathbb{P}^{n-1}$:

$$
[\psi]=[\psi_{1}:\cdots:\psi_{n}].
$$

The gauge acts on this point by the diagonal torus $(\mathbb{C}^{\times})^{n-1}$, and the action is not trivial. A single spinor therefore carries very little gauge-invariant information.

**The orbit is determined by the zero entries.** On the open set where every entry is nonzero, the torus acts transitively: given $[\psi]$ and $[\varphi]$ with all entries nonzero, the scalars $t_{k}=\psi_{k}/\varphi_{k}$ send one to the other. So the gauge orbit of a spinor with no zero entry is the whole open set, and the only invariant of a single spinor is the set of indices $l$ for which $\psi_{l}=0$. In particular, no ratio $\psi_{j}/\psi_{l}$ is gauge invariant: it is multiplied by $t_{j}/t_{l}$.

**Invariants need a cycle.** A product of coordinates around a closed cycle is gauge invariant:

$$
X_{k_{1}k_{2}}X_{k_{2}k_{3}}\cdots X_{k_{m}k_{1}}
\longmapsto
\Big(\prod_{r}t_{k_{r}}^{-1}t_{k_{r+1}}\Big)X_{k_{1}k_{2}}\cdots X_{k_{m}k_{1}}
=X_{k_{1}k_{2}}\cdots X_{k_{m}k_{1}}.
$$

A single coordinate is not invariant, and a column alone has no invariant product of this kind unless it closes through a row of another element. The invariant content of the construction lies in the element $X$, not in one of its rows.

## The Hermitian Gauge and the Norm

If the family is Hermitian and the basis is Hermitian, the gauge is $|t_{k}|=1$. In that case

$$
\sum_{l=1}^{n}\lvert\psi_{l}\rvert^{2}
\longmapsto
\sum_{l=1}^{n}\lvert t_{l}\rvert^{2}\lvert\psi_{l}\rvert^{2}
=\sum_{l=1}^{n}\lvert\psi_{l}\rvert^{2},
$$

so the Hermitian norm of a spinor is gauge invariant. The gauge orbit of a spinor is then the set of spinors with the same moduli $\lvert\psi_{1}\rvert,\dots,\lvert\psi_{n}\rvert$, and a spinor is described by its point of the sphere modulo the torus of phases.

No other quadratic invariant exists: a quadratic form in the entries is invariant under $(\mathbb{C}^{\times})^{n-1}$ only when it is a sum of terms $\lvert\psi_{l}\rvert^{2}$ with equal coefficients, that is, a multiple of the norm.

## Chirality

A column of length $n$ has no canonical split into two blocks. A split requires an extra grading: an algebra automorphism $\Gamma$ with $\Gamma^{2}=1$ that commutes with every $P_{k}$.

**Proposition.** Let $\Gamma$ be an algebra automorphism with $\Gamma^{2}=1$ and $\Gamma P_{k}=P_{k}\Gamma$ for every $k$. Then $\Gamma$ acts on each line $A_{kl}$ by a sign $\varepsilon_{k}\varepsilon_{l}$, with $\varepsilon_{k}=\pm1$, and it splits each column into the entries with $\varepsilon_{k}=+1$ and those with $\varepsilon_{k}=-1$.

**Proof.** Since $\Gamma$ commutes with $P_{k}$, it preserves the line $A_{kl}$, so it acts on it by a scalar. On the diagonal line $A_{kk}=\mathbb{C}P_{k}$ the scalar is $\varepsilon_{k}$, because $\Gamma(P_{k})$ is an idempotent in the same line and is nonzero. On $A_{kl}$ the scalar is $\varepsilon_{k}\varepsilon_{l}^{-1}=\varepsilon_{k}\varepsilon_{l}$, by the product rule and $\varepsilon_{l}^{2}=1$. The column of index $l$ then splits according to the sign $\varepsilon_{k}$ of each row.

So a chirality is a choice of signs $\varepsilon_{1},\dots,\varepsilon_{n}$, one per line, and the split of a column is the partition of its entries into the two signs. A balanced split, with $n/2$ entries of each sign, exists only for even $n$. It is not canonical: the sign function is extra data. In $M_{4}(\mathbb{C})$ and $M_{6}(\mathbb{C})$ the root supplies it, and the columns split $2+2$ and $3+3$. In $M_{3}(\mathbb{C})$ and $M_{5}(\mathbb{C})$ no balanced split exists, and the column is not chiral in the balanced sense.

## What a Spinor Is Not

A spinor is not the whole element of $M_{n}(\mathbb{C})$, not a Peirce line, and not an invariant of the algebra. It is the coordinate column of the component of $X$ in the left space $M_{n}P_{l}$, taken up to the overall factor of the column. Changing the basis changes it by the gauge; changing the family changes the decomposition and the tuple. The invariant object is the element $X$; the spinor is one row of its description.

## Summary

The Peirce coordinates of $X$ are the numbers $X_{kl}$ in $X=\sum X_{kl}E_{kl}$, and a spinor is a column $(X_{1l},\dots,X_{nl})$ up to a common factor. The gauge sends $X_{kl}\mapsto t_{k}^{-1}t_{l}X_{kl}$, so a spinor transforms by $\psi_{k}\mapsto t_{k}^{-1}\psi_{k}$ up to the overall factor, with effective group $(\mathbb{C}^{\times})^{n-1}$. Projectively, the orbit of a spinor with no zero entry is the whole open set, and the only invariant of a single spinor is its zero pattern; invariant products are cycles of coordinates. In the Hermitian gauge the norm is invariant. A chiral split of a column requires an extra sign function on the lines, balanced only for even $n$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X_{kl}$ | The Peirce coordinate of $X$ in position $(k,l)$ |
| $\psi^{(l)}$ | The column of index $l$, a spinor |
| $t_{k}$ | A gauge parameter, $t_{k}\ne0$ |
| $\Gamma$ | A grading, an automorphism with $\Gamma^{2}=1$ commuting with the family |
| $\varepsilon_{k}=\pm1$ | The sign of $\Gamma$ on the line $V_{k}$ |
| $H$ | A root of $1$ of order two, when the family is so parametrised |

## Further Reading

- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the lines and the family.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the choice of the units and the gauge.
- [The Peirce Coordinates](peirce-coordinates-and-companion-nilpotents.html), for the coordinates in the one-idempotent case.
- [The Two-Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the chiral split at $n=4$.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the adjoint action on the frame, which is a different construction.
