# __The Quaternionic Structure and the Real Forms of $M_4(\mathbb{C})$__

## Introduction

A real form of a complex algebra is a real algebra whose complexification is the given one. For $M_4(\mathbb{C})$ there are exactly two:

$$
M_4(\mathbb{R}),\qquad M_2(\mathbb{H}),
$$

both of real dimension $16$. The first is the fixed algebra of the conjugation $A\mapsto\bar A$; the second is the fixed algebra of the **quaternionic structure**

$$
\theta(A)=J\bar A J^{-1},\qquad J^{2}=-I,
$$

for an antilinear involution $J$ of $\mathbb{C}^{4}$ with $J^{2}=-1$. The two are the two real forms of the Brauer class of $M_4$: the split form and the quaternionic form.

This article states the antilinear structures of $\mathbb{C}^{4}$, the induced antilinear automorphisms of $M_4$, the two fixed algebras and their dimensions, the classification by the Brauer group of $\mathbb{R}$, the quaternionic matrices and their conjugate transpose, the place of the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ as a complex subalgebra and not a real form, and the antilinear automorphism group. The real forms of the Lie algebra are *The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$*; the $*$-structures are *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*.

## The Antilinear Structures of $\mathbb{C}^{4}$

**Definition.** A **real structure** on $\mathbb{C}^{4}$ is an antilinear map $\sigma$ with $\sigma^{2}=1$. A **quaternionic structure** is an antilinear map $J$ with $J^{2}=-1$.

**Proposition.** A real structure is the conjugation of a real form: there is a basis in which

$$
\sigma(z_1,\dots,z_4)=(\bar z_1,\dots,\bar z_4).
$$

A quaternionic structure makes $\mathbb{C}^{4}$ into a quaternionic vector space of quaternionic dimension two: the maps $z\mapsto az$ and $z\mapsto bJz$ for $a,b\in\mathbb{R}$ give the left action of $\mathbb{H}$, with $J$ playing the role of $j$.

**Proof.** For the real structure, the fixed space $\mathbb{R}^{4}=\{v:\sigma(v)=v\}$ is a real subspace of real dimension four, and $\mathbb{C}^{4}=\mathbb{R}^{4}\otimes\mathbb{C}$; choosing a real basis gives the displayed form. For the quaternionic structure, $J$ is a complex-antilinear operator with $J^{2}=-1$, so it satisfies the relations of right multiplication by $j$ on $\mathbb{H}^{2}$; the complex dimension four is the quaternionic dimension two.

**The standard matrices.** With $\mathbb{C}^{4}=\mathbb{C}^{2}\oplus\mathbb{C}^{2}$,

$$
\sigma_0=\bar{\phantom{v}},\qquad
J_0=\begin{pmatrix}0&-I_2\\I_2&0\end{pmatrix}\bar{\phantom{v}},
$$

where the bar is the componentwise conjugation. Then $\sigma_0^{2}=1$ and $J_0^{2}=-1$.

## The Induced Antilinear Automorphisms

**Definition.** An antilinear automorphism of $M_4(\mathbb{C})$ is a bijection $\theta$ with

$$
\theta(A+B)=\theta(A)+\theta(B),\qquad
\theta(\lambda A)=\bar\lambda\theta(A),\qquad
\theta(AB)=\theta(A)\theta(B).
$$

**Proposition.** For every antilinear involution $\sigma$ of $\mathbb{C}^{4}$ with $\sigma^{2}=\pm1$, the map

$$
\theta_\sigma(A)=\sigma A\sigma^{-1}
$$

is an antilinear automorphism of $M_4(\mathbb{C})$ of order two.

**Proof.** The map is conjugate-linear because $\sigma$ is, multiplicative because conjugation is an automorphism, and of order two because $\sigma^{2}=\pm1$ is a scalar. In the two cases, $\sigma^{-1}=\pm\sigma$, and the sign cancels in the conjugation.

**The two fixed algebras.** Let

$$
M_4^{\sigma}=\{A:\sigma A\sigma^{-1}=A\}=\{A:A\sigma=\sigma A\}.
$$

**Theorem.** If $\sigma^{2}=1$, then $M_4^{\sigma}\cong M_4(\mathbb{R})$. If $J^{2}=-1$, then $M_4^{J}\cong M_2(\mathbb{H})$. In both cases the fixed algebra has real dimension $16$.

**Proof.** For the real structure, choose the basis in which $\sigma$ is the componentwise conjugation. The condition $A\bar v=\overline{Av}$ for all $v$ says that $A$ has real entries, so $M_4^{\sigma}=M_4(\mathbb{R})$, of real dimension $16$.

For the quaternionic structure, write $A=X+iY$ with $X,Y$ real and use $J$ real, $J^{2}=-1$. The condition $AJ=J\bar A$ becomes

$$
XJ=JX,\qquad YJ=-JY.
$$

