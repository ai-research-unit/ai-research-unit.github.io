# __Remarkable Subspaces of the Complexoid and the Two Forms__

## Introduction

The two forms of the complex space, the plain bilinear form $\langle Q_1,Q_2\rangle=Q_1Q_2$ and the Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$, are read here on the two remarkable subspaces of the complex numbers, the real subspace $\mathbb{R}_{\mathbb{C}}$ and the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$. This article gives the restriction rule, the value of the two forms on a general pair of each subspace, their algebraic norms, their signatures and their null sets, and reports the sense in which the real subspace carries the definite form and the imaginary one its negative.

The restriction here is read on a base of dimension one over $\mathbb{R}$; the forms and their algebraic norms are those of *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, above this article in this category, and the subspaces are those of *Complexoid Subspaces*. The topological norm $|\cdot|=\sqrt{\langle\cdot\rangle_{*}}$ and the invertibility criterion are *Complex Norm and Invertibility*, below this article in this category.

**Conventions.** **Bar** is complex conjugation and the **Hermitian** mark is the bar, ${}^{*}=\bar{\cdot}$. Elements of the two subspaces are written $Q_1=q_1$ and $Q_2=q_2$ on the real subspace and $Q_1=iq'_1$ and $Q_2=iq'_2$ on the imaginary one; the letters $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ are the two forms and are never elements. The form $\langle\cdot,\cdot\rangle_{\natural}$ coincides with $\langle\cdot,\cdot\rangle$ here, and the form $\langle\cdot,\cdot\rangle_{\natural*}$ with $\langle\cdot,\cdot\rangle_{*}$; *Complex Norm and Invertibility*, below this article in this category, writes the positive definite norm as $\langle Q\rangle_{*}=Q\bar Q$, the algebraic norm of $\langle\cdot\rangle_{*}$, not as $\langle Q\rangle_{\natural}=Q^2$.

## The Restriction Rule

The **restriction** of a form $\varphi$ to a subspace $U$ is the form read on the elements of $U$,

$$
\varphi|_{U}(Q_1,Q_2)=\varphi(Q_1,Q_2)\qquad(Q_1,Q_2\in U),
$$

and the only thing that happens is that the two arguments are confined to the subspace. The symmetry is inherited, since the identity $\langle Q_1,Q_2\rangle=\langle Q_2,Q_1\rangle$ and the conjugate symmetry $\langle Q_1,Q_2\rangle_{*}=\overline{\langle Q_2,Q_1\rangle_{*}}$ hold in the ambient space and involve nothing outside $U$; the restriction is read off the coordinates of the two elements. Both subspaces are real lines, so every restriction is a form on a one-dimensional real space, and its rank is at most one.

## The Two Forms on the Real Subspace

On the real subspace the bar is the identity, so the two forms coincide, and both are the multiplication of the coordinates,

$$
\langle q_1,q_2\rangle=\langle q_1,q_2\rangle_{*}=q_1q_2.
$$

Both values are real, so the imaginary parts of the two forms vanish identically on the subspace; the algebraic norms are $\langle q_1\rangle=q_1^{2}$ and $\langle q_1\rangle_{*}=q_1^{2}$, the same square; both forms are positive definite, since $q_1^{2}>0$ for $q_1\neq0$; each has rank $1$ and is non-degenerate; and each has the null set $\{0\}$ alone, because $q_1^{2}=0$ forces $q_1=0$. The subspace carries one form, not two, and it is the definite one.

## The Two Forms on the Imaginary Subspace

On the imaginary subspace the bar is the negation, so the two forms differ by a sign, and both are real again,

$$
\langle iq'_1,iq'_2\rangle=(iq'_1)(iq'_2)=-q'_1q'_2,\qquad \langle iq'_1,iq'_2\rangle_{*}=(iq'_1)\overline{(iq'_2)}=+q'_1q'_2.
$$

The two forms are therefore the negative of each other on the subspace, $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{*}$, and their common value is real, so the imaginary parts vanish there as well. The algebraic norms are opposite,

$$
\langle iq'_1\rangle=(iq'_1)^{2}=-q'^2_1,\qquad \langle iq'_1\rangle_{*}=(iq'_1)\overline{(iq'_1)}=+q'^2_1=-\langle iq'_1\rangle,
$$

