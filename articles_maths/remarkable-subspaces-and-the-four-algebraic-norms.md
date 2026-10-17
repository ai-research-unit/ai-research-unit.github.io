# __Remarkable Subspaces and the Four Algebraic Norms__

## Introduction

The four **algebraic norms** of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*, $\langle\cdot\rangle$, $\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{\natural*}$, are the four general algebraic norms, and each of them is read on each of the remarkable subspaces of *Introduction to the Remarkable Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_{+}$ and the anti-Hermitian subspace $\mathbb{M}_{-}$. This article carries out that reading, one subspace to a section, and states for each subspace what each of the four algebraic norms becomes there and what its signature over $\mathbb{R}$ is.

The rule is the same on every subspace and needs no proof beyond the definition. The **algebraic norm** of a form is that form read at its two equal arguments, and the algebraic norm of a restriction is the restriction of the algebraic norm: for a subspace $U$ and a form $\varphi$,

$$
\varphi|_{U}(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\varphi(\tilde Q)\big|_{\tilde Q\in U},
$$

so that the algebraic norm on $U$ is the algebraic norm of the ambient space read on the elements of $U$. The value of the algebraic norm on $U$ is therefore read off the coordinates of the element of $U$, and its **signature over $\mathbb{R}$** is the signature of the symmetric real bilinear form obtained from the polarisation of the restriction, on any real basis of $U$. The four algebraic norms are the same four functions everywhere; the remarkable subspaces differ in the coordinate form they impose, and it is that which specialises the four.

The two tables below are the summary, and the six sections after them are the detail. The restriction table gives the value of each of the four algebraic norms on a general element of each subspace; the signature table gives the signature over $\mathbb{R}$ of each.

| subspace | element | $\langle\cdot\rangle$ | $\langle\cdot\rangle_{*}$ | $\langle\cdot\rangle_{\natural}$ | $\langle\cdot\rangle_{\natural*}$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q=Ae_t$ | $A^{2}$ | $\lvert A\rvert^{2}$ | $A^{2}$ | $\lvert A\rvert^{2}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q=\sum_kP_k\vec e_k$ | $-\sum_kP_k^{2}$ | $\sum_k\lvert P_k\rvert^{2}$ | $\sum_kP_k^{2}$ | $-\sum_k\lvert P_k\rvert^{2}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde Q=h=\sum_\mu h_\mu e_\mu$, $h_\mu\in\mathbb{R}$ | $h_0^{2}-\sum_kh_k^{2}$ | $\sum_\mu h_\mu^{2}$ | $\sum_\mu h_\mu^{2}$ | $h_0^{2}-\sum_kh_k^{2}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\tilde Q=ih$ | $-h_0^{2}+\sum_kh_k^{2}$ | $\sum_\mu h_\mu^{2}$ | $-\sum_\mu h_\mu^{2}$ | $h_0^{2}-\sum_kh_k^{2}$ |
| $\mathbb{M}_+$ | $\tilde Q=a_0e_t+i\vec p$, $a_0\in\mathbb{R}$ | $a_0^{2}+(\vec p,\vec p)$ | $a_0^{2}+(\vec p,\vec p)$ | $a_0^{2}-(\vec p,\vec p)$ | $a_0^{2}-(\vec p,\vec p)$ |
| $\mathbb{M}_-$ | $\tilde Q=ib_0e_t+\vec q$, $b_0\in\mathbb{R}$ | $-b_0^{2}-(\vec q,\vec q)$ | $b_0^{2}+(\vec q,\vec q)$ | $-b_0^{2}+(\vec q,\vec q)$ | $b_0^{2}-(\vec q,\vec q)$ |

Reading each restriction as a real quadratic form, the signatures are these.

| subspace | $\dim_{\mathbb{R}}$ | $\langle\cdot\rangle$ | $\langle\cdot\rangle_{*}$ | $\langle\cdot\rangle_{\natural}$ | $\langle\cdot\rangle_{\natural*}$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $(1,1)$ | $(2,0)$ | $(1,1)$ | $(2,0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $(3,3)$ | $(6,0)$ | $(3,3)$ | $(0,6)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $(3,1)$ | $(4,0)$ | $(0,4)$ | $(1,3)$ |
| $\mathbb{M}_+$ | $4$ | $(4,0)$ | $(4,0)$ | $(1,3)$ | $(1,3)$ |
| $\mathbb{M}_-$ | $4$ | $(0,4)$ | $(4,0)$ | $(3,1)$ | $(1,3)$ |

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t=1$, $\vec e_k^{2}=-e_t$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written in the centre–vector split $\tilde Q=c+v$ with $c=Q_te_t\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_k\vec e_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$, the coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and $\mathbb{B}$ is identified with $\mathbb{C}^{4}$ by $\tilde Q\mapsto(Q_t,Q_x,Q_y,Q_z)$. The vector parts carry the complex bilinear dot product $(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k$ and the cross product $\vec P\times\vec Q$.

The four general forms are the four pairings of *Conventions in the Biquaternion Universe*, written with the one bracket $\langle\cdot,\cdot\rangle$ whose subscript records the pair $(a,b)$:

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_\mu P_\mu Q_\mu,
$$
$$
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu},
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

and the four **algebraic norms** are their algebraic norms,

$$
\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2},\qquad
\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2},\qquad
\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2},\qquad
\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}.
$$