The first says that $X$ commutes with the complex structure $J$, so $X$ lies in the commutant of $J$ in $M_4(\mathbb{R})$, of real dimension $8$; the second says that $Y$ anticommutes with $J$, so $Y=JZ$ with $Z$ commuting with $J$, again of real dimension $8$. Hence $\dim_\mathbb{R}M_4^{J}=16$. The algebra is the algebra of endomorphisms of $\mathbb{C}^{4}$ commuting with the quaternionic structure, that is, the quaternionic-linear endomorphisms of $\mathbb{H}^{2}$, which is $M_2(\mathbb{H})$. $\square$

**The check.** In the standard basis the two conditions have rank $8$ each, so the solution space is $16$-dimensional; the computation is the one displayed, with $J_0$ the block matrix above.

## The Classification

**Theorem.** Every real form of $M_4(\mathbb{C})$ is isomorphic to $M_4(\mathbb{R})$ or to $M_2(\mathbb{H})$.

**Proof.** A real form $A$ is a real central simple algebra with $A\otimes_\mathbb{R}\mathbb{C}\cong M_4(\mathbb{C})$. By the Wedderburn theorem, $A\cong M_k(D)$ with $D$ a division algebra over $\mathbb{R}$; the only finite-dimensional real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The real dimension is $k^{2}\dim_\mathbb{R}D=16$. The possibilities are $D=\mathbb{R}$ with $k=4$, giving $M_4(\mathbb{R})$; $D=\mathbb{H}$ with $k=2$, giving $M_2(\mathbb{H})$; and $D=\mathbb{C}$, giving $k^{2}\cdot2=16$, which has no integer solution. Hence the two forms. $\square$

**The Brauer reading.** The Brauer group $Br(\mathbb{R})=\mathbb{Z}/2$ has two classes: the split class of $\mathbb{R}$ and the class of $\mathbb{H}$. The algebra $M_4(\mathbb{C})$ is split over $\mathbb{C}$; its real forms are the split algebra $M_4(\mathbb{R})$ and the quaternionic algebra $M_2(\mathbb{H})$, whose class is that of $\mathbb{H}$.

**The dimensions.** Both forms have real dimension $16$, and both complexify to $M_4(\mathbb{C})$:

$$
M_4(\mathbb{R})\otimes_\mathbb{R}\mathbb{C}\cong M_4(\mathbb{C}),\qquad
M_2(\mathbb{H})\otimes_\mathbb{R}\mathbb{C}\cong M_4(\mathbb{C}).
$$

## The Quaternionic Matrices

**Definition.** $M_2(\mathbb{H})$ is the algebra of $2\times2$ matrices with quaternionic entries, with the usual product; its real dimension is $4\cdot4=16$.

**The conjugate transpose.** For $A=(a_{ij})$ with $a_{ij}\in\mathbb{H}$, put $A^{*}=(\bar a_{ji})$, where the bar is the quaternionic conjugate. Then $(AB)^{*}=B^{*}A^{*}$ and $A^{**}=A$.

**The unitary group.** The quaternionic unitary group is

$$
Sp(2)=\{A\in M_2(\mathbb{H}):A^{*}A=I\},
$$

of real dimension $10$. It is the compact real form of $Sp(2,\mathbb{C})$ and the maximal compact subgroup of $SU^{*}(4)\cong Spin(5,1)$. The algebra $\mathfrak{sp}(2)$ is the compact real form of $\mathfrak{sp}(2,\mathbb{C})\cong\mathfrak{so}(5,\mathbb{C})$, and it appears here as the fixed algebra of the quaternionic involution on $\mathfrak{sl}_4(\mathbb{C})$; the two roles are the two sides of the isomorphism $SU^{*}(4)\cong Spin(5,1)$ of *The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$*.

**The embedding.** The scalar quaternions give a copy of $\mathbb{H}$ inside $M_2(\mathbb{H})$, and the complexification of that copy is $M_2(\mathbb{C})=\mathbb{B}$. The chain

$$
\mathbb{H}\subset M_2(\mathbb{H})\subset M_4(\mathbb{C})
$$

has real dimensions $4$, $16$ and $32$; the last inclusion is the complexification.

**The determinant.** The quaternionic determinant is not a multiplicative homomorphism in the naive sense; the **Dieudonné determinant** is defined on $GL_2(\mathbb{H})$ with values in $\mathbb{H}^{\times}/[\mathbb{H}^{\times},\mathbb{H}^{\times}]$, and the subgroup $SL_2(\mathbb{H})$ is the kernel. The Lie algebra $\mathfrak{sl}_2(\mathbb{H})$ is the real form $\mathfrak{su}^{*}(4)$ of the Lie algebra article.

## The Place of the Biquaternion Algebra

**The biquaternion algebra.** $\mathbb{B}\cong M_2(\mathbb{C})$ is a complex algebra of complex dimension $4$ and real dimension $8$. It is **not** a real form of $M_4(\mathbb{C})$: its complexification is

$$
\mathbb{B}\otimes_\mathbb{R}\mathbb{C}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$

of complex dimension $8$, not $M_4(\mathbb{C})$. The real forms of $M_4(\mathbb{C})$ are the two algebras above, of real dimension $16$.

