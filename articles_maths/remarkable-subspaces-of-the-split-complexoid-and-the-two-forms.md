# __Remarkable Subspaces of the Split-Complexoid and the Two Forms__

## Introduction

The two forms of the split-complex space, the symmetric bilinear form $\langle Q_1,Q_2\rangle=Q_1Q_2$ and the conjugate-symmetric Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2}$, are read here on the four distinguished lines of the algebra — the real line $\mathbb{R}_{\mathbb{D}}$, the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, and the two idempotent lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$ — one line to a section, with the table of the restrictions below and the value on a general pair displayed for each.

The forms and their norms are *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*; the four lines, their bases and dimensions are *Split-Complexoid Subspaces*; the restriction of a form to a subspace is stated once and is not re-derived. The products read on the same lines are *Remarkable Subspaces and the Two Products of the Split-Complexoid Space*, above this article in this category. This article owns the **value of the two forms on each line, their ranks and their null sets, and the picture of the level sets of the Hermitian norm**.

**The reading fixed here.** The bar is the conjugation $j\mapsto-j$ and ${}^{*}=\bar{\cdot}$; the algebra is commutative. In this article $Q_1=q_1+jq'_1$ and $Q_2=q_2+jq'_2$ are elements, so $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{*}$ name forms and norms only, and $\Pi_1=\tfrac12(1+j)$, $\Pi_2=\tfrac12(1-j)$.

## The Restriction Rule

The **restriction** of a form $\varphi$ to a subspace $U$ is the form read on the elements of $U$,

$$
\varphi|_U(Q_1,Q_2)=\varphi(Q_1,Q_2)\big|_{Q_1,Q_2\in U},
$$

and restricting changes only the two arguments. Symmetry is inherited by the bilinear form and conjugate-symmetry by the Hermitian form; the value on a general pair is read off the coordinates of the two elements. This is the restriction rule of the two forms, quoted here and not re-proved. The only thing that is new on $\mathbb{D}$ is that the two forms, which agree on the real line, differ elsewhere, and that the two idempotent lines annihilate the Hermitian form.

## The Real Subspace

On $\mathbb{R}_{\mathbb{D}}$ the elements are real, $Q_1=q_1$, $Q_2=q_2$, with $q'_1,q'_2=0$. The two forms coincide and are the product of the two real coordinates:

$$
\langle q_1,q_2\rangle=q_1q_2,
\qquad
\langle q_1,q_2\rangle_{*}=q_1\overline{q_2}=q_1q_2 .
$$

Both are real-valued, symmetric, non-degenerate and of **rank $1$**; the algebraic norm is the square $q_1^2$, positive definite; the null set is the origin alone. So the real line is the definite line of both forms, and the two forms are indistinguishable on it. This is the line where the two products agree, and the form reading agrees with the product reading.

## The Split Imaginary Subspace

On $j\mathbb{R}_{\mathbb{D}}$ the elements are $Q_1=jq'_1$, $Q_2=jq'_2$. The product is computed with $j^2=+1$, and the conjugation is $\overline{jq'_2}=-jq'_2$:

$$
\langle jq'_1,jq'_2\rangle=(jq'_1)(jq'_2)=q'_1q'_2,
\qquad
\langle jq'_1,jq'_2\rangle_{*}=jq'_1\overline{jq'_2}=jq'_1(-jq'_2)=-q'_1q'_2 .
$$

The two forms no longer coincide: the bilinear form is $+q'_1q'_2$ and the Hermitian form is $-q'_1q'_2$. Both are real-valued and of rank $1$, with null set the origin, but the bilinear form is **positive definite** on the line and the Hermitian form is **negative definite**. The algebraic norms are $(q'_1)^2$ and $-(q'_1)^2$.