$\langle\cdot\rangle$ is the general plain bilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle$, $\langle\cdot\rangle_{*}$ the general plain sesquilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle_{*}$, $\langle\cdot\rangle_{\natural}$ the general quaternionic bilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle_{\natural}$ and $\langle\cdot\rangle_{\natural*}$ the general quaternionic sesquilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle_{\natural*}$; the names, the bracket and the pair of each are the convention of *Conventions in the Biquaternion Universe*, and the four are defined in *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, which also counts them, and separated, as the algebraic norms of those forms, in *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*. $\langle\cdot\rangle_{*}$ is also the Hermitian algebraic norm and $\langle\cdot\rangle_{\natural*}$ the Krein algebraic norm. The Euclidean norm is $\lVert\tilde Q\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$, the square root of $\langle\cdot\rangle_{*}$ and the unique topological norm of the space.

The remarkable subspaces and their real bases are those of *Introduction to the Remarkable Subspaces*, and are used here in the coordinate form that article gives: the centre $\mathbb{C}_{\mathbb{B}}=\{Ae_t:A\in\mathbb{C}\}$, of real dimension two; the vector subspace $\mathrm{Vect}(\mathbb{B})=\{\sum_kP_k\vec e_k:P_k\in\mathbb{C}\}$, of real dimension six; the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\{\sum_\mu h_\mu e_\mu:h_\mu\in\mathbb{R}\}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}=\{ih:h\in\mathbb{H}_{\mathbb{B}}\}$, of real dimension four; and the Hermitian subspace $\mathbb{M}_+=\{a_0e_t+i\vec p:a_0\in\mathbb{R},\ \vec p\ \text{real}\}$ and the anti-Hermitian subspace $\mathbb{M}_-=\{ib_0e_t+\vec q:b_0\in\mathbb{R},\ \vec q\ \text{real}\}$, of real dimension four. A signature $(n,m)$ over $\mathbb{R}$ counts $p$ positive and $q$ negative squares of the real quadratic form; it is definite when one of the two numbers is zero and indefinite otherwise.

## The Centre Subspace

**On the centre the four algebraic norms collapse to two, $\langle\cdot\rangle=\langle\cdot\rangle_{\natural}=A^{2}$ and $\langle\cdot\rangle_{*}=\langle\cdot\rangle_{\natural*}=\lvert A\rvert^{2}$.** An element of the centre is $\tilde Q=Ae_t$ with $A=a+ib$ complex, and its only nonzero coordinate is $Q_t=A$. Every one of the four sums therefore reduces to its $0$-th term, $\varepsilon_0=1$ and $\overline{A}$ in place of $A$ for the two sesquilinear ones, so that

$$
\langle Ae_t\rangle=A^{2},\qquad \langle Ae_t\rangle_{*}=\lvert A\rvert^{2},\qquad \langle Ae_t\rangle_{\natural}=A^{2},\qquad \langle Ae_t\rangle_{\natural*}=\lvert A\rvert^{2}.
$$

