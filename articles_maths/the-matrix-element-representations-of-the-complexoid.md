# __The Matrix Element Representations of the Complexoid__

## Introduction

The complex algebra sits inside the real matrix algebras in two natural ways: the regular representation, in which a complex number becomes a $2 \times 2$ real matrix, and its doubling, in which it becomes a $4 \times 4$ real matrix. This article reads the two models together: the two matrices, their determinants and traces, the invertible elements and the units of the definite norm, the commutant of each model, and the sense in which the second model adds two dimensions and no new content.

The element-level treatment of the regular matrix is *Complex Regular Element Representation* and the coordinate reading is *Complex Two-Component Element Representation*, both below this article in this category; both are cited here and not repeated, and this article states the matrix facts at the level of the algebra. The two algebraic norms and the two forms are *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, below this article in this category; the definite norm, its multiplicativity, the criterion of invertibility and the group of units are *Complex Norm and Invertibility*, in `### Algebra`, also below.

The elements are written $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$, as *Conventions in Mathematics* fixes; the capital letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ are reserved for the two forms and the two algebraic norms of the companion articles, and no element or subspace constant is written with them, the field of conformal matrices below carrying the calligraphic $\mathcal{K}$ instead. The **bar** is complex conjugation and the star coincides with the bar.

## The Regular Representation in $M_2(\mathbb{R})$

**Definition.** The **left regular representation** of $\mathbb{C}$ is the map

$$
L : \mathbb{C} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{C}), \qquad L_{Q_1}(Q_2) = Q_1Q_2 .
$$

In the basis $1, i$ its matrix, acting on the column of the real coordinates of $Q_2$, is the **Cayley matrix**

$$
\mathsf{M}_2(Q_1) = \begin{pmatrix} q_1 & -q'_1 \\ q'_1 & q_1 \end{pmatrix} = q_1I + q'_1J, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = -I .
$$

**Proposition.** $\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2) = \mathsf{M}_2(Q_1Q_2)$ for all $Q_1, Q_2$, and $\mathsf{M}_2$ is faithful.

**Proof.** Both sides are $\mathbb{R}$-linear in the second factor and agree on the basis, since $L_{Q_1}(L_{Q_2}(1)) = (Q_1Q_2)1 = L_{Q_1Q_2}(1)$ and likewise on $i$; faithfulness holds because $Q_1 = L_{Q_1}(1)$, so $\mathsf{M}_2(Q_1) = 0$ gives $Q_1 = 0$.

The image is the field of matrices of the shape $q_1I + q'_1J$, the **conformal matrices**, the real matrices commuting with $J$; the article *Complex Regular Element Representation* owns this identification and the derivation of the entries. The transpose is the bar in the matrix picture, $\mathsf{M}_2(Q_1)^{\mathsf{T}} = \mathsf{M}_2(\bar Q_1)$, and the two distinguished lines of the algebra go to the scalar matrices and to the multiples of $J$.

## The Determinant and the Trace

**Proposition.** For $Q_1 = q_1 + iq'_1$,

$$
\det \mathsf{M}_2(Q_1) = q_1^2 + q'^2_1 = Q_1\bar Q_1 = \langle Q_1\rangle_{*}, \qquad \operatorname{tr}\mathsf{M}_2(Q_1) = 2q_1 = Q_1 + \bar Q_1 .
$$

**Proof.** $\det \mathsf{M}_2(Q_1) = q_1 \cdot q_1 - (-q'_1)(q'_1) = q_1^2 + q'^2_1$, and the diagonal entries are both $q_1$.

The determinant is the **definite algebraic norm** $\langle Q_1\rangle_{*} = \lvert Q_1 \rvert^2$, and the trace is the **algebra trace**, twice the real part. The two are the invariants of the field extension $\mathbb{C}$ over $\mathbb{R}$, and they move as the two invariants do: the determinant is multiplicative, and the trace is additive on sums,

