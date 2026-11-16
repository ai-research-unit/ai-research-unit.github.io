# __The Peirce Basis in $n$ Dimensions__

## Introduction

The Peirce decomposition of $M_{n}(\mathbb{C})$ relative to a complete family of $n$ idempotents gives $n^{2}$ lines and no element inside the mixed ones. A **Peirce basis** is a choice of one nonzero element in each line, normalised so that the chosen elements multiply by the matrix-unit rule. The basis is not part of the decomposition: the decomposition is canonical given the family, while the basis is a choice, and the freedom of the choice is the **Peirce gauge**.

The article proves that a Peirce basis exists, that it is unique up to the gauge, and that the gauge is a torus of dimension $n-1$. It identifies the basis with a system of matrix units, proves that two such systems are conjugate by an invertible element unique up to the centre, gives the coordinates of an element in the basis, the dimension count of the families and of the frames, and the projective reading of the construction. It assumes *The Peirce Decomposition in $n$ Dimensions*.

## The Definition

**Definition.** Let $A_{kl}=P_{k}M_{n}(\mathbb{C})P_{l}$ be the Peirce lines of a complete family $P_{1},\dots,P_{n}$. A **Peirce basis** is a family $E_{kl}\in A_{kl}$, one element for each pair $(k,l)$, such that

$$
E_{kl}E_{pq}=\delta_{lp}E_{kq},\qquad E_{kk}=P_{k}.
$$

**The diagonal is forced.** Since $A_{kk}=\mathbb{C}P_{k}$, an element of the diagonal line is $E_{kk}=c_{k}P_{k}$. The product rule with $k=l=p=q=k$ gives $c_{k}^{2}=c_{k}$, and the element is nonzero, so $c_{k}=1$. The condition $E_{kk}=P_{k}$ is therefore a consequence of the product rule and of the choice of a nonzero element in each diagonal line, not an extra normalisation.

**The basis is a set of elements, not a set of subspaces.** The lines are the decomposition; the elements $E_{kl}$ are a selection inside them. The selection is what the word *basis* names.

## Existence

**Theorem.** Every complete family of $n$ idempotents in $M_{n}(\mathbb{C})$ admits a Peirce basis.

**Proof.** Let $V_{k}=\operatorname{im}P_{k}$. Choose $v_{k}\in V_{k}$ nonzero, and let $\ell_{k}$ be the linear form with $\ell_{k}(v_{l})=\delta_{kl}$. Set

$$
E_{kl}=v_{k}\ell_{l}.
$$

Then $E_{kl}\in\mathbb{C}\,v_{k}\ell_{l}=A_{kl}$ and $E_{kk}=v_{k}\ell_{k}=P_{k}$. For the product,

$$
E_{kl}E_{pq}=v_{k}\ell_{l}(v_{p})\ell_{q}=\delta_{lp}\,v_{k}\ell_{q}=\delta_{lp}E_{kq}.
$$

So the $E_{kl}$ are a Peirce basis.

**The basis is a pair of dual bases.** The vectors $v_{1},\dots,v_{n}$ are a basis of $\mathbb{C}^{n}$, one vector in each line $V_{k}$, and the forms $\ell_{1},\dots,\ell_{n}$ are the dual basis. The Peirce basis $E_{kl}=v_{k}\ell_{l}$ is the same data written as matrices. Conversely, every Peirce basis arises this way: $E_{kl}$ has rank one, its image is $V_{k}$, and its kernel is $\bigoplus_{p\ne l}V_{p}$, so it is $v_{k}\ell_{l}$ for the vector $v_{k}=E_{kl}(\text{any vector of }V_{l})$ and the form $\ell_{l}$ with that kernel.

## Coordinates

**Definition.** The **Peirce coordinates** of $X\in M_{n}(\mathbb{C})$ in the basis are the numbers $X_{kl}$ in

$$
X=\sum_{k,l=1}^{n}X_{kl}E_{kl}.
$$

They are unique, because the $E_{kl}$ are a basis of the algebra: the lines sum directly.

**The product is the matrix product of the coordinates.** If $X=\sum X_{kl}E_{kl}$ and $Y=\sum Y_{kl}E_{kl}$, then

$$
XY=\sum_{k,l,p,q}X_{kl}Y_{pq}E_{kl}E_{pq}
=\sum_{k,q}\Big(\sum_{l}X_{kl}Y_{lq}\Big)E_{kq}.
$$

So the coordinate of $XY$ in position $(k,q)$ is $\sum_{l}X_{kl}Y_{lq}$. In a Peirce basis the algebra reads as the array of its coordinates with the matrix product. This is a statement about coordinates, not a new object: the array is the element written in the chosen basis.

## The Gauge

**Theorem.** Let $E$ and $E'$ be two Peirce bases of the same family. Then there are nonzero scalars $t_{1},\dots,t_{n}$ with

$$
E'_{kl}=t_{k}t_{l}^{-1}E_{kl}.
$$

Conversely, every such choice gives a Peirce basis of the same family.

**Proof.** Both $E'_{kl}$ and $E_{kl}$ span the same line $A_{kl}$, so $E'_{kl}=c_{kl}E_{kl}$ with $c_{kl}\ne0$. The product rule gives