On the real basis $e_t,ie_t$ the pairs $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ are the complex square $A^{2}=(a^{2}-b^{2})+2iab$, of signature $(1,1)$, and the pairs $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ are the positive definite $\lvert A\rvert^{2}=a^{2}+b^{2}$, of signature $(2,0)$. The centre is the only subspace of the remarkable subspaces on which $\langle\cdot\rangle_{\natural*}$ is positive definite.

## The Vector Subspace

**On the vector subspace the two bilinear algebraic norms are opposite, $\langle\cdot\rangle=-N$, and the two sesquilinear ones are opposite, $\langle\cdot\rangle_{\natural*}=-H$.** An element is $\tilde Q=\sum_kP_k\vec e_k$, with no scalar coordinate, so that the four sums run over $k=1,2,3$ alone and the sign $\varepsilon_k=-1$ of the bilinear ones enters with full force,

$$
B=-\sum_kP_k^{2},\qquad H=\sum_k\lvert P_k\rvert^{2},\qquad N=\sum_kP_k^{2},\qquad K=-\sum_k\lvert P_k\rvert^{2}.
$$

On the real basis $\vec e_k$ and $i\vec e_k$ the form $\langle\cdot\rangle_{*}$ is the positive sum of the six squares, of signature $(6,0)$, and $\langle\cdot\rangle_{\natural*}$ its negative, of signature $(0,6)$, the only subspace of the remarkable subspaces on which $\langle\cdot\rangle_{\natural*}$ is negative definite. The complex squares $P_k^{2}$ split into $p_k^{2}-q_k^{2}$ on the real parts and the imaginary parts, so that $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}=-B$ are of signature $(3,3)$. The vector subspace is thus the mirror in which the sign vector $\varepsilon$ has its sharpest effect, the two bilinear algebraic norms and the two sesquilinear ones each being negatives of one another.

## The Quaternion Subspace

**On the quaternion subspace the two sesquilinear algebraic norms coincide with the two bilinear ones, $\langle\cdot\rangle_{*}=\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{\natural*}=\langle\cdot\rangle$, and the values are real.** An element is $h=\sum_\mu h_\mu e_\mu$ with all $h_\mu$ real, so that the coefficientwise conjugation is the identity and

$$
\langle h\rangle=h_0^{2}-\sum_kh_k^{2},\qquad H(h)=\sum_\mu h_\mu^{2},\qquad \langle h\rangle_{\natural}=\sum_\mu h_\mu^{2},\qquad \langle h\rangle_{\natural*}=h_0^{2}-\sum_kh_k^{2}.
$$

Because $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural}$ are equal and $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural*}$ are equal, the four algebraic norms are the two, and both pairs are already real on this subspace. $\langle\cdot\rangle_{\natural}=\langle\cdot\rangle_{*}$ is the sum of the four squares, of signature $(4,0)$: the quaternion subspace is the one subspace of the remarkable subspaces of dimension four on which the multiplicative algebraic norm $\langle\cdot\rangle_{\natural}$ is positive definite, and it is the subspace on which the multiplicative and the definite senses of the norm meet, as they do on $\mathbb{H}$ itself. $\langle\cdot\rangle=\langle\cdot\rangle_{\natural*}$ is the Lorentzian form $h_0^{2}-\sum_kh_k^{2}$, of signature $(1,3)$, the form of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

## The Anti-Quaternion Subspace

**On the anti-quaternion subspace the bilinear algebraic norms change sign against the quaternion subspace, $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ both, while $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ do not.** An element is $\tilde Q=ih$ with $h$ real, so that $Q_\mu=ih_\mu$ and the squares $Q_\mu^{2}=-h_\mu^{2}$ while the moduli $\lvert Q_\mu\rvert^{2}=h_\mu^{2}$ stay unchanged,

$$
\langle ih\rangle=-h_0^{2}+\sum_kh_k^{2},\qquad \langle ih\rangle_{*}=\sum_\mu h_\mu^{2},\qquad \langle ih\rangle_{\natural}=-\sum_\mu h_\mu^{2},\qquad \langle ih\rangle_{\natural*}=h_0^{2}-\sum_kh_k^{2}.
$$