$$
\det \mathsf{M}_2(Q_1Q_2) = \det \mathsf{M}_2(Q_1)\,\det \mathsf{M}_2(Q_2), \qquad \operatorname{tr}\mathsf{M}_2(Q_1 + Q_2) = \operatorname{tr}\mathsf{M}_2(Q_1) + \operatorname{tr}\mathsf{M}_2(Q_2) ,
$$

the first statement being $\langle Q_1Q_2\rangle_{*} = \langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$, the multiplicativity of the definite norm. The other algebraic norm, the bilinear diagonal $\langle Q_1\rangle = Q_1^2$, is complex and is not a determinant of this real model; it is the diagonal of the bilinear form of *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, below this article in this category, and the model reads that bilinear along the two trace pairings

$$
\tfrac{1}{2}\operatorname{tr}\bigl(\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2)\bigr) = \operatorname{Re}(Q_1Q_2), \qquad
\tfrac{1}{2}\operatorname{tr}\bigl(\mathsf{M}_2(Q_1)^{\mathsf{T}}\mathsf{M}_2(Q_2)\bigr) = \operatorname{Re}(Q_1\bar Q_2) ,
$$

the real parts of the two forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$. The pair $(\det, \operatorname{tr})$ recovers the matrix, and hence the element up to the sign of $q'_1$, since $q_1 = \tfrac{1}{2}\operatorname{tr}\mathsf{M}_2(Q_1)$ and $q'^2_1 = \det\mathsf{M}_2(Q_1) - \tfrac{1}{4}\bigl(\operatorname{tr}\mathsf{M}_2(Q_1)\bigr)^2$.

## The Invertible Elements and the Units of the Definite Norm

**Proposition.** $\mathsf{M}_2(Q_1)$ is invertible exactly when $Q_1 \neq 0$, equivalently when $\det \mathsf{M}_2(Q_1) = \langle Q_1\rangle_{*} \neq 0$; the image is the field of conformal matrices, and the invertible elements are the nonzero ones.

The criterion is that of *Complex Norm and Invertibility*, in `### Algebra` below, read on the matrix: the determinant is the definite norm and it vanishes only at $Q_1 = 0$. The invertible conformal matrices are the matrices of the shape $q_1I + q'_1J$ with $(q_1,q'_1) \neq (0,0)$; they form a group under multiplication, the image of the multiplicative group $\mathbb{C}^{\times}$.

**Proposition.** The elements of definite norm one, $\lvert Q_1 \rvert^2 = 1$, the unit circle, are mapped onto the group of matrices preserving the definite form,

$$
\mathsf{M}_2(Q_1)^{\mathsf{T}}\mathsf{M}_2(Q_1) = I, \qquad \det \mathsf{M}_2(Q_1) = 1 ,
$$

the rotation group of the plane.

**Proof.** For a matrix of the shape $q_1I + q'_1J$,
$\mathsf{M}_2(Q_1)^{\mathsf{T}}\mathsf{M}_2(Q_1) = \mathsf{M}_2(\bar Q_1)\mathsf{M}_2(Q_1) = \mathsf{M}_2(\lvert Q_1 \rvert^2) = \lvert Q_1 \rvert^2 I$ and $\det \mathsf{M}_2(Q_1) = \lvert Q_1 \rvert^2$, so the two conditions are both $\lvert Q_1 \rvert^2 = 1$, and conversely.

The units of the definite norm are therefore the elements of the unit circle, and their images are the real matrices preserving the definite form with determinant one, the rotation group. The operator is developed in *Complex Regular Element Representation*, below this article in this category, and the group is *The Versors and the Orthogonal Group of the Complex Numbers*, also below; the metric distance itself is *The Two Metrics of the Complex Numbers*, below this article in this category.

## The $4 \times 4$ Model

**Definition.** The **doubled regular representation** reads a complex number on the real space $\mathbb{C} \oplus \mathbb{C}$ with basis $(1,0), (i,0), (0,1), (0,i)$, each summand acted on by left multiplication:

$$
\mathsf{M}_4(Q_1) = \begin{pmatrix} \mathsf{M}_2(Q_1) & 0 \\ 0 & \mathsf{M}_2(Q_1) \end{pmatrix} \in M_4(\mathbb{R}) .
$$