$$
c_{kl}c_{lq}E_{kq}=E'_{kl}E'_{lq}=E'_{kq}=c_{kq}E_{kq},
$$

hence $c_{kl}c_{lq}=c_{kq}$. Since $E'_{11}=c_{11}P_{1}$ is idempotent and nonzero, $c_{11}=1$. Setting $t_{k}=c_{k1}$ gives $c_{kl}=c_{k1}c_{1l}=t_{k}c_{1l}$. From $c_{1l}c_{l1}=c_{11}=1$ and $c_{l1}=t_{l}$, we get $c_{1l}=t_{l}^{-1}$. So $c_{kl}=t_{k}t_{l}^{-1}$. The converse is a direct check of the product rule. 

**The gauge group.** The scalars $t_{k}$ form $(\mathbb{C}^{\times})^{n}$, but a common scalar acts trivially, since $(\lambda t_{k})(\lambda t_{l})^{-1}=t_{k}t_{l}^{-1}$. The effective group is

$$
(\mathbb{C}^{\times})^{n}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{n-1},
$$

the **Peirce gauge**. It acts on the coordinates by

$$
X'_{kl}=t_{k}^{-1}t_{l}X_{kl},
$$

because $X'_{kl}E'_{kl}=X_{kl}E_{kl}$ and $E'_{kl}=t_{k}t_{l}^{-1}E_{kl}$.

**The Hermitian case.** If the family is Hermitian, $P_{k}^{*}=P_{k}$, a Hermitian Peirce basis has $E_{lk}=E_{kl}^{*}$. In the form $E_{kl}=v_{k}v_{l}^{*}$, with $v_{k}$ a unit vector, this is automatic, and the gauge is restricted to $|t_{k}|=1$. The gauge group is then $(S^{1})^{n-1}$.

## The Corners

**A Peirce corner is a line $A_{kl}$, and the basis takes one element from each of the $n^{2}$ corners.** The word is the one used in the biquaternion articles, where the four lines $\mathbb{B}_{++},\mathbb{B}_{+-},\mathbb{B}_{-+},\mathbb{B}_{--}$ are called the four corners. In $M_{n}(\mathbb{C})$ there are $n^{2}$ of them.

**The diagonal corners and the off-diagonal corners behave differently.** The diagonal corner $A_{kk}=\mathbb{C}P_{k}$ contains exactly two idempotents, $0$ and $P_{k}$, and the basis takes the nonzero one: $E_{kk}=P_{k}$, canonical once the family is fixed. An off-diagonal corner $A_{kl}$, $k\ne l$, contains no idempotent, since $A_{kl}^{2}=0$; the basis takes a nilpotent $E_{kl}$, and the choice is free up to the gauge. So the basis is fixed on the $n$ diagonal corners and chosen on the $n^{2}-n$ off-diagonal ones.

**The product of two basis elements names a third corner.** The rule $E_{kl}E_{pq}=\delta_{lp}E_{kq}$ says that the product of the element of the corner $(k,l)$ with the element of the corner $(p,q)$ is the element of the corner $(k,q)$ when $l=p$, and is zero otherwise. In the corner language of *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*, the corners are the summands $A_{kl}=\operatorname{Hom}(V_{l},V_{k})$ and the composites are the products of maps.

## Systems of Matrix Units

**Definition.** A **system of $n\times n$ matrix units** in $M_{n}(\mathbb{C})$ is a family $E_{kl}$, one element for each pair $(k,l)$, with

$$
E_{kl}E_{pq}=\delta_{lp}E_{kq},\qquad E_{kk}=P_{k}.
$$

A Peirce basis is exactly such a system: the definition of §*The Definition* and this one are the same list of conditions. The coordinate map of §*Coordinates* sends the system to the $n^{2}$ elementary matrices, so a system of matrix units is the same data as an isomorphism $M_{n}(\mathbb{C})\to M_{n}(\mathbb{C})$ carrying the family to the standard diagonal family.

**Uniqueness up to conjugation.** Every two systems of $n\times n$ matrix units of $M_{n}(\mathbb{C})$ are conjugate by an invertible element, and the conjugating unit is unique up to the centre.

*Proof.* By the Skolem–Noether theorem every automorphism of $M_{n}(\mathbb{C})$ is inner, so it is enough to compare each system with the standard one. The data $(v_{k})$, $(\ell_{k})$ of §*Existence* give $E_{kl}=v_{k}\ell_{l}$; two bases $v$ and $v'$ of $\mathbb{C}^{n}$ differ by an invertible $U$ with $Uv_{k}=v'_{k}$, and then $UE_{kl}U^{-1}=v'_{k}\ell'_{l}=E'_{kl}$. If $U$ and $U'$ both carry the system to the same one, then $U^{-1}U'$ commutes with every $E_{kl}$, hence with the whole algebra, since the invertibles span it, so it is a scalar. The conjugating unit is therefore unique up to the centre.

