# __The Matrix Algebra $M_4(\mathbb{C})$__

## Introduction

The **matrix algebra** $M_4(\mathbb{C})$ is the algebra of $4\times4$ complex matrices under the product. It is the ambient algebra of this category: the root, the idempotents, the Peirce corners, the frame, the principal $\mathfrak{sl}_2$ and the chiralities are all structures on it. This article fixes the algebra itself: the matrix units, the trace, the determinant, the centre, the simplicity, the real dimension, the unit group $GL_4(\mathbb{C})$ and the projective group $PGL_4(\mathbb{C})$.

Throughout, $M_4=M_4(\mathbb{C})=\operatorname{End}(\mathbb{C}^4)$, $I$ is the identity, and $A^*=\bar A^{\mathsf T}$ is the conjugate transpose. No positive definite form, no norm and no topology are used; the positive definite trace form and the topology are *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$* and *The Topology of $M_4(\mathbb{C})$*. The element, its coordinates and the trace are *The Element, the Coordinates and the Trace of $M_4(\mathbb{C})$*.

The algebra is **central simple** of complex dimension $16$ and real dimension $32$. It has centre $\mathbb{C}I$, no proper two-sided ideal, and many zero divisors. Its unit group is $GL_4(\mathbb{C})$, of complex dimension $16$; its projective group is $PGL_4(\mathbb{C})$, of complex dimension $15$. The group $PGL_4$ is the group of frames modulo overall scale, and it is the group that acts on the root and on the gauge in the articles that follow.

**The full algebra and the regular model.** The $M_4(\mathbb{C})_{\mathbb{B},L}$ articles study the four-dimensional subalgebra of $M_4(\mathbb{C})$ that is the image of the left regular representation of the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$. That image is not the full algebra: it is a copy of $M_2(\mathbb{C})$ inside $M_4(\mathbb{C})$, of complex dimension $4$, and its trace and determinant are the biquaternion trace and norm. The present article and the rest of this category treat the full sixteen-dimensional algebra. The distinction is stated precisely in §*The Full Algebra and the Regular Model*. A construction of the algebra from the two-sided operators on a smaller matrix algebra is §*A Construction from the Two-Sided Operators*; it is one route to the algebra, not a definition.

## The Algebra and the Matrix Units

**Definition.** Let $E_{ij}$ be the $4\times4$ matrix with entry $1$ in position $(i,j)$ and $0$ elsewhere. The sixteen matrices $E_{ij}$, $i,j=1,2,3,4$, are the **matrix units**.

**Proposition.** The matrix units are a basis of $M_4$, and

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

The unit is

$$
I=\sum_{k=1}^{4}E_{kk},
$$

the product is associative, and the algebra is non-commutative.

**Proof.** The product is the elementary computation: the $(r,s)$ entry of $E_{ij}E_{kl}$ is $\delta_{ri}\delta_{jk}\delta_{ls}$, which is the $(r,s)$ entry of $\delta_{jk}E_{il}$. The sixteen units are linearly independent because $E_{ij}$ has a $1$ in a position where the other units have $0$. Associativity is associativity of the matrix product. For non-commutativity, $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$, and these are different.

**The dimension.** The algebra has complex dimension $16$, because the sixteen units are a basis, and real dimension

$$
\dim_\mathbb{R}M_4(\mathbb{C})=2\cdot16=32,
$$

because each of the sixteen complex entries is two real numbers.

**A general element.** A matrix is

$$
A=\sum_{i,j=1}^{4}A_{ij}E_{ij}
=\begin{pmatrix}
A_{11}&A_{12}&A_{13}&A_{14}\\
A_{21}&A_{22}&A_{23}&A_{24}\\
A_{31}&A_{32}&A_{33}&A_{34}\\
A_{41}&A_{42}&A_{43}&A_{44}
\end{pmatrix}.
$$

The entries $A_{ij}$ are the coordinates of $A$ in the basis of matrix units.

**The product in coordinates.** For $A=\sum A_{ij}E_{ij}$ and $B=\sum B_{kl}E_{kl}$,

$$
AB=\sum_{i,j,k,l}A_{ij}B_{kl}E_{ij}E_{kl}
=\sum_{i,l}\Bigl(\sum_{j=1}^{4}A_{ij}B_{jl}\Bigr)E_{il}.
$$

This is the matrix product. It is the formula that the Peirce coordinates generalize to an arbitrary frame in *The Peirce Decomposition of $M_4(\mathbb{C})$*.

