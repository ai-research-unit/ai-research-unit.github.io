# __The Endomorphisms of $\mathbb{C}^2$__

## Introduction

This article treats the algebra of the operators on the complex two-space: the complex-linear endomorphisms, their identification with the matrix algebra $M_2(\mathbb{C})$, the group of units and the projective quotient, the conjugate-linear maps, and the two centralisers cut out by the complex structure. The algebra is the first non-commutative object of the synthetic part, and it is the algebra whose simple module is the space itself.

The article states the structure of the algebra as an operator algebra on $\mathbb{C}^2$. It does not restate the matrix theory: the product rule, the trace, the determinant, the six subspaces, the centraliser and the double centraliser of a matrix and the Jordan form are the subject of the $M_2(\mathbb{C})$ Model articles of the biquaternion category, cited at each point. The tensor square is *The Tensor Square of $\mathbb{C}^2$*; the classical groups as groups of matrices are *The Classical Groups of $\mathbb{C}^2$*; the general theory of endomorphism algebras is *Endomorphisms of a Linear Space* and *The Endomorphism Algebra of a Module*.

**The two facts that organise the article are the dimension count and the commutant.** The algebra has dimension $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$; the operators that commute with the complex structure are exactly the complex-linear ones, and the operators that commute with all of them are the complex scalars.

## The Algebra of Endomorphisms

**The complex-linear endomorphisms of $\mathbb{C}^2$ form the algebra $M_2(\mathbb{C})$, of dimension $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$; the composition is the product and the identity is the unit.**

**Definition.** The **endomorphism algebra** is
$$
\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)=\{T:\mathbb{C}^2\to\mathbb{C}^2:T\text{ complex-linear}\},
$$
with the sum, the scalar multiplication and the composition of maps. It is written $\operatorname{End}(V)$ when the space is fixed.

**Theorem (the matrix algebra).** After the choice of the complex basis $e_1,e_2$, the map $T\mapsto M(T)$ sending an operator to its matrix is an isomorphism of $\mathbb{C}$-algebras
$$
\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)\cong M_2(\mathbb{C}).
$$
The algebra has dimension $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$.

*Proof.* The matrix of $T$ in the basis has entries $M_{jk}$ defined by $T(e_k)=\sum_jM_{jk}e_j$. The map is bijective by the correspondence between linear maps and matrices, it preserves the sum and the scalar product entrywise, and $M(ST)=M(S)M(T)$ by the rule of the product of matrices. The dimension is the number of entries, $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$.

**Definition.** The **matrix units** are $E_{jk}$, the matrix with $1$ in the entry $(j,k)$ and $0$ elsewhere. They satisfy
$$
E_{jk}E_{lm}=\delta_{kl}E_{jm},\qquad \sum_{j,k}M_{jk}E_{jk}=M.
$$

**Proposition (the centre and the simplicity).** The centre of $\operatorname{End}(V)$ is the line of scalar operators $\mathbb{C}I$, of real dimension $2$, and the algebra is simple: its only two-sided ideals are $0$ and the whole algebra.

*Proof.* A matrix commuting with every $E_{jk}$ is scalar: commuting with $E_{11}$ and $E_{22}$ kills the two off-diagonal entries, and commuting with $E_{12}$ makes the two diagonal entries equal. A nonzero two-sided ideal contains a nonzero matrix $M$, hence contains $E_{jj}ME_{kk}=M_{jk}E_{jk}$ for some pair with $M_{jk}\neq0$, hence contains every $E_{lm}$ by multiplying by the units on the left and on the right, hence is the whole algebra.

**Proposition (trace and determinant).** The trace $\operatorname{tr}T$ and the determinant $\det T$ are defined by the matrix, are independent of the basis, and satisfy
$$
\operatorname{tr}(ST)=\operatorname{tr}(TS),\qquad \det(ST)=\det S\,\det T.
$$
Every $T$ satisfies the Cayley–Hamilton identity
$$
T^2-(\operatorname{tr}T)\,T+(\det T)I=0.
$$