The same matrix is the image of the scalar matrix $Q_1 I_2 \in M_2(\mathbb{C})$ under the identification $M_2(\mathbb{C}) \cong M_4(\mathbb{R})$ that replaces each complex entry by its real $2 \times 2$ matrix in the basis $1, i$.

**Proposition.** $\mathsf{M}_4(Q_1)\mathsf{M}_4(Q_2) = \mathsf{M}_4(Q_1Q_2)$, the map is faithful, and

$$
\det \mathsf{M}_4(Q_1) = \bigl(q_1^2 + q'^2_1\bigr)^2 = \langle Q_1\rangle_{*}^2, \qquad \operatorname{tr}\mathsf{M}_4(Q_1) = 4q_1 = 2 \operatorname{tr}\mathsf{M}_2(Q_1) .
$$

**Proof.** Multiplication is block by block and $\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2) = \mathsf{M}_2(Q_1Q_2)$ on each block; the determinant of a block-diagonal matrix is the product of the block determinants, and the trace is their sum.

The determinant is the square of the definite norm, and the trace is twice the $2 \times 2$ trace. The square is the product of the norms of the simple modules the matrix model acts on: here the module is the direct sum of two copies of the simple module $\mathbb{C}$, so the determinant is the product of two copies of the norm.

## The Commutant of the Model

The **commutant** of a model is the set of matrices with real entries commuting with every matrix of the image.

**Proposition.** The commutant of the $4 \times 4$ model is the set of block matrices

