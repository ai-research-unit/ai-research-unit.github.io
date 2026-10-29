# __Spinors as Peirce Coordinates in $M_3(\mathbb{C})$__

## Introduction

A Peirce basis turns an element of $M_3(\mathbb{C})$ into a $3\times3$ array of coordinates. A **column** of that array is a tuple of $3$ scalars, and this tuple is the **spinor** of the family in the basis. The column is the coordinate form of an element of the left space $M_3P_l\cong\mathbb{C}^{3}$; left multiplication acts on it by the matrix of the element.

The choice of column rather than row is fixed by the action. This article defines the spinor, computes the gauge action, gives the projective reading, the Hermitian norm and the chiral split, and states the weight of the chain. It assumes *The Peirce Decomposition of $M_3(\mathbb{C})$* and *The Peirce Basis of $M_3(\mathbb{C})$*.

## The Column

Every element is

$$
X=\sum_{k,l=1}^{3}X_{kl}E_{kl},
$$

and for fixed $l$ the **column** is

$$
\psi^{(l)}=(X_{1l},\dots,X_{3 l}).
$$

A **spinor** is a column up to a common nonzero factor.

**Why a column.** Left multiplication by $A=\sum A_{rs}E_{rs}$ gives

$$
(AX)_{rl}=\sum_{s=1}^{3}A_{rs}X_{sl},
$$

so the column is multiplied by the matrix $A$. The column is the space on which the left action acts, that is, the coordinate form of $M_3P_l\cong\mathbb{C}^{3}$. Right multiplication acts on the rows instead. The corpus attaches the spinor to the left action, so the coordinate form is a column.

**The spinor is not the whole element.** The element is the full array, the sum of its $3$ columns. A column is the coordinate vector of the component of $X$ in the left space $M_3P_l$; that component is a matrix, but the column itself is not closed under multiplication.

## The Gauge

**Proposition.** Under $E'_{kl}=t_kt_l^{-1}E_{kl}$ the coordinates transform by $X'_{kl}=t_k^{-1}t_lX_{kl}$, so after multiplying the column by $t_l^{-1}$ the entries transform by

$$
\psi_k\longmapsto t_k^{-1}\psi_k .
$$

**Proof.** The coordinate law is that of *The Peirce Basis of $M_3(\mathbb{C})$*. Multiplying the column by $t_l^{-1}$ removes the factor $t_l$ and leaves $t_k^{-1}$ on the $k$-th entry.

The effective group is $(\mathbb{C}^{\times})^{3-1}$: the common rescaling of all entries is the overall factor of the column, which is not part of the spinor.

## The Projective Reading

A spinor up to scale is a point of $\mathbb{P}^{3-1}$,

$$
[\psi]=[\psi_1:\cdots:\psi_3].
$$

On the open set where every entry is nonzero, the gauge acts transitively: given $[\psi]$ and $[\varphi]$, the scalars $t_k=\psi_k/\varphi_k$ send one to the other. So the orbit of a spinor with no zero entry is the whole open set, and the only invariant of a single spinor is its zero pattern.

**Invariants need a cycle.** A product of coordinates around a closed cycle is gauge invariant:

$$
X_{k_1k_2}X_{k_2k_3}\cdots X_{k_mk_1}\longmapsto\Bigl(\prod_r t_{k_r}^{-1}t_{k_{r+1}}\Bigr)X_{k_1k_2}\cdots X_{k_mk_1}=X_{k_1k_2}\cdots X_{k_mk_1}.
$$

A single column has no invariant of this kind unless it closes through a row of another element. The invariant content of the construction lies in the element, not in one column.

## The Hermitian Norm

If the family and the basis are Hermitian, the gauge is $|t_k|=1$, and

$$
\sum_{k=1}^{3}|\psi_k|^{2}\longmapsto\sum_{k=1}^{3}|\psi_k|^{2}.
$$

The norm is gauge invariant, and the orbit is the set of spinors with the same moduli.

