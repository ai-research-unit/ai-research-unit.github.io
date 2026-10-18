# __Worked Examples in the Biquaternion Algebra__

## Introduction

This article works the computations of the biquaternion algebra out on explicit elements. The aim is a reference of concrete facts: the multiplication table of the basis, the remarkable subspaces exhibited on one element, the four conjugations applied to that element, and explicit zero-divisor pairs. The idempotents and the minimal left ideals are the general subject of *Square Roots of One and the Idempotents of the Biquaternion Algebra*; here they are only exhibited. The **physical interpretation** is attached to each computation, so that the dictionary of *The Four-Vector Element Representation of Biquaternions* and of *Conventions in the Biquaternion Universe* can be checked arithmetically.

**Notation.** A biquaternion is written in developed form
$$
\tilde{Q}=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu\in\mathbb{C},
$$
with the quaternion basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and the central complex unit $i$, $i^2=-1$, commuting with every $e_\mu$. The scalar part is $\mathrm{Sc}\,\tilde{Q}=Q_t$, the vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and the quaternion conjugate is $\tilde{Q}^{\natural}=Q_te_t-\vec Q$. The fixed element used throughout is
$$
\tilde{Q}=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z .
$$

## The Multiplication Table

The products of the quaternion basis elements follow the cyclic rule $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$, with $\vec e_\mu^2=-e_t$ and $\vec e_\mu \vec e_\nu=-\vec e_\nu \vec e_\mu$ for $\mu\neq\nu$:

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

The table is the quaternion table, but the coefficients are now complex and the central element $i$ multiplies every entry. As a $\mathbb{C}$-algebra the dimension is $4$; as a real algebra the basis may be taken as $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ and the dimension is $8$.

In physics these eight real components are the eight real numbers a general element carries, and the four complex components $Q_\mu=q_\mu+iq'_\mu$ split each into a "material" and an "informational" part according to the sector dictionary: the coefficients of an element of the material sector are pure imaginary in the time slot and real in the space slots, and conversely for the informational sector.

## Remarkable Subspaces on a Concrete Element

The remarkable real subspaces are the fixed and anti-fixed spaces of the three commuting involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}={}^{\natural}\circ\bar{\cdot}$; the fourth conjugation $\flat=-{}^{*}$ has the same two eigenspaces as ${}^{*}$ with the roles exchanged, so it contributes no further subspaces. On the fixed element:

| Subspace | Defining condition | Component of $\tilde{Q}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | $\tilde{Q}^{\natural}=\tilde{Q}$ | $(2+i)e_t$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | $\tilde{Q}^{\natural}=-\tilde{Q}$ | $(1-i)\vec e_x+3\vec e_y+i\vec e_z$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | $\tilde{Q}^{*}=\tilde{Q}$ | $2e_t+\vec e_x+3\vec e_y$ |
| $i\mathbb{H}_{\mathbb{B}}$ (anti-quaternion) | $\tilde{Q}^{*}=-\tilde{Q}$ | $ie_t-i\vec e_x+i\vec e_z$ |
| $\mathbb{M}_+$ (Hermitian) | $\tilde{Q}^{*}=\tilde{Q}$ | $2e_t-i\vec e_x+i\vec e_z$ |
| $\mathbb{M}_-$ (anti-Hermitian) | $\tilde{Q}^{\flat}=\tilde{Q}$ | $ie_t+\vec e_x+3\vec e_y$ |

The scalar-vector decomposition reads $\tilde{Q}=(2+i)e_t+\bigl((1-i)\vec e_x+3\vec e_y+i\vec e_z\bigr)$, and the quaternion-anti-quaternion decomposition reads
$$
\tilde{Q}=\bigl(2e_t+\vec e_x+3\vec e_y\bigr)+i\bigl(e_t-\vec e_x+\vec e_z\bigr)=\tilde{Q}_r+i\tilde{Q}_i .
$$
The Hermitian decomposition reads
$$
\tilde{Q}=\bigl(2e_t-i\vec e_x+i\vec e_z\bigr)+\bigl(ie_t+\vec e_x+3\vec e_y\bigr)=\tilde{Q}_++\tilde{Q}_-,
$$
and the two pieces are distinguished by the signs: $\tilde{Q}_+$ has real scalar part and purely imaginary vector part — the **informational sector** — while $\tilde{Q}_-$ has purely imaginary scalar part and real vector part — the **material sector**.