*Proof.* The trace and the determinant of a matrix are invariant under conjugation, hence independent of the basis; the multiplicativity of the determinant and the cyclicity of the trace are the matrix identities. The Cayley–Hamilton identity in dimension two is the computation of the characteristic polynomial $\lambda^2-(\operatorname{tr}T)\lambda+\det T$ at $\lambda=T$, and it is verified entrywise or by the general theorem (*The Product, the Trace and the Determinant* in the $M_2(\mathbb{C})$ Model).

**Remark (the spectrum).** Over $\mathbb{C}$ every operator has two eigenvalues counted with multiplicity, the roots of $\lambda^2-(\operatorname{tr}T)\lambda+\det T$. **The discriminant $\Delta=(\operatorname{tr}T)^2-4\det T$ separates the two cases**: for $\Delta\neq0$ the eigenvalues are distinct and the operator is diagonalisable; for $\Delta=0$ the operator is either scalar or a single Jordan block of size two, and in the second case it is not diagonalisable (*The Spectrum* and *The Jordan Basis* in the $M_2(\mathbb{C})$ Model).

## The General Linear Group and the Projective Group

**The invertible operators form the open dense group $\mathrm{GL}_2(\mathbb{C})$ of real dimension $8$; the scalar operators act trivially on the projective line, and the quotient $\mathrm{PGL}_2(\mathbb{C})$ acts faithfully there.**

**Definition.** The **general linear group** is $\mathrm{GL}_2(\mathbb{C})=\{T:\det T\neq0\}$, and the **special linear group** is $\mathrm{SL}_2(\mathbb{C})=\{T:\det T=1\}$.

**Proposition (the dimensions).** The group $\mathrm{GL}_2(\mathbb{C})$ is open and dense in $\operatorname{End}(\mathbb{C}^2)$ and has real dimension $8$; the subgroup $\mathrm{SL}_2(\mathbb{C})$ is a complex hypersurface of real dimension $6$.

*Proof.* The complement of $\mathrm{GL}_2$ is the zero set of the determinant, a polynomial equation, hence closed and of empty interior; the group is nonempty and open. The dimension is that of the algebra. The condition $\det T=1$ is one complex equation on the four complex entries, hence a complex hypersurface of complex dimension $3$ and real dimension $6$, and it is a subgroup because the determinant is multiplicative.

**Definition.** The **projective general linear group** is $\mathrm{PGL}_2(\mathbb{C})=\mathrm{GL}_2(\mathbb{C})/\mathbb{C}^{\times}$, the quotient by the scalar matrices; the **projective special linear group** is $\mathrm{PSL}_2(\mathbb{C})=\mathrm{SL}_2(\mathbb{C})/\{\pm I\}$.

**Proposition ($\mathrm{PGL}_2=\mathrm{PSL}_2$).** Every class in $\mathrm{PGL}_2(\mathbb{C})$ has a representative of determinant $1$, so the natural map $\mathrm{PSL}_2(\mathbb{C})\to\mathrm{PGL}_2(\mathbb{C})$ is an isomorphism; both groups have real dimension $6$.

*Proof.* For $A$ with $d=\det A\neq0$, choose $\lambda$ with $\lambda^2d=1$ and replace $A$ by $\lambda A$; the determinant becomes $1$ and the class in the quotient is unchanged. The kernel of the map is the set of scalars of determinant $1$, that is $\{\pm I\}$, which is exactly the subgroup quotiented out. The dimension is $8-2=6$.

**Proposition (the action on the projective line).** The group $\mathrm{PGL}_2(\mathbb{C})$ acts on $\mathbb{CP}^1$ by
$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}\cdot[z_1:z_2]=[az_1+bz_2:cz_1+dz_2],
$$
the action is faithful and sharply $3$-transitive, and the stabiliser of a point has real dimension $4$.

*Proof.* The formula is well defined because the scalar matrices act trivially, and it is an action because the product of matrices corresponds to the composition. The kernel is the scalars, so the action is faithful. Three distinct points are sent to three distinct points by a unique element: in the chart $[t:1]$ the condition is the interpolation of a Möbius map at three points, which has a unique solution with $ad-bc\neq0$. The orbit of a point is $\mathbb{CP}^1$ of real dimension $2$, so the stabiliser has dimension $6-2=4$.

