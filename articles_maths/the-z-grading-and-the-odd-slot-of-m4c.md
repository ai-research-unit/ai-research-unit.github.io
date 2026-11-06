# __The $\mathbb{Z}$-Grading and the Odd Slot of $M_4(\mathbb{C})$__

## Introduction

The Clifford algebra of a four-dimensional space has sixteen basis elements, and they are usually grouped by **grade**: one scalar, four vectors, six bivectors, four trivectors, one pseudoscalar. The grouping is the visible form of the $\mathbb{Z}$-grading of the exterior algebra. The Clifford algebra itself is not $\mathbb{Z}$-graded: the product of two vectors has a scalar part and a bivector part, so the grade is not additive on the product. What the Clifford algebra has is a $\mathbb{Z}$-**filtration**, whose associated graded algebra is the exterior algebra; the parity is the only grading that survives on the algebra itself.

The biquaternion algebra is the even part. Its product sees the parity and nothing finer: the product of two even elements is even, and the split of the even part into scalars, bivectors and pseudoscalars is not visible in the multiplication table of $\mathbb{B}$ alone. The odd slot is worse: it is a copy of $\mathbb{B}$, of real dimension eight, and the product of two odd elements is even, but the split of the odd slot into four vectors and four trivectors is not a submodule split. Left multiplication by an even element mixes the two.

The sixteen two-sided operators $L_{\mathrm{pau},e_\mu} R_{\mathrm{pau},e_\nu}$ give the exact dictionary. Each of them is one Clifford basis element up to a scalar $\pm1$ or $\pm i$, and the table of their grades is the dictionary between the two-sided index pair and the Clifford grade. The table is not a function of the indices alone: the four vectors are $L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y}$, a staircase, not a row or a column. The frame is the choice of that staircase.

The body writes the abstract Clifford frame as $v_0,v_1,v_2,v_3$, with $v_0^2=1$ and $v_k^2=-1$, and the frame elements as cells. The gamma notation for the same objects is collected in the Gamma section. The two-sided basis is *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*; the even slot and the odd slot are *Biquaternion Versors and the Orthogonal Group*; the traces that read the scalar and pseudoscalar coordinates are *The Vector and the Axial Traces of $M_4(\mathbb{C})$*.

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
| 1 | $v_\mu$ | 4 | odd |
| 2 | $v_{\mu\nu}=v_\mu v_\nu$ | 6 | even |
| 3 | $v_{\mu\nu\rho}$ | 4 | odd |
| 4 | $\omega=v_0v_1v_2v_3$ | 1 | even |

The even part has dimension $1+6+1=8$; the odd part has dimension $4+4=8$. The odd slot is therefore the sum of the vector and trivector grades, not one grade.

## The Odd Slot

**The split.** As a real vector space,
$$
\mathrm{Cl}^{1}=V\oplus\Lambda^{3}V,
\qquad
\dim V=4,\quad\dim\Lambda^{3}V=4 .
$$
The four vectors are the $v_\mu$; the four trivectors are the $v_{\mu\nu\rho}$. The split is the grade split of the odd part.

**The module structure.** The odd slot is a left $\mathbb{B}$-module, $\mathrm{Cl}^{1}=\mathbb{B}u$, of real dimension eight. The left multiplication by an even element preserves the parity but not the grade: a bivector times a vector is a vector plus a trivector,
$$
\Lambda^{2}V\cdot V\subseteq\Lambda^{3}V\oplus V,
$$
the trivector part the exterior product and the vector part the contraction. The split $V\oplus\Lambda^{3}V$ is therefore **not** a $\mathbb{B}$-submodule split. The odd slot is a copy of $\mathbb{B}$ as a module, but the copy does not respect the vector/trivector split. This is the algebraic reason the split is recovered from the frame, not from the module.

**The Hodge duality.** The four-dimensional Hodge star gives a linear isomorphism
$$
*:\Lambda^{1}V\longrightarrow\Lambda^{3}V,
\qquad
*^2=\pm1
$$
on the odd slot. The four pairs
$$
(v_{0},v_{123}),\quad
(v_{1},v_{023}),\quad
(v_{2},v_{013}),\quad
(v_{3},v_{012})
$$
are the Hodge pairs. Each pair spans a two-dimensional subspace of the odd slot. The Hodge star exchanges the vector and the trivector of the pair, and the Clifford product of the two is a scalar plus a scalar multiple of the pseudoscalar $\omega$.

