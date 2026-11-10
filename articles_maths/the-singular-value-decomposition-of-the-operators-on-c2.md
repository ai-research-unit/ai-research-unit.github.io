# __The Singular Value Decomposition of the Operators on $\mathbb{C}^2$__

## Introduction

**The question.** An operator on the duo-complex numbers is a complex-linear map $A:\mathbb{C}^2\to\mathbb{C}^2$. After the choice of the complex basis it is a $2\times2$ complex matrix, and the map is an isomorphism of algebras $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)\cong M_2(\mathbb{C})$. The question of this article is the following. *What is the shortest way to write an operator as a sum of rank-one operators, and what are the weights of the terms?*

**The answer.** Two terms at most, and the weights are the square roots of the eigenvalues of $A^{\dagger}A$:

$$
A=U\Sigma V^{\dagger}=\sigma_1u_1v_1^{\dagger}+\sigma_2u_2v_2^{\dagger},
\qquad
\sigma_1\geq\sigma_2\geq0,
\qquad
Av_i=\sigma_iu_i .
$$

with $U,V\in\mathrm{U}(2)$ and $\Sigma=\operatorname{diag}(\sigma_1,\sigma_2)$. In the language of the algebra, this is the singular value decomposition in $M_2(\mathbb{C})$. Two is the complex dimension of the space, so the bound is the dimension and not a property of the operator. What the theorem says is that two terms always suffice and that the weights and the two orthonormal families can be chosen at once.

**Why the space and not the algebra.** The algebra $M_2(\mathbb{C})$ is also the biquaternion algebra $\mathbb{B}$, but the carrier here is the module $\mathbb{C}^2$ and not the algebra. An operator is a map of the module, its adjoint is taken for the Hermitian form $H$ of the space, and the decomposition is the canonical form of the map. *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra* reads the other object: an endomorphism of the four-dimensional algebra, with four terms and with a multiplication that meets the decomposition. **The same matrix algebra, two different carriers, and the number of terms counts the carrier.**

**The contrast in one line.** The biquaternion endomorphism has four weights because its carrier has complex dimension four. An operator here has two because the carrier has complex dimension two. A reduced biquaternion element, read in its regular representation, has its weights repeated in pairs because its matrix is block diagonal.

**The method.** The article proceeds in two stages, and the order matters. The first stage is the Hilbert-space theory: the Hermitian form, the adjoint, the spectral theorem for the positive operator $A^{\dagger}A$, the rank-one decomposition and its operator form. The second stage reads the result: the rank cases, the three identities, the explicit formula in the four entries, the geometry, the non-uniqueness, the truncation, and the place of the atoms in the two cones.

**The letters.** $A$ and $B$ are operators, $A^{\dagger}$ is the adjoint of $A$, and $\mathrm{I}_2$ is the identity. The unitaries of the decomposition are $U$ and $V$, the scale is $\Sigma$ with coordinate projectors $\Pi_i=e_ie_i^{\dagger}$, the weights are $\sigma_1\geq\sigma_2$, and the left and right singular vectors are $u_i$ and $v_i$. The eigenvalues of $A^{\dagger}A$ are $\lambda_1\geq\lambda_2$, so $\lambda_i=\sigma_i^2$. The Hermitian form is $H$, the norm is $\lVert Q\rVert$, and the two norms of an operator are the Frobenius norm $\langle A\rangle_*^{1/2}$ and the operator norm $\lVert A\rVert_{\mathrm{op}}$. The two numbers of the explicit formula are $T$ and $\Delta$. The two cones are $\mathcal{C}$, the bilinear cone of the matrices $u\phi^{\mathsf T}$, and $\mathcal{C}_{H}$, the Hermitian cone of the matrices $uu^{\dagger}$. The biquaternion element is $\tilde Q$ with matrix $\mathsf M_2(\tilde Q)$ and algebraic norm $N(\tilde Q)$, and the reduced biquaternion is $\breve Q$ with the two complex coordinates $Q_+,Q_-$.

**The order of the article.** The operator and its adjoint come first, with the Hilbert–Schmidt form and the classes of Hermitian, unitary and positive operators (§*The Operator and the Adjoint*). The spectral theorem for $A^{\dagger}A$ is stated and proved, because the article uses it and does not import it (§*The Spectral Theorem for $A^{\dagger}A$*). The decomposition is stated and proved, with its rank-one form, its computation and its operator form (§*The Decomposition*). The weights are examined in their own section: the rank cases, the three identities, the explicit formula, a worked example, the geometry, the non-uniqueness and the truncation (§*The Weights*). The atoms are then placed in the two cones, and the length of an operator is identified with its rank (§*The Two Cones and the Length*). The comparison with the biquaternion and reduced biquaternion decompositions closes the body (§*The Comparison with the Neighbouring Decompositions*).

**Boundaries.** The space, the two scalar structures, the complex structure $J$ and the Hermitian form are *Duo-Complex Numbers*. The algebra of operators, its units, its centre, its trace and its determinant, the conjugate-linear maps and the centraliser of $J$ are *The Endomorphisms of $\mathbb{C}^2$*. The space as the defining module of $M_2(\mathbb{C})$, the three canonical forms and the two cones as objects of the space are *$M_2(\mathbb{C})$ Defining Representation*; the rank-one family read as a semigroup, with its composition law, and the side-by-side comparison of the two cones, are its operators companion. **This article takes nothing from either of them**: the bilinear cone and the Hermitian cone are defined in place as the two sets of rank-one matrices that the decomposition produces, and the length is defined and proved here. The general SVD, the polar decomposition and the Eckart–Young theorem are likewise not imported: the article proves what it uses at size two, and it cites the general theory in §*Further Reading*.

**Conventions.** The space is $V=\mathbb{C}^2$ with the complex basis $e_1,e_2$, and an operator is written $A$ and identified with its matrix in that basis. The Hermitian form is $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$, linear in the first slot and conjugate-linear in the second, with norm $\lVert Q\rVert^2=H(Q,Q)$. The adjoint is defined by $H(AQ_1,Q_2)=H(Q_1,A^{\dagger}Q_2)$. The dagger is the conjugate transpose, the transpose is written ${}^{\mathsf T}$, and the entries of $A$ are

$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
$$

## The Operator and the Adjoint

### The Operator as a Matrix

**Definition.** An **operator** on the duo-complex numbers is a complex-linear map $A:V\to V$. The operators form the algebra $\operatorname{End}_{\mathbb{C}}(V)$ under addition, scalar multiplication and composition, with the identity $\mathrm{I}_2$.

