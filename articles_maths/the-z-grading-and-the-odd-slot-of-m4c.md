# __The $\mathbb{Z}$-Grading and the Odd Slot of $M_4(\mathbb{C})$__

## Introduction

The Clifford algebra of a four-dimensional space has sixteen basis elements, and they are usually grouped by **grade**: one scalar, four vectors, six bivectors, four trivectors, one pseudoscalar. The grouping is the visible form of the $\mathbb{Z}$-grading of the exterior algebra. The Clifford algebra itself is not $\mathbb{Z}$-graded: the product of two vectors has a scalar part and a bivector part, so the grade is not additive on the product. What the Clifford algebra has is a $\mathbb{Z}$-**filtration**, whose associated graded algebra is the exterior algebra; the parity is the only grading that survives on the algebra itself.

The biquaternion algebra is the even part. Its product sees the parity and nothing finer: the product of two even elements is even, and the split of the even part into scalars, bivectors and pseudoscalars is not visible in the multiplication table of $\mathbb{B}$ alone. The odd slot is worse: it is a copy of $\mathbb{B}$, of real dimension eight, and the product of two odd elements is even, but the split of the odd slot into four vectors and four trivectors is not a submodule split. Left multiplication by an even element mixes the two.

The sixteen two-sided operators $T_{\mu\nu}=L_\mu R_\nu$ give the exact dictionary. Each of them is one Clifford basis element up to a scalar $\pm1$ or $\pm i$, and the table of their grades is the dictionary between the two-sided index pair and the Clifford grade. The table is not a function of the indices alone: the four vectors are $T_{tx},T_{xy},T_{yy},T_{zy}$, a staircase, not a row or a column. The frame is the choice of that staircase.

This article fixes the two gradings, describes the odd slot, gives the grade table of the sixteen two-sided operators, and states what the biquaternion product can and cannot see. The Clifford frame is *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*; the two-sided basis is *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*; the even slot and the odd slot are *Biquaternion Versors and the Orthogonal Group*; the traces that read the scalar and pseudoscalar coordinates are *The Vector and the Axial Traces of $M_4(\mathbb{C})$*.

## The Two Gradings

**The parity grading.** The Clifford algebra is
$$
\mathrm{Cl}(V)=\mathrm{Cl}^{0}\oplus\mathrm{Cl}^{1},
$$
the even and odd parts, with
$$
\mathrm{Cl}^{i}\mathrm{Cl}^{j}\subseteq\mathrm{Cl}^{i+j\bmod 2}.
$$
The grade involution $\alpha$ is $+1$ on $\mathrm{Cl}^{0}$ and $-1$ on $\mathrm{Cl}^{1}$; it is an automorphism. The even part is the biquaternion algebra,
$$
\mathrm{Cl}^{0}\cong\mathbb{B}\cong M_2(\mathbb{C}),
$$
of real dimension eight; the odd part is a copy of it, $\mathrm{Cl}^{1}=\mathbb{B}u$ for any non-isotropic $u\in V$.

**The filtration.** For $k=0,1,2,3,4$, let $\mathrm{Cl}^{\le k}$ be the span of the products of at most $k$ vectors. Then
$$
\mathrm{Cl}^{\le0}\subset\mathrm{Cl}^{\le1}\subset\mathrm{Cl}^{\le2}\subset\mathrm{Cl}^{\le3}\subset\mathrm{Cl}^{\le4}=\mathrm{Cl},
$$
with
$$
\dim\mathrm{Cl}^{\le k}=\sum_{j=0}^{k}\binom{4}{j},
\qquad
\dim\mathrm{Cl}^{\le4}=1+4+6+4+1=16 .
$$
The associated graded algebra is the exterior algebra:
$$
\operatorname{gr}\mathrm{Cl}\cong\Lambda^{\bullet}V,
\qquad
\dim\Lambda^{k}V=\binom{4}{k}.
$$
The symbol map sends the filtration layer $\mathrm{Cl}^{\le k}$ to the quotient $\mathrm{Cl}^{\le k}/\mathrm{Cl}^{\le k-1}\cong\Lambda^{k}V$; the Clifford product is the exterior product plus contractions, and the contractions are what destroy the $\mathbb{Z}$-grading.

**The precise statement.** The Clifford algebra is **$\mathbb{Z}$-filtered**, not $\mathbb{Z}$-graded. The $\mathbb{Z}$-grading lives on the exterior algebra $\Lambda^{\bullet}V$, which is the associated graded. The parity is the mod-two reduction of the filtration; it is a genuine grading of $\mathrm{Cl}$, and it is the only one.

**The dimensions.**