**The product rule.** With $u$ a unit timelike vector and $\mathrm{Cl}^{1}=\mathbb{B}u$, let $\mathrm{J}(c)=ucu^{-1}$ be the conjugation by $u$, an automorphism of $\mathbb{B}$. Then
$$
(b_1+b_2u)(c_1+c_2u)=\bigl(b_1c_1+b_2\mathrm{J}(c_2)\bigr)+\bigl(b_1c_2+b_2\mathrm{J}(c_1)\bigr)u,
$$
for $b_1,b_2,c_1,c_2\in\mathbb{B}$. The twist $\mathrm{J}$ is the reflection of the bivectors that the vector $u$ defines; it is not the identity on the whole of $\mathbb{B}$, because an even element need not commute with $u$. The twisted rule is the multiplication of the Clifford algebra written over its even part. The product of two odd elements is even, and the product of an even and an odd element is odd; this is the parity grading in operation form.

## The Sixteen Two-Sided Operators

**The theorem.** Each $L_{\mathrm{pau},e_\mu} R_{\mathrm{pau},e_\nu}$ is exactly one Clifford basis element up to a scalar $\pm1$ or $\pm i$. The table gives the element and its grade; the element is written in the frame $v_\mu$.

| $L_{\mathrm{pau},e_\mu} R_{\mathrm{pau},e_\nu}$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $I$ (0) | $-iv_{0}$ (1) | $iv_{123}$ (3) | $i\omega$ (4) |
| $\vec e_x$ | $v_{23}$ (2) | $-iv_{023}$ (3) | $-iv_{1}$ (1) | $v_{01}$ (2) |
| $\vec e_y$ | $-v_{13}$ (2) | $iv_{013}$ (3) | $-iv_{2}$ (1) | $v_{02}$ (2) |
| $\vec e_z$ | $v_{12}$ (2) | $-iv_{012}$ (3) | $-iv_{3}$ (1) | $v_{03}$ (2) |

**The verification.** The table follows from the definitions $L_{\mathrm{pau},e_\mu}(x)=e_\mu x$, $R_{\mathrm{pau},e_\nu}(x)=xe_\nu$, the multiplication table of the biquaternion units, and the correspondence
$$
e_t\mapsto I,\quad \vec e_x\mapsto v_{2}v_{3},\quad \vec e_y\mapsto v_{3}v_{1},\quad \vec e_z\mapsto v_{1}v_{2},\quad i\mapsto i\omega.
$$
Each product $e_\mu x e_\nu$ is a signed basis element, and the scalar $i$ is the pseudoscalar. The signs are those of the quaternion multiplication table; a direct computation gives the sixteen entries.

**The counts.** The table has one grade-0 entry, four grade-1 entries, six grade-2 entries, four grade-3 entries and one grade-4 entry:
$$
1+4+6+4+1=16 .
$$
The counts are the dimensions of the exterior algebra; the table is a bijection between the sixteen two-sided operators and the sixteen Clifford basis elements.

**The five cells of the frame.** The frame is the five entries
$$
iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\qquad
iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\qquad
iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\qquad
iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\qquad
-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}.
$$
The first four have grade 1; the last has grade 4. The four vectors are the staircase
$$
L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\ L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\ L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\ L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},
$$
not a row and not a column. This is the exact sense in which the frame is a choice, not a property of the index pair.

**The Hodge pairs in the table.** The four vector entries are paired with the four trivector entries:
$$
L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}\leftrightarrow L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_y},\qquad
L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y}\leftrightarrow L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_x},\qquad
L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}\leftrightarrow L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_x},\qquad
L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y}\leftrightarrow L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_x}.
$$
Each pair is one Hodge pair $(v_\mu,v_{\nu\rho\sigma})$. The pattern is the frame written twice: the vector entry and its trivector partner differ by the exchange of the second index and the sign of the scalar $i$.

## What the Biquaternion Product Sees