**Physical interpretation.** One element is read at once as four numbers: the real part of $\tilde{Q}_-$ is $3$ in the space slots together with an imaginary time slot, exactly the form $ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ of a material four-position, while $\tilde{Q}_+$ is of the form $ct'\,e_t+i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ of an informational four-position. The example therefore shows the sector exchange on a single element: it carries both a material and an informational four-vector. The norm and the inverse of the element are computed below; the time and space slots are $Q_t$ and $Q_x,Q_y,Q_z$ throughout.

## The Four Conjugations on the Concrete Element

Applying the four conjugations to $\tilde{Q}=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$ gives
$$
\tilde{Q}^{\natural}=(2+i)e_t-(1-i)\vec e_x-3\vec e_y-i\vec e_z,
$$
$$
\tilde{Q}^{*}=(2-i)e_t+(1+i)\vec e_x+3\vec e_y-i\vec e_z,
$$
$$
\tilde{Q}^{*}=\tilde{Q}^{\natural}\bar{\cdot}=(2-i)e_t-(1+i)\vec e_x-3\vec e_y+i\vec e_z,
$$
$$
\tilde{Q}^{\flat}=-\tilde{Q}^{*}=-(2-i)e_t+(1+i)\vec e_x+3\vec e_y-i\vec e_z .
$$
Each is an involution, and the Klein group is visible in $\tilde{Q}^{*}=\tilde{Q}^{\natural}\bar{\cdot}=\tilde{Q}^{*{}^{\natural}}$; the fourth conjugation satisfies $(\tilde{Q}^{*})^{\flat}=-\tilde{Q}$, so it is the composition of ${}^{*}$ with the central sign $-1$. The fixed points of each involution give the remarkable subspaces above: for instance the Hermitian part of $\tilde{Q}$ is $\tfrac12(\tilde{Q}+\tilde{Q}^{*})=2e_t-i\vec e_x+i\vec e_z$, which agrees with the table.

**Physical interpretation.** The quaternion conjugation reverses the spatial part and leaves the time slot, so it is the **spatial reversal** of the four-vector; the complex conjugation conjugates the coefficients $Q_\mu=q_\mu+iq'_\mu$, so it exchanges the material and informational interpretations of each slot and is the **sector exchange**; the Hermitian conjugation is the composition, the adjoint of a four-vector, and it is the involution that selects the observables.

## Idempotents and the Two Minimal Left Ideals

The standard idempotents $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ satisfy $\tilde\Pi_+^2=\tilde\Pi_+$, $\tilde\Pi_-^2=\tilde\Pi_-$, $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$; they are primitive, and they give the decomposition $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ into two minimal left ideals of real dimension $4$. Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

**Physical interpretation.** The two idempotents correspond to the **chiral projectors** onto the two Weyl components, and the decomposition $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ is the splitting of the algebra into the two chiralities (*Modules over the Biquaternion Algebra*).

## The Norm and the Inverse of the Concrete Element

The norm and the inverse are the two quantities every physics calculation of the framework needs, and they are worth exhibiting on the fixed element. With $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$,

$$
\langle\tilde{Q}\rangle_{\natural}=(2+i)^2+(1-i)^2+3^2+i^2=(3+4i)+(-2i)+9-1=11+2i ,
$$

which is nonzero, so $\tilde{Q}$ is a unit, with inverse
$$
\tilde{Q}^{-1}=\frac{\tilde{Q}^{\natural}}{\langle\tilde{Q}\rangle_{\natural}}=\frac{(2+i)e_t-(1-i)\vec e_x-3\vec e_y-i\vec e_z}{11+2i}.
$$

The element is neither purely material nor purely informational: its norm is complex with both parts nonzero, so it does not lie on either real sector and is not null. The material part $\tilde{Q}_-$ of the Hermitian decomposition has norm $\langle\tilde{Q}_-\rangle_{\natural}=\sum_\mu(Q_-)_\mu^2=(i)^2+1+9=i^2+10=9$, a spacelike interval in the $ict$ coordinate; the informational part has norm $\langle\tilde{Q}_+\rangle_{\natural}=4+(-i)^2+(i)^2=4-1-1=2$.

**Physical interpretation.** The norm $11+2i$ measures the element; its vanishing would be the light cone and its being real would be membership of a real sector. The example shows the generic case: a unit with a complex norm, whose material and informational halves have separately real intervals.

