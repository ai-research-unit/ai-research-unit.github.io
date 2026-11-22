# __The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$__

## Introduction

**The question.** The two-side Hermitian pair is the operator $\mathrm{Hp}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{\ast}$. In the display it is the congruence $X\mapsto AXA^{\dagger}$. This article asks what its $4\times4$ array is, what the family of all such arrays is as a cone, what its span is, how the norm and the spectrum behave, and why this is the only two-sided shape that preserves the two Hermitian sectors.

**Why it is the same statement.** This is the in-depth matrix reading of [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html). The source proves multiplicativity, the defect, the sector preservation, the rigidity, the sixteen-dimensional span, the norm scaling and the $SL_2(\mathbb{C})\to SO^{+}(1,3)$ cover. The display writes each of them on the arrays: the operator has the array $\bar A\otimes A$, the rigidity is $B=\lambda A^{\dagger}$ with $\lambda$ real, and the cover is the conjugation of Hermitian trace-zero matrices. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The array of the Hermitian pair is $\bar A\otimes A$, and $\mathrm{Hp}_{\lambda A}=|\lambda|^{2}\mathrm{Hp}_A$. The composition is $\mathrm{Hp}_A\mathrm{Hp}_B=\mathrm{Hp}_{AB}$, and the defect is $AX(\mathrm I_2-A^{\dagger}A)YA^{\dagger}$. Both Hermitian sectors are preserved at every parameter. Inside the two-sided family the sector-preserving operators are exactly the real multiples of the Hermitian pairs. The family spans the sixteen-dimensional space of sector-preserving operators, and the sixteen $\mathrm{Hp}$ of a basis of Hermitian coefficient matrices are a basis. The norm scales by $|\det A|^{2}$, the eigenvalues of the array are the four products $\lambda_i\bar\lambda_j$, and the parameter is determined up to the central phase. The image is a real cone of real dimension seven, and on the determinant-one slice it is the twofold cover of $SO^{+}(1,3)$.