so the algebraic norm of $\langle\cdot\rangle$ is the negative square and the algebraic norm of $\langle\cdot\rangle_{*}$ the positive one. The form $\langle\cdot,\cdot\rangle$ is **negative definite** on the subspace, its value $-q'^2_1$ vanishing only at the origin; the form $\langle\cdot,\cdot\rangle_{*}$ is **positive definite**, its value $+q'^2_1$ vanishing only at the origin; each has rank $1$, is non-degenerate, and has the null set $\{0\}$ alone.

The subspace contains no nonzero isotropic element of either form. This is the anisotropy of the two forms met in *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, above this article in this category, where $\langle Q\rangle=Q^{2}$ and $\langle Q\rangle_{*}=|Q|^{2}$ vanish only together with $Q$.

## The Table of the Two

The two forms on the two subspaces, with the coordinates $q_1$ and $q_2$ on the real subspace and $q'_1$ and $q'_2$ on the imaginary one.

| subspace | $\langle\cdot,\cdot\rangle$ | $\langle\cdot,\cdot\rangle_{*}$ | algebraic norm of $\langle\cdot\rangle$ | algebraic norm of $\langle\cdot\rangle_{*}$ | imaginary part | signature of the restriction | null set |
|---|---|---|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $q_1q_2$ | $q_1q_2$ | $q_1^{2}$ | $q_1^{2}$ | zero | $(1,0)$ for both | $\{0\}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $-q'_1q'_2$ | $+q'_1q'_2$ | $-q'^2_1$ | $+q'^2_1$ | zero | $(0,1)$ for $\langle\cdot,\cdot\rangle$, $(1,0)$ for $\langle\cdot,\cdot\rangle_{*}$ | $\{0\}$ |

Three readings of the table. The **two forms coincide on the real subspace** and are **opposite on the imaginary one**, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{*}$. The **real subspace carries the definite form and the imaginary one its negative**, in the sense that $\langle\cdot,\cdot\rangle$ is positive definite on $\mathbb{R}_{\mathbb{C}}$ and negative definite on $i\mathbb{R}_{\mathbb{C}}$, while $\langle\cdot,\cdot\rangle_{*}$ is positive definite on both. And the **imaginary part of each form vanishes** on each subspace, so each restriction is a real symmetric bilinear form recovered from its own algebraic norm.

## Summary

On the real subspace the two forms of the complex space coincide, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{*}=q_1q_2$, both real-valued and positive definite, with the same algebraic norm $q_1^{2}$, rank $1$ and null set $\{0\}$. On the imaginary subspace the two forms are opposite, $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{*}$, with $\langle\cdot,\cdot\rangle=-q'_1q'_2$ negative definite and $\langle\cdot,\cdot\rangle_{*}=+q'_1q'_2$ positive definite, the algebraic norms $-q'^2_1$ and $+q'^2_1$, rank $1$ and null set $\{0\}$ each. The two forms are therefore told apart by their restriction to the imaginary subspace and not by their restriction to the real one, where they agree; the real subspace carries the definite form and the imaginary one its negative, and the imaginary parts of both forms vanish on both subspaces. The reading is a collapse: two forms in place of four, the two real lines in place of the six possible subspaces, and no nonzero isotropic element anywhere.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | the real subspace, elements $Q_1=q_1$, real dimension $1$ |
| $i\mathbb{R}_{\mathbb{C}}$ | the imaginary subspace, elements $Q_1=iq'_1$, real dimension $1$ |
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | the general plain bilinear form, equal to $\langle\cdot,\cdot\rangle_{\natural}$ |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | the Hermitian form, equal to $\langle\cdot,\cdot\rangle_{\natural*}$ |
| $\varphi|_U$ | the restriction of a form to a subspace |
| $(1,0)$, $(0,1)$ | the signatures of the definite and the negative definite restriction |
| $\{0\}$ | the null set of each of the four restrictions |

## Further Reading

- [The Two Forms and the Two Algebraic Norms of the Complexoid Space](the-two-forms-and-the-two-algebraic-norms-of-the-complexoid-space.html), above this article in this category, for the two forms, their algebraic norms and their definiteness.
- [Complexoid Subspaces](complexoid-subspaces.html), for the two subspaces, their bases and their dimensions.
- [Complex Norm and Invertibility](complex-norm-and-invertibility.html), below this article in this category, for the definite norm that the two restrictions carry.