**The opposite algebra.** The map $A\mapsto A^{\mathsf T}$ is an anti-automorphism, $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$, and it is an isomorphism $M_4\to M_4^{\mathrm{op}}$. The algebra is isomorphic to its opposite, as every matrix algebra is.

## The Trace and the Determinant

**Definition.** The **trace** is the linear functional

$$
\operatorname{tr}A=\sum_{k=1}^{4}A_{kk}.
$$

The **determinant** is the multiplicative polynomial

$$
\det A=\sum_{\sigma\in S_4}\operatorname{sgn}(\sigma)\prod_{k=1}^{4}A_{k,\sigma(k)}.
$$

Both are polynomial functions of the entries; the trace is linear and the determinant is homogeneous of degree $4$.

**Proposition.** The trace is linear and satisfies

$$
\operatorname{tr}(AB)=\operatorname{tr}(BA),\qquad
\operatorname{tr}(E_{ij})=\delta_{ij},\qquad
\operatorname{tr}(I)=4.
$$

It is invariant under conjugation:

$$
\operatorname{tr}(SAS^{-1})=\operatorname{tr}A.
$$

**Proof.** The $(i,i)$ entry of $AB$ is $\sum_jA_{ij}B_{ji}$, and the $(j,j)$ entry of $BA$ is $\sum_iB_{ji}A_{ij}$; the sums are equal. The other identities are immediate from the definition. For conjugation, use $\operatorname{tr}((SA)S^{-1})=\operatorname{tr}(S^{-1}SA)$.

**Proposition.** The determinant is multiplicative,

$$
\det(AB)=\det A\det B,\qquad \det I=1,
$$

and invariant under conjugation:

$$
\det(SAS^{-1})=\det A.
$$

**Proof.** Multiplicativity is the product formula for determinants, and $\det I=1$ is the identity permutation. For conjugation, $\det(SAS^{-1})=\det S\det A\det S^{-1}=\det A$.

**The characteristic polynomial and Cayley–Hamilton.** The characteristic polynomial is

$$
\chi_A(t)=\det(tI-A)=t^4-(\operatorname{tr}A)t^3+c_2t^2-c_1t+\det A,
$$

with

$$
c_2=\frac12\bigl((\operatorname{tr}A)^2-\operatorname{tr}(A^2)\bigr),\qquad
c_1=\frac16\bigl((\operatorname{tr}A)^3-3\operatorname{tr}A\operatorname{tr}(A^2)+2\operatorname{tr}(A^3)\bigr).
$$

Cayley–Hamilton states

$$
\chi_A(A)=0.
$$

**Proof.** The characteristic polynomial is the determinant of $tI-A$; expanding along the permutations gives the displayed coefficients, which are the elementary symmetric functions of the eigenvalues expressed through the power sums. Cayley–Hamilton is the standard theorem for matrices over a commutative ring (*The Jordan–Chevalley Decomposition of a Matrix*).

**The trace is the unique invariant linear functional.** If $\varphi:M_4\to\mathbb{C}$ is linear and $\varphi(AB)=\varphi(BA)$ for all $A,B$, then $\varphi=c\operatorname{tr}$ for some $c\in\mathbb{C}$.

**Proof.** The condition says that $\varphi$ vanishes on every commutator $[A,B]$. The commutators span the traceless subspace $\mathfrak{sl}_4(\mathbb{C})$, of dimension $15$: the elementary commutators $[E_{ij},E_{ji}]=E_{ii}-E_{jj}$ span the diagonal traceless subspace, and $[E_{ij},E_{jk}]=E_{ik}$ for $i\ne k$ gives the off-diagonal units. Hence $\varphi$ vanishes on $\mathfrak{sl}_4$ and is determined by its value on $I$, so $\varphi=\varphi(I)\operatorname{tr}/4$.

**The determinant is the unique multiplicative polynomial of degree four normalised at $I$.** A polynomial function $f:M_4\to\mathbb{C}$ with $f(AB)=f(A)f(B)$ for all $A,B$, homogeneous of degree $4$, and $f(I)=1$, is $f=\det$. On the invertible matrices $f$ is a rational character of $GL_4(\mathbb{C})$, and every such character is a power of the determinant; homogeneity of degree $4$ and $f(I)=1$ force the first power. The details are in Horn and Johnson, *Matrix Analysis*.

**The bilinear trace form.** The pairing