| grade | basis | dimension | parity |
|---|---|---|---|
| 0 | $I$ | 1 | even |
| 1 | $\gamma^\mu$ | 4 | odd |
| 2 | $\gamma^{\mu\nu}$ | 6 | even |
| 3 | $\gamma^{\mu\nu\rho}$ | 4 | odd |
| 4 | $\gamma^5$ | 1 | even |

The even part has dimension $1+6+1=8$; the odd part has dimension $4+4=8$. The odd slot is therefore the sum of the vector and trivector grades, not one grade.

## The Odd Slot

**The split.** As a real vector space,
$$
\mathrm{Cl}^{1}=V\oplus\Lambda^{3}V,
\qquad
\dim V=4,\quad\dim\Lambda^{3}V=4 .
$$
The four vectors are the $\gamma^\mu$; the four trivectors are the $\gamma^{\mu\nu\rho}$. The split is the grade split of the odd part.

**The module structure.** The odd slot is a left $\mathbb{B}$-module, $\mathrm{Cl}^{1}=\mathbb{B}u$, of real dimension eight. The left multiplication by an even element preserves the parity but not the grade: a bivector times a vector is a vector plus a trivector,
$$
\gamma^{\mu\nu}\gamma^{\rho}
=\gamma^{\mu\nu\rho}+g^{\nu\rho}\gamma^{\mu}-g^{\mu\rho}\gamma^{\nu},
$$
so the split $V\oplus\Lambda^{3}V$ is **not** a $\mathbb{B}$-submodule split. The odd slot is a copy of $\mathbb{B}$ as a module, but the copy does not respect the vector/trivector split. This is the algebraic reason the split is recovered from the frame, not from the module.

**The Hodge duality.** The four-dimensional Hodge star gives a linear isomorphism
$$
*:\Lambda^{1}V\longrightarrow\Lambda^{3}V,
\qquad
\gamma^{\mu}\longmapsto \gamma^{\mu\nu\rho}\propto\varepsilon^{\mu\nu\rho\sigma}\gamma_{\sigma}\gamma^{5},
$$
with $*^2=\pm1$ on the odd slot. The four pairs
$$
(\gamma^{0},\gamma^{123}),\quad
(\gamma^{1},\gamma^{023}),\quad
(\gamma^{2},\gamma^{013}),\quad
(\gamma^{3},\gamma^{012})
$$
are the Hodge pairs. Each pair spans a two-dimensional subspace of the odd slot. The Hodge star exchanges the vector and the trivector of the pair, and the Clifford product of the two is a scalar plus a scalar multiple of the pseudoscalar.

**The product rule.** With $u$ a unit timelike vector and $\mathrm{Cl}^{1}=\mathbb{B}u$, let $\theta(c)=ucu^{-1}$ be the conjugation by $u$, an automorphism of $\mathbb{B}$. Then
$$
(b_1+b_2u)(c_1+c_2u)=\bigl(b_1c_1+b_2\theta(c_2)\bigr)+\bigl(b_1c_2+b_2\theta(c_1)\bigr)u,
$$
for $b_1,b_2,c_1,c_2\in\mathbb{B}$. The twist $\theta$ is the reflection of the bivectors that the vector $u$ defines; it is not the identity on the whole of $\mathbb{B}$, because an even element need not commute with $u$. The twisted rule is the multiplication of the Clifford algebra written over its even part. The product of two odd elements is even, and the product of an even and an odd element is odd; this is the parity grading in operation form.

## The Sixteen Two-Sided Operators

**The theorem.** Each $T_{\mu\nu}=L_\mu R_\nu$ is exactly one Clifford basis element up to a scalar $\pm1$ or $\pm i$. The table is the following; the entry is the Clifford element and its grade.

| $T_{\mu\nu}$ | $\nu=t$ | $\nu=x$ | $\nu=y$ | $\nu=z$ |
|---|---|---|---|---|
| $\mu=t$ | $I$ (0) | $-i\gamma^{0}$ (1) | $i\gamma^{123}$ (3) | $i\gamma^{5}$ (4) |
| $\mu=x$ | $\gamma^{23}$ (2) | $-i\gamma^{023}$ (3) | $-i\gamma^{1}$ (1) | $\gamma^{01}$ (2) |
| $\mu=y$ | $-\gamma^{13}$ (2) | $i\gamma^{013}$ (3) | $-i\gamma^{2}$ (1) | $\gamma^{02}$ (2) |
| $\mu=z$ | $\gamma^{12}$ (2) | $-i\gamma^{012}$ (3) | $-i\gamma^{3}$ (1) | $\gamma^{03}$ (2) |