The Euclidean square $\langle\cdot\rangle_{*}$ is untouched by the translation by $i$, of signature $(4,0)$; the two sesquilinear algebraic norms are unchanged, $\langle ih\rangle_{*}=H(h)$ and $\langle ih\rangle_{\natural*}=\langle h\rangle_{\natural*}$; and the two bilinear algebraic norms are negated, $\langle ih\rangle=-\langle h\rangle$ and $\langle ih\rangle_{\natural}=-\langle h\rangle_{\natural}$, so that $\langle\cdot\rangle$ becomes $-K$, of signature $(3,1)$, and $\langle\cdot\rangle_{\natural}$ becomes $-H$, of signature $(0,4)$. The anti-quaternion subspace is the imaginary translate of the quaternion subspace, and the effect of the translation is precisely the sign that separates the complex bilinear algebraic norm $\langle\cdot\rangle_{\natural}$ from the topological one: on $\mathbb{H}_{\mathbb{B}}$, $\langle\cdot\rangle_{\natural}=\lVert\cdot\rVert_E^{2}$, and on $i\mathbb{H}_{\mathbb{B}}$, $\langle\cdot\rangle_{\natural}=-\lVert\cdot\rVert_E^{2}$. That sign is what makes $\langle\cdot\rangle_{\natural}$ definite on each of the two real forms, positive on the one and negative on the other, while $\langle\cdot\rangle_{\natural}$ is indefinite on the whole algebra.

## The Hermitian Subspace

**On the Hermitian subspace the general plain bilinear algebraic norm coincides with the general plain sesquilinear one, $\langle\cdot\rangle=\langle\cdot\rangle_{*}$, and the general quaternionic bilinear with the general quaternionic sesquilinear, $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{\natural*}$.** An element is $\tilde Q=a_0e_t+i\vec p$ with $a_0$ real and $\vec p$ a real vector, so that $Q_t=a_0$ is real and $Q_k=ip_k$ is purely imaginary: the products $Q_t^{2}=a_0^{2}$ and $Q_k^{2}=-p_k^{2}$ give

$$
B=a_0^{2}+(\vec p,\vec p),\qquad H=a_0^{2}+(\vec p,\vec p),\qquad N=a_0^{2}-(\vec p,\vec p),\qquad K=a_0^{2}-(\vec p,\vec p).
$$

On this subspace the effect of the sign vector $\varepsilon$ is cancelled by the effect of the central imaginary unit: the sign $\varepsilon_k=-1$ of the bilinear sums composes with the sign $i^{2}=-1$ of the imaginary coordinates to give a net $+1$, so that the two bilinear algebraic norms take the same values as the two sesquilinear ones, $\langle\cdot\rangle=\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural}=\langle\cdot\rangle_{\natural*}$. The pair $\langle\cdot\rangle=\langle\cdot\rangle_{*}$ is the positive sum of the four squares, of signature $(4,0)$, and the pair $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{\natural*}$ is the form $a_0^{2}-(\vec p,\vec p)$, of signature $(1,3)$, indefinite. On the Hermitian subspace the two bilinear algebraic norms coincide with the two sesquilinear ones, and the coincidence is exact rather than up to sign; it is this coincidence that makes the four algebraic norms fall to the two real forms there, and it does not make the multiplicative algebraic norm definite. the definite one is $\langle\cdot\rangle_{*}$, of signature $(4,0)$, the Euclidean square; $\langle\cdot\rangle_{\natural}$ is indefinite on $\mathbb{M}_+$, of signature $(1,3)$.

## The Anti-Hermitian Subspace

**On the anti-Hermitian subspace the two bilinear algebraic norms are the negative of the two on the Hermitian subspace, and the two sesquilinear ones agree with it.** An element is $\tilde Q=ib_0e_t+\vec q$ with $b_0$ real and $\vec q$ a real vector, so that $Q_t=ib_0$ is purely imaginary and $Q_k=q_k$ is real:

$$
B=-b_0^{2}-(\vec q,\vec q),\qquad H=b_0^{2}+(\vec q,\vec q),\qquad N=-b_0^{2}+(\vec q,\vec q),\qquad K=b_0^{2}-(\vec q,\vec q).
$$

The Euclidean square $\langle\cdot\rangle_{*}$ and the Krein algebraic norm $\langle\cdot\rangle_{\natural*}$ are the same as on the Hermitian subspace, because the passage from $\mathbb{M}_+$ to $\mathbb{M}_-$ replaces the imaginary vector $\vec p$ by the real vector $\vec q$ and the real $a_0$ by the imaginary $ib_0$, an exchange that touches the bilinear algebraic norms and not the sesquilinear ones. So $\langle\cdot\rangle_{*}$ is positive definite of signature $(4,0)$, unchanged, and $\langle\cdot\rangle_{\natural*}=b_0^{2}-(\vec q,\vec q)$ is the Lorentzian form of signature $(1,3)$, unchanged; while $\langle\cdot,\cdot\rangle=-H$ is negative definite, of signature $(0,4)$, and $\langle\cdot,\cdot\rangle_{\natural}=-K$ is of signature $(3,1)$. The material sector is this subspace, and the section below reads it.

## The Material Interpretation

**Remark (the material reading).** Restricted to the material sector $\mathbb{M}_-$ the four algebraic norms read

$$
B=-b_0^{2}-(\vec q,\vec q),\qquad H=b_0^{2}+(\vec q,\vec q),\qquad N=-b_0^{2}+(\vec q,\vec q),\qquad K=b_0^{2}-(\vec q,\vec q),
$$

so that $\langle\cdot\rangle=-H$ and $\langle\cdot\rangle_{\natural}=-K$ there: the interval $\langle\cdot\rangle_{\natural}$ of signature $(3,1)$ and its negative $\langle\cdot\rangle_{\natural*}$ of signature $(1,3)$, the Euclidean square $\langle\cdot\rangle_{*}$ of signature $(4,0)$ and its negative. The passage from the interval to the Euclidean square is the passage between $\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{*}$, and it is the single sign the Hermitian conjugation inserts in the second slot; the passage between $\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle_{\natural}$ is the sign the natural conjugation inserts in the first. On the material sector the pair is the Minkowski form and the Euclidean one that the physics part of the corpus reads as the metric of the biquaternion universe, and it is here that the four algebraic norms acquire the two forms — the interval and the Euclidean square — that the physical readings of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* carry.

## What the Remarkable Subspaces Separate

The remarkable subspaces separate the four algebraic norms in a way that no single one of them does on the whole algebra. On $\mathbb{B}$ no algebraic norm is both definite and multiplicative, and $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural}$ are two different functions; on the quaternion subspace the two functions become one, $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}$, and on the anti-quaternion subspace they become opposite, $\langle\cdot\rangle_{\natural}=-H$, the one subspace being the imaginary translate of the other. The coincidence of the quaternion subspace, and its failure on the other four subspaces, is the content of the real-form caution of *The 12 Products of the Biquaternioid Complex Space* read at the two equal arguments and on the remarkable subspaces.

Three facts summarise the separation. Only $\langle\cdot\rangle_{*}$ is definite on every one of the remarkable subspaces; $\langle\cdot\rangle$ is definite on exactly two, the two sectors, with exchanged signs; $\langle\cdot\rangle_{\natural}$ is definite on exactly two of them, positive on the quaternion subspace and negative on its imaginary translate; and $\langle\cdot\rangle_{\natural*}$ is definite on exactly two, the centre and the vector subspace, where it is the positive definite form and its negative. The four algebraic norms are thus definite on the whole algebra only for $\langle\cdot\rangle_{*}$; each of the other three is definite on a proper pair of subspaces, and the remarkable subspaces are the places where the pair is read.

The same facts are read in the four algebraic norms of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* and in the four pairings of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; the restrictions to the remarkable subspaces are the same object read on the remarkable subspaces, and the tables above and the four pairings' own restriction tables agree cell by cell.

## Summary