$$
(A,B)\longmapsto\operatorname{tr}(AB)
$$

is symmetric and non-degenerate, because $\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}$ and the matrix of the pairing in the unit basis is a permutation matrix. It is not positive definite: $\operatorname{tr}(A^2)$ can be negative for real $A$, and it can be zero for $A\ne0$. The positive definite form is $\operatorname{tr}(A^*B)$, and it is a different object; it belongs to *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*.

## The Centre and the Simplicity

**Theorem.** The centre of $M_4$ is the line of scalars:

$$
Z(M_4)=\mathbb{C}I.
$$

**Proof.** Let $A$ commute with every $E_{ij}$. From $AE_{ij}=E_{ij}A$ compare entries. The $(r,s)$ entry of $AE_{ij}$ is $A_{ri}\delta_{js}$, and the $(r,s)$ entry of $E_{ij}A$ is $\delta_{ri}A_{js}$. Taking $r=i$, $s=j$ gives $A_{ii}=A_{jj}$ for all $i,j$, so all diagonal entries are equal to a common $\lambda$. Taking $r=i$, $s\ne j$ gives $A_{ij}=0$ for $i\ne j$. Hence $A=\lambda I$. The scalars commute with everything, so the centre is exactly $\mathbb{C}I$.

**Corollary.** The algebra is **central**: its centre is the base field $\mathbb{C}$.

**Theorem.** The algebra is **simple**: its only two-sided ideals are $0$ and $M_4$.

**Proof.** Let $\mathcal{I}\ne0$ be a two-sided ideal, and let $0\ne A\in\mathcal{I}$. Some entry $A_{kl}$ is nonzero. For every $i,j$,

$$
E_{ik}AE_{lj}=A_{kl}E_{ij}
$$

by the product rule. The left-hand side lies in $\mathcal{I}$ because $\mathcal{I}$ is two-sided, so $E_{ij}\in\mathcal{I}$ for every $i,j$. The units span $M_4$, hence $\mathcal{I}=M_4$.

**Corollary.** The algebra is **central simple** over $\mathbb{C}$. It is not a direct sum of two nonzero algebras, and it has no proper two-sided ideal.

**The algebra is not a division algebra.** Zero divisors exist:

$$
E_{11}E_{22}=0,\qquad E_{11}\ne0,\quad E_{22}\ne0.
$$

More generally, $AB=0$ with $A,B\ne0$ exactly when $\operatorname{im}B\subseteq\ker A$. Sylvester's inequality then gives

$$
\operatorname{rank}A+\operatorname{rank}B\le4,
$$

which is necessary but not sufficient. The zero divisors do not form an ideal: the two-sided ideal generated by any nonzero element is the whole algebra.

**The singular set.** The set

$$
\Sigma=\{A:\det A=0\}
$$

is the zero locus of the determinant, a complex hypersurface of complex dimension $15$, hence of real codimension $2$. Its complement is the open dense group $GL_4(\mathbb{C})$. The stratification by rank and the singular set are *The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$*.

## The Groups

**The unit group.** The **general linear group**

$$
GL_4(\mathbb{C})=\{A:\det A\ne0\}
$$

is the group of invertible matrices. It has complex dimension $16$ and real dimension $32$. It is connected: every invertible matrix is a product of elementary matrices and a diagonal matrix, and the diagonal matrices can be joined to $I$ by a path in $\mathbb{C}^\times$.

**The determinant homomorphism.** The determinant is a surjective homomorphism

$$
\det:GL_4(\mathbb{C})\longrightarrow\mathbb{C}^\times,
$$

with kernel the **special linear group**

$$
SL_4(\mathbb{C})=\{A:\det A=1\},
$$

of complex dimension $15$. The fibration $SL_4\to GL_4\to\mathbb{C}^\times$ is locally trivial, and the Lie algebra of $SL_4$ is the traceless subalgebra $\mathfrak{sl}_4$.

**The projective group.** The **projective general linear group** is

$$
PGL_4(\mathbb{C})=GL_4(\mathbb{C})/\mathbb{C}^\times I,
$$

of complex dimension $16-1=15$. It acts on $M_4$ by conjugation,

$$
A\longmapsto SAS^{-1},
$$

and the kernel of the action is exactly the scalars: if $SAS^{-1}=A$ for every $A$, then $S$ commutes with every matrix, hence $S\in\mathbb{C}^\times I$ by the centre theorem. The conjugation action preserves the trace, the determinant, the characteristic polynomial and the rank.