**Remark (two actions, two quotients).** The group $\mathrm{GL}_2(\mathbb{C})$ acts on $\mathbb{C}^2$ and on $\mathbb{CP}^1$; the group $\mathrm{PGL}_2(\mathbb{C})$ acts on $\mathbb{CP}^1$ only, and the scalar matrices are exactly the kernel of the second action. **The two actions are not the same action read twice**: the first is transitive on the nonzero vectors, the second on the lines, and the first does not descend to the projective line without the quotient. The Möbius action is *The Projective Line and the Möbius Action* in the $M_2(\mathbb{C})$ Model, and the groups as classical groups are *The Classical Groups of $\mathbb{C}^2$*.

## Conjugate-Linear Maps

**The conjugate-linear endomorphisms form a real vector space of dimension $8$; the product of two of them is complex-linear, and together with the complex-linear maps they fill the real endomorphism algebra.**

**Definition.** A map $T:\mathbb{C}^2\to\mathbb{C}^2$ is **conjugate-linear** when it is additive and $T(\lambda z)=\overline{\lambda}T(z)$ for every $\lambda\in\mathbb{C}$. The space is written $\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V)$.

**Proposition (the dimension and the model).** The space $\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V)$ is a complex vector space of complex dimension $4$ and real dimension $8$. Every element is uniquely $A\circ c$, where $A\in\operatorname{End}(V)$ and $c$ is the coefficientwise conjugation $c(z)=\overline{z}$; the map $A\mapsto A\circ c$ is a complex-linear isomorphism of vector spaces.

*Proof.* The map $c$ is conjugate-linear and invertible, with $c^2=I$. If $T$ is conjugate-linear, then $A=T\circ c^{-1}=T\circ c$ is complex-linear, because $A(\lambda z)=T(\overline{\lambda}\overline{z})=\overline{\overline{\lambda}}T(\overline{z})=\lambda A(z)$; and $T=A\circ c$. The correspondence is bijective and complex-linear in $A$. The dimension is that of $\operatorname{End}(V)$.

**Theorem (the splitting of the real algebra).** The real endomorphism algebra is the direct sum
$$
\operatorname{End}_{\mathbb{R}}(V)=\operatorname{End}_{\mathbb{C}}(V)\oplus\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V),
$$
of two complex vector spaces of complex dimension $4$, hence of real dimensions $8+8=16$.

*Proof.* This is the splitting $T=T_++T_-$ of *The Realification of $\mathbb{C}^2$*, with $T_+=\tfrac12(T-JTJ)$ and $T_-=\tfrac12(T+JTJ)$.

**Proposition (the product rule).** The product of two conjugate-linear maps is complex-linear, the product of a complex-linear and a conjugate-linear map is conjugate-linear in either order, and the product of two complex-linear maps is complex-linear.

*Proof.* For conjugate-linear $S,T$ and $\lambda\in\mathbb{C}$, $ST(\lambda z)=S(\overline{\lambda}T(z))=\overline{\overline{\lambda}}S(T(z))=\lambda ST(z)$. The other two cases are the same computation with one or with no conjugation.

**Remark (a graded algebra).** The decomposition is a $\mathbb{Z}_2$-grading of the real algebra, with the even part $\operatorname{End}_{\mathbb{C}}(V)$ and the odd part $\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V)$. **The odd part is not a subalgebra; it is a bimodule over the even part**, and its square lies in the even part. In the standard basis every real-linear map is $T(z)=Az+B\overline{z}$ with $A,B\in M_2(\mathbb{C})$, the complex-linear maps are those with $B=0$ and the conjugate-linear ones those with $A=0$; the form is *The Realification of $\mathbb{C}^2$*.

## The Centraliser of $J$ and the Double Centraliser

**The operators commuting with the complex structure are exactly the complex-linear ones; the operators commuting with all of them are exactly the complex scalars.**

**Theorem (the centraliser of $J$).** In $\operatorname{End}_{\mathbb{R}}(V)$,
$$
\{T:TJ=JT\}=\operatorname{End}_{\mathbb{C}}(V),
$$
of real dimension $8$.

*Proof.* The condition $TJ=JT$ is the condition of complex linearity, by the proposition of *The Realification of $\mathbb{C}^2$*. The dimension is that of $M_2(\mathbb{C})$ over $\mathbb{R}$.