**Proposition (the matrix algebra).** The map sending an operator to its matrix in the basis $e_1,e_2$ is an isomorphism of $\mathbb{C}$-algebras

$$
\operatorname{End}_{\mathbb{C}}(V)\cong M_2(\mathbb{C}),
$$

of complex dimension $4$ and real dimension $8$.

*Proof.* The matrix of $A$ has entries $A_{jk}$ defined by $A(e_k)=\sum_jA_{jk}e_j$. The correspondence between linear maps and matrices is bijective, it preserves the sum and the scalar multiplication entrywise, and the matrix of a composition is the product of the matrices. The dimension is the number of entries.

**The operator and the matrix are the same object, and the basis is the only choice.** A statement about an operator is therefore a statement about a $2\times2$ matrix, and the decomposition below is a canonical form of the matrix. The choice of basis is recorded once and is not mentioned again except where a change of basis matters.

### The Hilbert–Schmidt Form and the Adjoint

**Definition (the form on operators).** The **Hilbert–Schmidt form** on the operator space is

$$
\langle\!\langle A,B\rangle\!\rangle=\operatorname{tr}(B^{\dagger}A)=\sum_{j=1}^{2}H(Ae_j,Be_j),
$$

linear in the first slot and conjugate-linear in the second. The **Frobenius norm** is

$$
\langle A\rangle_*=\langle\!\langle A,A\rangle\!\rangle=\operatorname{tr}(A^{\dagger}A)=\lvert a\rvert^2+\lvert b\rvert^2+\lvert c\rvert^2+\lvert d\rvert^2.
$$

**The operator norm** is the norm of the map,

$$
\lVert A\rVert_{\mathrm{op}}=\sup_{\lVert Q\rVert=1}\lVert AQ\rVert.
$$

**Definition (the adjoint).** The **adjoint** of $A$ is the operator $A^{\dagger}$ defined by

$$
H(AQ_1,Q_2)=H(Q_1,A^{\dagger}Q_2)\qquad\text{for all }Q_1,Q_2\in V.
$$

**Proposition (the adjoint is the conjugate transpose).** In the basis $e_1,e_2$ the matrix of $A^{\dagger}$ is the conjugate transpose of the matrix of $A$, and the operation is involutive and conjugate-linear,

$$
(A^{\dagger})^{\dagger}=A,
\qquad
(\lambda A)^{\dagger}=\overline{\lambda}A^{\dagger},
\qquad
(AB)^{\dagger}=B^{\dagger}A^{\dagger}.
$$

*Proof.* Write $H(Q_1,Q_2)=Q_2^{\dagger}Q_1$ in the basis. Then

$$
H(AQ_1,Q_2)=Q_2^{\dagger}AQ_1=(A^{\dagger}Q_2)^{\dagger}Q_1=H(Q_1,A^{\dagger}Q_2),
$$

which identifies the matrix of $A^{\dagger}$ as the conjugate transpose. The three rules are the corresponding identities of the conjugate transpose.

### The Hermitian, Unitary and Positive Operators

**Definition.** An operator is **Hermitian** when $A^{\dagger}=A$, **unitary** when $A^{\dagger}A=A A^{\dagger}=\mathrm{I}_2$, and **positive semidefinite** when $H(AQ,Q)\geq0$ for every $Q$.

**Proposition (the unitary group).** The unitary operators form the group $\mathrm{U}(2)$ of real dimension $4$, and they are exactly the operators that preserve the Hermitian form,

$$
H(AQ_1,AQ_2)=H(Q_1,Q_2)\qquad\text{for all }Q_1,Q_2 .
$$

*Proof.* If $A^{\dagger}A=\mathrm{I}_2$, then $H(AQ_1,AQ_2)=H(A^{\dagger}AQ_1,Q_2)=H(Q_1,Q_2)$. Conversely, if the form is preserved, then $H((A^{\dagger}A-\mathrm{I}_2)Q_1,Q_2)=0$ for all $Q_1,Q_2$, and the nondegeneracy of $H$ gives $A^{\dagger}A=\mathrm{I}_2$. The four complex entries are constrained by the four real equations of $A^{\dagger}A=\mathrm{I}_2$, and the constraints are independent at the identity.

**Proposition (the positive operator $A^{\dagger}A$).** For every operator $A$, the operator $A^{\dagger}A$ is Hermitian and positive semidefinite, and

$$
H(A^{\dagger}AQ,Q)=\lVert AQ\rVert^2 .
$$

*Proof.* The adjoint of $A^{\dagger}A$ is $A^{\dagger}A$, and $H(A^{\dagger}AQ,Q)=H(AQ,AQ)=\lVert AQ\rVert^2\geq0$.

**The operator $A^{\dagger}A$ is the only positive operator the decomposition needs.** Its eigenvalues are nonnegative, and its eigenvectors are the right singular vectors. The whole content of the SVD is the spectral theorem applied to it.

## The Spectral Theorem for $A^{\dagger}A$

### The Statement

**Theorem (the spectral theorem at size two).** Let $S$ be a Hermitian operator on $V$. There are a unitary operator $W$ and real numbers $\lambda_1\geq\lambda_2$ such that

$$
S=W\Lambda W^{\dagger},
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2).
$$

If $S$ is positive semidefinite, then $\lambda_1\geq\lambda_2\geq0$. The numbers $\lambda_1,\lambda_2$ are the eigenvalues of $S$, counted with multiplicity, and the columns of $W$ are an orthonormal eigenbasis.

### The Proof at Size Two

**The characteristic polynomial.** For

$$
S=\begin{pmatrix}\alpha&\beta\\\overline{\beta}&\delta\end{pmatrix},
\qquad
\alpha,\delta\in\mathbb{R},
$$

the characteristic polynomial is

$$
\chi_S(\lambda)=\lambda^2-(\alpha+\delta)\lambda+(\alpha\delta-\lvert\beta\rvert^2).
$$

Its discriminant is

$$
(\alpha+\delta)^2-4(\alpha\delta-\lvert\beta\rvert^2)=(\alpha-\delta)^2+4\lvert\beta\rvert^2\geq0,
$$

so the two roots are real. Write them $\lambda_1\geq\lambda_2$. Each root is an eigenvalue: at a root $\lambda$ the determinant of $S-\lambda\mathrm{I}_2$ vanishes, so $S-\lambda\mathrm{I}_2$ has a nonzero kernel.

**The eigenbasis.** If $\lambda_1>\lambda_2$, eigenvectors for distinct eigenvalues are orthogonal: from $Sx=\lambda_1x$ and $Sy=\lambda_2y$,

$$
\lambda_1H(x,y)=H(Sx,y)=H(x,Sy)=\lambda_2H(x,y),
$$

