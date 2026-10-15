# __Remarkable Subspaces of the Complexoid and the Two Forms__

## Introduction

The two forms of the complex space, the plain bilinear form $B(A,C)=AC$ and the Hermitian form $H(A,C)=A\bar C$, are read here on the two remarkable subspaces of the complex numbers, the real subspace $\mathbb{R}_{\mathbb{C}}$ and the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$. This article gives the restriction rule, the value of the two forms on a general pair of each subspace, their algebraic norms, their signatures and their null sets, and reports the sense in which the real subspace carries the definite form and the imaginary one its negative.

The restriction here is read on a base of dimension one over $\mathbb{R}$; the forms and their algebraic norms are those of *The Two Forms and the Two Algebraic Norms of the Complex Space*, above this article in this category, and the subspaces are those of *Complex Subspaces*. The topological norm $|\cdot|=\sqrt{H}$ and the invertibility criterion are *Complex Norm and Invertibility*, below this article in this category.

**Conventions.** **Bar** is complex conjugation and the **Hermitian** mark is the bar, ${}^{*}=\bar{\cdot}$. Elements of the two subspaces are written $A=a$ and $C=c$ on the real subspace and $A=ia'$ and $C=ic'$ on the imaginary one; the letters $B$ and $H$ are the two forms and are never elements. The form $N$ coincides with $B$ here, and the form $K$ with $H$; the letter $N$ with one argument is the positive definite norm of *Complex Norm and Invertibility*, below this article in this category.

## The Restriction Rule

The **restriction** of a form $\varphi$ to a subspace $U$ is the form read on the elements of $U$,

$$
\varphi|_{U}(A,C)=\varphi(A,C)\qquad(A,C\in U),
$$

and the only thing that happens is that the two arguments are confined to the subspace. The symmetry is inherited, since the identity $B(A,C)=B(C,A)$ and the conjugate symmetry $H(A,C)=\overline{H(C,A)}$ hold in the ambient space and involve nothing outside $U$; the restriction is read off the coordinates of the two elements. Both subspaces are real lines, so every restriction is a form on a one-dimensional real space, and its rank is at most one.

## The Two Forms on the Real Subspace

On the real subspace the bar is the identity, so the two forms coincide, and both are the multiplication of the coordinates,

$$
B(a,c)=H(a,c)=ac.
$$

Both values are real, so the imaginary parts of the two forms vanish identically on the subspace; the algebraic norms are $B(a)=a^{2}$ and $H(a)=a^{2}$, the same square; both forms are positive definite, since $a^{2}>0$ for $a\neq0$; each has rank $1$ and is non-degenerate; and each has the null set $\{0\}$ alone, because $a^{2}=0$ forces $a=0$. The subspace carries one form, not two, and it is the definite one.

## The Two Forms on the Imaginary Subspace

On the imaginary subspace the bar is the negation, so the two forms differ by a sign, and both are real again,

$$
B(ia',ic')=(ia')(ic')=-a'c',\qquad H(ia',ic')=(ia')\overline{(ic')}=+a'c'.
$$

The two forms are therefore the negative of each other on the subspace, $B=-H$, and their common value is real, so the imaginary parts vanish there as well. The algebraic norms are opposite,

$$
B(ia')=(ia')^{2}=-a'^{2},\qquad H(ia')=(ia')\overline{(ia')}=+a'^{2}=-B(ia'),
$$

so the algebraic norm of $B$ is the negative square and the algebraic norm of $H$ the positive one. The form $B$ is **negative definite** on the subspace, its value $-a'^{2}$ vanishing only at the origin; the form $H$ is **positive definite**, its value $+a'^{2}$ vanishing only at the origin; each has rank $1$, is non-degenerate, and has the null set $\{0\}$ alone.

The subspace contains no nonzero isotropic element of either form. This is the anisotropy of the two forms met in *The Two Forms and the Two Algebraic Norms of the Complex Space*, above this article in this category, where $B(A)=A^{2}$ and $H(A)=|A|^{2}$ vanish only together with $A$.

## The Table of the Two

The two forms on the two subspaces, with the coordinates $a$ on the real subspace and $a'$ on the imaginary one.

| subspace | $B$ | $H$ | algebraic norm of $B$ | algebraic norm of $H$ | imaginary part | signature of the restriction | null set |
|---|---|---|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $ac$ | $ac$ | $a^{2}$ | $a^{2}$ | zero | $(1,0)$ for both | $\{0\}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $-a'c'$ | $+a'c'$ | $-a'^{2}$ | $+a'^{2}$ | zero | $(0,1)$ for $B$, $(1,0)$ for $H$ | $\{0\}$ |

Three readings of the table. The **two forms coincide on the real subspace** and are **opposite on the imaginary one**, $B=H$ and $B=-H$. The **real subspace carries the definite form and the imaginary one its negative**, in the sense that $B$ is positive definite on $\mathbb{R}_{\mathbb{C}}$ and negative definite on $i\mathbb{R}_{\mathbb{C}}$, while $H$ is positive definite on both. And the **imaginary part of each form vanishes** on each subspace, so each restriction is a real symmetric bilinear form recovered from its own algebraic norm.

## Summary

On the real subspace the two forms of the complex space coincide, $B=H=ac$, both real-valued and positive definite, with the same algebraic norm $a^{2}$, rank $1$ and null set $\{0\}$. On the imaginary subspace the two forms are opposite, $B=-H$, with $B=-a'c'$ negative definite and $H=+a'c'$ positive definite, the algebraic norms $-a'^{2}$ and $+a'^{2}$, rank $1$ and null set $\{0\}$ each. The two forms are therefore told apart by their restriction to the imaginary subspace and not by their restriction to the real one, where they agree; the real subspace carries the definite form and the imaginary one its negative, and the imaginary parts of both forms vanish on both subspaces. The reading is a collapse: two forms in place of four, the two real lines in place of the six possible subspaces, and no nonzero isotropic element anywhere.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | the real subspace, elements $A=a$, real dimension $1$ |
| $i\mathbb{R}_{\mathbb{C}}$ | the imaginary subspace, elements $A=ia'$, real dimension $1$ |
| $B(A,C)=AC$ | the general plain bilinear form, equal to $N$ |
| $H(A,C)=A\bar C$ | the Hermitian form, equal to $K$ |
| $\varphi|_U$ | the restriction of a form to a subspace |
| $(1,0)$, $(0,1)$ | the signatures of the definite and the negative definite restriction |
| $\{0\}$ | the null set of each of the four restrictions |

## Further Reading

- *The Two Forms and the Two Algebraic Norms of the Complex Space*, above this article in this category, for the two forms, their algebraic norms and their definiteness.
- *Complex Subspaces* (`articles_maths/complexoid-subspaces.md`), for the two subspaces, their bases and their dimensions.
- *Complex Norm and Invertibility* (`articles_maths/complex-norm-and-invertibility.md`), below this article in this category, for the definite norm that the two restrictions carry.