**The projective group is the group of frames modulo scale.** A frame is an ordered basis $(v_1,v_2,v_3,v_4)$ of $\mathbb{C}^4$. The group $GL_4$ acts simply transitively on frames. Two frames that differ by an overall scalar give the same matrix units $E_{ij}=v_i\ell_j$, because the scalar cancels between the vector and the dual functional. The group of frames modulo overall scale is therefore $PGL_4$. This is the group that acts on the root and on the gauge; the count of the frame is

$$
\underbrace{15}_{PGL_4}
=
\underbrace{12}_{\text{root}}
+
\underbrace{3}_{\text{gauge}} .
$$

**The standard flag and the Borel subgroup.** The standard flag is

$$
0\subset\mathbb{C}e_1\subset\mathbb{C}e_1\oplus\mathbb{C}e_2\subset\mathbb{C}e_1\oplus\mathbb{C}e_2\oplus\mathbb{C}e_3\subset\mathbb{C}^4.
$$

Its stabiliser in $GL_4$ is the Borel subgroup $B$ of upper triangular matrices, of complex dimension $10$ (four diagonal entries and six strictly upper entries). The flag variety $GL_4/B$ has complex dimension

$$
16-10=6.
$$

The spectral flag of a root is a point of this variety; the geometry of all flags is *The Geometry of the Idempotents of $M_4(\mathbb{C})$* and *The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$*.

## The Real Structure

**The algebra as a real algebra.** The multiplication of matrices is $\mathbb{R}$-bilinear, and the real dimension is $32$. Multiplication by $i$ is a real-linear endomorphism

$$
J:M_4\longrightarrow M_4,\qquad J(A)=iA,
$$

with $J^2=-\mathrm{id}$. It is complex-linear as a map of the complex vector space, and it is the complex structure that exhibits the real algebra as a complex algebra. The real algebra $M_4(\mathbb{C})$ is the complexification of the real algebra $M_4(\mathbb{R})$:

$$
M_4(\mathbb{C})=\mathbb{C}\otimes_{\mathbb{R}}M_4(\mathbb{R}).
$$

**The conjugate transpose.** The map

$$
A\longmapsto A^*=\bar A^{\mathsf T}
$$

is a $\mathbb{C}$-antilinear involution:

$$
(A+B)^*=A^*+B^*,\qquad (\lambda A)^*=\bar\lambda A^*,\qquad (AB)^*=B^*A^*,\qquad A^{**}=A.
$$

It is not complex-linear and it is not an algebra automorphism; it is a **Hermitian involution** of the real algebra.

**Hermitian and skew-Hermitian parts.** Every matrix splits uniquely as

$$
A=\frac12(A+A^*)+\frac12(A-A^*),
$$

with $A+A^*$ Hermitian and $A-A^*$ skew-Hermitian. The real subspaces

$$
\operatorname{Herm}_4=\{A:A^*=A\},\qquad
\mathfrak{u}(4)=\{A:A^*=-A\}
$$

have real dimensions $16$ each, and $M_4=\operatorname{Herm}_4\oplus\mathfrak{u}(4)$ as a real vector space. The skew-Hermitian space is the Lie algebra $\mathfrak{u}(4)$ of the $*$-unitary group; its traceless part is $\mathfrak{su}(4)$, of real dimension $15$. As a complex Lie algebra, $M_4(\mathbb{C})=\mathfrak{u}(4)\otimes_{\mathbb{R}}\mathbb{C}=\mathfrak{u}(4)\oplus i\mathfrak{u}(4)$, with the Hermitian matrices $i\mathfrak{u}(4)$.

**The $*$-unitary groups.** The **$*$-unitary group** is

$$
U(4)=\{U:U^*U=I\},
$$

of real dimension $16$, and the **special $*$-unitary group** is $SU(4)=U(4)\cap SL_4(\mathbb{C})$, of real dimension $15$. The projective $*$-unitary group $PU(4)=U(4)/U(1)$ is a maximal compact subgroup of $PGL_4(\mathbb{C})$. These groups are used in *The Polar Decomposition of $M_4(\mathbb{C})$* and *The Exponential and the Lie Group of $M_4(\mathbb{C})$*; the present article only records the real structure.

**No positive definite form is used.** The Hermitian involution defines the positive definite trace form $\operatorname{tr}(A^*B)$ on the real space, but this article does not use it. The algebraic statements above — centre, simplicity, trace, determinant, groups — are independent of any form. The one form that does appear, the bilinear pairing $\operatorname{tr}(AB)$, is indefinite and is not the Hermitian form.