so $(\lambda_1-\lambda_2)H(x,y)=0$ and $H(x,y)=0$. Normalising one eigenvector for each eigenvalue gives an orthonormal basis. If $\lambda_1=\lambda_2$, the discriminant vanishes, hence $\alpha=\delta$ and $\beta=0$, so $S=\alpha\mathrm{I}_2$ and every orthonormal basis is an eigenbasis. In both cases the matrix $W$ whose columns are the basis vectors is unitary and $W^{\dagger}SW=\Lambda$, that is $S=W\Lambda W^{\dagger}$.

**The sign.** If $S$ is positive semidefinite and $x$ is a unit eigenvector for $\lambda$, then

$$
\lambda=H(Sx,x)\geq0.
$$

This proves the statement.

### The Square Root

**Definition.** For a positive semidefinite $S=W\operatorname{diag}(\lambda_1,\lambda_2)W^{\dagger}$, the **square root** is

$$
S^{1/2}=W\operatorname{diag}\bigl(\sqrt{\lambda_1},\sqrt{\lambda_2}\bigr)W^{\dagger}.
$$

**Proposition (the square root is positive and unique).** The operator $S^{1/2}$ is Hermitian and positive semidefinite, its square is $S$, and it is the only positive semidefinite operator whose square is $S$.

*Proof.* The operator $S^{1/2}$ is Hermitian because $W$ is unitary and the diagonal entries are real, and it is positive semidefinite because the square roots are nonnegative. Its square is $W\Lambda W^{\dagger}=S$. If $T$ is positive semidefinite and $T^2=S$, then $T$ commutes with $S$, because $TS=T^3=ST$; hence $T$ preserves every eigenspace of $S$. On the eigenspace of $S$ for $\lambda$, the operator $T$ is positive semidefinite and $T^2=\lambda\mathrm{I}$, so $T=\sqrt{\lambda}\mathrm{I}$ there. Hence $T=S^{1/2}$.

**The modulus.** The **modulus** of an operator $A$ is

$$
\lvert A\rvert=(A^{\dagger}A)^{1/2}.
$$

It is positive semidefinite, and $\lvert A\rvert^2=A^{\dagger}A$. The modulus carries the weights of the decomposition, and the unitaries carry the directions.

## The Decomposition

### The Theorem

**Theorem (the singular value decomposition).** For every operator $A$ on $V$ there are unitary operators $U,V\in\mathrm{U}(2)$ and real numbers $\sigma_1\geq\sigma_2\geq0$ such that

$$
A=U\Sigma V^{\dagger},
\qquad
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2).
$$

Equivalently, with the columns $u_1,u_2$ of $U$ and $v_1,v_2$ of $V$,

$$
A=\sigma_1u_1v_1^{\dagger}+\sigma_2u_2v_2^{\dagger},
\qquad
Av_i=\sigma_iu_i .
$$

The numbers $\sigma_1,\sigma_2$ are the **singular values** of $A$, the vectors $u_i$ its **left singular vectors** and the vectors $v_i$ its **right singular vectors**. The pairs are ordered by the decreasing singular values.

### The Proof

**The spectral theorem on $A^{\dagger}A$.** The operator $A^{\dagger}A$ is Hermitian and positive semidefinite, so §*The Spectral Theorem for $A^{\dagger}A$* gives a unitary $V$ and real numbers $\lambda_1\geq\lambda_2\geq0$ with

$$
A^{\dagger}A=V\operatorname{diag}(\lambda_1,\lambda_2)V^{\dagger}.
$$

Put $\sigma_i=\sqrt{\lambda_i}$ and let $v_i=Ve_i$ be the columns of $V$. Then

$$
A^{\dagger}Av_i=\sigma_i^2v_i,
\qquad
H(v_i,v_j)=\delta_{ij}.
$$

**The images are orthogonal and of the right length.** For all $i,j$,

$$
H(Av_i,Av_j)=H(A^{\dagger}Av_i,v_j)=\sigma_i^2H(v_i,v_j)=\sigma_i^2\delta_{ij}.
$$

Hence $\lVert Av_i\rVert=\sigma_i$, and the images of distinct right vectors are orthogonal. For each index with $\sigma_i>0$ define

$$
u_i=\frac{Av_i}{\sigma_i}.
$$

The $u_i$ are orthonormal, because $H(u_i,u_j)=\sigma_i^{-1}\sigma_j^{-1}H(Av_i,Av_j)=\delta_{ij}$. When $\sigma_i=0$, the identity $H(Av_i,Av_i)=0$ and the definiteness of $H$ give $Av_i=0$. Complete the family $u_i$ with $\sigma_i=0$ to an orthonormal basis of $V$, in the order of the indices, and let $U$ be the unitary operator whose columns are the completed family.

**The identity on the basis.** For every $i$,

$$
Av_i=\sigma_iu_i,
$$

by the definition where $\sigma_i>0$ and because both sides vanish where $\sigma_i=0$. Hence $AV=U\Sigma$, that is $A=U\Sigma V^{\dagger}$, and the two displays of the theorem are the same statement.

**The uniqueness of the weights.** The numbers $\lambda_i=\sigma_i^2$ are the eigenvalues of $A^{\dagger}A$, hence are determined by $A$; the ordering then determines the pair $(\sigma_1,\sigma_2)$. The singular values are therefore intrinsic, and the two unitary families are not, as §*The Non-Uniqueness* shows.

### The Rank-One Form

**The sum of two atoms.** The decomposition reads

$$
A=\sigma_1u_1v_1^{\dagger}+\sigma_2u_2v_2^{\dagger}.
$$

Each term is the rank-one operator $Q\mapsto\sigma_i\,(v_i^{\dagger}Q)\,u_i$, with the column on the left and the row on the right. The two terms are orthogonal in the Hilbert–Schmidt form,

$$
\langle\!\langle u_1v_1^{\dagger},u_2v_2^{\dagger}\rangle\!\rangle
=\operatorname{tr}\bigl(v_2u_2^{\dagger}u_1v_1^{\dagger}\bigr)
=(u_2^{\dagger}u_1)(v_1^{\dagger}v_2)=0,
$$

so the decomposition is an orthogonal sum and the Pythagorean identity of §*The Three Identities* follows at once.

**The order of the terms matters only for the weights.** The sum is commutative as a sum of matrices, but the pair $(\sigma_1,\sigma_2)$ is ordered. **The decomposition is an ordered sum of up to two rank-one components weighted by the singular values**, and the order is the decreasing order of the weights.

### The Computation

**Step one.** Form the Hermitian positive semidefinite matrix $A^{\dagger}A$.