**The parity.** The product of two even elements is even, and the product of an even and an odd element is odd. This is visible in the multiplication of $\mathbb{B}$ and in the rule for the odd slot; no frame is needed.

**The grade.** The grade is not visible. The multiplication table of $\mathbb{B}$ does not distinguish a scalar from a pseudoscalar: both are central in $\mathbb{B}$, and the product of two bivectors can be a scalar plus a pseudoscalar plus a bivector. The splitting into grades requires the frame, which supplies the $v_\mu$ and hence the grade projectors.

**The central imaginary and the pseudoscalar.** In $\mathbb{B}$ the element $i$ is central. In $\mathrm{Cl}$ the pseudoscalar $\omega$ is even but not central: it commutes with the even part and anticommutes with the odd part. The identification $i\mapsto i\omega$ is an isomorphism of real algebras, but it does not preserve the centre in the ambient algebra: the image of the centre is the real plane spanned by $I$ and $i\omega$, which is central in the even part and not in the whole Clifford algebra. This is the algebraic reason the chirality is not a scalar.

**The odd slot as an operation.** The odd elements are not in $\mathbb{B}$; as operations on $\mathbb{B}$ they are the bar and the conjugate-linear left multiplications,
$$
\bar{\cdot},\qquad
\bar{\cdot}\,L_{-i \vec e_k},
$$
in the real-linear dictionary. The grade of the operation is recovered from the frame, not from the biquaternion product. The operation-level statement is *The Star and the Conjugate-Linear Operators of $M_4(\mathbb{C})$*.

**The two dictionaries.** The complex-linear dictionary reads the same five cells as one-sided and two-sided operators,
$$
iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}=R_{i \vec e_x},\qquad
iL_{i \vec e_k}R_{\mathrm{pau},\vec e_y},\qquad
-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}=R_{-i \vec e_z},
$$
up to the scalar $i$; its even part is the complexified even Clifford algebra $M_2\oplus M_2$, not the left factor $\mathbb{B}$. The real-linear dictionary has the left factor as its even part. The grade table is the same in both, because it is a table of the same sixteen two-sided operators against the same abstract Clifford basis; the difference is which operators represent the frame, not the grades.

## The Frame Dependence

**The canonical part.** The filtration and the parity are canonical: they are defined by the Clifford algebra and the vector space $V$, with no choice of frame. The dimensions $1,4,6,4,1$ are canonical.

**The frame part.** The assignment of a grade to a particular $L_{\mathrm{pau},e_\mu} R_{\mathrm{pau},e_\nu}$ is frame-dependent. A different frame $\tilde v_\mu=Uv_\mu U^{-1}$ gives a different five-element subset of the sixteen two-sided operators and a different staircase of vectors. The grade of the Clifford element is canonical; its expression in the two-sided basis is not.

**The invariant statement.** The correct invariant statement is: the sixteen two-sided operators are a Clifford basis up to scalars; the five cells are a frame inside it; the grade table is the matrix of the change of basis between the two-sided basis and the Clifford basis. The table above is one such matrix, for the frame of the corpus.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are the frame $v_\mu$ of the Clifford algebra written as $4\times4$ matrices; the body writes the cells.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z},
$$

with $\gamma_\mu=v_\mu$ and $\gamma_5=i\omega$ in the matrix representation.

The grade table in the gamma basis is
$$
\begin{array}{c|cccc}
 & t & x & y & z\\ \hline
t & I & -i\gamma_0 & i\gamma_{123} & i\gamma_5\\
x & \gamma_{23} & -i\gamma_{023} & -i\gamma_1 & \gamma_{01}\\
y & -\gamma_{13} & i\gamma_{013} & -i\gamma_2 & \gamma_{02}\\
z & \gamma_{12} & -i\gamma_{012} & -i\gamma_3 & \gamma_{03}
\end{array}
$$
with the correspondence $e_t\mapsto I$, $\vec e_x\mapsto\gamma_2\gamma_3$, $\vec e_y\mapsto\gamma_3\gamma_1$, $\vec e_z\mapsto\gamma_1\gamma_2$ and $i\mapsto i\gamma_5$.

Over $\mathbb{R}$ the dictionary is complex-linear: the products of the five span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