**The verification.** The table follows from the definitions $L_\mu(x)=e_\mu x$, $R_\nu(x)=xe_\nu$, the multiplication table of the biquaternion units, and the correspondence
$$
e_t\mapsto I,\quad e_x\mapsto\gamma^{2}\gamma^{3},\quad e_y\mapsto\gamma^{3}\gamma^{1},\quad e_z\mapsto\gamma^{1}\gamma^{2},\quad i\mapsto i\gamma^{5}.
$$
Each product $e_\mu x e_\nu$ is a signed basis element, and the scalar $i$ is the pseudoscalar. The signs are those of the quaternion multiplication table; a direct computation gives the sixteen entries. $\square$

**The counts.** The table has one grade-0 entry, four grade-1 entries, six grade-2 entries, four grade-3 entries and one grade-4 entry:
$$
1+4+6+4+1=16 .
$$
The counts are the dimensions of the exterior algebra; the table is a bijection between the sixteen two-sided operators and the sixteen Clifford basis elements.

**The five gammas.** The frame is the five entries
$$
\gamma^{0}=iT_{tx},\qquad
\gamma^{1}=iT_{xy},\qquad
\gamma^{2}=iT_{yy},\qquad
\gamma^{3}=iT_{zy},\qquad
\gamma^{5}=-iT_{tz}.
$$
The first four are the four vectors; the last is the pseudoscalar. The four vectors are the staircase
$$
T_{tx},\ T_{xy},\ T_{yy},\ T_{zy},
$$
not a row and not a column. This is the exact sense in which the frame is a choice, not a property of the index pair.

**The Hodge pairs in the table.** The four vector entries are paired with the four trivector entries:
$$
T_{tx}\leftrightarrow T_{ty},\qquad
T_{xy}\leftrightarrow T_{xx},\qquad
T_{yy}\leftrightarrow T_{yx},\qquad
T_{zy}\leftrightarrow T_{zx}.
$$
Each pair is one Hodge pair $(\gamma^\mu,\gamma^{\nu\rho\sigma})$. The pattern is the frame written twice: the vector entry and its trivector partner differ by the exchange of the second index and the sign of the scalar $i$.

## What the Biquaternion Product Sees

**The parity.** The product of two even elements is even, and the product of an even and an odd element is odd. This is visible in the multiplication of $\mathbb{B}$ and in the rule for the odd slot; no frame is needed.

**The grade.** The grade is not visible. The multiplication table of $\mathbb{B}$ does not distinguish a scalar from a pseudoscalar: both are central in $\mathbb{B}$, and the product of two bivectors can be a scalar plus a pseudoscalar plus a bivector. The splitting into grades requires the frame, which supplies the $\gamma^\mu$ and hence the grade projectors.

**The central imaginary and the pseudoscalar.** In $\mathbb{B}$ the element $i$ is central. In $\mathrm{Cl}$ the pseudoscalar $\gamma^{5}$ is even but not central: it commutes with the even part and anticommutes with the odd part. The identification $i\mapsto i\gamma^{5}$ is an isomorphism of real algebras, but it does not preserve the centre in the ambient algebra: the image of the centre is the real plane spanned by $I$ and $i\gamma^{5}$, which is central in the even part and not in the whole Clifford algebra. This is the algebraic reason the chirality is not a scalar.

**The odd slot as an operation.** The odd elements are not in $\mathbb{B}$; as operations on $\mathbb{B}$ they are the bar and the left multiplications,
$$
\gamma^{0}=\bar{\cdot},\qquad
\gamma^{k}=\bar{\cdot}L_{-i e_k},
$$
in the real-linear dictionary. The grade of the operation is recovered from the frame, not from the biquaternion product. The operation-level statement is *The Star and the Conjugate-Linear Operators of $M_4(\mathbb{C})$*.

**The two dictionaries.** The complex-linear dictionary
$$
\gamma^{0}=R_{i e_x},\qquad
\gamma^{k}=L_{i e_k}R_{e_y},\qquad
\gamma^{5}=R_{-i e_z}
$$
uses the same five entries up to the scalar $i$; its even part is the complexified even Clifford algebra $M_2\oplus M_2$, not the left factor $\mathbb{B}$. The real-linear dictionary has the left factor as its even part. The grade table is the same in both, because it is a table of the same sixteen two-sided operators against the same abstract Clifford basis; the difference is which operators represent the frame, not the grades.

## The Frame Dependence

**The canonical part.** The filtration and the parity are canonical: they are defined by the Clifford algebra and the vector space $V$, with no choice of frame. The dimensions $1,4,6,4,1$ are canonical.

**The frame part.** The assignment of a grade to a particular $T_{\mu\nu}$ is frame-dependent. A different frame $\tilde\gamma^\mu=U\gamma^\mu U^{-1}$ gives a different five-element subset of the sixteen two-sided operators and a different staircase of vectors. The grade of the Clifford element is canonical; its expression in the two-sided basis is not.