**Step two.** Diagonalise it by the spectral theorem,

$$
A^{\dagger}A=V\operatorname{diag}(\lambda_1,\lambda_2)V^{\dagger},
\qquad
\lambda_1\geq\lambda_2\geq0,
\qquad
V\in\mathrm{U}(2).
$$

**Step three.** Take the singular values $\sigma_i=\sqrt{\lambda_i}$ for $i=1,2$.

**Step four.** Read the right singular vectors $v_1,v_2$ as the columns of $V$.

**Step five.** For each positive $\sigma_i$, define $u_i=Av_i/\sigma_i$. These are orthonormal left singular vectors. If a weight vanishes, complete the family of the $u_i$ with positive weight to a unitary basis of $V$.

**Step six.** Assemble $U$ from the $u_i$ and $V$ from the $v_i$. Then $A=U\Sigma V^{\dagger}$ with $\Sigma=\operatorname{diag}(\sigma_1,\sigma_2)$.

**The computation is finite and exact at this size.** The only non-elementary step is the diagonalisation of a $2\times2$ Hermitian matrix, which is the quadratic formula of §*The Proof at Size Two*. No iteration and no approximation is involved.

### The Operator Form

**The three factors.** The decomposition is the product of three operators:

$$
A=U\,\Sigma\,V^{\dagger},
$$

where $U$ and $V$ are unitary and $\Sigma$ is Hermitian, positive semidefinite and diagonal in the basis $e_1,e_2$. Read as a map of the sphere, $V^{\dagger}$ turns the source, $\Sigma$ stretches the two axes by $\sigma_1$ and $\sigma_2$, and $U$ turns the result into place.

**The spectral form of the scale.** Let $\Pi_i=e_ie_i^{\dagger}$ be the coordinate projectors. Then

$$
\Sigma=\sigma_1\Pi_1+\sigma_2\Pi_2,
\qquad
\Pi_i\Pi_j=\delta_{ij}\Pi_i,
\qquad
\Pi_1+\Pi_2=\mathrm{I}_2,
$$

and the decomposition reads

$$
A=\sigma_1\,U\Pi_1V^{\dagger}+\sigma_2\,U\Pi_2V^{\dagger}.
$$

The operators $U\Pi_iV^{\dagger}=u_iv_i^{\dagger}$ are the atoms of §*The Rank-One Form*, and the scale is the modulus carried into the basis of the right singular vectors.

**The modulus and the unitaries.** Multiplying the decomposition by its adjoint,

$$
A^{\dagger}A=V\Sigma^2V^{\dagger},
$$

because $U^{\dagger}U=\mathrm{I}_2$. Hence $\Sigma=V^{\dagger}\lvert A\rvert V$, and the weights are the diagonal entries of the modulus in the basis of the right singular vectors. **The modulus is intrinsic; the two unitaries are the choice of the two orthonormal bases.**

## The Weights

### The Rank Cases

**The number of positive weights is the rank.** The image of $A$ is spanned by the vectors $u_i$ with $\sigma_i>0$, and the right vectors form a basis, so the image has dimension equal to the number of positive weights. The three cases are the following.

| $\operatorname{rank}A$ | the weights | the decomposition |
|---|---|---|
| $2$ | $\sigma_1\geq\sigma_2>0$ | two terms, $A$ invertible |
| $1$ | $\sigma_1>0$, $\sigma_2=0$ | one term, $A=\sigma_1u_1v_1^{\dagger}$ |
| $0$ | $\sigma_1=\sigma_2=0$ | $A=0$ |

**The generic operator has two distinct positive weights.** A coincidence $\sigma_1=\sigma_2$ means that the two eigenvalues of $A^{\dagger}A$ coincide, which is the single real equation $\sigma_1^2=\sigma_2^2$ on the eight real parameters of the entries; it is a closed set with empty interior, because the equation fails at the diagonal matrix $\operatorname{diag}(2,1)$. The operators with a repeated positive weight are exactly the nonzero complex multiples of a unitary operator, as §*The Non-Uniqueness* shows.

### The Three Identities

**The product is the determinant.** Multiplying the two weights,

$$
\sigma_1\sigma_2=\sqrt{\det(A^{\dagger}A)}=\sqrt{\lvert\det A\rvert^2}=\lvert\det A\rvert .
$$

The determinant of $A^{\dagger}A$ is $\overline{\det A}\det A$, because $\det A^{\dagger}=\overline{\det A}$.

**The sum of squares is the Frobenius norm.** Summing the squares,

$$
\sigma_1^2+\sigma_2^2=\operatorname{tr}(A^{\dagger}A)=\langle A\rangle_*=T,
$$

with $T=\lvert a\rvert^2+\lvert b\rvert^2+\lvert c\rvert^2+\lvert d\rvert^2$. The identity is the Pythagorean theorem for the orthogonal decomposition of §*The Rank-One Form*, and it says that a truncation which discards the second term loses exactly $\sigma_2^2$ of the Frobenius norm.

**The largest weight is the operator norm.** For a unit vector $Q=\alpha v_1+\beta v_2$,

$$
\lVert AQ\rVert^2=\sigma_1^2\lvert\alpha\rvert^2+\sigma_2^2\lvert\beta\rvert^2\leq\sigma_1^2,
$$

with equality at $Q=v_1$. Hence

$$
\lVert A\rVert_{\mathrm{op}}=\sigma_1 .
$$

When $A$ is invertible, the smallest weight is the reciprocal of the operator norm of $A^{-1}$, because the singular values of $A^{-1}$ are $\sigma_2^{-1}\geq\sigma_1^{-1}$.

**The three identities read together.** The two weights determine the modulus of the determinant, the Frobenius norm and the operator norm, and they are determined by them: the pair $(\sigma_1,\sigma_2)$ is the nonnegative solution with $\sigma_1\geq\sigma_2$ of the two equations $\sigma_1\sigma_2=\lvert\det A\rvert$ and $\sigma_1^2+\sigma_2^2=T$. **The two weights are exactly what the size and the volume change leave free.**

### The Explicit Formula

**The formula.** Let

$$
T=\lvert a\rvert^2+\lvert b\rvert^2+\lvert c\rvert^2+\lvert d\rvert^2,
\qquad
\Delta=\lvert\det A\rvert^2=\lvert ad-bc\rvert^2 .
$$

Then

$$
\sigma_{1,2}=\sqrt{\frac{T\pm\sqrt{T^2-4\Delta}}{2}},
$$

with the plus sign for $\sigma_1$ and the minus sign for $\sigma_2$.

