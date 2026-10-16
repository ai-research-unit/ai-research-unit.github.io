# __Worked Examples in the Biquaternion Algebra__

## Introduction

This article works the computations of the biquaternion algebra out on explicit elements. The aim is a reference of concrete facts: the multiplication table of the basis, the remarkable subspaces exhibited on one element, the four conjugations applied to that element, and explicit zero-divisor pairs. The idempotents and the minimal left ideals are the general subject of *Square Roots of One and the Idempotents of the Biquaternion Algebra*; here they are only exhibited. The **physical interpretation** is attached to each computation, so that the dictionary of *The Four-Vector Element Representation of Biquaternions* and of *Conventions in the Biquaternion Universe* can be checked arithmetically.

**Notation.** A biquaternion is written in developed form
$$
\tilde{Q}=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3,\qquad Q_\mu\in\mathbb{C},
$$
with the quaternion basis $e_0=1,e_1,e_2,e_3$ and the central complex unit $i$, $i^2=-1$, commuting with every $e_\mu$. The scalar part is $\mathrm{Sc}\,\tilde{Q}=Q_0$, the vector part is $\vec Q=Q_1e_1+Q_2e_2+Q_3e_3$, and the quaternion conjugate is $\tilde{Q}^{\natural}=Q_0e_0-\vec Q$. The fixed element used throughout is
$$
\tilde{Q}=(2+i)e_0+(1-i)e_1+3e_2+ie_3 .
$$

## The Multiplication Table

The products of the quaternion basis elements follow the cyclic rule $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, with $e_k^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$:

| | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

The table is the quaternion table, but the coefficients are now complex and the central element $i$ multiplies every entry. As a $\mathbb{C}$-algebra the dimension is $4$; as a real algebra the basis may be taken as $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ and the dimension is $8$.

In physics these eight real components are the eight real numbers a general element carries, and the four complex components $Q_\mu=q_\mu+iq'_\mu$ split each into a "material" and an "informational" part according to the sector dictionary: the coefficients of an element of the material sector are pure imaginary in the time slot and real in the space slots, and conversely for the informational sector.

## Remarkable Subspaces on a Concrete Element

The remarkable real subspaces are the fixed and anti-fixed spaces of the three commuting involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}={}^{\natural}\circ\bar{\cdot}$; the fourth conjugation $\flat=-{}^{*}$ has the same two eigenspaces as ${}^{*}$ with the roles exchanged, so it contributes no further subspaces. On the fixed element:

| Subspace | Defining condition | Component of $\tilde{Q}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | $\tilde{Q}^{\natural}=\tilde{Q}$ | $(2+i)e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | $\tilde{Q}^{\natural}=-\tilde{Q}$ | $(1-i)e_1+3e_2+ie_3$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | $\tilde{Q}^{*}=\tilde{Q}$ | $2e_0+e_1+3e_2$ |
| $i\mathbb{H}_{\mathbb{B}}$ (anti-quaternion) | $\tilde{Q}^{*}=-\tilde{Q}$ | $ie_0-ie_1+ie_3$ |
| $\mathbb{M}_+$ (Hermitian) | $\tilde{Q}^{*}=\tilde{Q}$ | $2e_0-ie_1+ie_3$ |
| $\mathbb{M}_-$ (anti-Hermitian) | $\tilde{Q}^{\flat}=\tilde{Q}$ | $ie_0+e_1+3e_2$ |

The scalar-vector decomposition reads $\tilde{Q}=(2+i)e_0+\bigl((1-i)e_1+3e_2+ie_3\bigr)$, and the quaternion-anti-quaternion decomposition reads
$$
\tilde{Q}=\bigl(2e_0+e_1+3e_2\bigr)+i\bigl(e_0-e_1+e_3\bigr)=\tilde{Q}_r+i\tilde{Q}_i .
$$
The Hermitian decomposition reads
$$
\tilde{Q}=\bigl(2e_0-ie_1+ie_3\bigr)+\bigl(ie_0+e_1+3e_2\bigr)=\tilde{Q}_++\tilde{Q}_-,
$$
and the two pieces are distinguished by the signs: $\tilde{Q}_+$ has real scalar part and purely imaginary vector part — the **informational sector** — while $\tilde{Q}_-$ has purely imaginary scalar part and real vector part — the **material sector**.