**The invariant statement.** The correct invariant statement is: the sixteen two-sided operators are a Clifford basis up to scalars; the five gammas are a frame inside it; the grade table is the matrix of the change of basis between the two-sided basis and the Clifford basis. The table above is one such matrix, for the frame of the corpus.

## Summary

The Clifford algebra of four dimensions is $\mathbb{Z}$-filtered, with associated graded $\Lambda^{\bullet}V$ of dimensions $1,4,6,4,1$; it is $\mathbb{Z}/2$-graded by parity, and that is the only grading on the algebra itself. The even part is $\mathbb{B}$; the odd part is a copy of $\mathbb{B}$ of real dimension eight, split as four vectors plus four trivectors. The split is not a $\mathbb{B}$-submodule split; it is recovered from the frame by Hodge duality. The sixteen two-sided operators are exactly the sixteen Clifford basis elements up to $\pm1,\pm i$, with the grade table
$$
\begin{array}{c|cccc}
 & t & x & y & z\\ \hline
t & I & -i\gamma^0 & i\gamma^{123} & i\gamma^5\\
x & \gamma^{23} & -i\gamma^{023} & -i\gamma^1 & \gamma^{01}\\
y & -\gamma^{13} & i\gamma^{013} & -i\gamma^2 & \gamma^{02}\\
z & \gamma^{12} & -i\gamma^{012} & -i\gamma^3 & \gamma^{03}
\end{array}
$$
and the five gammas are $\gamma^0=iT_{tx}$, $\gamma^1=iT_{xy}$, $\gamma^2=iT_{yy}$, $\gamma^3=iT_{zy}$, $\gamma^5=-iT_{tz}$. The biquaternion product sees the parity and not the grade; the grade needs the frame. The odd slot is a copy of $\mathbb{B}$ as a module, but the vector/trivector split is not a module split, which is why the geometric content of the odd sector is carried by the dictionary rather than by the product.

| quantity | value |
|---|---|
| parity | $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, $\dim=8+8$ |
| filtration | $\operatorname{gr}\mathrm{Cl}\cong\Lambda^{\bullet}V$ |
| grade dimensions | $1,4,6,4,1$ |
| odd slot | $V\oplus\Lambda^3V$, $4+4$ |
| Hodge pairs | $(\gamma^0,\gamma^{123})$, $(\gamma^1,\gamma^{023})$, $(\gamma^2,\gamma^{013})$, $(\gamma^3,\gamma^{012})$ |
| five gammas | $iT_{tx},iT_{xy},iT_{yy},iT_{zy},-iT_{tz}$ |
| scalar | $T_{tt}=I$ |
| pseudoscalar | $T_{tz}=i\gamma^5$ |
| vectors | $T_{tx},T_{xy},T_{yy},T_{zy}$ |
| trivectors | $T_{ty},T_{xx},T_{yx},T_{zx}$ |
| bivectors | $T_{xt},T_{xz},T_{yt},T_{yz},T_{zt},T_{zz}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}(V)$ | the Clifford algebra of the Lorentzian four-space |
| $\mathrm{Cl}^{\le k}$ | the filtration layer of products of at most $k$ vectors |
| $\operatorname{gr}\mathrm{Cl}$ | the associated graded algebra, $\Lambda^{\bullet}V$ |
| $\alpha$ | the grade involution |
| $\gamma^\mu$ | the four vector gammas |
| $\gamma^{\mu\nu}$, $\gamma^{\mu\nu\rho}$ | the bivectors and trivectors |
| $\gamma^5$ | the pseudoscalar |
| $T_{\mu\nu}$ | the two-sided operator $L_\mu R_\nu$ |
| $\mathbb{B}$ | the biquaternion algebra, $\mathrm{Cl}^{0}$ |
| $V$ | the Lorentzian vector space, grade 1 |
| $\Lambda^3V$ | the trivector space, grade 3 |

## Further Reading

- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five gammas, the Clifford basis and the frame.
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the sixteen $T_{\mu\nu}$ and their multiplication table.
- [The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$](the-operators-of-the-peirce-decomposition-of-m4c.html), for $L_a$, $R_a$ and $T_{a,b}$.
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the even and odd slots of the envelope.
- [The Vector and the Axial Traces of $M_4(\mathbb{C})$](the-vector-and-the-axial-traces-of-m4c.html), for the two coordinates $T_{tt}$ and $T_{tz}$ that the traces read.
- [The Star and the Conjugate-Linear Operators of $M_4(\mathbb{C})$](the-star-and-the-conjugate-linear-operators-of-m4c.html), for the operation-level form of the odd generators.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the chirality and its relation to the pseudoscalar.
- [The Dirac Algebra and Biquaternions: A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html), for the explicit matrices and the even-part identification.