## Explicit Zero Divisors

**Example (an explicit pair).** With the standard idempotents, $\tilde\Pi_+\tilde\Pi_-=0$ with both factors nonzero. In unnormalised form, set $\tilde Q_1=e_t+i\vec e_z$ and $\tilde Q_2=e_t-i\vec e_z$, twice the two idempotents. Then
$$
\tilde Q_1\tilde Q_2=e_t-(i\vec e_z)^2=e_t-1=0,\qquad \tilde Q_1\neq0,\qquad \tilde Q_2\neq0 .
$$
Both $\tilde Q_1$ and $\tilde Q_2$ have two nonzero complex coefficients. Moreover $\langle\tilde Q_1\rangle_{\natural}=1+i^2=0$, so $\tilde Q_1$ is **null** as well as a zero divisor; it is not nilpotent, since $\tilde Q_1^2=(e_t+i\vec e_z)^2=e_t+2i\vec e_z-(\vec e_z)^2=2e_t+2i\vec e_z=2\tilde Q_1\neq0$.

**Physical interpretation.** The pair $\tilde Q_1=e_t+i\vec e_z$, $\tilde Q_2=e_t-i\vec e_z$ is a **lightlike pair**: each is null, $N=0$, so each is a light-cone element, and their product vanishes. This is the algebraic content of the light cone: two null elements whose product is zero are the two null directions of a lightlike plane. The element $\tilde Q_1$ being null but not nilpotent is the statement that a lightlike direction squares to a multiple of itself and not to zero; the genuinely nilpotent directions are the pure null vectors, such as $\vec e_x+i\vec e_y$, whose square vanishes (*Zero Divisors of the Biquaternion Algebra*).

## Physical Readings

The computations read as the framework's calibration set. The multiplication table is the product law of the physical objects; the remarkable subspaces exhibited on one element are the interpretations of one four-vector; the four conjugations applied to it are the four forms; and the idempotents are the pure states. Read as a calibration, the article is where the vocabulary of the series is checked against a single element, so it is also the place where the interpretations of the other articles can be tested against one another.

## Summary

The multiplication of $\mathbb{B}$ is the quaternion table with complex coefficients and central $i$, $i^2=-1$. On the element $\tilde{Q}=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$ the remarkable subspaces are exhibited by the scalar-vector, quaternion-anti-quaternion and Hermitian-anti-Hermitian decompositions of $\tilde{Q}$, and the four conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat}=-{}^{*}$ act on it as listed. The element has norm $\langle\tilde{Q}\rangle_{\natural}=11+2i$, so it is a unit with $\tilde{Q}^{-1}=\tilde{Q}^{\natural}/(11+2i)$; its material part has norm $9$ and its informational part norm $2$. The idempotents $\tilde\Pi_+,\tilde\Pi_-$ satisfy $\tilde\Pi_+\tilde\Pi_-=0$ and give $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ with each summand minimal; the pair $\tilde Q_1=e_t+i\vec e_z$, $\tilde Q_2=e_t-i\vec e_z$ is an explicit zero-divisor pair, both factors null.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\tilde{Q}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$ | Developed form, $Q_\mu\in\mathbb{C}$ |
| $i$ | Central complex unit, $i^2=-1$ |
| $\mathrm{Sc}\,\tilde{Q}=Q_t$, $\vec Q=\sum_{\mu\in\{x,y,z\}}Q_\mu\vec e_\mu$ | Scalar and vector parts |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}={}^{\natural}\circ\bar{\cdot}$, ${}^{\flat}=-{}^{*}$ | The four conjugations |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | The remarkable subspaces |
| $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\ \tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ | Orthogonal primitive idempotents; correspond to the chiral projectors |
| $\langle\tilde{Q}\rangle_{\natural}=11+2i$ | Norm of the fixed element; nonzero, so a unit |
| $\tilde{Q}^{-1}=\tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$ | Inverse of the fixed element |
| $\tilde Q_1=e_t+i\vec e_z,\ \tilde Q_2=e_t-i\vec e_z$ | Null zero-divisor pair, $\tilde Q_1\tilde Q_2=0$ |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the quaternion and biquaternion computations.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents and minimal left ideals in the structure theory of finite-dimensional algebras.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for idempotents, minimal ideals and the decomposition of a ring into simple modules.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2nd ed. 2001), for the complexification of the quaternions and the null cone.
