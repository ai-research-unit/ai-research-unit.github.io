# __The Peirce Basis of $M_4(\mathbb{C})$__

## Introduction

The Peirce cut of $M_4(\mathbb{C})$ gives $16$ lines and no element inside the mixed ones. A **Peirce basis** selects one nonzero element in each line, with the matrix-unit product rule. The diagonal elements are forced; the mixed elements are not, and their freedom is the **frame group**.

This article proves that the basis exists, computes the frame group, gives the coordinates, and reads the count $15=12+3$ as an orbit–stabiliser count. It assumes *The Peirce Decomposition of $M_4(\mathbb{C})$*.

## The Definition

**Definition.** A **Peirce basis** relative to the family $P_1,\dots,P_4$ is a family $E_{kl}\in A_{kl}$ with

$$
E_{kl}E_{pq}=\delta_{lp}E_{kq},\qquad E_{kk}=P_k .
$$

**The diagonal is forced.** Since $A_{kk}=\mathbb{C}P_k$, a nonzero diagonal element is $cP_k$; idempotence gives $c^{2}=c$, hence $c=1$. So $E_{kk}=P_k$ is a consequence of the rule, not an extra normalisation.

**The mixed elements are a choice.** A nonzero $E_{kl}\in A_{kl}$ can be rescaled, and the rescalings are constrained by the rule.

## Existence

**Theorem.** Every complete family of 4 nonzero idempotents of $M_4(\mathbb{C})$ admits a Peirce basis.

**Proof.** Choose $v_k$ spanning $V_k=\operatorname{im}P_k$ and $\ell_l$ with $\ell_l(v_k)=\delta_{kl}$, and set $E_{kl}=v_k\ell_l$. Then $E_{kl}\in A_{kl}$, $E_{kk}=v_k\ell_k=P_k$, and

$$
E_{kl}E_{pq}=v_k\ell_l(v_p)\ell_q=\delta_{lp}E_{kq}.
$$

So the $16$ elements are a basis.

**The basis is a pair of dual bases.** The vectors $v_1,\dots,v_4$ are a basis of $\mathbb{C}^{4}$ and the forms $\ell_1,\dots,\ell_4$ are the dual basis. The Peirce basis is that pair written as matrices.

## Coordinates

Every element has a unique expansion

$$
X=\sum_{k,l=1}^{4}X_{kl}E_{kl},
$$

and the numbers $X_{kl}$ are its **Peirce coordinates**. If $Y=\sum Y_{kl}E_{kl}$, then

$$
XY=\sum_{k,q}\Bigl(\sum_{l=1}^{4}X_{kl}Y_{lq}\Bigr)E_{kq},
$$

so in a Peirce basis the algebra reads as the array of coordinates with the matrix product. The array is the element, not a new object.

## The Indefinite Form

**Theorem.** Two Peirce bases of the same family differ by

$$
E'_{kl}=t_kt_l^{-1}E_{kl},\qquad t_1,\dots,t_4\in\mathbb{C}^{\times}.
$$

Conversely, every such choice is a Peirce basis of the same family.

**Proof.** Each primed element is a nonzero multiple of the unprimed one, $E'_{kl}=c_{kl}E_{kl}$. The product rule gives $c_{kl}c_{lq}=c_{kq}$, so $c_{kl}=c_{k1}c_{1l}$. From $c_{1l}c_{l1}=c_{11}=1$ and $c_{11}=1$, set $t_k=c_{k1}$; then $c_{kl}=t_kt_l^{-1}$. The converse is a direct check.

**The effective frame group.** A common scalar acts trivially, since $(\lambda t_k)(\lambda t_l)^{-1}=t_kt_l^{-1}$. The effective group is

$$
(\mathbb{C}^{\times})^{4}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{4-1},
$$

of complex dimension $3$. The coordinates transform by

$$
X'_{kl}=t_k^{-1}t_lX_{kl}.
$$

In the Hermitian case the frame group is restricted to $|t_k|=1$, of real dimension $3$.

**The biquaternion case adds no parameter beyond the frame group.** At $n=2$ the biquaternion article names the mixed units by choosing one nonzero element of a mixed line, the partner being fixed by the normalisation; the freedom is the reciprocal rescaling. An involution anticommuting with the root names the same normalised pair in one symbol, so it is a way to write the frame point, not a datum beyond the basis.

## The Count

**The spaces.** The family space is the set of ordered $4$-tuples of lines summing to $\mathbb{C}^{4}$; the frame group is the fibre of the map from bases to families; the frame space is the set of Peirce bases modulo the common scale.

**The dimensions.**

$$
\dim_{\mathbb{C}}(\text{families})=12,\qquad
\dim_{\mathbb{C}}(\text{frame group})=3,\qquad
\dim_{\mathbb{C}}(\text{frames})=15 .
$$

**The orbit–stabiliser reading.** $PGL_4(\mathbb{C})$ acts transitively on the family space, and the stabiliser of a family is the diagonal torus modulo the scalars, of dimension $3$. Hence

$$
\dim PGL_4=15=12+3 .
$$

In real dimensions the count is $30=24+6$.

**The projective reading.** A family is an ordered $4$-tuple of points of $\mathbb{P}^{4-1}$ in general position. A Peirce basis is a lift of that tuple to a basis of $\mathbb{C}^{4}$, and the frame group is the freedom of the lift, one scale per point modulo the common scale. The family is the orbit; the frame group is the stabiliser; the basis is a point of the total space.

## What the Basis Is Not

The basis is not canonical: two bases of the same family differ by the frame group. It is not a second decomposition: the lines are the cut, and the $E_{kl}$ are one element per line. It is not a list of spinors: the units are elements of the algebra, while a spinor is a column of coordinates.

## Summary

A Peirce basis of $M_4(\mathbb{C})$ is a choice $E_{kl}\in A_{kl}$ with $E_{kl}E_{pq}=\delta_{lp}E_{kq}$ and $E_{kk}=P_k$. It exists, and it is unique up to $E_{kl}\mapsto t_kt_l^{-1}E_{kl}$, a torus of dimension $3$. The coordinates multiply by the matrix product and transform by $X_{kl}\mapsto t_k^{-1}t_lX_{kl}$. The family has dimension $12$, the frame group $3$, the frame $15$, and the count is the orbit–stabiliser count of $PGL_4$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_k$ | A member of the family |
| $A_{kl}$ | The Peirce line |
| $E_{kl}$ | The chosen element of $A_{kl}$ |
| $X_{kl}$ | The Peirce coordinate |
| $t_k$ | A frame parameter |
| $PGL_4(\mathbb{C})$ | The group of the family space |

## Further Reading

- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the coefficient basis, the four left matrices and the transpose as the quaternion conjugation.
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the matrix units, the sixteen two-sided operators and the caveat on the two bases.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce units and the gauge.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the lines and the rule.
- [Spinors as Coordinates in $M_4(\mathbb{C})$](spinors-as-coordinates-in-m4c.html), for the columns of the array.
- [The Frame, the Simple Nilpotents and the Frame Group of $M_4(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-frame-group-of-m4c.html), for the simple nilpotents and the same torus.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the general statement.