## The Full Algebra and the Regular Model

**The regular model $M_4(\mathbb{C})_{\mathbb{B},L}$ is a four-dimensional subalgebra.** The biquaternion algebra

$$
\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}
$$

is isomorphic to $M_2(\mathbb{C})$ as a complex algebra, of complex dimension $4$. Its left regular representation on itself is a map

$$
L:\mathbb{B}\longrightarrow\operatorname{End}_\mathbb{C}(\mathbb{B})\cong M_4(\mathbb{C}),
$$

and the image is a four-dimensional subalgebra of $M_4(\mathbb{C})$ isomorphic to $\mathbb{B}$. The $M_4(\mathbb{C})_{\mathbb{B},L}$ articles study that image: its matrix product, its trace, its determinant (the square of the biquaternion norm), its spectral projectors and its Peirce coordinates. The subscript $L$ records that the matrices are matrices of left multiplication.

**The full algebra is sixteen-dimensional.** The algebra $M_4(\mathbb{C})$ of this category is the whole of $\operatorname{End}(\mathbb{C}^4)$, of complex dimension $16$. It contains many four-dimensional subalgebras isomorphic to $M_2(\mathbb{C})$, one for each embedding, and the regular model is one of them. The full algebra has sixteen matrix units, sixteen Peirce lines and a sixteen-dimensional adjoint representation; the regular model has four matrix units in its own basis, four Peirce lines and a four-dimensional adjoint representation.

**The two traces and the two determinants.** The trace of the full algebra is the sum of the four diagonal entries of a $4\times4$ matrix; the trace of the regular model is the trace of the left multiplication operator, which is four times the biquaternion scalar part. The determinant of the full algebra is the usual $4\times4$ determinant; the determinant of the regular model is the square of the biquaternion norm, because the regular representation contains two copies of the defining module. The two agree on the scalars, where the full determinant is the square of the norm. A statement about the biquaternion norm is not a statement about the full determinant, and a statement about the full determinant is not a statement about the norm.

**The $L$ model is not a quotient.** The full algebra does not contain the regular model as an ideal, because it is simple. The model is a subalgebra, and the full algebra is a larger algebra of the same matrix size. The category $M_4(\mathbb{C})$ is about the larger algebra; the $M_4(\mathbb{C})_{\mathbb{B},L}$ category is about the representation of $\mathbb{B}$. The two should not be identified.

## A Construction from the Two-Sided Operators

**The map.** For $a,b\in M_n(\mathbb{C})$ put $T_{a,b}(X)=aXb$. The map $a\otimes b^{\mathrm{opp}}\mapsto T_{a,b}$ is an algebra isomorphism
$$
M_n(\mathbb{C})\otimes_\mathbb{C}M_n(\mathbb{C})^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(M_n(\mathbb{C}))\cong M_{n^2}(\mathbb{C}),
$$
because the images of the matrix-unit basis of the tensor product are the matrix units of $\operatorname{End}_{\mathbb{C}}(M_n(\mathbb{C}))$.

**The case $n=2$.** With $\mathbb{B}\cong M_2(\mathbb{C})$ this gives $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$. In the coefficient basis the images are the sixteen $T_{\mu\nu}=L_\mu R_\nu$; they are not the matrix units, and every $E_{ij}$ is a sum of four of them. The construction reaches the square orders $n^2$ and, in the two-factor form, the products $mn$: it gives $M_4$ and $M_9$, and $M_6$ from $M_2$ and $M_3$, but not $M_3$ or $M_5$. It is one construction of the algebra, not a definition, and it chooses no gamma frame. The full account, with the sixteen matrices, the multiplication tables and the coefficient formula, is *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*.

## Summary