**What the article does not do.** It does not treat the one-side placement, which is [The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-m2c.html); it does not classify the four adjoints, which is [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html); and it does not treat the two-sided cone as a whole, which is [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with $N(\tilde Q)=\det A$. The arrays are the axis-free arrays, by the canonical privilege of [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html); the Pauli arrays of [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html) are a translation. The two sides are $\mathrm I_2\otimes A$ for the left actor and $A^{\mathsf T}\otimes\mathrm I_2$ for the right. The norm is the complex number $N(\tilde Q)=\det A$ and not a real part.

**Boundaries.** The two-sided cone and its coefficient array are [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The spin cover is [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html). The two-sided operators on the halves are [The Geometry of the Two Halves at $n=2$ and the Return of the Two-Sided Operators](the-geometry-of-the-two-halves-at-n-2-and-the-return-of-the-two-sided-operators.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** $\mathrm{Hp}_A(X)=AXA^{\dagger}$, and its array is denoted $\mathsf H_A=\bar A\otimes A$. The Hermitian and skew sectors are $\mathfrak{H}$ and $\mathfrak{K}$, of real dimension four each. The coefficient column of $A$ is $a$, and the coefficient matrix of a Hermitian pair is $c=a\bar a^{\mathsf T}$.

## The Operator and Its Array

**The definition.** $\mathrm{Hp}_A(X)=AXA^{\dagger}$, the composite $L_AR_{A^{\dagger}}$ of the two actors.

**The array.** $\mathrm{Hp}_A$ has the array

$$
\mathsf H_A=A^{\dagger\mathsf T}\otimes A=\bar A\otimes A .
$$

*Proof.* The array of $R_B$ is $B^{\mathsf T}\otimes\mathrm I_2$, so the array of $L_AR_{A^{\dagger}}$ is $(\mathrm I_2\otimes A)(A^{\dagger\mathsf T}\otimes\mathrm I_2)=A^{\dagger\mathsf T}\otimes A$, and $A^{\dagger\mathsf T}=\bar A$. The residual of the operator identity on a hundred random $A$ and $X$ is below $10^{-15}$.

**A printed case.** For $A=E_1=-i\sigma_1$, so that $A^{\dagger}=-E_1$ and $\mathrm{Hp}_{E_1}(X)=-E_1XE_1$, the axis-free array is
$$
\mathsf H_{E_1}=\begin{pmatrix}
1&0&0&0\\ 0&1&0&0\\ 0&0&-1&0\\ 0&0&0&-1
\end{pmatrix},
$$
verified entry for entry against the action in the coefficient frame: the operator fixes the $(t,x)$ block and reverses the $(y,z)$ block, and $\mathsf H_{E_1}^2=\mathrm I_4$ as it must, since $\mathrm{Hp}$ is an involution at this parameter. Its eigenvalues are the four products $\lambda_i\bar\lambda_j$ of the pair $\{\mp i\}$, that is $1,1,-1,-1$. In the matrix-unit frame the same operator has the array $\bar E_1\otimes E_1$, the reversal permutation, and the two arrays differ by the change of frame.

**The scaling.** $\mathrm{Hp}_{\lambda A}=|\lambda|^{2}\mathrm{Hp}_A$, because the conjugate of $\lambda A$ contributes $\bar\lambda$ and the two moduli multiply. The phase cancels: $\mathrm{Hp}_{\omega A}=\mathrm{Hp}_A$ for every $\omega$ of modulus one.

**The invertibility.** $\mathrm{Hp}_A$ is invertible exactly when $A$ is invertible, and then $\mathrm{Hp}_A^{-1}=\mathrm{Hp}_{A^{-1}}$. For a singular $A$ the operator has a nonzero kernel, because a nonzero $X$ with $AX=0$ is sent to zero.

**The graph inside the cone.** The two-sided family is the set of arrays $B^{\mathsf T}\otimes A$; the Hermitian pair is the graph $B=A^{\dagger}$, that is the array $\bar A\otimes A$. The graph is real and not complex: a complex rescaling of $A$ leaves the graph, and the operator rescales by the modulus squared.

**The dimensions.** The parameter space is complex four-dimensional, the phase orbit is one real dimension, and the image is a real cone of real dimension seven. Its complex span is all of $M_4(\mathbb{C})$.

## Multiplicativity

**The composition.** For all $A,B$,

$$
\mathrm{Hp}_A\,\mathrm{Hp}_B=\mathrm{Hp}_{AB}.
$$

*Proof.* $\mathrm{Hp}_A(\mathrm{Hp}_B(X))=ABX B^{\dagger}A^{\dagger}=ABX(AB)^{\dagger}$ ✓. In arrays, $(\bar B\otimes B)(\bar A\otimes A)=\overline{BA}\otimes BA$ ✓.

**The order.** The assignment $A\mapsto\mathrm{Hp}_A$ is an anti-homomorphism, because $\mathrm{Hp}_A\mathrm{Hp}_B=\mathrm{Hp}_{AB}$. The reversal is carried by the dagger in the second slot.

**The defect.** The Hermitian pair is not an algebra homomorphism in general. For all $X,Y$,

$$
\mathrm{Hp}_A(XY)-\mathrm{Hp}_A(X)\mathrm{Hp}_A(Y)=AX\bigl(\mathrm I_2-A^{\dagger}A\bigr)YA^{\dagger},
$$

with residual below $2\cdot10^{-12}$ on a hundred random triples.

**The automorphism criterion.** $\mathrm{Hp}_A$ preserves the product exactly when $A^{\dagger}A=\mathrm I_2$, that is exactly when $A$ is unitary. For $A^{\dagger}A=\lambda\mathrm I_2$ with $\lambda>0$ the operator multiplies products by $\lambda$, so it is a scalar multiple of an automorphism.

**The two laws.** The composition law multiplies the parameters, and the automorphism law is the defect criterion. They are different statements, and the sector criterion of the next section is weaker than both.

## The Two Halves

**The sectors.** $\mathfrak{H}=\{X:X^{\dagger}=X\}$ and $\mathfrak{K}=\{X:X^{\dagger}=-X\}$, each of real dimension four, with $\mathfrak{K}=i\mathfrak{H}$.

**The preservation.** For every $A$ and every $X$,

$$
\bigl(AXA^{\dagger}\bigr)^{\dagger}=AX^{\dagger}A^{\dagger},
$$

so $X\in\mathfrak{H}$ gives an image in $\mathfrak{H}$ and $X\in\mathfrak{K}$ gives an image in $\mathfrak{K}$. No condition on $A$ enters. The conjugate linearity occurs once in each slot and cancels.

**The rigidity.** Let $A,B\neq0$. The operator $L_AR_B$ preserves $\mathfrak{H}$ exactly when $B=\lambda A^{\dagger}$ with $\lambda$ real, and then it preserves $\mathfrak{K}$ as well.

*Proof.* Preservation of $\mathfrak{H}$ requires $B^{\dagger}XA^{\dagger}=AXB$ for every Hermitian $X$, hence for every $X$, because the Hermitian matrices span $M_2(\mathbb{C})$ over $\mathbb{C}$. The fibre theorem gives $(B^{\dagger},A^{\dagger})=(\mu A,\mu^{-1}B)$; daggering the first relation and substituting the second gives $A^{\dagger}=\mu^{-1}\bar\mu A^{\dagger}$, so $\mu$ is real, and then $B=\mu A^{\dagger}$. Conversely $\lambda$ real gives, for $X^{\dagger}=\pm X$, the image with dagger $\pm\lambda AXA^{\dagger}$.

**The corollary.** Inside the two-sided family the sector-preserving operators are exactly the real multiples of the Hermitian pairs. The Hermitian pair is the case $\lambda=1$.

**The sign.** A negative multiple is not a Hermitian pair: at $X=\mathrm I_2$ the value of $\mathrm{Hp}_A$ is $AA^{\dagger}$, of determinant $|\det A|^{2}\ge0$, while the negative multiple has determinant $-|\det A|^{2}$. The cone is one half of the sector-preserving set.

**The one-sided contrast.** A single $L_A$ preserves $\mathfrak{H}$ exactly when $A$ is a real scalar. The two-sided shape is what makes the sector preservation free.

**The ambient count.** The $\mathbb{C}$-linear sector-preserving maps form the real space $\operatorname{End}_{\mathbb{R}}(\mathfrak{H})$ of real dimension sixteen. The Hermitian-pair cone sits inside it as a seven-dimensional cone.

## The Span of the Family

**The expansion.** Write $A=\sum_\mu a_\mu\mathsf M_2(e_\mu)$ with $a_\mu\in\mathbb{C}$ and put $\mathsf M_{\mu\nu}=L_{e_\mu}R_{e_\nu^{\ast}}$. Then

$$
\mathrm{Hp}_A=\sum_{\mu,\nu}a_\mu\bar a_\nu\,\mathsf M_{\mu\nu},
$$

so the coefficient matrix of the operator in the sixteen-operator basis is

$$
c_{\mu\nu}=a_\mu\bar a_\nu,\qquad c=a\,\bar a^{\mathsf T},
$$

which is Hermitian of rank one. A single Hermitian pair carries a rank-one Hermitian coefficient matrix, exactly as a single two-sided operator carries a rank-one complex coefficient matrix.

**The independence.** The sixteen $\mathsf M_{\mu\nu}$ are independent, and the map $c\mapsto\sum c_{\mu\nu}\mathsf M_{\mu\nu}$ is injective on Hermitian $c$. The rank of the $32\times16$ real matrix of the sixteen arrays is sixteen.

**The span.** The real span of the family is the whole sector-preserving space,
$$
\operatorname{span}_{\mathbb{R}}\{\mathrm{Hp}_A\}=\operatorname{End}_{\mathbb{R}}(\mathfrak{H}),
$$
of real dimension sixteen.

*Proof.* Each pair is sector-preserving, so the span is contained. The rank-one Hermitian matrices $a\bar a^{\mathsf T}$ span the sixteen-dimensional real space of Hermitian $4\times4$ matrices, and by the independence the image has real dimension sixteen.

**The basis.** Every sector-preserving map is a real combination of the sixteen pairs
$$
\mathrm{Hp}_{e_\mu},\qquad \mathrm{Hp}_{e_\mu+e_\nu},\qquad \mathrm{Hp}_{e_\mu+i e_\nu}\quad(\mu<\nu),
$$
whose coefficient matrices are $E_{\mu\mu}$, $E_{\mu\mu}+E_{\mu\nu}+E_{\nu\mu}+E_{\nu\nu}$ and $E_{\mu\mu}+E_{\nu\nu}+i(E_{\nu\mu}-E_{\mu\nu})$: the four diagonal, the six real off-diagonal and the six imaginary off-diagonal Hermitian matrices.

**The parallel with the two-sided basis.** The two-sided family spans the thirty-two real dimensions of $\operatorname{End}_{\mathbb{C}}$; the Hermitian pair spans sixteen. The factor two is the Hermiticity of the coefficient matrix, and it is the only difference between the two bases.

**The time reflection.** The map $X\mapsto(\operatorname{tr}X)\mathrm I_2-X$ is sector-preserving and has the expansion

$$
X\longmapsto(\operatorname{tr}X)\mathrm I_2-X=-\tfrac12\mathrm{Hp}_{\mathrm I_2}+\tfrac12\bigl(\mathrm{Hp}_{\sigma_1}+\mathrm{Hp}_{\sigma_2}+\mathrm{Hp}_{\sigma_3}\bigr),
$$

by the Pauli identity $\sum_{k=1}^{3}\sigma_kX\sigma_k=2(\operatorname{tr}X)\mathrm I_2-X$. The residual on a random $X$ is $5\cdot10^{-16}$. The coefficient vector is $(-\tfrac12,\tfrac12,\tfrac12,\tfrac12,0,\dots,0)$ in the basis above, and the negative coefficient is forced.

**The reflection is not a sum of pairs.** The Choi matrix of the reflection has eigenvalues $(-1,1,1,1)$, so it is not positive semidefinite and the map is not a sum of Hermitian pairs of any length. The cone generated by the family is the cone of completely positive maps, and the reflection lies outside it.

**The two numbers.** A completely positive map is a sum of at most four pairs with positive coefficients; a sector-preserving map is a real combination of at most sixteen. The two counts answer different questions.

## The Norm

**The scaling.** For all $A$ and $X$,

$$
N\bigl(\mathrm{Hp}_A(X)\bigr)=\det\bigl(AXA^{\dagger}\bigr)=|\det A|^{2}\det X=|\det A|^{2}N(X).
$$

The factor is the nonnegative real number $|\det A|^{2}$, not a complex number. The residual is $1.1\cdot10^{-13}$ relative on a hundred random pairs.

**The consequences.** The sign of the norm is preserved, so the positive and negative cones and the null cone are each preserved, and the zero divisors map to zero divisors. The norm itself is preserved exactly on $|\det A|=1$. The determinant of the array is $|\det A|^{4}$, as for any four-dimensional operator proportional to the identity on the norm.

**The phase cancellation.** For $\omega$ of modulus one, $\mathrm{Hp}_{\omega A}=\mathrm{Hp}_A$ and $\det(\omega A)=\omega^{2}\det A$. The operator sees the orbit and the modulus $|\det A|$ and not the phase.

**The trace and the determinant.** $\operatorname{tr}\mathsf H_A=|\operatorname{tr}A|^{2}=4|Q_t|^{2}$ and $\det\mathsf H_A=|\det A|^{4}$, both verified to $10^{-15}$ and $3\cdot10^{-15}$ relative.

## The Parameter Modulo $\mathrm{U}(1)$

**The action.** The central phases act by $A\mapsto\omega A$ and leave the operator unchanged.

**The fibre.** If $\mathrm{Hp}_A=\mathrm{Hp}_B$ with $A,B\neq0$, then $\bar A\otimes A=\bar B\otimes B$, so by the fibre theorem of [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html) the pairs are proportional: $B=\lambda A$ and $\bar B=\lambda^{-1}\bar A$. Conjugating the first gives $\bar B=\bar\lambda\bar A$, so $\lambda^{-1}=\bar\lambda$ and $|\lambda|=1$. The fibre is exactly the $\mathrm{U}(1)$ orbit.

**The dimension.** The parameter space is complex four-dimensional, the orbit is one real dimension, and the quotient has real dimension seven. The cone is a real cone over $\mathbb{CP}^{3}$, of real dimension seven.

**The cone is not a space.** The sum of two Hermitian pairs is not a Hermitian pair, and the cone is not closed under multiplication by $i$ except at the zero parameter.

## The Intersections with the One-Sided Families

**The statement.** The cone meets each one-sided family in the same closed ray:
$$
\operatorname{End}_{LR\ast}\cap L(M_2)=\operatorname{End}_{LR\ast}\cap R(M_2)=\{t\,\mathrm I_4:t\ge0\}.
$$

**The proof.** If $\bar A\otimes A=\mathrm I_2\otimes C$ with $A\neq0$, the fibre theorem gives $(A,A^{\dagger})=(\lambda C,\lambda^{-1}\mathrm I_2)$, so $A=\lambda^{-1}\mathrm I_2$ is central and the array is $|\lambda|^{-2}\mathrm I_4$. The scalar is a modulus squared and is nonnegative. The right family is the same computation.

**The ray is not a line.** The negative multiples are not in the cone, because they would need a negative modulus.

**The contrast with the product set.** The full two-sided family meets $L$ in all of $L$ and $R$ in all of $R$, because $L_A=L_AR_{\mathrm I}$. The graph meets the two axes only at the central ray.

## The Spectrum

**The four products.** Let $\lambda_1,\lambda_2$ be the eigenvalues of $A$. The eigenvalues of the array $\mathsf H_A=\bar A\otimes A$ are the four products

$$
\lambda_i\bar\lambda_j,\qquad i,j\in\{1,2\}.
$$

*Proof.* The eigenvalues of a Kronecker product are the products of the eigenvalues, and those of $\bar A$ are $\bar\lambda_i$. The four power sums $\operatorname{tr}\mathsf H_A^{k}$ agree with $\sum(\lambda_i\bar\lambda_j)^{k}$ for $k=1,2,3$ to $8.5\cdot10^{-15}$ relative on sixty random $A$.

**The trace and the determinant.** The trace is $\operatorname{tr}\mathsf H_A=|\lambda_1+\lambda_2|^{2}=|\operatorname{tr}A|^{2}=4|Q_t|^{2}$, and the determinant is $\det\mathsf H_A=|\lambda_1\lambda_2|^{4}=|\det A|^{4}$.

**The reading.** The two diagonal products $|\lambda_i|^{2}$ are nonnegative real, and the two off-diagonal products are conjugate. A central parameter gives four equal eigenvalues $|\lambda|^{2}$ and the scalar operator $|\lambda|^{2}\mathrm I_4$. A singular parameter gives at least two vanishing products. The spectrum is invariant under the central phase, and it depends only on the eigenvalues of $A$.

## The Image and the Kernel

**The rank.** The rank of the array $\bar A\otimes A$ is the square of the rank of $A$:
$$
\operatorname{rank}\mathsf H_A=\operatorname{rank}(A)^{2}.
$$

**The image.** The image of $\mathrm{Hp}_A$ is the space $AM_2A^{\dagger}$. For invertible $A$ it is the whole carrier, of complex dimension four. For $A=uw^{\dagger}$ of rank one it is the line $\mathbb{C}\,uu^{\dagger}$, of complex dimension one.

**The kernel.** For $A=uw^{\dagger}$ of rank one,
$$
\ker\mathrm{Hp}_A=\{X:w^{\dagger}Xw=0\},
$$
a hyperplane of complex dimension three. For invertible $A$ the kernel is $\{0\}$.

**The two kernels.** The kernel of the linear map is a subspace of the carrier; the kernel of the parameter map $A\mapsto\mathrm{Hp}_A$ is the central phase orbit. The two are different objects and neither is the other.

**The group anti-homomorphism.** On $\mathrm{GL}_2(\mathbb{C})$ the map $A\mapsto\mathrm{Hp}_A$ is an anti-homomorphism with kernel the central $\mathrm{U}(1)$, and its image is a group of real dimension seven. The parameter is recovered from the operator up to the phase.

## The Determinant-One Slice

**The slice.** On $\det A=1$ the group is $SL_2(\mathbb{C})$, of real dimension six, and the operator preserves the norm.

**The Lorentz action.** The Hermitian matrices form a real four-dimensional space with the quadratic form $\det X$ of signature $(1,3)$, and for $A\in SL_2(\mathbb{C})$,
$$
\det\bigl(AXA^{\dagger}\bigr)=\det X .
$$
The action is therefore an isometry of the form on the Hermitian space.

**The cover.** The map
$$
SL_2(\mathbb{C})\longrightarrow SO^{+}(1,3),\qquad A\longmapsto\bigl(X\mapsto AXA^{\dagger}\bigr)
$$
is a twofold cover with kernel $\{\pm\mathrm I_2\}$. Both groups have real dimension six, the domain is connected, and the kernel is exactly the two central signs.

**The conformal extension.** A general invertible $A=r\omega U$ with $r>0$, $|\omega|=1$ and $\det U=1$ gives $\mathrm{Hp}_A=r^{2}\mathrm{Hp}_U$: a Lorentz transformation composed with a dilation of ratio $r^{2}$ on the carrier, $r^{4}$ on the norm and $r^{8}$ on the determinant of the array. The image is the conformal group $CO^{+}(1,3)$ of real dimension seven, and the kernel is the central phase.

## Where $n=2$ Differs

**The array.** At $n=2$ the array is $\bar A\otimes A$ of size $4\times4$; at order $n$ it is of size $n^2\times n^2$. The formula and the multiplicativity are the same at every order.

**The dimension of the cone.** The parameter modulo the phase has real dimension $2n^2-1$, which is seven at $n=2$. The cone is a real cone over $\mathbb{CP}^{n^2-1}$.

**The rank.** The rank of the operator is the square of the rank of the parameter at every order, so at $n=2$ it is one or four.

**The cover.** At $n=2$ the norm-one slice is $SL_2(\mathbb{C})$ and the form is the Minkowski form of the Hermitian $2\times2$ matrices. At order $n$ the slice is $SL_n(\mathbb{C})$ and the form is the determinant on the Hermitian $n\times n$ matrices, of signature $(1,n^2-1)$. The twofold cover survives only at $n=2$.

**The sixteen.** The number sixteen is $n^4$ at $n=2$, the real dimension of the sector-preserving space and the number of basis pairs.

## Summary

The two-side Hermitian pair of the display is the congruence $X\mapsto AXA^{\dagger}$, with the array $\bar A\otimes A$. The composition is $\mathrm{Hp}_A\mathrm{Hp}_B=\mathrm{Hp}_{AB}$, the defect is $AX(\mathrm I_2-A^{\dagger}A)YA^{\dagger}$, and the automorphisms are the unitary parameters. The operator rescales by $|\lambda|^{2}$ under a complex rescaling of the parameter, so the parameter is a point of $M_2(\mathbb{C})/\mathrm{U}(1)$.

Both Hermitian sectors are preserved at every parameter, and inside the two-sided family the sector-preserving operators are exactly the real multiples of the Hermitian pairs; the Hermitian pair is the positive half. The family spans the sixteen-dimensional space of sector-preserving maps, with the rank-one Hermitian coefficient matrix $a\bar a^{\mathsf T}$, and the time reflection needs four pairs with one negative coefficient and is not a sum of pairs.

The norm scales by the nonnegative factor $|\det A|^{2}$, the parameter is determined up to the central phase, and the cone has real dimension seven. The eigenvalues of the array are the four products $\lambda_i\bar\lambda_j$, the rank is the square of the rank of the parameter, and the cone meets each one-sided family in the closed ray of nonnegative multiples of the identity. On the determinant-one slice the operator is an isometry of the Minkowski form and the map is the twofold cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$ with kernel $\{\pm\mathrm I_2\}$; on all invertibles the image is $CO^{+}(1,3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Hp}_A(X)=AXA^{\dagger}$ | the two-side Hermitian pair |
| $\mathsf H_A=\bar A\otimes A$ | its array |
| $\mathfrak{H},\mathfrak{K}$ | the Hermitian and skew sectors |
| $c=a\bar a^{\mathsf T}$ | the rank-one Hermitian coefficient matrix |
| $N(X)=\det X$ | the norm, the quadratic form of the display |
| $\operatorname{End}_{LR\ast}$ | the cone of Hermitian pairs |

## Further Reading

- [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html), for the source's multiplicativity, rigidity, span, norm and cover.
- [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html), for the cone in which the pair is a graph.
- [The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-m2c.html), for the other placement.
- [The Geometry of the Two Halves at $n=2$ and the Return of the Two-Sided Operators](the-geometry-of-the-two-halves-at-n-2-and-the-return-of-the-two-sided-operators.html), for the sector geometry in the regular representation.
- [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html), for the rotor action and the cover.