This is the first place where the split sign separates the two forms. On the complex field both forms take the value $-a'^2$ on the anti-fixed line, because $(ia')(ic')=-a'c'$ and $ia'\overline{ic'}=ia'(-ic')=-a'c'$ agree; here the bilinear product loses the sign through $j^2=+1$ while the conjugation keeps it, and the two forms part. So the Hermitian form is positive on the real line and negative on the split imaginary line, the signature of its realification being $(1,1)$; the bilinear form is positive on both, the signature of its realification being $(2,0)$.

## The Two Idempotent Lines

On an idempotent line the element is $Q_1=\lambda\Pi_i$, with $\lambda$ real, and the conjugate is the other idempotent,

$$
\overline{\Pi_1}=\Pi_2,
\qquad
\overline{\Pi_2}=\Pi_1,
\qquad
\Pi_1\Pi_2=0 .
$$

The Hermitian form therefore vanishes on the line:

$$
\langle \lambda\Pi_i,\mu\Pi_i\rangle_{*}=\lambda\mu\,\Pi_i\overline{\Pi_i}=\lambda\mu\,\Pi_i\Pi_{3-i}=0 ,
$$

because the conjugate of an idempotent is the complementary one and the two multiply to zero. So each idempotent line is **totally isotropic** for $\langle\cdot,\cdot\rangle_{*}$: the restriction of $\langle\cdot,\cdot\rangle_{*}$ to the line is the zero form, of **rank $0$**, and its null set is the whole line. The line, which is the null cone, the zero divisors together with the origin (*Zero Divisors of the Split-Complex Algebra*, below this article in this category), is exactly the set where the Hermitian norm vanishes, $\langle \lambda\Pi_i\rangle_{*}=0$.

The bilinear form does not vanish there:

$$
\langle \lambda\Pi_i,\mu\Pi_i\rangle=\lambda\mu\,\Pi_i^2=\lambda\mu\,\Pi_i\in\mathbb{R}\Pi_i,
$$

a non-zero element of the line for $\lambda,\mu\neq0$, so the restriction of $\langle\cdot,\cdot\rangle$ to the line has **rank $1$** and null set the origin. The two lines are orthogonal to each other for $\langle\cdot,\cdot\rangle$, $\langle \Pi_1,\Pi_2\rangle=\Pi_1\Pi_2=0$, while for $\langle\cdot,\cdot\rangle_{*}$ they are not, $\langle \Pi_1,\Pi_2\rangle_{*}=\Pi_1\bar\Pi_2=\Pi_1\Pi_1=\Pi_1$. The two forms thus behave in opposite ways on the finest pieces of the algebra.

| line | $\langle\cdot,\cdot\rangle$ on a general pair | $\langle\cdot,\cdot\rangle_{*}$ on a general pair | rank $\langle\cdot,\cdot\rangle$ | rank $\langle\cdot,\cdot\rangle_{*}$ | null set of $\langle\cdot,\cdot\rangle_{*}$ |
|---|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $q_1q_2$ | $q_1q_2$ | $1$ | $1$ | $\{0\}$ |
| $j\mathbb{R}_{\mathbb{D}}$ | $q'_1q'_2$ | $-q'_1q'_2$ | $1$ | $1$ | $\{0\}$ |
| $\mathbb{R}\Pi_1$ | $\lambda\mu\Pi_1$ | $0$ | $1$ | $0$ | the whole line |
| $\mathbb{R}\Pi_2$ | $\lambda\mu\Pi_2$ | $0$ | $1$ | $0$ | the whole line |

## The Level Sets of the Hermitian Norm

The algebraic norm of $\langle\cdot\rangle_{*}$ is the norm $\langle Q\rangle_{*}=q^2-q'^2$, and its level sets are the object that replaces the circles of the complex case. With $Q=q+jq'$,

$$
\langle Q\rangle_{*}=c\iff q^2-q'^2=c .
$$

For $c>0$ this is a pair of hyperbolas with transverse axis the real line $\mathbb{R}_{\mathbb{D}}$, with vertices at $q=\sqrt c$ and $q=-\sqrt c$; for $c<0$ a pair of hyperbolas with transverse axis the split imaginary line $j\mathbb{R}_{\mathbb{D}}$; and for $c=0$ the degenerate pair of lines $q=q'$ and $q=-q'$, which are the two idempotent lines. So the **two families of hyperbolas**, one spacelike and one timelike, replace the two families of circles of the complex case, and the degenerate level $c=0$ is the null cone itself, the pair of lines on which the form is isotropic and the ring has its zero divisors.

On $\mathbb{C}$ the same construction gives $\lvert A\rvert^2=c$, a circle for every $c>0$ and the single point $A=0$ for $c=0$. The difference is the sign: the complex form is definite, so its positive level sets are circles and the zero level is a point; the split form is indefinite, so its two non-zero level sets are the two families of hyperbolas and its zero level is the two lines. The unit level $c=1$, the unit hyperbola, is the carrier of the group of hyperbolic rotations of *The Matrix Element Representations of the Split-Complexoid*, above this article in this category.

## Comparison with the Complex Interpretation

On the complex field the Hermitian form is definite on both of its subspaces: $\langle a\rangle_{*}=a^2$ on the real line and $\langle ia'\rangle_{*}=a'^2$ on the pure imaginary line, both positive definite with null set the origin, and $\mathbb{C}$ has no idempotent line at all, because it has no non-trivial idempotents. So on $\mathbb{C}$ the Hermitian form is definite everywhere, and the level sets are circles.

On $\mathbb{D}$ the Hermitian form is definite on each of the two eigenlines, with **opposite signs** — positive on $\mathbb{R}_{\mathbb{D}}$, negative on $j\mathbb{R}_{\mathbb{D}}$ — and is identically zero on each of the two idempotent lines. It is therefore not definite on $\mathbb{D}$, and the difference is produced by the two objects that $\mathbb{D}$ has and $\mathbb{C}$ does not: the sign $j^2=+1$, which flips the anti-fixed line to negative, and the two idempotents $\Pi_{1,2}$, on whose lines the form collapses to the zero form. The bilinear form, by contrast, is positive definite on both eigenlines and non-degenerate on both idempotent lines, and it is the form that stays faithful to the product everywhere.

## Summary

The symmetric bilinear form $\langle\cdot,\cdot\rangle$ and the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ of the split-complex space are read on the four distinguished lines. On the real line the two forms coincide and are the product $q_1q_2$, positive definite of rank $1$ with null set the origin. On the split imaginary line they part, $\langle\cdot,\cdot\rangle=+q'_1q'_2$ and $\langle\cdot,\cdot\rangle_{*}=-q'_1q'_2$, both of rank $1$ and null set the origin, the one positive definite and the other negative definite; this sign is the split sign. On the two idempotent lines the Hermitian form vanishes identically, each line being totally isotropic of rank $0$, while the bilinear form has rank $1$ with null set the origin and is orthogonal on the two lines.

The level sets of the Hermitian norm $\langle\cdot\rangle_{*}=q^2-q'^2$ are two families of hyperbolas, spacelike for $c>0$ and timelike for $c<0$, with the degenerate level $\langle\cdot\rangle_{*}=0$ the two idempotent lines, the null cone of the zero divisors; they replace the circles of the complex case, whose definite Hermitian form has circles as positive level sets and a point as its zero level. The Hermitian form is definite on each eigenline but of opposite signs on the two, and zero on the idempotent lines, so on $\mathbb{D}$ it is not definite; the bilinear form, definite on the eigenlines and non-degenerate on the idempotent lines, is the one the product leaves faithful.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | the symmetric bilinear form |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2}$ | the Hermitian form |
| $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ | the real and split imaginary lines |
| $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ | the idempotent lines, totally isotropic for $\langle\cdot,\cdot\rangle_{*}$ |
| $\langle Q\rangle_{*}=q^2-q'^2$ | the Hermitian norm, the algebraic norm of $\langle\cdot\rangle_{*}$ |
| $q=q'$ and $q=-q'$ | the null cone, the two idempotent lines |
| $q^2-q'^2=c$ | the level hyperbolas of $\langle\cdot\rangle_{*}$ |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex plane, its null lines and the hyperbolas of its norm.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic vectors, totally isotropic subspaces and signature in dimension two.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the isotropic lines of the split-complex algebra and its Clifford reading.