**The subalgebra.** $\mathbb{B}$ sits inside $M_4(\mathbb{C})$ as the left factor $M_2\otimes I$ of the Kronecker decomposition, of complex dimension $4$. The ambient algebra is the endomorphism algebra of $\mathbb{B}$, and the inclusion of the left factor is the left regular representation, not a real form. The right factor $I\otimes M_2$ is a second copy of $\mathbb{B}$, and the two copies commute.

**The quaternionic form and the biquaternion.** The quaternionic form $M_2(\mathbb{H})$ contains $\mathbb{H}$ as its scalars; the biquaternion algebra $\mathbb{B}=M_2(\mathbb{C})$ contains $\mathbb{C}$ as its scalars. The two are related by complexification: $\mathbb{H}\otimes_\mathbb{R}\mathbb{C}\cong M_2(\mathbb{C})=\mathbb{B}$, the complexification of the quaternion algebra being the biquaternion algebra. This is the precise sense in which the biquaternion algebra is the complexified quaternion algebra, and it is not the complexification of $M_2(\mathbb{H})$.

## The Antilinear Automorphism Group

**Proposition.** Every antilinear automorphism of $M_4(\mathbb{C})$ is of the form

$$
\theta(A)=U\bar A U^{-1}
$$

for some $U\in GL_4(\mathbb{C})$, and

$$
\operatorname{Aut}_\mathbb{R}(M_4)=PGL_4(\mathbb{C})\rtimes\mathbb{Z}/2.
$$

**Proof.** Composing $\theta$ with the conjugation gives a complex-linear automorphism, which is inner by Skolem–Noether; hence $\theta(A)=U\bar A U^{-1}$. The linear automorphisms form the normal subgroup $PGL_4$, and the antilinear ones form the nontrivial coset. $\square$

**The real structures on the algebra.** The antilinear involutions of $M_4$ fall into two classes, according to whether the square is the identity or an inner automorphism of order two. The first class gives the real form $M_4(\mathbb{R})$, the second the quaternionic form $M_2(\mathbb{H})$. The classification of the classes is the classification of the real forms, and the two are exchanged by no automorphism of the complex algebra: they are the two elements of $Br(\mathbb{R})$.

**The physical interpretation.** A Majorana condition is a real structure on the spinor module, $\psi=C\bar\psi$ with $C^{2}=\pm1$; a quaternionic structure is the same condition with the opposite sign. The two signs are the two real forms of the algebra, and the choice is a choice of the reality layer, not of the Clifford frame of *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*.

## Summary

The two real forms of $M_4(\mathbb{C})$ are $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$, both of real dimension $16$, fixed respectively by a real structure $\sigma^{2}=1$ and a quaternionic structure $J^{2}=-1$ on $\mathbb{C}^{4}$. The quaternionic fixed algebra has real dimension $16$: the real part commutes with $J$ and the imaginary part anticommutes with it, each of dimension $8$. The classification is the Brauer classification of the real central simple algebras of degree four, and the two forms are the split and quaternionic classes. The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is a complex subalgebra of dimension $4$, not a real form; its complexification is $M_2\oplus M_2$, and the complexification of $\mathbb{H}$ is $\mathbb{B}$. The antilinear automorphisms form the coset $PGL_4\rtimes\mathbb{Z}/2$, and the antilinear involutions of the two signs give the two real forms.

| Quantity | Value |
|---|---|
| Real forms of $M_4(\mathbb{C})$ | $2$ |
| $M_4(\mathbb{R})$ | real dimension $16$ |
| $M_2(\mathbb{H})$ | real dimension $16$ |
| Fixed algebra of $\sigma^{2}=1$ | $M_4(\mathbb{R})$ |
| Fixed algebra of $J^{2}=-1$ | $M_2(\mathbb{H})$ |
| $\dim_\mathbb{R}\mathbb{H}$ | $4$ |
| $\dim_\mathbb{R}\mathbb{B}$ | $8$ |
| $\dim_\mathbb{C}\mathbb{B}$ | $4$ |
| $\dim Sp(2)$ | $10$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | a real structure, antilinear with $\sigma^{2}=1$ |
| $J$ | a quaternionic structure, antilinear with $J^{2}=-1$ |
| $\theta_\sigma(A)=\sigma A\sigma^{-1}$ | the induced antilinear automorphism |
| $M_4^{\sigma}$ | the fixed algebra of $\theta_\sigma$ |
| $Sp(2)$ | the quaternionic unitary group |
| $Br(\mathbb{R})$ | the Brauer group $\mathbb{Z}/2$ |
| $\mathbb{B}$ | the biquaternion algebra $M_2(\mathbb{C})$ |

## Further Reading

- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra and its subalgebras.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the $*$-structures.
- [The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$](the-lie-algebra-gl4-and-sl4-of-m4c.html), for $\mathfrak{su}^{*}(4)\cong\mathfrak{so}(5,1)$ and $\mathfrak{sp}(2)$.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c.html), for the two copies of $\mathbb{B}$.
- [The Derivations and the Automorphisms of $M_4(\mathbb{C})$](the-derivations-and-the-automorphisms-of-m4c.html), for the antilinear automorphism group.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for $\mathbb{B}$ and its complexification of $\mathbb{H}$.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Brauer group and the real forms.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the quaternionic matrix algebras and the Dieudonné determinant.