**Theorem (the double centraliser).** The operators commuting with every complex-linear operator are the maps $z\mapsto\alpha z$ with $\alpha\in\mathbb{C}$, that is
$$
\{T\in\operatorname{End}_{\mathbb{R}}(V):TS=ST\text{ for all }S\in\operatorname{End}_{\mathbb{C}}(V)\}=\{aI+bJ:a,b\in\mathbb{R}\}\cong\mathbb{C},
$$
of real dimension $2$. The centraliser of this line is $\operatorname{End}_{\mathbb{C}}(V)$ again.

*Proof.* Let $T$ commute with every $S$. Since $J$ is complex-linear, $T$ commutes with $J$, hence $T$ is complex-linear. A complex-linear operator commuting with every complex-linear operator is scalar: testing against $E_{11}$ and $E_{12}$ gives the same computation as for the centre. Hence $T=aI+bJ$, that is multiplication by the complex number $a+ib$. Conversely such a map commutes with every complex-linear map. The second statement is the same computation applied to the line: a map commuting with $aI+bJ$ for all $a,b$ commutes with $J$, hence is complex-linear.

**Remark (the two centralisers are not the same).** The centraliser of $J$ is the whole matrix algebra, of dimension $8$; the centraliser of the matrix algebra is the line of complex scalars, of dimension $2$. **The passage from an operator to the operators commuting with it thus loses and then recovers the algebra**: the bicommutant of $\operatorname{End}_{\mathbb{C}}(V)$ in $\operatorname{End}_{\mathbb{R}}(V)$ is $\operatorname{End}_{\mathbb{C}}(V)$, which is the finite-dimensional case of the double centraliser theorem. The matrix computation is *The Centraliser and the Double Centraliser* in the $M_2(\mathbb{C})$ Model; the general theorem is *The Endomorphism Algebra of a Module*.

**Remark (the centraliser of one operator).** The centraliser in $\operatorname{End}_{\mathbb{C}}(V)$ of a single operator $T$ is larger than the scalars: it has complex dimension $4$ when $T$ is scalar and complex dimension $2$ otherwise. **The two-dimensional case is the algebra of polynomials in $T$**, which is $\mathbb{C}[T]$ and coincides with the centraliser for every non-scalar $2\times2$ matrix (*The Centraliser and the Double Centraliser* in the $M_2(\mathbb{C})$ Model).

## The Biquaternion Identification

**The algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)$ is the biquaternion algebra, and the space is its unique simple module.**

**Theorem (the identification).** There is an isomorphism of $\mathbb{C}$-algebras
$$
\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C}),
$$
given on the units by
$$
e_t\mapsto I,\qquad \vec e_x\mapsto\begin{pmatrix}i&0\\0&-i\end{pmatrix},\qquad \vec e_y\mapsto\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad \vec e_z\mapsto\begin{pmatrix}0&i\\i&0\end{pmatrix}.
$$

*Proof.* The four matrices are complex-linear and satisfy the quaternion relations: the three vector images square to $-I$, their pairwise products are the images of the corresponding vector units, and they are linearly independent over $\mathbb{C}$. They therefore define a $\mathbb{C}$-algebra homomorphism from $\mathbb{B}$, which is of dimension $4$ over $\mathbb{C}$, into $M_2(\mathbb{C})$, also of dimension $4$; the map is injective because the images are independent, hence bijective.

**Theorem (the simple module).** The space $\mathbb{C}^2$ is a simple left module over $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)$ under $T\cdot z=T(z)$; it is the unique simple module up to isomorphism, and the action is faithful.

*Proof.* A submodule is a complex subspace stable under every operator; the only such subspaces are $0$ and the whole space, since the operators $E_{jk}$ move any nonzero vector to any other. Faithfulness is the definition of the endomorphism algebra as a subalgebra of the maps. Uniqueness is the classification of the simple modules over a matrix algebra (*The Regular Module in the Biquaternion Algebra* and *Modules over an Algebra*).

**Remark (the choices behind the identification).** The isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ is not canonical: it depends on the choice of the complex basis of $\mathbb{C}^2$ and on the identification of the quaternion units with the three matrices above. **What is canonical is the algebra of operators and its action on the space**; the matrix model is a coordinate reading, and the conjugations of the biquaternion algebra are read on the matrices by the corresponding conjugations (*The Element, the Coordinates and the Conjugations* and *The Conjugations and the Adjoints* in the $M_2(\mathbb{C})$ Model).