The algebra $M_4(\mathbb{C})$ is the algebra of $4\times4$ complex matrices, of complex dimension $16$ and real dimension $32$, with basis the sixteen matrix units $E_{ij}$, product $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and unit $I$. Its trace is the sum of the diagonal entries, its determinant is the usual multiplicative polynomial of degree four, and the two are invariant under conjugation. The centre is $\mathbb{C}I$ and the algebra is central simple: its only two-sided ideals are $0$ and the algebra. The unit group is $GL_4(\mathbb{C})$, of complex dimension $16$, with determinant epimorphism onto $\mathbb{C}^\times$ and kernel $SL_4(\mathbb{C})$ of dimension $15$; the projective group $PGL_4(\mathbb{C})$ has dimension $15$ and acts by conjugation, with kernel the scalars. The real structure is the conjugate transpose, with Hermitian and skew-Hermitian parts of real dimension $16$ each, and the $*$-unitary groups $U(4)$ and $SU(4)$. The $M_4(\mathbb{C})_{\mathbb{B},L}$ model is a four-dimensional subalgebra of the full sixteen-dimensional algebra; the two have different traces and determinants and must not be identified. A second construction gives the algebra as $M_2(\mathbb{C})\otimes M_2(\mathbb{C})^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(M_2(\mathbb{C}))$, hence as $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$; in the coefficient basis its basis is not the matrix-unit basis, and every matrix unit is a sum of four of its elements.

$$
\boxed{\ \dim_\mathbb{C}M_4(\mathbb{C})=16,\quad \dim_\mathbb{R}=32,\quad Z(M_4)=\mathbb{C}I,\quad \dim_\mathbb{C}PGL_4=15,\quad \dim_\mathbb{C}SL_4=15.\ }
$$

| Object | Complex dimension | Real dimension |
|---|---|---|
| $M_4(\mathbb{C})$ | $16$ | $32$ |
| $GL_4(\mathbb{C})$ | $16$ | $32$ |
| $SL_4(\mathbb{C})$ | $15$ | $30$ |
| $PGL_4(\mathbb{C})$ | $15$ | $30$ |
| $\mathfrak{sl}_4(\mathbb{C})$ | $15$ | $30$ |
| $\mathfrak{u}(4)$ | — | $16$ |
| $\mathfrak{su}(4)$ | — | $15$ |
| $\operatorname{Herm}_4$ | — | $16$ |
| Flag variety $GL_4/B$ | $6$ | $12$ |
| Centre $\mathbb{C}I$ | $1$ | $2$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_4(\mathbb{C})$ | the algebra of $4\times4$ complex matrices |
| $E_{ij}$ | the matrix unit, $1$ in position $(i,j)$ |
| $I$ | the unit, $\sum_kE_{kk}$ |
| $\operatorname{tr}$, $\det$ | the trace and the determinant |
| $A^*=\bar A^{\mathsf T}$ | the conjugate transpose |
| $Z(M_4)$ | the centre, $\mathbb{C}I$ |
| $GL_4$, $SL_4$, $PGL_4$ | the unit group, the determinant-one subgroup, the projective group |
| $\mathfrak{u}(4)$, $\mathfrak{su}(4)$ | the skew-Hermitian algebra and its traceless part |
| $\operatorname{Herm}_4$ | the Hermitian matrices |
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$ |
| $B$ | the Borel subgroup of upper triangular matrices |
| $\Sigma=\{\det=0\}$ | the singular set |
| $L$ | the left regular representation of $\mathbb{B}$, with image $M_4(\mathbb{C})_{\mathbb{B},L}$; $L_a=L(a)$ |
| $R_b$ | right multiplication on $A$, $R_b(X)=Xb$ |
| $T_{a,b}=L_aR_b$ | the two-sided operator $X\mapsto aXb$ |
| $F_{ij}$ | matrix units of $A=M_n(\mathbb{C})$ in the construction |
| $c^{\lambda}_{\ \mu\rho}$ | structure constants of $\mathbb{B}$, $e_\mu e_\rho=\sum_\lambda c^{\lambda}_{\ \mu\rho}e_\lambda$ |
| $N$ | the biquaternion norm, $N(a)=a_t^2+a_x^2+a_y^2+a_z^2$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for central simple algebras, matrix rings and two-sided ideals.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the simplicity of $M_n(\mathbb{C})$ and the structure of matrix rings.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the trace, the determinant, the characteristic polynomial, the singular values and the polar decomposition.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $GL_4$, $SL_4$, $U(4)$ and their Lie algebras.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the general algebra at order $n$.
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the sixteen matrices $T_{\mu\nu}$, their product tables, the coefficient formula and the length.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the abstract theorem $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.
- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the sixteen matrices $T_{\mu\nu}$, the gamma frame and the product question.
- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the four-dimensional regular model and its different trace and determinant.
- [Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), for the root that produces the idempotents.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the sixteen corners of the full algebra.
- [The Element, the Coordinates and the Trace of $M_4(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m4c.html), for the element and its trace.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the positive definite trace form.
