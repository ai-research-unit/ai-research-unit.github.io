# __The Peirce Basis of $M_4(\mathbb{C})$__

## Introduction

The Peirce cut of $M_4(\mathbb{C})$ gives $16$ lines and no element inside the mixed ones. A **Peirce basis** selects one nonzero element in each line, with the matrix-unit product rule. The diagonal elements are forced; the mixed elements are not, and their freedom is the **gauge**.

This article proves that the basis exists, computes the gauge, gives the coordinates, and reads the count $15=12+3$ as an orbit–stabiliser count. It assumes *The Peirce Decomposition of $M_4(\mathbb{C})$*.

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

## The Gauge

**Theorem.** Two Peirce bases of the same family differ by

$$
E'_{kl}=t_kt_l^{-1}E_{kl},\qquad t_1,\dots,t_4\in\mathbb{C}^{\times}.
$$

Conversely, every such choice is a Peirce basis of the same family.

**Proof.** Each primed element is a nonzero multiple of the unprimed one, $E'_{kl}=c_{kl}E_{kl}$. The product rule gives $c_{kl}c_{lq}=c_{kq}$, so $c_{kl}=c_{k1}c_{1l}$. From $c_{1l}c_{l1}=c_{11}=1$ and $c_{11}=1$, set $t_k=c_{k1}$; then $c_{kl}=t_kt_l^{-1}$. The converse is a direct check.

**The effective gauge.** A common scalar acts trivially, since $(\lambda t_k)(\lambda t_l)^{-1}=t_kt_l^{-1}$. The effective group is

$$
(\mathbb{C}^{\times})^{4}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{4-1},
$$

of complex dimension $3$. The coordinates transform by

$$
X'_{kl}=t_k^{-1}t_lX_{kl}.
$$

In the Hermitian case the gauge is restricted to $|t_k|=1$, of real dimension $3$.

**The second root is not extra data.** In the biquaternion case $n=2$ a second root is sometimes used to name the mixed units. It is one way to fix the gauge, not a parameter beyond the basis: a different second root changes $E_{kl}$ by the allowed rescaling.

## The Count

**The spaces.** The family space is the set of ordered $4$-tuples of lines summing to $\mathbb{C}^{4}$; the gauge is the fibre of the map from bases to families; the frame space is the set of Peirce bases modulo the common scale.

**The dimensions.**

$$
\dim_{\mathbb{C}}(\text{families})=12,\qquad
\dim_{\mathbb{C}}(\text{gauge})=3,\qquad
\dim_{\mathbb{C}}(\text{frames})=15 .
$$

**The orbit–stabiliser reading.** $PGL_4(\mathbb{C})$ acts transitively on the family space, and the stabiliser of a family is the diagonal torus modulo the scalars, of dimension $3$. Hence

$$
\dim PGL_4=15=12+3 .
$$

In real dimensions the count is $30=24+6$.

**The projective reading.** A family is an ordered $4$-tuple of points of $\mathbb{P}^{4-1}$ in general position. A Peirce basis is a lift of that tuple to a basis of $\mathbb{C}^{4}$, and the gauge is the freedom of the lift, one scale per point modulo the common scale. The family is the orbit; the gauge is the stabiliser; the basis is a point of the total space.

## What the Basis Is Not

The basis is not canonical: two bases of the same family differ by the gauge. It is not a second decomposition: the lines are the cut, and the $E_{kl}$ are one element per line. It is not a list of spinors: the units are elements of the algebra, while a spinor is a column of coordinates.

## Summary

A Peirce basis of $M_4(\mathbb{C})$ is a choice $E_{kl}\in A_{kl}$ with $E_{kl}E_{pq}=\delta_{lp}E_{kq}$ and $E_{kk}=P_k$. It exists, and it is unique up to $E_{kl}\mapsto t_kt_l^{-1}E_{kl}$, a torus of dimension $3$. The coordinates multiply by the matrix product and transform by $X_{kl}\mapsto t_k^{-1}t_lX_{kl}$. The family has dimension $12$, the gauge $3$, the frame $15$, and the count is the orbit–stabiliser count of $PGL_4$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_k$ | A member of the family |
| $A_{kl}$ | The Peirce line |
| $E_{kl}$ | The chosen element of $A_{kl}$ |
| $X_{kl}$ | The Peirce coordinate |
| $t_k$ | A gauge parameter |
| $PGL_4(\mathbb{C})$ | The group of the family space |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce units and the gauge.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the lines and the rule.
- [Spinors as Peirce Coordinates in $M_4(\mathbb{C})$](spinors-as-peirce-coordinates-in-m4c.html), for the columns of the array.
- [The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m4c.html), for the simple nilpotents and the same torus.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the general statement.