## Summary

The complex-linear endomorphisms of $\mathbb{C}^2$ form the algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)\cong M_2(\mathbb{C})$, of dimension $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$, with the matrix units $E_{jk}$ satisfying $E_{jk}E_{lm}=\delta_{kl}E_{jm}$; its centre is the line of scalars, it is simple, and its trace, determinant and Cayley–Hamilton identity are $T^2-(\operatorname{tr}T)T+(\det T)I=0$. The invertible operators form $\mathrm{GL}_2(\mathbb{C})$, open and dense of real dimension $8$; $\mathrm{SL}_2(\mathbb{C})$ has dimension $6$; and $\mathrm{PGL}_2(\mathbb{C})=\mathrm{GL}_2(\mathbb{C})/\mathbb{C}^{\times}\cong\mathrm{PSL}_2(\mathbb{C})$ has dimension $6$ and acts faithfully and sharply $3$-transitively on $\mathbb{CP}^1$, with stabilisers of dimension $4$.

The conjugate-linear maps form a complex vector space of dimension $4$ and real dimension $8$, every one of them is $A\circ c$ with $A$ complex-linear, and the real algebra splits as $\operatorname{End}_{\mathbb{R}}=\operatorname{End}_{\mathbb{C}}\oplus\operatorname{Hom}_{\bar{\mathbb{C}}}$ with dimensions $16=8+8$; the product of two odd elements is even. The centraliser of $J$ is $\operatorname{End}_{\mathbb{C}}$, of dimension $8$; the centraliser of $\operatorname{End}_{\mathbb{C}}$ is the line $\{aI+bJ\}\cong\mathbb{C}$, of dimension $2$; and the bicommutant returns $\operatorname{End}_{\mathbb{C}}$. The algebra is the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, and the space is its unique simple module.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)$ | the complex-linear endomorphisms, isomorphic to $M_2(\mathbb{C})$ |
| $E_{jk}$ | the matrix units, $E_{jk}E_{lm}=\delta_{kl}E_{jm}$ |
| $\operatorname{tr}T$, $\det T$ | the trace and the determinant, independent of the basis |
| $\mathrm{GL}_2(\mathbb{C})$, $\mathrm{SL}_2(\mathbb{C})$ | the invertible operators and those of determinant $1$ |
| $\mathrm{PGL}_2(\mathbb{C})=\mathrm{GL}_2(\mathbb{C})/\mathbb{C}^{\times}$ | the projective general linear group, isomorphic to $\mathrm{PSL}_2(\mathbb{C})$ |
| $\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V)$ | the conjugate-linear endomorphisms, complex dimension $4$ |
| $c(z)=\overline{z}$ | the coefficientwise conjugation, a conjugate-linear involution |
| $\{T:TJ=JT\}=\operatorname{End}_{\mathbb{C}}(V)$ | the centraliser of the complex structure |
| $\{T:TS=ST\ \forall S\}=\{aI+bJ\}$ | the centraliser of the algebra, the complex scalars |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space and the complex structure.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-complex-two-space.html), for the splitting of the real endomorphisms and the matrix form $T(z)=Az+B\overline{z}$.
- [The Tensor Square of $\mathbb{C}^2$](the-tensor-square-of-the-complex-two-space.html), the next article, for $V\otimes V$ and its relation to the endomorphism algebra.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-the-complex-two-space.html), for $\mathrm{GL}_2$, $\mathrm{SL}_2$, $\mathrm{U}(2)$, $\mathrm{SU}(2)$ and their intersections.
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the matrix computations of the product, the trace and the determinant.
- [$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m2c-model-the-centraliser-and-the-double-centraliser.html), for the centraliser of a single matrix and the bicommutant.
- [$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](m2c-representation-gl2-sl2-and-the-determinant.html), for the groups and the determinant.
- [$M_2(\mathbb{C})$ Representation : The Projective Line and the Möbius Action](m2c-representation-the-projective-line-and-the-mobius-action.html), for the action on $\mathbb{CP}^1$.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and its isomorphism with $M_2(\mathbb{C})$.
- [The Endomorphism Algebra of a Module](the-endomorphism-algebra-of-a-module.html), for the double centraliser theorem in general.