The Clifford algebra of four dimensions is $\mathbb{Z}$-filtered, with associated graded $\Lambda^{\bullet}V$ of dimensions $1,4,6,4,1$; it is $\mathbb{Z}/2$-graded by parity, and that is the only grading on the algebra itself. The even part is $\mathbb{B}$; the odd part is a copy of $\mathbb{B}$ of real dimension eight, split as four vectors plus four trivectors. The split is not a $\mathbb{B}$-submodule split; it is recovered from the frame by Hodge duality. The sixteen two-sided operators are exactly the sixteen Clifford basis elements up to $\pm1,\pm i$, with the grade table
$$
\begin{array}{c|cccc}
 & t & x & y & z\\ \hline
t & 0 & 1 & 3 & 4\\
x & 2 & 3 & 1 & 2\\
y & 2 & 3 & 1 & 2\\
z & 2 & 3 & 1 & 2
\end{array}
$$
and the five cells of the frame are $iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}$, $iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y}$, $iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}$, $iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y}$ and $-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$. The biquaternion product sees the parity and not the grade; the grade needs the frame. The odd slot is a copy of $\mathbb{B}$ as a module, but the vector/trivector split is not a module split, which is why the geometric content of the odd sector is carried by the dictionary rather than by the product.

| quantity | value |
|---|---|
| parity | $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, $\dim=8+8$ |
| filtration | $\operatorname{gr}\mathrm{Cl}\cong\Lambda^{\bullet}V$ |
| grade dimensions | $1,4,6,4,1$ |
| odd slot | $V\oplus\Lambda^3V$, $4+4$ |
| Hodge pairs | $(v_0,v_{123})$, $(v_1,v_{023})$, $(v_2,v_{013})$, $(v_3,v_{012})$ |
| five cells | $iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$ |
| scalar | $L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}=I$ |
| pseudoscalar | $L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$ up to $-i$ |
| vectors | $L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y}$ |
| trivectors | $L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_y},L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_x},L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_x},L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_x}$ |
| bivectors | $L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},e_t},L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_z},L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},e_t},L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_z},L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},e_t},L_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_z}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}(V)$ | the Clifford algebra of the Lorentzian four-space |
| $\mathrm{Cl}^{\le k}$ | the filtration layer of products of at most $k$ vectors |
| $\operatorname{gr}\mathrm{Cl}$ | the associated graded algebra, $\Lambda^{\bullet}V$ |
| $\alpha$ | the grade involution |
| $v_\mu$ | the four frame vectors of $V$ |
| $v_{\mu\nu}$, $v_{\mu\nu\rho}$ | the bivectors and trivectors |
| $\omega$ | the pseudoscalar, $v_0v_1v_2v_3$ |
| $L_{\mathrm{pau},e_\mu} R_{\mathrm{pau},e_\nu}$ | the two-sided operator $L_{\mathrm{pau},e_\mu} R_{\mathrm{pau},e_\nu}$ |
| $\mathbb{B}$ | the biquaternion algebra, $\mathrm{Cl}^{0}$ |
| $V$ | the Lorentzian vector space, grade 1 |
| $\Lambda^3V$ | the trivector space, grade 3 |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five gammas, the Clifford basis and the set.
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the sixteen $L_{\mathrm{pau},e_\mu} R_{\mathrm{pau},e_\nu}$ and their multiplication table.
- [The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$](the-operators-of-the-peirce-decomposition-of-m4c.html), for $L_a$, $R_a$ and $L_{a}R_{b}$.
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the even and odd slots of the envelope.
- [The Vector and the Axial Traces of $M_4(\mathbb{C})$](the-vector-and-the-axial-traces-of-m4c.html), for the two coordinates $L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}$ and $L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$ that the traces read.
- [The Star and the Conjugate-Linear Operators of $M_4(\mathbb{C})$](the-star-and-the-conjugate-linear-operators-of-m4c.html), for the operation-level form of the odd generators.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the chirality and its relation to the pseudoscalar.
- [Conventions of the Matrix Models](../articles_physics/matrix-representations-conventions.html), for the explicit matrices and the even-part identification, §*The Clifford Structure and the Frame*.