## The Chiral Split

A grading is an algebra automorphism $\Gamma$ with $\Gamma^{2}=1$ that commutes with the family. It preserves each line and acts on $A_{kl}$ by $\varepsilon_k\varepsilon_l$ with $\varepsilon_k=\pm1$, so a column splits into the entries with $\varepsilon_k=+1$ and those with $\varepsilon_k=-1$.

For $n=3$ the order of $H$ is $3$, so no power of $H$ is an involution. A grading that commutes with the family is $\operatorname{Ad}_S$ with $S=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)$ and $\sigma_k=\pm1$; its sign pattern has $p$ plus signs and $3-p$ minus signs. The balanced split does not exist. The possible splits are $1+2$, and each depends on the choice of $S$. The decomposition itself supplies no chirality.

A balanced split of a column needs an even number of entries, and a sign function with $n/2$ signs of each type. For odd $n$ no balanced split exists; a split $p+q$ still exists if a sign function is chosen, but it is not canonical. The split is data on the lines, not a consequence of the cut.

## The Spin of the Column

The chain of the frame acts on the column by left multiplication. Its generator is

$$
J_3=\sum_{k=1}^{3}\Bigl(\frac{3+1}{2}-k\Bigr)E_{kk},
$$

and on the column the entries have the $3$ distinct weights $\frac{3-1}{2},\frac{3-3}{2},\dots,-\frac{3-1}{2}$. The column is therefore the irreducible space of spin

$$
j=\frac{3-1}{2}=1 .
$$

This is the highest-weight computation read on the spinor: the highest weight of $J_3=h/2$ on the left space $M_3P_l$. For $n=2$ it gives $j=\tfrac12$ and the column is the two-component spinor. For $n=3$ it gives $1$ and the column has $2j+1=3$ components.

The column has three entries. Under the chain, $J_3$ has weights $1,0,-1$, so the column is the highest-weight-two space. This is the first case in which the Peirce spinor is not a two-component object: it has three components, and the word *spinor* names a coordinate column, not a highest-weight-one state.

## The Half-Angle

The Peirce spinor carries no half-angle. A half-angle requires two further choices: a one-parameter path of families generated by rotations, and a lift of that path to a double cover of the rotation group. Neither is part of the Peirce data. The polar-operator articles make both choices; their half-angle is a statement about the path and the lift. At a fixed family there is no angle, and the spinor is a column of coordinates.

## What a Spinor Is Not

A spinor is not an arbitrary element of $M_3(\mathbb{C})$; it is one column of the coordinates of an element. It is not a Peirce line; it is a tuple of coordinates on $3$ of them. It is not gauge invariant; only the element and its cycle invariants are. It is not the pair of all columns; that is the element.

## Summary

The Peirce coordinates of $X$ are the numbers $X_{kl}$ in $X=\sum X_{kl}E_{kl}$, and a spinor is a column $(X_{1l},\dots,X_{3 l})$ up to scale. The gauge sends $\psi_k\mapsto t_k^{-1}\psi_k$, with effective group $(\mathbb{C}^{\times})^{3-1}$; projectively the orbit is fixed by the zero pattern; in the Hermitian gauge the norm is invariant. Under the chain the column is the highest-weight-two space, so the number of components is $3=2j+1$. A balanced chiral split exists only for even $n$, and the half-angle is a path-and-lift parameter, not a Peirce object.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X_{kl}$ | The Peirce coordinate |
| $\psi^{(l)}$ | The column of index $l$, a spinor |
| $t_k$ | A gauge parameter |
| $J_3$ | The chain generator |
| $j$ | The spin, $(3-1)/2$ |

## Further Reading

- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the lines.
- [The Peirce Basis of $M_3(\mathbb{C})$](the-peirce-basis-of-m3c.html), for the units and the gauge.
- [Spinors as Peirce Coordinates in $n$ Dimensions](spinors-as-peirce-coordinates-in-n-dimensions.html), for the general statement.