**Physical interpretation.** One element is read at once as four numbers: the real part of $\tilde{Q}_-$ is $3$ in the space slots together with an imaginary time slot, exactly the form $ict\,e_0+\vec x$ of a material four-position, while $\tilde{Q}_+$ is of the form $ct'\,e_0+i\vec x'$ of an informational four-position. The example therefore shows the sector exchange on a single element: it carries both a material and an informational four-vector. The norm and the inverse of the element are computed below; the time and space slots are $Q_0$ and $Q_1,Q_2,Q_3$ throughout.

## The Four Conjugations on the Concrete Element

Applying the four conjugations to $\tilde{Q}=(2+i)e_0+(1-i)e_1+3e_2+ie_3$ gives
$$
\tilde{Q}^{\natural}=(2+i)e_0-(1-i)e_1-3e_2-ie_3,
$$
$$
\tilde{Q}^{*}=(2-i)e_0+(1+i)e_1+3e_2-ie_3,
$$
$$
\tilde{Q}^{*}=\tilde{Q}^{\natural}\bar{\cdot}=(2-i)e_0-(1+i)e_1-3e_2+ie_3,
$$
$$
\tilde{Q}^{\flat}=-\tilde{Q}^{*}=-(2-i)e_0+(1+i)e_1+3e_2-ie_3 .
$$
Each is an involution, and the Klein group is visible in $\tilde{Q}^{*}=\tilde{Q}^{\natural}\bar{\cdot}=\tilde{Q}^{*{}^{\natural}}$; the fourth conjugation satisfies $(\tilde{Q}^{*})^{\flat}=-\tilde{Q}$, so it is the composition of ${}^{*}$ with the central sign $-1$. The fixed points of each involution give the remarkable subspaces above: for instance the Hermitian part of $\tilde{Q}$ is $\tfrac12(\tilde{Q}+\tilde{Q}^{*})=2e_0-ie_1+ie_3$, which agrees with the table.

**Physical interpretation.** The quaternion conjugation reverses the spatial part and leaves the time slot, so it is the **spatial reversal** of the four-vector; the complex conjugation conjugates the coefficients $Q_\mu=q_\mu+iq'_\mu$, so it exchanges the material and informational interpretations of each slot and is the **sector exchange**; the Hermitian conjugation is the composition, the adjoint of a four-vector, and it is the involution that selects the observables.

## Idempotents and the Two Minimal Left Ideals

The standard idempotents $\tilde\Pi_+=\tfrac12(e_0+ie_3)$ and $\tilde\Pi_-=\tfrac12(e_0-ie_3)$ satisfy $\tilde\Pi_+^2=\tilde\Pi_+$, $\tilde\Pi_-^2=\tilde\Pi_-$, $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$ and $\tilde\Pi_++\tilde\Pi_-=e_0$; they are primitive, and they give the decomposition $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ into two minimal left ideals of real dimension $4$. Here $ie_3$ is a root of $+1$, $(ie_3)^2=e_0$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

**Physical interpretation.** The two idempotents are the **chiral projectors** onto the two Weyl components, and the decomposition $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ is the splitting of the algebra into the two chiralities (*Modules over the Biquaternion Algebra*).

## The Norm and the Inverse of the Concrete Element

The norm and the inverse are the two quantities every physics calculation of the framework needs, and they are worth exhibiting on the fixed element. With $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$,

$$
\langle\tilde{Q}\rangle_{\natural}=(2+i)^2+(1-i)^2+3^2+i^2=(3+4i)+(-2i)+9-1=11+2i ,
$$

which is nonzero, so $\tilde{Q}$ is a unit, with inverse
$$
\tilde{Q}^{-1}=\frac{\tilde{Q}^{\natural}}{\langle\tilde{Q}\rangle_{\natural}}=\frac{(2+i)e_0-(1-i)e_1-3e_2-ie_3}{11+2i}.
$$

The element is neither purely material nor purely informational: its norm is complex with both parts nonzero, so it does not lie on either real sector and is not null. The material part $\tilde{Q}_-$ of the Hermitian decomposition has norm $\langle\tilde{Q}_-\rangle_{\natural}=\sum_\mu(Q_-)_\mu^2=(i)^2+1+9=i^2+10=9$, a spacelike interval in the $ict$ coordinate; the informational part has norm $\langle\tilde{Q}_+\rangle_{\natural}=4+(-i)^2+(i)^2=4-1-1=2$.

