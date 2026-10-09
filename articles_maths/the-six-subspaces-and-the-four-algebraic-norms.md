# __The Six Subspaces and the Four Algebraic Norms__

## Introduction

The four **algebraic norms** of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*, $B$, $N$, $H$ and $K$, are the diagonals of the four general forms, and each of them is read on each of the six distinguished subspaces of *Introduction to the Six Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_{+}$ and the anti-Hermitian subspace $\mathbb{M}_{-}$. This article carries out that reading, one subspace to a section, and states for each subspace what each of the four algebraic norms becomes there and what its signature over $\mathbb{R}$ is.

The rule is the same on every subspace and needs no proof beyond the definition. The **algebraic norm** of a form is its diagonal, and the diagonal of a restriction is the restriction of the diagonal: for a subspace $U$ and a form $\varphi$,

$$
\varphi|_{U}(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\varphi(\tilde Q)\big|_{\tilde Q\in U},
$$

so that the algebraic norm on $U$ is the algebraic norm of the ambient space read on the elements of $U$. The value of the algebraic norm on $U$ is therefore read off the coordinates of the element of $U$, and its **signature over $\mathbb{R}$** is the signature of the symmetric real bilinear form obtained from the polarisation of the restriction, on any real basis of $U$. The four algebraic norms are the same four functions everywhere; the six subspaces differ in the coordinate form they impose, and it is that which specialises the four.

The two tables below are the summary, and the six sections after them are the detail. The restriction table gives the value of each of the four algebraic norms on a general element of each subspace; the signature table gives the signature over $\mathbb{R}$ of each.

| subspace | element | $B$ | $N$ | $H$ | $K$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q=Ae_0$ | $A^{2}$ | $A^{2}$ | $\lvert A\rvert^{2}$ | $\lvert A\rvert^{2}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q=\sum_kP_ke_k$ | $-\sum_kP_k^{2}$ | $\sum_kP_k^{2}$ | $\sum_k\lvert P_k\rvert^{2}$ | $-\sum_k\lvert P_k\rvert^{2}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde Q=h=\sum_\mu h_\mu e_\mu$, $h_\mu\in\mathbb{R}$ | $h_0^{2}-\sum_kh_k^{2}$ | $\sum_\mu h_\mu^{2}$ | $\sum_\mu h_\mu^{2}$ | $h_0^{2}-\sum_kh_k^{2}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\tilde Q=ih$ | $-h_0^{2}+\sum_kh_k^{2}$ | $-\sum_\mu h_\mu^{2}$ | $\sum_\mu h_\mu^{2}$ | $h_0^{2}-\sum_kh_k^{2}$ |
| $\mathbb{M}_+$ | $\tilde Q=a_0e_0+i\mathbf p$, $a_0\in\mathbb{R}$ | $a_0^{2}+(\mathbf p,\mathbf p)$ | $a_0^{2}-(\mathbf p,\mathbf p)$ | $a_0^{2}+(\mathbf p,\mathbf p)$ | $a_0^{2}-(\mathbf p,\mathbf p)$ |
| $\mathbb{M}_-$ | $\tilde Q=ib_0e_0+\mathbf q$, $b_0\in\mathbb{R}$ | $-b_0^{2}-(\mathbf q,\mathbf q)$ | $-b_0^{2}+(\mathbf q,\mathbf q)$ | $b_0^{2}+(\mathbf q,\mathbf q)$ | $b_0^{2}-(\mathbf q,\mathbf q)$ |

Reading each restriction as a real quadratic form, the signatures are these.

| subspace | $\dim_{\mathbb{R}}$ | $B$ | $N$ | $H$ | $K$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $(1,1)$ | $(1,1)$ | $(2,0)$ | $(2,0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $(3,3)$ | $(3,3)$ | $(6,0)$ | $(0,6)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_+$ | $4$ | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_-$ | $4$ | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$, $e_0=1$, $e_k^{2}=-e_0$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written in the centre–vector split $\tilde Q=c+v$ with $c=Q_0e_0\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_ke_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$, the coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and $\mathbb{B}$ is identified with $\mathbb{C}^{4}$ by $\tilde Q\mapsto(Q_0,Q_1,Q_2,Q_3)$. The vector parts carry the complex bilinear dot product $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$ and the cross product $\mathbf P\times\mathbf Q$.

The four general forms are the four pairings of *Conventions in the Biquaternion Universe*, written with the one bracket $\langle\cdot,\cdot\rangle$ whose subscript records the pair $(a,b)$:

$$
B(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,
\qquad
N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_\mu P_\mu Q_\mu,
$$
$$
H(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu},
\qquad
K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

and the four **algebraic norms** are their diagonals,

$$
B(\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2},\qquad
N(\tilde Q)=\sum_\mu Q_\mu^{2},\qquad
H(\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2},\qquad
K(\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}.
$$

$B$ is the general plain bilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle$, $N$ the general quaternionic bilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle_{\natural}$, $H$ the general plain sesquilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle_{*}$ and $K$ the general quaternionic sesquilinear algebraic norm $\langle\tilde Q,\tilde Q\rangle_{\natural*}$; the names, the bracket and the pair of each are the convention of *Conventions in the Biquaternion Universe*, and the four are defined in *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, which also counts them, and separated, as the diagonals of those forms, in *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. $H$ is also the Hermitian algebraic norm and $K$ the Krein algebraic norm. The Euclidean norm is $\lVert\tilde Q\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$, the square root of $H$ and the unique topological norm of the space.

The six subspaces and their real bases are those of *Introduction to the Six Subspaces*, and are used here in the coordinate form that article gives: the centre $\mathbb{C}_{\mathbb{B}}=\{Ae_0:A\in\mathbb{C}\}$, of real dimension two; the vector subspace $\mathrm{Vect}(\mathbb{B})=\{\sum_kP_ke_k:P_k\in\mathbb{C}\}$, of real dimension six; the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\{\sum_\mu h_\mu e_\mu:h_\mu\in\mathbb{R}\}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}=\{ih:h\in\mathbb{H}_{\mathbb{B}}\}$, of real dimension four; and the Hermitian subspace $\mathbb{M}_+=\{a_0e_0+i\mathbf p:a_0\in\mathbb{R},\ \mathbf p\ \text{real}\}$ and the anti-Hermitian subspace $\mathbb{M}_-=\{ib_0e_0+\mathbf q:b_0\in\mathbb{R},\ \mathbf q\ \text{real}\}$, of real dimension four. A signature $(p,q)$ over $\mathbb{R}$ counts $p$ positive and $q$ negative squares of the real quadratic form; it is definite when one of the two numbers is zero and indefinite otherwise.

## The Centre Subspace

**On the centre the four algebraic norms collapse to two, $B=N=A^{2}$ and $H=K=\lvert A\rvert^{2}$.** An element of the centre is $\tilde Q=Ae_0$ with $A=a+ib$ complex, and its only nonzero coordinate is $Q_0=A$. Every one of the four sums therefore reduces to its $0$-th term, $\varepsilon_0=1$ and $\overline{A}$ in place of $A$ for the two sesquilinear ones, so that

$$
B(Ae_0)=A^{2},\qquad N(Ae_0)=A^{2},\qquad H(Ae_0)=\lvert A\rvert^{2},\qquad K(Ae_0)=\lvert A\rvert^{2}.
$$

On the real basis $e_0,ie_0$ the pairs $B$ and $N$ are the complex square $A^{2}=(a^{2}-b^{2})+2iab$, of signature $(1,1)$, and the pairs $H$ and $K$ are the positive definite $\lvert A\rvert^{2}=a^{2}+b^{2}$, of signature $(2,0)$. The centre is the only subspace of the six on which $K$ is positive definite.

## The Vector Subspace

**On the vector subspace the two bilinear algebraic norms are opposite, $B=-N$, and the two sesquilinear ones are opposite, $K=-H$.** An element is $\tilde Q=\sum_kP_ke_k$, with no scalar coordinate, so that the four sums run over $k=1,2,3$ alone and the sign $\varepsilon_k=-1$ of the bilinear ones enters with full force,

$$
B=-\sum_kP_k^{2},\qquad N=\sum_kP_k^{2},\qquad H=\sum_k\lvert P_k\rvert^{2},\qquad K=-\sum_k\lvert P_k\rvert^{2}.
$$

On the real basis $e_k$ and $ie_k$ the form $H$ is the positive sum of the six squares, of signature $(6,0)$, and $K$ its negative, of signature $(0,6)$, the only subspace of the six on which $K$ is negative definite. The complex squares $P_k^{2}$ split into $p_k^{2}-q_k^{2}$ on the real parts and the imaginary parts, so that $B$ and $N=-B$ are of signature $(3,3)$. The vector subspace is thus the mirror in which the sign vector $\varepsilon$ has its sharpest effect, the two bilinear algebraic norms and the two sesquilinear ones each being negatives of one another.

## The Quaternion Subspace

**On the quaternion subspace the two sesquilinear algebraic norms coincide with the two bilinear ones, $H=N$ and $K=B$, and the values are real.** An element is $h=\sum_\mu h_\mu e_\mu$ with all $h_\mu$ real, so that the coefficientwise conjugation is the identity and

$$
B(h)=h_0^{2}-\sum_kh_k^{2},\qquad N(h)=\sum_\mu h_\mu^{2},\qquad H(h)=\sum_\mu h_\mu^{2},\qquad K(h)=h_0^{2}-\sum_kh_k^{2}.
$$

Because $H$ and $N$ are equal and $K$ and $B$ are equal, the four algebraic norms are the two, and both pairs are already real on this subspace. $N=H$ is the sum of the four squares, of signature $(4,0)$: the quaternion subspace is the one subspace of the six of dimension four on which the multiplicative algebraic norm $N$ is positive definite, and it is the subspace on which the multiplicative and the definite senses of the norm meet, as they do on $\mathbb{H}$ itself. $B=K$ is the Lorentzian form $h_0^{2}-\sum_kh_k^{2}$, of signature $(1,3)$, the form of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Anti-Quaternion Subspace

**On the anti-quaternion subspace the bilinear algebraic norms change sign against the quaternion subspace, $B$ and $N$ both, while $H$ and $K$ do not.** An element is $\tilde Q=ih$ with $h$ real, so that $Q_\mu=ih_\mu$ and the squares $Q_\mu^{2}=-h_\mu^{2}$ while the moduli $\lvert Q_\mu\rvert^{2}=h_\mu^{2}$ stay unchanged,

$$
B(ih)=-h_0^{2}+\sum_kh_k^{2},\qquad N(ih)=-\sum_\mu h_\mu^{2},\qquad H(ih)=\sum_\mu h_\mu^{2},\qquad K(ih)=h_0^{2}-\sum_kh_k^{2}.
$$

The Euclidean square $H$ is untouched by the translation by $i$, of signature $(4,0)$; the two sesquilinear algebraic norms are unchanged, $H(ih)=H(h)$ and $K(ih)=K(h)$; and the two bilinear algebraic norms are negated, $B(ih)=-B(h)$ and $N(ih)=-N(h)$, so that $N$ becomes $-H$, of signature $(0,4)$, and $B$ becomes $-K$, of signature $(3,1)$. The anti-quaternion subspace is the imaginary translate of the quaternion subspace, and the effect of the translation is precisely the sign that separates the complex bilinear algebraic norm $N$ from the topological one: on $\mathbb{H}_{\mathbb{B}}$, $N=\lVert\cdot\rVert_E^{2}$, and on $i\mathbb{H}_{\mathbb{B}}$, $N=-\lVert\cdot\rVert_E^{2}$. That sign is what makes $N$ definite on each of the two real forms, positive on the one and negative on the other, while $N$ is indefinite on the whole algebra.

## The Hermitian Subspace

**On the Hermitian subspace the general plain bilinear algebraic norm coincides with the general plain sesquilinear one, $B=H$, and the general quaternionic bilinear with the general quaternionic sesquilinear, $N=K$.** An element is $\tilde Q=a_0e_0+i\mathbf p$ with $a_0$ real and $\mathbf p$ a real vector, so that $Q_0=a_0$ is real and $Q_k=ip_k$ is purely imaginary: the products $Q_0^{2}=a_0^{2}$ and $Q_k^{2}=-p_k^{2}$ give

$$
B=a_0^{2}+(\mathbf p,\mathbf p),\qquad N=a_0^{2}-(\mathbf p,\mathbf p),\qquad H=a_0^{2}+(\mathbf p,\mathbf p),\qquad K=a_0^{2}-(\mathbf p,\mathbf p).
$$

On this subspace the effect of the sign vector $\varepsilon$ is cancelled by the effect of the central imaginary unit: the sign $\varepsilon_k=-1$ of the bilinear sums composes with the sign $i^{2}=-1$ of the imaginary coordinates to give a net $+1$, so that the two bilinear algebraic norms take the same values as the two sesquilinear ones, $B=H$ and $N=K$. The pair $B=H$ is the positive sum of the four squares, of signature $(4,0)$, and the pair $N=K$ is the form $a_0^{2}-(\mathbf p,\mathbf p)$, of signature $(1,3)$, indefinite. On the Hermitian subspace the two bilinear algebraic norms coincide with the two sesquilinear ones, and the coincidence is exact rather than up to sign; it is this coincidence that makes the four algebraic norms fall to the two real forms there, and it does not make the multiplicative algebraic norm definite. $N$ is indefinite on $\mathbb{M}_+$, of signature $(1,3)$; the definite one is $H$, of signature $(4,0)$, the Euclidean square.

## The Anti-Hermitian Subspace

**On the anti-Hermitian subspace the two bilinear algebraic norms are the negative of the two on the Hermitian subspace, and the two sesquilinear ones agree with it.** An element is $\tilde Q=ib_0e_0+\mathbf q$ with $b_0$ real and $\mathbf q$ a real vector, so that $Q_0=ib_0$ is purely imaginary and $Q_k=q_k$ is real:

$$
B=-b_0^{2}-(\mathbf q,\mathbf q),\qquad N=-b_0^{2}+(\mathbf q,\mathbf q),\qquad H=b_0^{2}+(\mathbf q,\mathbf q),\qquad K=b_0^{2}-(\mathbf q,\mathbf q).
$$

The Euclidean square $H$ and the Krein algebraic norm $K$ are the same as on the Hermitian subspace, because the passage from $\mathbb{M}_+$ to $\mathbb{M}_-$ replaces the imaginary vector $\mathbf p$ by the real vector $\mathbf q$ and the real $a_0$ by the imaginary $ib_0$, an exchange that touches the bilinear algebraic norms and not the sesquilinear ones. So $H$ is positive definite of signature $(4,0)$, unchanged, and $K=b_0^{2}-(\mathbf q,\mathbf q)$ is the Lorentzian form of signature $(1,3)$, unchanged; while $B=-H$ is negative definite, of signature $(0,4)$, and $N=-K$ is of signature $(3,1)$. The material sector is this subspace, and the section below reads it.

## The Material Reading

**Remark (the material reading).** Restricted to the material sector $\mathbb{M}_-$ the four algebraic norms read

$$
K=b_0^{2}-(\mathbf q,\mathbf q),\qquad N=-b_0^{2}+(\mathbf q,\mathbf q),\qquad H=b_0^{2}+(\mathbf q,\mathbf q),\qquad B=-b_0^{2}-(\mathbf q,\mathbf q),
$$

so that $N=-K$ and $B=-H$ there: the interval $N$ of signature $(3,1)$ and its negative $K$ of signature $(1,3)$, the Euclidean square $H$ of signature $(4,0)$ and its negative. The passage from the interval to the Euclidean square is the passage between $N$ and $H$, and it is the single sign the Hermitian conjugation inserts in the second slot; the passage between $K$ and $N$ is the sign the natural conjugation inserts in the first. On the material sector the pair is the Minkowski form and the Euclidean one that the physics part of the corpus reads as the metric of the biquaternion universe, and it is here that the four algebraic norms acquire the two forms — the interval and the Euclidean square — that the physical readings of *The Anti-Hermitian Subspace M- as the Material Sector* and *The Hermitian Subspace M+ as the Informational Sector* carry.

## What the Six Subspaces Separate

The six subspaces separate the four algebraic norms in a way that no single one of them does on the whole algebra. On $\mathbb{B}$ no algebraic norm is both definite and multiplicative, and $N$ and $H$ are two different functions; on the quaternion subspace the two functions become one, $N=H$, and on the anti-quaternion subspace they become opposite, $N=-H$, the one subspace being the imaginary translate of the other. The coincidence of the quaternion subspace, and its failure on the other four subspaces, is the content of the real-form caution of *The 12 Products of the Biquaternion Complex Space* read on the diagonal and on the six.

Three facts summarise the separation. Only $H$ is definite on every one of the six; $N$ is definite on exactly two of them, positive on the quaternion subspace and negative on its imaginary translate; $B$ is definite on exactly two, the two sectors, with exchanged signs; and $K$ is definite on exactly two, the centre and the vector subspace, where it is the positive definite form and its negative. The four algebraic norms are thus definite on the whole algebra only for $H$; each of the other three is definite on a proper pair of subspaces, and the six subspaces are the places where the pair is read.

The same facts are read in the four algebraic norms of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* and in the four pairings of *The Four Pairings of the Biquaternion Algebra*; the restrictions to the six subspaces are the same object read on the six, and the tables above and the four pairings' own restriction tables agree cell by cell.

## Summary

**The four algebraic norms are the same four functions on the whole algebra and on each of the six subspaces.** On the centre they collapse to two, $B=N=A^{2}$ and $H=K=\lvert A\rvert^{2}$; on the vector subspace the two bilinear ones are opposites, $B=-N$, and the two sesquilinear ones are opposites, $K=-H$; on the quaternion subspace the two sesquilinear ones coincide with the two bilinear ones, $H=N$ and $K=B$, and both pairs are real; on the anti-quaternion subspace $B$ and $N$ change sign against the quaternion subspace while $H$ and $K$ do not; on the Hermitian subspace $B=H$ and $N=K$; and on the anti-Hermitian subspace the two bilinear ones are the negatives of those on the Hermitian subspace while the two sesquilinear ones agree with it.

**The signatures over $\mathbb{R}$** are: the centre, $B$ and $N$ of signature $(1,1)$ and $H$ and $K$ of signature $(2,0)$; the vector subspace, $B$ and $N$ of signature $(3,3)$, $H$ of signature $(6,0)$ and $K$ of signature $(0,6)$; the quaternion subspace, $B$ and $K$ of signature $(1,3)$ and $N$ and $H$ of signature $(4,0)$; the anti-quaternion subspace, $B$ and $K$ of signature $(3,1)$ and $(1,3)$ respectively and $N$ of signature $(0,4)$ with $H$ of signature $(4,0)$; the Hermitian subspace, $B$ and $H$ of signature $(4,0)$ and $N$ and $K$ of signature $(1,3)$; and the anti-Hermitian subspace, $B$ of signature $(0,4)$, $N$ of signature $(3,1)$, $H$ of signature $(4,0)$ and $K$ of signature $(1,3)$. Only $H$ is definite on the six; $N$ is definite on the quaternion subspace and its imaginary translate alone, $B$ on the two sectors alone, and $K$ on the centre and the vector subspace alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the four pairings: the bilinear, the general quaternionic bilinear, the sesquilinear and the general quaternionic sesquilinear form |
| $B,N,H,K$ | the four algebraic norms, the diagonals of the four pairings, of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces, the two real forms |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces; the informational and the material sector |
| $\tilde Q=Ae_0$ | the general element of the centre, $A\in\mathbb{C}$ |
| $\tilde Q=\sum_kP_ke_k$ | the general element of the vector subspace, $P_k\in\mathbb{C}$ |
| $h=\sum_\mu h_\mu e_\mu$ | the general element of the quaternion subspace, $h_\mu\in\mathbb{R}$ |
| $a_0e_0+i\mathbf p$, $ib_0e_0+\mathbf q$ | the general elements of the two sectors, $a_0,b_0\in\mathbb{R}$, $\mathbf p,\mathbf q$ real |
| $(p,q)$ | the signature over $\mathbb{R}$ of a real quadratic form |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the four algebraic norms, the reduction from the twelve products to four, and the separation of the multiplicative and the definite senses of the norm
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the convention of the four pairings — the one bracket, the four names, the pairs and the trace form — and for the readings of the four on the algebra and on the material sector
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section, with their defining conditions, bases and dimensions
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the coordinate blocks, the intersections and the sums of the six
- *The Six Subspaces and the Four Forms* (`articles_maths/the-six-subspaces-and-the-four-forms.md`), for the same six subspaces read at the level of the forms, with the value of each form on a general pair, its real and imaginary parts and the alternating companion of the two sesquilinear forms, of which the tables here are the diagonals
- *The Six Subspaces and the Four General Products* (`articles_maths/the-six-subspaces-and-the-four-general-products.md`), for the four general products read on the six subspaces, one subspace to a section
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four pairings and the four degree-two functions whose diagonals are the four algebraic norms, and their own restrictions to the six subspaces
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general forms and their Gram matrices