*Proof.* The eigenvalues of $A^{\dagger}A$ are the roots of $\lambda^2-T\lambda+\Delta=0$, because the trace of $A^{\dagger}A$ is $T$ and its determinant is $\Delta$. The roots are $(T\pm\sqrt{T^2-4\Delta})/2$, and the singular values are their square roots. The discriminant is nonnegative, since it equals $(\sigma_1^2-\sigma_2^2)^2$.

**The formula is the quadratic formula and nothing else.** The numbers $T$ and $\Delta$ are the elementary symmetric functions of the squares of the weights, $T=\sigma_1^2+\sigma_2^2$ and $\Delta=\sigma_1^2\sigma_2^2$, and the four entries enter only through them. **The singular values of a $2\times2$ matrix are therefore functions of the two nonnegative numbers $T$ and $\Delta$**, and not of the eight real parameters separately.

### A Worked Example

**The operator.** Take the real matrix

$$
A=\begin{pmatrix}3&0\\4&5\end{pmatrix}.
$$

**The two invariants.** $T=9+0+16+25=50$ and $\Delta=\lvert15\rvert^2=225$. Hence

$$
\sigma_{1,2}=\sqrt{\frac{50\pm\sqrt{2500-900}}{2}}
=\sqrt{\frac{50\pm40}{2}},
$$

that is $\sigma_1=\sqrt{45}=3\sqrt5$ and $\sigma_2=\sqrt5$.

**The right vectors.** The matrix $A^{\mathsf T}A=\begin{pmatrix}25&20\\20&25\end{pmatrix}$ has the eigenvectors $(1,1)$ and $(1,-1)$, normalised to

$$
v_1=\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},
\qquad
v_2=\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

**The left vectors.** $Av_1=(3,9)/\sqrt2$, so $u_1=Av_1/\sigma_1=(1,3)/\sqrt{10}$; and $Av_2=(3,-1)/\sqrt2$, so $u_2=Av_2/\sigma_2=(3,-1)/\sqrt{10}$. The two are orthonormal.

**The decomposition.**

$$
A=3\sqrt5\,u_1v_1^{\mathsf T}+\sqrt5\,u_2v_2^{\mathsf T}.
$$

The two identities hold: $\sigma_1\sigma_2=15=\lvert\det A\rvert$ and $\sigma_1^2+\sigma_2^2=50=\langle A\rangle_*$. The daggers are transposes here, because the matrix is real and the two families are real.

### The Geometric Reading

**The ellipsoid.** The space is $\mathbb{R}^4$ as a real vector space, and the realification of $A$ has the four singular values $\sigma_1,\sigma_1,\sigma_2,\sigma_2$, because $A(iv_i)=iA(v_i)$. The image of the unit sphere of $V$ is therefore the ellipsoid of $\mathbb{R}^4$ whose principal semi-axes are $\sigma_1$ and $\sigma_2$, each counted twice, along the directions $u_1,iu_1$ and $u_2,iu_2$.

**The ellipse in the plane.** In the real plane spanned by $v_1,v_2$, the unit circle is carried onto the ellipse of semi-axes $\sigma_1$ and $\sigma_2$ and area $\pi\sigma_1\sigma_2=\pi\lvert\det A\rvert$. The right vectors are the directions of the circle that are carried onto the axes, and the left vectors are the directions of the axes in the image. When the rank is one the ellipse degenerates to a segment of length $2\sigma_1$, and when the rank is zero it degenerates to the origin.

**The two unitary factors.** The decomposition is a unitary motion of the source, a scaling of the two axes and a unitary motion of the target, in that order. The weights are the only part of the decomposition that is not a symmetry of the Hermitian form, and the two unitaries are the two symmetries.

### The Non-Uniqueness

**Where the freedom is.** The weights are determined by $A$. The two families are not, and the freedom has three regimes.

**Distinct positive weights.** If $\sigma_1>\sigma_2>0$, the eigenvalues of $A^{\dagger}A$ are distinct, so each eigenspace is a line and $v_i$ is determined up to a phase. The left vector $u_i=Av_i/\sigma_i$ inherits the same phase, so the freedom is

$$
u_i\mapsto e^{i\theta_i}u_i,
\qquad
v_i\mapsto e^{i\theta_i}v_i,
\qquad
i=1,2,
$$

with two independent phases. In matrix form the freedom is $U\mapsto UP$ and $V\mapsto VP$ with $P=\operatorname{diag}(e^{i\theta_1},e^{i\theta_2})$, the same phase matrix on both sides. The phases do not mix the two terms.

**Coincident positive weights.** If $\sigma_1=\sigma_2=\sigma>0$, then $A^{\dagger}A=\sigma^2\mathrm{I}_2$ and every orthonormal basis is an eigenbasis. The freedom is $U\mapsto UW$ and $V\mapsto VW$ with $W\in\mathrm{U}(2)$, the same unitary on both sides, and $A=\sigma UV^{\dagger}$ is $\sigma$ times a unitary operator. The two terms are no longer distinguished, and the decomposition is unique only up to the common unitary mixing.

**A vanishing weight.** If $\sigma_1>0$ and $\sigma_2=0$, the vector $v_1$ is determined up to a phase, the vector $u_1$ follows, and $v_2$ is any unit vector in the kernel of $A$, that is any unit vector orthogonal to $v_1$. The vector $u_2$ is any unit vector orthogonal to $u_1$, and its phase is independent of the phase of $v_2$ because the second term vanishes. The completion is therefore a genuine choice and not a symmetry of the operator.

**The invariant summary.** What the decomposition determines intrinsically is the unordered pair of weights, and the two lines of the right and left vectors when the weights are distinct and positive. The ordering, the phases and the completion of the zero-weight directions are the three choices.

### The Truncation

**The nearest operator of smaller rank.** Let

$$
A_1=\sigma_1u_1v_1^{\dagger}
$$

be the first term. Then $A_1$ has rank at most one, and

$$
\langle A-A_1\rangle_*^{1/2}=\sigma_2,
\qquad
\lVert A-A_1\rVert_{\mathrm{op}}=\sigma_2 .
$$

**Theorem (the best rank-one approximation).** For every operator $B$ of rank at most one,

$$
\langle A-B\rangle_*^{1/2}\geq\sigma_2,
\qquad
\lVert A-B\rVert_{\mathrm{op}}\geq\sigma_2 .
$$

The first term $A_1$ attains both bounds.

*Proof.* If $B=0$ the error is $\langle A\rangle_*^{1/2}\geq\sigma_2$. Otherwise $B$ has a kernel, which is a line. Choose a unit vector $w$ in the kernel and write $w=\alpha v_1+\beta v_2$. Then