**Physical interpretation.** The norm $11+2i$ measures the element; its vanishing would be the light cone and its being real would be membership of a real sector. The example shows the generic case: a unit with a complex norm, whose material and informational halves have separately real intervals.

## Explicit Zero Divisors

**Example (an explicit pair).** With the standard idempotents, $\tilde\Pi_+\tilde\Pi_-=0$ with both factors nonzero. In unnormalised form, set $\tilde A=e_0+ie_3$ and $\tilde B=e_0-ie_3$. Then
$$
\tilde A\tilde B=e_0-(ie_3)^2=e_0-1=0,\qquad \tilde A\neq0,\qquad \tilde B\neq0 .
$$
Both $\tilde A$ and $\tilde B$ have two nonzero complex coefficients. Moreover $\langle\tilde A\rangle_{\natural}=1+i^2=0$, so $\tilde A$ is **null** as well as a zero divisor; it is not nilpotent, since $\tilde A^2=(e_0+ie_3)^2=e_0+2ie_3-(e_3)^2=2e_0+2ie_3=2\tilde A\neq0$.

**Physical interpretation.** The pair $\tilde A=e_0+ie_3$, $\tilde B=e_0-ie_3$ is a **lightlike pair**: each is null, $N=0$, so each is a light-cone element, and their product vanishes. This is the algebraic content of the light cone: two null elements whose product is zero are the two null directions of a lightlike plane. The element $\tilde A$ being null but not nilpotent is the statement that a lightlike direction squares to a multiple of itself and not to zero; the genuinely nilpotent directions are the pure null vectors, such as $e_1+ie_2$, whose square vanishes (*Zero Divisors of the Biquaternion Algebra*).

## Physical Readings

The computations read as the framework's calibration set. The multiplication table is the product law of the physical objects; the remarkable subspaces exhibited on one element are the interpretations of one four-vector; the four conjugations applied to it are the four forms; and the idempotents are the pure states. Read as a calibration, the article is where the vocabulary of the series is checked against a single element, so it is also the place where the interpretations of the other articles can be tested against one another.

## Summary

The multiplication of $\mathbb{B}$ is the quaternion table with complex coefficients and central $i$, $i^2=-1$. On the element $\tilde{Q}=(2+i)e_0+(1-i)e_1+3e_2+ie_3$ the remarkable subspaces are exhibited by the scalar-vector, quaternion-anti-quaternion and Hermitian-anti-Hermitian decompositions of $\tilde{Q}$, and the four conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat}=-{}^{*}$ act on it as listed. The element has norm $\langle\tilde{Q}\rangle_{\natural}=11+2i$, so it is a unit with $\tilde{Q}^{-1}=\tilde{Q}^{\natural}/(11+2i)$; its material part has norm $9$ and its informational part norm $2$. The idempotents $\tilde\Pi_+,\tilde\Pi_-$ satisfy $\tilde\Pi_+\tilde\Pi_-=0$ and give $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ with each summand minimal; the pair $\tilde A=e_0+ie_3$, $\tilde B=e_0-ie_3$ is an explicit zero-divisor pair, both factors null.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ | Developed form, $Q_\mu\in\mathbb{C}$ |
| $i$ | Central complex unit, $i^2=-1$ |
| $\mathrm{Sc}\,\tilde{Q}=Q_0$, $\vec Q=\sum_{k=1}^3Q_ke_k$ | Scalar and vector parts |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}={}^{\natural}\circ\bar{\cdot}$, ${}^{\flat}=-{}^{*}$ | The four conjugations |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | The remarkable subspaces |
| $\tilde\Pi_+=\tfrac12(e_0+ie_3),\ \tilde\Pi_-=\tfrac12(e_0-ie_3)$ | Orthogonal primitive idempotents; chiral projectors |
| $\langle\tilde{Q}\rangle_{\natural}=11+2i$ | Norm of the fixed element; nonzero, so a unit |
| $\tilde{Q}^{-1}=\tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$ | Inverse of the fixed element |
| $\tilde A=e_0+ie_3,\ \tilde B=e_0-ie_3$ | Null zero-divisor pair, $\tilde A\tilde B=0$ |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the quaternion and biquaternion computations.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents and minimal left ideals in the structure theory of finite-dimensional algebras.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for idempotents, minimal ideals and the decomposition of a ring into simple modules.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2nd ed. 2001), for the complexification of the quaternions and the null cone.