**The biquaternion instance.** At $n=2$ the four elements $\tilde\Pi_{+},\vec\Upsilon_{+-},\vec\Upsilon_{-+},\tilde\Pi_{-}$ are a system of $2\times2$ matrix units, and the theorem above is the one proved in *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*, §*Systems of Matrix Units*. There the two proofs differ in style only: the biquaternion article conjugates into $M_{2}(\mathbb{C})$ and uses that every automorphism of $M_{2}(\mathbb{C})$ is inner, which is the same Skolem–Noether step.

## Dimensions and the Projective Count

**The three spaces.** Three sets are attached to the construction:

- the **family space**, the set of ordered $n$-tuples of lines $V_{1},\dots,V_{n}$ with $V_{1}\oplus\cdots\oplus V_{n}=\mathbb{C}^{n}$;
- the **frame space**, the set of Peirce bases;
- the **gauge**, the fibre of the map from frames to families over a fixed family.

**The dimensions.** The family space is an open subset of $(\mathbb{P}^{n-1})^{n}$, so

$$
\dim_{\mathbb{C}}(\text{families})=n(n-1)=n^{2}-n .
$$

The gauge is $(\mathbb{C}^{\times})^{n-1}$, of dimension $n-1$. The frame space is the total space, of dimension

$$
(n^{2}-n)+(n-1)=n^{2}-1 .
$$

**The orbit and the stabiliser.** The group $PGL_{n}(\mathbb{C})$ acts on the family space, and it acts transitively: a family is a projective frame, and $PGL_{n}$ sends one projective frame to any other. The family is therefore the orbit, and its dimension is $n^{2}-n$. The stabiliser of a family is the diagonal torus modulo the scalars, of dimension $n-1$: an element of $PGL_{n}$ that fixes each line acts on the $n$ lines by $n$ scalars, and the common scalar is the identity of $PGL_{n}$. The gauge is this stabiliser. The count is the orbit–stabiliser count of the frame space:

$$
\dim PGL_{n}=n^{2}-1=(n^{2}-n)+(n-1).
$$

For $n=3$ it reads $8=6+2$: the frame space has dimension $8$, the family $6$, and the gauge $2$. The family is the orbit, and the gauge is the stabiliser.

**The projective reading.** A family is $n$ points of $\mathbb{P}^{n-1}$ in general position, that is, a projective frame. A Peirce basis is a lift of that projective frame to a basis of $\mathbb{C}^{n}$, and the gauge is the freedom of the lift: each point may be rescaled independently, with the common rescaling of all $n$ points acting trivially. The decomposition is the projective data; the basis is the lift.

**The biquaternion layer.** For $n=2$ the same count is $3=2+1$ in complex dimensions, that is, $6=4+2$ in real dimensions. The family has four real parameters and the gauge two. The extra datum used in the biquaternion articles is a point of the gauge, not an extra parameter.

## What the Basis Is Not

The basis is not canonical. Two bases of the same family differ by the gauge, and the gauge is nontrivial for $n\ge2$.

The basis is not a second decomposition. The lines are the decomposition; the $E_{kl}$ are one element per line, and the choice does not change the lines.

The basis exists only when the components are lines. A coarse family, with a component of dimension greater than one, has no Peirce basis: a component of dimension $d>1$ carries a whole space of elements, and no single element spans it.

## Summary

A Peirce basis is a choice of one nonzero element in each Peirce line, with $E_{kl}E_{pq}=\delta_{lp}E_{kq}$ and $E_{kk}=P_{k}$. It exists for every complete family of $n$ idempotents of $M_{n}(\mathbb{C})$, and it is unique up to the gauge $E_{kl}\mapsto t_{k}t_{l}^{-1}E_{kl}$, a torus of dimension $n-1$. A basis is the same data as a system of matrix units, and two systems are conjugate by an invertible element unique up to the centre. In the basis the coordinates multiply by the matrix product, and the coordinates change by $X_{kl}\mapsto t_{k}^{-1}t_{l}X_{kl}$. The family space has dimension $n^{2}-n$, the gauge $n-1$, and the frame space $n^{2}-1$, which is the orbit–stabiliser count of $PGL_{n}$; for $n=3$ it is $8=6+2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{k}$ | A member of the complete orthogonal family |
| $A_{kl}=P_{k}M_{n}P_{l}$ | The Peirce line |
| $E_{kl}$ | The chosen element of $A_{kl}$ |
| $X_{kl}$ | The Peirce coordinate of $X$ |
| $t_{k}$ | A gauge parameter, $t_{k}\ne0$ |
| $V_{k}=\operatorname{im}P_{k}$ | The line of the $k$-th idempotent |
| $PGL_{n}$ | The projective linear group, of dimension $n^{2}-1$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions and the invertibles of a fine decomposition.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for matrix units and the matrix product of coordinates.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the lines and their multiplication.
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the case $n=2$ of §*Systems of Matrix Units*.
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for the normalised pair $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$.
- [Spinors as Peirce Coordinates in $n$ Dimensions](spinors-as-peirce-coordinates-in-n-dimensions.html), for the rows of the coordinate array.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-mnc.html), for the frame and the nilpotents.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m3c.html), for the orbit–stabiliser count at $n=3$.