$$
\lVert(A-B)w\rVert=\lVert Aw\rVert=\sqrt{\sigma_1^2\lvert\alpha\rvert^2+\sigma_2^2\lvert\beta\rvert^2}\geq\sigma_2,
$$

so the operator norm of the difference is at least $\sigma_2$, and the Frobenius norm is at least the operator norm. The first term attains the bound, because the difference is the second term and $\langle\sigma_2u_2v_2^{\dagger}\rangle_*^{1/2}=\sigma_2$.

**Uniqueness when the two weights differ.** Suppose $\sigma_1>\sigma_2$ and a competitor $B$ attains the bound. If $B$ were zero the error would be $\langle A\rangle_*^{1/2}>\sigma_2$, so $B$ is nonzero, and its kernel contains a unit vector $w$. The bound gives

$$
\sigma_2=\lVert A-B\rVert_{\mathrm{op}}\geq\lVert(A-B)w\rVert=\lVert Aw\rVert\geq\sigma_2,
$$

so equality holds throughout, and $\lVert Aw\rVert=\sigma_2$ with $\lVert w\rVert=1$ forces $w$ to be a unit multiple of $v_2$, because $\sigma_1>\sigma_2$. The kernel of $B$ is therefore the line of $v_2$, and $B=u'v_1^{\dagger}$ for some vector $u'$. Then

$$
\langle A-B\rangle_*=\lVert\sigma_1u_1-u'\rVert^2+\sigma_2^2,
$$

because $v_1$ and $v_2$ are orthonormal. Equality forces $u'=\sigma_1u_1$, that is $B=A_1$. **A repeated positive weight is the only case in which the best approximation of rank at most one is not unique.**

**The truncation is the spectral truncation.** The best approximation by an operator of rank at most one keeps the largest weight and discards the other. **This is the Eckart–Young theorem at size two**, and the error is exactly the discarded weight.

## The Two Cones and the Length

### The Atoms Are Points of the Bilinear Cone

**The atom.** The rank-one operator $u_iv_i^{\dagger}$ is the matrix $u_i\phi_i^{\mathsf T}$ with $\phi_i=\overline{v_i}$. The pairing $\phi^{\mathsf T}u$ carries no conjugation, so the row $\phi_i^{\mathsf T}$ is the functional $Q\mapsto v_i^{\dagger}Q$. The atom is therefore a point of the **bilinear cone**

$$
\mathcal{C}=\{u\phi^{\mathsf T}:u\in V,\ \phi\in V^{*}\},
$$

defined here as a set and nothing more. The pair *$M_2(\mathbb{C})$ Defining Representation* and its operators companion study the same cone as a semigroup and give it its composition law; the present article uses the set and its nonnegative span only. The decomposition says that every operator is a nonnegative linear combination of at most two points of that cone,

$$
A=\sigma_1u_1v_1^{\dagger}+\sigma_2u_2v_2^{\dagger},
\qquad
\sigma_i\geq0 .
$$

**The cone generates the algebra.** The cone alone is the set of rank at most one matrices. Its nonnegative span is the whole algebra, because every matrix is a sum of two points of the cone, and the SVD gives the sum with orthogonal terms and with the weights as coefficients. **The weights are the coefficients of the operator in the cone, and the rank is the number of coefficients that are needed.**

### The Hermitian Case

**The Hermitian operator.** If $A=A^{\dagger}$, the spectral theorem already writes $A=W\Lambda W^{\dagger}$ with $\Lambda=\operatorname{diag}(\lambda_1,\lambda_2)$ real. Take the right singular vectors to be the eigenvectors, $V=W$, and let $\Sigma=\operatorname{diag}(\lvert\lambda_1\rvert,\lvert\lambda_2\rvert)$ and $S=\operatorname{diag}(\operatorname{sgn}\lambda_1,\operatorname{sgn}\lambda_2)$, with the convention $\operatorname{sgn}0=1$. Then $S$ is unitary and

$$
A=(WS)\,\Sigma\,W^{\dagger},
$$

because $S\Sigma=\Lambda$. Hence the singular values are the absolute values of the eigenvalues, the left vectors are $u_i=\operatorname{sgn}(\lambda_i)w_i$ for the nonzero weights, and the decomposition is the spectral decomposition with the signs of the eigenvalues absorbed into the left unitary.

**The atoms are Hermitian.** With $V=W$ the atom of the index $i$ is

$$
\sigma_iu_iw_i^{\dagger}=\lvert\lambda_i\rvert\operatorname{sgn}(\lambda_i)\,w_iw_i^{\dagger}=\lambda_iw_iw_i^{\dagger},
$$

a point of the **Hermitian cone** $\mathcal{C}_{H}=\{uu^{\dagger}\}$. **For a Hermitian operator the two cones meet**: the general decomposition uses the bilinear cone, and the Hermitian operator uses the Hermitian cone, and the two agree on the spectral decomposition.

**The identity as two atoms.** For any orthonormal basis $u_1,u_2$,

$$
\mathrm{I}_2=u_1u_1^{\dagger}+u_2u_2^{\dagger}.
$$

The identity is not a point of the bilinear cone, because its rank is two, but it is the sum of two points of the Hermitian cone. **This is the length two of the identity in *$M_2(\mathbb{C})$ Defining Representation : Operators*, read as the SVD of the identity**: $\sigma_1=\sigma_2=1$ and every orthonormal basis is a pair of singular vectors.

### The Length is the Rank

**Definition.** The **length** of an operator is the least number of rank-one operators whose sum is the operator.

**Theorem (the length is the rank).** For every operator $A$ on $V$, the length is $\operatorname{rank}A$.

*Proof.* The SVD writes $A$ as a sum of $\operatorname{rank}A$ rank-one terms, so the length is at most the rank. Conversely, a sum of $r$ rank-one operators has image contained in the sum of their images, of dimension at most $r$, so the rank is at most $r$. Hence the length is at least the rank.

**The SVD computes the length.** The decomposition is not merely one sum of rank-one terms; it is a sum with the least possible number of terms, and the number is the rank. **The weights and the rank are the two invariants that the decomposition exhibits at once**: the rank is the number of nonzero weights, and the weights are the sizes of the terms.

## The Comparison with the Neighbouring Decompositions

### The Biquaternion Endomorphisms

**Four terms against two.** An endomorphism of the biquaternion algebra is a complex-linear map $F:\mathbb{B}\to\mathbb{B}$, and $\mathbb{B}$ has complex dimension four. The SVD of *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra* writes it as