$$
\left\{ \begin{pmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{pmatrix} : P_{11}, P_{12}, P_{21}, P_{22} \in \mathcal{K} \right\}, \qquad \mathcal{K} = \{ \mathsf{M}_2(Q_1) : Q_1 \in \mathbb{C} \} \cong \mathbb{C} ,
$$

a real vector space of dimension $8$, isomorphic to $M_2(\mathbb{C})$.

**Proof.** A matrix commutes with the image exactly when it commutes with $\mathsf{M}_4(1) = I_4$ and with $\mathsf{M}_4(i) = \begin{pmatrix} J & 0 \\ 0 & J \end{pmatrix}$. Writing it in $2 \times 2$ blocks and comparing entries block by block, each block must commute with $J$, that is, lie in $\mathcal{K}$; conversely any such block matrix commutes with $\begin{pmatrix} J & 0 \\ 0 & J \end{pmatrix}$. Four blocks of real dimension two give dimension eight, and $\mathcal{K} \cong \mathbb{C}$ gives $M_2(\mathbb{C})$.

The contrast with the $2 \times 2$ model is the point. There the commutant is $\mathcal{K}$ itself, of real dimension two, because the module $\mathbb{C}$ is simple and its endomorphism algebra is $\mathbb{C}$. Here the module is the direct sum of two copies of that simple module, so the endomorphism algebra grows to $M_2$ over it. This is the ordinary double-centralizer phenomenon.

## The Two Models Compared

| model | module | image | commutant | determinant | trace |
|---|---|---|---|---|---|
| $2 \times 2$ | $\mathbb{C}$, simple | $\mathcal{K} \cong \mathbb{C}$ | $\mathcal{K} \cong \mathbb{C}$, dimension $2$ | $q_1^2 + q'^2_1 = \langle Q_1\rangle_{*}$ | $2q_1$ |
| $4 \times 4$ | $\mathbb{C} \oplus \mathbb{C}$ | $\operatorname{diag}(\mathcal{K}, \mathcal{K}) \cong \mathbb{C}$ | $M_2(\mathbb{C})$, dimension $8$ | $(q_1^2 + q'^2_1)^2 = \langle Q_1\rangle_{*}^2$ | $4q_1$ |

The $4 \times 4$ model is the $2 \times 2$ model doubled: it is the direct sum of two copies of the $2 \times 2$ model, acting on the same simple module twice. It carries the second copy of the simple module, two real dimensions of the same irreducible type, and therefore adds no new content to the algebra, the image remaining the same field $\mathbb{C}$; what changes is only the commutant, which grows from the field to the $2 \times 2$ matrices over it. The determinant is squared and the trace doubled for the same reason, the dimension of the module. In this precise sense the $4 \times 4$ model extends the $2 \times 2$ model by two dimensions that add nothing to the algebra, the image being the same field $\mathbb{C}$ inside a larger matrix algebra.

## Summary

The complex algebra has two real matrix models. The regular representation sends $Q_1 = q_1 + iq'_1$ to the Cayley matrix $\mathsf{M}_2(Q_1) = q_1I + q'_1J$ in $M_2(\mathbb{R})$, which is multiplicative and faithful; its image is the field of conformal matrices, its determinant is the definite algebraic norm $\langle Q_1\rangle_{*} = q_1^2 + q'^2_1$, and its trace is the algebra trace $2q_1$. The model is invertible exactly on the nonzero elements, the determinant being $\langle\cdot\rangle_{*}$, and the units of the definite norm are mapped onto the rotation group, the matrices with $M^{\mathsf{T}} M = I$ and determinant one.

The doubled model sends $Q_1$ to the block-diagonal matrix $\operatorname{diag}(\mathsf{M}_2(Q_1), \mathsf{M}_2(Q_1))$ in $M_4(\mathbb{R})$, equivalently to the scalar matrix $Q_1 I_2$ of $M_2(\mathbb{C}) \cong M_4(\mathbb{R})$. Its determinant is $\langle Q_1\rangle_{*}^2$, the square of the definite norm, and its trace is $4q_1$; the doubling comes from the module being the direct sum of two copies of the simple module. The commutant of the $4 \times 4$ model is $M_2(\mathbb{C})$, of real dimension eight, against the commutant of the $2 \times 2$ model, which is $\mathbb{C}$ itself; the growth is the double-centralizer phenomenon on the commutative base.

The two models differ by two dimensions of module that add nothing to the algebra: the $4 \times 4$ model is the $2 \times 2$ model repeated twice, with the same image $\mathbb{C}$ and only a larger commutant, its determinant squared and its trace doubled by the dimension of the module.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{Q_1}, \mathsf{M}_2(Q_1)$ | the left regular representation and its Cayley matrix $q_1I + q'_1J$ |
| $J$ | $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, the matrix of multiplication by $i$, $J^2 = -I$ |
| $\mathcal{K}$ | the field of conformal matrices $\{\mathsf{M}_2(Q_1)\} \cong \mathbb{C}$ (a calligraphic $\mathcal{K}$, kept apart from the form $\langle\cdot,\cdot\rangle_{\natural*}$) |
| $\mathsf{M}_2(Q_1)^{\mathsf{T}} = \mathsf{M}_2(\bar Q_1)$ | the transpose is the bar |
| $\det \mathsf{M}_2(Q_1) = \langle Q_1\rangle_{*} = q_1^2 + q'^2_1$ | the determinant is the definite algebraic norm |
| $\operatorname{tr}\mathsf{M}_2(Q_1) = 2q_1 = Q_1 + \bar Q_1$ | the trace is the algebra trace |
| $\mathsf{M}_4(Q_1) = \operatorname{diag}(\mathsf{M}_2(Q_1), \mathsf{M}_2(Q_1))$ | the doubled model, on $\mathbb{C} \oplus \mathbb{C}$ |
| $\det \mathsf{M}_4(Q_1) = \langle Q_1\rangle_{*}^2$, $\operatorname{tr}\mathsf{M}_4(Q_1) = 4q_1$ | the invariants of the doubled model |
| commutant | the matrices commuting with the whole image |

## Further Reading

- Arthur Cayley, "A memoir on the theory of matrices" (1858), for the matrix realization of a two-dimensional algebra.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for the regular representation and the double centralizer theorem.
- Serge Lang, *Algebra*, 3rd edition (Springer, 2002), for the regular module of a field, its simplicity and its commutant.
- Charles C. Pinter, *A Book of Abstract Algebra* (Dover, 2010), for the regular representation of an algebra by matrices.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the conformal and rotation matrices of multiplication by a complex number.