**The four algebraic norms are the same four functions on the whole algebra and on each of the remarkable subspaces.** On the centre they collapse to two, $\langle\cdot\rangle=\langle\cdot\rangle_{\natural}=A^{2}$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}=\lvert A\rvert^{2}$; on the vector subspace the two bilinear ones are opposites, $\langle\cdot\rangle=-N$, and the two sesquilinear ones are opposites, $\langle\cdot\rangle_{*}=-K$; on the quaternion subspace the two sesquilinear ones coincide with the two bilinear ones, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural}$, and both pairs are real; on the anti-quaternion subspace $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ change sign against the quaternion subspace while $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ do not; on the Hermitian subspace $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{\natural*}$; and on the anti-Hermitian subspace the two bilinear ones are the negatives of those on the Hermitian subspace while the two sesquilinear ones agree with it.

**The signatures over $\mathbb{R}$** are: the centre, $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ of signature $(1,1)$ and $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ of signature $(2,0)$; the vector subspace, $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ of signature $(3,3)$, $\langle\cdot\rangle_{*}$ of signature $(6,0)$ and $\langle\cdot\rangle_{\natural*}$ of signature $(0,6)$; the quaternion subspace, $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural*}$ of signature $(1,3)$ and $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural}$ of signature $(4,0)$; the anti-quaternion subspace, $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural*}$ of signature $(3,1)$ and $(1,3)$ respectively and $\langle\cdot\rangle_{*}$ of signature $(4,0)$ with $\langle\cdot\rangle_{\natural}$ of signature $(0,4)$; the Hermitian subspace, $\langle\cdot\rangle$ and $\langle\cdot\rangle_{*}$ of signature $(4,0)$ and $\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{\natural*}$ of signature $(1,3)$; and the anti-Hermitian subspace, $\langle\cdot\rangle$ of signature $(0,4)$, $\langle\cdot\rangle_{*}$ of signature $(4,0)$, $\langle\cdot\rangle_{\natural}$ of signature $(3,1)$ and $\langle\cdot\rangle_{\natural*}$ of signature $(1,3)$. Only $\langle\cdot\rangle_{*}$ is definite on the remarkable subspaces; $\langle\cdot\rangle$ is definite on the two sectors alone, $\langle\cdot\rangle_{\natural}$ on the quaternion subspace and its imaginary translate alone, and $\langle\cdot\rangle_{\natural*}$ on the centre and the vector subspace alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the four pairings: the bilinear, the sesquilinear, the general quaternionic bilinear and the general quaternionic sesquilinear form |
| $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{\natural*}$ | the four algebraic norms of the four pairings, of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces, the two real forms |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces; the informational and the material sector |
| $\tilde Q=Ae_t$ | the general element of the centre, $A\in\mathbb{C}$ |
| $\tilde Q=\sum_kP_k\vec e_k$ | the general element of the vector subspace, $P_k\in\mathbb{C}$ |
| $h=\sum_\mu h_\mu e_\mu$ | the general element of the quaternion subspace, $h_\mu\in\mathbb{R}$ |
| $a_0e_t+i\vec p$, $ib_0e_t+\vec q$ | the general elements of the two sectors, $a_0,b_0\in\mathbb{R}$, $\vec p,\vec q$ real |
| $(n,m)$ | the signature over $\mathbb{R}$ of a real quadratic form |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the four algebraic norms, the reduction from the twelve products to four, and the separation of the multiplicative and the definite senses of the norm
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the convention of the four pairings — the one bracket, the four names, the pairs and the trace form — and for the readings of the four on the algebra and on the material sector
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces themselves, one to a section, with their defining conditions, bases and dimensions
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the coordinate blocks, the intersections and the sums of the remarkable subspaces
- *Remarkable Subspaces and the Four Forms* (`articles_maths/remarkable-subspaces-and-the-four-forms.md`), for the same remarkable subspaces read at the level of the forms, with the value of each form on a general pair, its real and imaginary parts and the alternating companion of the two sesquilinear forms, of which the tables here are the algebraic norms
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the four general products read on the remarkable subspaces, one subspace to a section
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the four forms, the four degree-two functions and the four algebraic norms they carry, and their own restrictions to the remarkable subspaces
- *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternioid-c-space.md`), for the four general forms and their Gram matrices