$$
F=\sum_{k=1}^{4}\rho_k\,\mathcal{P}_{\tilde U_k,\tilde V_k},
\qquad
\rho_1\geq\rho_2\geq\rho_3\geq\rho_4\geq0,
$$

with four orthonormal families and the weights the square roots of the eigenvalues of $F^{*}F$. The elementary endomorphism is $\mathcal P_{\tilde U,\tilde V}(\tilde X)=\tilde U\langle\tilde X,\tilde V\rangle_{*}$, that is $\tilde U\tilde V^{\dagger}$ applied to $\tilde X$ when the two vectors are read as columns, so the atom there is the atom here. **The number four is the complex dimension of the carrier, and the two terms of this article are the same theorem at dimension two.** The mechanism is identical: the spectral theorem on the positive operator, the images of the right vectors, and the completion of the vanishing directions.

**The matrix size.** The endomorphisms of $\mathbb{B}$ form $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, of complex dimension sixteen, so the SVD there is the SVD of a $4\times4$ matrix. The SVD here is the SVD of a $2\times2$ matrix. **The two articles are the two ends of the same ladder, and the ladder is indexed by the dimension of the carrier.**

### The Biquaternion Element

**The two weights of an element.** The biquaternion SVD also computes the weights of a left multiplier $L_{\tilde Q}$ and finds the four weights

$$
\bigl(\rho_1(\tilde Q),\rho_1(\tilde Q),\rho_2(\tilde Q),\rho_2(\tilde Q)\bigr),
$$

each of the two weights of the element repeated twice. The pair is given by

$$
\rho_{1,2}(\tilde Q)=\sqrt{S\pm\sqrt{S^2-\lvert N(\tilde Q)\rvert^2}},
\qquad
S=\langle\tilde Q,\tilde Q\rangle_{*} .
$$

**The pair is the pair of singular values of the $2\times2$ matrix of the element.** In the matrix model of the biquaternion algebra the element $\tilde Q$ is a $2\times2$ complex matrix $\mathsf M_2(\tilde Q)$ with

$$
\det \mathsf M_2(\tilde Q)=N(\tilde Q),
\qquad
\langle \mathsf M_2(\tilde Q)\rangle_*=2\langle\tilde Q,\tilde Q\rangle_{*} .
$$

The explicit formula of §*The Explicit Formula* applied to $\mathsf M_2(\tilde Q)$ gives, with $T=2S$ and $\Delta=\lvert N(\tilde Q)\rvert^2$,

$$
\sigma_{1,2}=\sqrt{\frac{2S\pm\sqrt{4S^2-4\lvert N(\tilde Q)\rvert^2}}{2}}
=\sqrt{S\pm\sqrt{S^2-\lvert N(\tilde Q)\rvert^2}},
$$

which is exactly the pair $\rho_1(\tilde Q),\rho_2(\tilde Q)$. **The two weights of a biquaternion element in the biquaternion SVD are the two singular values of its $2\times2$ matrix in this article**, and the doubling of the pair in the four weights of $L_{\tilde Q}$ is the doubling of the matrix block in the regular representation.

**The lesson.** A weight of an element and a singular value of an operator are the same number read in two carriers. The biquaternion article reads the element through the left multiplication on the four-dimensional algebra; this article reads the same matrix as an operator on the two-dimensional module. **The singular values are intrinsic to the matrix, and the carrier decides how many times they are counted.**

### The Reduced Biquaternion Element

**The block diagonal matrix.** A reduced biquaternion $\breve Q$ is a pair of complex numbers $(Q_+,Q_-)$ in the idempotent basis, and its real regular representation $L_{\breve Q}$ is carried by the fixed matrix $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, read blockwise, to the block diagonal matrix $\operatorname{diag}(\mathsf b(Q_+),\mathsf b(Q_-))$, where $\mathsf b$ is the real $2\times2$ block of the multiplication by a complex number. The matrix $P$ is orthogonal up to the factor $\sqrt2$, because $P^{\mathsf T}P=2\,\mathrm{I}_2$, so the conjugation preserves the singular values. The singular values of the regular representation are therefore

$$
\lvert Q_+\rvert,\ \lvert Q_+\rvert,\ \lvert Q_-\rvert,\ \lvert Q_-\rvert,
$$

each repeated twice, as the regular representation of a complex scalar repeats its modulus twice. **The repetition is the signature of the block diagonal form, and it is not the repetition of the biquaternion element**, whose two weights are distinct in general. The duo-complex operator is a single $2\times2$ complex block and has no repetition.

### The Polar Decomposition

**The corollary.** Write $A=U\Sigma V^{\dagger}$ and put

$$
P=V\Sigma V^{\dagger}=\lvert A\rvert,
\qquad
W=UV^{\dagger}.
$$

Then $W$ is unitary, $P$ is positive semidefinite, and

$$
A=WP .
$$

This is the **polar decomposition** of $A$. The SVD is finer than the polar decomposition: the polar decomposition separates the modulus from the unitary part, and the SVD diagonalises the modulus in an orthonormal basis. **The polar decomposition is the SVD with the spectral decomposition of the modulus left undone.**

**The singular case.** If $A$ is invertible, $P$ is invertible and $W$ is unique. If $A$ is singular, $W$ is determined on the range of $P$ and is arbitrary on the kernel, which is the freedom of the vanishing weight in §*The Non-Uniqueness*.

### What the Product Shares

**The weights are not multiplicative.** The singular values of a product are not, in general, the products of the singular values. The largest weight is only submultiplicative, and the second weight has no product rule: the two weights of $AB$ are the square roots of the eigenvalues of $B^{\dagger}A^{\dagger}AB$, which mixes the two factors and is not the product of the two positive operators.

**The determinant is multiplicative.** The product of the two weights is, because the determinant is:

$$
\sigma_1(AB)\sigma_2(AB)=\lvert\det(AB)\rvert=\lvert\det A\rvert\,\lvert\det B\rvert=\sigma_1(A)\sigma_2(A)\sigma_1(B)\sigma_2(B).
$$

**The operator norm is submultiplicative.** For every $Q$,

$$
\lVert ABQ\rVert\leq\sigma_1(A)\lVert BQ\rVert\leq\sigma_1(A)\sigma_1(B)\lVert Q\rVert,
$$

so

$$
\sigma_1(AB)\leq\sigma_1(A)\sigma_1(B).
$$

**The algebra enters the decomposition twice.** Through the determinant, which is multiplicative and which fixes the product of the two weights, and through the operator norm, which is submultiplicative and which is the largest weight. The product of two operators does not decompose term by term, and the unitaries of a product are not the products of the unitaries. **The decomposition is a canonical form of the operator as a linear map, not a decomposition of the algebra.**

## Summary

Every operator $A$ on $\mathbb{C}^2$ has a singular value decomposition

$$
A=U\Sigma V^{\dagger}=\sigma_1u_1v_1^{\dagger}+\sigma_2u_2v_2^{\dagger},
\qquad
\sigma_1\geq\sigma_2\geq0,
\qquad
U,V\in\mathrm{U}(2),
$$

with $\Sigma=\operatorname{diag}(\sigma_1,\sigma_2)$ and $Av_i=\sigma_iu_i$. The weights are the square roots of the eigenvalues of $A^{\dagger}A$, the right vectors are an orthonormal eigenbasis of $A^{\dagger}A$, and the left vectors are the normalised images of the right ones, completed by an arbitrary orthonormal basis where a weight vanishes. The proof is the spectral theorem for the Hermitian positive semidefinite operator $A^{\dagger}A$ at size two, proved here and not quoted.

The three identities are $\sigma_1\sigma_2=\lvert\det A\rvert$, $\sigma_1^2+\sigma_2^2=\langle A\rangle_*=T$ and $\sigma_1=\lVert A\rVert_{\mathrm{op}}$; the explicit formula is

$$
\sigma_{1,2}=\sqrt{\frac{T\pm\sqrt{T^2-4\Delta}}{2}},
\qquad
T=\lvert a\rvert^2+\lvert b\rvert^2+\lvert c\rvert^2+\lvert d\rvert^2,
\qquad
\Delta=\lvert\det A\rvert^2,
$$

with the plus sign for $\sigma_1$ and the minus sign for $\sigma_2$. The rank is the number of positive weights, with the cases $2$, $1$ and $0$; the image of the unit sphere is the ellipsoid of $\mathbb{R}^4$ with semi-axes $\sigma_1,\sigma_1,\sigma_2,\sigma_2$, and the unit circle of the plane of $v_1,v_2$ is carried onto the ellipse of semi-axes $\sigma_1,\sigma_2$ and area $\pi\lvert\det A\rvert$; and the best approximation of rank at most one is the first term, with error $\sigma_2$ in both the Frobenius and the operator norm.

The freedom of the decomposition is a phase per term when the weights are distinct and positive, a common unitary mixing of the two terms when they coincide, and an arbitrary completion of the left and right vectors of a vanishing weight. The atoms are points of the bilinear cone of *$M_2(\mathbb{C})$ Defining Representation : Operators*, the Hermitian operator uses the Hermitian cone, the identity is the sum of two Hermitian atoms, and the length of an operator is its rank. The comparison with the biquaternion category is exact: the four weights of a biquaternion endomorphism are the four singular values of a $4\times4$ matrix, the pair of weights of a biquaternion element is the pair of singular values of its $2\times2$ matrix, and the repetition in the reduced biquaternion case is the block diagonal form of its regular representation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\mathbb{C}^2$ | the carrier, of complex dimension $2$ |
| $A$, $B$ | an operator and a competing operator of the truncation |
| $A^{\dagger}$ | the adjoint, the conjugate transpose |
| $\mathrm{I}_2$ | the identity operator |
| $H(Q_1,Q_2)$ | the Hermitian form, linear in the first slot |
| $\lVert Q\rVert$ | the norm of a vector |
| $\langle\!\langle A,B\rangle\!\rangle$ | the Hilbert–Schmidt form, $\operatorname{tr}(B^{\dagger}A)$ |
| $\langle A\rangle_*^{1/2}$, $\lVert A\rVert_{\mathrm{op}}$ | the Frobenius norm and the operator norm |
| $U$, $V$ | the two unitary operators of the decomposition |
| $\Sigma=\operatorname{diag}(\sigma_1,\sigma_2)$ | the scale, Hermitian and positive semidefinite |
| $\Pi_i=e_ie_i^{\dagger}$ | the coordinate projectors of the scale |
| $\sigma_1\geq\sigma_2$ | the singular values, the weights of the decomposition |
| $\lambda_1\geq\lambda_2$ | the eigenvalues of $A^{\dagger}A$, the squares of the weights |
| $u_i$, $v_i$ | the left and the right singular vectors |
| $\lvert A\rvert=(A^{\dagger}A)^{1/2}$ | the modulus of $A$ |
| $T=\langle A\rangle_*$ | the sum of the squared moduli of the four entries |
| $\Delta=\lvert\det A\rvert^2$ | the squared modulus of the determinant |
| $\mathcal{C}$ | the bilinear cone, the matrices $u\phi^{\mathsf T}$ |
| $\mathcal{C}_{H}$ | the Hermitian cone, the matrices $uu^{\dagger}$ |
| $\operatorname{rank}A$ | the number of positive singular values, the length |
| $\mathsf M_2(\tilde Q)$, $N(\tilde Q)$ | the $2\times2$ matrix of a biquaternion element and its algebraic norm |
| $\breve Q=(Q_+,Q_-)$ | a reduced biquaternion and its two complex coordinates |

## Further Reading

- [Duo-Complex Numbers](duo-complex-numbers.html), for the space, the two scalar structures, the complex structure $J$ and the Hermitian form $H$.
- [The Endomorphisms of $\mathbb{C}^2$](the-endomorphisms-of-c2.html), for the algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)\cong M_2(\mathbb{C})$, its units, its trace and determinant, and the centraliser of $J$.
- [$M_2(\mathbb{C})$ Defining Representation](m2c-defining-representation.html), for the space as the defining module, the three canonical forms and the two cones as point sets.
- [$M_2(\mathbb{C})$ Defining Representation : Operators](m2c-defining-representation-operators.html), for the cone of rank-one operators, its composition law and the length that this article computes.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-c2.html), for the Gram matrices and the real pictures of $H$, $B$ and $\omega$.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-c2.html), for $\mathrm{U}(2)$, $\mathrm{SU}(2)$ and the groups defined by the three forms.
- [The Tensor Square of $\mathbb{C}^2$](the-tensor-square-of-c2.html), for $\mathbb{C}^2\otimes\mathbb{C}^2$ and its relation to the endomorphism algebra.
- [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra.html), for the four-term decomposition on the four-dimensional carrier and for the weights of a biquaternion element.
- [Comparison of the Polar Decomposition](comparison-of-the-polar-decomposition.html), for the polar decomposition in the neighbouring categories.
- [The Polar Decomposition of an Operator of the Form](the-polar-decomposition-of-an-operator-of-the-form.html), for the modulus and the unitary factor in a general setting.
- G. H. Golub and C. F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013), for the general singular value decomposition, the computation and the Eckart–Young theorem.
